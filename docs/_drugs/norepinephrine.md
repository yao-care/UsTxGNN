---
layout: default
title: Norepinephrine
parent: Moderate Evidence (L3-L4)
nav_order: 976
evidence_level: L4
indication_count: 3
monitor_inn: "NOREPINEPHRINE"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome"]
last_modified_at: 2026-10-14
description: "Norepinephrine: predicted new indication Obstructive lung disease (evidence level L4). Approved use: Asthma, bronchitis, pulmonary emphysema, bronchiectasis…"
---

# Norepinephrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Norepinephrine: From Asthma and Obstructive Airway Disease to Obstructive Lung Disease
{: .text-alpha }

## One-Sentence Summary

Norepinephrine is an adrenergic agonist (a catecholamine) whose historical indications in the knowledge graph include asthma, bronchitis, emphysema, bronchiectasis and hypotensive disorders.
The TxGNN model predicts it may be effective for **obstructive lung disease**, but only **1 clinical trial** (graded low relevance) and **18 publications** (mostly background reviews and physiology papers) were found, and none test norepinephrine as a treatment for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema, bronchiectasis, hypotensive disorder (from the knowledge graph; no approved indication text in the US license record) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Norepinephrine is known as an adrenergic agonist with predominantly alpha-1 activity. Its original indications in the knowledge graph (asthma, bronchitis, emphysema, bronchiectasis) are themselves obstructive airway diseases, so the prediction largely restates the historical label rather than offering new repurposing insight.

The literature does discuss adrenergic signalling and airway innervation in asthma and COPD, and neuroimmune mechanisms are plausible (PMID 29696025, 21271508, 41601146). However, systemic norepinephrine is a potent vasopressor and not a practical bronchodilator. The high TxGNN score is a computational prediction only and is not supported by clinical evidence for this use.

The other two predictions are weaker still. "Respiratory malformation" (score 99.84%) is supported only by preclinical work on noradrenergic control of breathing and by prenatal-exposure safety papers, which are not treatment evidence. "Rienhoff syndrome" (score 99.83%) has no trials and no literature, so no mechanistic link can be established.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function, exercise and skeletal muscle feedback in hypertension rehabilitation. It does not test norepinephrine for obstructive lung disease and provides no efficacy or safety evidence for this indication. |

## Literature Evidence

No randomized trials were found. The retrieved publications are reviews and physiological or observational studies, listed here by relevance.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29696025](https://pubmed.ncbi.nlm.nih.gov/29696025/) | 2018 | Review | Front Immunol | Adrenergic signalling at the interface of allergic asthma and viral infections |
| [41601146](https://pubmed.ncbi.nlm.nih.gov/41601146/) | 2026 | Review | Ann Med | Neuroimmune circuits in respiratory disease and potential therapeutic targets |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | Airway innervation in asthma and COPD, including sympathetic norepinephrine signalling |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Review | Semin Immunol | Neuroendocrine regulation of inflammation by the sympathetic nervous system |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Review | Crit Care Clin | Catecholamines (norepinephrine, epinephrine, dopamine) in critical care |
| [40870471](https://pubmed.ncbi.nlm.nih.gov/40870471/) | 2025 | Review | Medicina (Kaunas) | Anxiety and depression as comorbidities of COPD |
| [3966494](https://pubmed.ncbi.nlm.nih.gov/3966494/) | 1985 | Physiological study | Am J Med | Effect of hypoxemia on sodium and water excretion in advanced COPD (11 patients) |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Physiological study | Am J Physiol Heart Circ Physiol | Muscle alpha-adrenergic responsiveness during exercise in COPD patients |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Panel study | Environ Pollut | Stress hormones and air pollution exposure in COPD and non-COPD participants |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Clinical study | Am J Med | Mechanisms of hypertension in COPD with acute respiratory failure, including norepinephrine levels |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| No number recorded (cancelled) | Norepinephrine (BioActive Nutritional, Inc.) | Liquid | No approved indication text recorded |

## Safety Considerations

- **Knowledge-graph contraindications**: hypertensive disorder, hypertension and thrombotic disease. These come from the knowledge graph and not from label text.
- **Drug Interactions**: 70 interactions were identified, all or mostly of Moderate severity. Examples include antidiabetic agents (metformin, sitagliptin, pioglitazone, canagliflozin, dapagliflozin, empagliflozin, semaglutide, insulins), as well as phentermine and diethylpropion.

Please refer to the package insert for key warnings and the full contraindication list, as label data was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial found is a Phase 1 hypertension study unrelated to this indication, and the literature consists of background reviews and physiology papers. The high TxGNN score is a computational prediction, the mechanistic overlap mostly restates the old label, and the only US product record is cancelled. Systemic norepinephrine is a vasopressor rather than a practical bronchodilator, and the knowledge-graph contraindications include hypertension and thrombotic disease.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clinical or well-designed preclinical evidence that norepinephrine, by a feasible route and dose, benefits obstructive lung disease
- Route and formulation compatibility assessment, since no suitable active US product is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

