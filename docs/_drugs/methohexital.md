---
layout: default
title: Methohexital
parent: Model Prediction Only (L5)
nav_order: 910
evidence_level: L5
indication_count: 5
---

# Methohexital
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Methohexital: From Anesthesia Induction to Insomnia

## One-Sentence Summary

Methohexital is an ultra-short-acting intravenous barbiturate anesthetic, marketed in the US as Brevital Sodium and as generic injections.
The TxGNN model predicts it may be effective for **insomnia**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intravenous anesthesia (the US license records provide no indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (1 NDA and 2 ANDA entries) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Methohexital is a barbiturate, and this class enhances GABA-A receptor activity, which is biologically consistent with sedation. That gives the insomnia prediction a plausible pharmacological basis.

The practical fit is poor, though. Methohexital is an ultra-short-acting drug given only by injection. Its short duration and intravenous route make it impractical for chronic insomnia, which needs a convenient, sustained-effect treatment such as an oral drug. The very high model score (0.999) is a prediction only, and nothing in the retrieved evidence confirms it.

Other predicted indications for this drug include migraine and headache disorders. The retrieved literature for those links anesthesia and electroconvulsive therapy (ECT) to headache, most likely as an adverse event, not as a treatment effect.

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
| NDA011559 | Brevital Sodium (Par Health USA, LLC) | Injection, powder, lyophilized, for solution | Not provided in the record |
| ANDA215488 | Methohexital Sodium (OneSource Specialty Pharma Limited) | Injection | Not provided in the record |
| ANDA215488 | Methohexital Sodium (Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc.) | Injection | Not provided in the record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction is supported only by a model score, with no clinical trials or publications. The drug's ultra-short action and intravenous-only use also make it a poor fit for chronic insomnia.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data
- Any clinical or preclinical evidence of benefit in insomnia
- An assessment of whether an injectable, ultra-short-acting drug can meet the route and duration needs of insomnia treatment
- Review of the migraine and headache signals, which so far appear to reflect adverse events around anesthesia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

