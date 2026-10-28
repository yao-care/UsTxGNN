---
layout: default
title: Chloroprocaine
parent: Model Prediction Only (L5)
nav_order: 520
evidence_level: L5
indication_count: 1
monitor_inn: "CHLOROPROCAINE"
predicted_indications: ["cauda equina syndrome"]
last_modified_at: 2026-10-14
description: "Chloroprocaine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the available data (used as a local anesthetic)"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Chloroprocaine: From Local Anesthesia to Cauda Equina Syndrome (Prediction Likely Reflects an Adverse Association)
{: .text-alpha }

## One-Sentence Summary

Chloroprocaine is an ester-type local anesthetic used for spinal, epidural and topical ocular anesthesia.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **4 publications** on this topic, and the publications mainly describe cauda equina syndrome as a **complication** of local anesthetics rather than something chloroprocaine treats.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data (used as a local anesthetic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, chloroprocaine is an ester-type local anesthetic that blocks voltage-gated sodium channels, and it is used for spinal and epidural anesthesia.

The prediction is **not mechanistically convincing**. The publications link chloroprocaine to cauda equina syndrome as a potential **cause** (neurotoxicity after intrathecal or epidural administration, particularly with large doses of preservative-containing formulations). No plausible mechanism has been identified by which a sodium channel blocker would treat or reverse cauda equina syndrome, which is typically a surgical emergency caused by nerve root compression.

The high TxGNN score (0.9901) most likely reflects the drug-disease association in the literature rather than a therapeutic effect. The association is more likely adverse than therapeutic.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiol Scand | Chloroprocaine vs lidocaine for selective spinal anesthesia in outpatient transurethral prostatectomy; an anesthesia comparison, not a treatment study for cauda equina syndrome |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiol Scand | Use of chloroprocaine for spinal anesthesia as an alternative to lidocaine (transient neurologic symptoms); neurologic sequelae were described after large doses of preservative-containing chloroprocaine |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Safety | Incidence and prevention of regional anesthesia complications, including neural injury and local anesthetic toxicity |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case report | Regional Anesthesia | Two cases of cauda equina syndrome after spinal-epidural anesthesia; cauda equina syndrome is a known complication, with chloroprocaine among the implicated agents |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA009435 | Nesacaine | Injection, solution | Not listed (valid) |
| NDA216227 | IHEEZO | Gel | Not listed (valid) |
| ANDA040273 | Chloroprocaine Hydrochloride | Injection, solution | Not listed (valid) |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency, cardiovascular disease and heart disease.
- **Drug Interactions:** 12 interactions were identified, of which 1 is Major, 10 are Moderate and 1 is Minor.
  - **Major:** Nitrous acid
  - **Moderate:** Sulfasalazine; topical, nasal or ophthalmic local anesthetics and related agents (lidocaine, benzocaine, cocaine, tetracaine, oxybuprocaine, cinchocaine)
  - **Minor:** Hyaluronidase
- The literature also reports neurotoxicity, including cauda equina syndrome and transient neurologic symptoms, after intrathecal or epidural administration of local anesthetics.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). The available literature describes cauda equina syndrome as a complication of spinal and epidural local anesthetics, not as a condition they treat, and no therapeutic mechanism is plausible. All three US authorizations are valid, and the drug is marketed.

**To proceed, the following is needed:**
- Confirmation that the model signal reflects an adverse (causative) association, and reclassification of the finding as a safety signal rather than a repurposing candidate
- Mechanism of action data and a plausible mechanistic link to cauda equina syndrome
- FDA package insert warnings and contraindications
- Original approved indication text for the authorizations
- Preclinical or clinical evidence of therapeutic benefit, if the candidate is to be reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

