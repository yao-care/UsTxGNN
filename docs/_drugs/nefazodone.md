---
layout: default
title: Nefazodone
parent: 僅模型預測 (L5)
nav_order: 958
evidence_level: L5
indication_count: 2
---

# Nefazodone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nefazodone: From Depression to Migraine Disorder

## One-Sentence Summary

Nefazodone is a serotonin antagonist and reuptake inhibitor (SARI-class), historically used as an antidepressant. The TxGNN model predicts potential efficacy for **Migraine Disorder** (score 99.60%), but this is currently supported only by **3 narrative review articles** and **no dedicated clinical trials** — the evidence is mechanistic/hypothesis-level, not clinically validated.

> **Note on original indication**: This evidence pack does not contain confirmed original-indication or MOA data for nefazodone (flagged as data gaps DG001/DG002 below). "Depression" reflects the drug's known SARI pharmacological class as referenced in the repurposing rationale, not a sourced field in this pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (inferred from SARI drug class; not independently confirmed in this evidence pack) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (mechanism/literature-level, no dedicated clinical trials) |
| Taiwan (TFDA) Market Status | 未上市 (Not Marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nefazodone is currently a data gap (DG002) in this evidence pack. Based on the repurposing rationale available, nefazodone is described as a 5-HT2A receptor antagonist combined with weak serotonin/norepinephrine reuptake inhibition (SARI class).

Serotonergic modulation has pharmacological plausibility in migraine prevention — other antidepressant classes (TCAs, SNRIs) already carry migraine-prophylaxis indications as precedent. However, this link is a mechanistic inference rather than direct clinical evidence specific to nefazodone. The TxGNN score of 0.996 reflects knowledge-graph similarity between nefazodone and other drugs/diseases in the graph, not clinical validation.

A secondary, lower-confidence prediction — **migraine with brainstem aura** (score 99.60%, evidence level L5, no supporting literature at all) — shares the same serotonergic rationale but lacks even review-level literature support, and involves brainstem-specific vascular/neural mechanisms not addressed by any available data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15926007](https://pubmed.ncbi.nlm.nih.gov/15926007/) | 2005 | Review | Neurological Sciences | Overview of emerging migraine preventive treatment options; nefazodone discussed among candidate agents. |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Current Pain and Headache Reports | Reviews prophylactic migraine therapies including topiramate, tizanidine, and nefazodone; overview of migraine pathophysiology. |
| [15549532](https://pubmed.ncbi.nlm.nih.gov/15549532/) | 2004 | Review | Neurological Sciences | Reviews new preventive migraine drugs; notes evidence quality varies from controlled trials to open/uncontrolled studies. |

All three are narrative reviews (Tier 3) that mention nefazodone alongside multiple other agents — none are nefazodone-specific efficacy studies.

---

## US Market Information

Nefazodone is not marketed in Taiwan (0 TFDA licenses on record); no license or approved-indication data is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in this evidence pack — TFDA label data is a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for migraine disorder is limited to three narrative reviews with no dedicated clinical trials, and the TFDA safety profile (warnings/contraindications) is entirely unavailable — this blocks any S1 safety pre-assessment. The secondary candidate (migraine with brainstem aura) has even weaker support (L5, no literature) and should remain deprioritized.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — resolve DG001 before any safety pre-assessment
- Confirmed MOA and original indication data from DrugBank — resolve DG002
- Dedicated clinical trial or case-series evidence specific to nefazodone in migraine prevention (current literature only mentions it in passing within broader reviews)
- DDI data, given nefazodone's known hepatic metabolism-related interaction profile is currently unqueried (query_status: not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

