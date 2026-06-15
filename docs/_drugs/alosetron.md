---
layout: default
title: Alosetron
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 6
---

# Alosetron
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

The txgnn-pipeline skill is infrastructure-focused and doesn't override the report format instructions. Proceeding directly with the report generation per the Evidence Pack v5 protocol.

---

# Alosetron: From Irritable Bowel Syndrome to Migraine Disorder

## One-Sentence Summary

Alosetron is a selective 5-HT₃ receptor antagonist, originally developed for the treatment of diarrhea-predominant irritable bowel syndrome (IBS-D) in women.
The TxGNN model predicts it may be effective for **Migraine Disorder** with a prediction score of **99.64%**,
however, **no clinical trials** and **no direct publications** currently support this specific repurposing direction, placing evidence entirely at the model-prediction level.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in regulatory database queried |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the queried regulatory sources. Based on known pharmacological class information, Alosetron belongs to the selective 5-HT₃ receptor antagonist class — sharing a drug class with ondansetron, granisetron, dolasetron, and tropisetron — whose primary established clinical role is the prevention of chemotherapy-induced nausea and emesis (CINV), as well as the management of IBS-D symptoms through modulation of visceral pain and gastrointestinal motility.

The biological basis for this prediction rests on the anatomical distribution of 5-HT₃ receptors within the trigeminovascular system. These receptors are expressed in the trigeminal ganglia and brainstem nuclei central to migraine pathophysiology. Serotonin is a well-established key modulator of migraine, and 5-HT₃ receptor antagonism could theoretically suppress the peripheral and central release of nociceptive mediators such as CGRP and substance P along the trigeminal pathway, potentially attenuating pain signal propagation.

Class-level indirect support exists: ondansetron and granisetron have been explored in sporadic clinical settings for migraine symptom relief. However, no clinical trials or publications have specifically evaluated alosetron for migraine. This prediction currently rests entirely on mechanistic plausibility and knowledge graph connectivity, and should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

> **Note:** One indirect class-level reference (PMID [15515406](https://pubmed.ncbi.nlm.nih.gov/15515406/), 2004, Narrative Review, *Scand J Rheumatology Suppl*) was identified under the broader **headache disorder** indication (Rank #5). This review covers the spectrum of use and tolerability of 5-HT₃ receptor antagonists as a class and does not evaluate alosetron specifically for any headache condition. It does not constitute direct evidence for the migraine repurposing hypothesis.

## US Market Information

No license records were found for Alosetron in the regulatory database queried. The drug is currently recorded as not marketed.

> **For context:** Alosetron (brand name Lotronex®) has a documented US FDA approval history for IBS-D in adult women, initially approved in 2000, voluntarily withdrawn, and re-approved in 2002 under a restricted-access Risk Evaluation and Mitigation Strategy (REMS) program due to serious gastrointestinal adverse events. This information derives from external domain knowledge and was not captured by the current regulatory query. The discrepancy should be investigated before any regulatory status conclusions are drawn.

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical advisory:** All safety data fields (key warnings, contraindications, drug-drug interactions) returned no results in the current query. Based on external pharmacological knowledge, Alosetron carries a boxed warning for ischemic colitis and serious complications of constipation under its US REMS program. These risks are highly material to any repurposing evaluation and must be retrieved from the FDA label prior to any clinical or research decision.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.64%) and the mechanistic connection between 5-HT₃ receptor antagonism and migraine pathophysiology is biologically plausible; however, evidence is entirely at L5 with no clinical trials or publications directly evaluating alosetron in any headache indication, and critical safety and regulatory data remain unconfirmed.

**To proceed, the following is needed:**
- Retrieve full MOA documentation from DrugBank (DB00969) to confirm receptor binding profile
- Obtain complete US FDA label including REMS-related boxed warnings, contraindications, and drug interactions — this is a blocking prerequisite before any safety evaluation can proceed
- Conduct a systematic literature review specifically for 5-HT₃ antagonists (ondansetron, granisetron) in migraine clinical trials to establish class-level evidence baseline
- Resolve regulatory database discrepancy: confirm current US approval status and REMS restrictions for Alosetron
- Assess route of administration compatibility — oral formulation requirements for migraine acute/preventive treatment context
- Evaluate whether known serious GI risks (ischemic colitis) constitute a risk-benefit barrier that would disqualify the repurposing pathway regardless of efficacy signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

