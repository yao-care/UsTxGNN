---
layout: default
title: Verteporfin
parent: Model Prediction Only (L5)
nav_order: 1288
evidence_level: L5
indication_count: 1
---

# Verteporfin
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

# Verteporfin: From Photodynamic Therapy Photosensitizer to Mitochondrial Oxidative Phosphorylation Disorder (Nuclear DNA Anomalies)

## One-Sentence Summary

Verteporfin is a photosensitizer used in photodynamic therapy (PDT), and it is marketed in the US as Visudyne.
The TxGNN model predicts it may be useful for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**.
This is a computational prediction only: **0 clinical trials** and **0 publications** currently support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied record (verteporfin is a photosensitizer used in photodynamic therapy) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Verteporfin generates reactive oxygen species (ROS) when activated by light, which is the basis of its use in PDT. In preclinical work it has also been reported to inhibit YAP-TEAD signaling and to modulate autophagy, independent of light.

No direct mechanistic evidence links verteporfin to nuclear-DNA-driven OXPHOS disorders. Any link would have to run through indirect pathways, such as autophagy/mitophagy or Hippo-YAP signaling, and is speculative.

There is also a countervailing concern. ROS generation and mitochondrial photodamage could worsen mitochondrial dysfunction rather than improve it. The very high TxGNN score (0.995; rank 12,092) should therefore be read as a hypothesis to test, not as support for efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021119 | Visudyne (Bausch & Lomb Incorporated) | Injection, powder, lyophilized, for solution | Not listed in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials, no literature, and no direct mechanistic support. Verteporfin's ROS-generating photosensitizing action could plausibly be harmful in mitochondrial disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank, and the original approved indications
- Preclinical evidence in OXPHOS-deficiency models, including a check that light-independent effects (autophagy/mitophagy, YAP-TEAD) are beneficial and ROS-related toxicity is not
- Route and dosing compatibility assessment, since the available route is injectable and the required route for the new indication is unspecified

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

