---
layout: default
title: Dofetilide
parent: 僅模型預測 (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
---

# Dofetilide
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

Using the txgnn-pipeline skill's report-writing conventions (this is a v5 pharmacist-report generation task), here is the report generated from the Evidence Pack.

---

# Dofetilide: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dofetilide is a Class III antiarrhythmic (selective Kv11.1/hERG/IKr potassium-channel blocker) originally indicated for pharmacologic cardioversion and maintenance of sinus rhythm in atrial fibrillation/atrial flutter. The TxGNN model predicts a very high association with **Stroke Disorder** (score 99.99%), and **5 clinical trials** and **8 publications** are currently linked to this pathway — however, on closer reading the evidence does not show dofetilide *preventing* stroke; it largely reflects the known AF–stroke co-occurrence in the knowledge graph, with one key trial (AFFIRM) actually showing rhythm-control strategies do **not** reduce stroke risk. This candidate should be treated as low-confidence pending further review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation / atrial flutter (rhythm conversion and maintenance of sinus rhythm) — per mechanistic evidence in this pack; not confirmed via a formal Taiwan/US label (see Data Gaps) |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.99% (rank 281 of all candidates) |
| Evidence Level | L3 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dofetilide is a selective Kv11.1 (hERG/IKr) potassium-channel blocker — a Class III antiarrhythmic approved for pharmacologic cardioversion of atrial fibrillation/atrial flutter and for maintenance of sinus rhythm afterward. (Note: this mechanism-of-action description is drawn from the evidence pack's repurposing rationale; the formal `original_moa` field is flagged as a data gap — DG002 — pending DrugBank confirmation.)

The link to "Stroke Disorder" is mechanistically indirect. TxGNN's high score appears to reflect the well-known clinical association between atrial fibrillation and cardioembolic stroke, rather than any direct pharmacological effect of dofetilide on stroke pathophysiology. Critically, this pack's own literature includes the AFFIRM trial sub-analysis (PMID 15007003), which found that a rhythm-control strategy (which includes Class III agents like dofetilide) offered **no reduction in stroke or death** compared with a rate-control strategy — both arms still required anticoagulation. This is evidence *against* interpreting rhythm restoration as a stroke-prevention mechanism.

In addition, dofetilide carries a well-established risk of QT prolongation and Torsades de Pointes, requiring in-hospital initiation and ECG monitoring — a safety burden that itself argues for caution rather than expanded use. One literature entry (PMID 30700466) even describes a case of dofetilide-associated facial paralysis being mistaken for stroke after cardioversion, underscoring how AF/stroke-adjacent search terms can surface adverse-event confounders rather than efficacy signals. Overall, the mechanistic case for repurposing dofetilide specifically for stroke is weak and is better explained as a knowledge-graph co-occurrence artifact than a therapeutic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A (catheter intervention) | Completed | 2,204 | CABANA trial: catheter ablation vs. antiarrhythmic drug therapy (dofetilide among comparator drugs) for AF; primary endpoint was a death/stroke/bleeding composite, not a dofetilide-specific stroke endpoint (relevance grade B). |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drugs (dofetilide a possible comparator) as first-line therapy for persistent AF; endpoints focus on rhythm control and ablation safety, not stroke outcomes (relevance grade B). |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | SAVE STROKE Phase II: neurological outcomes after AF ablation vs. routine medication in recent-stroke patients; does not use dofetilide as an intervention (relevance grade C). |
| [NCT00392106](https://clinicaltrials.gov/study/NCT00392106) | Phase 3 | Suspended | 240 | Device (HIFU pulmonary vein ablation) trial for paroxysmal AF vs. best medical therapy; a medical-device study, not a dofetilide drug trial (relevance grade C). |
| [NCT05034432](https://clinicaltrials.gov/study/NCT05034432) | Phase 4 | Recruiting | 100 | Prophylactic ventricular arrhythmia ablation in high-risk LVAD candidates; population and endpoint (ventricular arrhythmia, not stroke/AF) have low relevance (relevance grade C). |

*None of these trials directly evaluate dofetilide's effect on stroke incidence; at best two (grade B) include dofetilide as a comparator arm in AF rhythm-control studies.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15007003](https://pubmed.ncbi.nlm.nih.gov/15007003/) | 2004 | RCT (post-hoc/substudy) | Circulation | AFFIRM sub-analysis: rhythm-control strategy (incl. Class III drugs) showed no survival or stroke-risk advantage over rate control; sinus rhythm itself was associated with lower mortality only in an on-treatment analysis. |
| [21955243](https://pubmed.ncbi.nlm.nih.gov/21955243/) | 2012 | Cohort | J Cardiovasc Electrophysiol | Dofetilide reduced frequency of ventricular arrhythmias and ICD therapies in patients with implanted defibrillators — an off-label use, not an approved indication. |
| [32538135](https://pubmed.ncbi.nlm.nih.gov/32538135/) | 2020 | Cohort | Circ Arrhythm Electrophysiol | Dofetilide use in AF patients with reduced LVEF being considered for ICD; describes safety outcomes and LVEF improvement, not stroke prevention. |
| [26233885](https://pubmed.ncbi.nlm.nih.gov/26233885/) | 2016 | Comparative effectiveness/Cohort | J Cardiol | Comparative effectiveness of antiarrhythmic drugs (including dofetilide) for AF rhythm control; limited comparative outcome data available. |
| [11445058](https://pubmed.ncbi.nlm.nih.gov/11445058/) | 2001 | Review | Curr Treat Options Cardiovasc Med | General review of atrial flutter management strategies, including rate/rhythm control goals. |
| [20638626](https://pubmed.ncbi.nlm.nih.gov/20638626/) | 2010 | Review | Gend Med | Review of gender differences in AF epidemiology and management. |
| [11174354](https://pubmed.ncbi.nlm.nih.gov/11174354/) | 2001 | Review | Am Heart J | Review of pharmacologic AF management strategies and embolic-risk context. |
| [32435191](https://pubmed.ncbi.nlm.nih.gov/32435191/) | 2020 | Preclinical (animal model) | Front Pharmacol | Pig model studying KCa2/Kv11.1 channel inhibition and AF conversion; mechanistic, not clinical, evidence. |

*No literature directly demonstrates a stroke-preventive or stroke-treatment effect of dofetilide; the strongest-tier evidence (AFFIRM, tier 1) argues against the rhythm-control-prevents-stroke hypothesis.*

---

## US Market Information

Dofetilide is currently **not marketed** under this evidence pack's regulatory dataset (`market_status: 未上市`, 0 licenses recorded). No NDA/license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Formal TFDA warnings, contraindications, and drug-interaction data could not be retrieved for this evaluation (data gap DG001, severity: Blocking — this prevents the candidate from advancing past the S1 safety screening stage). Known class-level concerns (QT prolongation, Torsades de Pointes risk requiring in-hospital initiation) are referenced qualitatively in the mechanistic literature above but are not yet backed by a verified label source in this pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high TxGNN score is not corroborated by direct clinical or mechanistic evidence of a stroke-preventive effect — the strongest available literature (AFFIRM) actually contradicts the rhythm-control-prevents-stroke hypothesis, and a blocking data gap (missing TFDA label/warnings, DG001) prevents even a basic safety screen.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA/official label for warnings and contraindications before any S1 safety evaluation can proceed
- Resolve DG002 (High): confirm mechanism-of-action data via DrugBank API rather than relying on rationale-text inference
- Drug-interaction (DDI) data, currently unavailable (`query_status: not_found`)
- A mechanistic study or clinical endpoint that isolates dofetilide's effect on stroke incidence independent of general AF rhythm-control strategy
- Re-evaluation against the AFFIRM-type negative evidence before considering advancement beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

