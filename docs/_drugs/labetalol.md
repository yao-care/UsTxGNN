---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 827
evidence_level: L5
indication_count: 4
---

# Labetalol
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha-1 and beta blocker that is marketed in the US for blood pressure control. The TxGNN model predicts it may be useful for **malignant renovascular hypertension**. Support is weak: **0 registered clinical trials** and only **2 indirect case reports**, so this remains a research question rather than an established use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied data (labetalol is generally used as an antihypertensive) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 (model prediction plus indirect case reports only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, labetalol blocks both alpha-1 and beta receptors. This lowers vascular resistance and heart rate, and it is already used in hypertensive emergencies. That makes it plausible for severe or malignant hypertension.

The renovascular subtype is driven by the renin-angiotensin system, and labetalol supports it only indirectly. The pack contains no label text to confirm how the predicted indication overlaps with the current approved indication. The 99.08% score is a model prediction, not clinical evidence.

Renal function and bilateral renal artery stenosis would need careful checking before any use in this setting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | The Medical Journal of Australia | A young man with malignant hypertension from hallucinogen-induced vasculitis. Minoxidil and labetalol controlled his blood pressure initially, and prednisone resolved the arteritis. This is not a renovascular stenosis case. |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case report | BMC Nephrology | An 18-month-old child with hyponatremic hypertensive syndrome (renovascular hypertension with hyponatremia) presenting as malignant hypertension. The abstract does not describe labetalol treatment. |

Neither paper tests labetalol in renovascular disease.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA209603 | Labetalol Hydrochloride (Golden State Medical Supply) | Tablet, film coated | Not listed |
| ANDA211953 | Labetalol Hydrochloride (RemedyRepack) | Tablet, film coated | Not listed |
| ANDA209603 | Labetalol Hydrochloride (A-S Medication Solutions) | Tablet, film coated | Not listed |
| ANDA209603 | Labetalol Hydrochloride (Northwind Health Company) | Tablet, film coated | Not listed |
| ANDA209603 | Labetalol Hydrochloride (Major Pharmaceuticals) | Tablet, film coated | Not listed |

Both oral (tablet) and injectable (solution) forms are marketed in the US. The 20 authorizations are listed as ANDAs (generic approvals), not brand NDAs.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests almost entirely on a model score. There are no trials, and the two case reports are indirect and do not test labetalol in renovascular disease. The other predicted indications are weaker still: malignant hypertensive renal disease has no supporting studies at all. The two pulmonary hypertension predictions have no credible mechanistic link and raise a safety concern, because non-selective beta blockade can worsen bronchospasm in lung disease. The 20 papers retrieved for the first pulmonary hypertension prediction are generic hypoxia biology keyword matches.

**To proceed, the following is needed:**
- The FDA label text (approved indications, warnings, contraindications) to check overlap with the predicted use
- Mechanism of action data from DrugBank
- A targeted literature search for labetalol in renovascular and malignant hypertension, including any controlled studies
- A safety review for bilateral renal artery stenosis and impaired renal function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

