---
layout: default
title: Dimenhydrinate
parent: Moderate Evidence (L3-L4)
nav_order: 610
evidence_level: L4
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Dimenhydrinate: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is an over-the-counter antihistamine sold in the US mainly as a motion sickness remedy (Dramamine, Gravol). The TxGNN model predicts it may be effective for **allergic urticaria**, but **0 clinical trials** and **1 publication** (a canine pharmacokinetic pilot study) currently support this direction. The evidence is very early-stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness (inferred from product names; approved indication text was not supplied) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the listed products carry authorization number M009) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Dimenhydrinate is a salt of diphenhydramine and 8-chlorotheophylline. Diphenhydramine is a first-generation H1 receptor antagonist, and dimenhydrinate is already marketed in the US for motion sickness.

H1 blockade is the established way to control histamine-driven wheals and itching in allergic urticaria. This class-level mechanism likely explains the very high TxGNN score. The same reasoning applies to the model's second prediction, **cold urticaria** (score 99.24%). It is a physical urticaria driven by mast cell histamine release, but it has no trial or literature evidence and sits at L5 (model prediction only).

The mechanistic link is a class and moiety effect of diphenhydramine. No dimenhydrinate-specific efficacy data in urticaria were supplied. First-generation antihistamines are also sedating and anticholinergic. Current guidance generally prefers second-generation H1 antihistamines, which limits the practical value of this repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic pilot study (dogs) | Veterinary Dermatology | Compared diphenhydramine levels after oral and IV diphenhydramine and oral dimenhydrinate in healthy dogs. It also looked at the effect on histamine-induced wheal formation. Dimenhydrinate has been reported to give better oral absorption of diphenhydramine. This is an animal study, not human evidence. |

---

## US Market Information

Approved indication text was not provided for these listings. The table shows five of the 20 licenses.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| M009 | Motion Sickness Relief | Tablet | Cardinal Health 110, LLC. DBA Leader |
| M009 | Dramamine | Chewable tablet | Lil' Drug Store Products, Inc. |
| M009 | Gravol | Syrup | Church & Dwight Co., Inc. |
| M009 | Motion Sickness Relief | Tablet | Allegiant Health |
| M009 | Dimenhydrinate | Tablet | CVS Pharmacy, Inc. |

Other dosage forms on the market include solution for injection, liquid-filled capsules and coated tablets.

---

## Safety Considerations

- **Class profile**: As a first-generation H1 antihistamine, it has a sedating and anticholinergic profile. This is a practical limitation for chronic urticaria treatment.
- **Drug Interactions**: The DDI query returned no results.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is sound, and the TxGNN score is very high. However, the only supporting literature is one canine pharmacokinetic pilot study, with no clinical trials. Second-generation antihistamines are already preferred for urticaria, and the safety review cannot proceed without package insert data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to complete the safety screen
- Detailed mechanism of action data (MOA)
- Human clinical evidence for dimenhydrinate specifically in urticaria, or a rationale for choosing it over second-generation antihistamines
- Route and dosage compatibility assessment for the urticaria indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

