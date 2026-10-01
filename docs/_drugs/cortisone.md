---
layout: default
title: Cortisone
parent: Moderate Evidence (L3-L4)
nav_order: 550
evidence_level: L4
indication_count: 9
---

# Cortisone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Cortisone: From Glucocorticoid Therapy to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Cortisone is a corticosteroid, but the US label data supplied lists no approved indication text for it.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**, yet only **1 clinical trial** was retrieved (not relevant to cortisone or this disease) and **10 publications** were listed. Most of those are 1950s to 1970s case reports or reviews, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US label data |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 (one ANDA, ANDA080694; three Boiron pellet listings with no application number) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cortisone is a prodrug converted by 11β-HSD1 to cortisol (hydrocortisone). Glucocorticoids are lympholytic and induce apoptosis in lymphoid and T-cell malignancies through the glucocorticoid receptor, so a biological rationale exists.

The cortisone-specific support is thin. It consists of 1950s case reports in mycosis fungoides (the most common form of primary cutaneous T-cell lymphoma), and some of them describe ulceronecrotic terminal courses. The high TxGNN score therefore looks like a knowledge-graph association rather than validated clinical evidence. Modern lymphoma regimens use prednisone, dexamethasone or methylprednisolone, not cortisone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Suspended | 422 | R-miniCHOP with or without oral azacitidine in patients aged 75+ with newly diagnosed diffuse large B-cell lymphoma. It involves neither cortisone nor cutaneous T-cell lymphoma, so it is not relevant. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6234331](https://pubmed.ncbi.nlm.nih.gov/6234331/) | 1984 | Review | J Am Acad Dermatol | Pre-Sézary syndrome: 18 patients with erythroderma and low circulating Sézary cells were followed for about 5 years. Only one died and none developed lymphoproliferative disease. Cortisone is not the focus. |
| [11917454](https://pubmed.ncbi.nlm.nih.gov/11917454/) | 2001 | Review | Dermatol Nurs | Summary of Sézary syndrome, the leukemic form of cutaneous T-cell lymphoma, an aggressive disease with the lowest median survival among cutaneous lymphomas. |
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Case report | Sven Lakartidn | Combined ACTH and cortisone therapy in impetigo herpetiformis, mycosis fungoides and psoriatic erythroderma. |
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Case report | Dermatologica | Effects of cortisone in two cases of mycosis fungoides. |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Case report | Lyon Med | Two mycosis cases treated with delta-cortisone. The terminal ulceronecrotic process was probably connected with the medication. |
| [13573074](https://pubmed.ncbi.nlm.nih.gov/13573074/) | 1958 | Case report | Bull Soc Fr Dermatol Syphiligr | Two mycosis cases treated with prednisone. Fatal ulcero-necrotic processes were very likely connected with the drug. |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Case report | Bull Soc Fr Dermatol Syphiligr | Two cases of bronchial epithelioma in patients with mycosis fungoides treated with cortisone. |
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Not classified | J Med Chir Prat | Article on mycosis fungoides. No abstract available. |
| [5161189](https://pubmed.ncbi.nlm.nih.gov/5161189/) | 1971 | Not classified | Bull Soc Fr Dermatol Syphiligr | A pleuropulmonary form of mycosis fungoides with scleroderma-like skin manifestations, treated with topical nitrogen mustard. |
| [4241287](https://pubmed.ncbi.nlm.nih.gov/4241287/) | 1969 | Not classified | Munch Med Wochenschr | Climatotherapy in dermatoses: indications and chances of success. Little direct relevance. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA080694 | Cortisone Acetate (Chartwell RX, LLC) | Tablet (oral) | Not listed |
| No application number listed | Cortisone aceticum (Boiron) | Pellet | Not listed |
| No application number listed | Cortisone aceticum (Boiron) | Pellet | Not listed |
| No application number listed | Cortisone aceticum (Boiron) | Pellet | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

The only safety signal in the retrieved material is two 1958 case reports in mycosis fungoides describing fatal ulcero-necrotic terminal courses probably linked to corticosteroid use (delta-cortisone and prednisone). These are anecdotal and should not be treated as established risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The link rests on a plausible class-level glucocorticoid mechanism and a few 1950s case reports, with no relevant trials and some reports of harm. The FDA package insert warnings and contraindications are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- The FDA package insert (for example for ANDA080694) to fill in warnings, contraindications and the original indication.
- Cortisone mechanism-of-action data from DrugBank.
- Modern clinical evidence on the role of systemic glucocorticoids in primary cutaneous T-cell lymphoma, and whether cortisone offers any advantage over prednisone or dexamethasone.

Among the other predictions, adrenocortical insufficiency (L2, Proceed with Guardrails) looks like an established replacement use. The retrieved trials test hydrocortisone rather than cortisone, so it needs the same label check.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

