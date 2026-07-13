---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: From Analgesic Use to Ankylosing Spondylitis

## One-Sentence Summary

Diflunisal is a difluorophenyl derivative of salicylic acid in the NSAID class, historically used for mild-to-moderate pain relief and musculoskeletal inflammation.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis** — the highest-evidence prediction among all candidates — with **0 clinical trials** and **7 publications** supporting this direction, including a 1986 double-blind controlled trial comparing diflunisal directly against phenylbutazone in AS patients.

> **Ranking note:** The highest TxGNN-scored prediction (rank 1) is acromesomelic dysplasia, Hunter-Thompson type (score 99.99%), a rare genetic skeletal disorder with no mechanistic connection to COX inhibition and no supporting clinical evidence. Ankylosing spondylitis (rank 5, score 99.98%) is featured here as the most clinically actionable and biologically plausible prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record (no US NDA found) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.98% (overall rank #856 among all drug–disease pairs) |
| Evidence Level | L3 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved from the available sources. Based on known pharmacological information, diflunisal belongs to the NSAID class as a difluorophenyl salicylate. Its anti-inflammatory and analgesic activity is mediated through inhibition of cyclooxygenase (COX-1 and COX-2) enzymes, which reduces prostaglandin E₂ (PGE₂) synthesis — the central mediator of joint inflammation and pain.

Ankylosing spondylitis (AS) is a chronic inflammatory arthritis of the axial skeleton, strongly associated with HLA-B27, characterized by elevated PGE₂ and other inflammatory mediators driving spinal enthesitis and progressive ankylosis. NSAIDs are the universally recognized first-line pharmacological treatment for AS: by suppressing PGE₂ production, they reduce axial pain, morning stiffness, and inflammatory load. The mechanistic rationale for diflunisal in AS is therefore direct and class-consistent.

Critically, this is not merely a class inference. A 12-week double-blind randomized controlled trial (PMID 3524970) and a 48-week prospective cohort study (PMID 4062389) both directly enrolled AS patients receiving diflunisal — demonstrating that diflunisal improved AS symptom severity comparable to phenylbutazone, with diflunisal showing a more rapid analgesic response. This body of work, though dated, provides stronger direct biological justification than most drug repurposing candidates at equivalent TxGNN score levels.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | Controlled comparative trial | Clinical Rheumatology | 12-week double-blind RCT + 36-week open extension in 38 AS patients: diflunisal 500 mg BID vs phenylbutazone 200 mg BID; both effective, diflunisal showed more pronounced and rapid analgesic onset |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Prospective cohort | Annals of the Rheumatic Diseases | 48-week longitudinal study in 38 AS patients on diflunisal or phenylbutazone; serum IgA correlated with disease activity markers including chest expansion and lumbar flexion index |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Cross-sectional study | The Journal of Rheumatology | Spirometric evaluation in 33 AS patients treated with diflunisal or phenylbutazone over 48 weeks; assessed NSAID impact on restrictive pulmonary function impairment caused by thoracic ankylosis |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Drug review | Clinical Pharmacy | Review of diclofenac sodium pharmacology and clinical efficacy in rheumatic diseases including AS; contextual NSAID class evidence |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Drug review | Drugs | Comprehensive review of diclofenac for AS, rheumatoid arthritis, and pain; 75–150 mg/day comparable to aspirin and indomethacin in rheumatic conditions |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Drug review | Drugs | Review of naproxen efficacy in rheumatic diseases; establishes propionic acid derivatives as preferred NSAID class — relevant comparative context for salicylate-class diflunisal |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Drug review | Drugs | Review of pirprofen as NSAID for AS, rheumatoid arthritis, and musculoskeletal disorders; contextual NSAID class comparison |

> **Note:** PMIDs 2670397, 6772422, 387372, and 3539573 concern other NSAIDs (diclofenac, naproxen, pirprofen), not diflunisal directly. They provide class-level context. The three direct diflunisal-in-AS studies are PMIDs 3524970, 4062389, and 3546687.

---

## US Market Information

No US NDA records found for diflunisal. The drug is currently not marketed in the United States.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Diflunisal has L3-level evidence for ankylosing spondylitis — including a direct double-blind comparative trial enrolling 38 AS patients — and its COX-inhibitor mechanism aligns precisely with the established NSAID standard of care for AS. However, the evidence base is dated (1980s), no modern RCT or placebo-controlled trial exists, and diflunisal currently holds no US market approval, creating a high evidence-gap risk before any advancement.

**To proceed, the following is needed:**

- **Retrieve MOA data from DrugBank** (DG002): Formal mechanism-of-action documentation to support regulatory submissions and mechanistic sections
- **Retrieve US FDA package insert** (DG001): Warnings, contraindications, and full safety labeling required before any S1 safety evaluation
- **Clarify current global regulatory status:** Confirm whether diflunisal retains approval in any jurisdiction (EU, Japan, etc.) and identify the reason for US market absence
- **Commission a modern systematic review:** The existing evidence dates to 1985–1986; a systematic search for any subsequent diflunisal use in spondyloarthropathy or AS is needed
- **Assess comparative safety profile vs modern NSAIDs in AS:** Evaluate GI, cardiovascular, and renal risk relative to currently preferred agents (celecoxib, naproxen, indomethacin) in the AS population
- **Evaluate commercial viability:** Assess IP landscape, manufacturing feasibility, and whether a repositioning development pathway (505(b)(2) or similar) is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

