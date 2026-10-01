---
layout: default
title: Mercuric Iodide
parent: Model Prediction Only (L5)
nav_order: 902
evidence_level: L5
indication_count: 10
---

# Mercuric Iodide
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

# Mercuric Iodide: From No Documented Approved Indication (Homeopathic Products) to Ventricular Tachycardia

## One-Sentence Summary

Mercuric iodide is a toxic inorganic mercury salt. In the US it appears only in homeopathic pellet products, and none of the listed products states an approved indication.
The TxGNN model predicts it may be effective for **ventricular tachycardia**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model output only and is not supported by pharmacological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None documented (no approved indication text in the listed products) |
| Predicted New Indication | Ventricular tachycardia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed (homeopathic pellet products) |
| Number of NDAs | 18 listed licenses (license numbers not recorded) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is documented. The marketed products are homeopathic pellets (Mercurius Iodatus Ruber, Mercurius Sulphuricus). No established therapeutic use of mercuric iodide could be used as a starting point for repurposing.

Mechanistically, the prediction is hard to justify. Mercury compounds are associated with cardiotoxicity, arrhythmia, oxidative myocardial injury and disrupted calcium homeostasis. An antiarrhythmic effect is therefore implausible, and a pro-arrhythmic risk is more likely. The high TxGNN score (99.99%) is a graph-based prediction and likely reflects network artifacts rather than real biology.

The other top-ranked predictions (ranks 2–10) are also cardiac rhythm or related disorders, including atrial fibrillation, arrhythmogenic right ventricular cardiomyopathy and catecholaminergic polymorphic ventricular tachycardia. None has any clinical or literature evidence. Their similar scores suggest a shared graph-proximity cluster rather than independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The 18 listed licenses include repeated entries for the same products. Five are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not recorded | Mercurius Iodatus Ruber | Pellet | Not listed |
| Not recorded | Mercurius Sulphuricus | Pellet | Not listed |
| Not recorded | Mercurius Iodatus Ruber | Pellet | Not listed |
| Not recorded | Mercurius Sulphuricus | Pellet | Not listed |
| Not recorded | Mercurius Sulphuricus | Pellet | Not listed |

All products are made by Hahnemann Laboratories, Inc.

---

## Safety Considerations

Please refer to the package insert for safety information.

Mercuric iodide is a toxic mercury salt, and mercury exposure is linked to cardiovascular toxicity. Use in vulnerable groups such as neonates and infants is not supportable on safety grounds. Two of the predicted indications are neonatal or infant arrhythmias. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials, no literature, no known mechanism and no documented original indication. Mercury's known cardiotoxicity argues against a therapeutic role in arrhythmia.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Toxicological assessment of any cardiac use, including mercury exposure limits
- Preclinical evidence showing a beneficial, not adverse, effect on cardiac electrophysiology
- Confirmation of the regulatory status and intended use of the homeopathic products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

