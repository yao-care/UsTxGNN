---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 9
---

# Acetic Acid
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

# Acetic Acid: From No Documented Indication to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is marketed in the US in several forms (solution, irrigant, cream, spray, and a homeopathic pellet), but the license records give no approved indication text.
The TxGNN model predicts it may be effective for **post-bacterial disorder**, but **none of the 18 matched clinical trials tests acetic acid as a treatment** and **no publications** were found, so this remains a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The US license records give no approved indication, so the relationship between an original use and the predicted one cannot be established from this record.

The only plausible link is indirect. Acetic acid (acetate) is a short-chain fatty acid produced by gut bacteria. Several matched trials measure it as a metabolite outcome in microbiome studies. That is a biomarker role, not a therapeutic one. No matched trial gives acetic acid to patients with a post-bacterial condition. The prediction therefore has no mechanistic or clinical support in the current evidence.

---

## Clinical Trial Evidence

Currently 18 trials matched by keyword. None tests acetic acid as an intervention for a post-bacterial condition. The 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05710094](https://clinicaltrials.gov/study/NCT05710094) | Phase 1 | Completed | 28 | Safety of topical SoftOx Biofilm Eradicator in chronic leg wounds. Composition not verified as acetic acid. |
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Apple cider vinegar plus metformin vs metformin alone in type 2 diabetes. Not a bacterial condition. |
| [NCT04036318](https://clinicaltrials.gov/study/NCT04036318) | N/A | Completed | 3022 | Presumptive periodic treatment of sexually transmitted infections in high-risk groups in Tanzania. Acetic acid is not the intervention. |
| [NCT03212729](https://clinicaltrials.gov/study/NCT03212729) | N/A | Completed | 10 | Antimicrobial photodynamic therapy added to endodontic treatment. Bacterial context only. |
| [NCT07048028](https://clinicaltrials.gov/study/NCT07048028) | N/A | Recruiting | 90 | Chitosan vs sodium hypochlorite combinations as root-canal irrigants. |
| [NCT04824261](https://clinicaltrials.gov/study/NCT04824261) | N/A | Unknown | 100 | 4% boric acid vs clotrimazole in otomycosis. |
| [NCT03619161](https://clinicaltrials.gov/study/NCT03619161) | N/A | Completed | 58 | Bathroom cleaning and eczema severity. Not about acetic acid. |
| [NCT06135116](https://clinicaltrials.gov/study/NCT06135116) | N/A | Completed | 60 | Regulatory T cells and cytokines in periodontal disease. Immunology study. |
| [NCT02872675](https://clinicaltrials.gov/study/NCT02872675) | N/A | Completed | 17 | Prebiotic supplementation in adults with and without exercise-induced bronchoconstriction. Bacterial metabolites are outcomes. |
| [NCT06612164](https://clinicaltrials.gov/study/NCT06612164) | N/A | Completed | 65 | Kefir consumption in healthy adults. Acetate is at most a fermentation product. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040166 | Acetic Acid (Chartwell RX, LLC) | Solution | Not stated |
| NDA012179 | Acetic Acid (NuCare Pharmaceuticals, Inc.) | Solution | Not stated |
| ANDA040607 | Acetic Acid (A-S Medication Solutions) | Solution | Not stated |
| ANDA040607 | Acetic Acid (TruPharma, LLC) | Solution | Not stated |
| Not listed | Aceticum acidum (Boiron) | Pellet | Not stated |

Other forms on the market include irrigant, cream, and spray.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for post-bacterial disorder rests on the model score alone (Evidence Level L5). No matched trial or publication tests acetic acid for this condition, and no original indication or mechanism is documented.

Among the other predicted indications, **tinea corporis** (rank 9, score 99.25%) has the most supportive material, rated L4. It includes historical reports of dilute acetic acid for tinea, and vinegar-based studies in tinea pedis and onychomycosis. Even there, no study tests acetic acid alone for tinea corporis. A 2023 case series also documents chemical burns from folk remedies (PMID 37256034), so concentration and exposure control matter. It would be a better candidate to investigate first.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved indications, obtained from the FDA labeling
- Mechanism of action data, e.g. from DrugBank
- A clear clinical definition of "post-bacterial disorder", then a targeted search for studies testing acetic acid itself
- If the tinea corporis direction is pursued: a comparative study of acetic acid alone, with a concentration and skin-safety plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

