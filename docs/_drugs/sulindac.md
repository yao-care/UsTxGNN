---
layout: default
title: Sulindac
parent: Model Prediction Only (L5)
nav_order: 1188
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "SULINDAC"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "pseudoachondroplasia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "WHIM syndrome", "hypermobility of coccyx"]
description: "Sulindac: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulindac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Sulindac: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Sulindac is a nonsteroidal anti-inflammatory drug (NSAID) originally used for inflammatory and degenerative joint conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, bursitis and tendinitis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general knowledge, sulindac is a cyclooxygenase (COX) inhibitor that reduces prostaglandin synthesis, and its efficacy in inflammatory joint disease is established.

The predicted disease is a rare skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5, which disrupt BMP/GDF5 signaling during skeletal development. Sulindac's COX inhibition has no known link to this signaling defect. The very high TxGNN score (0.999) is therefore a model output only, likely reflecting network proximity to other skeletal and joint disease nodes rather than a mechanism-based rationale. At most, NSAIDs might relieve joint pain symptomatically, which is not disease-modifying repurposing.

The other top-ranked predictions show the same pattern. Most are rare congenital skeletal or developmental disorders (brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome and others) with no supporting evidence. The most biologically coherent candidate is rheumatoid vasculitis (rank 9), an extra-articular complication of rheumatoid arthritis, but NSAIDs are generally not effective for vasculitis, and no evidence was provided for it either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA072711 | SULINDAC (PuraCap Laboratories / Blu Pharmaceuticals) | Tablet | Not available (valid) |
| ANDA072051 | SULINDAC (Sun Pharmaceutical Industries) | Tablet | Not available (valid) |
| ANDA072050 | SULINDAC (PD-Rx Pharmaceuticals) | Tablet | Not available (valid) |
| ANDA072710 | SULINDAC (PuraCap Laboratories / Blu Pharmaceuticals) | Tablet | Not available (valid) |
| ANDA071795 | Sulindac (PD-Rx Pharmaceuticals) | Tablet | Not available (valid) |

All six records are cancelled; only the first five are shown. The only dosage form is oral tablet.

## Safety Considerations

**Contraindications / cautions from the drug-disease knowledge graph** (these come from knowledge-graph relationships, not from package insert text):
- Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, cardiovascular and heart disease
- Gastrointestinal: peptic ulcer disease (including active peptic ulcer disease), gallbladder disease
- Renal and urinary: kidney disease, nephrolithiasis, acute urate nephropathy
- Hepatic: liver disease
- Haematological: blood coagulation disease, anaemia, hemoglobinopathy
- Autoimmune and connective tissue: systemic lupus erythematosus (including paediatric), connective tissue disease
- Other: bone disease, cartilage disease, substance abuse/dependence

Several of these (bone and cartilage disease, connective tissue disease) overlap with the predicted skeletal indications and should be reviewed carefully.

**Drug Interactions** (a screening query returned 100 interactions; the main ones from the 20 listed are shown):
- **Moderate**: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), mesalazine, balsalazide, metformin, sulfonylureas (chlorpropamide, glimepiride), potassium citrate, potassium bicarbonate, and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate)
- **Minor**: famotidine, ranitidine, cimetidine, linaclotide

Please refer to the package insert for full safety information, as label warnings were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score.

**To proceed, the following is needed:**
- Mechanism of action data for sulindac and a credible biological rationale linking it to GDF5/BMP signaling or skeletal development
- Preclinical evidence (for example, cell or animal models of GDF5-related dysplasia)
- Package insert warnings and contraindications to complete safety screening
- Clarification of regulatory and commercial status, since the drug is marketed in the US with 6 of 6 licenses valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

