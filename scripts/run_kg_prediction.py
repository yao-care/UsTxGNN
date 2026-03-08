#!/usr/bin/env python3
"""執行知識圖譜方法預測

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/repurposing_candidates.csv
"""

import re
from pathlib import Path
from typing import Dict, Optional, Set

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_drugbank_vocab(base_dir: Path) -> pd.DataFrame:
    """載入 DrugBank 詞彙表"""
    return pd.read_csv(base_dir / "data" / "external" / "drugbank_vocab.csv")


def load_drug_disease_relations(base_dir: Path) -> pd.DataFrame:
    """載入藥物-疾病關係"""
    return pd.read_csv(base_dir / "data" / "external" / "drug_disease_relations.csv")


def build_drugbank_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立藥物名稱索引"""
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]
        index[name_upper] = drugbank_id

        # 移除鹽類後綴
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " MALEATE", " ACETATE", " CITRATE",
            " PHOSPHATE", " BROMIDE", " CHLORIDE", " TARTRATE",
            " FUMARATE", " SUCCINATE", " MESYLATE", " BESYLATE",
        ]
        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    return index


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 適應症映射"""
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def normalize_ingredient(ingredient: str) -> str:
    """標準化成分名稱"""
    if not ingredient:
        return ""

    # 轉大寫
    name = ingredient.upper().strip()

    # 移除括號內容
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # 移除鹽類後綴
    salt_patterns = [
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+MALEATE$",
        r"\s+ACETATE$", r"\s+CITRATE$", r"\s+PHOSPHATE$",
    ]
    for pattern in salt_patterns:
        name = re.sub(pattern, "", name)

    return name.strip()


def map_ingredient_to_drugbank(
    ingredient: str,
    drugbank_index: Dict[str, str],
) -> Optional[str]:
    """映射成分到 DrugBank ID"""
    if not ingredient:
        return None

    name = normalize_ingredient(ingredient)

    # 完全匹配
    if name in drugbank_index:
        return drugbank_index[name]

    # 部分匹配（成分可能包含多個藥物）
    for db_name, db_id in drugbank_index.items():
        if db_name in name or name in db_name:
            return db_id

    return None


def main():
    print("=" * 60)
    print("執行知識圖譜方法預測 - US FDA")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. 載入藥品資料
    print("1. 載入藥品資料...")
    fda_path = base_dir / "data" / "raw" / "us_fda_drugs.json"
    fda_df = pd.read_json(fda_path)
    print(f"   總藥品數: {len(fda_df)}")

    # 過濾有成分的藥品
    fda_df = fda_df[fda_df["ActiveIngredient"].notna() & (fda_df["ActiveIngredient"] != "")]
    print(f"   有成分資料: {len(fda_df)}")

    # 2. 載入 DrugBank 詞彙表
    print()
    print("2. 載入 DrugBank 詞彙表...")
    drugbank_df = load_drugbank_vocab(base_dir)
    drugbank_index = build_drugbank_index(drugbank_df)
    print(f"   DrugBank 藥物數: {len(drugbank_df)}")

    # 3. DrugBank 映射
    print()
    print("3. 執行 DrugBank 映射...")

    mapping_results = []
    for _, row in fda_df.iterrows():
        ingredient = row["ActiveIngredient"]
        drugbank_id = map_ingredient_to_drugbank(ingredient, drugbank_index)

        mapping_results.append({
            "ProductNDC": row.get("ProductNDC", ""),
            "DrugName": row.get("DrugName", ""),
            "ActiveIngredient": ingredient,
            "NormalizedIngredient": normalize_ingredient(ingredient),
            "drugbank_id": drugbank_id,
        })

    mapping_df = pd.DataFrame(mapping_results)
    mapped_count = mapping_df["drugbank_id"].notna().sum()
    print(f"   映射成功: {mapped_count} / {len(mapping_df)} ({mapped_count/len(mapping_df)*100:.2f}%)")

    # 4. 載入藥物-疾病關係
    print()
    print("4. 載入藥物-疾病關係...")
    relations_df = load_drug_disease_relations(base_dir)
    drug_indication_map = build_drug_indication_map(relations_df)
    print(f"   有適應症的藥物: {len(drug_indication_map)}")

    # 5. 生成老藥新用候選
    print()
    print("5. 生成老藥新用候選...")

    candidates = []
    valid_drugs = mapping_df[mapping_df["drugbank_id"].notna()].drop_duplicates(
        subset=["NormalizedIngredient"]
    )

    for _, row in valid_drugs.iterrows():
        drug_name = row["NormalizedIngredient"]

        # 查找 TxGNN 中的適應症
        kg_diseases = drug_indication_map.get(drug_name, set())

        for disease in kg_diseases:
            candidates.append({
                "DrugName": row["DrugName"],
                "ActiveIngredient": row["ActiveIngredient"],
                "NormalizedIngredient": drug_name,
                "drugbank_id": row["drugbank_id"],
                "PotentialIndication": disease,
                "Source": "TxGNN Knowledge Graph",
            })

    candidates_df = pd.DataFrame(candidates)

    if len(candidates_df) > 0:
        candidates_df = candidates_df.drop_duplicates(
            subset=["NormalizedIngredient", "PotentialIndication"]
        )

    print(f"   候選數: {len(candidates_df)}")

    # 6. 儲存結果
    print()
    print("6. 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 儲存映射結果
    mapping_df.to_csv(output_dir / "drug_mapping.csv", index=False)
    print(f"   映射結果: {output_dir / 'drug_mapping.csv'}")

    # 儲存候選結果
    candidates_df.to_csv(output_dir / "repurposing_candidates.csv", index=False)
    print(f"   候選結果: {output_dir / 'repurposing_candidates.csv'}")

    # 7. 統計報告
    print()
    print("=" * 60)
    print("統計報告")
    print("=" * 60)
    print(f"  總藥品數: {len(fda_df)}")
    print(f"  DrugBank 映射成功: {mapped_count} ({mapped_count/len(fda_df)*100:.2f}%)")
    print(f"  老藥新用候選數: {len(candidates_df)}")

    if len(candidates_df) > 0:
        unique_drugs = candidates_df["NormalizedIngredient"].nunique()
        unique_diseases = candidates_df["PotentialIndication"].nunique()
        print(f"  涉及藥物: {unique_drugs}")
        print(f"  涉及疾病: {unique_diseases}")

        print()
        print("前 10 個最常見的潛在新適應症:")
        for disease, count in candidates_df["PotentialIndication"].value_counts().head(10).items():
            print(f"    {disease}: {count}")

    print()
    print("完成！")
    print()
    print("下一步: 生成 FHIR 資源")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
