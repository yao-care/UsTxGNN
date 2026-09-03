---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 1013
evidence_level: L5
indication_count: 6
---

# Pantoprazole
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

# Pantoprazole: From Acid-Related Disorders to Active Peptic Ulcer Disease

## One-Sentence Summary

> Pantoprazole is a proton pump inhibitor (PPI) established for acid-related gastrointestinal disorders such as erosive esophagitis and GERD.
> The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
> with **3 clinical trials** and **20 publications** currently supporting this direction — though this largely confirms an already well-established PPI indication rather than a truly novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in regulatory data provided; supporting literature in this evidence pack (PMID 11402494) identifies pantoprazole's labeled use as short-term treatment of erosive esophagitis and other acid-related disorders |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Pantoprazole is part of the proton pump inhibitor (PPI) class, its efficacy in acid-related gastrointestinal disorders has been proven, and mechanistically may be applicable to active peptic ulcer disease.

The repurposing rationale explicitly notes: pantoprazole is an irreversible H⁺/K⁺-ATPase (proton pump) inhibitor that directly suppresses gastric parietal cell acid secretion — this is the standard pharmacological mechanism for treating peptic ulcer disease. Supporting literature in the pack (e.g., PMID 19938880, PMID 9017763) confirms this mechanism and its established role alongside H2-receptor antagonists in acid-peptic disorder management.

**Important caveat**: unlike a typical novel repurposing candidate, the model's own supporting rationale states this is "not a novel repurposing but a core pharmacological indication" for the PPI class. In other words, active peptic ulcer disease is already a textbook/label-adjacent use of pantoprazole (including as a component of H. pylori triple/quadruple eradication therapy), rather than an unexpected new application. This should be factored into how the prediction is interpreted for decision-making — it validates model calibration more than it reveals a new therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled trial comparing Ilaprazole vs. Pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated influence of PPIs (incl. pantoprazole) and statins on clopidogrel antiplatelet effects in PCI/stent patients; relevant to PPI-treated ulcer/GI populations |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor SRH fading/early rebleeding after endoscopic hemostasis and high-dose PPI infusion in bleeding peptic ulcer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective randomized study comparing intermittent vs. continuous pantoprazole infusion for peptic ulcer rebleeding after endoscopic therapy |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Multicenter, randomized, active-controlled study of tegoprazan (P-CAB) vs. PPI for ESD-induced artificial ulcer healing |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Comparison of three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Prospective randomized controlled trial of pantoprazole infusion as adjuvant to endoscopic therapy in peptic ulcer bleeding |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | Randomized controlled trial: amoxycillin + clarithromycin with sucralfate or pantoprazole for H. pylori eradication in duodenal ulcer |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT (comparative) | Aliment Pharmacol Ther | Pantoprazole, amoxycillin, and azithromycin or clarithromycin for H. pylori eradication in duodenal ulcer |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative study | Hepato-gastroenterology | Compared lansoprazole vs. pantoprazole efficacy in active duodenal ulcer treatment and H. pylori eradication |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | Trial | Aliment Pharmacol Ther | Two-week pantoprazole + one week amoxycillin/clarithromycin effective for H. pylori eradication and duodenal ulcer healing |
| [10228801](https://pubmed.ncbi.nlm.nih.gov/10228801/) | 1999 | Trial | Hepato-gastroenterology | Rapid symptomatic improvement with pantoprazole, amoxycillin, and metronidazole in H. pylori-positive duodenal ulcer patients |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review / Network Meta-analysis | Am J Gastroenterol | Compared P-CAB vs. PPI efficacy/safety for healing grade C/D esophagitis, an acid-related indication mechanistically linked to peptic ulcer treatment |

---

## US Market Information

No marketing authorization / license records were found in the evidence pack (market status: **Not Marketed**, total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3 trials and a substantial literature base (including RCTs on PPI-based H. pylori eradication and ulcer healing), but the rationale itself flags that this "new indication" is functionally a core, already-established PPI use rather than a novel repurposing signal — and the drug currently has no marketing authorization on record. Guardrails are appropriate to avoid overstating novelty while the underlying evidence remains genuinely strong for the pharmacological class.

**To proceed, the following is needed:**
- TFDA (or relevant regulatory) label warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Detailed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Drug-drug interaction (DDI) data, currently not found
- Clarification of original/labeled indication and marketing status, since no licenses are on record for this market
- Confirmation of whether this candidate should be scored as a repurposing opportunity vs. a label-extension/validation case, given the rationale's own caveat about mechanistic overlap with the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

