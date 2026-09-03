---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 897
evidence_level: L5
indication_count: 4
---

# Memantine
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

# Memantine: From Alzheimer's Disease to Migraine Disorder

## One-Sentence Summary

Memantine is an NMDA receptor antagonist most widely known for treating moderate-to-severe Alzheimer's disease dementia (this Evidence Pack does not itself document the original indication — see note below). The TxGNN model predicts it may also be effective for **Migraine Disorder** (prophylaxis), and unlike the other three candidates in this evidence pack, this prediction is backed by real clinical and literature evidence: **2 clinical trials** (including a completed Phase 3 RCT) and **20 publications**, among them a meta-analysis, a systematic review, and a network meta-analysis.

> **Note on multiple candidates**: This Evidence Pack (`TW-DB01043-multi`) contains four TxGNN-predicted indications for memantine, ranked by prediction score. The highest-scoring candidate (pulmonary hypertension) has essentially no supporting evidence and a "Hold" recommendation. This report focuses on **Migraine Disorder** because it is the only candidate with substantive clinical support; the others are summarized briefly near the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (`original_indications` is empty; `original_moa` is a data gap). Memantine is broadly known as a therapy for moderate-to-severe Alzheimer's disease — pending confirmation against an official label. |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L2 |
| US Market Status | Not Marketed (per Evidence Pack; `total_licenses = 0`) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is flagged as a data gap in this Evidence Pack, but the repurposing rationale field itself supplies the relevant pharmacology: memantine is a **non-competitive NMDA receptor antagonist**. Migraine pathophysiology centers on cortical spreading depression (CSD) and glutamatergic excitotoxicity, both of which are modulated by NMDA receptor signaling. Blocking the NMDA receptor is theorized to suppress CSD propagation and reduce trigeminovascular sensitization — the mechanism thought to drive migraine attacks.

This mechanistic plausibility is reinforced by an unusually deep literature base for a "predicted" indication: two mechanistic reviews (PMID 36869904, PMID 29508147) explicitly frame NMDA antagonists as anti-migraine agents, and a completed Phase 3 RCT (NCT04698525) directly compared memantine to an established migraine prophylactic (sodium valproate). This is a case where mechanism, clinical trial data, and a substantial body of prior investigation converge — considerably stronger support than a model score alone.

That said, the evidence is not unanimous: a 2021 commentary (PMID 34510445) is titled "Memantine for migraine — Big promise but little evidence," and the completed Phase 3 trial enrolled only 33 patients, limiting statistical power. The evidence level (L2) reflects one completed Phase 2/3 RCT rather than confirmatory replication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Compared memantine against sodium valproate (AAN Level A) for prophylaxis of episodic migraine; a head-to-head active-comparator design, though the small sample limits definitive conclusions. |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by Invitation | 3300 | Pragmatic EMR-based registry across 10 common neurological disorders at NorthShore University HealthSystem; provides real-world prescribing context rather than a direct memantine efficacy comparison. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clinical Neuropharmacology | Systematic review and meta-analysis of memantine vs. placebo for migraine; notes efficacy remains controversial. |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic Review | Headache | Assesses efficacy and safety of memantine for prophylactic treatment of episodic migraine. |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network Meta-analysis | Frontiers in Pharmacology | Compares oral preventive migraine medications in adults 18–65, positioning memantine among comparator options. |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (double-blind, placebo-controlled) | Headache | Randomized placebo-controlled study of memantine for prophylaxis of migraine without aura. |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical Practice Guideline | Annals of Internal Medicine | 2023 VA/DoD headache management guideline covering migraine and tension-type headache prevention. |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective Cohort | The Journal of Headache and Pain | Retrospective review of 60 patients treated with memantine as migraine preventive therapy in a university headache clinic. |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review (mechanistic) | Naunyn-Schmiedeberg's Archives of Pharmacology | Reviews memantine and ketamine, both NMDA receptor antagonists, as potential anti-migraine agents. |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review (mechanistic) | Neurotherapeutics | Reviews glutamate/NMDA receptor signaling as a therapeutic target for migraine. |
| [34048395](https://pubmed.ncbi.nlm.nih.gov/34048395/) | 2021 | Review | Continuum (Minneapolis, Minn.) | Overview of pharmacologic and non-pharmacologic preventive migraine treatments. |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary | Headache | "Memantine for migraine — Big promise but little evidence"; cautionary perspective on the evidence base. |

---

## US Market Information

No marketing authorization records are present in this Evidence Pack (`total_licenses = 0`, `market_status = 未上市/Not Marketed`). This is inconsistent with memantine's status as a long-marketed drug in most jurisdictions and should be treated as a **data gap requiring verification** rather than a confirmed absence of approval.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all flagged as data gaps or not found in this Evidence Pack — notably `DG001`, a **Blocking** severity gap for TFDA label warnings/contraindications, which must be resolved before any S1 safety evaluation.)

---

## Other Predicted Indications (Not Prioritized)

This Evidence Pack also flagged three additional TxGNN predictions for memantine, all with materially weaker support than migraine:

- **Pulmonary Hypertension** (rank 1, score 99.54%, L5, **Hold**) — Despite the highest raw TxGNN score, the two literature hits are not on-target: one concerns NMDA receptor *activation* (opposite pharmacology) and metabolic effects, the other is a PK/safety study of an unrelated compound (MN-08, a memantine nitrate derivative, not memantine itself). No clinical trials or established mechanistic link.
- **Migraine with Brainstem Aura** (rank 4, score 99.41%, L3, Research Question) — Mechanistically plausible extrapolation from the general migraine literature, but no trial or study specifically targets this aura subtype; the key RCT (PMID 26638119) explicitly excludes migraine *with* aura.
- **Kyphoscoliotic Heart Disease** (rank 3, score 99.43%, L5, Hold) — No clinical trials, no literature, and no plausible mechanistic link between NMDA receptor antagonism and this thoracic-deformity-related cardiopulmonary condition. Model prediction only.

None of these three warrant further action at this time.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the Migraine Disorder indication)

**Rationale:**
Migraine is the only one of the four TxGNN-predicted indications for memantine with a coherent mechanism, a completed Phase 3 RCT, and a substantial supporting literature base (meta-analysis, systematic review, network meta-analysis). However, the pivotal trial's small sample size (n=33) and an explicit skeptical commentary in the literature ("big promise but little evidence") mean the evidence supports guarded exploration rather than an unconditional Go.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism-of-action and original-indication documentation from DrugBank (DG002)
- A larger, adequately powered confirmatory RCT for migraine prophylaxis
- Drug-drug interaction data (current DDI query returned no results)
- Verification of actual US/Taiwan market/licensing status, which currently conflicts with memantine's known long-standing marketing history
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

