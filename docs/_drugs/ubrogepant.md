---
layout: default
title: Ubrogepant
parent: 僅模型預測 (L5)
nav_order: 1274
evidence_level: L5
indication_count: 3
---

# Ubrogepant
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

# Ubrogepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Ubrogepant is an oral CGRP (calcitonin gene-related peptide) receptor antagonist originally developed for the acute treatment of migraine with or without aura in adults.
> The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a rare migraine subtype,
> with **0 dedicated clinical trials** for this specific subtype but **20 supporting publications** on ubrogepant's pharmacology, safety, and efficacy in general migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (with/without aura) — established via literature (PMID 32020557); no formal license record in evidence pack |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.85% (rank 4506) |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed *(per evidence pack; note: conflicts with literature indicating FDA approval as Ubrelvy in Dec 2019 — see Market Information section)* |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on known information from the supporting literature, ubrogepant is a small-molecule, highly-selective **CGRP receptor antagonist** ("gepant") that blocks calcitonin gene-related peptide-mediated activation of the trigeminovascular system, a key pathway in migraine pain transmission. Its efficacy in acute migraine treatment (with or without aura) has been established through Phase 3 RCTs (ACHIEVE I/II) and is FDA-approved in the United States.

Migraine with brainstem aura (formerly "basilar-type migraine") is a rare migraine subtype involving brainstem-origin aura symptoms. Since ubrogepant's mechanism does not involve vasoconstriction — unlike triptans, which are often contraindicated or used with caution in this subtype due to theoretical cerebrovascular risk — CGRP receptor blockade offers a mechanistically plausible, lower vasoconstrictive-risk alternative. However, this rationale is extrapolated from general migraine trial data; **no Phase 3 or subtype-specific RCT currently exists** for migraine with brainstem aura specifically, meaning the prediction rests on mechanistic plausibility rather than direct outcome evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37979595](https://pubmed.ncbi.nlm.nih.gov/37979595/) | 2023 | RCT (Phase 3) | Lancet | Ubrogepant 100mg vs placebo for acute migraine treatment administered during the prodrome phase, before headache onset |
| [31742631](https://pubmed.ncbi.nlm.nih.gov/31742631/) | 2019 | RCT | JAMA | ACHIEVE II trial: ubrogepant superior to placebo for pain freedom and relief of most bothersome associated symptom at 2 hours |
| [33874756](https://pubmed.ncbi.nlm.nih.gov/33874756/) | 2021 | RCT (subgroup analysis) | Cephalalgia | Safety and efficacy of ubrogepant across cardiovascular risk categories in ACHIEVE I/II — no vasoconstrictive safety signal |
| [39569702](https://pubmed.ncbi.nlm.nih.gov/39569702/) | 2025 | RCT (safety/DDI substudy) | Headache | TANDEM study: safety/tolerability of ubrogepant for acute treatment in patients on concurrent preventive atogepant |
| [31913519](https://pubmed.ncbi.nlm.nih.gov/31913519/) | 2020 | RCT (52-week extension) | Headache | Long-term safety of ubrogepant over 52 weeks of repeated acute treatment |
| [32020557](https://pubmed.ncbi.nlm.nih.gov/32020557/) | 2020 | Review | Drugs | First global approval summary: ubrogepant approved in the US (Dec 2019) for acute migraine treatment ± aura |
| [32011192](https://pubmed.ncbi.nlm.nih.gov/32011192/) | 2020 | Review | Expert Opin Pharmacother | Overview of CGRP-mediated neurogenic inflammation and trigeminovascular pathway relevant to ubrogepant's mechanism |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network Meta-analysis | J Headache Pain | Comparative efficacy of ubrogepant vs. lasmiditan and rimegepant for acute migraine treatment |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook Clin Neurol | Overview of second-generation gepants (ubrogepant, rimegepant) and CGRP-mediated antimigraine mechanism |
| [33948091](https://pubmed.ncbi.nlm.nih.gov/33948091/) | 2021 | Narrative Review | J Pain Res | Summary of ACHIEVE I/II trial results and long-term open-label extension safety data |

---

## US Market Information

No license or NDA records are currently available in the evidence pack (`taiwan_regulatory.total_licenses = 0`). This is notable because the supporting literature (PMID 32020557) documents that ubrogepant (brand name **Ubrelvy**) received its first global FDA approval in **December 2019** for acute migraine treatment in adults. This discrepancy suggests the market/license dataset in this evidence pack may be stale or incomplete and should be independently verified against current FDA Orange Book / TFDA records before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications (DG001) constitute a **blocking** data gap — safety evaluation (Stage S1) cannot proceed until this is resolved.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the CGRP receptor antagonism mechanism is plausible for extending ubrogepant's use from general migraine to the brainstem aura subtype, no direct clinical trial or case-level evidence exists for this specific indication, and a **blocking** data gap (missing TFDA/FDA label warnings and contraindications) prevents safety evaluation from proceeding to Stage S1.

**To proceed, the following is needed:**
- TFDA/FDA package insert data — warnings, contraindications (DG001, blocking)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Verification of actual current US/Taiwan market and license status (data conflict identified above)
- Subtype-specific clinical evidence (case series or trial) for migraine with brainstem aura, given historical caution around vasoactive drugs in this population

*Note: The two lower-ranked candidates (atrophoderma vermiculata, ulerythema ophryogenesis) show no mechanistic plausibility or supporting literature and are classified L5/Hold — likely knowledge-graph false positives, not recommended for further evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

