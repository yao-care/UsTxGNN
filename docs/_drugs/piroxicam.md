---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 1050
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Adult Rheumatoid Arthritis/Osteoarthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is a long-acting oxicam-class NSAID historically used for adult rheumatic and osteoarthritic pain and inflammation. Among 10 TxGNN-predicted indications, the model's top 9 hits are ultra-rare genetic/dysplasia syndromes with **no mechanistic or evidentiary support** (explicitly flagged in the evidence pack as likely embedding artifacts); the only prediction with real clinical grounding is **Juvenile Idiopathic Arthritis (JIA)**, backed by **1 multicentre RCT, 1 open-label clinical trial, and 2 systematic reviews/network meta-analyses**. This report focuses on the JIA candidate as the only one warranting decision-stage evaluation.

> **Note on candidate selection**: TxGNN's rank-1 prediction (colobomatous microphthalmia–rhizomelic dysplasia syndrome, score 99.996%) and ranks 2–9 all carry `evidence_level: L5` and `recommendation: Hold`, with the pack's own rationale text stating they have "no known biological association" with piroxicam's COX-1/2 mechanism and no supporting literature/trials. JIA (rank 10) is the only candidate with `evidence_level: L2` and `recommendation: Proceed with Guardrails`, so it is treated as the substantive prediction for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Taiwan regulatory dataset (piroxicam has 0 TW licenses); internationally, piroxicam is a conventional NSAID indicated for adult rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis |
| Predicted New Indication | Juvenile Idiopathic Arthritis (JIA) |
| TxGNN Prediction Score | 99.93% (rank 2,538 of all disease candidates) |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses (TW) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this evidence pack (data gap DG002). Based on information embedded in the evidence pack's repurposing rationale, piroxicam is a COX-1/2 inhibitor that suppresses prostaglandin synthesis, producing anti-inflammatory, analgesic, and antipyretic effects — the standard NSAID mechanism used across the rheumatic disease spectrum.

JIA and adult rheumatoid arthritis share the same core inflammatory joint pathophysiology, and NSAIDs (including piroxicam specifically) have historically been used as symptomatic first-line therapy in both. This is not a novel mechanistic leap — it is a re-application of an established drug class to a pediatric variant of the same disease process.

Historical clinical evidence directly supports this: a 1986 multicentre double-blind crossover RCT compared piroxicam to naproxen in juvenile chronic arthritis, and a 1987 open-label trial evaluated piroxicam specifically in juvenile rheumatoid arthritis, alongside a dedicated pediatric pharmacokinetic study. However, piroxicam's long half-life and comparatively higher gastrointestinal/cutaneous toxicity have led regulatory bodies (e.g., EMA) to restrict its long-term use, which is why it has largely been superseded by other NSAIDs in current pediatric practice — a factor that should inform any repurposing evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no entries under `clinical_trials` or `ictrp_trials` for this indication in the evidence pack; supporting evidence exists only in the published literature below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT (multicentre, crossover) | British Journal of Rheumatology | 8-week double-blind crossover trial in 47 children with seronegative JCA; piroxicam vs. naproxen, no significant difference in efficacy |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Clinical Trial (open-label) | European Journal of Rheumatology and Inflammation | 26 children (age 3–25) randomized to piroxicam or naproxen for JRA; significant reduction in painful/swollen joint counts |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic Review / Network Meta-analysis | World Journal of Clinical Cases | Compares multiple NSAIDs (including piroxicam) for JIA efficacy and safety |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic Review / Network Meta-analysis | Indian Pediatrics | Comparative efficacy/safety of nine NSAIDs in JIA patients |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic Study | European Journal of Clinical Pharmacology | Steady-state PK of piroxicam (0.4 mg/kg once daily) in 10 children with rheumatic disease; half-life ~22–40h |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Review (pediatric drug safety) | Clinical Rheumatology | Long-term toxicity of NSAIDs/DMARDs in 117 children followed over ~8.6 years in a pediatric rheumatology clinic |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderärztliche Praxis | Discusses drug therapy of JCA, including piroxicam and sulfasalazine |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort | International Ophthalmology | Frequency/complications of chronic iridocyclitis in ANA-positive pauciarticular JCA (disease-context evidence) |

---

## Taiwan Market Information

No Taiwan license records exist for piroxicam in this evidence pack (`total_licenses: 0`, `market_status: 未上市`). Piroxicam is not currently marketed in Taiwan.

---

## Safety Considerations

Official TFDA warnings, contraindications, and drug-drug interaction data are unavailable in this evidence pack (blocking data gap DG001; DDI query returned `not_found`). Based on the literature included above:

- **Toxicity profile**: A pediatric long-term follow-up study (PMID 9890680) documented adverse events across 155 NSAID exposures in a rheumatology clinic cohort, informing the general pediatric NSAID safety context.
- **Regulatory restriction (noted in rationale)**: Piroxicam's long half-life and elevated GI/cutaneous adverse event rate have led to EMA restrictions limiting it to short-term, second-line use — relevant when considering chronic JIA management.

Please refer to the official package insert for complete and authoritative safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A multicentre RCT, an open-label pediatric trial, and two systematic reviews/network meta-analyses support piroxicam's historical efficacy in JIA/JCA, giving this candidate genuine (L2) evidentiary grounding — unlike the other 9 TxGNN predictions in this pack, which are unsupported and should be held. However, the blocking absence of TFDA label/safety data (DG001) and piroxicam's known long half-life/toxicity profile in pediatric long-term use mean this cannot proceed without further safety review.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert data — warnings, contraindications, DDI (DG001, blocking)
- Confirmed DrugBank MOA record (DG002)
- Updated pediatric dosing/safety comparison against NSAIDs currently approved for JIA (given piroxicam's EMA long-term use restriction)
- No further evaluation recommended for ranks 1–9 (rare dysplasia/genetic syndromes) unless new supporting evidence emerges — current data indicates these are TxGNN embedding artifacts, not credible repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

