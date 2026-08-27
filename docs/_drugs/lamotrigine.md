---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 831
evidence_level: L5
indication_count: 9
---

# Lamotrigine
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

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Lamotrigine is a broad-spectrum anticonvulsant originally developed for epilepsy (seizure disorders) and later established for bipolar disorder. The TxGNN model, supported by pharmacological literature, predicts it may be effective for **Trigeminal Neuralgia**, with **4 clinical trials** (including 2 lamotrigine-specific completed studies) and **19 publications** currently supporting this direction.

> **Note on model ranking:** TxGNN's single highest-scoring node ("trigeminal nerve neoplasm," score 99.97%) is flagged in the evidence pack's own rationale as a likely knowledge-graph confusion with "trigeminal neuralgia" — its only supporting literature is a general neuralgia review and an unrelated tumor case report, with no lamotrigine-specific evidence (Evidence Level L5, Hold). This report instead focuses on the second-ranked, substantively evidenced candidate, **trigeminal neuralgia**, which carries real drug-specific clinical trial data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (and bipolar disorder) — per literature evidence in this pack; no TFDA license text available |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| US Market Status | Not marketed (0 licenses on record in this evidence pack) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lamotrigine is a voltage-gated sodium channel blocker that inhibits glutamate release and stabilizes neuronal membranes. According to the evidence pack's mechanistic rationale, this action can suppress abnormal discharges at the trigeminal ganglion — the same underlying mechanism exploited by carbamazepine and oxcarbazepine, the established first-line drugs for trigeminal neuralgia.

Trigeminal neuralgia and epilepsy share a common therapeutic class: both are neuronal hyperexcitability disorders responsive to sodium-channel-blocking anticonvulsants. This mechanistic overlap is why several second-generation antiepileptics, lamotrigine included, have been trialed as add-on or alternative therapy when first-line agents fail or are poorly tolerated.

This is not purely theoretical extrapolation — the European Academy of Neurology guideline (PMID 30860637, a Tier 1 guideline source) already lists lamotrigine among treatment options for TN, and two completed clinical trials (a placebo-controlled add-on study and a head-to-head Phase 2/3 comparison against carbamazepine) provide direct human evidence, albeit in small cohorts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine (Lamictal) safety and efficacy in reducing trigeminal neuralgia attacks |
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Head-to-head comparison of lamotrigine vs. carbamazepine efficacy and safety in trigeminal neuralgia |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study evaluating lamotrigine's effect on neuropathic facial pain / neuralgia |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Comparative efficacy of carbamazepine vs. oxcarbazepine in TN (background comparator trial; does not use lamotrigine) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Comparative study | Journal of the Chinese Medical Association | Companion publication to NCT00913107; evaluated efficacy/safety of lamotrigine vs. carbamazepine in TN patients |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology guideline on TN management, including pharmacotherapy recommendations |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on TN pharmacotherapy; lamotrigine noted among options beyond first-line carbamazepine/oxcarbazepine |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic review | Biomedicines | Umbrella review of drug therapies for TN and their efficacy/side-effect profiles |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview of TN pathophysiology through pharmacological treatment |
| [39365662](https://pubmed.ncbi.nlm.nih.gov/39365662/) | 2025 | Cohort | Pain | Nationwide Danish disease-trajectory study of TN comorbidities (7.2M individuals) |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical guide to TN diagnosis and management |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case report | Multiple Sclerosis and Related Disorders | Refractory TN in an MS patient successfully treated with pregabalin + lamotrigine combination |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka (Neurological Surgery) | Japanese review of TN pharmacotherapy listing lamotrigine as an off-label alternative |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Clinical evidence review | BMJ Clinical Evidence | Overview of TN diagnosis, prognosis, and treatment options |

---

## US Market Information

No FDA/regulatory license records are present in this evidence pack (`total_licenses = 0`). This is flagged as a data gap (DG001: TFDA label/warning data blocking) rather than a confirmed absence of marketing authorization — regulatory data collection for this drug should be re-verified before relying on this status.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed placebo-controlled add-on trial and a completed Phase 2/3 head-to-head trial against carbamazepine provide direct, drug-specific evidence for lamotrigine in trigeminal neuralgia, reinforced by guideline-level literature and a consistent sodium-channel-blocking mechanism shared with established TN therapies. However, both pivotal trials are small (N=20 and N=21), and no confirmatory large-scale Phase 3 RCT exists — guardrails are warranted before broader clinical application.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — currently blocking safety evaluation)
- Detailed mechanism of action data from DrugBank (DG002)
- A larger, confirmatory Phase 3 RCT in trigeminal neuralgia
- Verification of actual US/Taiwan market and licensing status, given the apparent inconsistency between "0 licenses on record" and lamotrigine's well-established clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

