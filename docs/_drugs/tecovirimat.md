---
layout: default
title: Tecovirimat
parent: 僅模型預測 (L5)
nav_order: 623
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: From Smallpox to Human Orthopoxvirus Infection (Mpox)

## One-Sentence Summary

Tecovirimat (TPOXX®) is an antiviral developed under the US biodefense program and FDA/EMA-approved for treatment of smallpox, acting by inhibiting the highly conserved orthopoxvirus VP37 (F13) envelope protein to block systemic viral spread.
The TxGNN model predicts it may be effective for **human infection by orthopoxvirus** (including mpox/monkeypox), with **20 publications** currently supporting this direction — including a landmark **Phase 3 RCT (PALM007, NEJM 2025)**.
However, the model's top-5 predicted indications (hordeolum, Vibrio infection, Klebsiella infection, noma, lumpy skin disease) are mechanistically incompatible false positives; this report focuses on the clinically meaningful indication at rank 6 (Evidence Level L1).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Smallpox (variola virus infection) — FDA-approved July 2018, EMA-approved January 2022 (Animal Rule) |
| Predicted New Indication | Human infection by orthopoxvirus (mpox/monkeypox) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 (Phase 3 RCT: PALM007, DRC, 2025) |
| US Market Status | Not found in database query (note: FDA NDA 208627 confirmed via literature) |
| Number of NDAs | 0 (database query result — see US Market Information section) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature, tecovirimat (ST-246) selectively inhibits the orthopoxvirus VP37 protein (also called F13), a phospholipase-like envelope wrapping protein essential for the formation of extracellular enveloped virions (EEV). By blocking EEV biogenesis, tecovirimat prevents systemic viral dissemination within the host — a mechanism distinct from nucleoside analogues such as cidofovir or brincidofovir. Critically, the VP37 target sequence is >95% conserved across all Orthopoxvirus species (variola, monkeypox, vaccinia, cowpox, camelpox), providing a strong mechanistic basis for cross-species activity.

Smallpox and mpox (monkeypox) are both caused by members of the Orthopoxvirus genus sharing near-identical replication machinery. The FDA's 2018 Animal Rule approval for smallpox was itself supported by efficacy data from vaccinia and monkeypox animal models — meaning mpox has always been an implicit part of the scientific rationale. This makes "human infection by orthopoxvirus" a mechanistically sound and well-precedented predicted indication rather than a novel extrapolation.

**Important clinical caveat**: Two recent Phase 3 RCTs — the STOMP trial (Clade IIb MPXV, 2024) and the PALM007 trial (Clade I MPXV in the DRC, PMID 40239067, 2025) — both failed to demonstrate superiority of tecovirimat over placebo for the primary endpoint of lesion healing time. Emerging resistance mutations in the F13 gene (PMID 39939832) further complicate the clinical picture. These findings do not negate mechanistic validity but indicate that unselected patient populations may not benefit; careful definition of target subgroups (immunocompromised, severe/disseminated disease) is essential.

---

## TxGNN Prediction Credibility Assessment

The top-5 TxGNN predictions and two others are **false positives** and should not be pursued. They share a hallmark of graph-based scoring saturation: clustered scores in a narrow 0.9961–0.9966 band with no supporting clinical or mechanistic evidence.

| Rank | Indication | Evidence Level | Reason for Rejection |
|------|-----------|---------------|---------------------|
| 1 | Hordeolum (stye) | L5 / Hold | Staphylococcal bacterial eye infection; tecovirimat has zero antibacterial activity |
| 2 | Vibrio infectious disease | L5 / Hold | Gram-negative bacterial infection; mechanism is completely unrelated |
| 3 | Klebsiella infectious disease | L5 / Hold | Gram-negative bacterial sepsis; scoring saturation artifact |
| 4 | Noma | L5 / Hold | Polymicrobial bacterial oral necrotizing infection; no mechanism |
| 5 | Lumpy skin disease | L5 / Hold | Capripoxvirus disease in cattle — non-human indication, outside drug repurposing scope |
| 7 | Idiopathic severe pneumococcemia | L5 / Hold | Pneumococcal bacteremia; completely unrelated mechanism |
| 10 | Phlebotomus fever | L5 / Hold | Caused by an RNA phlebovirus; tecovirimat exclusively targets DNA poxviruses |

The three remaining predictions with some clinical basis are: **human infection by orthopoxvirus** (rank 6, L1, Proceed with Guardrails), **vaccinia** (rank 8, L2, Proceed with Guardrails), and **coinfection** (rank 9, L3 — specifically mpox/HIV coinfection, Research Question).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04957485](https://clinicaltrials.gov/study/NCT04957485) | Phase 2 | Active, Not Recruiting | 100 | Double-blind RCT evaluating TPOXX® + JYNNEOS® smallpox vaccine vs. placebo + JYNNEOS®; assesses whether concurrent tecovirimat administration impairs vaccine immunogenicity — directly relevant to orthopoxvirus post-exposure prophylaxis scenarios |
| [NCT05380752](https://clinicaltrials.gov/study/NCT05380752) | N/A | No Longer Available | N/A | Expanded Access Protocol for IV TPOXX (10 mg/mL) in patients with confirmed or suspected orthopoxvirus infection unable to take oral formulation, or with significant vaccinia adverse reactions; terminated following resolution of the mpox public health emergency |
| [NCT05976100](https://clinicaltrials.gov/study/NCT05976100) | Phase 1 | Completed | 90 | Safety, tolerability, and pharmacokinetics of NIOCH-14 (a Russian-developed anti-poxvirus compound distinct from tecovirimat); indirect comparator only, not directly applicable |

> **Note**: The PALM007 Phase 3 RCT (Clade I MPXV, DRC, 2025) and STOMP Phase 3 trial (Clade IIb MPXV) were not captured in the ClinicalTrials.gov query but are documented in the literature evidence below as the highest-quality clinical data currently available.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40239067](https://pubmed.ncbi.nlm.nih.gov/40239067/) | 2025 | Phase 3 RCT | N Engl J Med | PALM007 trial: tecovirimat vs. placebo in Clade I MPXV (Democratic Republic of Congo); primary endpoint (lesion healing time) not met; limited effect on mortality — major evidence update challenging mpox efficacy |
| [32882158](https://pubmed.ncbi.nlm.nih.gov/32882158/) | 2021 | Comprehensive Review | Expert Rev Anti-Infective Ther | Definitive overview of tecovirimat: mechanism (VP37 inhibition), FDA Animal Rule approval pathway, stockpiling strategy, and rationale for expanded anti-orthopoxvirus applications including mpox |
| [30120738](https://pubmed.ncbi.nlm.nih.gov/30120738/) | 2018 | Drug Approval Summary | Drugs | First global approval of tecovirimat for smallpox; clinical pharmacology, safety from healthy volunteer trials, and regulatory pathway |
| [40378361](https://pubmed.ncbi.nlm.nih.gov/40378361/) | 2025 | Mechanistic Review | PLoS Pathogens | From discovery to mechanistic insights: F13/VP37 protein structure, poxvirus inhibition mechanism, and implications of emerging resistance |
| [39939832](https://pubmed.ncbi.nlm.nih.gov/39939832/) | 2025 | Structural Study | Nature Microbiology | Crystal structure of F13 homodimer bound to tecovirimat; identifies resistance mutation sites and structural basis for drug action — informs next-generation design |
| [39707867](https://pubmed.ncbi.nlm.nih.gov/39707867/) | 2024 | Systematic Review | J Med Virology | Systematic review of tecovirimat effectiveness in mpox (2022 outbreak); evaluates real-world evidence across high-risk populations including people living with HIV |
| [39401235](https://pubmed.ncbi.nlm.nih.gov/39401235/) | 2024 | Narrative Review | JAMA | Comprehensive review of mpox clinical presentation, diagnostics, and treatment; covers STOMP trial context, and discusses second WHO PHEIC declaration (August 2024) |
| [36374026](https://pubmed.ncbi.nlm.nih.gov/36374026/) | 2022 | Review | Antimicrob Agents Chemother | Tecovirimat for human monkeypox virus: mechanism, animal model efficacy, human safety profile, and rationale for off-label use during the 2022 global outbreak |
| [37828248](https://pubmed.ncbi.nlm.nih.gov/37828248/) | 2023 | Experimental | Nature Microbiology | Human iPSC-derived skin organoid model of MPXV infection; keratinocytes support active replication; provides a platform for drug efficacy testing |
| [40210872](https://pubmed.ncbi.nlm.nih.gov/40210872/) | 2025 | Experimental | Signal Transduct Target Ther | Novel brincidofovir derivatives show superior anti-orthopoxvirus potency compared to tecovirimat; contextualizes tecovirimat's limitations and positions next-generation alternatives |

---

## US Market Information

The current database query returned 0 FDA NDA records for tecovirimat. Based on published literature, the following approvals are documented:

| Authorization | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 208627† | TPOXX® | Oral capsule (200 mg) | Treatment of smallpox disease caused by variola virus in adults and pediatric patients weighing ≥13 kg; FDA approved July 13, 2018 |
| NDA 214771† | TPOXX® | IV injection (200 mg/20 mL) | Treatment of smallpox in patients unable to take oral formulation; FDA approved May 2022 |
| EU/1/22/1623† | TECOVIRIMAT SIGA | Oral capsule / IV solution | Smallpox, mpox (monkeypox), and cowpox in adults and paediatric patients; EMA approved January 2022 |

†Records derived from published literature (PMID 30120738, PMID 32882158) and SIGA Technologies press releases; not reflected in current database query. **Database refresh is required** to populate FDA NDA records for this drug.

---

## Safety Considerations

Please refer to the package insert (FDA NDA 208627/214771) for complete safety information.

**Key drug interaction concern from literature**: Tecovirimat is a moderate CYP3A4 inducer. This is clinically significant because mpox disproportionately affects people living with HIV (PLWH), many of whom receive ritonavir-boosted protease inhibitor-based ART regimens. CYP3A4 induction by tecovirimat may reduce plasma concentrations of HIV protease inhibitors, potentially compromising HIV virologic suppression. Detailed metabolic pathway analysis for mpox/HIV co-treatment is available in PMID 37287302. The European AIDS Clinical Society (EACS) 2025 guidelines (PMID 41088922) provide a management framework for HIV/mpox co-infected patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tecovirimat has an established FDA/EMA approval for smallpox and a mechanistically sound rationale for activity against all orthopoxviruses including mpox; however, two Phase 3 RCTs (STOMP for Clade IIb and PALM007 for Clade I mpox) both failed to demonstrate superiority over placebo for lesion healing, indicating that the mechanistic case does not automatically translate to clinical benefit in unselected populations. A guardrails approach focused on specific high-risk subgroups (severe/disseminated disease, immunocompromised patients) is appropriate while awaiting subgroup and post-hoc analyses.

**To proceed, the following is needed:**
- Obtain full FDA package insert and TFDA submission dossier for complete safety and DDI data extraction
- Update regulatory database to reflect FDA NDA 208627/214771 approval records
- Define target patient subpopulation (immunocompromised, severe disease, specific viral clade) based on emerging subgroup analyses from PALM007 and STOMP trials
- Clarify CYP3A4 induction magnitude and clinical impact on ART regimens in HIV/mpox co-infected patients before any co-prescription protocol is developed
- Await results of Phase 2 RCT (NCT04957485) evaluating TPOXX® + JYNNEOS® vaccine combination for orthopoxvirus post-exposure prophylaxis
- Monitor resistance surveillance: F13 mutations conferring tecovirimat resistance (PMID 39939832) are an emerging concern requiring molecular epidemiology tracking in treatment cohorts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

