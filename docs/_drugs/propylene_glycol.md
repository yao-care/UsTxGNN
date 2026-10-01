---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 1093
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Propylene Glycol: From Ocular Lubricant to Bronchitis

## One-Sentence Summary

Propylene glycol is a solvent and excipient. In the US records it appears as an ingredient in lubricant eye drops. The TxGNN model predicts it may be effective for **bronchitis**, but the four listed clinical trials are all unrelated (grade C) and the literature is indirect. Only model-level evidence supports the prediction (**Evidence Level L5**), and it may be a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the regulatory records. The products are lubricant eye drops. |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% (model rank 3314) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Propylene glycol is mainly used as a solvent, vehicle, and humectant rather than as a therapeutic agent. No pharmacological mechanism links it to bronchitis, so the high TxGNN score is most likely a knowledge-graph artifact.

The literature points the other way. Propylene glycol is a major e-cigarette liquid constituent, and reviews link e-cigarette aerosols to airway irritation and possible worsening of lung disease. This is a possible safety signal for airway use, not evidence of benefit.

The other top predictions are also ocular (diabetic retinopathy and several cataract types). They have no mechanistic rationale or supporting trials either. The one on-topic retinopathy paper studied propylene glycol mannate sulfate, a different compound, so it is probably a name-matching false positive.

## Clinical Trial Evidence

None of these trials tests propylene glycol as an active agent. All were graded C for relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Cyclosporine inhalation solution to prevent bronchiolitis obliterans syndrome after lung transplant. Propylene glycol is at most the vehicle. |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access study of cyclosporine inhalation solution in lung and stem cell transplant recipients. Propylene glycol is only a possible excipient. |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Open-label extension of inhaled cyclosporine for chronic lung rejection. It does not test propylene glycol. |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | Cyclosporine inhalation solution for bronchiolitis obliterans syndrome after transplant. Not relevant to propylene glycol in bronchitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews whether chronic e-cigarette use could cause lung disease, including COPD and chronic bronchitis. It raises a safety concern rather than showing benefit. |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette liquids and aerosols contain airway irritants linked to worse lung disease. Health effects in people with existing respiratory disease are poorly understood. |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal) | Respir Res | Quercetin reduced lung inflammation in a mouse COPD model. Only indirectly related to propylene glycol. |

## US Market Information

The regulatory records list 20 authorizations in total. Five are shown below. The approved-indication text is blank in the records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M018 | Equate Complete Relief Lubricant Eye Drops (Walmart) | Solution/drops | Not listed |
| M018 | Leader Restorative Formula Lubricant Eye Drops (Cardinal Health) | Solution/drops | Not listed |
| M018 | Splash Pure PF (Laboratorios Sophia) | Emulsion | Not listed |
| M018 | Rite Aid Lubricant Eye Drops Restorative Performance | Solution/drops | Not listed |
| M018 | Systane Pro PF (Alcon Laboratories) | Emulsion | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

The literature also raises a possible airway irritation signal from inhaled propylene glycol, based on e-cigarette research.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no mechanism and no relevant efficacy data for bronchitis. The available literature suggests a possible airway safety concern rather than a benefit.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Any direct evidence of propylene glycol efficacy in bronchitis, and an assessment of inhalation safety
- Confirmation of whether an airway-compatible route or formulation is feasible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

