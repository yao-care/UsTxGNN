---
layout: default
title: Binetrakin
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 9
---

# Binetrakin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Binetrakin: From No Recorded Indication to Craniostenosis Cataract

## One-Sentence Summary

Binetrakin is marketed as the product GUNA-IL 4 (oral drops), but no approved indication is recorded for it.
The TxGNN model predicts it may be effective for **craniostenosis cataract** (a syndromic cataract), along with several other cataract types.
There are currently **0 clinical trials** and **0 publications** for this top prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the approved indication text is empty) |
| Predicted New Indication | Craniostenosis cataract |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Binetrakin. Its original indication is also not recorded. As a result, the drug's mechanism cannot be linked to craniostenosis cataract, and the similarity between the original and new indications cannot be assessed.

The product name "GUNA-IL 4" suggests an interleukin-4-related preparation, but this is only an inference from the name and is not confirmed by the data. The prediction is therefore best read as a statistical signal from the knowledge graph, not a mechanism-based hypothesis.

TxGNN gave the same high score (about 99.1%) to a group of related cataract terms: mature, immature, tetanic, nuclear senile, cortical, senile, diabetic, and type 2 diabetes-associated cataract. This clustering suggests the model is picking up a general "cataract" signal rather than something specific to craniostenosis cataract. It should not be read as separate confirmations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for craniostenosis cataract.

Only two of the other cataract predictions have any papers. All are indirect: they describe cytokine changes in diseased eyes, and none studies Binetrakin.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35585570](https://pubmed.ncbi.nlm.nih.gov/35585570/) | 2022 | RCT (aqueous humor biomarker analysis) | BMC Ophthalmology | Changes in 28 cytokines and angiogenic factors in aqueous humor after conbercept injection in proliferative diabetic retinopathy with neovascular glaucoma, linked to intraoperative bleeding (diabetic cataract prediction) |
| [20213480](https://pubmed.ncbi.nlm.nih.gov/20213480/) | 2010 | Animal study | Graefe's Arch Clin Exp Ophthalmol | IL-2 and IFN-gamma profiles and tyrosine nitration in the retina of diabetic rats (diabetic cataract prediction) |
| [23049540](https://pubmed.ncbi.nlm.nih.gov/23049540/) | 2012 | Animal study | Exp Diabetes Res | Nicotine exacerbated cataract development in a type 1 diabetic rat model (diabetic cataract prediction) |
| [10502054](https://pubmed.ncbi.nlm.nih.gov/10502054/) | 1999 | Expression study | Graefe's Arch Clin Exp Ophthalmol | TGF-alpha, TGF-beta2 and IL-8 mRNA expression in lens epithelial cells from senile cataract patients (senile cataract prediction) |
| [8157173](https://pubmed.ncbi.nlm.nih.gov/8157173/) | 1994 | Observational | Graefe's Arch Clin Exp Ophthalmol | IL-4, IgG and oligoclonal IgG were elevated in aqueous humor of cataract patients with prior uveitis (senile cataract prediction) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not recorded | GUNA-IL 4 (Guna spa) | Solution / drops | Not recorded |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the DDI query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials, no direct literature, no mechanism data, and no recorded approved indication. The available papers describe cytokine changes in diseased eyes and do not test the drug. The evidence stays at L5 for the top prediction (L4 for diabetic and senile cataract).

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank), to test whether any biological link to cataract exists
- The package insert, covering warnings and contraindications, which is currently blocking safety screening
- The product's approved indication text and license number, to establish the original indication
- Route compatibility assessment, since the current product is an oral drop and any ocular use would need a suitable formulation
- A targeted search for direct evidence, including preclinical lens models

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

