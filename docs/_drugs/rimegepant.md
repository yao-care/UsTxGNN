---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 1125
evidence_level: L5
indication_count: 6
---

# Rimegepant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Rimegepant is a CGRP receptor antagonist approved by the FDA for acute and preventive treatment of migraine.
> The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**,
> with **no dedicated clinical trials** but **14 supporting publications** on rimegepant in general migraine populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local license data (drug not currently marketed); per FDA approval documented in literature: acute treatment of migraine with or without aura, and preventive treatment of episodic migraine |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on the literature evidence collected, rimegepant is a small-molecule calcitonin gene-related peptide (CGRP) receptor antagonist that blocks CGRP signalling in the trigeminovascular system. It was first approved by the FDA in 2020 (Nurtec® ODT) for acute treatment of migraine with or without aura, and later for preventive treatment of episodic migraine.

The predicted new indication, migraine with brainstem aura, is a specific migraine subtype. Unlike triptans, gepants such as rimegepant do not cause vasoconstriction, which theoretically makes them more suitable for this subtype — brainstem aura and hemiplegic migraine have traditionally been considered a relative or absolute contraindication for triptans due to their vasoconstrictive action. This pharmacological distinction provides a plausible mechanistic rationale for the TxGNN prediction.

However, all 14 literature items identified relate to general migraine populations (efficacy, safety, pharmacokinetics, long-term open-label studies); none specifically enrolled or studied patients with migraine with brainstem aura, a subgroup that is routinely excluded from standard migraine RCTs. The current evidence is therefore an indirect extrapolation from mechanism plus general-population efficacy/safety data, not direct evidence for this specific subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | J Headache Pain | Indirect comparison of relative efficacy: rimegepant vs. lasmiditan and ubrogepant for acute migraine treatment |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 open-label safety | J Headache Pain | 24-week open-label study confirms long-term safety/tolerability of once-daily 75 mg rimegepant for episodic migraine prevention |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 open-label long-term safety | Cephalalgia | Long-term safety and effectiveness of rimegepant ODT 75 mg for acute migraine treatment in Chinese adults |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospective cohort | Headache | Off-label use of rimegepant in adolescents shows favorable tolerability and effectiveness for acute migraine |
| [41133671](https://pubmed.ncbi.nlm.nih.gov/41133671/) | 2026 | Phase 1 PK/Safety | Headache | Single-dose PK, safety, and tolerability of weight-adjusted rimegepant ODT in children aged 6–12 with migraine history |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | Phase 1 RCT (PK/Safety) | Clin Pharmacol Drug Dev | Randomized placebo-controlled trial confirms PK and safety of single/multiple 75 mg rimegepant ODT dosing in healthy Chinese adults |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Comprehensive review of rimegepant's efficacy in acute and preventive migraine treatment; superior to placebo in pivotal Phase 3 trials |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Review (drug approval summary) | Drugs | First-approval summary of rimegepant ODT for acute migraine; conventional tablet under investigation for prevention and trigeminal neuralgia |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handb Clin Neurol | Review of second-generation CGRP receptor antagonists (gepants) including rimegepant, mechanism and clinical development |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Manag | Overview of rimegepant among new acute migraine treatment options (lasmiditan, ubrogepant, rimegepant) |

---

## US Market Information

Rimegepant is not currently marketed in this jurisdiction — no license/NDA records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The CGRP-antagonist, non-vasoconstrictive mechanism offers a plausible rationale for use in migraine with brainstem aura, and rimegepant has substantial general-population migraine evidence (including Phase 3/4 studies). However, no clinical trial or publication directly studies this specific subtype, and a **Blocking** data gap on official safety warnings/contraindications (DG001) prevents entry into the S1 safety evaluation stage.

**To proceed, the following is needed:**
- Official label warnings, contraindications, and DDI data (TFDA or equivalent regulatory source)
- Formal mechanism of action (MOA) documentation from DrugBank
- Subtype-specific evidence (case series, registry data, or targeted trials) in migraine with brainstem aura or hemiplegic migraine populations
- Confirmation of local regulatory pathway, given the drug is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

