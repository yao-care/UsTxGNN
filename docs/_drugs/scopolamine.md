---
layout: default
title: Scopolamine
parent: Model Prediction Only (L5)
nav_order: 1145
evidence_level: L5
indication_count: 6
---

# Scopolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Scopolamine: From an Unrecorded Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine is a non-selective muscarinic antagonist marketed in the US mainly as transdermal patches. The US label data supplied does not include its approved indication text.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone, and the mechanism suggests it could even be harmful in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US label data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the sampled licenses are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, scopolamine is a non-selective muscarinic antagonist. Any link to cauda equina syndrome would therefore run through bladder or bowel dysfunction, not through the underlying nerve-root compression.

The link is weak, and it may be contraindicated. Cauda equina syndrome commonly presents with urinary retention or an areflexic bladder, and an anticholinergic could worsen retention. The very high score (99.99%) is a graph-based prediction with no trial or literature record behind it.

The other five predictions are all rated L5 and are also unsupported by any trial or publication:

- **Obsolete neurogenic bladder (score 99.98%):** This is the most mechanistically plausible. Antimuscarinics are established therapy for neurogenic detrusor overactivity, but scopolamine has no bladder-specific evidence. Its central effects (sedation, confusion) and the availability of better bladder-selective agents limit its value. The disease label is obsolete in the ontology and should be remapped, for example to neurogenic detrusor overactivity. This is a research question only.
- **Papillary conjunctivitis (99.98%):** No plausible disease-modifying mechanism. Scopolamine is also known to cause ocular irritation.
- **Atopic conjunctivitis (99.80%):** The disease is mast-cell and IgE-driven, and antimuscarinic action does not target it. It may worsen dry-eye symptoms.
- **Rosacea conjunctivitis (99.40%):** Reduced tear secretion could worsen dry eye. The prediction appears to be a graph-proximity artifact.
- **Vernal conjunctivitis (99.08%):** The disease is Th2-driven allergic, so muscarinic blockade does not address it.

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
| ANDA215329 | Scopolamine (Bryant Ranch Prepack) | Patch, extended release | Not listed in supplied data |
| ANDA208769 | Scopolamine (A-S Medication Solutions) | System | Not listed in supplied data |
| ANDA218384 | Scopolamine (Amneal Pharmaceuticals NY LLC) | Patch, extended release | Not listed in supplied data |
| ANDA215329 | Scopolamine (Bryant Ranch Prepack) | Patch, extended release | Not listed in supplied data |
| ANDA212342 | Scopolamine (Ingenus Pharmaceuticals, LLC) | Patch, extended release | Not listed in supplied data |

Other dosage forms recorded for the drug include patch and solution/drops. Route compatibility with the predicted indications has not been assessed.

---

## Safety Considerations

Please refer to the package insert for safety information.

Points raised in the mechanistic assessment, not from label data:
- An anticholinergic could worsen urinary retention, which is common in cauda equina syndrome.
- Topical and transdermal scopolamine can cause ocular irritation and conjunctival reactions, which is relevant to the conjunctivitis predictions.
- Central anticholinergic effects (sedation, confusion) limit practical use in bladder-related indications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). The mechanism is weak for cauda equina syndrome and may be contraindicated because of the risk of worsening urinary retention. The conjunctivitis predictions have no plausible mechanism.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications and approved indication text), which is currently blocking safety screening
- Mechanism of action data for scopolamine from DrugBank
- Remapping of "obsolete neurogenic bladder" to a current term such as neurogenic detrusor overactivity, followed by a literature search on antimuscarinic use in that condition
- Route compatibility assessment for the transdermal and topical forms against each predicted indication
- A safety review of anticholinergic effects on urinary retention and the eye

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

