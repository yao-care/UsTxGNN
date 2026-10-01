---
layout: default
title: Felodipine
parent: Model Prediction Only (L5)
nav_order: 696
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Felodipine: From Hypertension to Pulmonary Hypertension (Unclear Multifactorial Mechanism)

## One-Sentence Summary

Felodipine is a dihydropyridine calcium channel blocker, a vasodilating drug that is marketed in the US as generic tablets. The licence records supplied do not state its indication, so hypertension is assumed here from its drug class.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**, with a very high graph score.
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it remains a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (hypertension assumed from drug class) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed entries are ANDA generic authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, felodipine is a dihydropyridine L-type calcium channel blocker. It lowers vascular tone by relaxing arterial smooth muscle, and this mechanistically may be applicable to pulmonary hypertension.

Pulmonary vasodilation is therefore theoretically plausible. The high TxGNN score reflects graph proximity between the drug and the disease, not experimental or clinical confirmation. Calcium channel blockers are generally reserved for the small group of pulmonary arterial hypertension patients who respond to vasodilator testing. A general-purpose vasodilator such as felodipine is not an established option for a broad or poorly defined pulmonary hypertension group.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA210847 | Felopdipine (as listed; Westminster Pharmaceuticals) | Tablet, extended release | Not stated in record |
| ANDA204800 | Felodipine (Bryant Ranch Prepack) | Tablet, film coated | Not stated in record |
| ANDA210847 | Felodipine (Yiling Pharmaceutical) | Tablet, extended release | Not stated in record |
| ANDA202170 | Felodipine (Bryant Ranch Prepack) | Tablet, extended release | Not stated in record |

All listed products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data provided.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. No trials or drug-specific literature support it, and calcium channel blockers are only used in a narrow, vasoreactive subset of pulmonary hypertension. Systemic vasodilators can also worsen oxygenation in lung-disease-related forms.

**To proceed, the following is needed:**
- Felodipine-specific preclinical or clinical data in pulmonary hypertension, ideally a defined subgroup such as vasoreactive PAH
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Approved indication text for the licences, to confirm the original indication

**Other predicted indications for this drug:**
- **Prinzmetal angina** (rank 7, score 99.07%) has by far the strongest support. It has felodipine-specific studies, including a double-blind comparison with nifedipine and placebo in stable angina (PMID 7744087), a felodipine vs nifedipine comparison in Prinzmetal angina (PMID 1746458), and ergonovine-provocation studies (PMID 8013514). Its evidence level is L2, and its recommendation is Proceed with Guardrails. It is a better candidate to prioritize than the pulmonary hypertension prediction.
- **Chronic pulmonary heart disease** (rank 6) has indirect, dated hemodynamic studies only. It is a research question, not a candidate for development.
- The remaining predictions (ranks 2–5) have no meaningful drug-specific evidence and stay on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

