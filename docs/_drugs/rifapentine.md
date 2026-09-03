---
layout: default
title: Rifapentine
parent: 僅模型預測 (L5)
nav_order: 1121
evidence_level: L5
indication_count: 10
---

# Rifapentine
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

# Rifapentine: From Tuberculosis to Leprosy

## One-Sentence Summary

Rifapentine is a rifamycin-class antimycobacterial, established for the treatment of pulmonary tuberculosis. The TxGNN model predicts it may also be effective against **leprosy** (Hansen's disease), with **20 publications** — including two NEJM RCTs on single-dose post-exposure prophylaxis — currently supporting this direction, though **no dedicated clinical trials for leprosy treatment** are yet registered.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for this market (drug currently not marketed); globally known and approved (e.g., US Priftin®) for pulmonary tuberculosis |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the source registry for this record. Based on general pharmacological knowledge, rifapentine is a long-acting **rifamycin** that inhibits bacterial DNA-dependent RNA polymerase, blocking mRNA synthesis. This is the same mechanistic class as rifampicin, and its efficacy against *Mycobacterium tuberculosis* is well established.

Tuberculosis and leprosy are both caused by mycobacterial species (*M. tuberculosis* and *M. leprae* respectively), and the two organisms share highly conserved RNA polymerase targets. Rifampicin has long been a backbone drug in WHO multidrug therapy (MDT) for leprosy, and murine-model studies confirm that rifapentine has **greater bactericidal activity against *M. leprae* than rifampicin**. This mechanistic overlap directly supports the plausibility of the TxGNN prediction.

Clinically, this hypothesis has already moved beyond theory: a large NEJM randomized controlled trial (single-dose rifapentine in household contacts of leprosy patients) demonstrated protective, post-exposure prophylactic effect. This positions rifapentine's leprosy-related evidence primarily in the **prevention/post-exposure prophylaxis (PEP)** space rather than active-disease treatment, which should be considered when interpreting the strength of this signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for leprosy treatment/prevention with rifapentine as a primary indication.

*(Note: one tangential trial, [NCT00814671](https://clinicaltrials.gov/study/NCT00814671), compared rifapentine dosing for pulmonary tuberculosis and is not leprosy-relevant.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37195940](https://pubmed.ncbi.nlm.nih.gov/37195940/) | 2023 | RCT | N Engl J Med | Single-dose rifapentine showed protective effect against leprosy in household contacts of patients, building on prior rifampicin PEP data |
| [37585641](https://pubmed.ncbi.nlm.nih.gov/37585641/) | 2023 | RCT (correspondence) | N Engl J Med | Follow-up discussion/correspondence on the household-contact rifapentine PEP trial |
| [37385746](https://pubmed.ncbi.nlm.nih.gov/37385746/) | 2023 | Cohort | BMJ Open | COMBINE protocol: population-wide active case-finding plus mass drug administration (including rifamycins) for leprosy control in "hot-spot" areas |
| [38440733](https://pubmed.ncbi.nlm.nih.gov/38440733/) | 2024 | Review | Front Immunol | Overview of leprosy treatment, prevention, immune response, and rifampicin-resistance emergence |
| [40278757](https://pubmed.ncbi.nlm.nih.gov/40278757/) | 2025 | Review | Trop Med Infect Dis | Review of efficacy, safety, and feasibility of rifamycin-based post-exposure chemoprophylaxis for leprosy (WHO "Towards Zero Leprosy" context) |
| [32936818](https://pubmed.ncbi.nlm.nih.gov/32936818/) | 2020 | Preclinical | PLoS Negl Trop Dis | Mouse-footpad model: rifapentine PEP efficacy against subclinical *M. leprae* infection |
| [29071280](https://pubmed.ncbi.nlm.nih.gov/29071280/) | 2017 | Preclinical/In vitro | Mol Biol Res Commun | Molecular simulation of rifabutin/rifapentine as alternatives to rifampicin in drug-resistant leprosy |
| [30207440](https://pubmed.ncbi.nlm.nih.gov/30207440/) | 2016 | Preclinical | Indian J Leprosy | Murine-model evaluation of rifapentine (alone/combination) against rifampicin-resistant leprosy |
| [37585642](https://pubmed.ncbi.nlm.nih.gov/37585642/) | 2023 | Correspondence | N Engl J Med | Author reply to commentary on the household-contact rifapentine PEP trial |
| [33758553](https://pubmed.ncbi.nlm.nih.gov/33758553/) | 2021 | Observational | HIV/AIDS (Auckland) | Determinants of hepatotoxicity in HIV patients on high-dose rifapentine+isoniazid at a combined leprosy-TB treatment center |

---

## US Market Information

Rifapentine currently has no NDA license on file in this registry (market status: Not Marketed, 0 total licenses). No product/dosage-form data available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Phase 3-quality NEJM RCT plus supportive preclinical/mechanistic data (superior *M. leprae* bactericidal activity vs. rifampicin) justify moving forward, but the evidence base is concentrated in **single-dose post-exposure prophylaxis**, not confirmed active-disease treatment, and no dedicated interventional trials for leprosy treatment are registered.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain FDA/TFDA label warnings and contraindications before any S1 safety assessment can proceed
- Resolve **DG002**: obtain formal DrugBank MOA record to confirm mechanistic rationale documentation
- Clarify intended use case — prophylaxis (household contacts) vs. treatment of active leprosy — as these require different evidence standards
- Assess drug-drug interaction risk given rifamycin-class enzyme induction (relevant if used in leprosy patients also on other chronic therapies)
- Confirm regulatory pathway feasibility given the drug's current "Not Marketed" status in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

