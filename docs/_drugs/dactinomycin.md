---
layout: default
title: Dactinomycin
parent: 僅模型預測 (L5)
nav_order: 564
evidence_level: L5
indication_count: 9
---

# Dactinomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dactinomycin: From Rhabdomyosarcoma / Wilms Tumor to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin (Actinomycin D) is a classic cytotoxic antibiotic established as a cornerstone of pediatric oncology, best known as the "A" in the VAC regimen (Vincristine + Actinomycin D + Cyclophosphamide) for rhabdomyosarcoma and Wilms tumor.
The TxGNN model's top-ranked prediction assigns it to **Relapsing-Remitting Multiple Sclerosis (RRMS)** with a score of 99.58%; however, **no supporting clinical trials or literature** have been identified for this indication.
This evidence pack covers 9 predicted indications in total — several rhabdomyosarcoma subtypes (Ranks 2, 5, 6) carry substantially stronger evidence (L1–L3) and merit higher prioritization.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rhabdomyosarcoma, Wilms tumor, Ewing's sarcoma, gestational trophoblastic neoplasia (established clinical use; no Taiwan regulatory data on file) |
| Predicted New Indication (Rank 1) | Relapsing-Remitting Multiple Sclerosis (RRMS) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 — model prediction only; zero clinical trials or publications identified |
| Taiwan Market Status | Not marketed (0 approved licenses) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Dactinomycin is a chromopeptide antibiotic that intercalates into the minor groove of double-stranded DNA, physically blocking RNA polymerase and halting transcription. This mechanism is cell-cycle non-specific but preferentially affects rapidly dividing cells — which is why it works so well against rhabdomyosarcoma, nephroblastoma, and Ewing's sarcoma, all of which are fast-proliferating solid tumors.

The theoretical bridge to RRMS runs through immunosuppression: autoreactive T and B lymphocytes that drive the relapsing-remitting cycle of CNS demyelination are themselves rapidly proliferating cells. In principle, a transcription inhibitor powerful enough to kill tumor cells could also ablate pathogenic lymphocyte clones, dampening relapse frequency. This is the same broad logic that has motivated the use of other cytotoxic agents (e.g., mitoxantrone) as last-resort MS therapies.

However, the mechanistic case breaks down quickly upon scrutiny. RRMS pathology centers on neuroinflammation, oligodendrocyte injury, and progressive axonal loss — processes that current disease-modifying therapies address with precise CNS penetration and receptor-level specificity (natalizumab targeting α4-integrin, ocrelizumab targeting CD20, fingolimod modulating sphingosine-1-phosphate receptors). Dactinomycin has no known neuroprotective activity, no published blood-brain barrier pharmacokinetics, and no intrathecal mechanism support. The repurposing rationale in this evidence pack explicitly flags this prediction as a probable knowledge-graph false positive: autoimmune and oncology disease nodes share a "lymphocyte proliferation hub" in TxGNN's graph, artificially inflating the score. This indication should not be pursued ahead of the strongly evidenced RMS subtypes in this same pack.

---

## Clinical Trial Evidence

No clinical trials linking Dactinomycin to relapsing-remitting multiple sclerosis are currently registered.

---

## Literature Evidence

No published literature directly linking Dactinomycin to relapsing-remitting multiple sclerosis is available.

---

## Summary of All Predicted Indications

Because the top-ranked prediction (RRMS) has no supporting evidence, the table below provides an at-a-glance view of all 9 predictions to support prioritization decisions:

| Rank | Indication | TxGNN Score | Evidence Level | Decision |
|------|-----------|-------------|----------------|----------|
| 1 | Relapsing-remitting multiple sclerosis | 99.58% | **L5** | Hold |
| 2 | Botryoid-type embryonal RMS of vagina | 99.54% | **L3** | Proceed with Guardrails |
| 3 | Extrahepatic bile duct rhabdomyosarcoma | 99.49% | **L4** | Research Question |
| 4 | Embryonal extrahepatic bile duct RMS | 99.48% | **L5** | Hold |
| 5 | Parameningeal embryonal rhabdomyosarcoma | 99.48% | **L1** ✓ | Proceed with Guardrails |
| 6 | Prostate embryonal rhabdomyosarcoma | 99.46% | **L3** | Proceed with Guardrails |
| 7 | Liver sarcoma | 99.42% | **L3** | Proceed with Guardrails |
| 8 | Upper aerodigestive tract neoplasm | 99.16% | **L4** | Research Question |
| 9 | Head and neck cancer | 99.16% | **L3** | Research Question |

**Rank 5 (parameningeal embryonal rhabdomyosarcoma)** is the highest-evidence prediction in this pack and is discussed in detail in the Conclusion section.

---

## Taiwan Market Information

Dactinomycin is not approved or marketed in Taiwan. No NDA or product licenses are on file with the TFDA.

> **Reference:** In the United States, Dactinomycin is marketed as **Cosmegen® (Lundbeck)** and is FDA-approved for Wilms tumor, rhabdomyosarcoma, Ewing's sarcoma, uterine sarcoma, gestational trophoblastic neoplasia, and testicular carcinoma.

---

## Cytotoxicity

Dactinomycin is a cytotoxic antineoplastic antibiotic. This section is required.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA intercalating antibiotic (Actinomycin class); inhibits RNA synthesis by blocking RNA polymerase |
| Myelosuppression Risk | **High** — leukopenia, thrombocytopenia, and anemia are characteristic; neutrophil nadir typically occurs around Day 14–21 post-dose |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential (at each cycle nadir), liver function tests — ALT/AST/bilirubin (dactinomycin-induced hepatopathy including veno-occlusive disease [VOD] documented in pediatric VAC regimens, PMID 9191535, 15143082; risk elevated in children under 3 years), renal function |
| Handling Protection | Classified as a vesicant — strict extravasation precautions required; must follow cytotoxic drug handling regulations (closed-system transfer devices, dedicated PPE) |

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan-specific warnings, contraindications, or drug interaction data are available, as this drug is not approved in Taiwan.

> **Hepatotoxicity alert (from embedded literature):** Veno-occlusive disease of the liver has been specifically documented in children receiving VAC chemotherapy containing Dactinomycin as part of Intergroup Rhabdomyosarcoma Study protocols (PMID 9191535; PMID 15143082). Age under 3 years is an independent risk factor. This is a critical safety consideration for any pediatric use.

---

## Conclusion and Next Steps

### For the Top-Ranked Prediction (RRMS): Hold

**Rationale:**
Despite a 99.58% TxGNN score, Dactinomycin has no clinical trials, no published evidence, and no credible mechanistic pathway specifically supporting use in RRMS. The high score reflects knowledge-graph topology (shared lymphocyte proliferation nodes between autoimmune and oncology disease spaces), not biological plausibility for this specific disease.

**What would be required to revisit:**
- Preclinical efficacy data in EAE (experimental autoimmune encephalomyelitis) mouse models
- CNS pharmacokinetic data demonstrating meaningful blood-brain barrier penetration
- A therapeutic window analysis separating selective immunosuppression from broad cytotoxicity
- Mechanistic differentiation from approved CNS-targeted immunotherapies

---

### Higher-Priority Indication: Parameningeal Embryonal Rhabdomyosarcoma (Rank 5)

**Decision: Proceed with Guardrails**

**Evidence summary:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19770373](https://pubmed.ncbi.nlm.nih.gov/19770373/) | 2009 | Phase 3 RCT (COG D9803) | J Clin Oncol | Compared VAC vs VAC/VTC in intermediate-risk RMS (including parameningeal); established VAC as standard backbone |
| [10856103](https://pubmed.ncbi.nlm.nih.gov/10856103/) | 2000 | Phase 3 RCT (IRS-IV) | J Clin Oncol | Demonstrated benefit of intensified VAC in local/regional embryonal RMS; VAC confirmed as standard |
| [12654440](https://pubmed.ncbi.nlm.nih.gov/12654440/) | 2003 | Retrospective Cohort | Int J Radiat Oncol | Assessed radiation volume influence on outcome in pediatric parameningeal RMS treated with VAC-based chemotherapy |

**Rationale:**
Parameningeal RMS is a high-risk anatomical subgroup with a risk of intracranial extension. Dactinomycin — as the intercalating backbone of VAC — inhibits RNA synthesis in rapidly proliferating RMS cells and acts as a radiosensitizer, which is particularly important for this site where concurrent radiotherapy is standard. Two completed Phase 3 RCTs (IRS-IV and COG D9803) directly evaluated VAC in populations that included parameningeal RMS patients, establishing Level 1 evidence. Evidence is absent for this precise subtype only due to its rarity, not due to a lack of mechanistic rationale.

**To proceed:**
- Confirm current standard-of-care alignment with IRS/COG/EpSSG guidelines for parameningeal RMS
- Assess whether any Taiwan pediatric oncology centers treat this subtype and what protocol they follow
- Review Dactinomycin procurement pathways given its absence from the Taiwan market (import/compassionate use channel required)
- Ensure hepatotoxicity monitoring plan for pediatric patients per PMID 15143082 guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

