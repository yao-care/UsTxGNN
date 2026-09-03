---
layout: default
title: Mechlorethamine
parent: 僅模型預測 (L5)
nav_order: 892
evidence_level: L5
indication_count: 3
---

# Mechlorethamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Mechlorethamine: From Hodgkin Lymphoma to Lymph Node Cancer

## One-Sentence Summary

Mechlorethamine (nitrogen mustard) is a classic alkylating chemotherapy agent historically used as the backbone of the MOPP regimen for Hodgkin lymphoma and as a topical gel for cutaneous T-cell lymphoma (mycosis fungoides). The TxGNN model further predicts strong relevance to **Lymph Node Cancer** (score 99.43%), a use area that substantially overlaps with the drug's established history rather than representing a wholly novel mechanism — supported by **50 matched clinical trial records** and **20 publications**, though most trials are indirect (lymphoma regimens using other agents) while the literature includes several historical RCTs of mechlorethamine-containing regimens.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma (as part of the MOPP regimen); historical topical use in cutaneous T-cell lymphoma/mycosis fungoides — no structured Taiwan/US license data available to confirm current labeling |
| Predicted New Indication | Lymph Node Cancer |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 (historical RCTs of mechlorethamine-based regimens exist for Hodgkin lymphoma; most matched ClinicalTrials.gov records are indirect) |
| US Market Status | Not marketed (no active licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available in this evidence pack. Based on known pharmacology, mechlorethamine is a bifunctional alkylating agent (the prototypical nitrogen mustard) that cross-links DNA strands and halts replication in rapidly dividing cells. It formed the backbone of the historic MOPP regimen (mechlorethamine, vincristine, procarbazine, prednisone), one of the first combination chemotherapy protocols to achieve durable remission in Hodgkin lymphoma, and a topical 0.016% gel formulation (chlormethine/mechlorethamine) is used for cutaneous T-cell lymphoma/mycosis fungoides — both malignancies of the lymphatic system.

Lymph node cancer (lymphoma broadly) is therefore mechanistically and clinically close to mechlorethamine's already-established use. The TxGNN prediction largely reinforces a decades-old, clinically validated application rather than identifying a genuinely new pharmacological pathway. This explains why the literature evidence (MOPP-regimen randomized trials) is comparatively strong, even though most matched ClinicalTrials.gov records in this pack involve adjacent but different regimens (rituximab, bendamustine, CAR-T, venetoclax, etc.) rather than mechlorethamine itself.

## Clinical Trial Evidence

*Note: none of the matched ClinicalTrials.gov records use mechlorethamine directly — they reflect the broader lymphoma/lymph-node-cancer treatment landscape retrieved by the search, not direct trials of this drug.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02005471](https://clinicaltrials.gov/study/NCT02005471) | Phase 3 | Completed | 389 | Venetoclax + rituximab vs. bendamustine + rituximab in relapsed/refractory CLL — not a mechlorethamine trial |
| [NCT02162771](https://clinicaltrials.gov/study/NCT02162771) | Phase 3 | Completed | 140 | Biosimilar rituximab (CT-P10) vs. Rituxan with CVP in advanced follicular lymphoma |
| [NCT01889069](https://clinicaltrials.gov/study/NCT01889069) | Phase 3 | Completed | 159 | Subcutaneous rituximab in untreated CD20+ DLBCL/follicular lymphoma |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | Epcoritamab + lenalidomide/rituximab vs. chemoimmunotherapy in untreated follicular lymphoma |
| [NCT00562965](https://clinicaltrials.gov/study/NCT00562965) | Phase 3 | Terminated | 29 | Inotuzumab ozogamicin + rituximab vs. investigator's choice in relapsed/refractory follicular NHL |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential autologous/haploidentical allogeneic HCT for high-risk lymphoma, myeloma, or CLL |
| [NCT00924326](https://clinicaltrials.gov/study/NCT00924326) | Phase 1/2 | Completed | 43 | Anti-CD19 CAR T-cell therapy in B-cell lymphoma |
| [NCT00974233](https://clinicaltrials.gov/study/NCT00974233) | Phase 2 | Completed | 34 | Bendamustine + rituximab induction with lenalidomide/rituximab maintenance in relapsed/refractory CLL/SLL |
| [NCT00450801](https://clinicaltrials.gov/study/NCT00450801) | Phase 2 | Completed | 22 | Rituximab + MACLO/IVAM chemotherapy in previously untreated mantle cell lymphoma |
| [NCT00911183](https://clinicaltrials.gov/study/NCT00911183) | Phase 2 | Completed | 67 | Rituximab-CHOP-type regimen in frail elderly diffuse large B-cell lymphoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3352775](https://pubmed.ncbi.nlm.nih.gov/3352775/) | 1988 | RCT | NCI Monographs | EORTC H5 trial: mantle irradiation + mechlorethamine/vincristine/procarbazine/prednisone (MVPP) vs. total nodal irradiation in stage I–II Hodgkin's disease |
| [7509381](https://pubmed.ncbi.nlm.nih.gov/7509381/) | 1994 | RCT | J Clin Oncol | Randomized comparison of MOPP alone vs. MOPP/ABVD alternation in stage IIIB/IV Hodgkin's disease |
| [2436740](https://pubmed.ncbi.nlm.nih.gov/2436740/) | 1987 | Cohort | Cancer | MOPP chemotherapy with/without involved-field radiotherapy in 37 children with Hodgkin's disease |
| [7540419](https://pubmed.ncbi.nlm.nih.gov/7540419/) | 1995 | Cohort | Annals of Oncology | Hybrid MOPP/ABVD plus radiotherapy in advanced Hodgkin's disease |
| [35393251](https://pubmed.ncbi.nlm.nih.gov/35393251/) | 2022 | Retrospective | Clin Lymphoma Myeloma Leuk | Chlormethine/mechlorethamine 0.016% gel as maintenance therapy in mycosis fungoides |
| [6809030](https://pubmed.ncbi.nlm.nih.gov/6809030/) | 1982 | Retrospective | Br J Dermatol | Topical mechlorethamine (HN2) among treatments in 92 cutaneous T-cell lymphoma patients |
| [24438970](https://pubmed.ncbi.nlm.nih.gov/24438970/) | 2014 | Review | J Am Acad Dermatol | Prognosis and management (part II) of mycosis fungoides/Sézary syndrome |
| [10473086](https://pubmed.ncbi.nlm.nih.gov/10473086/) | 1999 | Mechanistic | Clin Cancer Res | O6-alkylguanine-DNA alkyltransferase and resistance to alkylating agents (incl. mechlorethamine) in cutaneous T-cell lymphoma |
| [31894937](https://pubmed.ncbi.nlm.nih.gov/31894937/) | 2020 | Review | American Family Physician | General overview of lymphoma diagnosis and treatment |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Cohort | Cancer | Characteristics and outcomes of Hodgkin lymphoma involving nodal and extranodal head/neck sites |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High — nitrogen mustards are well-documented potent bone-marrow suppressants at the class level; product-specific hematologic toxicity data is not available in this evidence pack (refer to package insert) |
| Emetogenicity Classification | High (for IV formulation; class-level classification per standard oncology emetogenicity scales) |
| Monitoring Items | CBC with differential and platelets, liver and renal function, injection/application site monitoring (vesicant potential) |
| Handling Protection | Cytotoxic/vesicant drug handling precautions expected (closed-system transfer devices, PPE, spill kit); specific TFDA/DrugBank handling requirements not confirmed in this evidence pack |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (TFDA/regulatory label warnings and contraindications) prevents safety pre-screening (S1), and the drug currently has no active market licenses on record. In addition, the repurposing signal for lymph node cancer largely reconfirms mechlorethamine's already-established historical role (MOPP regimen, topical CTCL use) rather than identifying a genuinely novel mechanism, so this candidate does not require de novo efficacy proof but does require safety documentation before advancing.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — Blocking gap
- Structured mechanism-of-action data from DrugBank — High-priority gap
- Confirmation of current formulation availability (IV vs. topical gel) and market access pathway
- Drug-drug interaction profile validation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

