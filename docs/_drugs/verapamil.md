---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 1287
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "VERAPAMIL"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Verapamil: Obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Verapamil is an L-type calcium channel blocker originally used for hypertension, atrial fibrillation, angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete bundle branch block** (the top-ranked prediction), but **no clinical trials and no publications** currently support this direction.
This is a model-only prediction, and the plausible direction of effect is unfavourable.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 12) |
| Number of NDAs | 12 (2 NDAs and 10 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, verapamil blocks L-type calcium channels, which slows conduction through the atrioventricular (AV) node and relaxes vascular smooth muscle. This explains its established use in hypertension, angina and supraventricular and ventricular arrhythmias.

The predicted indication, obsolete bundle branch block, is a conduction defect in the His-Purkinje system. Because verapamil slows cardiac conduction, it could be harmful rather than helpful in this setting. The disease term is also flagged as obsolete. The very high score (0.9962) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The knowledge graph itself lists atrioventricular block and heart failure among the contraindicated conditions for verapamil.

### Other Predictions Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 0.9927 | L5 | Biologically plausible through vasodilation, but no trials or literature; typically managed with IV agents under specialist care |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 0.9926 | L5 | Verapamil is generally avoided in pulmonary hypertension because of its negative inotropic effects |
| 5 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9926 | L5 | Indirect preclinical support only; calcium channel blockers are not recommended in this group |
| 6 | Braddock syndrome | 0.9915 | L5 | No mechanistic rationale identified |
| 7 | Periodic paralysis with transient compartment-like syndrome | 0.9908 | L5 | Calcium channel biology is conceptually relevant, but the prediction is unsupported |

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication (or for any of the other six predicted indications).

## Literature Evidence

Currently no related literature available for the top-ranked indication.

For the other predictions, only two indications returned publications, and none provides therapeutic evidence in humans:

- **Malignant renovascular hypertension:** [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) (2012, Review) covers factors affecting the aldosterone/renin ratio, which is a diagnostic topic. [10224210](https://pubmed.ncbi.nlm.nih.gov/10224210/) (1999, Case report) describes renal myofibromatosis as a cause of infantile hypertension. Neither studies verapamil treatment.
- **Pulmonary hypertension owing to lung disease and/or hypoxia (rank 5):** 20 papers were retrieved, and most are off-topic. The most relevant are preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24977753](https://pubmed.ncbi.nlm.nih.gov/24977753/) | 2014 | Preclinical | J Trauma Acute Care Surg | Verapamil preserved cytoskeletal function in an in vitro intestinal model after hypoxia-reoxygenation |
| [21962069](https://pubmed.ncbi.nlm.nih.gov/21962069/) | 2011 | Preclinical | High Alt Med Biol | Calcium entry through L-type channels in sheep pulmonary arteries after long-term hypoxia |
| [9768801](https://pubmed.ncbi.nlm.nih.gov/9768801/) | 1998 | Preclinical | Anesth Analg | Ketamine-induced pulmonary vasodilation in rat lung is partly mediated by L-type calcium channels (verapamil used as a probe) |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathol Biol | Calcium antagonists for migraine prophylaxis; efficacy not firmly demonstrated (off-topic) |
| [9440591](https://pubmed.ncbi.nlm.nih.gov/9440591/) | 1998 | Review | Chest | Multifocal atrial tachycardia, typically seen in COPD patients (off-topic) |

## US Market Information

The drug is marketed in the US, with 12 valid licences. Approved-indication text is not available in the licence records. Five representative entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019614 | Verapamil Hydrochloride | Capsule, delayed release | Not available |
| NDA018925 | Verapamil HCl | Injection | Not available |
| ANDA075138 | Verapamil Hydrochloride | Capsule, extended release | Not available |
| ANDA078906 | Verapamil Hydrochloride | Tablet, film coated, extended release | Not available |
| ANDA213232 | Verapamil Hydrochloride | Injection, solution | Not available |

Available dosage forms span both oral (tablets, extended-release and delayed-release capsules) and injectable routes.

## Safety Considerations

- **Contraindicated conditions (knowledge graph, not label text):** The graph lists many conditions, including atrioventricular block, heart failure, hypotensive disorder, aortic stenosis, hypertrophic cardiomyopathy, ventricular tachycardia (certain forms), myasthenia gravis and neuromuscular junction disease, kidney disease, liver disease, angioedema (several forms), and neutropenia/agranulocytosis. The AV block and heart failure entries are directly relevant to the top-ranked prediction.
- **Drug Interactions:** 100 interactions were found in the DDInter database. Among those reviewed, the major one is **loperamide**. Moderate interactions include clarithromycin, cimetidine, aprepitant, bupropion, metformin, canagliflozin, acetylsalicylic acid, several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone) and several calcium salts. Morphine is a minor interaction.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for bundle branch block rests on a model score alone, with no clinical trials or literature, and verapamil's conduction-slowing effect suggests potential harm. The knowledge graph also lists AV block as a contraindication. None of the seven predicted indications has human therapeutic evidence.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- A review of whether the disease term is valid, since it is flagged as obsolete
- If an alternative is pursued, the more plausible candidates are the hypertension-related predictions (malignant hypertensive renal disease, malignant renovascular hypertension), which would need dedicated literature and clinical evidence
- Confirmation of the current US marketing status, since the drug is marketed with 12 valid licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

