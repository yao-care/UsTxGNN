---
layout: default
title: Golimumab
parent: Model Prediction Only (L5)
nav_order: 758
evidence_level: L5
indication_count: 5
---

# Golimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Golimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is an anti-TNF-alpha monoclonal antibody marketed in the US for inflammatory arthritis (rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis).
The TxGNN model predicts it may be useful for **rheumatoid vasculitis**, with a very high score.
However, the **3 registered trials** and **6 publications** found only give RA-level context or a safety signal. **None directly tests golimumab in rheumatoid vasculitis.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (from the literature; the US license records contain no indication text) |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (mechanistic rationale only; no direct studies) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records (2 unique BLAs: BLA125289, BLA125433) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, golimumab is a fully human antibody that neutralizes TNF-alpha. TNF-alpha drives synovial inflammation in rheumatoid arthritis and may also contribute to its extra-articular vascular inflammation. Golimumab's efficacy in RA is established.

Rheumatoid vasculitis is a severe extra-articular complication of RA, mostly in seropositive patients. Because the two conditions share inflammatory pathways, the model's prediction is plausible in principle. The literature notes that the incidence of rheumatoid vasculitis has declined since anti-TNF biologics were introduced.

There are important caveats:
- No cited source tests golimumab in rheumatoid vasculitis.
- The very high score (0.997) probably reflects proximity to RA in the knowledge graph rather than direct evidence.
- Case reports describe **vasculitis arising during anti-TNF therapy** (for example, Takayasu's arteritis). This suggests a paradoxical risk that must be weighed against any benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; no vasculitis efficacy endpoint |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Observational study of new immune-mediated inflammatory diseases in patients on biologics; no efficacy data for rheumatoid vasculitis |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional tocilizumab study in RA; RA context only, no vasculitis endpoint |

All three trials were graded C for relevance. None studies golimumab in rheumatoid vasculitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (36 RCTs) | Int J Mol Sci | Original and biosimilar TNF inhibitors, including golimumab, similarly reduce joint destruction in RA; no vasculitis data |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Med | Update on biologic therapy for autoimmune diseases, including its drawbacks and adverse events |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Review | Semin Arthritis Rheum | Frequency, causes and treatment of end-stage renal disease in RA |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatol Int | Pyoderma gangrenosum and pyogenic arthritis presenting as severe sepsis in an RA patient on golimumab; mentions rheumatoid vasculitis as a known RA complication |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of Takayasu's arteritis arising under anti-TNF therapy (paradoxical vasculitis safety signal) |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocul Immunol Inflamm | Behçet disease-associated uveitis successfully treated with golimumab; shows activity in another inflammatory condition, not rheumatoid vasculitis |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA 125289 | Simponi (Janssen Biotech, Inc.) | Injection, solution | Not listed in the record |
| BLA 125433 | SIMPONI ARIA (Janssen Biotech, Inc.) | Solution | Not listed in the record |

BLA125289 appears twice in the source data, so only two unique authorizations are shown.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found.
- **Vasculitis signal**: Published case reports describe vasculitis (Takayasu's arteritis) arising during anti-TNF therapy. Any use in a vasculitic disease would need close monitoring.

Please refer to the package insert for other safety information (warnings and contraindications).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on mechanism and knowledge-graph proximity to RA. There is no trial or study of golimumab in rheumatoid vasculitis, and case reports raise a paradoxical vasculitis concern.

**To proceed, the following is needed:**
- Direct clinical evidence in rheumatoid vasculitis (case series, cohorts or trials)
- Package insert warnings and contraindications
- Detailed mechanism of action data (for example, from DrugBank)
- Note: The same pack's rank 3 (inflammatory spondylopathy) and rank 5 (polyarticular juvenile rheumatoid arthritis) have Phase 3 support. Both are likely on-label or near-label uses rather than true repurposing, so verify them against the US label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

