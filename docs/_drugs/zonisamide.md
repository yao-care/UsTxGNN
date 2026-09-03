---
layout: default
title: Zonisamide
parent: 僅模型預測 (L5)
nav_order: 1312
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide: From Partial-Onset Epilepsy to Absence Epilepsy

## One-Sentence Summary

Zonisamide is a broad-spectrum antiepileptic drug best known for treating partial (focal) seizures via sodium- and T-type calcium-channel blockade. Among the ten indications flagged by TxGNN, **Absence Epilepsy** stands out as the only candidate backed by substantial real-world evidence, supported by **4 clinical trials** (including a 583-patient Phase 3 head-to-head RCT) and **20 publications**, including ILAE and AAN/AES practice guidelines and a Cochrane network meta-analysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Taiwan/US license records; based on general pharmacology, zonisamide is an established anticonvulsant for partial-onset seizures) |
| Predicted New Indication | Absence Epilepsy |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, zonisamide is a benzisoxazole-derivative, broad-spectrum antiepileptic drug that blocks voltage-gated sodium channels and T-type calcium channels, with additional modulation of GABAergic/glutamatergic transmission. It has long been approved and used for focal (partial) and generalized seizures in both adults and children.

Absence epilepsy is driven by abnormal thalamocortical oscillatory circuits, in which T-type calcium channel activity in thalamic relay neurons plays a central pathophysiological role. Zonisamide's T-type calcium channel blockade maps directly onto this mechanism, making this a mechanistically direct extension of an already-approved seizure indication rather than a speculative cross-disease inference.

This mechanistic clarity is notably stronger than several other TxGNN-flagged candidates for this drug. Predictions such as Tourette syndrome and trichotillomania rely on indirect dopamine/serotonin or glutamate reasoning with zero supporting trials or literature (L5, Hold). More importantly, two high-scoring candidates — **methemoglobinemia** and **methemoglobinemia, alpha type** — should be treated as safety red flags rather than opportunities: zonisamide is a sulfonamide-class compound, and sulfonamides are a known *cause* of methemoglobinemia, not a treatment for it. This illustrates why raw TxGNN rank/score alone should never be used to prioritize candidates without evidence triage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00477295](https://clinicaltrials.gov/study/NCT00477295) | Phase 3 | Completed | 583 | Randomized, double-blind, non-inferiority trial comparing zonisamide vs. carbamazepine monotherapy in newly diagnosed partial epilepsy — the strongest direct efficacy/safety comparison available. |
| [NCT00848549](https://clinicaltrials.gov/study/NCT00848549) | Phase 3 | Completed | 295 | Long-term double-blind extension study assessing safety, tolerability, and long-term efficacy of zonisamide monotherapy in newly diagnosed partial seizures. |
| [NCT07443241](https://clinicaltrials.gov/study/NCT07443241) | N/A | Completed | 779 | Retrospective analysis of sex-related differences in status epilepticus etiology/outcomes; provides epidemiological context but is not zonisamide-specific. |
| [NCT04939675](https://clinicaltrials.gov/study/NCT04939675) | N/A | Unknown | 40 | Development/validation of an epilepsy screening questionnaire; not a treatment efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | Clinical Study | Epilepsy Research | Chart review of 45 pediatric patients with absence seizures; 51.1% achieved seizure freedom on zonisamide, directly supporting efficacy. |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | Case Series/Open Study | Epilepsy Research | Zonisamide effective in drug-resistant juvenile absence epilepsy (JAE). |
| [23350722](https://pubmed.ncbi.nlm.nih.gov/23350722/) | 2013 | Guideline/Evidence Review (ILAE) | Epilepsia | Updated ILAE evidence review of AED efficacy as initial monotherapy across seizure types and syndromes. |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES joint guideline update on efficacy and tolerability of newer AEDs for new-onset epilepsy. |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network Meta-analysis (IPD) | Cochrane Database Syst Rev | Individual-participant-data network meta-analysis of AED monotherapy across epilepsy types. |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | Clinical Study | Epileptic Disorders | Zonisamide effective and tolerable in juvenile myoclonic epilepsy, including absence seizure components. |
| [34941639](https://pubmed.ncbi.nlm.nih.gov/34941639/) | 2021 | Review | Pediatric Reports | Review of therapeutic options for childhood absence epilepsy, situating zonisamide among second-line agents. |
| [16321507](https://pubmed.ncbi.nlm.nih.gov/16321507/) | 2006 | Clinical Experience Review | Epilepsy Research | Japanese post-marketing experience across partial and generalized seizure types, including absence seizures. |
| [15043806](https://pubmed.ncbi.nlm.nih.gov/15043806/) | 2004 | Review | Curr Treat Options Neurol | Review of idiopathic generalized epilepsy management, including absence seizure treatment options. |
| [28931473](https://pubmed.ncbi.nlm.nih.gov/28931473/) | 2017 | Safety Review | Epilepsy & Behavior | Comparative review of psychiatric/behavioral side effects across older vs. newer AEDs, including zonisamide. |

---

## US Market Information

Zonisamide currently has **no license records** in this evidence pack (`market_status: Not Marketed`, `total_licenses: 0`). No NDA/product table can be generated at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications and DDI data have not yet been retrieved for this drug (see data gap remediation below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Absence epilepsy is supported by L1-level evidence — a completed 583-patient Phase 3 head-to-head RCT, ILAE and AAN/AES guideline recognition, and a Cochrane network meta-analysis — making it a credible, mechanistically direct label-expansion candidate. However, the drug is not currently marketed in this jurisdiction, and core safety documentation is still missing.

**To proceed, the following is needed:**
- Retrieve TFDA package insert (warnings/contraindications) — currently blocking S1 safety review (DG001)
- Retrieve detailed MOA documentation via DrugBank API (DG002)
- Assess regulatory filing/NDA pathway given zero existing local licenses
- Treat TxGNN's methemoglobinemia predictions (both entries) as pharmacovigilance signals, not repurposing opportunities — zonisamide's sulfonamide structure is a known risk factor for this condition, not a treatment for it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

