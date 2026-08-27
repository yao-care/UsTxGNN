---
layout: default
title: Gepirone
parent: 僅模型預測 (L5)
nav_order: 750
evidence_level: L5
indication_count: 3
---

# Gepirone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Gepirone: From Major Depressive Disorder to Postpartum Depression and Agoraphobia

## One-Sentence Summary

Gepirone is a 5-HT1A receptor partial agonist (azapirone class) whose extended-release form was approved in the US in 2023 as Exxua for major depressive disorder; it is **not marketed in Taiwan**. TxGNN predicts potential efficacy in **Postpartum Depression** and **Agoraphobia**, but current support is limited to **1 open-label study and 2 review articles** — no dedicated clinical trials or RCTs exist for either indication. A third top-ranked signal, "benign paroxysmal torticollis of infancy," is flagged by the evidence pack itself as likely knowledge-graph noise and has been excluded from the actionable recommendations below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — approved in the US as Exxua® (gepirone ER, 2023); no approved indication on record in Taiwan |
| Predicted New Indications | Postpartum Depression (rank 3); Agoraphobia (rank 2) |
| TxGNN Prediction Score | Postpartum Depression: 99.52% · Agoraphobia: 99.66% |
| Evidence Level | L4 (both indications — mechanism/uncontrolled study level, no RCTs) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

**Excluded signal:** Rank 1, "benign paroxysmal torticollis of infancy" (score 99.67%), is assessed as L5 / decision stage S0 / Hold in the evidence pack itself — no clinical, mechanistic, or pediatric safety basis exists linking a 5-HT1A partial agonist to this self-limited infant condition. It is treated as candidate noise and excluded from further discussion.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gepirone is currently a data gap in this evidence pack. Based on known pharmacology, gepirone is an azapirone and potent 5-HT1A receptor partial agonist — the same drug class as buspirone. Its extended-release formulation is already approved in the United States (Exxua, 2023) for major depressive disorder, establishing serotonergic modulation as its core clinical mechanism.

**Agoraphobia** frequently co-occurs with panic disorder and generalized anxiety disorder, both of which respond to 5-HT1A agonism. An open-label study from 1993 evaluated gepirone in patients with combined generalized anxiety disorder and panic disorder with agoraphobia, providing indirect but not indication-specific support.

**Postpartum depression** is clinically classified as an MDD subtype. Since gepirone's serotonergic mechanism is already validated for MDD in the US, mechanistic extension to postpartum depression is plausible. However, no data in this pack address perinatal pharmacokinetics, lactation safety, or neuroendocrine interactions specific to the postpartum period.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Agoraphobia or Postpartum Depression.

---

## Literature Evidence

### Agoraphobia

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8096526](https://pubmed.ncbi.nlm.nih.gov/8096526/) | 1993 | Open-label study | J Clin Psychopharmacol | Uncontrolled 6-week study in 21 patients with generalized anxiety disorder + panic disorder with agoraphobia; gepirone titrated from 2 to 12 mg/day; 3 dropped out in week 1 |

### Postpartum Depression

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40282849](https://pubmed.ncbi.nlm.nih.gov/40282849/) | 2025 | Review | Medicina (Kaunas) | Narrative review of current and future antidepressant monotherapies, referencing STAR*D-era evidence across SSRIs/SNRIs/TCAs/MAOIs |
| [38993656](https://pubmed.ncbi.nlm.nih.gov/38993656/) | 2024 | Review | Psychopharmacol Bull | Overview of newly approved psychotropic agents, including novel antidepressants |

Neither publication is specific to postpartum depression as a primary endpoint; both are general antidepressant reviews that mention newer agents in passing.

---

## Taiwan Market Information

Gepirone has no Taiwan Food and Drug Administration (TFDA) marketing license on record (0 licenses, market status: 未上市/Not marketed). No dosage forms, brand names, or approved indication text are available for the Taiwan market.

*External reference for context: gepirone ER is approved in the United States as Exxua® for MDD (2023) — this approval is not reflected in Taiwan regulatory data.*

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug-drug interaction records are currently available — this is flagged as a **Blocking** data gap (DG001) in the evidence pack, meaning the candidate cannot yet enter formal safety pre-screening (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Both plausible indications (agoraphobia, postpartum depression) rest on L4 evidence — a single uncontrolled study and general reviews, with zero registered clinical trials — and the evidence pack itself scores them only as "Research Question," not a Go-level signal.
- A Blocking data gap (missing TFDA label warnings/contraindications) prevents any safety pre-screening, and gepirone is not currently marketed in Taiwan.
- The top-ranked TxGNN signal (infant torticollis) is explicitly assessed as likely model noise and should not drive prioritization.

**To proceed, the following is needed:**
- TFDA-equivalent or FDA label data (warnings, contraindications, DDI) to complete S1 safety pre-screening
- Confirmed mechanism-of-action documentation from DrugBank
- Indication-specific clinical trials for either agoraphobia or postpartum depression (current literature is exploratory/indirect only)
- Perinatal/lactation safety data if postpartum depression is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

