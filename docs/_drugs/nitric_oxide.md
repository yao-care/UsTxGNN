---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 970
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide (DB00435): Repurposing Candidate for Pulmonary Arterial Hypertension

> **Evaluator's note on indication selection:** TxGNN's top five ranked predictions for nitric oxide (dental/periodontal malformation syndrome, hypertrichosis, Ambras syndrome, Dandy-Walker–related syndrome, isolated hair shaft abnormality) were reviewed against their supporting evidence and judged to be **keyword co-occurrence artifacts with no real mechanistic basis** — each is explicitly flagged `Hold`/L4–L5 in the underlying evidence pack. This report instead focuses on **Pulmonary Arterial Hypertension (rank 7)**, the highest-ranked prediction for this drug that is both mechanistically coherent and backed by substantial clinical evidence (L1, *Proceed with Guardrails*). A closely related sibling prediction, *PAH associated with congenital heart disease* (rank 8, also L1), reinforces the same signal and is discussed alongside it.

## One-Sentence Summary

Nitric oxide has no documented original indication or license on file in this evidence pack (market status: **Not Marketed**, 0 registered authorizations), and its mechanism-of-action data is currently missing (data gap).
The TxGNN model predicts it may be effective for **Pulmonary Arterial Hypertension**,
with **50 clinical trials** and **20 publications** currently supporting this direction — including a completed Phase 3 trial of inhaled nitric oxide itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no approved indication on file) |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for nitric oxide is flagged as a **blocking data gap (DG002)** in this evidence pack, and no original indication is currently on file for this drug in this jurisdiction. That said, the literature retrieved in support of this prediction consistently describes NO's canonical pharmacology: it diffuses into pulmonary vascular smooth muscle and activates soluble guanylate cyclase (sGC), raising intracellular cGMP and producing potent, relatively lung-selective vasodilation.

This is the same NO–sGC–cGMP axis already targeted — indirectly — by approved PAH therapies such as PDE5 inhibitors (sildenafil, which prevents breakdown of cGMP) and sGC stimulators (riociguat, which sensitizes sGC to NO). Because inhaled NO acts further upstream, supplying the vasodilator signal directly, the link TxGNN identified has a coherent, well-documented pharmacological rationale rather than being a spurious statistical association. This is further reinforced by the closely related, similarly-scored prediction "pulmonary arterial hypertension associated with congenital heart disease" (rank 8, also L1/Proceed with Guardrails), which shares essentially the same trial and literature base — inhaled NO is already established practice in neonatal/pediatric post-cardiac-surgery pulmonary hypertension.

The main uncertainty is not mechanistic plausibility but clinical positioning: most of the strongest completed trials involve inhaled NO in acute, procedural, or neonatal contexts (post-cardiac-surgery PH, vasoreactivity testing, PPHN) rather than chronic idiopathic PAH, where oral pathway-modulating drugs (PDE5i, sGC stimulators, prostacyclin analogues) are standard of care. This distinction should be central to any further evaluation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01959828](https://clinicaltrials.gov/study/NCT01959828) | Phase 3 | Completed | 18 | Japanese multi-center study of IK-3001 (inhaled NO) for peri-/post-operative PH associated with cardiac surgery |
| [NCT00005776](https://clinicaltrials.gov/study/NCT00005776) | Phase 3 | Terminated | 235 | NINOS landmark RCT: iNO vs 100% oxygen in term/near-term infants with hypoxic respiratory failure |
| [NCT00005773](https://clinicaltrials.gov/study/NCT00005773) | Phase 3 | Terminated | 302 | Early vs standard-threshold iNO therapy to reduce death/ECMO use in term/near-term infants with respiratory failure |
| [NCT03602781](https://clinicaltrials.gov/study/NCT03602781) | Phase 3 | Withdrawn | 0 | Planned randomized withdrawal study of iNO (LTOT) in PAH patients with prior exercise tolerance improvement |
| [NCT01265888](https://clinicaltrials.gov/study/NCT01265888) | Phase 2 | Completed | 31 | Dose-escalation study of inhaled NO (GeNOsyl® system) in PAH (WHO Group 1) and PH secondary to IPF |
| [NCT02734953](https://clinicaltrials.gov/study/NCT02734953) | Phase 2 | Completed | 10 | Effects of iNO on invasively-measured pulmonary vascular parameters in PAH patients |
| [NCT03727451](https://clinicaltrials.gov/study/NCT03727451) | Phase 2 | Completed | 17 | Dose-escalation safety/efficacy study of pulsed iNO in PH associated with pulmonary fibrosis or sarcoidosis on LTOT |
| [NCT04231084](https://clinicaltrials.gov/study/NCT04231084) | Phase 4 | Completed | 115 | Acute hemodynamic comparison of inhaled NO vs inhaled epoprostenol across PH phenotypes |
| [NCT00352430](https://clinicaltrials.gov/study/NCT00352430) | Phase 1 | Completed | 31 | NO-based therapies evaluated for hemolysis-associated pulmonary hypertension (sickle cell disease/thalassemia) |
| [NCT00001963](https://clinicaltrials.gov/study/NCT00001963) | Phase 1 | Completed | 28 | Comparison of endothelium-derived vs hemoglobin-transported NO vascular effects in healthy subjects (mechanistic) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32442078](https://pubmed.ncbi.nlm.nih.gov/32442078/) | 2020 | Review | Current Medicinal Chemistry | Comprehensive review of the NO pathway in PAH: pathomechanism, biomarkers, and drug targets |
| [23822809](https://pubmed.ncbi.nlm.nih.gov/23822809/) | 2013 | Review | Am J Respir Crit Care Med | NO deficiency and endothelial dysfunction as central drivers of pulmonary vascular disease in PAH |
| [20051913](https://pubmed.ncbi.nlm.nih.gov/20051913/) | 2010 | Review | Journal of Hypertension | Role of NO, oxidative stress, and inflammation in PAH pathogenesis |
| [33836637](https://pubmed.ncbi.nlm.nih.gov/33836637/) | 2021 | Review | J Cardiovasc Pharmacol Ther | Combination PAH therapy targeting the NO and prostacyclin pathways together |
| [38054614](https://pubmed.ncbi.nlm.nih.gov/38054614/) | 2024 | Review | Small | Novel inhalable NO delivery systems (NO-releasing microspheres) developed for PAH treatment |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Diagnosis and treatment overview of PAH, including NO-pathway-directed therapy |
| [39209476](https://pubmed.ncbi.nlm.nih.gov/39209476/) | 2024 | Review | Eur Respir J | Current PAH treatment algorithm across the endothelin, NO, prostacyclin, and BMP/activin pathways |
| [37516248](https://pubmed.ncbi.nlm.nih.gov/37516248/) | 2023 | Review | Presse Médicale | General review of PAH pathophysiology and treatment, including NO signaling |
| [15194181](https://pubmed.ncbi.nlm.nih.gov/15194181/) | 2004 | Review | J Am Coll Cardiol | NO pathway and PDE-5 inhibition as therapeutic strategy in PAH |
| [33773120](https://pubmed.ncbi.nlm.nih.gov/33773120/) | 2021 | RCT | Lancet Respir Med | REPLACE trial: switching to riociguat (NO-pathway sGC stimulator) vs continued PDE5i in PAH |

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Collection of TFDA-equivalent label warnings and contraindications for this drug is flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any formal S1 safety review can proceed. No drug-drug interaction data was found (`query_status: not_found`).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The NO–sGC–cGMP pathway underlying this prediction is well-established PAH pharmacology, and it is supported by 50 clinical trials (including a completed Phase 3 trial of NO itself) and 20 publications — evidence level L1. However, most direct NO trials are in acute/perioperative/neonatal PH settings rather than chronic idiopathic PAH, so guardrails are needed around indication scope, route, and dosing before advancing further.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA-equivalent label warnings/contraindications) — currently blocking
- Resolve DG002 (formal mechanism-of-action documentation)
- Route compatibility assessment (inhaled vs other routes; `route_compatibility.status` is currently pending)
- Clarify which PAH subpopulation (acute vasoreactivity/perioperative vs chronic idiopathic PAH) the repurposing claim targets, given the evidence base skews toward the former
- Formal DDI review, since none was found in current sources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

