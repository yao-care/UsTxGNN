---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 728
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From Rheumatoid Arthritis/Osteoarthritis to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a non-selective COX-1/COX-2 inhibiting NSAID with long-established use in rheumatic and musculoskeletal pain (rheumatoid arthritis, osteoarthritis). Among the 10 candidate indications TxGNN surfaced for this drug, only **Ankylosing Spondylitis** is backed by real evidence — **20 publications, including at least 7 head-to-head randomized controlled trials** spanning 1974–2012 — while the other 9 candidates (all rare skeletal dysplasias) have zero clinical or literature support and are flagged in the evidence pack itself as likely knowledge-graph embedding artifacts, not genuine repurposing signals.

*Note: the highest TxGNN-scored candidate (acromesomelic dysplasia, Hunter-Thompson type, score 99.99%) is not used as the report subject — it, and 7 other top-10 candidates, have no clinical trials, no literature, and mechanistic rationales explicitly noting no biological link to NSAID pharmacology. Ankylosing Spondylitis (rank 8 by TxGNN score, but the only clinically substantiated candidate) is presented here instead.*

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack; literature identifies flurbiprofen as an established NSAID for rheumatoid arthritis, osteoarthritis, and allied rheumatic conditions |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Flurbiprofen is a non-selective COX-1/COX-2 inhibitor — a conventional phenylalkanoic-acid NSAID — that suppresses prostaglandin synthesis to produce anti-inflammatory and analgesic effects. This is the same mechanism by which other NSAIDs (indomethacin, naproxen, phenylbutazone) are used to manage the axial inflammation and joint pain of ankylosing spondylitis.

Ankylosing spondylitis and the drug's established rheumatic-disease indications share the same underlying inflammatory pathology, so extending flurbiprofen's use to AS involves no mechanistic leap. In fact, the evidence base shows this is not a novel repurposing hypothesis at all: multiple double-blind RCTs from the 1970s–80s directly compared flurbiprofen against indomethacin, phenylbutazone, and naproxen in AS patients and found comparable efficacy. TxGNN's prediction here effectively re-discovers a clinically confirmed use rather than proposing new pharmacology — which is why this candidate, unlike the other 9 in this evidence pack, clears an L1 evidence bar.

By contrast, the remaining top-ranked candidates (acromesomelic dysplasia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, myosclerosis, brachyolmia, etc.) are structural/developmental or fibrotic disorders with no inflammatory component NSAIDs act on. Each has zero registered trials and zero literature; the evidence pack's own rationale attributes their high TxGNN scores to graph proximity within a skeletal/joint-disease cluster rather than genuine pharmacological relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered (all supporting studies below predate modern trial registries such as ClinicalTrials.gov).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT | British Medical Journal | Double-blind crossover in 35 AS patients: flurbiprofen (150 mg/day) approached the efficacy of phenylbutazone (300 mg/day) and was well tolerated |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | RCT | Annals of the Rheumatic Diseases | Double-blind crossover of indomethacin, flurbiprofen, and placebo in AS |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT | European Journal of Clinical Pharmacology | Parallel double-blind trial in 27 active AS patients: flurbiprofen and phenylbutazone equally effective for pain/tenderness relief |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT | Current Medical Research and Opinion | Parallel double-blind trial in 26 AS patients: flurbiprofen (150–200 mg/day) vs indomethacin (75–100 mg/day), equally effective |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT | Southern Medical Journal | Companion publication: flurbiprofen vs indomethacin in 26 active AS patients, equally effective, well tolerated |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT | New Zealand Medical Journal | 4-week double-blind crossover, 30 AS patients: flurbiprofen 200 mg/day vs naproxen 750 mg/day, comparable efficacy; more side effects with flurbiprofen |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT | American Journal of Medicine | 26-week double-blind trial, 90 AS patients: flurbiprofen 200 mg/day as effective as phenylbutazone 300 mg/day |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT | American Journal of Medicine | 26-week double-blind trial, 57 AS patients: flurbiprofen 100–200 mg/day effectively controlled pain vs indomethacin |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Cohort | American Journal of Medicine | Pooled safety analysis of 9 Phase III trials, 1,677 patients (941 on flurbiprofen) across AS/OA/RA: no clinically significant liver or kidney signal |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Comprehensive review of flurbiprofen pharmacology and efficacy across rheumatoid arthritis, degenerative joint disease, and ankylosing spondylitis |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Seven-plus double-blind RCTs and a large pooled safety cohort, spanning nearly two decades, consistently show flurbiprofen is effective and tolerable for ankylosing spondylitis at doses comparable to other established NSAIDs — this is strong (L1) historical evidence, not a speculative signal. However, Taiwan-specific regulatory and safety data are completely absent (0 TFDA licenses, no label warnings/contraindications, no DDI data on file), so this cannot advance to a full Go without local safety documentation.

**To proceed, the following is needed:**
- TFDA-approved product label (warnings/precautions and contraindications) — download and parse from TFDA's official site (blocking gap, DG001)
- DrugBank-sourced mechanism-of-action confirmation via API query (DG002)
- Confirmation of Taiwan market/import pathway, since flurbiprofen currently holds zero licenses locally
- The other 9 TxGNN-flagged candidates (all rare skeletal dysplasias) should remain on Hold — no clinical, literature, or mechanistic support exists for pursuing them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

