#!/usr/bin/env python3
"""執行 TxGNN 深度學習預測

使用 TxGNN 圖神經網路模型進行藥物-疾病預測。

使用方法:
    # 方法 1: 使用 uv (需先安裝 ml 依賴)
    uv sync --extra ml
    uv run python scripts/run_dl_prediction.py

    # 方法 2: 使用 conda 環境 (推薦)
    conda activate txgnn
    python scripts/run_dl_prediction.py

前置條件:
    1. 已執行 run_kg_prediction.py (產生 drug_mapping.csv)
    2. 安裝 PyTorch, DGL, TxGNN
    3. 下載預訓練模型

產生檔案:
    data/processed/txgnn_dl_predictions.csv
"""

import sys
from pathlib import Path

# NOTE: Do NOT add src to path here - we need the installed TxGNN package, not our local txgnn module


def check_environment():
    """檢查執行環境"""
    print("=" * 60)
    print("TxGNN Deep Learning Prediction - Environment Check")
    print("=" * 60)
    print()

    # Check PyTorch
    try:
        import torch
        print(f"✓ PyTorch: {torch.__version__}")
        if torch.cuda.is_available():
            print(f"  CUDA available: {torch.cuda.get_device_name(0)}")
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            print(f"  MPS (Apple Silicon) available")
        else:
            print(f"  Using CPU")
    except ImportError:
        print("✗ PyTorch not installed")
        print("  Install: pip install torch")
        return False

    # Check DGL
    try:
        import dgl
        print(f"✓ DGL: {dgl.__version__}")
    except ImportError:
        print("✗ DGL not installed")
        print("  Install: pip install dgl")
        return False

    # Check TxGNN
    try:
        import ustxgnn
        print(f"✓ TxGNN: installed")
    except ImportError:
        print("✗ TxGNN not installed")
        print("  Install: pip install git+https://github.com/mims-harvard/TxGNN.git")
        return False

    print()
    return True


def download_model(model_dir: Path):
    """下載預訓練模型"""
    if (model_dir / "model.pt").exists():
        print(f"✓ Pre-trained model exists: {model_dir}")
        return True

    print("Downloading pre-trained model...")
    try:
        import gdown
    except ImportError:
        print("✗ gdown not installed. Install: pip install gdown")
        return False

    model_dir.mkdir(parents=True, exist_ok=True)
    zip_path = model_dir.parent / "model_ckpt.zip"

    # TxGNN official model
    gdown.download(
        "https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj",
        str(zip_path),
        quiet=False,
    )

    import zipfile
    print("Extracting model...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(model_dir.parent)

    zip_path.unlink()
    print(f"✓ Model downloaded to: {model_dir}")
    return True


def run_prediction(
    drug_mapping_path: Path,
    output_path: Path,
    model_dir: Path,
    data_dir: Path,
    min_score: float = 0.5,
    top_k: int = 50,
    max_drugs: int | None = None,  # Limit number of drugs for testing
):
    """執行深度學習預測"""
    import pandas as pd
    from tqdm import tqdm

    print()
    print("=" * 60)
    print("Running TxGNN Deep Learning Prediction")
    print("=" * 60)
    print()

    # Load drug mapping
    print(f"Loading drug mapping: {drug_mapping_path}")
    drug_mapping = pd.read_csv(drug_mapping_path)
    valid_drugs = drug_mapping[drug_mapping["drugbank_id"].notna()]
    unique_drugs = valid_drugs["drugbank_id"].unique()
    print(f"  Total drugs with DrugBank ID: {len(unique_drugs)}")

    # Initialize TxGNN
    from txgnn import TxData, TxGNN

    print()
    print("Loading TxGNN data...")
    tx_data = TxData(data_folder_path=str(data_dir))
    tx_data.prepare_split(split="complex_disease", seed=42)
    print(f"  Nodes: {tx_data.G.number_of_nodes()}")
    print(f"  Edges: {tx_data.G.number_of_edges()}")

    print()
    print("Loading pre-trained model...")
    import torch
    # TxGNN/DGL may not fully support MPS, use CUDA if available, else CPU
    if torch.cuda.is_available():
        device = "cuda:0"
    else:
        device = "cpu"
    print(f"  Device: {device}")

    model = TxGNN(
        data=tx_data,
        weight_bias_track=False,
        proj_name="UsTxGNN",
        exp_name="us_drug_repurposing",
        device=device,
    )
    model.load_pretrained(str(model_dir))

    # Build mappings
    print()
    print("Building node mappings...")
    df = tx_data.df.copy()

    # Drug mapping
    drug_rows = df[df.x_type == "drug"][["x_id", "x_idx"]].drop_duplicates()
    drugbank_to_idx = dict(zip(drug_rows["x_id"].astype(str), drug_rows["x_idx"].astype(int)))

    # Disease mapping - get indices from df, names from node.csv
    disease_rows = df[df.y_type == "disease"][["y_id", "y_idx"]].drop_duplicates()
    all_disease_indices = sorted(disease_rows["y_idx"].astype(int).unique().tolist())

    # Load disease names from node.csv (TSV format)
    # Map y_idx -> y_id -> node_name
    node_df = pd.read_csv(data_dir / "node.csv", sep="\t")
    disease_nodes = node_df[node_df["node_type"].str.strip('"') == "disease"]
    node_id_to_name = dict(zip(disease_nodes["node_id"].str.strip('"'), disease_nodes["node_name"].str.strip('"')))

    # Create y_idx -> name mapping via y_id
    disease_idx_to_name = {}
    for _, row in disease_rows.iterrows():
        y_idx = int(row["y_idx"])
        y_id = str(row["y_id"])
        disease_idx_to_name[y_idx] = node_id_to_name.get(y_id, f"disease_{y_idx}")

    print(f"  Drugs in TxGNN: {len(drugbank_to_idx)}")
    print(f"  Diseases: {len(all_disease_indices)}")

    # Find drugs to predict
    drugs_to_predict = []
    for db_id in unique_drugs:
        if str(db_id) in drugbank_to_idx:
            drugs_to_predict.append(db_id)

    print(f"  Drugs matched in TxGNN: {len(drugs_to_predict)}")

    # Limit drugs if specified
    if max_drugs is not None and max_drugs > 0:
        drugs_to_predict = drugs_to_predict[:max_drugs]
        print(f"  Limited to first {len(drugs_to_predict)} drugs")

    # Run predictions
    print()
    print("Running predictions...")
    predictions = []

    for db_id in tqdm(drugs_to_predict, desc="Predicting"):
        drug_idx = drugbank_to_idx[str(db_id)]

        # Create prediction dataframe
        df_predict = pd.DataFrame({
            "x_idx": [drug_idx] * len(all_disease_indices),
            "relation": ["indication"] * len(all_disease_indices),
            "y_idx": all_disease_indices,
        })

        # Predict
        with torch.no_grad():
            pred_scores = model.predict(df_predict)

        etype = ("drug", "indication", "disease")
        if etype not in pred_scores:
            continue

        scores = torch.sigmoid(pred_scores[etype]).cpu().numpy()

        # Collect top predictions
        drug_preds = []
        for i, disease_idx in enumerate(all_disease_indices):
            score = float(scores[i])
            if score >= min_score:
                disease_name = disease_idx_to_name.get(disease_idx, f"disease_{disease_idx}")
                drug_preds.append({
                    "drugbank_id": db_id,
                    "disease_idx": disease_idx,
                    "disease_name": disease_name,
                    "txgnn_score": score,
                })

        # Keep top k
        drug_preds = sorted(drug_preds, key=lambda x: x["txgnn_score"], reverse=True)[:top_k]
        predictions.extend(drug_preds)

    # Create results dataframe
    result_df = pd.DataFrame(predictions)

    if len(result_df) > 0:
        result_df = result_df.sort_values("txgnn_score", ascending=False)
        result_df["rank"] = range(1, len(result_df) + 1)
        result_df["source"] = "TxGNN Deep Learning Model"

        # Save
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result_df.to_csv(output_path, index=False)

    # Statistics
    print()
    print("=" * 60)
    print("Results Summary")
    print("=" * 60)
    print(f"  Total predictions: {len(result_df)}")
    print(f"  Unique drugs: {result_df['drugbank_id'].nunique()}")
    print(f"  Unique diseases: {result_df['disease_name'].nunique()}")
    if len(result_df) > 0:
        print(f"  Avg score: {result_df['txgnn_score'].mean():.4f}")
        print(f"  Max score: {result_df['txgnn_score'].max():.4f}")
    print()
    print(f"Results saved to: {output_path}")

    return result_df


def main():
    base_dir = Path(__file__).parent.parent

    # Paths
    drug_mapping_path = base_dir / "data" / "processed" / "drug_mapping.csv"
    output_path = base_dir / "data" / "processed" / "txgnn_dl_predictions.csv.gz"
    model_dir = base_dir / "model_ckpt"
    data_dir = base_dir / "data"

    # Check environment
    if not check_environment():
        print()
        print("=" * 60)
        print("Setup Instructions")
        print("=" * 60)
        print("""
Option 1: Use conda (recommended for full TxGNN support)
---------------------------------------------------------
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm gdown

Option 2: Use uv (basic PyTorch only)
--------------------------------------
uv sync --extra ml
# Note: DGL installation may vary by platform
""")
        return

    # Check data
    if not drug_mapping_path.exists():
        print(f"✗ Drug mapping not found: {drug_mapping_path}")
        print("  Please run: uv run python scripts/run_kg_prediction.py")
        return

    # Download model if needed
    if not download_model(model_dir):
        return

    # Parse command line args
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-drugs", type=int, default=None,
                        help="Limit number of drugs to predict (for testing)")
    parser.add_argument("--min-score", type=float, default=0.3,
                        help="Minimum score threshold (default: 0.3)")
    args = parser.parse_args()

    # Run prediction
    run_prediction(
        drug_mapping_path=drug_mapping_path,
        output_path=output_path,
        model_dir=model_dir,
        data_dir=data_dir,
        min_score=args.min_score,
        top_k=50,
        max_drugs=args.max_drugs,
    )


if __name__ == "__main__":
    main()
