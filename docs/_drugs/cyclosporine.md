---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 7
---

# Cyclosporine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cyclosporine: From Organ Transplant Rejection to Chronic Granulomatous Disease

## One-Sentence Summary

Cyclosporine is a calcineurin inhibitor widely established as immunosuppressive therapy to prevent organ transplant rejection and graft-versus-host disease (GvHD) in allogeneic hematopoietic stem cell transplantation (allo-HSCT).
The TxGNN model predicts it may be effective for **Granulomatous Disease, Chronic, Autosomal Recessive (CGD)**,
with **1 clinical trial** and **1 publication** currently supporting this direction — primarily in the context of HSCT regimens that represent the only curative strategy for CGD, where Cyclosporine serves as standard GvHD prophylaxis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory data available in current dataset (established use: organ transplant rejection, GvHD prophylaxis) |
| Predicted New Indication | Granulomatous Disease, Chronic, Autosomal Recessive (CGD) |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L3 |
| US Market Status | Not found in current dataset (likely data collection gap) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on information embedded in the mechanistic rationale, Cyclosporine is a calcineurin inhibitor that blocks the NFAT (Nuclear Factor of Activated T-cells) signaling pathway, thereby suppressing T cell activation and IL-2 secretion. It is a standard component of immunosuppressive regimens following organ transplantation and allo-HSCT, where it serves to prevent GvHD.

Chronic Granulomatous Disease (CGD) is a rare primary immunodeficiency caused by mutations in components of the NADPH oxidase complex (most commonly the *CYBB* gene encoding gp91phox). The functional consequence is the inability of phagocytes to generate reactive oxygen species, rendering patients susceptible to life-threatening infections with catalase-positive bacteria and fungi. The only curative treatment is allo-HSCT — and herein lies the connection to Cyclosporine.

The mechanistic link is **indirect**: Cyclosporine does not correct the underlying NADPH oxidase defect in CGD, nor does it enhance phagocyte killing function. Rather, it enables successful HSCT by suppressing donor T cells and preventing GvHD, thereby allowing engraftment of healthy donor hematopoietic stem cells that reconstitute a functional immune system. The TxGNN prediction almost certainly reflects the strong co-occurrence of Cyclosporine and CGD within HSCT-related nodes in the knowledge graph, rather than a novel, direct therapeutic mechanism for the disease itself. This distinction is critical to interpreting the prediction's clinical relevance.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Evaluated abatacept (CTLA4-Ig) combined with **Cyclosporine + mycophenolate mofetil** as GvHD prophylaxis in children undergoing unrelated donor HSCT for serious non-malignant diseases (including CGD). Cyclosporine functions as background GvHD prophylaxis; the investigational agent is abatacept. The trial confirms CGD is treated via HSCT but does not directly assess Cyclosporine's independent efficacy in CGD. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohort | J Allergy Clin Immunol | Retrospective cohort demonstrating excellent survival after matched related or unrelated donor HSCT for CGD. Validates allo-HSCT (employing standard Cyclosporine-containing conditioning regimens) as a curative strategy for CGD in both pediatric and adult patients. Cyclosporine is part of the GvHD prophylaxis protocol, not the subject of independent evaluation. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic connection between Cyclosporine and CGD is indirect — Cyclosporine functions as GvHD prophylaxis within the HSCT procedure that cures CGD, rather than as a direct therapeutic agent targeting the NADPH oxidase deficiency. With L3 evidence comprising a single cohort study confirming HSCT efficacy and one Phase 1 trial where Cyclosporine is a background medication rather than the investigational drug, there is insufficient evidence to advance this as a novel repurposing candidate distinct from Cyclosporine's already-established role in transplant medicine.

**To proceed, the following is needed:**
- **Research question clarification**: Define whether the goal is (a) optimizing Cyclosporine-based GvHD prophylaxis protocols specifically within CGD HSCT, or (b) exploring any direct immunomodulatory role of Cyclosporine in CGD pathophysiology independent of HSCT
- **Mechanism of action data**: Retrieve full MOA entry from DrugBank (DB00091) to formally document calcineurin inhibition pathway
- **Regulatory data correction**: Verify US FDA approval status — current dataset shows 0 licenses, which is inconsistent with Cyclosporine's well-established global clinical use (multiple approved formulations known to exist); re-query pipeline required
- **Safety data**: Retrieve package insert warnings and contraindications from source to complete safety assessment before any S1 evaluation can proceed
- **Dedicated clinical evidence**: A trial prospectively evaluating Cyclosporine-specific dosing, timing, and outcomes in CGD HSCT would be needed to distinguish Cyclosporine's contribution from the overall transplant procedure effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

