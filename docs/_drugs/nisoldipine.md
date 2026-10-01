---
layout: default
title: Nisoldipine
parent: Model Prediction Only (L5)
nav_order: 968
evidence_level: L5
indication_count: 5
---

# Nisoldipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Nisoldipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

> Nisoldipine is a dihydropyridine calcium channel blocker marketed in the US as an antihypertensive (Sular).
> The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
> but there are **0 clinical trials** and **no publications about nisoldipine in this condition**, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the license records carry no indication text, so this is inferred from the drug class) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all records are the same application, NDA020356) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record. Based on known information, nisoldipine is a dihydropyridine L-type calcium channel blocker that relaxes vascular smooth muscle and lowers vascular resistance. Pulmonary vasodilation is therefore superficially plausible.

The mechanistic fit is weak for this specific indication. In pulmonary hypertension caused by lung disease or hypoxia (Group 3), calcium channel blockers can blunt hypoxic pulmonary vasoconstriction. That may worsen ventilation-perfusion matching and hypoxemia. Guidelines do not support them outside the small vasoreactive subset of Group 1 pulmonary arterial hypertension.

The very high score most likely reflects graph proximity to other antihypertensive drugs rather than a validated mechanism. The literature retrieved for this prediction is generic hypoxia biology (brain aging, cancer, altitude, multiple sclerosis). None of it involves nisoldipine or the treatment of pulmonary hypertension.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The search returned 18 articles for this prediction. All are narrative reviews or basic research on hypoxia, and none involves nisoldipine. Most relevant entries are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Describes the four basic mechanisms of hypoxemia, including low ambient oxygen, hypoventilation, V/Q mismatch and shunt. Background only, with no drug data. |
| [9446167](https://pubmed.ncbi.nlm.nih.gov/9446167/) | 1997 | Review | Revue Medicale de Liege | Hepatopulmonary syndrome. No abstract available and no link to nisoldipine. |
| [2164797](https://pubmed.ncbi.nlm.nih.gov/2164797/) | 1990 | Review | Annales Francaises d'Anesthesie et de Reanimation | Post-anoxia encephalopathies. States that calcium channel blockers cannot yet be recommended for hypoxic brain injury. |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia and brain aging: neurodegeneration versus neuroprotection. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical evidence and molecular mechanisms of hypoxia-induced cognitive impairment. |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Cellular responses to hypoxia in vascular disease, inflammation and cancer. |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Hypoxia and innate immunity, with a focus on HIF signalling. |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Role of hypoxia in multiple sclerosis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020356 | Sular (Covis Pharma US, Inc) | Tablet, film coated, extended release (oral) | Indication text not included in the record |

The same NDA appears three times in the records, likely as separate strengths or product entries.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no trials, and the retrieved literature is unrelated to nisoldipine. Calcium channel blockers may also worsen oxygenation in Group 3 pulmonary hypertension, so the mechanism may work against the indication.

The other predictions from the same model are weaker or equally unsupported:
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.77%, L5, Hold): same graph neighbourhood, no trials or literature.
- **Malignant renovascular hypertension** (99.75%, L4, Research Question): only one indirect 1987 review on calcium antagonism, and the acute setting needs titratable intravenous drugs.
- **Malignant hypertensive renal disease** (99.75%, L5, Hold): class-level inference only.
- **Braddock syndrome** (99.68%, L5, Hold): likely a graph artifact via pulmonary hypertension nodes.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Targeted literature search on nisoldipine or dihydropyridine calcium channel blockers in pulmonary hypertension, including hemodynamic and gas-exchange effects
- Review of the remaining unretrieved articles from the original literature set
- Consider prioritizing the hypertension-related predictions (malignant renovascular hypertension and malignant hypertensive renal disease), where the mechanism is more coherent with the approved use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

