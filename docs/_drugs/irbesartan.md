---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 809
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB) originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **0 clinical trials** and **0 publications** currently support this specific prediction.
The score most likely reflects the drug's closeness to its already approved hypertension use rather than independent evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (the U.S. license records compiled for this report contain no indication text, so these come from the knowledge-graph indication edges) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 9 (1 NDA and 8 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, irbesartan is an AT1 receptor blocker. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to renovascular hypertension, which is driven largely by activation of the renin-angiotensin system.

Malignant renovascular hypertension is largely a severe subtype of the already labeled hypertension use. The very high TxGNN score (0.993) most likely reflects knowledge-graph proximity to existing indications rather than new evidence.

There are important caveats:
- Malignant hypertension is a hypertensive emergency, usually managed with rapid-acting agents rather than an oral ARB.
- ARBs carry a risk of acute kidney injury in patients with bilateral renal artery stenosis, a common cause of renovascular hypertension.

### Other predicted indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 99.31% | L5 | No trials or literature. Rapid-acting agents are typically used. Hold. |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.25% | L4 | Indirect preclinical evidence only (cardiac and high-altitude animal models). Research question. |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.25% | L5 | Heterogeneous category with no supporting evidence. Hold. |

The literature evidence for the top-ranked prediction is empty, so the table below covers only the third-ranked indication (pulmonary hypertension owing to lung disease and/or hypoxia), the only one with retrieved publications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked prediction. For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), the relevant items are all preclinical or review articles:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Pleiotropic effects of AT1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclinical | PLoS One | Irbesartan protects cardiomyocytes under hypoxic stress in vitro |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclinical | Sleep & Breathing | Irbesartan attenuates sleep apnea-induced cardiac apoptosis in an animal model |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical | Am J Physiol Heart Circ Physiol | Irbesartan inhibits coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclinical | Biomed Pharmacother | Irbesartan ameliorates chronic mountain sickness in rats via cholesterol metabolism |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Preclinical | Eur Rev Med Pharmacol Sci | Irbesartan improves oxidative stress in high-altitude pulmonary hypertension in rats via intestinal flora |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preclinical | Renal Failure | Irbesartan ameliorates cyclosporine nephrotoxicity (peripheral relevance) |

These findings are indirect: they come mostly from cardiac or high-altitude animal models, not pulmonary arterial pressure outcomes in patients. Several other retrieved items (herbal extracts in diabetic kidney disease, a roxadustat overdose case report) are not relevant to irbesartan and are omitted.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020757 | Avapro (Sanofi-Aventis U.S. LLC) | Tablet, film coated | Not available (cancelled) |
| ANDA202910 | Irbesartan (AvPAK) | Tablet | Not available (cancelled) |
| ANDA203071 | Irbesartan (A-S Medication Solutions) | Tablet | Not available (cancelled) |
| ANDA091236 | Irbesartan (Alembic Pharmaceuticals Inc.) | Tablet | Not available (cancelled) |
| ANDA202254 | Irbesartan (Macleods Pharmaceuticals Limited) | Tablet | Not available (cancelled) |

Nine licenses are on record in total (1 NDA, 8 ANDAs), and all are cancelled. Only the first five are listed above.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The 20 retrieved include two **Major** interactions, both with potassium supplements (potassium citrate and potassium bicarbonate), which raise the risk of hyperkalaemia. Most others are Moderate, including:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - Insulins (aspart, degludec)
  - Acetylsalicylic acid, morphine, bupropion, aprepitant, dronabinol
  - Bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate)
- **Knowledge-graph contraindication signals** (not label text) include:
  - Angioedema (including RAAS-blocker-induced and hereditary forms)
  - Anuria and renal artery obstruction
  - Hypotensive disorder
  - Diabetic ketoacidosis
  - Hepatic coma and hepatic encephalopathy
  - Gout and hypercalcaemia
  - Pancreatitis and systemic lupus erythematosus
  - Myopathy and rhabdomyolysis

The renal artery obstruction signal is directly relevant to the predicted renovascular indication. Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or literature for malignant renovascular hypertension. The indication largely overlaps the existing hypertension use. Malignant hypertension is an emergency typically managed with rapid-acting agents, and ARBs carry kidney risks in renal artery stenosis. The pulmonary hypertension prediction has only indirect preclinical support and is best treated as a research question.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clinical evidence in renovascular hypertension, with specific attention to renal safety in bilateral renal artery stenosis
- Confirmation of the current U.S. regulatory status, since all licenses are recorded as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

