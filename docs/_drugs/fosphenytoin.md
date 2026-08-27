---
layout: default
title: Fosphenytoin
parent: 僅模型預測 (L5)
nav_order: 739
evidence_level: L5
indication_count: 7
---

# Fosphenytoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fosphenytoin: From Seizure Disorders to Manic Bipolar Affective Disorder

## One-Sentence Summary

Fosphenytoin (DB01320) is a phosphate-ester prodrug of phenytoin, a voltage-gated sodium channel blocker historically used to control seizures and status epilepticus. Among seven TxGNN-flagged candidate indications in this evidence pack, most (conjunctivitis, NSIAD, Tourette syndrome, granulomatous myositis, myositis fibrosa, fibromyalgia) carry zero supporting literature or trials and are explicitly flagged in the model rationale as likely false positives or weak mechanistic analogies — this report instead focuses on **Manic Bipolar Affective Disorder**, the only candidate with any literature evidence (**2 publications**, no registered clinical trials), reflecting a mechanistic hypothesis shared with established mood stabilizers (carbamazepine, valproate, lamotrigine).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in this evidence pack's regulatory data (no license records); per known pharmacology, fosphenytoin/phenytoin is indicated for seizure disorders and status epilepticus |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.18% (rank 17,836) |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original MOA data for fosphenytoin is not available in this evidence pack (flagged as a High-severity data gap). Based on established pharmacology, fosphenytoin is rapidly converted in vivo to phenytoin, a voltage-gated sodium channel blocker that suppresses pathological neuronal hyperexcitability — the basis of its anticonvulsant effect.

Several other sodium-channel-acting anticonvulsants (carbamazepine, valproate, lamotrigine) are already clinically established mood stabilizers for bipolar disorder, on the hypothesis that dampening excessive limbic/cortical firing also stabilizes mood. Fosphenytoin's prediction extends this class-level mechanism to phenytoin itself.

However, this is a mechanistic analogy rather than confirmed evidence specific to fosphenytoin: the only direct clinical data is a single small open-label pilot study from 2003, with no subsequent controlled trials in the two decades since. The mechanistic link is plausible but unconfirmed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/) | 2003 | Open-label pilot study | The Journal of Clinical Psychiatry | Tested intravenous high-dose fosphenytoin as an acute antimanic treatment, hypothesizing that anticonvulsant mechanisms could rapidly control acute mania; fosphenytoin was chosen over IV phenytoin for its lower cardiac/local-vein toxicity. |
| [23205958](https://pubmed.ncbi.nlm.nih.gov/23205958/) | 2012 | Review | Epilepsia | Historical review of AED chemical-structure development (phenobarbital → phenytoin → carbamazepine → valproate); not directly focused on mania, included as background structural/class context only. |

---

## US Market Information

Fosphenytoin is not currently marketed and holds no NDA records in this evidence pack (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Obtaining the TFDA/FDA label warnings and contraindications is flagged as a **Blocking** data gap in this evidence pack — it currently prevents formal safety pre-screening (S1) of this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the manic bipolar indication rests on a single small open-label pilot study (2003) with no controlled follow-up in over 20 years, and the drug is unmarketed with no NDA. A Blocking-severity data gap (missing label warnings/contraindications) also prevents safety pre-screening. The remaining six TxGNN-flagged candidates in this evidence pack have no clinical trial or literature support at all and are independently scored Hold/L5 by the same evidence pack.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) to clear the Blocking safety data gap
- Confirmed original MOA documentation from DrugBank
- A controlled (ideally randomized) trial evaluating fosphenytoin/phenytoin in acute mania to update evidence beyond the single 2003 pilot study
- Drug-drug interaction (DDI) profile, currently not found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

