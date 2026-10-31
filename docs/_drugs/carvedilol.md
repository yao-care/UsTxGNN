---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 502
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Carvedilol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Carvedilol
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

## Carvedilol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Carvedilol is a non-selective beta-blocker with alpha-1 blocking activity, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **0 clinical trials** and **0 publications** currently support this specific indication. This is a model prediction only, and it is closely tied to the drug's existing hypertension use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9955 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of FDA Applications | at least 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carvedilol is a non-selective beta-blocker with alpha-1 blockade. Its blood-pressure-lowering effect is established in hypertension, and mechanistically it may be applicable to hypertension-related kidney damage.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Here, the model may be picking up how close this disease sits to the original hypertension indication. Malignant hypertensive renal disease is essentially a severe complication of hypertension, so this is arguably an extension of the existing indication rather than true repurposing. No trials or literature were found for this specific indication.

Other predictions in the same list follow a similar pattern:
- **Malignant renovascular hypertension** (0.9955): a subtype of hypertension; beta-1 blockade may reduce renin release. No direct evidence.
- **Pulmonary hypertension, unclear multifactorial mechanism** (0.9954): beta-blockade is controversial in pulmonary arterial hypertension because of possible reduced cardiac output. No direct evidence.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (0.9954): only indirect preclinical data, for example carvedilol reversing hypoxia-induced hypertension in rats (PMID 26291659). Evidence level L4, labelled a research question.
- **Braddock syndrome** (0.9937): no clear mechanistic rationale can be established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (malignant hypertensive renal disease).

For reference, the closest evidence found for the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia) is mostly preclinical or indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Beta-blocker effects on lung function in heart failure; addresses airway safety rather than pulmonary hypertension efficacy |
| [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) | 2015 | Animal study | Eur J Pharmacol | Carvedilol reversed hypertension induced by chronic intermittent hypoxia in rats |
| [20508210](https://pubmed.ncbi.nlm.nih.gov/20508210/) | 2010 | Animal study | Am J Respir Crit Care Med | Adrenergic receptor blockade reversed right heart remodeling in pulmonary hypertensive rats |
| [16639551](https://pubmed.ncbi.nlm.nih.gov/16639551/) | 2006 | Animal study | Pflugers Arch | Carvedilol inhibited right ventricular hypertrophy induced by chronic hypobaric hypoxia |
| [24798657](https://pubmed.ncbi.nlm.nih.gov/24798657/) | 2014 | Crossover study (11 patients) | J Clin Hypertens | Nighttime carvedilol vs nifedipine on sleep blood pressure in hypertensive patients with sleep apnoea |
| [10862260](https://pubmed.ncbi.nlm.nih.gov/10862260/) | 2000 | Review | Presse Med | Beta-blocker intoxication; carvedilol listed among the more toxic agents (safety context) |

## US Market Information

All nine US authorizations are valid, and none has approved-indication text on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204717 | Carvedilol Phosphate (AvKARE) | Capsule, extended release | Not available |
| ANDA077614 | Carvedilol (A-S Medication Solutions) | Tablet, film coated | Not available |
| ANDA078384 | Carvedilol (Golden State Medical Supply) | Tablet, film coated | Not available |
| ANDA076373 | Carvedilol (Teva) | Tablet, film coated | Not available |
| ANDA078786 | Carvedilol (Method Pharmaceuticals) | Tablet, film coated | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

- **Contraindications suggested by the knowledge graph** (not label text): liver failure, bronchitis, asthma (including intrinsic and allergic), diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, peripheral vascular disease and arterial disease, intermittent claudication, atrioventricular block, pulmonary emphysema, bronchial disease, Prinzmetal angina, sick sinus syndrome, anaphylaxis, and intraoperative floppy iris syndrome.
- **Drug interactions** (100 recorded; main ones shown):
  - **Major:** epinephrine.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), hyoscyamine, atropine, bupropion, morphine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate).
  - **Minor:** acetylsalicylic acid, aluminum hydroxide, attapulgite.
- **Pulmonary hypertension and lung disease:** beta-blockade may reduce cardiac output and is a concern in airway disease, so tolerability needs clarification before any use in those populations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or literature for malignant hypertensive renal disease, and it largely overlaps with carvedilol's existing hypertension use. The drug is marketed with nine valid US licenses, but label safety data is missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data (for example from DrugBank)
- A literature and trial search specific to hypertensive kidney disease
- Clarification of whether this is a true new indication or a subtype of the existing hypertension indication
- For the pulmonary hypertension predictions, human safety and tolerability data on beta-blockade in lung disease
- Confirmation of current US marketing status for the product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

