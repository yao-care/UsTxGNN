---
layout: default
title: Talc
parent: 僅模型預測 (L5)
nav_order: 1195
evidence_level: L5
indication_count: 10
---

# Talc
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

# TALC (DB09511): From No Approved Indication to Predicted Thrombotic Disease Signal

## One-Sentence Summary

> TALC (DrugBank DB09511) has no approved indication and no marketing authorization on file in this jurisdiction — mechanism of action data is also unavailable.
> The TxGNN model's top prediction is that TALC could be effective for **Thrombotic Disease** (score 99.85%), but the underlying literature describes talc-induced thrombosis in intravenous drug users rather than any treatment effect, making this a likely **reversed-causality artifact** rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file — drug is not currently marketed in this jurisdiction |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (per model scoring) — **but see caveat below: the underlying studies document toxicity, not efficacy** |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no mechanism of action data is available for TALC, and it holds no approved indication or license in this jurisdiction. Based on the literature retrieved, this prediction does **not** appear pharmacologically reasonable.

All of the highest-relevance publications describe talc as a **cause** of thrombotic and vaso-occlusive pathology — not a treatment for it. Talc particles introduced intravenously (typically from crushed oral tablets injected by drug users) embolize into small pulmonary, retinal, and cerebral vessels, producing angiothrombotic pulmonary granulomatosis, pulmonary hypertension, retinal/cerebral microembolism, and even ischemic infarction. This is the well-documented "talc-induced angiothrombotic" toxicity syndrome, distinct from talc's one clinically established pharmacological use (as a sclerosing agent instilled into the pleural space for pleurodesis, where it deliberately induces local inflammation and adhesion).

The most plausible explanation for the high TxGNN score is that the knowledge graph embedding conflated "talc is associated with thrombotic disease" (as an adverse/causal relationship) with "talc treats thrombotic disease" — a known failure mode for graph-based repurposing models when adverse-event literature dominates the co-occurrence signal. No mechanistic, anticoagulant, or antithrombotic rationale supports this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Case series | J Can Assoc Radiol | Talc granulomatosis and angiothrombotic pulmonary hypertension in drug addicts — talc as causal agent |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Case report | Arch Neurol | Systemic talc granulomatosis with ischemic medullary infarction after IV drug injection |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Case report | Am J Med Sci | Retinal and cerebral microembolization of talc in a drug abuser |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Case report | Rev Clin Esp | Angiothrombotic pulmonary granulomatosis in IV drug addicts caused by injected talc |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Case series/Review | Arch Pathol Lab Med | Talc/cellulose-induced pulmonary vascular thrombosis and granulomatosis from crushed-tablet IV injection |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Case report | Tex Heart Inst J | Trousseau syndrome (malignancy-associated thrombosis); no direct talc mechanism, keyword co-occurrence only |
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Review | Curr Opin Oncol | SVC syndrome secondary to catheter-related thrombosis; talc not directly implicated |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Observational | Int Ophthalmol | Notes "talc retinopathy" among vaso-occlusive retinal diseases; not a treatment context |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Case report | Dtsch Med Wochenschr | Acute right heart failure after IV heroin/flunitrazepam injection (talc-adulterant context) |
| [8010794](https://pubmed.ncbi.nlm.nih.gov/8010794/) | 1994 | Case series | Ann Thorac Surg | VATS for chylothorax; tangential mention of pleurodesis, not thrombotic disease treatment |

---

## US Market Information

TALC is not currently marketed and has no NDA or license on file in this jurisdiction (0 licenses recorded).

---

## Other TxGNN-Predicted Indications (Ranks 2–10)

For context, TxGNN generated 10 candidate indications for TALC in this evidence pack. All received a **Hold** recommendation:

| Rank | Disease | Score | Evidence Level | Key Issue |
|------|---------|-------|-----------------|-----------|
| 2 | Exostosis | 99.53% | L5 | No literature or trials; no plausible mechanism |
| 3 | Rheumatoid arthritis | 99.53% | L4 | Literature shows talc/silica as an autoimmune **trigger** (silicosis, ASIA syndrome), not a treatment |
| 4 | Bronchitis | 99.53% | L4 | Literature shows talc **inhalation causes** bronchitis/pneumoconiosis — reversed causality |
| 5 | Heparin cofactor 2 deficiency | 99.39% | L5 | No evidence; rare genetic disorder unrelated to talc pharmacology |
| 6 | Factor 5 excess w/ spontaneous thrombosis | 99.36% | L5 | No evidence; no plausible mechanism |
| 7 | Antithrombin deficiency type 2 | 99.30% | L5 | No evidence; no plausible mechanism |
| 8 | Vein disease | 99.19% | L4 | Retrieved trials do not use talc (keyword coincidence); literature is adverse-effect case series |
| 9 | Fibromyalgia | 99.15% | L5 | Single unrelated case report (glove-powder peritonitis) |
| 10 | Myositis fibrosa | 99.15% | L5 | No evidence; theoretical fibrosis analogy only |

No candidate in this set has genuine efficacy evidence. Several (thrombotic disease, rheumatoid arthritis, bronchitis, vein disease) are best explained as the model mistaking documented **adverse effects/toxicity** of talc for therapeutic associations.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: no drug label warnings, contraindications, or safety label data were available in this evidence pack (a blocking data gap — see below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked and majority of predicted indications for TALC are unsupported by genuine treatment evidence — the literature that does exist largely documents talc-induced toxicity (angiothrombotic pulmonary disease, pneumoconiosis, autoimmune reactions from inhalation/IV exposure) rather than therapeutic benefit, and no clinical trials support any of the 10 candidates. This is consistent with a knowledge-graph artifact rather than a real repurposing opportunity.

**To proceed, the following is needed:**
- Official product label / warnings and contraindications data (currently a **blocking** data gap — required before any S1 safety screening)
- Verified mechanism of action data from DrugBank or equivalent source
- Independent pharmacological rationale for any candidate indication beyond TxGNN's raw score, given the demonstrated risk of reversed-causality signals in this dataset
- If any candidate is pursued further, manual re-classification of the "pending" literature entries to confirm whether they describe efficacy or adverse effects before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

