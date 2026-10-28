---
layout: default
title: Tolmetin
parent: Model Prediction Only (L5)
nav_order: 1240
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "TOLMETIN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "WHIM syndrome"]
description: "Tolmetin: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Tolmetin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tolmetin: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Tolmetin is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** currently support this prediction. It rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tolmetin is a non-selective cyclooxygenase (COX) inhibitor of the NSAID class. Its efficacy in rheumatoid arthritis and related joint conditions is established, through reducing inflammation and pain.

For the predicted indication, the link is weak. Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene. Tolmetin has no known effect on GDF5/BMP signalling or on the underlying skeletal growth defect. The high score (0.9998) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, symptomatic joint pain relief could be hypothesised.

### Other Predictions Reviewed

The other top-ranked predictions are also weakly supported:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 0.9998 | L5 | No clear link; COX inhibition does not address the TGF-beta bioavailability defect |
| 3 | Myosclerosis | 0.9998 | L5 | Weak and speculative; possible symptomatic analgesia only |
| 4 | Brachyolmia | 0.9997 | L5 | No clear link to the bone development pathway |
| 5 | Pseudoachondroplasia | 0.9995 | L5 | Indirect symptomatic use of NSAIDs for joint pain; no tolmetin-specific evidence |
| 6 | Rheumatoid nodulosis | 0.9976 | L5 | Indirect; lies within the rheumatoid arthritis spectrum, but NSAIDs do not generally resolve nodules |
| 9 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9972 | L5 | No identifiable link |
| 10 | WHIM syndrome | 0.9971 | L5 | No link; established therapy targets CXCR4 |

Ranks 6 to 8 are the most biologically plausible, but they largely overlap tolmetin's existing indications and are not true new uses.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074473 | Tolmetin Sodium | Tablet, film coated (oral) | Not available (valid) |
| ANDA073393 | Tolmetin Sodium | Capsule (oral) | Not available (valid) |

Both authorizations, held by Atland Pharmaceuticals, LLC, are cancelled.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension and hypertensive disorder, liver failure and liver disease, kidney disease, gallbladder disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, pyoureter.
- **Drug Interactions**: 100 interactions were found. Examples from those reviewed:
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, naltrexone, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes
  - **Minor**: famotidine, ranitidine, cimetidine, linaclotide

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical or literature support and no plausible mechanistic link to a genetic skeletal growth defect.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- FDA package insert warnings and contraindications
- Any preclinical or clinical evidence in the predicted disease
- If pursuing a more plausible direction (rheumatoid nodulosis, polyarticular JIA, spondyloarthropathy), evidence on whether tolmetin offers any advantage over current standard care
- Confirmation of product availability, given that the drug is marketed with 2 valid licenses of 2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

