---
layout: default
title: Fenfluramine
parent: Model Prediction Only (L5)
nav_order: 698
evidence_level: L5
indication_count: 4
---

# Fenfluramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Fenfluramine: From Seizures in Dravet and Lennox-Gastaut Syndromes to Proximal 16p11.2 Microdeletion Syndrome

## One-Sentence Summary

Fenfluramine (Fintepla) is a serotonin-releasing drug marketed in the US for seizures in developmental epileptic encephalopathies (Dravet syndrome and Lennox-Gastaut syndrome).
The TxGNN model predicts it may be useful for **proximal 16p11.2 microdeletion syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it remains a hypothesis-level research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license record (the seizure indications above come from the drug's known marketed use) |
| Predicted New Indication | Proximal 16p11.2 microdeletion syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. Based on general pharmacology, fenfluramine is a serotonin-releasing agent and 5-HT2 receptor agonist with anorectic (appetite-suppressing) effects.

The 16p11.2 deletion syndrome includes hyperphagia and obesity, epilepsy, and autism-spectrum features. Fenfluramine's seizure indication and its appetite-suppressing effects overlap with two of these features, which gives a plausible but indirect link. This reasoning rests on general pharmacology, not on any trial or publication in this dataset.

The model also ranked three other predictions highly: hypervitaminosis, obsolete hypertelorism, and frontorhiny. None has a credible mechanistic link, and all are likely knowledge-graph artifacts. Hypertelorism and frontorhiny are structural craniofacial conditions, and hypervitaminosis is managed by stopping the vitamin and giving supportive care. The 16p11.2 microdeletion syndrome is the only prediction with a biologically reasonable connection.

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
| NDA212102 | Fintepla (UCB, Inc.) | Solution | Not stated in the record |

---

## Safety Considerations

- **Cardiopulmonary risks**: Valvular heart disease and pulmonary arterial hypertension are known concerns with fenfluramine. Any future study in a new population would need to weigh them.
- **Drug Interactions**: No interaction records were found in the query.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and an indirect pharmacological argument. No trials or publications exist for this syndrome, and the known cardiopulmonary risks raise the bar for any new use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications
- Mechanism-of-action data
- Preclinical or literature evidence linking serotonergic activity to the seizure or appetite phenotypes of 16p11.2 deletion
- A risk-benefit and cardiac monitoring plan for any exploratory study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

