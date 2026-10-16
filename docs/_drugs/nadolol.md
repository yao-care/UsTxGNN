---
layout: default
title: Nadolol
parent: Model Prediction Only (L5)
nav_order: 950
evidence_level: L5
indication_count: 5
monitor_inn: "NADOLOL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Nadolol
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

# Nadolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nadolol is a non-selective beta-blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 (all cancelled; listed under ANDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nadolol is a non-selective beta-adrenergic blocker, its efficacy in hypertension is established, and mechanistically it may be applicable to hypertension-related end-organ disease. Beta-blockade also reduces renin release from the kidney, which is relevant when the renin-angiotensin system is activated.

Malignant hypertensive renal disease is a severe kidney complication of hypertension. The high TxGNN score most likely reflects how close this condition sits to the existing hypertension indication in the knowledge graph, rather than any independent evidence.

There is an important clinical caveat. In malignant hypertension, acute management typically relies on parenteral agents, and an oral beta-blocker would be adjunctive at most. The prediction is therefore plausible but unproven.

Other predictions from the same model (all L5, all Hold):

| Predicted Indication | TxGNN Score | Evidence Available | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 99.59% | None | Plausible link through renin suppression |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.53% | 12 publications, all indirect (mostly preclinical) | No human evidence; beta-blockade may worsen bronchospasm and right ventricular function |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.53% | None | Beta-blockers are used cautiously in pulmonary hypertension |
| Braddock syndrome | 99.43% | None | No mechanistic rationale; likely a knowledge-graph artifact |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), 12 publications were retrieved, but they are indirect and predominantly preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6488695](https://pubmed.ncbi.nlm.nih.gov/6488695/) | 1984 | Preclinical (dog) | Clin Physiol Biochem | Chronic propranolol lowered pulmonary artery pressure in conscious dogs; nadolol had a similar effect on total pulmonary resistance |
| [39252618](https://pubmed.ncbi.nlm.nih.gov/39252618/) | 2025 | Preclinical (rat) | CNS Neurol Disord Drug Targets | Nadolol reduced brain-cell ferroptosis in a stroke model via the HOIL-1/IRP2 pathway (not pulmonary hypertension) |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Preclinical (rat) | PLoS One | β2-adrenergic receptor-dependent attenuation of hypoxic pulmonary vasoconstriction in intermittent hypoxic rats |
| [2566504](https://pubmed.ncbi.nlm.nih.gov/2566504/) | 1989 | Preclinical | Eur J Pharmacol | Beta-blockers protected isolated guinea pig hearts from anoxia |
| [8729060](https://pubmed.ncbi.nlm.nih.gov/8729060/) | 1996 | Preclinical | J Mol Cell Cardiol | Nadolol was used in a study of hypoxia-induced action potential shortening in rabbit hearts |
| [24795691](https://pubmed.ncbi.nlm.nih.gov/24795691/) | 2014 | Preclinical (rat) | Front Neurol | β1-blockers lowered norepinephrine release via presynaptic β1-adrenoceptors |

The remaining retrieved papers cover myocardial ischemia and arrhythmia models and non-mammalian cardiovascular physiology, and do not address the predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212856 (cancelled) | Nadolol (VGYAAN Pharmaceuticals) | Tablet | Not available |
| ANDA210955 (cancelled) | Nadolol (Unichem Pharmaceuticals) | Tablet | Not available |
| ANDA203455 (cancelled) | Nadolol (BluePoint Laboratories) | Tablet | Not available |
| ANDA207761 (cancelled) | Nadolol (Zydus Lifesciences) | Tablet | Not available |
| ANDA201893 (cancelled) | Nadolol (BluePoint Laboratories) | Tablet | Not available |

A sixth license (ANDA208832, Amneal Pharmaceuticals NY LLC, tablet) is also cancelled. All six licenses are cancelled, and no valid license is currently on record.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from package insert text, and should be verified against the label):
- Cardiac and respiratory: atrioventricular block, pulmonary emphysema, bronchial disease
- Neuromuscular: myasthenia gravis (including adult-onset), neuromuscular junction disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, hypercalcemia, potassium deficiency, gout, hyperuricemia
- Kidney and liver: kidney disease, anuria, liver disease, hepatic coma and encephalopathy, pancreatitis, gallbladder disease
- Other: systemic lupus erythematosus, anxiety and neurotic disorders, dysthymic disorder, neonatal jaundice

Kidney disease and anuria appear in this list, which is directly relevant to a renal indication and needs careful review.

**Drug Interactions:** 100 interactions were identified. Examples from the first 20 listed:
- **Major:** Epinephrine
- **Moderate:** hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, atropine, hyoscyamine, methscopolamine, bupropion, morphine, canagliflozin, dapagliflozin, chlorpropamide, cimetidine, calcium acetate, calcium phosphate
- **Minor:** acetylsalicylic acid, clarithromycin, magnesium oxide

Package insert warnings were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but has no supporting trials or literature (L5). Acute management of malignant hypertension relies on other agents, and all US licenses for nadolol are currently cancelled. Package insert safety data are also missing, and the knowledge graph flags kidney disease as a contraindication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Clinical evidence (trials, cohort studies or systematic reviews) of oral beta-blockers in malignant hypertensive nephropathy
- Clarification of the US regulatory status, given that all licenses are cancelled
- Safety assessment for renal impairment and for the pulmonary hypertension predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

