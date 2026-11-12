---
layout: default
title: Golimumab
parent: Model Prediction Only (L5)
nav_order: 758
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "GOLIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease"]
description: "Golimumab: predicted new indication Hypermobility of coccyx (evidence level L5). Approved use: Not recorded in the local data"
---

# Golimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Golimumab: Hypermobility of coccyx
{: .text-alpha }

## One-Sentence Summary

Golimumab is an anti-TNF-alpha monoclonal antibody originally used for inflammatory rheumatic and bowel diseases, including rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis and ulcerative colitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypermobility of coccyx |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 3 of 3) |
| Number of FDA Applications | 3 (active: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Golimumab is a fully human monoclonal antibody that neutralizes TNF-alpha. TNF-alpha is a central cytokine in rheumatoid arthritis, and it is also implicated in vasculitic inflammation.

Rheumatoid vasculitis is a severe extra-articular complication of rheumatoid arthritis, mostly seen in seropositive patients. Its incidence has fallen since biologic DMARDs, including anti-TNF agents, were introduced. This gives a biological rationale for the prediction.

The supporting evidence is indirect, though. No trial or paper provided here tests golimumab in rheumatoid vasculitis. Reports of Takayasu arteritis arising during anti-TNF therapy also raise a possible paradoxical-reaction concern. The high TxGNN score is a model prediction and is not backed by direct clinical data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Recruiting | 80 | Compares stopping immunosuppressants for a longer versus shorter period before shoulder replacement in rheumatology patients. It does not evaluate golimumab in rheumatoid vasculitis and is not relevant to this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (36 RCTs) | Int J Mol Sci | Compares TNF inhibitors, including golimumab, for reducing joint destruction in rheumatoid arthritis. It does not address vasculitis. |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Med | Overview of biologic therapies for autoimmune diseases, covering benefits and drawbacks such as cost and adverse events. |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Review | Semin Arthritis Rheum | Frequency, causes and treatment of end-stage renal disease in rheumatoid arthritis. Only background relevance. |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatol Int | Pyoderma gangrenosum and pyogenic arthritis presenting as severe sepsis in a rheumatoid arthritis patient on golimumab. Notes that rheumatoid vasculitis has become less frequent in the biologic era. |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocul Immunol Inflamm | Behçet disease-associated uveitis treated successfully with golimumab. An example of off-label use in another inflammatory condition. |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of Takayasu's arteritis arising during anti-TNF therapy. This is a paradoxical-reaction signal relevant to vasculitis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125289 | Simponi (Janssen Biotech, Inc.) | Injection, solution | Not stated in the data; status valid |
| BLA125433 | Simponi Aria (Janssen Biotech, Inc.) | Solution | Not stated in the data; status valid |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The first 20 returned are summarized below.
  - **Major**:
    - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone (including ophthalmic).
    - Deferiprone.
    - Radiopharmaceuticals and radioimmunotherapies: iobenguane (I-131), ibritumomab tiuxetan, tositumomab, tositumomab (I-131).
  - **Moderate**: metronidazole, tinidazole, rosuvastatin, simvastatin.
  - **Minor**: zinc sulfate, zinc acetate, zinc gluconate.
- **Paradoxical reactions**: Case reports describe vasculitis (Takayasu's arteritis) arising during anti-TNF therapy. This needs attention in any vasculitis setting.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale (TNF-alpha blockade) is plausible, but there is no direct clinical evidence for golimumab in rheumatoid vasculitis. The only registered trial is unrelated, and the literature consists of reviews and case reports. Anti-TNF-associated vasculitis has also been reported.

<!-- review:begin us-lic-20261106-golimumab-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Anti-TNF-associated vasculitis has also been reported. The market status is "Cancelled only"." Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-golimumab-1 -->

**To proceed, the following is needed:**
- Direct clinical data, such as case series, observational studies or trials of golimumab (or anti-TNF agents) in rheumatoid vasculitis
- Mechanism of action data and a clearer account of the link to rheumatoid arthritis pathology
- Package insert warnings and contraindications, to allow a safety screen
- A safety assessment of paradoxical vasculitis under anti-TNF therapy
- Confirmation of current US regulatory and product availability

<!-- review:begin us-lic-20261106-golimumab-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of current US regulatory and product availability, given the cancelled licenses" Removed: it said the FDA applications were cancelled, discontinued, or not active, which did not match the FDA data (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 3 FDA applications or NDC listings for this drug, 3 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-golimumab-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The market status is "Cancelled only"" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "given the cancelled licenses" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

