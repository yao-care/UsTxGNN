---
layout: default
title: Benzocaine
parent: Model Prediction Only (L5)
nav_order: 447
evidence_level: L5
indication_count: 1
---

# Benzocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Benzocaine: From Topical Anesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Benzocaine is a topical local anesthetic marketed in the US as gels, a liquid and a lozenge. The approved indication text is not recorded in the source data.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data (marketed products are topical anesthetics) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 license records |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the source record lists no original indications. The prediction therefore cannot be checked against a documented mechanism. The only support is the TxGNN knowledge-graph score of 0.994, which is a computational prediction, not clinical evidence.

As general background (not derived from the supplied data), benzocaine is an ester-type local anesthetic that blocks voltage-gated sodium channels. That could plausibly ease ocular surface discomfort. It would not address the usual causes of papillary conjunctivitis, which are allergic responses and mechanical irritation from contact lenses or prostheses.

There are also reasons for caution:
- Benzocaine is a recognized contact sensitizer, so it could worsen allergic or irritative ocular surface disease.
- Repeated use of topical ocular anesthetics carries a risk of corneal toxicity.

No hypothesis is supported beyond the model score.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M022 | Kank-A | Liquid | Not recorded |
| M022 | GPS Topical Anesthetic | Gel | Not recorded |
| M022 | Gelato Topical Anesthetic (2 records) | Gel | Not recorded |
| M022 | Defend | Gel | Not recorded |

Of the 20 license records, these are the first 5 returned, which cover 4 distinct products. Registered dosage forms are liquid, gel and lozenge. None is an ophthalmic form, so route compatibility with an eye indication is unassessed.

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found in the drug interaction query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5), with no trials or publications. No mechanism data, approved indication text or safety information is available to assess it. Benzocaine's sensitizing potential and the corneal toxicity risk of topical ocular anesthetics also argue against advancing it.

**To proceed, the following is needed:**
- The FDA package insert, to fill the warnings and contraindications gap (blocking for safety screening)
- Mechanism of action data from DrugBank, to assess any mechanistic link to papillary conjunctivitis
- A systematic search of trials and literature for benzocaine in conjunctival or ocular surface disease
- A route compatibility assessment, since no ophthalmic formulation is currently registered
- A clear account of why an anesthetic would treat an allergic or mechanical condition, including a sensitization risk review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

