# UsTxGNN - United States Drug Repurposing Predictions

[![Website](https://img.shields.io/badge/Website-ustxgnn.yao.care-blue)](https://ustxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Drug repurposing predictions for the United States using the TxGNN model.

## Disclaimer

- The results of this project are for research purposes only and do not constitute medical advice.
- Drug repurposing candidates require clinical validation before application.

## Project Overview

| Item | Count |
|------|-------|
| **Drug Reports** | 944 |
| **Total Predictions** | 168,043,848 |

## Prediction Methods

### Knowledge Graph Method
Direct querying of drug-disease relationships in the TxGNN knowledge graph, identifying potential repurposing candidates based on existing connections in the biomedical network.

### Deep Learning Method
Uses the TxGNN pre-trained neural network model to compute prediction scores, evaluating the likelihood of new therapeutic indications for approved drugs.

## Links

- Website: https://ustxgnn.yao.care
- TxGNN Paper: https://doi.org/10.1038/s41591-023-02233-x
