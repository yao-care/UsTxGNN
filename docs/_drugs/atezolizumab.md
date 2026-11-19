---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 6
monitor_inn: "ATEZOLIZUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-06
description: "Atezolizumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). In the US: 3 FDA applications (3 active)"
---

# Atezolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Atezolizumab: PD-L1 inhibitor → uterine ligament adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Atezolizumab is a PD-L1–blocking antibody that is marketed in the United States. The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**, but **no clinical trials and no publications** were found for this specific disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 3) |
| Number of FDA Applications | 3 (active: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for atezolizumab: "PD L1 may be expressed on tumor cells and/or tumor infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD L1 to the PD 1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation and cytokine production. […] Atezolizumab is a monoclonal antibody that binds to PD L1 and blocks its interactions with both PD 1 and B7.1 receptors." ([DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee), label version 2026-10-13; accessed 2026-11-19.) Based on general knowledge, atezolizumab is an antibody that blocks PD-L1, which can restore T-cell activity against tumour cells. A plausible link to this prediction would be PD-L1 expression in gynecologic adenocarcinomas.

This link is speculative. The score comes from the model only, and no study in the compiled data examines uterine ligament adenocarcinoma. Any rationale is extrapolated from immunotherapy experience in related gynecologic cancers and would need biomarker confirmation (for example, PD-L1 expression in the tumour) before it could be relied on.

## Clinical Trial Evidence

Currently no related clinical trials registered for uterine ligament adenocarcinoma.

For context only, two trials exist in a related disease, cervical cancer, but they do not study the predicted disease itself and do not change the evidence level:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02921269](https://clinicaltrials.gov/study/NCT02921269) | Phase 2 | Completed | 11 | Atezolizumab plus bevacizumab in recurrent, persistent or metastatic cervical cancer; very small, so efficacy evidence is limited |
| [NCT03738228](https://clinicaltrials.gov/study/NCT03738228) | Phase 1 | Completed | 40 | Atezolizumab as an immune primer and with extended-field chemoradiotherapy in node-positive locally advanced cervical cancer; safety and feasibility focus |

## Literature Evidence

Currently no related literature available for uterine ligament adenocarcinoma.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761034 | TECENTRIQ | Injection, solution | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: 75 interactions were recorded. Examples include:
  - Major: adalimumab, baricitinib, BCG live vaccine (Tice substrain)
  - Moderate: corticosteroids (hydrocortisone, prednisone, dexamethasone, methylprednisolone and others), azathioprine, anakinra, alemtuzumab, roflumilast, and several vaccines

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9993), but no trial or publication directly studies uterine ligament adenocarcinoma, so the evidence level is L5 and the prediction remains hypothetical.

**To proceed, the following is needed:**
- Evidence that the disease is PD-L1 dependent, such as tumour PD-L1 expression data
- Mechanism of action data and a review of the package insert warnings and contraindications
- Any case series or early-phase studies in this rare gynecologic tumour
- A safety plan addressing interactions with immunosuppressants and live vaccines

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

