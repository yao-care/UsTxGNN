---
layout: default
title: Nicardipine
parent: Moderate Evidence (L3-L4)
nav_order: 964
evidence_level: L4
indication_count: 5
monitor_inn: "NICARDIPINE"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant renovascular hypertension", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-14
description: "Nicardipine: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L4). Approved use: Hypertension / hypertensive disorder"
---

# Nicardipine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Nicardipine: From Hypertension to Pulmonary Hypertension Due to Lung Disease and/or Hypoxia

## One-Sentence Summary

Nicardipine is a calcium channel blocker originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but there are currently **0 clinical trials** and only **1 directly relevant publication** (a 1988 animal study) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (from the knowledge graph; no approved-indication text is available in the license records) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all licenses listed as cancelled) |
| Number of NDAs | 12 (2 NDAs and 10 ANDAs) |
| Recommended Decision | Hold |

*Note: The prediction ranked first by the model is "pulmonary hypertension with unclear multifactorial mechanism" (score 99.26%, L5, no trials or literature). This report focuses on the second-ranked prediction, which has the most supporting literature.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, nicardipine is a dihydropyridine calcium channel blocker. It relaxes vascular smooth muscle and causes vasodilation, which is how it lowers blood pressure in hypertension.

Pulmonary hypertension due to lung disease or hypoxia is driven largely by hypoxic pulmonary vasoconstriction (HPV), a calcium-dependent constriction of pulmonary arteries. Blocking calcium entry could, in principle, relax these vessels and lower pulmonary pressure. A 1988 study in dogs (PMID 3132192) directly examined nicardipine's effect on regional HPV, which gives physiological support for this link.

There is an important caution. Inhibiting HPV can worsen ventilation-perfusion matching and lower blood oxygenation in patients with lung disease. The mechanistic rationale is therefore plausible but double-edged. The high TxGNN score is a computational prediction and does not replace clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Most of the retrieved publications are indirect or unrelated (cardiomyocyte physiology, in vitro cell work, other calcium blockers). The most relevant ones are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3132192](https://pubmed.ncbi.nlm.nih.gov/3132192/) | 1988 | Preclinical / physiology study | British Journal of Anaesthesia | Effect of nicardipine on regional hypoxic pulmonary vasoconstriction in 14 open-chest dogs; higher doses raised cardiac output, so responses were also assessed under controlled cardiac output |
| [19035721](https://pubmed.ncbi.nlm.nih.gov/19035721/) | 2008 | Clinical study (indirect) | Journal of Neurosurgery | Effect of IV nicardipine on brain tissue oxygenation during hypertensive emergencies in acute brain disease |
| [22366846](https://pubmed.ncbi.nlm.nih.gov/22366846/) | 2012 | Preclinical (indirect) | Anesthesia and Analgesia | Nimodipine- vs nitroglycerin-induced hypotension and memory in mice; nicardipine also tested |
| [2693295](https://pubmed.ncbi.nlm.nih.gov/2693295/) | 1989 | Review | Fundamental & Clinical Pharmacology | Calcium antagonists' CNS effects, including use in cerebral ischaemia, vasospasm and hypoxia |
| [14751848](https://pubmed.ncbi.nlm.nih.gov/14751848/) | 2004 | Preclinical | Am J Physiol Lung Cell Mol Physiol | 5-HT-induced calcium influx in rat small pulmonary arteries; relevant to the mechanism of pulmonary vasoconstriction |
| [3288055](https://pubmed.ncbi.nlm.nih.gov/3288055/) | 1988 | Review | Annals of the NY Academy of Sciences | Cardiomyocyte pathophysiology (general background) |

No randomized controlled trials or human studies in pulmonary hypertension were found.

---

## US Market Information

All 12 licenses in the data are listed as cancelled, and none include approved-indication text. Five representative entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019734 | CARDENE IV (Baxter Healthcare) | Injection, solution | Not listed in the data |
| NDA022276 | Nicardipine Hydrochloride (Hikma) | Injection | Not listed in the data |
| ANDA218638 | Nicardipine Hydrochloride (Zydus) | Capsule | Not listed in the data |
| ANDA216420 | Nicardipine Hydrochloride (Armas) | Injection | Not listed in the data |
| ANDA217548 | Nicardipine Hydrochloride (Fresenius Kabi) | Injection | Not listed in the data |

Both oral (capsule) and injectable forms exist among the listed licenses.

---

## Cytotoxicity

Not applicable: nicardipine is not an antineoplastic drug.

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: liver disease, gallbladder disease, hypotensive disorder, impaired renal function, intracerebral hemorrhage, cerebral infarction, ischemic stroke susceptibility, cerebrovascular disorder, cerebral artery occlusion, brain stem infarction.
- **Drug Interactions**: 100 interactions were identified. Most are Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), bupropion, aprepitant, morphine, aspirin, cimetidine, miconazole, magnesium sulfate, and SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin). One **Major** interaction was noted with **dolasetron**.
- **Indication-specific concern**: Blocking hypoxic pulmonary vasoconstriction may worsen oxygenation in patients with lung disease.

Please refer to the package insert for full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and one 1988 animal study, with no clinical trials and no human data in pulmonary hypertension. The possible worsening of oxygenation through HPV inhibition is a real safety concern. Current evidence is at the L4 level.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Human haemodynamic and oxygenation studies in pulmonary hypertension due to lung disease
- Review of the current US regulatory status, since all listed licenses are cancelled
- Assessment of whether the other predictions merit follow-up. Malignant renovascular hypertension and malignant hypertensive renal disease overlap with the original indication, and the Braddock syndrome prediction has no identifiable mechanistic link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

