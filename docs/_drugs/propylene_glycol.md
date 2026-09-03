---
layout: default
title: Propylene Glycol
parent: 僅模型預測 (L5)
nav_order: 1093
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Propylene Glycol: From Pharmaceutical Excipient to Bronchitis (Prediction Under Review)

## One-Sentence Summary

> Propylene glycol (PG) is not marketed in Taiwan as a standalone therapeutic product and has no recorded original indication — it is conventionally used as a pharmaceutical excipient/solvent in other formulations.
> The TxGNN model's top-ranked prediction is **Bronchitis**, but the supporting clinical trials involve a different active drug (inhaled cyclosporine) with PG only as a solvent, and the literature signal actually points toward airway irritation risk rather than therapeutic benefit.
> Evidence for this specific prediction is therefore weak and partly contradictory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record; PG is conventionally used as a pharmaceutical excipient/solvent, not marketed as a standalone active drug in Taiwan |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for propylene glycol is not available. Based on known information, PG is not developed as a standalone therapeutic agent — it functions almost exclusively as an excipient/solvent within other drug formulations (e.g., inhalation solutions, ophthalmic preparations, oral/topical vehicles). It has no established original indication or proven clinical efficacy of its own.

The clinical trials retrieved for the "bronchitis" prediction (all Grade C relevance) are actually studies of **Cyclosporine Inhalation Solution** for bronchiolitis obliterans syndrome after lung/stem-cell transplant — PG appears only as a formulation solvent, not as the tested active ingredient. This means the trial evidence does not directly demonstrate any therapeutic effect of PG itself on bronchitis.

More notably, the associated literature evidence trends in the opposite direction: reviews on e-cigarette ("vaping") liquids — which commonly contain propylene glycol as a base — discuss its potential association with airway irritation, chronic bronchitis, and COPD-like pathology, rather than any protective or therapeutic role. Taken together, the mechanistic rationale for PG as a treatment for bronchitis is not well supported and may even represent a safety signal rather than an efficacy signal.

For context, among PG's other TxGNN-predicted indications, **diabetic retinopathy** (rank 3) reached a higher evidence stage (L3 / S1, "Research Question") based on formulation-related ophthalmic literature, though it still lacks direct efficacy data for PG itself. This suggests any further exploration of PG repurposing may be better directed there than toward bronchitis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Tested Cyclosporine Inhalation Solution (CIS) for preventing bronchiolitis obliterans syndrome post-lung transplant; PG is a formulation solvent only, not the tested drug |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access CIS study in lung/stem-cell transplant recipients with bronchiolitis obliterans; PG not the active agent |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Long-term follow-up of inhaled cyclosporine for chronic rejection prevention; trial terminated, PG not the active agent |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | CIS treatment trial for bronchiolitis obliterans syndrome in transplant recipients; PG present only as excipient |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Discusses whether chronic e-cigarette use (liquids commonly containing PG) may cause chronic bronchitis and COPD-like lung disease |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | Reviews e-cigarette constituents (including PG-based e-liquids) and potential links to asthma/airway pathology |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (mouse model) | Respiratory Research | Studies quercetin (not PG) in an elastase/LPS mouse model of chronic bronchitis/COPD; PG not the study agent |

---

## US Market Information

Propylene glycol has no marketing authorization records in the current dataset (0 licenses; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (bronchitis) has a high model score but is not supported by genuine PG-specific clinical evidence — the retrieved trials tested a different active drug (inhaled cyclosporine) with PG only as a solvent, and the associated literature raises a potential airway-irritation safety concern rather than a therapeutic signal. This does not meet the bar to advance beyond model prediction (S0).

**To proceed, the following is needed:**
- TFDA/regulatory label data on warnings and contraindications for PG (currently blocking, DG001)
- Confirmed mechanism of action data from DrugBank or other authoritative source (DG002)
- If pursued, a re-scoped evidence search specifically distinguishing PG-as-active-agent studies from PG-as-excipient studies
- Consider evaluating the diabetic retinopathy prediction (L3/S1) instead, given its comparatively stronger (though still indirect) evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

