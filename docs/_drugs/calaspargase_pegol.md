---
layout: default
title: Calaspargase Pegol
parent: 僅模型預測 (L5)
nav_order: 485
evidence_level: L5
indication_count: 4
---

# Calaspargase Pegol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Calaspargase Pegol: From Acute Lymphoblastic Leukemia to Insomnia

## One-Sentence Summary

Calaspargase pegol is a PEGylated asparaginase used in multi-agent chemotherapy for Acute Lymphoblastic Leukemia (ALL), acting primarily by depleting circulating asparagine to starve protein synthesis-dependent malignant lymphoblasts. The TxGNN model predicts it may be effective for **Insomnia** with a score of 99.80%, yet **no clinical trials and no published literature** support this direction — the prediction is assessed as likely graph neural network noise rather than a genuine biological signal. This report covers all four top-ranked predictions, all of which are recommended as **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) — internationally approved; no licenses found in this system |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| US Market Status | Not marketed (0 license records) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Based on mechanistic analysis, this prediction is **not biologically plausible**. Detailed MOA data is not available in the current evidence pack, but calaspargase pegol is well characterized as an enzymatic asparaginase — it depletes serum asparagine (Asn) to block protein synthesis in Asn-dependent tumor cells (lymphoblasts). This is the defining pharmacological mechanism of the asparaginase drug class.

Sleep regulation operates through entirely distinct neurobiological pathways: adenosine accumulation, melatonin synthesis from tryptophan, GABAergic inhibitory tone, and circadian transcription factor cycling. None of these pathways share a meaningful intersection with asparagine depletion. There is no published hypothesis, preclinical model, or mechanistic rationale connecting asparaginase activity to insomnia treatment.

The TxGNN score of 99.80% for insomnia is therefore suspected to reflect **cross-domain graph neighborhood noise** — an artifact of the graph neural network picking up distant, non-biological co-occurrence edges — rather than a real repurposing opportunity. This interpretation is strongly supported by the complete absence of any clinical trial or literature evidence, and by the systematic false-positive pattern observed across all four top-ranked predictions (see Conclusion section).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No license records are available for calaspargase pegol in this system (0 NDAs, market status: not marketed).

> **Note for Review Teams**: Calaspargase pegol (brand name Asparlas®) received FDA approval in December 2018 (NDA 761102) for use as a component of multi-agent chemotherapy for ALL in pediatric and young adult patients (≥1 month to <22 years). If this record shows zero licenses, it may indicate a data pipeline gap rather than a true absence of regulatory approval. Verification against the FDA Orange Book is recommended before concluding the drug is unapproved.

---

## Cytotoxicity

Calaspargase pegol is an antineoplastic agent (asparaginase class) and requires the following assessment:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Asparaginase class (enzymatic depletion of circulating L-asparagine) |
| Myelosuppression Risk | Low (myelosuppression is not a primary class toxicity; bone marrow is not the main target organ) |
| Emetogenicity Classification | Low |
| Monitoring Items | Coagulation panel (PT, aPTT, fibrinogen, antithrombin III), liver function (ALT, AST, total bilirubin, albumin), pancreatic enzymes (amylase, lipase), blood glucose, CBC with differential |
| Handling Protection | Must follow cytotoxic drug handling regulations; anaphylaxis risk requires emergency resuscitation equipment available at the bedside during every administration |

> **Class-effect safety concerns** (for clinical reference, pending formal label data): hypersensitivity/anaphylaxis; acute pancreatitis; coagulopathy (both thrombotic and hemorrhagic); hepatotoxicity; hyperglycemia. Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications for calaspargase pegol lack any supporting clinical or literature evidence (all L5), and mechanistic analysis identifies two distinct false-positive patterns that explain the high model scores:

| Rank | Predicted Indication | TxGNN Score | False-Positive Pattern |
|------|---------------------|-------------|------------------------|
| 1 | Insomnia | 99.80% | Cross-domain graph noise — no mechanistic bridge between asparagine depletion and sleep regulation |
| 2 | Factor V excess with spontaneous thrombosis | 99.25% | ADR misread as therapeutic signal — asparaginase depletes coagulation proteins (adverse effect), not Factor V specifically |
| 3 | Heparin cofactor 2 deficiency | 99.24% | Mechanism direction reversed — asparaginase suppresses HCII synthesis, worsening not treating HCII deficiency |
| 4 | Antithrombin deficiency type 2 | 99.21% | Strongest ADR-as-treatment false positive — AT-III depletion is a well-documented severe adverse effect of asparaginase therapy; using this drug to treat AT deficiency would directly aggravate the condition |

Predictions 2–4 represent a particularly important failure mode: the knowledge graph encodes strong asparaginase–coagulation edges derived from **adverse drug reaction** relationships, but the GNN treats them as potential therapeutic edges. This is a known structural limitation of KG-based drug repurposing models.

**To proceed, the following is needed:**

- Verify US market status against the FDA Orange Book (possible data pipeline gap flagged above)
- Retrieve complete MOA data from DrugBank API (Data Gap DG002) to formally document asparagine depletion as the primary mechanism
- Flag this candidate as a **confirmed false-positive case study** for TxGNN model calibration — the ADR-edge misclassification pattern (Ranks 2–4) is reproducible and worth reporting to the model development team
- No further evidence collection for the insomnia indication is warranted at this time; resources should be redirected to higher-priority candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

