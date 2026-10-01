---
layout: default
title: Collagenase Clostridium Histolyticum
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
---

# Collagenase Clostridium Histolyticum
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

# Collagenase Clostridium Histolyticum: From Localized Collagen-Degrading Therapy to Primary Release Disorder of Platelets

## One-Sentence Summary

Collagenase clostridium histolyticum is an enzyme that breaks down collagen and is marketed in the US as a locally applied product (Santyl ointment).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data (the Evidence Pack notes Dupuytren's contracture as a marketed indication under Xiaflex/Xiapex) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (listed as BLA101995) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, collagenase clostridium histolyticum is a bacterial collagenase preparation that cleaves type I and III collagen. This action is used in locally applied and locally injected products.

A primary release disorder of platelets is an intrinsic defect in platelet secretion. The link to this drug appears to be network proximity in the knowledge graph (platelet-collagen signaling), not a therapeutic mechanism. A locally administered collagen-degrading enzyme has no established role in correcting a platelet secretion defect.

The high score should therefore be read as a likely knowledge-graph artifact, not a credible repurposing signal. Degrading collagen could also, in theory, work against hemostasis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA101995 | COLLAGENASE SANTYL (Smith & Nephew, Inc.) | Ointment | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information.

The prediction rationale also notes that the product's labeling contains bleeding-related warnings. Use in a bleeding or platelet disorder would therefore raise a safety concern. This is not confirmed by the safety data in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or preclinical support and no plausible mechanism, and it is probably a knowledge-graph artifact. There is also a theoretical bleeding-related safety concern in this patient population.

Two other predictions in the same list are worth noting:
- **Ledderhose disease (plantar fibromatosis)** is the only genuine repurposing candidate, at evidence level L4. It is mechanistically plausible because it is biologically close to Dupuytren's disease, but the evidence is limited to three case reports.
- **Palmar fibromatosis (Dupuytren's contracture)** has the strongest evidence (L1, including Phase 3 trials and a 2024 randomized comparison with fasciectomy). It appears to be an already-approved indication, so it is not a true repurposing finding. The empty original-indication field appears to be a data gap.

**To proceed, the following is needed:**
- The US package insert warnings and contraindications
- Detailed mechanism of action data (MOA)
- A corrected original-indication record for this drug
- For Ledderhose disease, a prospective study or controlled trial of collagenase
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

