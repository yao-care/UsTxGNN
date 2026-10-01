---
layout: default
title: Meperidine
parent: Model Prediction Only (L5)
nav_order: 898
evidence_level: L5
indication_count: 2
---

# Meperidine
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

# Meperidine: From Pain Management to Tourette Syndrome

## One-Sentence Summary

Meperidine is a mu-opioid agonist analgesic that is currently marketed in the US as injectable and other dosage forms.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** retrieved.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US label data provided. Meperidine is known as an opioid analgesic for pain. |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Meperidine is a mu-opioid receptor agonist with some serotonergic activity. Its efficacy as an analgesic is established, and opioid and monoaminergic signaling have been discussed in tic disorders. This is only a general hypothesis and is not evidence for meperidine itself.

The link between the original and predicted indications is weak. Pain relief and the control of motor and vocal tics are unrelated clinical goals. The 99.46% score comes from graph-based pattern matching, and no trial or publication supports this drug-disease pair.

Safety concerns make a favorable benefit-risk profile unlikely for a chronic neurodevelopmental condition without direct data. These include serotonin syndrome risk, seizure risk from the neurotoxic metabolite normeperidine, and dependence liability.

TxGNN also predicted **trichotillomania** (score 99.39%, L5, Hold). That link looks mechanistically contradictory. Opioid antagonists such as naltrexone have been studied in that condition, while meperidine is an agonist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The source lists 11 authorizations. The table shows the 3 unique authorization numbers among the first 5 records, since NDA021171 appears several times.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021171 | DEMEROL (Hospira, Inc.) | Injection, solution | Not provided in source data |
| ANDA088744 | Meperidine Hydrochloride (Hikma Pharmaceuticals USA Inc.) | Solution | Not provided in source data |
| ANDA080445 | Meperidine Hydrochloride (Hikma Pharmaceuticals USA Inc.) | Injection | Not provided in source data |

An oral tablet form is also listed among the available dosage forms.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or interaction data were retrieved. The lack of interaction data likely reflects a data gap rather than an absence of interactions.

The following concerns come from the mechanistic assessment, not from label data:
- **Serotonin syndrome**: risk is higher with serotonergic co-medications.
- **Seizure threshold**: the metabolite normeperidine is neurotoxic and can lower it.
- **Dependence**: opioids carry dependence liability, which matters for chronic use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or literature. The safety profile is unfavorable for a chronic condition. The trichotillomania prediction looks mechanistically contradictory.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking meperidine to tic disorders
- Comparison against existing Tourette syndrome treatments for benefit-risk
- A full drug interaction check, especially for serotonergic drugs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

