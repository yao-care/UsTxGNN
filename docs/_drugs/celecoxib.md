---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 510
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Celecoxib: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis…"
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "inflammatory spondylopathy", "WHIM syndrome"]
---

# Celecoxib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Celecoxib: From Arthritis (Rheumatoid Arthritis, Ankylosing Spondylitis, Osteoarthritis) to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Celecoxib is a COX-2 inhibitor originally used to treat inflammatory and degenerative joint diseases such as rheumatoid arthritis, ankylosing spondylitis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder, but **no clinical trials and no publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis, juvenile idiopathic arthritis (taken from the knowledge-graph indication list, because the US license records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 12 US authorizations (1 NDA and 11 ANDAs, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Celecoxib is generally known as a selective COX-2 inhibitor that reduces prostaglandin-driven inflammation and pain. Its efficacy in arthritis is well established.

For this prediction, however, the mechanistic link is weak. Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by loss-of-function mutations in the *CDMP1/GDF5* gene. This is a developmental defect, not an inflammatory process, and COX-2 inhibition does not address it.

The very high TxGNN score most likely reflects the disease's closeness to musculoskeletal disease nodes in the knowledge graph, not a biological rationale. At best, celecoxib might offer symptomatic pain relief, and no evidence for that was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All listed authorizations are cancelled. The compiled data contains no approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020998 | CELEBREX (Viatris Specialty LLC) | Capsule | Not listed |
| ANDA205129 | Celecoxib (Radha Pharmaceuticals) | Capsule | Not listed |
| ANDA204776 | Celecoxib (Northwind Health Company) | Capsule | Not listed |
| ANDA204519 | Celecoxib (Alembic Pharmaceuticals) | Capsule | Not listed |
| ANDA207446 | Celecoxib (Cipla USA) | Capsule | Not listed |

Only these 5 of the 12 authorizations are shown. The only dosage form is an oral capsule.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text)**: hypertension, kidney disease, liver disease, gallbladder disease, congestive heart failure, peptic ulcer disease (including active), asthma, stroke and cerebrovascular disorders, myocardial infarction and coronary thrombosis, cardiovascular and heart disease, anemia and hemoglobinopathy, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were identified. The one **Major** interaction shown is with **eliglustat**. Examples of Moderate interactions are hydrocortisone, metformin, sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), nateglinide, exenatide, mesalazine, balsalazide, olsalazine, cimetidine, levofloxacin, metronidazole, kanamycin and naltrexone.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or literature, and no credible biological link between COX-2 inhibition and the genetic cause of this disease. The cardiovascular, gastrointestinal and renal risk signals and the cancelled US market status add further practical barriers.

**To proceed, the following is needed:**
- A biological rationale connecting celecoxib to GDF5/CDMP1 pathway biology or to a clinical symptom target
- Preclinical or case-level evidence in this disease
- Package insert warnings and contraindications, plus detailed mechanism of action data
- Confirmation of regional product availability

**Note on other predictions in the same set:** Among the other predicted indications, **inflammatory spondylopathy** (rank 9; TxGNN score 99.80%) has by far the strongest support: Phase 3 and Phase 4 RCTs in ankylosing spondylitis (for example NCT00648141, n=458, and NCT02528201, n=330) and an RCT-based publication (PMID 38228361). It is rated L1 with a "Proceed with Guardrails" recommendation. However, it largely overlaps with celecoxib's existing approved uses, so it is label-consistent rather than true repurposing. Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (rank 8) is likewise an overlap with an existing use. The other predictions are computational only or have very limited evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

