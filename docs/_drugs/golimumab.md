---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 758
evidence_level: L5
indication_count: 5
---

# Golimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Golimumab: From Approved Autoimmune Indications to Rheumatoid Vasculitis (and Three Other Predicted Uses)

## One-Sentence Summary

Golimumab is a fully human anti-TNF-α monoclonal antibody used globally for rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis, but it is **not currently licensed in Taiwan**. The TxGNN model's top-ranked new prediction is **Rheumatoid Vasculitis**, supported by only **3 clinical trials** (none disease-specific) and **6 publications** (mostly case reports), including one report of vasculitis *arising during* anti-TNF therapy — a signal that cuts against, rather than for, this indication. Two lower-ranked predictions (**Inflammatory Spondylopathy** and **Polyarticular Juvenile RA**) are actually much better supported (L1 evidence, completed Phase 3 trials) but largely reflect golimumab's *existing* global label rather than a novel repurposing hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not currently licensed in Taiwan (globally approved for rheumatoid arthritis / psoriatic arthritis / ankylosing spondylitis per literature evidence) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed (market_status: 未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information from the evidence literature in this pack, golimumab is a fully human IgG1κ monoclonal antibody that neutralizes TNF-α, and is part of the anti-TNF biologic class (alongside infliximab, etanercept, adalimumab, certolizumab). Its efficacy in rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis is well established (PMID 20065639, 28530020).

Rheumatoid vasculitis is a severe extra-articular manifestation of rheumatoid arthritis, and TNF-α is plausibly involved in its inflammatory pathway — one case report (PMID 29075910) notes that the incidence of rheumatoid vasculitis has declined since anti-TNF agents entered practice, which is the basis of TxGNN's mechanistic link.

However, this mechanistic story is directly contradicted by another case report in the same evidence set (PMID 22999907), describing two patients who developed Takayasu's arteritis — a large-vessel vasculitis — **while receiving** anti-TNF therapy. This "paradoxical vasculitis" phenomenon is a recognized class effect of anti-TNF agents. None of the three retrieved trials were designed to test golimumab's efficacy specifically in rheumatoid vasculitis; they are either indirectly related (perioperative management, IMID risk registry) or study a different drug (tocilizumab). Given this mixed and partly contradictory signal, the mechanistic case is plausible but unproven, and carries an active safety caveat.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Evaluates perioperative immunosuppressant/biologic hold duration in rheumatology patients undergoing shoulder arthroplasty; not a rheumatoid vasculitis efficacy trial. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study of the risk of developing a second immune-mediated inflammatory disease (IMID) in patients treated with biologics/immunosuppressants; provides safety-signal context, not efficacy data. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional real-world study of tocilizumab (not golimumab) in RA patients with inadequate response to DMARDs/biologics; only indirectly relevant. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | RCT (network meta-analysis, 36 RCTs) | Int J Mol Sci | Compares 5 anti-TNF agents (incl. golimumab) vs methotrexate on radiographic joint destruction in general RA; not vasculitis-specific. |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Overview of biologic therapies for autoimmune/rheumatic disease, including mechanisms and drawbacks of TNF-targeted agents. |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Describes frequency, causes and treatment of end-stage renal disease in RA patients; tangential to vasculitis. |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatol Int | RA patient on golimumab developed pyoderma gangrenosum/pyogenic arthritis presenting as severe sepsis; notes rheumatoid vasculitis incidence has fallen since anti-TNF introduction. |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report | Joint Bone Spine | Two cases of Takayasu's arteritis (large-vessel vasculitis) occurring **during** anti-TNF therapy — a cautionary "paradoxical vasculitis" signal. |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocul Immunol Inflamm | Golimumab successfully treated Behçet's disease-associated uveitis, illustrating off-label anti-inflammatory potential in other immune-mediated conditions (not vasculitis). |

## US Market Information

Golimumab is not currently marketed and has no license records in the available regulatory data (market_status: 未上市, total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information (TFDA warnings, contraindications, and DDI data are not currently available — see DG001, a Blocking data gap).

Note: independent of the formal safety fields above, the literature evidence itself flags a mechanistic safety concern — anti-TNF agents have been reported to coincide with new-onset vasculitis (PMID 22999907) — which should be weighed alongside any Taiwan-specific label data once obtained.

## Other Predicted Indications in This Candidate Pack

This evidence pack evaluated five TxGNN-predicted indications for golimumab; the other four are summarized here for completeness.

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Rationale |
|------|---------|------|------|------|------|------|
| 2 | Hypermobility of coccyx | 99.67% | L5 | S0 | Hold | Mechanically/structurally driven condition, not TNF-α-mediated; no trials or literature; likely a knowledge-graph false positive. |
| 3 | Inflammatory spondylopathy | 99.66% | L1 | S3 | Proceed with Guardrails | Corresponds to ankylosing spondylitis/axial spondyloarthritis — an indication for which golimumab is already globally approved, with numerous completed Phase 3 RCTs (e.g. NCT00265083, NCT03270501). Not a novel hypothesis, but a strong candidate for Taiwan market entry. |
| 4 | Kummell disease | 99.61% | L5 | S0 | Hold | Structural vertebral compression/avascular necrosis, not an autoimmune/inflammatory disease; no supporting evidence; likely knowledge-graph noise. |
| 5 | Polyarticular juvenile rheumatoid arthritis | 99.59% | L1 | S3 | Proceed with Guardrails | Shares TNF-α-driven synovitis mechanism with adult RA; IV golimumab has completed Phase 3 support (GO-VIVA-type trial, NCT02277444), though the SC formulation trial (NCT01230827) was terminated without meeting its primary endpoint — formulation-specific efficacy differences should be tracked. |

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, Rheumatoid Vasculitis)

**Rationale:**
- The mechanistic story for rheumatoid vasculitis is undermined by a contradictory case report showing vasculitis onset during anti-TNF therapy, and no trial directly tests golimumab in this disease; evidence level is only L4.
- By contrast, two lower-ranked predictions in this same pack (Inflammatory Spondylopathy, Polyarticular Juvenile RA) reach L1 evidence with completed Phase 3 trials and represent golimumab's already-established global label — these are the more actionable near-term opportunities, flagged as "Proceed with Guardrails."

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) via PDF download and parsing (DG001, Blocking) — required before any S1 safety screening, for whichever indication is pursued.
- Confirmed mechanism-of-action data via DrugBank API (DG002).
- If pursuing rheumatoid vasculitis specifically: a dedicated efficacy trial or systematic review, plus formal pharmacovigilance review of the paradoxical-vasculitis safety signal, before advancing past Hold.
- If pursuing the stronger candidates (inflammatory spondylopathy / polyarticular JIA): a Taiwan market-entry/licensing assessment rather than a repurposing safety workup, since these are established indications elsewhere.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

