---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a long-acting dihydropyridine L-type calcium channel blocker (CCB), internationally established for hypertension and stable angina pectoris.
The TxGNN model identifies **Brain Stem Infarction** as its top predicted new indication (score 99.94%), with a broader cerebrovascular prediction cluster spanning 10 indications.
Among these, **Intracerebral Hemorrhage** (rank 10) carries the strongest evidence base — including one completed Phase 3 trial (TRIDENT, n = 1,671) and 8 publications — supporting a **Proceed with Guardrails** recommendation for that specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Stable Angina (internationally established; Taiwan TFDA license data returned 0 records — possible data gap) |
| Predicted New Indication | Brain Stem Infarction (TxGNN Rank #1) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (brain stem infarction); best-in-set: L2 (intracerebral hemorrhage, rank 10) |
| Taiwan Market Status | 未上市（TFDA 紀錄為 0，疑似資料缺漏） |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold (brain stem infarction) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacology, amlodipine is a dihydropyridine L-type calcium channel blocker that inhibits voltage-gated Ca²⁺ entry into vascular smooth muscle and myocardial cells, producing sustained systemic vasodilation and blood pressure reduction without reflex tachycardia — a profile that makes it one of the most widely prescribed antihypertensives worldwide.

The TxGNN model's top 10 predictions form a coherent cerebrovascular cluster: brain stem infarction, MRI-defined brain infarct, cerebral artery occlusion, intracerebral hemorrhage, and related hypertensive end-organ damage. Two mechanistic pathways underpin this entire cluster. First, **blood pressure control**: sustained systolic BP reduction directly decreases the risk of all stroke subtypes, both ischemic and hemorrhagic, and amlodipine's long half-life (35–50 hours) provides stable, non-pulsatile BP control — particularly valuable in the post-stroke setting where BP fluctuation worsens outcomes. Second, **neuroprotection via Ca²⁺ overload inhibition**: during cerebral ischemia, excitotoxic Ca²⁺ influx through L-type channels is a primary driver of neuronal death; animal studies using the transient middle cerebral artery occlusion (tMCAO) model demonstrate that amlodipine reduces infarct volume through anti-apoptotic (Bcl-2↑, Bax↓), anti-autophagic (beclin-1↓), and antioxidative mechanisms.

The most clinically compelling evidence comes from **intracerebral hemorrhage (rank 10)**, where the completed TRIDENT Phase 3 trial (n = 1,671) directly tested a fixed-dose combination containing amlodipine (perindopril + indapamide + amlodipine) for secondary prevention of recurrent stroke following ICH — directly validating the cerebrovascular repurposing rationale. This represents a materially different evidence base from the rank 1 prediction (brain stem infarction), which currently rests on model inference alone.

---

## Clinical Trial Evidence

> **Note:** The top-ranked prediction (brain stem infarction, rank 1) has no registered clinical trials. The tables below present evidence for the two highest-evidence indications in this dataset.

### Intracerebral Hemorrhage (Rank 10 · Evidence Level L2 · Recommendation: Proceed with Guardrails)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial: double-blind RCT of fixed low-dose triple pill (perindopril + indapamide + **amlodipine**) vs. placebo on top of standard care; primary endpoint = time to first recurrent stroke in ICH survivors; **strongest direct evidence in this dataset** |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | CASE-J sub-study: high-dose ARB monotherapy vs. ARB + **CCB** combination in Japanese elderly high-risk hypertensives; cardiovascular events including ICH as outcomes |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | IPAD trial: antihypertensive treatment (including amlodipine as a permitted agent) in adults with type 2 diabetes; ICH as secondary endpoint; very large sample |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | NA | Recruiting | 140 | TRICH trial: triple antihypertensive therapy post-ICH guided by TRICH risk score; amlodipine as a component of the triple regimen; Hong Kong multicenter design |

### Cerebral Artery Occlusion (Rank 6 · Evidence Level L3 · Recommendation: Research Question)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) | NA | Unknown | 8,000 | STEP trial: intensive SBP target (<130 mmHg) vs. standard (<150 mmHg) in elderly hypertensives aged 60–80; cerebrovascular events as endpoints; amlodipine as one of the standard treatment options |

---

## Literature Evidence

> **Note:** Brain stem infarction (rank 1) has no publications. The tables below cover the two indications with available literature.

### Cerebral Artery Occlusion (Rank 6)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Animal Study | J Neurosci Res | Amlodipine + atorvastatin vs. monotherapy after 90-min MCAO in metabolic syndrome Zucker rats; combination showed additive neuroprotection via anti-apoptotic (Bcl-2↑, Bax↓) and anti-autophagic (beclin-1↓) mechanisms; reduced infarct size 24h post-reperfusion |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Animal Study | Brain Research | Synergistic benefit of amlodipine + atorvastatin after MCAO in Zucker rats; reduced infarct volume compared to either drug alone; combination superior to monotherapy |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Animal Study | Brain Research | Ischemic stroke protection by amlodipine + atorvastatin in metabolic syndrome model; full serum/physical parameter analysis post-tMCAO; consistent with two above studies (same group, independent confirmation) |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Animal Study | Brain Research | CCBs with antioxidative properties prevent neuronal damage after transient focal ischemia in rats; amlodipine's free radical scavenging effect implicated as a supplementary neuroprotective mechanism |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Animal Study | Am J Hypertens | Amlodipine reduces stroke size after focal brain ischemia in ApoE-deficient mice; L-type CCB action in reducing infarct volume in a hyperlipidemic genetic model |

### Intracerebral Hemorrhage (Rank 10)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial Protocol | Int J Stroke | TRIDENT trial rationale and design paper; describes scientific basis for amlodipine in the triple-pill strategy for ICH secondary prevention; details recruitment progress across international sites |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT Protocol | Hypertension Res | CASE-J trial design: candesartan vs. amlodipine in high-risk Japanese hypertensives; cerebrovascular events including hemorrhagic stroke as composite endpoints |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Observational | Neurol Sci | Atenolol vs. other antihypertensives in acute hypertensive ICH (n=138); contextualizes the comparative role of CCBs (including amlodipine) in ICH blood pressure management |

---

## Taiwan Market Information

TFDA regulatory data returned **0 approved licenses** for amlodipine in this dataset. This is almost certainly a **data pipeline gap** — amlodipine is a WHO Essential Medicine listed in over 150 countries' formularies and is unambiguously marketed in Taiwan under multiple brand names. The TFDA NHI drug database and official drug license portal should be queried directly to resolve this discrepancy before any regulatory filing assessment.

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan-specific key warnings, contraindications, or drug interaction data were available in this Evidence Pack. The DDI query returned no interactions (query_status: not_found).

> **Data Gap Alert:** TFDA package insert safety data (DG001, severity: Blocking) is missing and must be retrieved before any S1 safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Hold** — for Brain Stem Infarction (TxGNN rank 1)

**Decision: Proceed with Guardrails** — for Intracerebral Hemorrhage (rank 10, highest evidence)

**Rationale:**
Brain stem infarction is the model's top-scored prediction but has zero supporting clinical trials or publications, placing it firmly at L5 (model prediction only). It cannot be advanced without dedicated preclinical or clinical evidence. In contrast, intracerebral hemorrhage is supported by a completed Phase 3 RCT (TRIDENT, n = 1,671) that directly tested an amlodipine-containing regimen for ICH secondary prevention, meeting L2 evidence criteria and justifying conditional advancement. The entire cerebrovascular prediction cluster is mechanistically plausible via BP control and Ca²⁺ overload neuroprotection, but each sub-indication requires individual evidence evaluation.

**To proceed with Intracerebral Hemorrhage, the following is needed:**
- Obtain and review the published TRIDENT main trial efficacy results (primary endpoint: recurrent stroke rate)
- Determine amlodipine's independent contribution vs. the perindopril/indapamide components within the triple-pill
- Resolve the TFDA data gap: download and parse the official amlodipine package insert to complete S1 safety screening (DG001)
- Document full MOA from DrugBank API (DG002) to support mechanistic regulatory narrative
- Define a safety monitoring plan for ICH secondary prevention context: BP targets, fall risk, peripheral edema monitoring, and neurological reassessment intervals

**To advance Brain Stem Infarction specifically:**
- Conduct targeted literature search: "amlodipine brain stem" / "CCB basilar artery" / "vertebrobasilar ischemia calcium channel"
- Evaluate whether brain stem infarction cases are captured as subgroups within existing cerebrovascular trials (e.g., STEP, TRIDENT)
- Consider a prospective registry or observational study design as a first step given complete absence of direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

