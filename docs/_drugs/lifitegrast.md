---
layout: default
title: Lifitegrast
parent: Model Prediction Only (L5)
nav_order: 860
evidence_level: L5
indication_count: 6
---

# Lifitegrast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Lifitegrast: From Dry Eye Disease to Penile Fibromatosis

## One-Sentence Summary

Lifitegrast is a topical eye drug that blocks LFA-1/ICAM-1 T-cell adhesion. The Evidence Pack does not list an approved indication, but the marketed product Xiidra is known to be used for dry eye disease.
The TxGNN model predicts it may be effective for **penile fibromatosis** with a very high score, but there are **0 clinical trials** and **0 publications** for this indication. The prediction is model-only and no mechanistic link is established.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the Evidence Pack (approved indication text is empty; Xiidra is known to be indicated for dry eye disease) |
| Predicted New Indication | Penile fibromatosis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 authorizations (1 ANDA and NDA208073 listed twice, for two manufacturers) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The mechanism-of-action field is a data gap in the Evidence Pack. The analysis notes describe lifitegrast as an LFA-1/ICAM-1 antagonist that blocks T-cell adhesion. This fits an inflammatory eye condition such as dry eye disease.

Penile fibromatosis (Peyronie-type fibrotic disease) is driven by fibroblast proliferation and collagen deposition. Lifitegrast has no documented role in either process. The high TxGNN score (0.996) appears to reflect a shared fibromatosis cluster in the knowledge graph, not drug-specific biology. The same pattern applies to the other fibromatosis predictions (palmar fibromatosis, Ledderhose disease, infantile digital fibromatosis), which have similar scores and no supporting evidence.

**This prediction is therefore best read as a graph-neighborhood artifact, not a credible repurposing lead.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA215063 | Lifitegrast (Aurobindo Pharma Limited) | For solution | Not listed in source data |
| NDA208073 | Xiidra (Bausch & Lomb Incorporated) | Solution/drops | Not listed in source data |
| NDA208073 | Xiidra (Novartis Pharmaceuticals Corporation) | Solution/drops | Not listed in source data |

Both dosage forms are ophthalmic products. No topical or injectable form for penile or connective-tissue use exists.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for penile fibromatosis rests only on a model score. There are no trials or publications, and no plausible link between LFA-1 blockade and fibrotic disease. The ophthalmic-only formulations also do not fit this indication.

**To proceed, the following is needed:**
- Preclinical evidence that LFA-1/ICAM-1 blockade affects fibroblast proliferation or collagen deposition
- Approved indication text and package insert warnings and contraindications (currently missing)
- A route-of-administration assessment, since only ophthalmic forms exist

**Alternative lead within this candidate:** Diabetic retinopathy (rank 6, score 99.03%, evidence level L4, "Research Question") is a more credible direction. LFA-1/ICAM-1-mediated leukostasis and inflammation contribute to retinal vascular damage, and a Phase 1b study of topical lifitegrast (SAR 1118; [PMID 22538219](https://pubmed.ncbi.nlm.nih.gov/22538219/)) cited its role in diabetic macular oedema. Two steps remain before that direction can be pursued:
- Manually verify what [NCT04030962](https://clinicaltrials.gov/study/NCT04030962) studied, because its title is truncated and it appears to be a dry eye study.
- Show that topical dosing can reach the retina.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

