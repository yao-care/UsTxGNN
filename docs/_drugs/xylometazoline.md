---
layout: default
title: Xylometazoline
parent: Model Prediction Only (L5)
nav_order: 1299
evidence_level: L5
indication_count: 2
---

# Xylometazoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Xylometazoline: From Topical Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

Xylometazoline is a topical alpha-adrenergic agonist that is already marketed as a nasal decongestant. The TxGNN model predicts it may be effective for **nasal cavity disease**, with **2 clinical trials** and **7 publications** currently supporting this direction. This is largely consistent with its existing use, so it is not a novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the retrieved license record (general pharmacology: nasal decongestion) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 (one completed Phase 3 trial, but small and indirect) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this record. Based on general pharmacology, xylometazoline is a topical alpha-adrenergic agonist. It constricts the blood vessels of the nasal mucosa, which reduces swelling and nasal resistance and widens the nasal airway.

This fits nasal obstruction and congestion. It also supports mucosal shrinkage before nasal procedures such as endoscopy and nasotracheal intubation, which is what most of the retrieved studies examine. Because the drug is already used as a nasal decongestant, the prediction is mainly confirming a known use rather than revealing a new one.

The main safety concern is rebound congestion and rhinitis medicamentosa with prolonged use. Any further development should keep this as a guardrail.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Blinded triple-crossover comparison of cocaine, lidocaine/xylometazoline and saline for intranasal analgesia before nasotracheal intubation. Xylometazoline is only part of a combination arm, and the endpoint is procedural analgesia. Indirect support only. |
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | N/A | Unknown | 80 | Foley catheter-assisted nasal intubation and nasal bleeding. Xylometazoline is not clearly the studied intervention. The link is weak and indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT | JAMA Otolaryngol Head Neck Surg | Double-blind, placebo-controlled trial of an intranasal local anesthetic and decongestant spray before flexible nasendoscopy in children |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Randomized blinded study | Eur Arch Otorhinolaryngol | Cotton pledget packing versus topical spray for nasal preparation before endoscopy (100 patients) |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Clinical study | Korean J Anesthesiol | Prophylactic xylometazoline spray compared with epinephrine gauze packing for expanding the nasal cavity before nasotracheal intubation |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | Double-blind randomized study | Arzneimittel-Forschung | Rhinomanometry study of a tuaminoheptane/N-acetylcysteine decongestant, with xylometazoline and placebo as comparators in 18 healthy subjects |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Physiological study | Rhinology | Effect of xylometazoline on nasal airflow asymmetry in healthy subjects and in people with common-cold rhinitis |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestn Otorinolaringol | Treatment of inflammatory nasal and sinus disease in elderly patients, including combined nasal sprays containing a decongestant |
| [20632242](https://pubmed.ncbi.nlm.nih.gov/20632242/) | 2010 | Animal study (dog) | Pneumologie | Xylometazoline reduced elevated nasal airway resistance in brachycephalic dogs by about 50%. Animal data only. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available in record | Metarivin Soln. 0.1% (Lydia Co., Ltd.) | Liquid | Not listed in record |

---

## Safety Considerations

- **Usage guardrail**: Rebound congestion and rhinitis medicamentosa with prolonged use.

For other safety information (warnings, contraindications, drug interactions), please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nasal cavity disease is consistent with xylometazoline's known decongestant pharmacology, and the retrieved studies support its use for nasal mucosal shrinkage. However, the evidence is small and indirect: one completed Phase 3 trial with 16 participants, where xylometazoline is part of a combination arm. The prediction is therefore not strong enough for L1.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The original approved indication and a valid license number for the marketed product
- Trials that directly test xylometazoline alone in nasal congestion or nasal disease, with limits on treatment duration

**Note on the second prediction:** *Acute laryngopharyngitis* (TxGNN score 99.89%) is rated **Hold** at L5. No trials or publications support it, xylometazoline is formulated for nasal delivery only, and local vasoconstriction in the larynx has not been evaluated for safety.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

