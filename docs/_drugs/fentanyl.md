---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 700
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent opioid (mu-opioid receptor agonist) used for pain relief and anesthesia. This is general drug knowledge, because the approved indication text is blank in the provided data.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with a very high score.
However, there are **0 clinical trials** and **0 publications** behind this prediction, so it is a model signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain management and anesthesia (general drug knowledge; not stated in the provided license data) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided record. Fentanyl is a mu-opioid receptor agonist, and it is marketed as an injection and as an extended-release patch.

The prediction is hard to support on biological grounds. NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*). These variants make the kidney reabsorb water without vasopressin. Fentanyl has no known direct action on this receptor. Opioids are generally reported to promote antidiuresis or hyponatremia, so a therapeutic benefit is implausible and a possible worsening of the condition cannot be excluded.

The high TxGNN score (0.995) should not be read as efficacy. Nothing in the data links fentanyl's known pharmacology to NSIAD.

**Second-ranked prediction:** Tourette syndrome (score 99.05%, also L5, also Hold). Any link would be indirect, through opioid signaling in cortico-striatal-thalamic circuits. No trials or literature were found. Fentanyl carries dependence, respiratory depression and abuse risks, and there is no evidence it is appropriate for a chronic tic disorder. A follow-up would start with other opioid-system modulators, not fentanyl.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019101 | Fentanyl Citrate (Hikma Pharmaceuticals USA Inc.) | Injection | Not listed in source data |
| ANDA077449 | Fentanyl (Ingenus Pharmaceuticals, LLC) | Patch, extended release | Not listed in source data |
| ANDA077449 | Fentanyl (Aveva Drug Delivery Systems Inc.) | Patch, extended release | Not listed in source data |
| ANDA210762 | Fentanyl Citrate (Fresenius Kabi USA, LLC) | Injection, solution | Not listed in source data |

Five of the 20 authorizations were provided. One of them, NDA019101, is repeated in the source with the same manufacturer, so it appears only once above.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score, with no trials or literature. The known pharmacology of opioids (antidiuresis, hyponatremia) argues against benefit in NSIAD, and fentanyl's abuse and respiratory-depression risks make it a poor candidate for repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before any safety screening
- Mechanism of action data (for example, from DrugBank)
- Evidence that opioid receptor activity affects the V2 receptor or *AVPR2*-driven water reabsorption
- Preclinical or mechanistic studies supporting any of the predicted indications
- For Tourette syndrome, a literature review of other opioid-system modulators before considering fentanyl

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

