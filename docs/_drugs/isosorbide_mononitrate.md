---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 816
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: A Nitrate Vasodilator Under Evaluation for Pulmonary Arterial Hypertension

## One-Sentence Summary

> Isosorbide mononitrate (ISMN, DB01020) has no Taiwan market license on file, and its original approved indication is not available in this Evidence Pack (data gap). TxGNN's top-ranked predictions (hypertrichosis, alopecia, and several rare congenital syndromes) were reviewed and found to have **no supporting mechanistic or literature evidence** — most appear to be artifacts of disease-embedding clustering in the model. The one candidate with genuine, if preliminary, support is **Pulmonary Arterial Hypertension (PAH)**, ranked #10 by TxGNN score but the only indication reaching evidence level **L3** with **6 literature references** and a coherent NO–sGC–cGMP mechanistic rationale.

**Note on methodology deviation:** This report deviates from mechanically reporting `predicted_indications[0]` (hypertrichosis) as the headline candidate. The evidence pack's own rationale text for ranks 1–9 explicitly states there is "no clinical or preclinical evidence" and flags internal contradictions (e.g., near-identical high scores for both alopecia and hypertrichosis — opposite phenotypes). Presenting a Hold-recommendation, zero-evidence prediction as the lead finding would be misleading. PAH is used below as the substantive candidate for evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — TFDA has no market license on file for this drug (data gap, see DG001/DG002) |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.94% (rank 10 of candidate list) |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold (Research Question — hypothesis-generating, not yet clinically actionable) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity — DrugBank MOA lookup pending). Based on known pharmacology reflected in the literature evidence itself, isosorbide mononitrate is a nitric oxide (NO) donor that acts through the NO–soluble guanylate cyclase (sGC)–cGMP signaling pathway to produce vasodilation.

This pathway is already a validated drug target in PAH: riociguat directly stimulates sGC, and sildenafil prolongs cGMP signaling by inhibiting its breakdown. One literature reference (PMID 29705351) directly examined NO-sensitive sGC stimulation in a monocrotaline-induced pulmonary hypertension rat model, and another (PMID 29377691) describes a novel hybrid molecule synthesized from ISMN itself that produced pulmonary vasodilation and reduced vascular remodeling in PAH rats. This gives the ISMN→PAH hypothesis a concrete mechanistic anchor, unlike the hair-disorder predictions.

However, the rationale also flags a known limitation: chronic nitrate use is associated with pharmacological tolerance and reflex tachycardia, and **no clinical trial has tested ISMN directly in PAH patients**. The supporting literature is a mix of drug-design, preclinical, and tangentially related clinical studies (several concern cirrhosis-related portal hypertension or coronary artery disease, not PAH) — so this remains a research hypothesis rather than a clinically supported repurposing case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29377691](https://pubmed.ncbi.nlm.nih.gov/29377691/) | 2018 | Drug design/synthesis | Journal of Medicinal Chemistry | Novel hybrid synthesized from ISMN + bardoxolone methyl lowered mean pulmonary artery pressure and right ventricular systolic pressure, with dual vasodilation and anti-remodeling activity in PAH rats |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical/Animal model | Life Sciences | Examined NO-sensitive soluble guanylate cyclase stimulation in monocrotaline-induced pulmonary hypertension rats, supporting the NO-sGC pathway as a target for halting PH progression |
| [3384359](https://pubmed.ncbi.nlm.nih.gov/3384359/) | 1988 | Review/Pharmacology | Gut | Oral ISMN reduced portal pressure via decreased portal venous resistance in cirrhotic patients with portal hypertension (hepatic, not pulmonary, vasculature) |
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical (CAD, not PAH) | Journal of Sexual Medicine | Hemodynamic study of sildenafil plus ISMN in coronary artery disease patients with erectile dysfunction; not a PAH population |
| [2759546](https://pubmed.ncbi.nlm.nih.gov/2759546/) | 1989 | Clinical (cirrhosis, unrelated) | Hepatology | Randomized study found ISMN had no significant effect on hepatic hemodynamics in HBsAg-positive cirrhosis — a negative finding, unrelated to PAH |
| [9673832](https://pubmed.ncbi.nlm.nih.gov/9673832/) | 1998 | Review | Clinical Pharmacokinetics | General pharmacokinetic review of vasodilator classes including nitrates; background context only |

---

## Taiwan Market Information

No licensing records are available — this drug currently has **0 approved licenses** and market status "未上市" (not marketed) in Taiwan.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are flagged as a **Blocking** data gap — DG001 — pending TFDA package insert retrieval; this must be resolved before any S1 safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PAH hypothesis has a coherent mechanistic basis (NO–sGC–cGMP pathway, an established PAH drug target) and preclinical/drug-design support, but no clinical trial has tested ISMN in PAH patients, and the drug is unmarketed in Taiwan with no available safety labeling. The other nine TxGNN-ranked predictions (hypertrichosis, alopecia, and several rare syndromes) lack any supporting evidence and should not be pursued further — they are most plausibly artifacts of disease-embedding proximity in the model.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action from DrugBank (DG002, High)
- A dedicated preclinical or early-phase clinical study of ISMN specifically in PAH populations
- Clarification of Taiwan/global regulatory status, since this drug currently has no Taiwan market license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

