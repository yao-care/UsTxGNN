---
layout: default
title: Technetium Tc-99M Sestamibi
parent: Model Prediction Only (L5)
nav_order: 1203
evidence_level: L5
indication_count: 10
monitor_inn: "TECHNETIUM TC-99M SESTAMIBI"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "cerebral infarction", "hypoalphalipoproteinemia", "cytomegalovirus infection", "Prinzmetal angina", "stroke disorder", "gastrin secretion abnormality", "cerebral arterial disease", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-14
description: "Technetium Tc-99M Sestamibi: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Not specified in the available license data"
---

# Technetium Tc-99M Sestamibi
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Technetium Tc-99m Sestamibi: From Diagnostic Imaging to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Technetium Tc-99m sestamibi is a diagnostic radiopharmaceutical supplied as an injectable kit, and the data compiled for this report do not list a specific approved indication for it.
The TxGNN model's top prediction is **homozygous familial hypercholesterolemia**, but **no clinical trials and no publications** support it.
The only prediction with any literature is **multiple endocrine neoplasia** (rank 2, **2 publications**), and that is a diagnostic use, not a therapeutic one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available license data |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, Tc-99m sestamibi is a lipophilic cation that accumulates in tissue in proportion to mitochondrial content and blood flow. It is used as an imaging agent, not as a lipid-modifying or therapeutic drug.

For homozygous familial hypercholesterolemia, no mechanism links a diagnostic tracer to cholesterol metabolism. The high TxGNN score is most likely an artifact of the knowledge graph. At most, myocardial perfusion imaging could help assess coronary disease in these patients. That would be a diagnostic use, not therapeutic repurposing.

The other top-10 predictions follow a similar pattern:
- **Lipid disorders** (hypoalphalipoproteinemia, obsolete familial combined hyperlipidemia): no plausible link to a diagnostic tracer. The "obsolete" disease term should be excluded from further review.
- **Cerebrovascular conditions** (cerebral infarction, stroke disorder, cerebral arterial disease): the three overlap and appear to be the same graph-derived artifact. Sestamibi has no neuroprotective or thrombolytic action.
- **Cytomegalovirus infection**: no antiviral mechanism. Its status as a P-glycoprotein substrate does not translate into antiviral activity.
- **Prinzmetal angina**: perfusion imaging could in principle show transient ischemia, but this is diagnostic only and unsupported by retrieved evidence.
- **Gastrin secretion abnormality**: only a loose association via gastrinoma in MEN1, and neuroendocrine imaging relies on other agents.
- **Multiple endocrine neoplasia** (rank 2): the most biologically plausible. Sestamibi accumulates in mitochondria-rich, hyperfunctioning parathyroid tissue, which is relevant to the hyperparathyroidism seen in MEN1 and MEN2A. This is largely an extension of existing parathyroid imaging, and sensitivity is reduced in multiglandular disease, which is typical of MEN.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or for any other prediction in the top 10.

## Literature Evidence

The top-ranked prediction (homozygous familial hypercholesterolemia) has no related literature. The only literature in the data supports the rank 2 prediction, multiple endocrine neoplasia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10896380](https://pubmed.ncbi.nlm.nih.gov/10896380/) | 2000 | Cohort (presumed, retrospective surgical series) | Archives of Surgery | Preoperative sestamibi scanning in MEN1 patients with recurrent hyperparathyroidism. Little or no value when 4 or more hypertrophied glands are present. High sensitivity and specificity with SPECT once 3 or more glands have been removed, which supports limited re-exploration. |
| [10807279](https://pubmed.ncbi.nlm.nih.gov/10807279/) | 2000 | Cohort (presumed, retrospective surgical series) | Archives of Surgery | Combined use of sestamibi scintigraphy, intraoperative gamma probe and rapid parathyroid hormone assay in hyperparathyroidism. Hypothesized to be particularly useful in patients needing reoperation. Not MEN-specific. |

Both study designs are presumed from truncated titles, and MEN-specific cohort sizes cannot be confirmed.

## US Market Information

All three authorizations are cancelled, and none is currently valid. No approved indication text was available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA079157 | Kit for the Preparation of Technetium Tc99m Sestamibi (Sun Pharmaceutical Industries) | Injection | Not available (cancelled) |
| ANDA078809 | Kit for the Preparation of Technetium Tc99m Sestamibi (Cardinal Health 414) | Injection, powder, lyophilized, for solution | Not available (cancelled) |
| ANDA078806 | Technetium Tc 99m Sestamibi (Jubilant Draximage) | Injection, powder, for solution | Not available (cancelled) |

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interactions were found in the data compiled for this report, and no disease contraindications were identified from the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical, literature or mechanistic support. The high score is most likely a knowledge-graph artifact, because a diagnostic tracer has no lipid-modifying action. The only prediction with literature, multiple endocrine neoplasia, concerns parathyroid localization, a diagnostic use that largely extends existing imaging practice rather than a new therapy. It is best treated as a research question (L3), not a repurposing candidate.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Mechanism of action data, for example from DrugBank
- For MEN, full-text review of the two studies to confirm design and MEN-specific cohort sizes, and a decision on whether a diagnostic-use question is in scope
- Confirmation of why all US licenses are cancelled, and whether other marketed sestamibi products exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

