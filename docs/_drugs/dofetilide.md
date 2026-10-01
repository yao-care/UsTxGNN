---
layout: default
title: Dofetilide
parent: Moderate Evidence (L3-L4)
nav_order: 619
evidence_level: L4
indication_count: 10
---

# Dofetilide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dofetilide: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dofetilide is an oral antiarrhythmic used for rhythm control in atrial fibrillation (AF) and atrial flutter.
The TxGNN model predicts it may be useful for **stroke disorder**, but the support is indirect: **5 clinical trials** and **8 publications** were retrieved, and none tests dofetilide for stroke prevention or treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation / atrial flutter (rhythm control). The license records contain no indication text, so this comes from the pack's rationale and literature. |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (the 5 listed are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in the source record. The pack's analysis describes dofetilide as a selective IKr (hERG/Kv11.1) potassium channel blocker. It prolongs cardiac repolarization to maintain sinus rhythm in AF and flutter.

The link to stroke is indirect. Stroke is a downstream complication of AF, but dofetilide has no known direct neuroprotective or antithrombotic action. The very high TxGNN score most likely reflects knowledge-graph proximity between AF and stroke, not a stroke-specific effect.

Post hoc AFFIRM data (PMID 15007003) suggest that sinus rhythm is associated with better survival, but the drugs used to maintain it were associated with worse survival. No stroke benefit from rhythm-control drugs is established, and rhythm control has not been shown to replace anticoagulation. The other top-10 predictions (for example ABri amyloidosis, Wildervanck syndrome, duodenal obstruction) have no supporting evidence and are likely knowledge-graph artifacts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2204 | CABANA: catheter ablation vs. antiarrhythmic drug therapy in AF. Dofetilide is not the isolated intervention, so this is only indirect evidence (grade B). |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | SAVE STROKE Phase II: neurological outcomes after AF ablation vs. routine medication in patients with recent stroke. No results, and dofetilide is not studied. |
| [NCT00392106](https://clinicaltrials.gov/study/NCT00392106) | Phase 3 | Suspended | 240 | Focused ultrasound pulmonary vein ablation vs. best medical therapy in paroxysmal AF. This is a device trial and does not count as Phase 3 drug evidence. |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drugs as first-line therapy for persistent AF. Not dofetilide-specific, and no stroke data yet. |
| [NCT05034432](https://clinicaltrials.gov/study/NCT05034432) | Phase 4 | Recruiting | 100 | PIVATAL: prophylactic ventricular arrhythmia ablation in LVAD candidates. Unrelated to stroke prevention with dofetilide. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26233885](https://pubmed.ncbi.nlm.nih.gov/26233885/) | 2016 | Systematic review / network meta-analysis | Journal of Cardiology | Comparative effectiveness of antiarrhythmic drugs for AF rhythm control, where comparative data to guide drug selection are limited. |
| [15007003](https://pubmed.ncbi.nlm.nih.gov/15007003/) | 2004 | Post hoc analysis of RCT (AFFIRM) | Circulation | Rhythm control gave no survival advantage over rate control in AF patients at high stroke risk. The on-treatment analysis relates survival to rhythm and treatment. |
| [21955243](https://pubmed.ncbi.nlm.nih.gov/21955243/) | 2012 | Cohort | J Cardiovasc Electrophysiol | Dofetilide reduced ventricular arrhythmias and ICD therapies. This is an off-label arrhythmia use, not a stroke outcome. |
| [32538135](https://pubmed.ncbi.nlm.nih.gov/32538135/) | 2020 | Cohort | Circ Arrhythm Electrophysiol | Outcomes and safety of dofetilide in AF patients with LVEF ≤35%. |
| [11174354](https://pubmed.ncbi.nlm.nih.gov/11174354/) | 2001 | Review | American Heart Journal | Pharmacologic management of AF. Notes the risk of embolic complications. |
| [11445058](https://pubmed.ncbi.nlm.nih.gov/11445058/) | 2001 | Review | Curr Treat Options Cardiovasc Med | Treatment of atrial flutter. |
| [20638626](https://pubmed.ncbi.nlm.nih.gov/20638626/) | 2010 | Review | Gender Medicine | Gender differences in AF. |
| [32435191](https://pubmed.ncbi.nlm.nih.gov/32435191/) | 2020 | Preclinical (animal) | Frontiers in Pharmacology | KCa2 and Kv11.1 channel inhibition in pigs with left ventricular dysfunction. |

None of these papers reports dofetilide preventing or treating stroke.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA210466 | Dofetilide | Capsule | Sun Pharmaceutical Industries, Inc. |
| ANDA207058 | Dofetilide | Capsule | Dr. Reddy's Laboratories Inc. |
| ANDA213220 | Dofetilide | Capsule | Novadoz Pharmaceuticals LLC |
| ANDA207058 | Dofetilide | Capsule | Major Pharmaceuticals |
| ANDA210740 | Dofetilide | Capsule | Aurobindo Pharma Limited |

Only oral capsules are listed. The records do not include approved indication text.

---

## Safety Considerations

- **Key Warnings**: Dofetilide carries QT-prolongation and torsades de pointes risk, and it must be initiated in a monitored setting. It can also cause bradycardia. A published case report (PMID 30700466) describes dofetilide-associated facial paralysis after cardioversion that mimicked stroke. Use in sinus-node dysfunction, as in the rank 4 prediction, is a safety concern rather than a therapeutic rationale.

Please refer to the package insert for full warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke prediction rests on AF–stroke proximity in the knowledge graph. No retrieved trial or paper tests dofetilide for stroke, and the retrieved trials compare ablation with antiarrhythmic drugs in general. Dofetilide also carries serious proarrhythmic risk and has no direct neuroprotective or antithrombotic mechanism.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank in the source record
- Dofetilide-specific data on stroke or thromboembolic outcomes, for example sub-analyses of AF rhythm-control trials
- Removal of the obsolete "susceptibility to ischemic stroke" term, or merging it into the stroke entry
- Reframing the question: dofetilide manages AF and does not replace anticoagulation for stroke prevention

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

