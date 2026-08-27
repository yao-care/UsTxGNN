---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 623
evidence_level: L5
indication_count: 10
---

# Dorzolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase (CA-II) inhibitor already used worldwide to lower intraocular pressure in open-angle glaucoma (as Trusopt/Cosopt).
The TxGNN model's top prediction extends this to **Primary Hereditary Glaucoma**, a rare inherited glaucoma subtype, currently supported by **1 completed Phase 2 clinical trial** and **no dedicated literature**.
Because the underlying pharmacology (reducing aqueous humor production) is already clinically validated in the broader glaucoma population, this is best characterized as a mechanistic subtype extension rather than a novel therapeutic hypothesis — but direct evidence for the hereditary subtype itself remains thin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this regulatory dataset; established clinical use (per trial/literature evidence in this pack) is topical treatment of open-angle glaucoma / ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | Not Marketed (no licenses on file in this jurisdiction) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data (DrugBank `original_moa`) is currently a data gap. However, the evidence trail collected across this drug's predicted indications consistently identifies dorzolamide as a **topical carbonic anhydrase II (CA-II) inhibitor**: it suppresses bicarbonate-dependent fluid transport in the ciliary body, reducing aqueous humor production and lowering intraocular pressure (IOP). This mechanism is already clinically proven — the evidence pack independently documents over 40 completed clinical trials and 20+ publications supporting dorzolamide (alone or as the fixed combination dorzolamide/timolol, "Cosopt") for open-angle glaucoma and ocular hypertension (see rank 6–7 candidates in the source data), including multiple Phase 3/4 head-to-head trials (e.g., NCT00878917, NCT00397241, NCT00822055).

Primary hereditary glaucoma (including congenital/juvenile open-angle forms) shares the same core pathology — pressure elevation driven by excess aqueous humor relative to outflow — so a CA-II inhibitor is mechanistically expected to lower IOP regardless of the underlying genetic etiology. This is not a novel biological hypothesis so much as a **population/subtype extension** of an already-validated drug class effect.

That said, this specific subtype introduces meaningful uncertainty: hereditary/congenital glaucoma patients often have coexisting angle developmental abnormalities (e.g., trabeculodysgenesis), which can alter both drug response and safety margins compared with typical adult primary open-angle glaucoma (POAG). The single supporting trial in this pack (NCT01527682) evaluated a prostaglandin analogue **plus** a carbonic anhydrase inhibitor as a drug class in pediatric glaucoma — it is not a dorzolamide-specific, hereditary-subtype-specific efficacy trial, so it should be read as supportive rather than confirmatory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed the ocular hypotensive effect of latanoprost plus dorzolamide in pediatric glaucoma patients refractory to surgery; enrollment target was later reduced from 96 to 68 eyes due to slow recruitment. Evaluates the carbonic-anhydrase-inhibitor drug class alongside dorzolamide rather than dorzolamide alone, so this is class-level rather than drug-specific evidence (relevance grade B). |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorizations (NDAs/licenses) are currently on file for dorzolamide in this regulatory dataset (0 total, market status: Not Marketed). This reflects a gap in the regulatory data source rather than evidence against the drug's efficacy — dorzolamide-based products (e.g., Trusopt, Cosopt) are approved and marketed in multiple jurisdictions globally.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — DDI query returned no results, and the TFDA label/warnings retrieval is flagged as a blocking data gap pending PDF acquisition and parsing.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The repurposing hypothesis rests on a pharmacologically sound and already-validated mechanism (CA-II inhibition lowering IOP), and the drug class has extensive direct evidence in the closely related open-angle glaucoma population. However, evidence specific to the hereditary/congenital glaucoma subtype is limited to a single class-level Phase 2 trial (L2), and critical safety and regulatory inputs (TFDA warnings/contraindications, confirmed MOA, market authorization status) are currently missing.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening can be completed)
- Confirmed mechanism of action from DrugBank API (High-severity gap affecting mechanistic-linkage confidence)
- A dorzolamide-specific efficacy/safety trial (or subgroup analysis) in patients with primary hereditary/congenital glaucoma, distinct from general pediatric CAI-class studies
- Assessment of route/formulation compatibility for the pediatric/hereditary glaucoma population (e.g., angle developmental abnormalities that may affect topical drug response)
- Clarification of market/licensing status in the target jurisdiction, since "Not Marketed" currently reflects a data gap rather than a regulatory rejection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

