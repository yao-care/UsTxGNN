---
layout: default
title: Flavoxate
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 8
---

# Flavoxate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Flavoxate: From Urinary Urgency/Frequency to Neurogenic Bladder

## One-Sentence Summary

Flavoxate is a direct-acting (musculotropic) urinary tract antispasmodic historically used to relieve dysuria, urgency, frequency, and nocturia associated with lower urinary tract irritation. The TxGNN model screened 8 candidate indications; among these, **Neurogenic Bladder** shows the strongest mechanistic overlap with flavoxate's known pharmacology (detrusor smooth-muscle relaxation), but currently **0 clinical trials** and **0 publications** support this specific indication in this evidence pack. The model's single highest-scoring hit (ADHD, inattentive type) was independently flagged by the analysis itself as likely model noise with no plausible mechanism, and is not carried forward as the primary candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug not marketed in Taiwan; no TFDA license record available) |
| Predicted New Indication | Neurogenic Bladder (obsolete term, per source ontology) |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Taiwan Market Status (TFDA) | 未上市 (Not Marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

> **Note on candidate selection:** This Evidence Pack (`TW-DB01148-multi`) contains **8** TxGNN-predicted indications for flavoxate, all rated **L5** with **zero** supporting trials or literature. The top-ranked hit by raw score (ADHD, inattentive type, 99.75%) was assessed in the source rationale as a probable knowledge-graph artifact — flavoxate has no known central dopaminergic/noradrenergic activity, so no biologically plausible link exists. We report **Neurogenic Bladder** (rank 6, decision stage S1) as the lead candidate instead, since it aligns with flavoxate's documented peripheral pharmacology. See the table below for all 8 candidates.

### Other Candidate Indications Screened

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|------------------|------|
| 1 | ADHD, inattentive type | 99.75% | L5 | Hold | Likely model noise — no CNS mechanism |
| 2 | Irritable Bowel Syndrome | 99.74% | L5 | Research Question | Plausible smooth-muscle class analogy (vs. mebeverine/alverine); unverified |
| 3 | Specific Developmental Disorder | 99.56% | L5 | Hold | Non-specific disease term, no mechanistic link |
| 4 | ADHD (general) | 99.39% | L5 | Hold | Same issue as rank 1 |
| 5 | Cauda Equina Syndrome | 99.27% | L5 | Hold | Surgical emergency; symptomatic overlap only |
| **6** | **Neurogenic Bladder (obsolete)** | **99.13%** | **L5** | **Research Question** | **Strongest mechanistic fit — lead candidate** |
| 7 | Gastroduodenitis | 99.12% | L5 | Hold | Symptomatic overlap only, no disease-modifying link |
| 8 | Peptic Ulcer Disease | 99.10% | L5 | Hold | Outdated anticholinergic-adjuvant rationale |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank was queried successfully but the specific MOA field was not returned; see Data Gap DG002). Based on generally known pharmacology, flavoxate is a musculotropic (direct-acting) spasmolytic with weak anticholinergic and local anesthetic-like activity, acting directly on urinary tract smooth muscle — most notably the bladder detrusor — to relieve spasm-related irritative voiding symptoms such as urgency, frequency, dysuria, and nocturia.

Because this established pharmacology centers specifically on detrusor smooth-muscle relaxation, the model's prediction of **Neurogenic Bladder** is mechanistically coherent: this condition is characterized by dysregulated detrusor activity (overactivity, non-compliance, or dyssynergia) causing urgency, frequency, and incontinence — the same symptom domain flavoxate is already used to manage. In contrast, the model's absolute top-ranked candidates (ADHD subtypes, developmental disorders) require a central-nervous-system mechanism that flavoxate does not possess, and are best interpreted as embedding-level noise rather than genuine repurposing signals.

No clinical trial or literature evidence for flavoxate specifically in neurogenic bladder was found in this data cutoff. This absence likely reflects a data/indexing gap rather than mechanistic implausibility — flavoxate's peripheral antispasmodic use already overlaps heavily with symptoms seen in neurogenic bladder, making a targeted literature search a reasonable next step rather than a dead end.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Flavoxate has **0** TFDA licenses on record and is currently **not marketed** in Taiwan (`market_status: 未上市`). No product name, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA label warnings/contraindications retrieval is flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any Stage 1 (S1) safety screening can proceed. A drug-drug interaction (DDI) database query also returned no results (`not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 8 candidate indications are rated L5 (model prediction only), with zero supporting clinical trials or literature across the board, and flavoxate is not currently marketed in Taiwan. A Blocking-severity data gap (TFDA label/warnings, DG001) means the drug cannot yet pass initial safety screening (S1), so no candidate — including the mechanistically favored Neurogenic Bladder — can advance beyond a research question at this time.

**To proceed, the following is needed:**
- Retrieve TFDA label warnings/contraindications (DG001 — Blocking; required before any S1 safety screening)
- Retrieve full DrugBank MOA text via API to confirm mechanistic detail (DG002 — High)
- Targeted literature/clinical-trial search using alternate terminology (e.g., "neurogenic detrusor overactivity," "overactive bladder, neurogenic") since the exact TxGNN disease label may not match how existing studies are indexed
- Drug-drug interaction (DDI) data source re-query, as the current lookup returned no results
- Confirmation of flavoxate's original approved indication(s), which are not populated in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

