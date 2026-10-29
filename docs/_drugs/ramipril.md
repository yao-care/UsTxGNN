---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 1107
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "RAMIPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
description: "Ramipril: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Not recorded in the local data"
---

# Ramipril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ramipril: Pulmonary hypertension owing to lung disease and/or hypoxia
{: .text-alpha }

## One-Sentence Summary

Ramipril is an ACE inhibitor originally used for hypertension and for reducing stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but the evidence is thin: **0 clinical trials** and only **1 directly relevant preclinical (rat) study** are currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of NDAs | 6 licences in total (1 NDA, 5 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, ramipril is an ACE inhibitor: it reduces the formation of angiotensin II, a peptide that causes vasoconstriction and is implicated in vascular remodelling.

Chronic hypoxia drives constriction and remodelling of the pulmonary blood vessels, and angiotensin II is thought to contribute to this process. This is the mechanistic link between ramipril's original cardiovascular use and the predicted indication. A 1996 rat study (PMID 9200213) found that ramipril given during 3 weeks of chronic hypoxia lowered baseline pulmonary perfusion pressure, which is consistent with this idea.

The other retrieved papers concern cardiac or renal renin-angiotensin biology and are only indirectly relevant. No clinical trials exist, and ramipril is not an established therapy for pulmonary hypertension. This prediction should therefore be treated as a research hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Only the first paper below addresses ramipril in a hypoxic pulmonary setting. The others are indirect, preclinical or mechanistic, and several are off-topic.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (rat) | Physiological Research | Ramipril (10 mg/kg daily) during 3 weeks of chronic hypoxia attenuated the effects of hypoxia on pulmonary blood vessels and lowered baseline perfusion pressure |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | Preclinical (transgenic rat) | Am J Physiol Regul Integr Comp Physiol | Cardiac muscle in rats with an activated renin-angiotensin system was less susceptible to hypoxia-reoxygenation damage |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | Preclinical / human tissue | Eur Heart J | ACE2 expression increases after myocardial infarction in rats and in human failing hearts |
| [18464162](https://pubmed.ncbi.nlm.nih.gov/18464162/) | 2008 | Preclinical (rat) | Microcirculation | Ramipril or valsartan reduced peritubular capillary loss in the kidney |
| [19380417](https://pubmed.ncbi.nlm.nih.gov/19380417/) | 2009 | Preclinical (animal) | Cardiovasc Res | ACE inhibition increased endothelial progenitor cells and new vessel formation under cardiac pressure overload |
| [24907870](https://pubmed.ncbi.nlm.nih.gov/24907870/) | 2014 | Preclinical (rat) | Basic Res Cardiol | Soluble guanylyl cyclase activation protected the heart after myocardial infarction beyond ACE inhibition |
| [32822951](https://pubmed.ncbi.nlm.nih.gov/32822951/) | 2020 | Preclinical (rat) | World Neurosurgery | Ramipril compared with bevacizumab for radiation-induced brain necrosis |
| [1650863](https://pubmed.ncbi.nlm.nih.gov/1650863/) | 1991 | Mechanistic review | Klin Wochenschr | Radical-scavenging properties of ACE inhibitors; ramipril lacks a sulfhydryl group and was inactive |

## US Market Information

All six licences are valid, and no approved-indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091604 | Ramipril (A-S Medication Solutions) | Capsule | Not available (valid) |
| ANDA078832 | Ramipril (Zydus Lifesciences) | Capsule | Not available (valid) |
| NDA219757 | Vostally (Metacel Pharmaceuticals) | Solution | Not available (valid) |
| ANDA078745 | Ramipril (Chartwell RX) | Capsule | Not available (valid) |
| ANDA077900 | Ramipril (Hikma Pharmaceuticals USA) | Capsule | Not available (valid) |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: the drug is linked to contraindication or caution signals in kidney disease, liver disease, renal artery obstruction, hypotensive disorders, hereditary angioedema, neutropenia and agranulocytosis, systemic lupus erythematosus, scleroderma and systemic sclerosis, and other connective tissue disorders. Package-insert confirmation is needed.
- **Drug Interactions**: 100 interactions were found in total. The two classified as Major are **potassium citrate** and **potassium bicarbonate**, because of the risk of raised potassium. Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, glimepiride, chlorpropamide, alogliptin, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin), aspirin, morphine, bupropion, dronabinol, and bowel-preparation agents.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9993), but the support is limited to a single 1996 animal study. There are no clinical trials, no ramipril-specific human evidence in pulmonary hypertension, and the drug is marketed with 6 valid licences. Ramipril is also not an established therapy in this disease.

**To proceed, the following is needed:**
- Mechanism-of-action data and package-insert warnings and contraindications (both currently missing)
- Confirmation of the original approved indications, since US licence records contain no indication text
- Replication of the preclinical hypoxic pulmonary hypertension findings in modern animal models
- Review of the safety of ACE inhibition in patients with pulmonary hypertension, including blood pressure and renal effects
- Assessment of whether a pulmonary vascular indication is feasible given the current market status (marketed, 6 valid licences)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

