---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout and Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a well-established xanthine oxidase (XO) inhibitor, widely used for the treatment of gout, hyperuricemia, and prophylaxis of tumor lysis syndrome.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **0 clinical trials** and **2 publications** currently supporting this direction.
Existing evidence is limited to a hypothesis paper and a single indirect preclinical study, making this an early-stage research question rather than an actionable clinical candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout and hyperuricemia (regulatory records not captured in current dataset — see US Market Information) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| US Market Status | Not captured in current dataset (data gap — allopurinol is widely available as a US generic) |
| Number of NDAs | 0 (regulatory query returned no results; data gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on established pharmacological knowledge, allopurinol is a potent inhibitor of xanthine oxidase (XO), the enzyme responsible for the final two steps in uric acid biosynthesis (hypoxanthine → xanthine → uric acid). XO inhibition lowers serum urate and simultaneously reduces reactive oxygen species (ROS) produced as a byproduct of the xanthine oxidation reaction.

Hepatic porphyrias are metabolic disorders caused by partial deficiencies in enzymes of the heme biosynthesis pathway. The primary lesion is excessive induction of 5-aminolevulinate synthase (ALAS), the pathway's rate-limiting enzyme, which drives accumulation of toxic porphyrin precursors (ALA, PBG). The proposed mechanistic bridge is that XO-derived ROS can trigger ALAS transcriptional induction — and therefore XO inhibition by allopurinol might dampen this ROS-mediated signalling, reduce ALAS over-expression, and alleviate precursor accumulation. This connection is biologically plausible at the molecular level and has been mentioned in the hypothesis literature.

However, this reasoning remains speculative. The two supporting publications do not directly test allopurinol in porphyria: one is a 2019 hypothesis paper proposing tryptophan-TDO inhibition as a parallel strategy, and the other is a 1992 rat study on carbamazepine-induced heme disruption. Neither provides experimental evidence for allopurinol efficacy in porphyria. The TxGNN model's high score (99.95%) most likely reflects graph-level proximity between xanthine oxidase metabolism and heme biosynthesis nodes rather than validated pharmacological activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes metabolic targeting of hepatic ALAS via inhibition of heme utilisation by tryptophan 2,3-dioxygenase (TDO) as therapy for acute hepatic porphyrias; discusses how disruption of the hepatic heme regulatory pool precipitates acute attacks, providing mechanistic context relevant to XO-ROS-ALAS pathway |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (Preclinical) | Biochemical Pharmacology | Examined effects of carbamazepine on heme metabolism in rat liver using a validated porphyria-exacerbation screening model; demonstrated that drugs depleting the hepatic heme pool secondarily induce ALAS, providing the mechanistic framework within which XO inhibition has been theorised to act |

---

## US Market Information

No US regulatory authorisation records were returned for allopurinol in the current dataset (query returned 0 results). This is a data gap: allopurinol (brand name Zyloprim®, NDA 016084) has long-standing FDA approval for gout, hyperuricemia, and recurrent calcium oxalate nephrolithiasis, and is widely available as a generic. A targeted FDA Orange Book or DailyMed query should be rerun to populate this section with accurate NDA information before clinical assessment proceeds.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, all supporting evidence is indirect — a mechanistic hypothesis and one preclinical heme-metabolism study using a different drug. There are no clinical trials, no case reports, and no direct animal data for allopurinol in hepatic porphyria, which is insufficient to support advancement.

**To proceed, the following is needed:**
- **Regulatory data remediation**: rerun FDA Orange Book / DailyMed query for allopurinol (DB00437 / Zyloprim®) to capture approved indications, dosing, and labelled warnings
- **MOA and safety data from DrugBank**: retrieve full mechanistic profile, known drug–drug interactions, and contraindications to enable proper safety screening
- **Package insert review**: obtain AERS/US label warnings and contraindications (all currently marked as data gap)
- **Proof-of-concept preclinical study**: test allopurinol in a validated acute intermittent porphyria mouse model (e.g., AIP mouse induced by phenobarbital + low-calorie diet) to determine whether XO inhibition measurably suppresses ALAS induction and reduces urinary ALA/PBG
- **Systematic literature search expansion**: broaden PubMed query to include allopurinol in heme metabolism, ALAS regulation, and porphyria case reports to rule out overlooked evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

