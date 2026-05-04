---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 1
---

# Aflibercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

以下是根據 Evidence Pack 產生的評估報告：

---

# Aflibercept: From Neovascular AMD to Esotropia

## One-Sentence Summary

Aflibercept is an anti-VEGF fusion protein (VEGF Trap), best known for treating neovascular (wet) age-related macular degeneration, diabetic macular edema, and retinal vein occlusion. The TxGNN model predicts it may also be effective for **Esotropia** (inward ocular deviation / strabismus). Currently, there are **0 clinical trials** and **0 publications** directly supporting this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No records in regulatory database (Neovascular AMD / DME based on known drug profile) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Market Status | ✗ Not Marketed (per regulatory query) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided evidence pack. Based on known pharmacological information, aflibercept is a recombinant fusion protein (VEGF Trap) comprising the VEGF-binding domains of VEGFR-1 and VEGFR-2, fused to the Fc portion of human IgG1. It binds VEGF-A, VEGF-B, and placental growth factor (PlGF) with higher affinity than either native receptor, blocking downstream signalling and inhibiting pathological angiogenesis and vascular hyper-permeability. Its efficacy in neovascular retinal diseases has been validated across multiple pivotal Phase 3 trials.

Esotropia is a form of strabismus in which one or both eyes deviate medially. Its aetiology spans accommodative imbalance, high myopia, and sensorimotor fusion disruption. A potential mechanistic bridge lies in the VEGF pathway's role in **ocular tissue remodelling and fibrosis**: anti-VEGF agents have been explored as surgical adjuncts in strabismus procedures to reduce post-operative scarring around extraocular muscles and Tenon's capsule, potentially improving alignment durability and reducing recurrence rates.

High-myopia–associated esotropia represents a further point of contact, as progressive axial elongation is accompanied by posterior-segment vascular changes where VEGF inhibition may have biological relevance. The TxGNN knowledge graph most likely identified this shared ophthalmological domain — vascular and connective-tissue biology within the eye — as the basis for its high-confidence prediction. However, without dedicated preclinical or clinical studies, the applicability of aflibercept to esotropia remains speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No licensing records were returned for aflibercept by the regulatory database query (query date: 2026-03-24). This is likely a database coverage gap rather than an indication of true non-approval: aflibercept (Eylea®) holds FDA approval in the United States for neovascular AMD, macular edema following CRVO and BRVO, diabetic macular edema, and diabetic retinopathy. A full regulatory verification against the FDA Orange Book is recommended as a next step.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a very high prediction score (99.38%), there is currently no clinical trial, observational study, or published literature to support the use of aflibercept in esotropia. An L5 evidence level — model prediction only — is insufficient to proceed to clinical evaluation without at least preclinical mechanistic corroboration.

**To proceed, the following is needed:**

- **Mechanistic studies**: Identify whether VEGF inhibition demonstrably affects extraocular muscle fibrosis, connective tissue remodelling, or accommodative tone in esotropia models (addresses DG002 — MOA gap)
- **Literature sweep**: Broaden search to include anti-VEGF agents as strabismus surgery adjuncts, or VEGF pathway involvement in paediatric/adult esotropia — current PubMed query returned 0 results but broader MeSH terms may yield relevant results
- **Safety review**: Obtain and parse the full prescribing information to complete S1 safety assessment (DG001 — currently a blocking gap)
- **Regulatory verification**: Confirm US FDA approval status via the Orange Book to establish a proper regulatory baseline for the repurposing dossier
- **Route-of-administration assessment**: Aflibercept is administered by intravitreal injection; confirm whether the same route would be appropriate for an esotropia indication or whether an alternative formulation would be required

---

*This report is generated for research reference purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

