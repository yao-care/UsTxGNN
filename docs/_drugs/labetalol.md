---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 827
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "LABETALOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
description: "Labetalol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Labetalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Labetalol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Labetalol is a combined alpha-1/beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
but there are currently **0 clinical trials** and only **1 publication** (a case report that does not specifically evaluate labetalol for this indication), so the evidence is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | 9 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, labetalol blocks both alpha-1 and beta adrenergic receptors, lowering systemic vascular resistance and blood pressure. It is already used for severe hypertension and hypertensive emergencies.

Malignant renovascular hypertension is a severe form of hypertension caused by narrowing of the renal arteries. Blood-pressure lowering with labetalol is biologically plausible, so the prediction is essentially an extension of the existing hypertension indication rather than a distinct repurposing. The high TxGNN score probably reflects this closeness to the known indication.

There are important caveats. Renovascular hypertension is driven largely by activation of the renin-angiotensin system, which labetalol does not target directly. The only retrieved publication describes a young man with malignant hypertension caused by hallucinogen-induced vasculitis. Labetalol and minoxidil were used for initial blood-pressure control, but the report does not evaluate labetalol in renovascular disease.

Other predicted indications are weaker. Malignant hypertensive renal disease rests on the model prediction alone, with no trials or literature. Two pulmonary hypertension predictions have no established mechanistic basis, because labetalol does not act on the pulmonary vascular pathways involved. They appear to be driven by the shared word "hypertension", and beta-blockade could worsen bronchospasm or hypoxia in lung disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | The Medical Journal of Australia | Malignant hypertension in a 20-year-old man with hallucinogen-induced vasculitis. Prednisone resolved the arteritis. Labetalol and minoxidil helped with initial blood-pressure control. Not specific to labetalol in renovascular disease. |

---

## US Market Information

No approved indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA209603 | Labetalol Hydrochloride (Golden State Medical Supply) | Tablet, film coated | Not available |
| ANDA211953 | Labetalol Hydrochloride (RemedyRepack) | Tablet, film coated | Not available |
| ANDA075215 | Labetalol Hydrochloride (Bryant Ranch Prepack) | Tablet, film coated | Not available |
| ANDA076051 | Labetalol Hydrochloride (Baxter Healthcare) | Injection, solution | Not available |
| ANDA075303 | Labetalol Hydrochloride (Hikma) | Injection | Not available |

Four more authorizations (oral tablets and injections) are also cancelled.

---

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The knowledge graph links labetalol with contraindications in several conditions, including:
  - Liver disease, liver failure, hepatic encephalopathy and hepatic coma
  - Kidney disease and anuria
  - Atrioventricular block
  - Pulmonary emphysema and bronchial disease
  - Diabetes mellitus and diabetic ketoacidosis
  - Hypotensive disorder
  - Systemic lupus erythematosus
  - Gout, pancreatitis and gallbladder disease
  - Electrolyte and metabolic disorders (potassium deficiency, hypercalcemia, hyperparathyroidism)
  - Anxiety and dysthymic disorders
  - Intraoperative floppy iris syndrome

  These should be verified against the official label.

- **Drug Interactions**: 100 interactions were found. Examples:
  - **Major**: Epinephrine, Dolasetron
  - **Moderate**: Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Morphine, Atropine, Hyoscyamine, Methscopolamine, Dicyclomine, Cimetidine, Canagliflozin, Dapagliflozin, Chlorpropamide, Calcium acetate, Calcium phosphate
  - **Minor**: Acetylsalicylic acid, Magnesium oxide

- The official package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible mainly because it overlaps with labetalol's existing hypertension use. There are no clinical trials, and the single publication is an unrelated case report. The renin-angiotensin-driven pathophysiology also does not match labetalol's mechanism. The pulmonary hypertension predictions are not supported mechanistically. Package insert safety data is missing, which blocks safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data
- Clinical or observational data on labetalol in renovascular or malignant hypertension
- Clarification of whether this is a true new indication or part of the existing hypertension indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

