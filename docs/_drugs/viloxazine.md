---
layout: default
title: Viloxazine
parent: 僅模型預測 (L5)
nav_order: 1291
evidence_level: L5
indication_count: 10
---

# Viloxazine
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

# Viloxazine: From Not Marketed to Attention-Deficit/Hyperactivity Disorder (ADHD)

## One-Sentence Summary

Viloxazine (DrugBank DB09185) has no marketing authorization or approved indication on file in this jurisdiction — it is currently listed as "Not Marketed" with zero registered licenses.
The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**, a use already supported by **14 clinical trials** and **20 publications**, including multiple completed Phase 3 RCTs. Notably, the extended-release formulation (Qelbree®/SPN-812) is already FDA-approved for ADHD in the US market — this prediction largely confirms an established indication rather than proposing a novel one for this molecule globally.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file (drug not marketed in this jurisdiction; 0 licenses) |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (per this dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: Ranks 2–9 of the TxGNN output (faciodigitogenital syndrome, Creutzfeldt-Jakob disease, chondromyxoid fibroma, X-linked adrenoleukodystrophy, etc.) have no clinical trial or literature support (Evidence Level L4–L5, decision stage S0–S1) and are excluded from this report as likely knowledge-graph noise. Rank 10 (ADHD, inattentive type) is a subtype of the rank-1 indication and shares the same evidentiary base.*

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record is not available for this entry (flagged as a High-severity data gap in the evidence pack, DG002). However, the supporting literature and trial evidence consistently describe viloxazine as a **selective norepinephrine reuptake inhibitor (NRI)** with additional **5-HT2B receptor antagonism and 5-HT2C receptor agonism**. This dual noradrenergic/serotonergic profile maps directly onto the prevailing ADHD pathophysiology hypothesis of prefrontal cortical norepinephrine/dopamine signaling deficits.

This is not a speculative repurposing case in the traditional sense: the extended-release formulation of viloxazine (Qelbree®, SPN-812) has already received FDA approval in the US for ADHD in both pediatric and adult populations. The "Not Marketed" status recorded in this dataset most likely reflects the absence of a local marketing authorization in this specific jurisdiction, not a lack of global regulatory validation. The TxGNN prediction therefore aligns with, rather than diverges from, real-world regulatory precedent — the primary open question is local market entry and jurisdiction-specific labeling, not proof-of-concept efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03247556](https://clinicaltrials.gov/study/NCT03247556) | Phase 3 | Completed | 297 | High-dose (400/600 mg) pivotal RCT in adolescents (12–17y) with ADHD |
| [NCT03247530](https://clinicaltrials.gov/study/NCT03247530) | Phase 3 | Completed | 477 | Low-dose (100/200 mg) pivotal RCT in children (6–11y) with ADHD |
| [NCT03247517](https://clinicaltrials.gov/study/NCT03247517) | Phase 3 | Completed | 310 | Low-dose (200/400 mg) pivotal RCT in adolescents with ADHD |
| [NCT04016779](https://clinicaltrials.gov/study/NCT04016779) | Phase 3 | Completed | 374 | Flexible-dose (200–600 mg) RCT in adults (18–65y); key trial supporting adult ADHD approval |
| [NCT03247543](https://clinicaltrials.gov/study/NCT03247543) | Phase 3 | Completed | 313 | High-dose (200/400 mg) pivotal RCT in children with ADHD |
| [NCT02633527](https://clinicaltrials.gov/study/NCT02633527) | Phase 2 | Completed | 222 | Dose-ranging, 5-arm RCT establishing efficacious dose range in children |
| [NCT01107496](https://clinicaltrials.gov/study/NCT01107496) | Phase 1/2 | Completed | 52 | Early immediate-release formulation safety/efficacy proof-of-concept in adults |
| [NCT04781140](https://clinicaltrials.gov/study/NCT04781140) | Phase 4 | Recruiting | 286 | Post-marketing RCT in preschool children (4–5y), extending age indication |
| [NCT04786990](https://clinicaltrials.gov/study/NCT04786990) | Phase 4 | Completed | 96 | Open-label safety trial of viloxazine co-administered with psychostimulants |
| [NCT04143217](https://clinicaltrials.gov/study/NCT04143217) | Phase 3 | Completed | 159 | Open-label extension study of long-term safety/efficacy in adults |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35896943](https://pubmed.ncbi.nlm.nih.gov/35896943/) | 2022 | RCT | CNS Drugs | Pivotal Phase 3 RCT confirming efficacy and safety of viloxazine ER in adults with ADHD |
| [37166701](https://pubmed.ncbi.nlm.nih.gov/37166701/) | 2023 | Systematic Review/Meta-analysis | CNS Drugs | Meta-analysis of nonstimulant ADHD treatments in adults, including viloxazine |
| [38137075](https://pubmed.ncbi.nlm.nih.gov/38137075/) | 2023 | Systematic Review/Meta-analysis | Brain Sciences | Pooled efficacy/safety analysis of viloxazine ER in children and adolescents |
| [35615643](https://pubmed.ncbi.nlm.nih.gov/35615643/) | 2022 | Systematic Review/Meta-analysis | J Cent Nerv Syst Dis | Meta-analysis of RCTs supporting FDA approval of viloxazine ER for pediatric ADHD |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Network Meta-analysis | J Psychiatr Res | Bayesian network meta-analysis comparing monoamine reuptake inhibitors, incl. viloxazine, in ADHD |
| [41123831](https://pubmed.ncbi.nlm.nih.gov/41123831/) | 2025 | Review | CNS Drugs | Review of viloxazine ER pharmacology and clinical use in adult ADHD |
| [34975586](https://pubmed.ncbi.nlm.nih.gov/34975586/) | 2021 | Review | Frontiers in Psychiatry | Overview of viloxazine's FDA approval pathway and 4 supporting Phase 3 trials |
| [38502148](https://pubmed.ncbi.nlm.nih.gov/38502148/) | 2024 | Review | Expert Rev Neurother | Viloxazine ER as an emerging nonstimulant treatment in children/adolescents |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Review | American Family Physician | General clinical review of adult ADHD diagnosis and treatment landscape |
| [37228994](https://pubmed.ncbi.nlm.nih.gov/37228994/) | 2023 | Review | Ann Med Surg | Comprehensive review of adult ADHD epidemiology and treatment options |

---

## US Market Information

No marketing authorizations are currently on file for viloxazine in this jurisdiction (0 licenses/NDAs registered, market status: Not Marketed). No product name, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this dataset (flagged as a Blocking data gap, DG001 — TFDA-equivalent label warnings/contraindications require retrieval and parsing before any S1 safety assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence Level L1 is met — five completed Phase 3 RCTs (n=297 to 477) plus supporting Phase 2, Phase 1/2, and Phase 4 trials, and 20 publications including systematic reviews and meta-analyses, consistently support viloxazine ER's efficacy and safety in ADHD across pediatric, adolescent, and adult populations. This is further reinforced by the fact that the drug already holds FDA approval for this indication in the US as Qelbree®. However, local regulatory groundwork (label data, MOA record, market authorization) is entirely absent, which prevents an unconditional "Go."

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings/contraindications) — Blocking gap (DG001)
- Formal DrugBank mechanism-of-action record — High-priority gap (DG002)
- Confirmation of local marketing authorization pathway/status and NDA documentation
- A local drug-drug interaction and safety monitoring plan, given the current "not found" DDI query status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

