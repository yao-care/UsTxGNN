---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 1238
evidence_level: L5
indication_count: 10
---

# Tocilizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

> Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody originally developed for rheumatoid arthritis and later extended to giant cell arteritis, juvenile idiopathic arthritis and cytokine release syndrome.
> The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**,
> but the **2 dedicated Phase 2/3 trials** identified were both terminated for lack of efficacy, and the supporting literature is largely negative or inconclusive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (per approved-indication literature in evidence pack, e.g. PMID 19368420, PMID 41023525) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, tocilizumab is a humanized monoclonal antibody that blocks both membrane-bound and soluble IL-6 receptors, and belongs to the IL-6 receptor antagonist class. Its efficacy in rheumatoid arthritis is well established, and it has since been approved for giant cell arteritis and juvenile idiopathic arthritis — all IL-6-driven inflammatory joint/vascular diseases.

Ankylosing spondylitis (AS) shares a broad "inflammatory arthritis" family resemblance with rheumatoid arthritis, and IL-6 is elevated in AS patients, which is the mechanistic basis for the TxGNN prediction. However, the pathogenesis of axial spondyloarthritis is now understood to be driven predominantly by the TNF-α/IL-17 axis rather than IL-6, which is more central in RA and GCA. This is reflected directly in the clinical evidence: two purpose-built trials of tocilizumab in AS (NCT01209689, NCT01209702) were both **terminated** because interim results did not show the expected treatment effect.

In short, the mechanistic hypothesis is biologically plausible but has already been directly tested and did not pan out — this is a case where TxGNN's high similarity score reflects shared disease-family features (chronic inflammatory arthritis, IL-6 involvement) rather than a validated therapeutic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | RCT of tocilizumab 8mg/kg or 4mg/kg IV vs. placebo q4w in AS patients with inadequate response to prior TNF antagonist therapy; terminated early for lack of expected efficacy |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Seamless RCT in TNF-antagonist-naïve AS patients who failed NSAIDs; evaluated reduction in signs/symptoms and inhibition of structural damage; also terminated early for lack of efficacy |

Both dedicated Phase 2/3 trials of tocilizumab specifically in AS were stopped early due to insufficient treatment effect — this is direct but negative clinical evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | BUILDER-1/BUILDER-2 randomised placebo-controlled trials assessing short-term symptomatic efficacy of tocilizumab in AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-analysis | Medicine | Comparative effectiveness of biologic regimens for AS; positions IL-6 blockade relative to TNF/IL-17 therapies |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis (Cohort) | Clin Rheumatol | Risk of serious infections with biologics (including IL-6 inhibitors) in AS and non-radiographic axial spondyloarthritis RCTs |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | Short review on the rationale and limits of IL-6 antagonism specifically in AS |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Front Med | Two AS cases with AA amyloidosis successfully treated with tocilizumab, suggesting a niche role in a specific complication rather than core AS disease activity |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporos Int | Systemic bone effects of biologic therapies, including tocilizumab, in RA and AS |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Review | Joint Bone Spine | Biologic agents for AS beyond TNFα antagonists, including IL-6 pathway inhibitors |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clin Exp Rheumatol | General review of biologics in RA and AS, noting differing efficacy patterns between the two diseases |

---

## US Market Information

Tocilizumab is currently **not marketed** in this jurisdiction (market status: 未上市), and no license/NDA records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the IL-6 mechanism provides plausible biological rationale, the two purpose-designed Phase 2/3 RCTs directly testing tocilizumab in ankylosing spondylitis (both TNF-naïve and TNF-inadequate-responder populations) were terminated early for lack of efficacy. This constitutes direct negative clinical evidence outweighing the TxGNN similarity score.

**To proceed, the following is needed:**
- TFDA/regional label warnings and contraindications (currently a blocking data gap, DG001)
- Detailed mechanism of action documentation (DG002)
- Full unpublished results from NCT01209689/NCT01209702 to confirm whether any AS subpopulation (e.g., axial disease severity, amyloidosis complication) showed a positive signal despite overall trial termination
- Re-evaluation against higher-ranked or better-evidenced candidates in this pack (e.g., polyarticular JIA, rank 7, which has L1 evidence and an existing "Proceed with Guardrails" recommendation) before committing further resources to the AS indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

