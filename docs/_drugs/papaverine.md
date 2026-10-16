---
layout: default
title: Papaverine
parent: Moderate Evidence (L3-L4)
nav_order: 1014
evidence_level: L4
indication_count: 10
monitor_inn: "PAPAVERINE"
predicted_indications: ["ischemic disease", "intracranial arteriosclerosis", "non-inflammatory vasculopathy", "vascular ectasia", "fibrocartilaginous embolism", "venous thromboembolism", "vascular insufficiency disorder", "angiodysplasia", "Raynaud disease", "Monckeberg arteriosclerosis"]
---

# Papaverine
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

# Papaverine: From Peripheral Vascular Disease to Ischemic Disease

## One-Sentence Summary

Papaverine is a smooth muscle relaxant and vasodilator, originally used for peripheral vascular disease and cerebral ischemia.
The TxGNN model predicts it may be effective for **ischemic disease**,
but the supporting evidence is thin: **1 registered clinical trial** (a diagnostic registry that does not test papaverine as a treatment) and **20 publications**, mostly reviews, procedural reports and animal studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral vascular disease, intermittent claudication, peripheral arterial disease, brain ischemia, transient ischemic attack |
| Predicted New Indication | Ischemic disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

*Note: the original indications come from the TxGNN knowledge graph. The data compiled for this report contains no approved indication text from the US label.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, papaverine is a non-specific smooth muscle relaxant and phosphodiesterase inhibitor. By raising cAMP and cGMP it causes vasodilation, which is plausibly relevant to ischemic conditions.

The original indications (peripheral arterial disease, cerebral ischemia, transient ischemic attack) already overlap strongly with "ischemic disease." This prediction is therefore largely an extension of existing uses rather than true repurposing, and it offers limited novelty.

The retrieved literature is indirect. It covers intra-arterial papaverine for non-occlusive mesenteric ischemia, coronary flow reserve measurement, and vasospasm management. These are procedural or adjunct uses, not efficacy trials of papaverine as a treatment for ischemic disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06125392](https://clinicaltrials.gov/study/NCT06125392) | N/A | Recruiting | 1000 | MICRO-SNAPE registry of patients with chronic angina and no obstructive coronary stenosis, collecting data on coronary microvascular dysfunction and spasm. It is a diagnostic registry and does not test papaverine as a therapy; the link to the drug is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3661361](https://pubmed.ncbi.nlm.nih.gov/3661361/) | 1987 | Cohort | Am Heart J | Intracoronary papaverine was superior to radiographic contrast for measuring coronary flow reserve in ischemic heart disease (a diagnostic use) |
| [16368347](https://pubmed.ncbi.nlm.nih.gov/16368347/) | 2006 | Comparative study | Ann Thorac Surg | Papaverine versus glyceryl trinitrate–verapamil solution for internal thoracic artery spasm, comparing delivery methods |
| [28455799](https://pubmed.ncbi.nlm.nih.gov/28455799/) | 2018 | Case report | J Robot Surg | Periarterial papaverine relieved renal artery vasospasm during robot-assisted partial nephrectomy |
| [21761272](https://pubmed.ncbi.nlm.nih.gov/21761272/) | 2011 | Guideline/Review | Neurocrit Care | Critical care guidelines on endovascular management of cerebral vasospasm after subarachnoid hemorrhage |
| [32713799](https://pubmed.ncbi.nlm.nih.gov/32713799/) | 2020 | Preclinical | J Pharmacol Sci | In mice with focal cerebral ischemia, papaverine reduced infarct volume and showed anti-inflammatory, immunomodulatory effects |
| [28832798](https://pubmed.ncbi.nlm.nih.gov/28832798/) | 2017 | Preclinical | Braz J Cardiovasc Surg | Papaverine and vitamin C were studied against rat liver ischemia-reperfusion injury after aortic cross-clamping |
| [7590571](https://pubmed.ncbi.nlm.nih.gov/7590571/) | 1995 | Review | Hepato-gastroenterology | Non-occlusive mesenteric ischemia, with vasodilator infusion among the discussed approaches |
| [7956590](https://pubmed.ncbi.nlm.nih.gov/7956590/) | 1994 | Review | Dis Colon Rectum | Acute arterial mesenteric ischemia syndromes: causes, diagnosis and management |
| [8293164](https://pubmed.ncbi.nlm.nih.gov/8293164/) | 1993 | Review | Curr Opin Neurol | Interventional neuroradiology, including superselective papaverine infusion for vasospasm after aneurysm rupture |
| [1291208](https://pubmed.ncbi.nlm.nih.gov/1291208/) | 1992 | Other | Chin Med J | Ligusticum chuanxiong preparations in ischemic stroke, with papaverine used as a comparator |

No randomized controlled trial of papaverine for ischemic disease was found.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Papaverine Hydrochloride (Nexus Pharmaceuticals, LLC) | Injection | Not available (license cancelled) |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): liver disease, gallbladder disease, hypotensive disorder, coronary artery disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, sudden cardiac arrest, heart conduction disease, glaucoma, atrioventricular block.
- **Drug Interactions**: The interaction query returned 100 records. The ones listed here include many rated **Major**: abiraterone, tramadol, adenosine, salbutamol, alfuzosin, amiodarone, amisulpride, amitriptyline, anagrelide, propofol, loperamide, apalutamide, apomorphine, arsenic trioxide, lumefantrine, asenapine and atomoxetine. Moderate-level interactions include amifostine, apraclonidine and aripiprazole. Many of the Major interactions involve QT prolongation or additive cardiovascular effects, so careful review is needed before any use alongside these agents.

Official package insert warnings and contraindications were not available in the compiled data; please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.91%), but the supporting evidence is indirect (diagnostic registry, procedural uses, case reports, animal studies) and the predicted indication largely overlaps papaverine's existing indications. The US license is cancelled, and the official safety label data are missing, which blocks safety screening.

**Other predicted indications (for reference):**
- **Raynaud disease** (L4, the most credible secondary candidate): vasospasm is a coherent target, supported only by a 1951 article, a case report of intra-arterial infusion, and a 2025 DIEP flap case series. It would need prospective comparison against calcium channel blockers.
- **Intracranial arteriosclerosis** (L4): only dated, small, uncontrolled studies from the 1970s–80s.
- **Vascular insufficiency disorder** (L4): literature concerns diagnostic intracavernosal use for erectile dysfunction, not systemic treatment.
- **Non-inflammatory vasculopathy, fibrocartilaginous embolism, angiodysplasia, Monckeberg arteriosclerosis** (L5): prediction only, with no supporting evidence.
- **Vascular ectasia and venous thromboembolism** (L5): the mechanism does not support benefit and the retrieved papers are unrelated, so these look like model artifacts.

**To proceed, the following is needed:**
- Obtain and review the current FDA package insert (warnings, contraindications) to complete safety screening
- Detailed mechanism of action data from DrugBank
- Clarify the regulatory status of the cancelled injection license and the availability of any marketed papaverine product
- Prospective or controlled clinical data for a defined ischemic indication (Raynaud disease is the most promising starting point)
- A cardiovascular safety and drug-interaction management plan, given the many Major interactions and the knowledge-graph contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

