---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 1092
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "PROPRANOLOL"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
description: "Propranolol: predicted new indication Distal myopathy, Tateyama type (evidence level L5). Approved use: Not recorded in the local data"
---

# Propranolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Propranolol: Distal myopathy, Tateyama type
{: .text-alpha }

## One-Sentence Summary

Propranolol is a non-selective beta-adrenergic blocker, originally used for hypertension, arrhythmias such as atrial fibrillation, hypertrophic cardiomyopathy, and infantile hemangioma.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, but **0 clinical trials** and **0 publications** currently support this prediction.
This is a model-only prediction with no supporting evidence in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 0.9940 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of FDA Applications | 8 (1 NDA and 7 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, propranolol is a non-selective beta-blocker that reduces heart rate and myocardial contractility. Its efficacy is established in cardiovascular conditions such as hypertension and hypertrophic cardiomyopathy.

The data compiled for this report do not support a mechanistic link between beta-blockade and the pathophysiology of this rare distal myopathy. The high TxGNN score (0.9940) is a computational prediction only, and the relationship to the original indications remains unassessed.

Other predictions in the same analysis show the same pattern:

- **Congenital myopathy with excess of thin filaments** (score 0.9930): prediction only, no trials or literature, Hold.
- Hold.
- **Chondroma** (0.9914): no mechanistic link; any anti-angiogenic rationale is speculative. Hold.
- **Cirrhotic cardiomyopathy** (0.9912): three publications, with mixed findings (see below). Research question, L4.
- **Cardiomyopathy** (0.9912): many publications, mostly on hypertrophic cardiomyopathy, which is already an approved use. Research question, L3.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for distal myopathy, Tateyama type.

For context, literature was found for two lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Clinical study (design unconfirmed) | Frontiers in Pharmacology | Cirrhotic cardiomyopathy: propranolol may correct prolonged QT intervals in cirrhosis |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Clinical/observational (unconfirmed) | PLoS One | Cirrhotic cardiomyopathy: blunted cardiovascular effects of beta-blockers, related to severity of cirrhosis |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Clinical/observational (unconfirmed) | Journal of Hepatology | Cirrhotic cardiomyopathy: non-selective beta-blockers impaired circulatory and renal function in refractory ascites |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical physiological study | European Heart Journal | Cardiomyopathy: effects of propranolol and verapamil on diastolic stiffness in hypertrophic cardiomyopathy |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Clinical hemodynamic study | British Heart Journal | Cardiomyopathy: nifedipine plus propranolol appeared superior to nifedipine alone in hypertrophic obstructive cardiomyopathy |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Clinical study | American Journal of Cardiology | Cardiomyopathy: propranolol and arrhythmia in hypertrophic cardiomyopathy |

## US Market Information

The drug is marketed, with 8 valid licenses. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018553 | Propranolol Hydrochloride (ANI Pharmaceuticals) | Capsule, extended release | Not available |
| ANDA078703 | Propranolol hydrochloride (AvKARE) | Capsule, extended release | Not available |
| ANDA078494 | Propranolol Hydrochloride (Proficient Rx) | Capsule, extended release | Not available |
| ANDA070322 | Propranolol Hydrochloride (Amici Pharmaceuticals) | Tablet | Not available |
| ANDA071972 | Propranolol Hydrochloride (Amneal Pharmaceuticals NY) | Tablet | Not available |

Three more cancelled licenses exist: ANDA070979 (solution), ANDA070221 (tablet), and ANDA078955 (tablet).

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The knowledge graph lists many disease-level contraindications. The most relevant to a muscle-disease prediction are myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, and myasthenia gravis. Others include:
  - Respiratory: bronchitis.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, gout, hypercalcemia, hyperparathyroidism, potassium deficiency.
  - Organ disease: liver disease, hepatic coma and encephalopathy, kidney disease, anuria, pancreatitis, gallbladder disease.
  - Autoimmune: systemic lupus erythematosus.
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder.

  The listing of myopathy and skeletal muscle disease as contraindications is a direct concern for the predicted indication.
- **Drug Interactions**: 100 interactions were identified; the 20 shown in the data include:
  - **Major**: epinephrine.
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, lorcaserin, canagliflozin, chlorpropamide, cimetidine, and calcium salts (calcium phosphate, calcium acetate).
  - **Minor**: ascorbic acid, acetylsalicylic acid, magnesium oxide.

Label warnings and contraindications were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for distal myopathy, Tateyama type rests only on a TxGNN model (deep learning) score of 0.9940, with no clinical trials, no literature, and no mechanistic rationale. In addition, the knowledge graph lists myopathy and skeletal muscle disease as contraindications for propranolol, and the drug is marketed with 8 valid licenses.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between beta-blockade and this myopathy
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- A literature search for case reports, preclinical models, or any beta-blocker use in distal myopathies
- A review of the contraindication signal for muscle disease
- If a cardiovascular-adjacent direction is of interest, cirrhotic cardiomyopathy is a better-supported research question, but the safety concerns in advanced cirrhosis must be addressed first. Cardiomyopathy is largely an existing on-label use (hypertrophic cardiomyopathy), so it is not a true repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

