---
layout: default
title: Chloroprocaine
parent: Model Prediction Only (L5)
nav_order: 520
evidence_level: L5
indication_count: 1
---

# Chloroprocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Chloroprocaine: From Local Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Chloroprocaine is a short-acting local anesthetic, marketed in the US as an injectable solution and an ophthalmic gel.
The TxGNN model predicts it may be relevant to **cauda equina syndrome**, but the **1 clinical trial** and **4 publications** found all describe this condition as a *complication* of neuraxial anesthesia, not something the drug treats.
The prediction most likely reflects an adverse-event association, not a therapeutic one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US label data provided (local anesthetic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 (model prediction only; the retrieved studies are safety reports, not efficacy evidence. The source pack labels this L4.) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 license records (NDA009435, NDA216227) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Chloroprocaine is a local anesthetic of the ester type, which blocks voltage-gated sodium channels and thereby interrupts nerve conduction.

**No therapeutic link is supported.** In the retrieved literature, cauda equina syndrome appears as a known complication of spinal and epidural anesthesia. Local anesthetic neurotoxicity, including with chloroprocaine, has been implicated. A drug that blocks nerve conduction has no known mechanism for treating a compressive or injury-related nerve-root disorder.

The high TxGNN score (0.99) most likely comes from a knowledge-graph connection through adverse events or anesthesia-related links. It should not be read as evidence of benefit. The prediction cannot be cross-checked against a known original mechanism or indication, because neither is available.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02067806](https://clinicaltrials.gov/study/NCT02067806) | N/A (observational) | Completed | 394 | Prospective safety study of 1% 2-chloroprocaine in spinal anesthesia, tracking neurological adverse events, especially transient neurological symptoms and cauda equina syndrome. It tests safety, not treatment, so it gives no direct support for this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiol Scand | Chloroprocaine vs lidocaine for selective spinal anesthesia in outpatient TURP. It compares anesthetic performance and does not address treating cauda equina syndrome. |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiol Scand | Review of chloroprocaine for spinal anesthesia. It notes that neurologic sequelae followed intrathecal injection of large doses of preservative-containing chloroprocaine. |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Saf | Incidence and prevention of regional anesthesia complications, including neural injury and local anesthetic toxicity. |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case report | Reg Anesth | Two cases of cauda equina syndrome after spinal-epidural anesthesia. Prior reports had implicated lidocaine, chloroprocaine, and procaine. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA009435 | Nesacaine | Injection, solution | Not listed in the data provided |
| NDA009435 | Chloroprocaine HCl | Injection, solution | Not listed in the data provided |
| NDA009435 | Chloroprocaine HCl | Injection, solution | Not listed in the data provided |
| NDA216227 | IHEEZO | Gel | Not listed in the data provided |
| NDA009435 | Nesacaine | Injection, solution | Not listed in the data provided |

---

## Safety Considerations

The literature above raises a specific neurotoxicity concern. Cauda equina syndrome and transient neurological symptoms have been reported after intrathecal or epidural local anesthetics, including chloroprocaine, particularly with large doses of preservative-containing formulations.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence describes cauda equina syndrome as a possible harm of neuraxial chloroprocaine, not a condition it treats. There is no efficacy evidence and no plausible mechanism for treatment, so the high model score is not actionable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, currently missing and blocking safety screening
- Mechanism of action data from DrugBank
- Expert review to confirm whether the prediction is an adverse-event artifact and should be dropped
- Any evidence of therapeutic benefit in cauda equina syndrome, which none of the retrieved studies provide
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

