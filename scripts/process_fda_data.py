#!/usr/bin/env python3
"""處理 US FDA NDC (National Drug Code) 藥品資料

將下載的 NDC ZIP 檔案解壓縮並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://www.accessdata.fda.gov/cder/ndctext.zip
    (NDC Directory - 包含所有在美國上市的藥品)

產生檔案:
    data/raw/us_fda_drugs.json
"""

import json
import zipfile
from io import StringIO
from pathlib import Path

import pandas as pd


def find_fda_zip(raw_dir: Path) -> Path:
    """在 raw 目錄中尋找 FDA ZIP 檔案

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        找到的 ZIP 檔案路徑

    Raises:
        FileNotFoundError: 找不到 ZIP 檔案
    """
    zip_files = list(raw_dir.glob("*.zip"))

    if not zip_files:
        raise FileNotFoundError(
            f"在 {raw_dir} 找不到 ZIP 檔案\n"
            f"請先下載 NDC 資料：\n"
            f"curl -L -o data/raw/drugsfda.zip https://www.accessdata.fda.gov/cder/ndctext.zip"
        )

    return zip_files[0]


def read_txt_from_zip(zf: zipfile.ZipFile, filename: str) -> pd.DataFrame:
    """從 ZIP 讀取 tab-separated txt 檔案

    Args:
        zf: ZipFile 物件
        filename: 檔案名稱

    Returns:
        DataFrame
    """
    matching_files = [f for f in zf.namelist() if f.lower().endswith(filename.lower())]
    if not matching_files:
        raise ValueError(f"ZIP 中找不到 {filename}")

    filepath = matching_files[0]
    print(f"  讀取: {filepath}")

    with zf.open(filepath) as f:
        content = f.read().decode("utf-8", errors="replace")
        df = pd.read_csv(StringIO(content), sep="\t", low_memory=False)

    return df


def process_ndc_zip(zip_path: Path, output_path: Path) -> Path:
    """處理 NDC ZIP 檔案

    Args:
        zip_path: ZIP 檔案路徑
        output_path: 輸出 JSON 檔案路徑

    Returns:
        輸出檔案路徑
    """
    print(f"讀取 ZIP 檔案: {zip_path}")
    print(f"檔案大小: {zip_path.stat().st_size / 1024 / 1024:.1f} MB")
    print()

    with zipfile.ZipFile(zip_path, "r") as zf:
        print("ZIP 內容:")
        for name in zf.namelist():
            print(f"  {name}")
        print()

        print("讀取資料檔案...")
        products = read_txt_from_zip(zf, "product.txt")

    print()
    print(f"原始資料: {len(products)} 筆")
    print(f"欄位: {list(products.columns)}")

    # 過濾有效藥品
    # 排除已下市 (有 ENDMARKETINGDATE) 和排除標記 (NDC_EXCLUDE_FLAG = 'Y')
    if "NDC_EXCLUDE_FLAG" in products.columns:
        products = products[products["NDC_EXCLUDE_FLAG"] != "Y"]
        print(f"排除 NDC_EXCLUDE_FLAG=Y 後: {len(products)} 筆")

    if "ENDMARKETINGDATE" in products.columns:
        # 保留沒有結束日期的（仍在上市）
        active = products[products["ENDMARKETINGDATE"].isna()].copy()
        print(f"排除已下市後: {len(active)} 筆")
    else:
        active = products.copy()

    # 標準化欄位名稱
    column_mapping = {
        "APPLICATIONNUMBER": "ApplNo",
        "PROPRIETARYNAME": "DrugName",
        "NONPROPRIETARYNAME": "GenericName",
        "SUBSTANCENAME": "ActiveIngredient",
        "DOSAGEFORMNAME": "Form",
        "ROUTENAME": "Route",
        "LABELERNAME": "Manufacturer",
        "STARTMARKETINGDATE": "ApprovalDate",
        "MARKETINGCATEGORYNAME": "MarketingCategory",
        "PHARM_CLASSES": "PharmClasses",
        "ACTIVE_NUMERATOR_STRENGTH": "Strength",
        "ACTIVE_INGRED_UNIT": "StrengthUnit",
        "PRODUCTNDC": "ProductNDC",
    }

    # 只保留需要的欄位
    columns_exist = [c for c in column_mapping.keys() if c in active.columns]
    active = active[columns_exist].copy()
    active = active.rename(columns={c: column_mapping[c] for c in columns_exist})

    # 過濾有成分的藥品
    if "ActiveIngredient" in active.columns:
        active = active[active["ActiveIngredient"].notna() & (active["ActiveIngredient"] != "")]
        print(f"有成分資料: {len(active)} 筆")

    # 去重（以 ProductNDC 或 DrugName + ActiveIngredient 為主鍵）
    if "ProductNDC" in active.columns:
        active = active.drop_duplicates(subset=["ProductNDC"])
    elif "DrugName" in active.columns and "ActiveIngredient" in active.columns:
        active = active.drop_duplicates(subset=["DrugName", "ActiveIngredient"])

    print(f"去重後: {len(active)} 筆")

    # 轉換為 JSON
    data = active.to_dict(orient="records")

    # 清理 NaN 值
    for record in data:
        for key, value in list(record.items()):
            if pd.isna(value):
                record[key] = None

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 儲存 JSON
    print()
    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示摘要
    print()
    print("=== 資料摘要 ===")
    if "ActiveIngredient" in active.columns:
        print(f"獨特成分數: {active['ActiveIngredient'].nunique()}")
    if "Form" in active.columns:
        print(f"劑型分布 (前5):")
        for form, count in active["Form"].value_counts().head(5).items():
            print(f"  {form}: {count}")

    return output_path


def main():
    print("=" * 60)
    print("處理 US FDA NDC 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "us_fda_drugs.json"

    raw_dir.mkdir(parents=True, exist_ok=True)

    zip_path = find_fda_zip(raw_dir)
    process_ndc_zip(zip_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
