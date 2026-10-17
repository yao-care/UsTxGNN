---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atezolizumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Transitional cell carcinoma (urothelial carcinoma)"
monitor_inn: "ATEZOLIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Atezolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Atezolizumab: From Transitional Cell Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is an anti-PD-L1 antibody originally used to treat transitional cell (urothelial) carcinoma.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
but only **1 early-phase clinical trial (Phase 1b)** and **no publications** currently support this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (urothelial carcinoma) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (as assigned in the compiled data; by the strict rubric this is closer to L5, since no observational study or systematic review is listed for this indication) |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA761034, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, atezolizumab is a PD-L1 immune checkpoint inhibitor, its efficacy in urothelial carcinoma has been established, and mechanistically it may be applicable to related urothelial tumours.

Prostatic urethra urothelial carcinoma arises from the same urothelial lineage as bladder and upper tract urothelial carcinoma. The PD-L1 checkpoint rationale therefore carries over naturally. The high TxGNN score likely reflects this close proximity to the approved indication in the knowledge graph.

No evidence specific to the prostatic urethra subsite is available. The only linked trial is a combination study that enrolls several genitourinary tumour types.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | Active, not recruiting | 914 | Phase 1b dose-escalation and expansion study of cabozantinib alone or with atezolizumab in advanced solid tumours, including urothelial carcinoma (bladder, renal pelvis, ureter, urethra), renal cell carcinoma and prostate cancer. It assesses safety, tolerability, preliminary efficacy and PK. It is not specific to prostatic urethra disease. |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761034 (cancelled) | TECENTRIQ (Genentech, Inc.) | Injection, solution | Not stated in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody) |
| Myelosuppression Risk | Low; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 75 interactions were identified. The 20 shown in the compiled data are mostly Moderate, with four rated Major:
  - Adalimumab (Major)
  - Baricitinib (Major)
  - Bacillus Calmette-Guérin live antigen (Major)
  - One further Major-level entry in the list
  - Moderate-level interactions include corticosteroids (hydrocortisone, prednisone, dexamethasone, methylprednisolone and others), roflumilast, azathioprine, alemtuzumab, anakinra, and several vaccines.
  - Immunosuppressants and live vaccines deserve particular attention.

Please refer to the package insert for warnings and contraindications, which are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale is strong because the tumour shares the urothelial lineage with the approved indication. However, the evidence is limited to one Phase 1b multi-tumour combination trial with no subsite-specific data and no literature. Package insert safety data are also missing, and the US licence is listed as cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Subsite-specific efficacy data or published reports in prostatic urethra urothelial carcinoma
- Confirmation of current US regulatory status
- A safety monitoring plan that accounts for immunosuppressant and live-vaccine interactions

**Other predicted indications (for reference):**
- Endocervical carcinoma (score 99.92%) has a stronger evidence base, with a completed Phase 2 trial (NCT02921269, n=11, atezolizumab plus bevacizumab) and a completed Phase 1 trial (NCT03738228, n=40). It is still small and early-phase, so it warrants further research rather than a Go decision.
- The remaining predictions, including other urothelial variants and rare cervical or uterine ligament carcinomas, are supported by model prediction only and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

