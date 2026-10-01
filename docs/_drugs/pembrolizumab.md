---
layout: default
title: Pembrolizumab
parent: Model Prediction Only (L5)
nav_order: 1024
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pembrolizumab: From Cancer Immunotherapy to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab (brand name KEYTRUDA) is a PD-1 blocking antibody used in cancer immunotherapy. The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** were retrieved to support this prediction. It is a model-only signal and should be treated as unvalidated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (pembrolizumab is an oncology PD-1 inhibitor) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125514) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Pembrolizumab is known to be a monoclonal antibody that blocks the PD-1 receptor on T cells. This releases the brake on tumour-directed immune responses, and the drug is established in oncology.

Gingival fibromatosis is a benign, slowly progressive fibrotic overgrowth of the gums. It can be hereditary or drug-induced. It is not a tumour driven by immune evasion, so there is no evident PD-1/PD-L1 pathway to target. The high TxGNN score (99.40%, model rank 13,775) reflects a statistical pattern in the knowledge graph rather than a known biological link.

The mechanistic link is therefore weak. Immune activation from checkpoint blockade could also carry a theoretical inflammatory risk in a benign condition. This prediction is not supported by any biological rationale at present.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125514 | KEYTRUDA (Merck Sharp & Dohme LLC) | Injection, solution | Not listed in source data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 checkpoint inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (immune-related adverse events are the main concern for this drug class) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature, and no plausible PD-1 blockade rationale for a benign fibrotic gingival condition. It is not recommended to advance this indication. Among the other top predictions, only lung hilum carcinoma has any indirect support (L4, "Research Question"), and it likely overlaps with existing approved lung cancer use.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications (this blocks safety screening)
- Preclinical or case-level evidence linking PD-1 signalling to gingival fibrosis
- A safety assessment of immune activation in a benign, non-life-threatening condition

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

