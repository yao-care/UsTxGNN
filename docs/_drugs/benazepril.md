---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 5
---

# Benazepril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

The txgnn-pipeline skill confirms this is standard TxGNN report generation work. Proceeding with the evaluation report now.

---

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE (angiotensin-converting enzyme) inhibitor, a well-established class of antihypertensive drugs that suppress the renin-angiotensin-aldosterone system (RAAS) to lower blood pressure.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, a severe, end-organ-threatening form of secondary hypertension driven by renal artery stenosis and RAAS hyperactivation.
Currently, **no dedicated clinical trials** or **directly supporting publications** have been identified for this specific repurposing direction; evidence rests on mechanistic reasoning alone (L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory data on file (not marketed in Taiwan) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 (Mechanistic rationale only) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, benazepril is an ACE inhibitor that blocks the conversion of angiotensin I to angiotensin II, thereby suppressing RAAS-mediated vasoconstriction and aldosterone secretion. Its efficacy in essential hypertension has been well established internationally, and it may mechanistically be applicable to malignant renovascular hypertension.

The rationale is particularly compelling because malignant renovascular hypertension is fundamentally a disease of RAAS overactivation. Renal artery stenosis reduces perfusion pressure to the kidney, triggering hypersecretion of renin from the juxtaglomerular apparatus. This drives an angiotensin II surge that causes severe, treatment-resistant hypertension with rapid end-organ damage (hypertensive retinopathy, encephalopathy, and renal failure). An ACE inhibitor directly intercepts this pathological cascade at its enzymatic core, making the mechanistic alignment between drug and disease exceptionally strong.

There is, however, a clinically critical counterpoint: in **bilateral** renal artery stenosis (or stenosis of a solitary functioning kidney), ACE inhibitors are a well-documented contraindication. By dilating the efferent arteriole, ACE inhibitors in this anatomical setting collapse glomerular filtration pressure and can precipitate acute renal failure. Any clinical application of benazepril in renovascular hypertension therefore demands rigorous pre-treatment imaging (renal angiography or duplex ultrasound) to confirm unilateral disease. The mechanistic link is scientifically sound, but patient stratification is non-negotiable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benazepril in Malignant Renovascular Hypertension.

---

## Literature Evidence

Currently no related literature available for Benazepril in Malignant Renovascular Hypertension.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical note for this indication:** ACE inhibitors are contraindicated in bilateral renal artery stenosis — a common anatomical variant in renovascular hypertension. Prescribing benazepril without prior imaging confirmation of unilateral disease carries a risk of acute renal failure. This represents a blocking safety concern that must be resolved before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for benazepril in malignant renovascular hypertension is internally consistent and biologically plausible, but there is currently zero clinical or published evidence specifically supporting this repurposing direction, comprehensive safety data from Taiwan regulatory sources is entirely unavailable, and a known class-level contraindication (bilateral renal artery stenosis) demands a mandatory safety stratification step before any clinical application.

**To proceed, the following is needed:**

- **Retrieve safety data**: Download and parse the official Taiwan TFDA package insert PDF to fill the blocking safety data gap (DG001)
- **Retrieve full MOA**: Query DrugBank API for detailed pharmacology of DB00542 (DG002)
- **Targeted literature review**: Broaden the PubMed query to cover all ACE inhibitors (not only benazepril) in renovascular hypertension to establish class-level evidence
- **Safety stratification protocol**: Define imaging criteria (renal duplex ultrasound / MRA / CTA) to distinguish unilateral from bilateral disease prior to enrollment
- **Exploratory study design**: Consider a pilot study in selected patients with confirmed unilateral renal artery stenosis, monitoring renal function, blood pressure response, and serum creatinine closely
- **Regulatory pathway assessment**: Evaluate whether Taiwan or US regulatory precedent exists for ACE inhibitors in renovascular hypertension before initiating a formal repurposing program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

