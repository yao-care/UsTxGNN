---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 831
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Lamotrigine: From Epilepsy and Bipolar Disorder to Trigeminal Nerve Neoplasm (Top-Ranked Prediction Not Supported; Trigeminal Neuralgia Is the Real Lead)

## One-Sentence Summary

Lamotrigine is an antiseizure medication, described in the retrieved literature as used for seizure and bipolar mood disorders.
The top-ranked TxGNN prediction is **Trigeminal Nerve Neoplasm**, but there are **0 clinical trials** and no lamotrigine-specific publications for it, and no credible antitumour mechanism.
The graph score is most likely driven by proximity to **trigeminal neuralgia** (rank 2), which has **4 registered trials** (2 directly on target) and **18 publications** behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the retrieved US label data (literature describes seizure and bipolar disorders) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1); better-supported candidate: trigeminal neuralgia (rank 2) |
| TxGNN Prediction Score | 99.97% (trigeminal neuralgia: 99.89%) |
| Evidence Level | L5 (trigeminal neuralgia: L2) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDAs, i.e. generics) |
| Recommended Decision | Hold (trigeminal neuralgia: Proceed with Guardrails) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the pack's rationale notes, lamotrigine blocks voltage-gated sodium channels and reduces glutamate release. These are properties shared with carbamazepine and oxcarbazepine.

**Trigeminal nerve neoplasm:** This prediction is not credible. Nothing supports an antitumour effect from lamotrigine. The high score most likely reflects the drug's graph proximity to trigeminal neuralgia, a pain disorder of the same nerve, rather than to any neoplasm. Neither retrieved paper concerns lamotrigine in a tumour.

**Trigeminal neuralgia:** This link is strong and biologically coherent. Carbamazepine and oxcarbazepine are the first-line drugs, and lamotrigine acts through the same sodium-channel mechanism. It is used off-label as an alternative in some settings (for example Japan, per PMID 38246671).

Several reflex-seizure predictions (startle epilepsy, audiogenic seizures, reading seizures and others) share a generic antiseizure rationale. Only startle epilepsy has direct lamotrigine reports, all small case series.

---

## Clinical Trial Evidence

**Trigeminal nerve neoplasm:** Currently no related clinical trials registered.

**Trigeminal neuralgia (rank 2), shown because it is the actionable lead:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Lamotrigine vs carbamazepine in trigeminal neuralgia; directly on target but small |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine; population to be confirmed |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study of lamotrigine in neuropathic facial pain; mechanistic only |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Carbamazepine vs oxcarbazepine; does not test lamotrigine, standard-of-care context only |

---

## Literature Evidence

**Trigeminal nerve neoplasm:** The two retrieved papers are about trigeminal neuralgia in general and do not evaluate lamotrigine in any neoplasm.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for neuralgia caused by a cavernous malformation |

**Trigeminal neuralgia (rank 2), key items:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on trigeminal neuralgia management |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drug efficacy and side effects in trigeminal neuralgia |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Carbamazepine and oxcarbazepine remain first-line; newer agents are possible adjuvants |
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Clinical study | J Chin Med Assoc | Lamotrigine vs carbamazepine: efficacy and side effects in trigeminal neuralgia |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case report | Mult Scler Relat Disord | Refractory trigeminal neuralgia in MS treated with pregabalin plus lamotrigine |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka | Lamotrigine used off-label in Japan as an alternative to carbamazepine |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206382 | Lamotrigine | Orally disintegrating tablet | Not listed in retrieved data |
| ANDA207497 | Lamotrigine | Film-coated extended-release tablet | Not listed in retrieved data |
| ANDA213271 | Lamotrigine | Orally disintegrating tablet | Not listed in retrieved data |

ANDA207497 appears under three labelers (Amneal ×2, AvKARE). Other US forms include standard, chewable, extended-release and dispersible tablets.

---

## Safety Considerations

Please refer to the package insert for safety information.

Literature retrieved for other predictions notes a recent warning on possible ventricular arrhythmias (PMID 40499085, target-trial analysis) and case reports of lamotrigine-associated hemophagocytic lymphohistiocytosis (PMID 33408106). These should be checked against the current label.

---

## Conclusion and Next Steps

**Decision: Hold** (trigeminal nerve neoplasm); **Proceed with Guardrails** for trigeminal neuralgia.

**Rationale:**
The neoplasm prediction is a graph artefact with no trials, no lamotrigine-specific literature and no mechanism, so it should not be pursued. Trigeminal neuralgia has a coherent mechanism and a completed Phase 2/3 trial against carbamazepine, but that trial is small (n=21), so evidence is L2 rather than L1.

**To proceed, the following is needed:**
- Re-rank or re-label the candidate so trigeminal neuralgia, not the neoplasm, is the lead indication
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the population in NCT00203229 and full results of NCT00913107
- A larger randomized trial or meta-analysis of lamotrigine in trigeminal neuralgia
- Detailed mechanism-of-action data (e.g. from DrugBank)
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

