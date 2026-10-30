---
layout: default
title: Acitretin
parent: Model Prediction Only (L5)
nav_order: 123
evidence_level: L5
indication_count: 4
monitor_inn: "ACITRETIN"
predicted_indications: ["acne (disease)", "pediatric systemic lupus erythematosus", "fetal erythroblastosis", "familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome"]
last_modified_at: 2026-10-30
description: "Acitretin: predicted new indication acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Acitretin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Acitretin: second-generation oral retinoid → acne (disease)
{: .text-alpha }

## One-Sentence Summary

Acitretin is an oral retinoid that normalizes keratinocyte differentiation and proliferation. The TxGNN model predicts it may be effective for **acne (disease)**, but the supporting evidence is thin: **1 clinical trial** and **18 publications** were retrieved, and most of them concern hidradenitis suppurativa (acne inversa) rather than acne vulgaris.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acne (disease) |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 6) |
| Number of FDA Applications | at least 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Acitretin is a second-generation oral retinoid. Retinoids as a class normalize keratinocyte differentiation and proliferation and reduce follicular hyperkeratinization, which gives a plausible link to the pilosebaceous unit, where acne develops.

The link is weaker than for isotretinoin. Acitretin has less direct sebosuppressive activity and is not a standard therapy for acne vulgaris. The retrieved evidence mostly concerns hidradenitis suppurativa (acne inversa), a follicular occlusion disorder. The label "acne (disease)" appears to blend the two conditions, so the high score of 0.9994 should be read cautiously.

Acitretin's teratogenicity is a major constraint. Long-term pregnancy avoidance is required, and the washout is prolonged because etretinate can form in the presence of alcohol.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07708480](https://clinicaltrials.gov/study/NCT07708480) | Phase 4 | Completed | 70 | Randomized comparison of apremilast (30 mg twice daily) and acitretin (25 mg twice daily) for 12 weeks in moderate-to-severe hidradenitis suppurativa. The primary outcome was the IHS4 severity score. No results were provided. |

This trial studies hidradenitis suppurativa, not acne vulgaris, and it is not a Phase 3 trial.

## Literature Evidence

Most items are reviews, guidelines or case reports, and few directly test acitretin in acne.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Guideline | J Eur Acad Dermatol Venereol | European S1 guideline for hidradenitis suppurativa/acne inversa |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Clinical report | Br J Dermatol | Long-term results of acitretin therapy for hidradenitis suppurativa |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case report | Cutis | Nodulocystic acne and hidradenitis suppurativa treated with acitretin |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Hautarzt | Drug therapy of acne inversa (antibiotics, TNF-α inhibitors) |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clin Dermatol | Vitamin A and retinoids in dermatology, including acitretin |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | Drugs | Current and future use of retinoids, including severe acne and related dermatoses |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacol Appl Skin Physiol | Dermatological indications likely to benefit from retinoids |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Review | Dermatology | Retinoids and sebaceous gland activity; isotretinoin's acne efficacy is attributed to sebaceous gland inhibition |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | Review | Clin Pharmacokinet | Pharmacokinetics and efficacy of retinoids; acitretin's main success is in psoriasis |

## US Market Information

The records in the local data show 6 generic acitretin capsule licences (ANDA), so the list may be partial. No approved-indication text is recorded in these records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202552 | Acitretin (Amneal) | Capsule | Not recorded |
| ANDA202148 | Acitretin (Mylan) | Capsule | Not recorded |
| ANDA204633 | Acitretin (Sigmapharm) | Capsule | Not recorded |
| ANDA217774 | Acitretin (Alembic) | Capsule | Not recorded |
| ANDA091455 | Acitretin (Teva) | Capsule | Not recorded |

## Safety Considerations

- **Teratogenicity**: Pregnancy must be avoided long term, and the washout is prolonged because of etretinate formation with alcohol.
- **Drug Interactions**: Major interactions are listed with doxycycline, minocycline, tetracycline and vitamin A. Moderate interactions are listed with sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide) and naltrexone.
- **Conditions of concern in the drug-disease data** (not label text): liver failure, drug-induced liver injury, pancreatitis, hypertriglyceridemia, diabetes mellitus and diabetic ketoacidosis, obesity, pseudotumor cerebri and intracranial hypertension, vision disorders including night blindness, hyperostosis, anxiety and dysthymic disorders, and substance abuse/dependence.

Package-insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No cited study directly addresses acne itself. The only trial and most of the literature concern hidradenitis suppurativa, so the evidence level is L5 despite the high model score. Acitretin's teratogenicity and organ toxicity add a significant safety burden for a condition with established alternatives.

**To proceed, the following is needed:**
- Clarify whether the prediction refers to acne vulgaris or acne inversa (hidradenitis suppurativa).
- Controlled clinical data in the clarified condition, ideally randomized trials.
- Package-insert warnings, contraindications and mechanism-of-action data.
- A pregnancy-prevention and hepatic, lipid and skeletal monitoring plan.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

