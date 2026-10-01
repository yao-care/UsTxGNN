---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 1130
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Rivaroxaban: From Anticoagulation (Thromboembolic Disease) to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is an oral anticoagulant (a direct factor Xa inhibitor) used to prevent and treat thrombosis. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this rests on model prediction only, with **0 clinical trials** and **4 publications** that do not test rivaroxaban in rheumatoid arthritis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation / thromboembolic disease (the US license records contain no indication text; inferred from the drug class and the retrieved literature) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, rivaroxaban is a direct factor Xa inhibitor. Its efficacy in thromboembolic disease is established, and any link to rheumatoid arthritis is speculative.

Rheumatoid arthritis involves chronic inflammation, which is associated with a hypercoagulable state and a higher risk of venous thromboembolism. Anticoagulation could address this thrombotic comorbidity. It would not be expected to change disease activity, such as joint inflammation or progression. A review of thrombin generation in autoimmune disease (PMID 34175144) describes this hypercoagulability as background, but it does not test rivaroxaban.

The very high TxGNN score is therefore not backed by any retrieved evidence that rivaroxaban treats rheumatoid arthritis. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower-extremity venous thromboembolism diagnosis and treatment; DVT incidence is 88–112 per 100,000 person-years and rises with age. Not specific to rheumatoid arthritis. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Narrative review of thrombin generation assay in autoimmune disease and its use for assessing hypercoagulability. Background only; does not test rivaroxaban. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation. Not about rheumatoid arthritis. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | An 88-year-old woman on oral steroids for rheumatoid arthritis had recurrent embolic events despite anticoagulation for atrial fibrillation. Rheumatoid arthritis is only a comorbidity; it is not evidence of efficacy. |

## US Market Information

The license records do not include approved-indication text, so the manufacturer is shown instead.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022406 | Xarelto | Tablet, film coated | Cardinal Health 107, LLC |
| NDA022406 | Xarelto | Tablet, film coated | A-S Medication Solutions |
| ANDA218445 | Rivaroxaban | Tablet, film coated | Indoco Remedies Limited |
| ANDA218445 | Rivaroxaban | Tablet | Florida Pharmaceutical Products, LLC |

Available forms include oral film-coated tablets, oral tablets, and granules for suspension.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.57%), but the evidence level is L5. No clinical trial exists, and none of the four retrieved papers shows rivaroxaban improving rheumatoid arthritis. Anticoagulation would at most address thrombotic comorbidity, not the disease itself.

**To proceed, the following is needed:**
- Mechanism of action data (MOA), and a mechanistic rationale linking factor Xa inhibition to rheumatoid arthritis disease activity
- Preclinical or clinical evidence of a disease-modifying effect, as opposed to thromboprophylaxis in patients who have rheumatoid arthritis
- Package insert warnings and contraindications, which are needed before any safety screening
- Approved-indication text for the US licenses, to confirm the original indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

