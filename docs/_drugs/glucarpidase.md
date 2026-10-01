---
layout: default
title: Glucarpidase
parent: Model Prediction Only (L5)
nav_order: 755
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity Rescue to Diabetic Cataract

## One-Sentence Summary

Glucarpidase is a recombinant enzyme that breaks down methotrexate in plasma. It is marketed in the US as Voraxaze for rescue from methotrexate toxicity.
The TxGNN model predicts it may be effective for **diabetic cataract**, along with nine other cataract and retinopathy variants.
Currently there are **0 clinical trials** and **0 publications** supporting any of these predictions, so this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methotrexate toxicity rescue (taken from the pack's rationale text; the license record has no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125327) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, glucarpidase is a recombinant bacterial carboxypeptidase G2. It hydrolyzes methotrexate into DAMPA and glutamate in plasma.

The review did not find a plausible link between this action and diabetic cataract. Diabetic cataract involves polyol-pathway and oxidative damage to the lens. Glucarpidase acts extracellularly on methotrexate and other folate-like substrates and has no known role in lens biology. At about 83 kDa, it is also unlikely to reach the lens.

The ten predictions look like a systematic graph artifact, not independent signals:

- All ten are cataract or retinopathy variants.
- They sit in a narrow score band of 0.9982–0.9985.
- Seven cataract subtypes share nearly identical scores. Three of them (tetanic, mature and immature cataract) have exactly the same score of 0.99833.

| Rank | Predicted Indication | Score |
|------|------|------|
| 1 | Diabetic cataract | 99.85% |
| 2 | Diabetic retinopathy | 99.84% |
| 3–7 | Tetanic, mature, immature, craniostenosis, and type 2 diabetes-associated cataract | 99.83% |
| 8–9 | Cortical cataract, nuclear senile cataract | 99.83% |
| 10 | Senile cataract | 99.82% |

Diabetic retinopathy has no supporting VEGF or retinal vascular link, and an intravitreal route has no supporting data.

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
| BLA125327 | Voraxaze (BTG International Inc.) | Injection, powder, for solution | Not stated in the license record |

The only registered route is injectable.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.85% score is not backed by any trial, publication or plausible mechanism, and it is most likely a knowledge-graph artifact. A large injectable enzyme also has no route to the lens or retina.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications and approved indication text), which is missing and blocks safety screening
- Mechanism of action data from DrugBank, to test any biological link to lens or retinal disease
- Any preclinical or clinical evidence for the predicted indications. Without it, there is no basis for advancing beyond a model-only hypothesis.
- A route-compatibility assessment for ocular delivery, which is still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

