---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan Cilexetil is an angiotensin II type 1 receptor (AT1R) antagonist (ARB class) widely used in clinical practice for hypertension and heart failure, though no Taiwan marketing authorization is currently on record.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** with a prediction score of 99.68%.
However, **0 registered clinical trials** and **0 direct publications** exist for this specific combination — the evidence basis rests on mechanistic rationale and indirect class-level data from ARBs in chronic kidney disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / Heart failure (ARB class; no Taiwan license data available) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Candesartan Cilexetil is a prodrug that is hydrolyzed upon oral absorption to its active form, candesartan — a selective and competitive blocker of the angiotensin II type 1 receptor (AT1R). By blocking AT1R, the drug suppresses the downstream effects of angiotensin II: vasoconstriction, aldosterone secretion, and — critically — efferent arteriolar constriction in the glomerulus. This last effect reduces intraglomerular hydraulic pressure and proteinuria, forming the basis of ARB-class nephroprotection.

Malignant hypertensive renal disease (MHRD) is a severe, rapidly progressive form of hypertensive nephropathy defined by fibrinoid necrosis of small renal vessels, thrombotic microangiopathy, and acute-on-chronic kidney injury. The central driver is RAS overactivation: markedly elevated angiotensin II levels cause intense renal arteriolar vasoconstriction, ischemic glomerular injury, and accelerated renal fibrosis. AT1R blockade by candesartan directly interrupts this cascade — reducing intraglomerular pressure, proteinuria, and inflammatory/fibrotic remodeling — making the mechanistic link to this prediction biologically coherent.

ARBs as a class carry strong indirect evidence for nephroprotection in CKD with hypertension (e.g., RENAAL and IDNT trials for losartan and irbesartan in diabetic nephropathy). MHRD represents an acute, severe end of the same pathophysiological continuum. The TxGNN knowledge graph prediction appropriately extrapolates this class benefit to the malignant hypertension context. One clinically critical caveat, however, is that initiating ARBs during the acute phase of MHRD may precipitate acute kidney injury in patients with severe bilateral renal artery vasoconstriction — a risk that must be factored into any clinical protocol.

---

## Clinical Trial Evidence

Currently no clinical trials specifically studying Candesartan Cilexetil in malignant hypertensive renal disease are registered (ClinicalTrials.gov and ICTRP searched on 2026-04-21, result count: 0).

---

## Literature Evidence

Currently no directly relevant literature is available for Candesartan Cilexetil in malignant hypertensive renal disease (PubMed searched on 2026-04-21, result count: 0).

---

## Taiwan Market Information

Candesartan Cilexetil currently has no marketing authorization in Taiwan (市場狀態：未上市). No license records are available for this drug from Taiwan FDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Package insert warnings, contraindications, and drug interaction data were not retrievable in the current Evidence Pack. Before clinical use, the following should be confirmed from the official prescribing information:
> - Contraindication in bilateral renal artery stenosis or solitary kidney with stenosis (known class risk for ARBs)
> - Hyperkalemia risk, especially with concurrent K⁺-sparing diuretics or renal impairment
> - Acute kidney injury risk upon initiation in volume-depleted patients

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The AT1R antagonism mechanism of Candesartan Cilexetil provides a strong theoretical basis for nephroprotection in malignant hypertensive renal disease, with robust class-level indirect evidence from ARBs in CKD; however, no direct clinical trial or observational data exists for this specific acute/malignant indication, and the initiation risk for acute kidney injury warrants careful patient selection and monitoring protocols before advancing.

**To proceed, the following is needed:**
- Obtain and review Taiwan TFDA (or originating country) package insert for official warnings and contraindications
- Retrieve drug-drug interaction profile (DrugBank API or prescribing information)
- Conduct a focused literature review on ARBs (as a class) in malignant hypertension and hypertensive emergency with acute renal involvement
- Define the treatment window (acute phase vs. stabilization phase) and eligibility criteria to minimize AKI risk
- Establish a safety monitoring plan: serum creatinine, eGFR, potassium, and blood pressure within 1–2 weeks of initiation
- Consider a prospective observational registry or pilot study before formal RCT design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

