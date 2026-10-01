---
layout: default
title: Polyethylene Glycol 400
parent: Model Prediction Only (L5)
nav_order: 1061
evidence_level: L5
indication_count: 2
---

# Polyethylene Glycol 400
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

# Polyethylene Glycol 400: From Ophthalmic Lubricant Products to Bronchitis

## One-Sentence Summary

Polyethylene glycol 400 (PEG 400) is mainly a pharmaceutical excipient and solvent. In the US market it appears in over-the-counter eye drops such as Blink Tears and Visine Dry Eye Relief.
The TxGNN model predicts it may be effective for **bronchitis**, but this rests on the model score alone. The **5 linked clinical trials** all study a different agent (PEGylated epoetin, Mircera) in anemia, and there are **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. DrugBank lists no original indication or MOA for PEG 400. Based on known information, PEG 400 is mainly an excipient, solvent and osmotic laxative base. Its marketed eye-drop products act as lubricants and do not treat a disease.

We found no credible mechanistic link between PEG 400 and bronchitis. The TxGNN score of 0.996 is a knowledge-graph prediction only. The trials attached to this prediction appear to have been matched on the string "polyethylene glycol", not on PEG 400 as an active agent. They involve methoxy polyethylene glycol-epoetin beta, a large PEGylated protein with a completely different pharmacology.

The second-ranked prediction, congenital ichthyosiform erythroderma (score 99.10%), has no trials or literature. Its only rationale is that PEG 400 works as a humectant and vehicle in topical products. That would be a vehicle effect, not disease-modifying activity.

---

## Clinical Trial Evidence

All five trials were graded C (low relevance). They study Mircera (methoxy polyethylene glycol-epoetin beta) in renal anemia, not PEG 400 and not bronchitis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00559273](https://clinicaltrials.gov/study/NCT00559273) | Phase 3 | Completed | 307 | Once-every-4-weeks subcutaneous Mircera vs darbepoetin for anemia in non-dialysis CKD. Unrelated to PEG 400 or bronchitis. |
| [NCT01519947](https://clinicaltrials.gov/study/NCT01519947) | Phase 4 | Completed | 87 | Effect of altitude on Mircera dose requirements in renal anemia. Unrelated to PEG 400 or bronchitis. |
| [NCT01379963](https://clinicaltrials.gov/study/NCT01379963) | N/A | Completed | 780 | Retrospective observational study of hemoglobin levels over 6 months of Mircera treatment. Unrelated. |
| [NCT01422824](https://clinicaltrials.gov/study/NCT01422824) | N/A | Completed | 185 | Observational safety and efficacy study of Mircera in hemodialysis patients (STABILE). Unrelated. |
| [NCT01309295](https://clinicaltrials.gov/study/NCT01309295) | N/A | Completed | 250 | Prospective observational study of Mircera in predialysis and dialysis CKD. Unrelated. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The regulatory record lists 20 authorizations in total. The distinct products among the five entries provided are below. The record gives no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M018 | Blink Tears | Solution/drops | Bausch & Lomb Incorporated |
| M018 | Blink Triple Care | Solution/drops | Bausch & Lomb Incorporated |
| M018 | Visine Dry Eye Relief | Solution/drops | Kenvue Brands LLC |

Other dosage forms on record include solution and topical gel.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting evidence (L5). The five linked trials concern a different PEGylated biologic in anemia, and no literature exists. No mechanistic link between PEG 400 and bronchitis could be established.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications. This is a blocking gap that prevents safety screening.
- Mechanism of action data from DrugBank.
- Trials or studies that actually test PEG 400 (not PEGylated proteins) in bronchitis, and a plausible route of administration for the respiratory tract.
- Re-screening of the trial matching, since the current links appear to be string-match artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

