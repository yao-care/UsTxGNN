---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 923
evidence_level: L5
indication_count: 10
---

# Mexiletine
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

# Mexiletine: From Ventricular Arrhythmia to Hypertrichosis

## One-Sentence Summary

Mexiletine is an oral class IB sodium channel blocker, used as an antiarrhythmic drug for ventricular arrhythmias. The label data in this pack does not state an indication, so this original use comes from the drug class and the supporting literature.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a graph-based signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular arrhythmia (not stated in the license text provided) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed authorizations are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Mexiletine is known to be a class IB voltage-gated sodium channel blocker, and its efficacy in ventricular arrhythmias is established.

No plausible mechanistic link to hypertrichosis has been identified. Hypertrichosis is a hair growth disorder, and sodium channel blockade has no known role in it. The very high TxGNN score (0.998) most likely reflects proximity in the knowledge graph. The same pattern appears in other hair-related predictions for this drug, such as Ambras-type hypertrichosis universalis congenita and isolated genetic hair shaft abnormality.

Treat this score as a hypothesis-generating signal only. Without trials, literature, or a mechanistic rationale, it does not support further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer | Approved Indication |
|---------|------|------|------|-----------|
| ANDA214089 | Mexiletine Hydrochloride | Capsule | Bryant Ranch Prepack | Not provided in source data |
| ANDA074450 | Mexiletine Hydrochloride | Capsule | ANI Pharmaceuticals, Inc. | Not provided in source data |
| ANDA074450 | Mexiletine Hydrochloride | Capsule | Bryant Ranch Prepack | Not provided in source data |

The pack lists 20 authorizations in total, all oral capsules. Only the first 5 records were provided, and they collapse to the 3 distinct entries above.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high graph-based score alone. There are no trials, no relevant publications, and no plausible mechanism linking sodium channel blockade to hypertrichosis.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting mexiletine's pharmacology to hair growth disorders
- Any preclinical or clinical signal specific to mexiletine in hypertrichosis
- Package insert warnings and contraindications (required before any safety screening)
- Confirmed mechanism of action data from DrugBank

**Note on other predictions for this drug:** Among the other predicted indications, **headache disorder** (rank 10, evidence level L3) is the most supported. Small observational and open-label studies report benefit in trigeminal autonomic cephalalgias and refractory chronic daily headache, but there are no RCTs. Any work on that indication would need safety screening first, given mexiletine's proarrhythmic risk in structural heart disease.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

