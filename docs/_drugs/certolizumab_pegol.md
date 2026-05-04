---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 6
---

# Certolizumab Pegol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

The txgnn-pipeline skill confirms this is a TxGNN reporting task. Proceeding to generate the evaluation report following the Evidence Pack v5 format, focusing on `predicted_indications[0]` (rheumatoid vasculitis).

---

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Certolizumab pegol (CZP, brand name Cimzia®) is a PEGylated anti-TNF-α biologic approved internationally for rheumatoid arthritis, Crohn's disease, psoriatic arthritis, and axial spondyloarthritis, though it has not been approved in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** (score 99.78%),
with **3 tangentially related clinical trials** and **8 publications** retrieved — however, the literature balance is striking: only **1 case report** documents therapeutic benefit, while **4 case reports** describe CZP-induced paradoxical vasculitis as an adverse drug reaction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for Rheumatoid Arthritis, Crohn's Disease, Psoriatic Arthritis, Axial Spondyloarthritis |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Certolizumab pegol is an Fc-free, PEGylated antigen-binding fragment (Fab') of a recombinant humanized monoclonal antibody that selectively neutralizes tumor necrosis factor-alpha (TNF-α). Unlike other anti-TNF biologics such as adalimumab or infliximab, CZP lacks the Fc region — a design that prevents complement-mediated cytotoxicity and significantly reduces placental transfer. Its efficacy in RA, Crohn's disease, PsA, and axSpA is all grounded in blocking TNF-α-driven inflammatory cascades.

Rheumatoid vasculitis (RV) is a serious extra-articular complication of long-standing seropositive RA, in which systemic TNF-α-mediated inflammation extends to vessel walls, causing ischemic leg ulcers, mononeuritis multiplex, and organ ischemia. On mechanistic grounds, neutralizing TNF-α could theoretically suppress this vascular inflammation — the same mechanism that underpins CZP's established efficacy in RA joint disease. This is the basis for the TxGNN model's high prediction score.

**However, the clinical signal is paradoxical and concerning.** Four of the eight retrieved publications document vasculitis as an *adverse drug reaction* to CZP or other anti-TNF agents — including leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis (HUV), medium-vessel vasculitis, and rapidly progressive glomerulonephritis. The probable mechanism for these paradoxical reactions involves immune complex deposition and complement activation in the context of anti-TNF-induced autoimmunity. Only a single case report (PMID 34786446) documents CZP used therapeutically for RV-related leg ulcers with benefit. The current adverse safety signal substantially outweighs the single therapeutic data point, placing this prediction in "biologically plausible but clinically high-risk" territory.

---

## Clinical Trial Evidence

No clinical trials directly evaluating CZP as a treatment for rheumatoid vasculitis were identified. The 3 retrieved trials have low direct relevance:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Compares two immunosuppressant hold strategies around elective shoulder arthroplasty in rheumatology patients; assesses flare incidence and wound complications — no vasculitis treatment focus |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study evaluating the risk of developing additional IMIDs in patients already treated with biologics or immunosuppressants for a single IMID; provides general epidemiological background |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab (not CZP) in RA patients with inadequate response to DMARDs; evaluates clinical practice patterns over 6 months — minimal relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Cohort | RMD Open | Long-term follow-up of CZP in 80 patients with IMID-related uveitis; demonstrates effectiveness and acceptable safety of CZP across multiple immune-inflammatory conditions |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Review | RMD Open | Systematic comparison of infection type and frequency across immune-modulatory drugs using Summary of Product Characteristics data; establishes CZP's infection safety profile in autoimmune disease treatment |
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case Report | JAAD Case Reports | **Only therapeutic evidence**: CZP successfully treated refractory leg ulcers due to rheumatoid vasculitis — sole case directly supporting this repurposing direction |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Case Report | Cureus | ⚠️ Anti-TNF (certolizumab pegol)-induced **medium-vessel vasculitis** in a 33-year-old with seronegative RA after inadequate prior treatment responses — paradoxical adverse event |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Case Report | Modern Rheumatology Case Reports | ⚠️ Rapidly progressive glomerulonephritis (pauci-immune, vasculitis-pattern) after introduction of CZP in a 30-year-old RA patient — autoimmune paradoxical reaction |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case Report | J Clin Pharmacy & Therapeutics | ⚠️ Hypocomplementemic urticarial vasculitis (HUV) developed *during* CZP treatment for RA — first reported case linking HUV specifically to CZP |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Retrospective Cohort | Clinical Medicine & Research | Single-center experience of cutaneous adverse events from biologic agents including CZP; documents a spectrum of skin and vascular reactions associated with anti-TNF use |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Case Report | Proceedings (Baylor Univ. Medical Center) | ⚠️ Leukocytoclastic vasculitis as a drug reaction *to* CZP in a psoriatic arthritis patient — first reported case associating this reaction specifically with CZP among TNF antagonists |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TNF-α blockade is mechanistically plausible for rheumatoid vasculitis, the clinical evidence balance is unfavorable: 4 of 8 retrieved publications document vasculitis as a *consequence* of anti-TNF therapy rather than a treatable target, and only 1 case report supports therapeutic benefit. Proceeding without substantially more safety and efficacy data would expose patients to poorly characterized risk.

**To proceed, the following is needed:**
- A structured retrospective case series or prospective registry documenting CZP use in confirmed rheumatoid vasculitis patients, with clear differentiation from drug-induced vasculitis
- Mechanistic studies or biomarker work to distinguish patients who may benefit (TNF-driven RV) from those at risk of paradoxical worsening (anti-TNF-induced vasculitis)
- Taiwan FDA package insert data for CZP: complete warning text, contraindications, and special population precautions
- Drug-drug interaction (DDI) profile for CZP in the rheumatoid vasculitis treatment context (e.g., concurrent immunosuppressants such as cyclophosphamide, azathioprine)
- Clarification of whether rheumatoid vasculitis patients were specifically included or excluded in the pivotal CZP RA clinical trials, and what outcomes were observed in that subset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

