---
layout: default
title: Tecovirimat
parent: Model Prediction Only (L5)
nav_order: 1204
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: From Smallpox to Hordeolum

## One-Sentence Summary

Tecovirimat is an antiviral originally used to treat smallpox and related orthopoxvirus infections such as cowpox.
The TxGNN model predicts it may be effective for **hordeolum** (stye), but there are **0 clinical trials** and **0 publications** supporting this prediction. It should be treated as a computational artifact until shown otherwise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smallpox (and other orthopoxvirus-related diseases; the US license records contain no indication text) |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tecovirimat inhibits the orthopoxvirus VP37 envelope-wrapping protein (the F13L/F13 homolog). This prevents the formation of egress-competent enveloped virions, which the virus needs to spread within the host. This explains its activity against smallpox, cowpox, vaccinia and mpox.

**The prediction for hordeolum is not mechanistically supported.** A hordeolum is an acute infection of an eyelid gland, caused mainly by *Staphylococcus aureus*. Tecovirimat has no antibacterial activity, and its viral target has no counterpart in these bacteria. The high TxGNN score appears to be a graph-based artifact rather than a biologically meaningful signal. The same applies to the other bacterial predictions in the top ranks (vibrio infection, Klebsiella infection, noma, pneumococcemia) and to phlebotomus fever, which is caused by an RNA virus that lacks the orthopoxvirus target.

**Predictions with real biological plausibility** are all in the orthopoxvirus family:
- **Human orthopoxvirus infection (including mpox):** evidence level L4. The literature consists mostly of narrative reviews, a human skin organoid model, and a clade I mpox report from the Democratic Republic of Congo (NEJM 2025). A 2025 report also notes that efficacy in recent clinical trials has been disappointing.
- **Vaccinia:** evidence level L4. This is the classic model for the drug's target, supported by indirect evidence from reviews.
- **Lumpy skin disease:** a capripoxvirus infection, plausible only by analogy and with no supporting data. It is also a veterinary disease.

These are extensions of the drug's existing indication class rather than new repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Both authorizations are listed as cancelled in the data compiled for this report. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208627 | TPOXX | Capsule | — |
| NDA214518 | TPOXX | Injection, solution, concentrate | — |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hordeolum prediction has no trials, no literature and no plausible mechanism. Tecovirimat acts on an orthopoxvirus-specific protein, and hordeolum is a bacterial infection. Both US NDAs are also currently cancelled.

**To proceed, the following is needed:**
- Redirect the evaluation to the orthopoxvirus-related predictions (mpox, vaccinia), which are better supported but largely overlap with the drug's existing indication class.
- For mpox, review primary randomized trial publications to verify efficacy. The current evidence consists mostly of reviews and case reports.
- Obtain the FDA package insert to complete the safety assessment (warnings, contraindications, interactions).
- Obtain formal mechanism-of-action data from DrugBank.
- Clarify the regulatory status of the cancelled NDAs.
- Do not pursue hordeolum or the other bacterial and non-poxvirus predictions unless new in vitro or clinical evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

