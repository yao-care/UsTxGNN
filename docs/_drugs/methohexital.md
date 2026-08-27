---
layout: default
title: Methohexital
parent: 僅模型預測 (L5)
nav_order: 909
evidence_level: L5
indication_count: 5
---

# Methohexital
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Methohexital: From General Anesthesia Induction to Insomnia

## One-Sentence Summary

Methohexital is an ultra-short-acting IV barbiturate anesthetic, used clinically mainly for anesthesia induction (notably electroconvulsive therapy, ECT). The TxGNN model predicts it may be effective for **Insomnia**, but this ranking currently has **zero clinical trials** and **zero publications** supporting it — the prediction score is high, but the evidence behind it is empty.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded — no US license found; known clinical use is IV anesthesia induction (commonly for ECT), based on evidence-pack context |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a Data Gap). Based on information present elsewhere in this evidence pack, methohexital is an ultra-short-acting barbiturate general anesthetic, used clinically as an induction agent — most notably for ECT — with an effect duration of only a few minutes.

On mechanistic grounds, barbiturates as a class enhance GABA-A receptor activity, which is the same broad mechanism used by sedative-hypnotics for insomnia, and this is likely why TxGNN scored the drug/disease pair highly. However, this analogy does not hold up pharmacokinetically: methohexital's ultra-short duration of action and IV-only administration make it fundamentally unsuited to sustained sleep induction/maintenance, which is what insomnia treatment requires. No clinical trial or published literature searches (ClinicalTrials.gov, ICTRP, PubMed) returned any results for methohexital + insomnia.

For context, other lower-ranked TxGNN predictions for this drug (migraine disorder, headache disorder) at least have case-report/case-series-level literature — though describing methohexital/ECT as a trigger of headache, not a treatment for it. The insomnia prediction, by contrast, has no supporting evidence of any kind; it should be treated as a pharmacological-class artifact of the model rather than a validated signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, this prediction has no clinical trial or literature support (Evidence Level L5) and is mechanistically implausible given methohexital's ultra-short IV pharmacokinetics, which are incompatible with insomnia treatment. The drug is also not currently marketed in the reference jurisdiction.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently a blocking data gap)
- Mechanism of action (MOA) data from DrugBank or primary literature
- Any preclinical or mechanistic studies specifically linking methohexital to sleep induction/maintenance, before this candidate can be re-scored above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

