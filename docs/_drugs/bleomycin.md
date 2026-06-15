---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Bleomycin: From Hodgkin's Lymphoma to Reticulum Cell Sarcoma (Aggressive Non-Hodgkin's Lymphoma)

## One-Sentence Summary

Bleomycin is a glycopeptide cytotoxic antibiotic established globally as a cornerstone of Hodgkin's lymphoma (ABVD regimen) and germ cell tumor (BEP regimen) treatment, though it currently holds no marketing authorization in Taiwan. The TxGNN model identified **6 new predicted indications**, with **Reticulum Cell Sarcoma** (equivalent to modern aggressive Non-Hodgkin's Lymphoma/DLBCL) demonstrating the strongest evidence base — **3 completed Phase 3 RCTs** (combined n=487) and **20 publications** directly supporting bleomycin-containing regimens. Notably, the top-scoring TxGNN prediction (Cauda Equina Neoplasm, 99.30%) carries only model-level evidence (L5) with no clinical trial support, illustrating that TxGNN rank does not always correspond to clinical actionability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hodgkin's Lymphoma / Germ Cell Tumors (established global use; no Taiwan license on record) |
| Predicted New Indication (Top Evidence) | Reticulum Cell Sarcoma / Aggressive Non-Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.14% (Rank #3 by TxGNN; Rank #1 by evidence strength) |
| Evidence Level | **L1** — 3 completed Phase 3 RCTs (n=487 total) |
| Taiwan Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Proceed with Guardrails** |

---

## Multi-Indication Prediction Summary

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|----------------|----------------|
| 1 | Cauda Equina Neoplasm | 99.30% | L5 | Hold |
| 2 | Adult Astrocytic Tumour | 99.28% | L3 | Research Question |
| **3** | **Reticulum Cell Sarcoma** | **99.14%** | **L1** | **Proceed with Guardrails** |
| 4 | Primary Pulmonary Lymphoma | 99.10% | L3 | Proceed with Guardrails |
| 5 | Pulmonary Blastoma | 99.04% | L4 | Hold |
| 6 | Well-differentiated Fetal Adenocarcinoma of the Lung | 99.03% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Although the DrugBank mechanism of action record was not retrieved in this data pull (marked as a high-severity data gap), bleomycin's pharmacology is extensively documented in the published literature. Bleomycin is a glycopeptide antibiotic that chelates ferrous iron (Fe²⁺) and activates molecular oxygen to generate reactive oxygen species, causing DNA single- and double-strand breaks. This cytotoxic effect is most pronounced during the G2/M phase of the cell cycle. Rapidly proliferating cells with high mitotic index — the defining hallmark of aggressive lymphomas — are therefore particularly vulnerable to this mechanism.

Reticulum cell sarcoma, now reclassified under modern oncological nomenclature as Diffuse Large B-Cell Lymphoma (DLBCL) or aggressive Non-Hodgkin's Lymphoma (NHL), shares the same lymphoid cell lineage as Hodgkin's lymphoma, bleomycin's most widely established original indication. The biological rationale is direct: both disease types involve clonally expanded lymphoid cells with high mitotic activity and sensitivity to G2/M-phase arrest. This mechanistic alignment explains bleomycin's historical inclusion as a key component of multi-agent NHL regimens — including BACOD, MACOP-B, and ProMACE-CytaBOM — developed throughout the 1970s–1990s. Bleomycin's relative marrow-sparing profile, an unusual property among cytotoxic agents, further enabled its combination at full doses with myelosuppressive chemotherapy partners.

The principal limitation for current clinical development is historical displacement: modern DLBCL standard of care has evolved to R-CHOP (rituximab + cyclophosphamide, doxorubicin, vincristine, prednisone), a regimen that does not include bleomycin and achieves cure rates of approximately 60–70% in advanced disease. Any new application of bleomycin in aggressive NHL must therefore define a specific niche — the most defensible candidates being HIV-associated lymphoma (where Phase 3 evidence is directly available), rituximab-ineligible patients, or combination backbone exploration in resource-limited settings.

---

## Clinical Trial Evidence

*Primary focus: Reticulum Cell Sarcoma / Aggressive Non-Hodgkin's Lymphoma*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005867](https://clinicaltrials.gov/study/NCT00005867) | Phase 3 | Completed | 310 | Largest RCT: CHOP vs PMitCEBO (bleomycin-containing) in good-risk aggressive NHL; direct head-to-head comparison of bleomycin regimen vs standard therapy |
| [NCT00002835](https://clinicaltrials.gov/study/NCT00002835) | Phase 3 | Completed | 116 | Randomized comparison of early intensification vs alternating triple therapy (bleomycin-containing) for poor-prognosis intermediate-grade/immunoblastic lymphoma |
| [NCT00002565](https://clinicaltrials.gov/study/NCT00002565) | Phase 3 | Completed | 61 | ATT (alternating triple therapy, bleomycin-containing) vs CHOP in intermediate-grade/immunoblastic NHL (International Index 2–5) |
| [NCT00003110](https://clinicaltrials.gov/study/NCT00003110) | Phase 2 | Completed | 5 | Direct test: 72-hour continuous infusion bleomycin as sole salvage agent in AIDS-related and immunocompetent NHL; bleomycin as the only study drug |
| [NCT00002524](https://clinicaltrials.gov/study/NCT00002524) | Phase 2 | Completed | 46 | Combination chemotherapy including bleomycin in AIDS-related lymphoma; completed with HIV-specific population context |
| [NCT00002571](https://clinicaltrials.gov/study/NCT00002571) | Phase 2 | Completed | 52 | ProMACE-CytaBOM (bleomycin-containing) combined with AZT and G-CSF in HIV-associated NHL |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | Completed | 20 | Sequential immunosuppression reduction + interferon α + ProMACE-CytaBOM for post-cardiac-transplant lymphoproliferative disease |
| [NCT00057811](https://clinicaltrials.gov/study/NCT00057811) | Phase 2 | Completed | 97 | Rituximab + rasburicase added to LMB/FAB chemotherapy in pediatric advanced B-cell leukemia/lymphoma; bleomycin component assessed for added toxicity |
| [NCT00031902](https://clinicaltrials.gov/study/NCT00031902) | Phase 1 | Unknown | N/A | Rituximab + PVB (cisplatin, vinblastine, bleomycin) in HIV-related NHL; Phase 1 dose-finding with rituximab addition |
| [NCT00032149](https://clinicaltrials.gov/study/NCT00032149) | Phase 1/2 | Unknown | 30 | PMitCEBO + G-CSF (bleomycin-containing) in good-prognosis HIV-related lymphoma; status unknown, limits current citability |

---

## Literature Evidence

*Primary focus: Reticulum Cell Sarcoma / Aggressive Non-Hodgkin's Lymphoma*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1699653](https://pubmed.ncbi.nlm.nih.gov/1699653/) | 1990 | RCT | Cancer | CALGB 7851: randomized comparison of bleomycin addition and high-dose MTX to CHOP in DLCL and other NHL (n=274); quantified bleomycin contribution within multi-agent backbone |
| [4109401](https://pubmed.ncbi.nlm.nih.gov/4109401/) | 1972 | Prospective Clinical Study | BMJ | Bleomycin monotherapy in 22 reticulum cell sarcoma patients (among 100 total lymphoma patients); response rate documented; established bone marrow-sparing profile enabling combination use |
| [7680764](https://pubmed.ncbi.nlm.nih.gov/7680764/) | 1993 | Retrospective Cohort | N Engl J Med | Landmark SWOG trial: CHOP equivalent to 3rd-generation regimens including ProMACE-CytaBOM (bleomycin-containing) in advanced NHL; established CHOP as standard — bleomycin regimens not inferior |
| [14962711](https://pubmed.ncbi.nlm.nih.gov/14962711/) | 2004 | Retrospective Cohort | Eur J Cancer | 3 EORTC randomized trials (n=936, median follow-up 8.7 years): CHVmP/BV (bleomycin + vincristine mid-interval) vs CHVmP and other regimens; long-term efficacy data for bleomycin in aggressive NHL |
| [15934513](https://pubmed.ncbi.nlm.nih.gov/15934513/) | 2005 | Clinical Perspective Review | Oncology | GELA 20-year experience with aggressive NHL and DLBCL including bleomycin-containing regimens; charts evolution toward R-CHOP and defines residual indication space |
| [12967352](https://pubmed.ncbi.nlm.nih.gov/12967352/) | 2003 | Review | Clinical Evidence | Systematic evidence review of NHL treatment options including bleomycin-containing regimens vs standard CHOP |
| [6205233](https://pubmed.ncbi.nlm.nih.gov/6205233/) | 1984 | Comprehensive Review | Med Clin North Am | Foundation review of NHL biology and chemotherapy pharmacology; contextualizes bleomycin's historical role in combination regimens |
| [37294956](https://pubmed.ncbi.nlm.nih.gov/37294956/) | 2023 | Narrative Review | Hematol Oncol | Lymphoma in pregnancy: ABVD (bleomycin-containing) safety and efficacy in high-risk special populations; supports use after first trimester |
| [17683387](https://pubmed.ncbi.nlm.nih.gov/17683387/) | 2007 | Case Report | J Dermatol | VNCOP-B (bleomycin-containing 3rd-generation regimen) achieved complete remission in cutaneous ALCL relapsed after CHOP; illustrates salvage potential in CD30-positive aggressive lymphoma |
| [1688927](https://pubmed.ncbi.nlm.nih.gov/1688927/) | 1990 | Retrospective Cohort | J Clin Oncol | Stages IE/IIE gastric NHL treated without gastrectomy using chemo-radiation with bleomycin-containing regimens (n=34); organ-preservation efficacy data in extranodal aggressive NHL |

---

## Taiwan Market Information

Bleomycin currently holds **no marketing authorization in Taiwan** (0 licenses on record). It is not marketed through any registered dosage form or route. Bleomycin is available internationally as an established antineoplastic agent — approved by the US FDA since 1973 (originally as Blenoxane) for Hodgkin's disease, testicular carcinoma, and squamous cell carcinoma, and used across global oncology centers in combination regimens. Any Taiwan application would require a complete regulatory submission.

---

## Cytotoxicity

Bleomycin meets all three antineoplastic classification criteria: it is a glycopeptide cytotoxic antibiotic; its established indications include lymphoma and germ cell malignancies; and it belongs to the conventional cytotoxic drug category.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional Cytotoxic — DNA-damaging glycopeptide antibiotic (non-intercalating mechanism) |
| Myelosuppression Risk | **Low** — Bleomycin is notable for bone marrow-sparing; myelosuppression is not the dose-limiting toxicity and this property is a key reason for its use in combination regimens |
| Emetogenicity Classification | Low |
| Primary Toxicity Concern | **Pulmonary toxicity (bleomycin-induced pneumonitis → fibrosis)** — cumulative dose-dependent; standard ceiling ≤400 units lifetime; risk amplified by advanced age, prior lung disease, renal impairment (CrCl < 50 mL/min), concurrent G-CSF use, and high FiO₂ exposure during anesthesia |
| Secondary Toxicities | Dermatological reactions (flagellate erythema, hyperpigmentation, Raynaud's phenomenon); acute febrile/anaphylactoid reactions (test dose of 1–2 units recommended before first full dose, especially in lymphoma patients) |
| Monitoring Items | Baseline and serial pulmonary function tests (DLCO, FVC), chest X-ray or HRCT at regular intervals, cumulative dose tracking per patient, serum creatinine/eGFR (dose adjustment required in renal impairment) |
| Handling Protection | Required — full cytotoxic drug handling protocols apply (closed-system transfer devices, appropriate PPE, dedicated preparation area) |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No Taiwan-specific prescribing information or drug interaction data was retrieved in this evaluation cycle. Both the key warnings and contraindications fields returned as data gaps. Given bleomycin's well-characterized pulmonary toxicity profile, consultation of a current reference (e.g., US FDA label, WHO Essential Medicines formulary) is strongly recommended before clinical use.

---

## Conclusion and Next Steps

### Reticulum Cell Sarcoma / Aggressive NHL

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs (NCT00005867 n=310, NCT00002835 n=116, NCT00002565 n=61) directly comparing bleomycin-containing regimens in aggressive Non-Hodgkin's Lymphoma provide Level 1 evidence — the highest in this multi-indication evaluation — with bleomycin's mechanistic fit to rapidly proliferating lymphoid cells well-established.

**To proceed, the following is needed:**

- **Niche definition vs. R-CHOP**: Clearly specify the target patient subgroup (HIV-associated NHL, rituximab-contraindicated patients, or salvage setting) where bleomycin adds value beyond current R-CHOP standard of care
- **Pulmonary toxicity risk management plan**: Mandatory baseline DLCO, structured monitoring schedule, and pre-defined discontinuation criteria (DLCO drop ≥ 15%, new infiltrates on imaging)
- **Taiwan regulatory pathway**: Full NDA/IND dossier required; leverage existing international approval data (US FDA, EMA) to support bridging application
- **MOA documentation**: Retrieve formal DrugBank/pharmacological record to complete mechanism submission requirements
- **Taiwan package insert / safety document**: TFDA pharmacovigilance submission with local safety monitoring plan

---

### Hold Decisions for Remaining 5 Indications

| Indication | Reason for Hold |
|------------|-----------------|
| **Cauda Equina Neoplasm** (L5) | TxGNN score reflects indirect graph linkage (lymphoma CNS invasion pathway), not direct efficacy signal; poor blood-brain/spinal barrier penetration (CSF/plasma ratio < 0.05); primary histotypes (schwannoma, ependymoma) are not bleomycin-sensitive; no trials or direct literature |
| **Adult Astrocytic Tumour** (L3) | 1970–1990s Phase 2 data superseded by Stupp protocol (temozolomide + radiotherapy); BBB penetration remains unresolved barrier; intratumoral delivery concept (PMID 12416544) warrants literature-level interest only |
| **Primary Pulmonary Lymphoma** (L3) | Mechanistically plausible for HL-type PPL but bleomycin accumulates in lung tissue (low bleomycin hydrolase) — creating a dual-edged risk profile where therapeutic and toxic pulmonary exposure co-occur; no PPL-specific trials |
| **Pulmonary Blastoma** (L4) | Evidence restricted to the rare germ cell differentiation subtype (bleomycin logic borrowed from BEP); the majority of pulmonary blastomas lack germ cell features; only case-report level data (n=2) |
| **Well-differentiated Fetal Adenocarcinoma of the Lung** (L5) | No clinical trials or literature; adenocarcinoma histology is not bleomycin-sensitive; Wnt/β-catenin–driven biology has no established link to bleomycin sensitivity; compounded by high pulmonary toxicity risk |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

