---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 918
evidence_level: L5
indication_count: 5
---

# Metoclopramide
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

# Metoclopramide: From No Local Approval to Predicted Gastric Ulcer Use

## One-Sentence Summary

Metoclopramide is a dopamine D2 antagonist / 5‑HT4 agonist prokinetic agent that is **not currently marketed in this jurisdiction** (no approved indication on file locally).
The TxGNN model predicts it may be effective for **Gastric Ulcer (disease)**, with **2 clinical trials** and **20 publications** returned by the evidence search — though most of this evidence is decades-old animal/mechanistic work, and the evidence pack's own mechanistic assessment flags the biological link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is not currently marketed in this jurisdiction (0 licenses) |
| Predicted New Indication | Gastric Ulcer (disease) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this evidence pack (open data gap DG002). Based on the pharmacology cited in the evidence pack's own repurposing rationale, metoclopramide acts as a dopamine D2 antagonist and 5‑HT4 agonist with **prokinetic** effects — it promotes gastric emptying and raises lower esophageal sphincter tone. It is not an acid suppressant or a mucosal protectant.

This matters because standard gastric ulcer therapy targets acid suppression (PPIs, H2 blockers) or *H. pylori* eradication — mechanisms metoclopramide does not share. The evidence pack's rationale explicitly notes this mismatch: 1970s–80s animal studies (rats, guinea pigs) on gastric ulcer protection show **inconsistent** results, and several are protective via non-acid-related mechanisms (improved gastric drainage, reduced pyloric reflux) rather than mucosal healing per se.

In short, the very high TxGNN score is not well corroborated by a coherent mechanistic story or by controlled clinical evidence — the biological plausibility for this specific indication is weak, which is reflected in the "Hold" recommendation already assigned in the evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Tests whether metoclopramide premedication before endoscopy improves GI-wall visibility and reduces need for repeat endoscopy/IR/surgery in upper GI bleeding — this is a premedication/visualization study, **not** a gastric-ulcer treatment trial. Graded low relevance (C); status not updated since the 2024 completion date. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist-led prescribing-safety quality-improvement programme in Scottish primary care. Unrelated to gastric ulcer treatment; weak co-occurrence match (graded C). |

---

## Literature Evidence

*20 publications were returned; the 5 below are the only ones with a completed study-type classification in the evidence pack. The remaining 15 are older, unclassified physiology/case reports and are not detailed here to avoid overstating their relevance.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT (small, surgical premedication) | Yonsei Medical Journal | IV metoclopramide + ranitidine reduced preoperative gastric contents vs. saline in day-case laparoscopic gynecologic surgery (n=20/group). A perioperative RCT, not a gastric-ulcer treatment study. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Annals of Internal Medicine | General pharmacology review; metoclopramide's established roles are as an antiemetic (chemotherapy-induced vomiting) and GI prokinetic, not an acid-suppressive ulcer therapy. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Era-appropriate review of gastric/duodenal ulcer drug therapy; metoclopramide appears only as a motility adjunct, predating the modern PPI/H2-blocker/*H. pylori* treatment paradigm. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | In rats, metoclopramide (20–50 mg/kg) showed an ulcer-protective effect in aspirin-induced and pylorus-ligated models, comparable to ranitidine. Preclinical only. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal study | Indian J Physiol Pharmacol | In guinea pigs, metoclopramide protected against experimentally-induced gastric ulceration without changing acid secretion — suggesting a drainage/motility-based mechanism rather than mucosal healing. Preclinical only. |

---

## Market Information

No approved product licenses are on file — metoclopramide is currently **not marketed** in this jurisdiction (0 of 0 NDAs).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is very high (99.93%), but the supporting evidence is almost entirely decades-old preclinical/animal work and tangentially related trials (endoscopy premedication, unrelated QI programme) — no controlled trial directly tests metoclopramide for gastric ulcer healing.
- The evidence pack's own mechanistic rationale flags weak biological plausibility: metoclopramide is a prokinetic agent, not an acid suppressant or mucosal protectant, which is the established mechanism class for this indication.
- The drug has no local market license (0 NDAs, not marketed), so there is no regulatory/safety file to begin a formal S1 review.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any safety evaluation
- Resolve DG002: confirm mechanism of action via DrugBank API to properly assess mechanistic relevance
- Clarify local licensing/import status given the current 0-NDA position
- Identify a modern, adequately powered RCT testing metoclopramide specifically for gastric ulcer healing (not motility/premedication surrogate endpoints) before advancing beyond Hold
- Complete the outstanding DDI query (currently `not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

