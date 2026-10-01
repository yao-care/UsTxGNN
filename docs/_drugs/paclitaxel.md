---
layout: default
title: Paclitaxel
parent: High Evidence (L1-L2)
nav_order: 1007
evidence_level: L1
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Paclitaxel: From Cancer Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane chemotherapy drug that is already marketed in the US in several injectable forms.
The TxGNN model predicts it is effective for **Female Breast Carcinoma**, and the prediction is supported by **50 linked clinical trials**, including several completed Phase 3 studies.
No indication-specific publications were retrieved for this prediction. Because breast cancer is an established use of paclitaxel, this is closer to **confirming existing standard use** than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

The US license records supplied contain no approved-indication text, so the original labeled indication could not be extracted.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this record. Paclitaxel is a cytotoxic taxane that stabilizes microtubules. This blocks cell division (mitotic arrest) and triggers apoptosis in rapidly dividing tumor cells.

Breast cancer is a well-established use of this mechanism. The linked trials use paclitaxel or nab-paclitaxel in adjuvant, neoadjuvant, and metastatic settings. The model score is consistent with this existing clinical use.

The evidence supports paclitaxel as guideline-standard therapy rather than a new use. What still needs to be confirmed is the exact regimen, formulation, and labeled indication against US regulatory records.

---

## Clinical Trial Evidence

The record links 50 trials to this indication. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00016406](https://clinicaltrials.gov/study/NCT00016406) | Phase 3 | Completed | 399 | Neoadjuvant AC followed by weekly paclitaxel vs a dose-dense regimen with G-CSF in inflammatory or locally advanced breast cancer |
| [NCT00014222](https://clinicaltrials.gov/study/NCT00014222) | Phase 3 | Completed | 2104 | Adjuvant EC → paclitaxel vs AC → paclitaxel vs CEF in node-positive or high-risk breast cancer |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Neoadjuvant carboplatin plus docetaxel or paclitaxel, then AC, in stage I-III triple-negative breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Paclitaxel + carboplatin + trastuzumab as first-line therapy in HER2-overexpressing metastatic disease |
| [NCT00589238](https://clinicaltrials.gov/study/NCT00589238) | Phase 2 | Terminated | 16 | Weekly paclitaxel ± carboplatin in basal-like breast cancer; underpowered |
| [NCT01705691](https://clinicaltrials.gov/study/NCT01705691) | Phase 2 | Completed | 50 | Neoadjuvant weekly paclitaxel vs eribulin, then AC, in HER2-negative locally advanced disease |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Completed | 200 | Adjuvant paclitaxel + trastuzumab in stage II-IIIA HER2-positive breast cancer |
| [NCT01307891](https://clinicaltrials.gov/study/NCT01307891) | Phase 2 | Completed | 64 | Nab-paclitaxel ± tigatuzumab in metastatic triple-negative breast cancer |
| [NCT04159142](https://clinicaltrials.gov/study/NCT04159142) | Phase 2 | Recruiting | 414 | Nab-paclitaxel + carboplatin vs nab-paclitaxel + capecitabine in advanced triple-negative breast cancer |
| [NCT05189067](https://clinicaltrials.gov/study/NCT05189067) | Phase 2/3 | Unknown | 190 | Adjuvant paclitaxel + trastuzumab vs docetaxel + trastuzumab in stage I HER2-positive disease |

Paclitaxel is often a backbone component of these regimens rather than the single variable tested, so the trials support the regimens more than paclitaxel alone.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## US Market Information

The record lists 20 licenses in total. Five are shown here. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA216355 | Paclitaxel protein-bound particles for injectable suspension (albumin-bound) | Injection, powder, lyophilized, for suspension | NorthStar Rx LLC |
| ANDA207326 | Paclitaxel | Injection, solution | Sagent Pharmaceuticals |
| ANDA075184 | Paclitaxel | Injection, solution, concentrate | Teva Parenteral Medicines, Inc. |
| ANDA207326 | Paclitaxel | Injection, solution | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. |
| ANDA075184 | Paclitaxel | Injection, solution, concentrate | Teva Parenteral Medicines, Inc. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabilizer) |
| Myelosuppression Risk | High (neutropenia is the main dose-limiting concern) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, neuropathy assessment, hypersensitivity monitoring during infusion |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries reflect the drug class and the toxicities noted in the evidence pack. The pack contains no DrugBank toxicity data, so please also refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Known toxicities noted in the evidence:** peripheral neuropathy, myelosuppression, and hypersensitivity reactions. Several linked trials test ways to reduce paclitaxel-induced neuropathy and infusion reactions.
- **Formulation:** paclitaxel (solvent-based) and albumin-bound nab-paclitaxel are distinct products. The regimen and formulation must be specified and not treated as interchangeable.

The package insert warnings and contraindications were not available in this record, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials (for example NCT00016406 and NCT00014222) and many Phase 2 trials include paclitaxel-based regimens in breast cancer. The drug is already marketed in the US, and this is standard use rather than a new indication. The guardrails reflect missing label and safety data and the known toxicities.

**To proceed, the following is needed:**
- Confirmation of the labeled indication and regimen against US regulatory records (the approved-indication text is missing from the current data)
- The package insert warnings and contraindications (currently missing, and blocking the safety screening step)
- Detailed mechanism-of-action data from DrugBank
- A defined regimen and formulation (paclitaxel vs nab-paclitaxel) and a monitoring plan for neuropathy and neutropenia
- Indication-specific literature for this prediction

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

