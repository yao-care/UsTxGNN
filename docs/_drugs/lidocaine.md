---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthetic Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a widely marketed local anesthetic, sold in the US as injections, gels, patches and other forms.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** were retrieved for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the provided US license records (lidocaine is a local anesthetic) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this record. From general pharmacology, lidocaine is a voltage-gated sodium channel blocker. It blocks nerve conduction, which is why it works as a local anesthetic.

That mechanism makes surface pain relief on the eye plausible. It does not suggest any effect on the underlying disease. Punctate epithelial keratoconjunctivitis is often viral or inflammatory, and nothing in the data shows lidocaine treats that process. The TxGNN score therefore looks more like a symptom-relief signal than evidence of a disease-modifying effect.

There is also a safety concern. Topical anesthetics can impair corneal healing and worsen keratopathy, so the safety direction for corneal surface disease is arguably unfavorable.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

## Literature Evidence

Currently no related literature available for this indication.

## US Market Information

Lidocaine has 20 US authorizations. The five main ones are listed below, and the records provided contain no approved-indication text. Other forms on the market include cream, spray and liquid.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA088327 | Lidocaine Hydrochloride | Injection, solution |
| M017 | POMG Night Time Pain Relief Roller | Gel |
| NDA006488 | Xylocain (Lidocaine HCl) | Injection, solution |
| NDA006488 | Xylocaine MPF | Injection, solution |
| ANDA209190 | Tridacaine XL | Patch |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug-interaction records were available for this drug. For this indication, the main concern is the possible effect of topical anesthetics on corneal healing (see above).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature, and no plausible disease-modifying mechanism. Topical anesthetics may also harm the corneal surface.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Targeted searches for lidocaine ophthalmic use in punctate epithelial keratoconjunctivitis, including a check of corneal-toxicity risk
- Route compatibility assessment (an ophthalmic form is needed, and none is confirmed in the US license list provided)

Other predicted indications should be reviewed separately. The closest evidence is for conjunctival disorder, where 18 trials were found but only 10 were provided. These trials use lidocaine as a procedural anesthetic, not as a treatment. Much of the related literature concerns SUNCT/SUNA headaches, which match the term by name only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

