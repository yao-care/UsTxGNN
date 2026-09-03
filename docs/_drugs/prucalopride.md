---
layout: default
title: Prucalopride
parent: 僅模型預測 (L5)
nav_order: 1097
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Chronic Constipation to Amyloidosis-Associated Intestinal Pseudo-Obstruction

## One-Sentence Summary

> Prucalopride is a selective 5-HT4 receptor agonist known clinically for promoting gastrointestinal motility in chronic constipation.
> Among 10 TxGNN-predicted indications, only **amyloidosis-related gastrointestinal dysmotility** (chronic intestinal pseudo-obstruction) has any supporting literature — **2 case/review publications**, no clinical trials — while the remaining 8 candidates, including the highest-scoring prediction (hypoalphalipoproteinemia), have **no mechanistic or evidentiary support** and are flagged as algorithmic noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic constipation (per known 5-HT4 agonist pharmacology, cited in evidence-pack rationale text; no license record available) |
| Predicted New Indication | Amyloidosis-associated intestinal pseudo-obstruction (rank 6, highest-evidence candidate) |
| TxGNN Prediction Score | 99.62% (rank 9,662 of full candidate list) |
| Evidence Level | L4 (mechanism/case-report level only) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for prucalopride is not available in this evidence pack (data gap, source: DrugBank, not yet retrieved). Based on the information present in the repurposing rationale fields, prucalopride is a selective 5-HT4 receptor agonist used clinically to enhance gastrointestinal motility in chronic constipation.

Amyloid deposits can infiltrate the enteric autonomic nervous plexus, producing chronic intestinal pseudo-obstruction (CIPO) — a motility failure state. This shares a plausible pathophysiological overlap with prucalopride's prokinetic mechanism, giving the prediction some biological rationale. However, the two supporting publications only document the *clinical presentation and diagnostic challenges* of amyloidosis-related CIPO; neither studies prucalopride treatment directly. This is therefore an indirect, mechanism-based hypothesis rather than treatment evidence.

By contrast, the TxGNN model's *highest-scoring* prediction (hypoalphalipoproteinemia, rank 1) and six other candidates (homozygous familial hypercholesterolemia, duodenal ulcer, oral candidiasis, obsolete familial combined hyperlipidemia, strongyloidiasis, HIV infection, acquired amyloid peripheral neuropathy) have **no mechanistic link, no clinical trials, and no literature**. The evidence pack itself characterizes these as algorithmic noise lacking biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*(for amyloidosis-associated intestinal pseudo-obstruction, rank 6 — the only candidate with literature support)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case Report | Cureus | 61-year-old man with chronic nausea, vomiting, and abdominal pain from recurrent small bowel dilation; extensive workup for CIPO ultimately pointed toward amyloidosis as an underlying cause, illustrating diagnostic difficulty rather than treatment outcome. |
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Review | Turkish J Gastroenterol | Notes that specific GI motility disorders (gastroparesis, CIPO, colonic inertia) are frequently misdiagnosed as functional GI disorders in Asia due to low physician awareness; does not address prucalopride use. |

A second candidate, primary (AL-type) amyloidosis (rank 9), shares the same review article (PMID 34231480) with the same limitation — descriptive of disease mechanism, not treatment evidence.

---

## Other TxGNN-Predicted Indications (Low Confidence, Not Pursued)

The remaining 8 of 10 predictions carry TxGNN scores in a similar range (99.5–99.8%) but have **no clinical trials, no literature, and no stated mechanistic link** — all rated L5 / Hold:

| Rank | Disease | TxGNN Score | Note |
|------|---------|------|------|
| 1 | Hypoalphalipoproteinemia | 99.82% | Highest score overall; no biological plausibility identified |
| 2 | Homozygous familial hypercholesterolemia | 99.67% | No mechanistic link |
| 3 | Duodenal ulcer | 99.65% | No link to Hp infection or acid secretion pathways |
| 4 | Oral candidiasis | 99.64% | No plausible mechanism |
| 5 | Familial combined hyperlipidemia (obsolete term) | 99.62% | Obsolete disease classification; recommend exclusion |
| 7 | Strongyloidiasis | 99.60% | No antiparasitic mechanism |
| 8 | HIV infection | 99.60% | No antiviral/immunomodulatory link |
| 10 | Acquired amyloid peripheral neuropathy | 99.55% | Conceptually adjacent to CIPO signal but unsupported by evidence |

These are listed for transparency but do not warrant further evaluation at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags TFDA/FDA warning and contraindication data as a **Blocking** data gap — DG001 — preventing entry into formal safety screening (S1) for any candidate in this set.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only 1 of 10 predicted indications (amyloidosis-associated intestinal pseudo-obstruction, plus its closely related primary-amyloidosis variant) has any literature support, and that support is mechanism-descriptive rather than treatment evidence — no clinical trials exist for prucalopride in this indication. The remaining candidates, including the top TxGNN-scored prediction, show no biological plausibility. Combined with missing MOA and regulatory safety data, this candidate set does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (DG001 — blocking; required before any safety screening)
- Confirmed mechanism of action data from DrugBank (DG002)
- Preclinical or clinical studies directly testing prucalopride in amyloidosis-related GI dysmotility (currently only disease-mechanism literature exists)
- Case series or real-world evidence of prucalopride use in CIPO/amyloidosis patients, if this signal is to be pursued as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

