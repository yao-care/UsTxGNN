---
layout: default
title: Home
nav_order: 1
description: "UsTxGNN - US FDA Drug Repurposing Predictions using TxGNN Knowledge Graph"
permalink: /
---

# UsTxGNN Drug Repurposing Reports
{: .fs-9 }

AI-powered drug repurposing predictions for US FDA approved drugs using the TxGNN knowledge graph.
{: .fs-6 .fw-300 }

[View Predictions](/drugs/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[FHIR API](/fhir/metadata){: .btn .fs-5 .mb-4 .mb-md-0 }

---

{: .warning }
> **Research Use Only**: The predictions on this site are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.

## Overview

UsTxGNN leverages the [TxGNN](https://www.nature.com/articles/s41591-023-02233-x) knowledge graph to identify potential new therapeutic uses for existing FDA-approved drugs. This approach, known as drug repurposing or drug repositioning, can accelerate the discovery of new treatments by building on established safety profiles.

### Key Features

- **104,000+ FDA Drugs**: Comprehensive coverage of US FDA approved medications
- **Knowledge Graph Predictions**: Powered by TxGNN's biomedical knowledge graph
- **Evidence Integration**: Links to ClinicalTrials.gov, PubMed, and DrugBank
- **FHIR R4 Compatible**: Standardized healthcare data exchange
- **SMART on FHIR**: EHR integration ready

## Data Sources

| Source | Description |
|:-------|:------------|
| [US FDA NDC](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory) | National Drug Code Directory |
| [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) | Therapeutic knowledge graph |
| [DrugBank](https://go.drugbank.com/) | Drug and target information |
| [ClinicalTrials.gov](https://clinicaltrials.gov/) | Clinical trial evidence |
| [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Biomedical literature |

## API Access

### FHIR R4 Endpoint

```
GET https://ustxgnn.yao.care/fhir/metadata
```

Available resources:
- `MedicationKnowledge` - Drug information
- `ClinicalUseDefinition` - Repurposing predictions

### SMART on FHIR

Launch the SMART app from your EHR system:
```
https://ustxgnn.yao.care/smart/launch.html
```

## Statistics

| Metric | Value |
|:-------|------:|
| Total FDA Drugs | 104,047 |
| DrugBank Mappings | 7,958 |
| Disease Ontology | 17,081 |
| Drug-Disease Relations | 80,127 |

## Citation

If you use UsTxGNN in your research, please cite:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  publisher={Nature Publishing Group}
}
```

---

## Disclaimer

{: .important }
> This website provides computational predictions for research purposes only. The information presented here:
> - Does NOT constitute medical advice
> - Should NOT be used for clinical decision-making without proper validation
> - Requires independent clinical trial verification before any therapeutic application
>
> Always consult qualified healthcare professionals for medical decisions.

---

*Last updated: {{ site.time | date: "%Y-%m-%d" }}*
