---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 1043
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Phenytoin: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Phenytoin is a classic hydantoin-class anticonvulsant, long used for seizure control. The TxGNN model's highest-scoring prediction ("trigeminal nerve neoplasm") was flagged by the underlying evidence review as a likely false positive with no plausible antineoplastic mechanism, so this report instead focuses on the model's next-best, evidence-supported candidate: **Trigeminal Neuralgia**, which is backed by **1 completed clinical trial** and **19 supporting publications**, including a European Academy of Neurology guideline.

> **Note on candidate selection**: TxGNN's #1-ranked prediction (trigeminal nerve neoplasm, score 99.99%) was reviewed and judged a pseudo-positive pairing — the retrieved literature actually concerns trigeminal neuralgia and Sturge-Weber syndrome, not tumour biology, and phenytoin has no known antineoplastic mechanism. Ranks #2–#8 (audiogenic seizures, startle epilepsy, micturition/eating/orgasm/thinking/reading-induced seizures) are all rare reflex-epilepsy subtypes with only preclinical animal-model or case-report support (L4–L5, Hold/Research Question). Rank #9, **trigeminal neuralgia**, is the only candidate with a completed prospective clinical trial and guideline-level literature, and is therefore the focus of this evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this evidence pack (drug is unmarketed locally); established clinical use is seizure/epilepsy control |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.97% (rank 1399) |
| Evidence Level | L2 |
| Market Status | ✗ Not Marketed (0 active licenses) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation was not available in this evidence pack (marked as a data gap). Based on well-established pharmacology, phenytoin is a voltage-gated sodium channel blocker that stabilizes hyperexcitable neuronal membranes and suppresses high-frequency repetitive firing — the same mechanism underlying its efficacy in epilepsy.

Trigeminal neuralgia is characterized by paroxysmal, high-frequency ectopic discharges in the trigeminal ganglion/root entry zone, a pathophysiology mechanistically analogous to epileptic hyperexcitability. This is why carbamazepine and oxcarbazepine — sodium channel blockers structurally related to phenytoin — are first-line therapies for trigeminal neuralgia. Phenytoin's same channel-blocking action provides a strong mechanistic rationale for its use, and it is already established in neurology practice as an intravenous rescue treatment for acute trigeminal neuralgia exacerbations when oral first-line agents are impractical (e.g., during dehydration or inability to swallow).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Completed | 15 | Prospective systematic study of IV phenytoin as acute rescue treatment for exacerbations of trigeminal neuralgia, addressing the clinical gap when oral first-line agents (carbamazepine/oxcarbazepine) cannot be used during severe flares. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | EAN clinical practice guideline on trigeminal neuralgia diagnosis and management |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview of TN pathophysiology and pharmacological treatment mechanisms |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | Journal of Pain Research | Comparative review of phenytoin vs. carbamazepine evidence base in TN |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort | Cephalalgia | Retrospective analysis of 144 cases: IV lacosamide and phenytoin for acute TN exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Case series | Headache | Retrospective cohort on IV phenytoin as acute rescue treatment for TN crisis |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | Clinical overview of TN diagnosis, mechanism, and anticonvulsant-based treatment |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clinical Evidence | Summary of TN clinical presentation and evidence-based treatment options |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed prospective clinical trial plus a retrospective cohort of 144 cases and guideline-level literature support intravenous phenytoin as an established off-label rescue therapy for acute trigeminal neuralgia exacerbations, consistent with its sodium-channel-blocking mechanism shared with first-line agents (carbamazepine/oxcarbazepine). Evidence level is L2 — sufficient to proceed cautiously, but not yet supported by a dedicated randomized controlled trial.

**To proceed, the following is needed:**
- TFDA-approved package insert (warnings, contraindications) — currently a **Blocking** data gap preventing formal safety (S1) evaluation
- Confirmed DrugBank/formal MOA documentation
- Local market access assessment, since the drug currently holds 0 active licenses (未上市/Not Marketed) in this jurisdiction
- Cardiac/hemodynamic monitoring protocol for IV administration, given phenytoin's narrow therapeutic index and known infusion-related risks (arrhythmia, hypotension)
- A prospective RCT comparing IV phenytoin to standard-of-care rescue options to upgrade evidence level beyond L2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

