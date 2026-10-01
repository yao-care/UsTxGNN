---
layout: default
title: Atracurium Besylate
parent: Moderate Evidence (L3-L4)
nav_order: 426
evidence_level: L4
indication_count: 10
---

# Atracurium Besylate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Atracurium Besylate: From Neuromuscular Blockade in Anesthesia to Preeclampsia

## One-Sentence Summary

Atracurium besylate is a non-depolarizing neuromuscular blocker used as a muscle relaxant during general anesthesia. The source data lists no approved indication text, so this comes from general pharmacology.
The TxGNN model predicts it may be relevant to **preeclampsia**, but **0 clinical trials** and only **4 publications** exist, and those describe anesthetic use in pregnancy rather than treatment of the disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data; general pharmacology: adjunct to general anesthesia (skeletal muscle relaxation) |
| Predicted New Indication | Preeclampsia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all listed authorizations are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. From general pharmacology, atracurium is a non-depolarizing nicotinic acetylcholine receptor antagonist at the neuromuscular junction. Its Hofmann elimination does not depend on renal, hepatic, or enzymatic function, which is useful in patients with organ dysfunction.

The link to preeclampsia appears to be **co-use, not therapy**. Atracurium is given to preeclamptic patients during anesthesia, for example for cesarean delivery, and it interacts with magnesium sulfate, which is commonly used in preeclampsia. The literature shows no evidence that atracurium treats or modifies preeclampsia itself.

The high TxGNN score therefore most likely reflects anesthetic co-use in the literature rather than a true mechanistic or therapeutic connection. A neuromuscular blocker has no recognized action on the placental, endothelial, or hypertensive pathways underlying preeclampsia.

The other nine predictions (cauda equina syndrome, blepharospasm, migraine, neurogenic bladder, thrombotic disease, and others) have no plausible mechanistic link or are supported only by unrelated papers. They are not developed further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9646009](https://pubmed.ncbi.nlm.nih.gov/9646009/) | 1998 | Review | Clin Pharmacokinet | Pharmacokinetics of neuromuscular relaxants in pregnancy. Atracurium's volume of distribution and clearance are unchanged during pregnancy, and its elimination is independent of renal, hepatic, and enzymatic function. |
| [3778800](https://pubmed.ncbi.nlm.nih.gov/3778800/) | 1986 | Clinical study | Br J Anaesth | Use of atracurium in pre-eclamptic patients as an anesthetic muscle relaxant (no abstract available). Does not address treating preeclampsia. |
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | Comparative clinical study | Anesth Pain Med | Serum IL-6, leptin, and adiponectin after cesarean section under general versus spinal anesthesia. Not about preeclampsia treatment. |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case series (n=12) | Rev Esp Anestesiol Reanim | Remifentanil bolus for cesarean section in high-risk patients. Not about atracurium as a treatment for preeclampsia. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA206010 | Atracurium Besylate | Injection, solution | AuroMedics Pharma LLC |
| ANDA206011 | Atracurium Besylate | Injection, solution | AuroMedics Pharma LLC |
| ANDA091489 | Atracurium Besylate | Injection, solution | Meitheal Pharmaceuticals Inc. |
| ANDA090782 | Atracurium Besylate | Injection, solution | Hospira, Inc. |
| ANDA091488 | Atracurium Besylate | Injection, solution | Meitheal Pharmaceuticals Inc. |

The source data lists 6 authorizations in total; 5 are shown here. All are injectable products.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found in the source data. General pharmacology notes an interaction with magnesium sulfate, which is relevant in preeclampsia care.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output plus literature describing anesthetic use in pregnancy, with no trials and no evidence that atracurium affects preeclampsia. Package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking; download and parse the label PDF)
- Mechanism of action data from DrugBank
- A biological rationale showing how neuromuscular blockade could modify preeclampsia, beyond co-use in anesthesia
- Confirmation of the approved indication text for the listed ANDAs
- Re-mapping of the obsolete "neurogenic bladder" term to a current ontology term, if that prediction is reviewed later

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

