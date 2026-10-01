---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 1220
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Obstructive Airway Disease to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator; the supplied data does not state its approved indication, so the airway-disease use comes from general knowledge and the literature abstracts. The TxGNN model predicts it may be effective for **thrombotic disease**, but **0 clinical trials** are registered, and none of the **19 retrieved publications** tests theophylline in thrombosis. This prediction is model-only (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (all approved-indication fields are blank). Likely asthma/COPD |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for theophylline is not available in the supplied data. From general pharmacology, theophylline is a phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. PDE inhibition raises platelet cAMP, which could in theory reduce platelet aggregation.

The mechanistic link is weak because the two effects oppose each other. Adenosine normally inhibits platelets, so blocking adenosine receptors could work against an antiplatelet effect. The net direction is unclear.

The original indication is an airway disease and the predicted one is a vascular and platelet disorder, so the two are mechanistically distant. The 0.996 score is a prediction only. All seven predicted indications score between 0.993 and 0.996, so the score does not separate well-supported from unsupported ones.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved papers tests theophylline for thrombosis. No RCTs were retrieved. The papers below are the closest by topic (platelet function, thrombosis, cAMP signalling). All were auto-classified and are pending relevance review.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug. Context only, not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Thromboxane A2 and prostacyclin in platelets and atherosclerosis. Prostacyclin raises platelet cAMP (background) |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Preclinical (in vitro) | Gen Pharmacol | Milrinone, a PDE inhibitor, reduced platelet aggregation and interacted with adenosine. Indirect support for the PDE/cAMP mechanism, not theophylline |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Preclinical (in vitro) | J Nutr | Aged garlic extract inhibited platelet aggregation via cAMP/cGMP signalling. Not theophylline |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Assay/Methodological | Platelets | Measurement of soluble CLEC-2 as a marker of platelet activation in patients at thrombotic risk |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay/Methodological | Br J Haematol | Platelet factor 4 radioimmunoassay. Theophylline appears only as an anticoagulant-tube additive to prevent platelet activation in the sample |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Methodological | PLoS One | Optimized plasma preparation for platelet-stored molecules |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Methodological | Cells | Effect of anticoagulation and sample processing on blood microRNA measurement |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observational | Cor Vasa | T-lymphocyte subsets in vascular disease. Theophylline is used only as a laboratory marker for lymphocyte subsets |
| [14231672](https://pubmed.ncbi.nlm.nih.gov/14231672/) | 1964 | Review (German) | Z Gesamte Inn Med | Chronic cor pulmonale after thromboembolic disease. No abstract available |

---

## US Market Information

The supplied data has no approved-indication text for any of these products. 5 of 20 authorizations are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090430 | Theophylline | Extended-release tablet | Alembic Pharmaceuticals Inc. |
| ANDA214806 | Theophylline | Extended-release tablet | Sun Pharmaceutical Industries Limited |
| ANDA206344 | Theophylline | Solution | PAI Holdings, LLC dba PAI Pharma |
| ANDA218063 | Theophylline | Extended-release tablet | Viona Pharmaceuticals Inc |
| ANDA216276 | Theophylline | Extended-release tablet | Amneal Pharmaceuticals NY LLC |

Other listed dosage forms include extended-release capsules. All routes are oral, except the solution, which is listed under "Other".

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records are available in the supplied data. The DDI query returned no results.

Two retrieved abstracts note that theophylline has a narrow therapeutic window and can be toxic above certain blood levels (PMIDs 27334733, 29254574). Any new-indication work would need drug-level monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The thrombotic disease prediction has no registered trials and no human studies. Its mechanistic rationale is contradictory (PDE inhibition versus adenosine antagonism), and the score alone cannot separate it from the other predictions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Preclinical or clinical evidence on theophylline's effect on platelet aggregation or thrombosis
- Confirmation of the original indication, since the approved-indication fields are blank

**Other predicted indications in the same pack:**
- **Nasal cavity disease (rank 2):** One completed Phase 2 trial, [NCT03990766](https://clinicaltrials.gov/study/NCT03990766) (nasal theophylline irrigation for post-viral olfactory dysfunction, n=27). It is provisionally L2, and randomization and results still need verification.
- **Obstructive lung disease (rank 5):** Probably not a true repurposing case, because this is the established use of theophylline.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

