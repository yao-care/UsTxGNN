# UsTxGNN

US drug repurposing predictions using TxGNN knowledge graph.

## Overview

This project uses TxGNN (Therapeutic Knowledge Graph Neural Network) to predict drug repurposing candidates for US FDA-approved drugs.

## Installation

```bash
uv sync
```

## Usage

```bash
# Process FDA data
uv run python scripts/process_fda_data.py

# Prepare external data
uv run python scripts/prepare_external_data.py

# Run KG prediction
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

## Disclaimer

This project is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
