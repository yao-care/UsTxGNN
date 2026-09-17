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

# Verteporfin: From Photodynamic Therapy (Wet AMD) to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

> Verteporfin is a benzoporphyrin-derivative photosensitizer known for photodynamic therapy (PDT) of neovascular (wet) age-related macular degeneration, and separately for inhibiting the Hippo pathway's YAP/TAZ-TEAD interaction in oncology research.
> The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
> but this is currently supported by **0 clinical trials** and **0 publications** — a model-only prediction with no mechanistic or empirical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan regulatory data (drug not marketed); known pharmacological use is photodynamic therapy for neovascular (wet) age-related macular degeneration |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Market Status (Taiwan) | Not marketed (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Verteporfin's established mechanism is light-dependent: upon photoactivation it generates reactive oxygen species (ROS) that occlude abnormal choroidal neovascularization, which is the basis of its use in wet AMD. It also has a separate, non-light-dependent mechanism as an inhibitor of the YAP/TAZ-TEAD interaction in the Hippo signaling pathway, which is studied mainly in oncology contexts.

Neither of these mechanisms has a known pathophysiological link to nuclear-DNA-encoded mitochondrial oxidative phosphorylation (OXPHOS) disorders (e.g., Leigh syndrome, Complex I/IV deficiencies). Standard therapeutic strategies for these disorders aim to *reduce* oxidative stress and support electron transport chain function, whereas verteporfin's principal photoactivated action is to *generate* ROS and cause oxidative damage — a direction that runs counter to the therapeutic needs of this indication.

Given this mechanistic mismatch, and the absence of any supporting clinical or literature evidence, this prediction should be treated as an unvalidated knowledge-graph signal rather than a plausible repurposing hypothesis at this stage. Additionally, the drug's `original_moa` field itself is flagged as a data gap, and the drug is not currently marketed in Taiwan, so foundational drug-level data needed for a safety/regulatory review is incomplete.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

Verteporfin currently holds no marketing licenses in Taiwan (market status: Not marketed, total licenses: 0). No license-level data is available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5 evidence) with no clinical trials or literature, and the proposed mechanism (ROS-generating photodynamic action) conflicts directionally with the therapeutic goals of mitochondrial OXPHOS disorders. Combined with missing MOA and safety data, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data (DrugBank/primary literature) to properly assess biological plausibility
- TFDA (or other regulatory) label data — warnings, contraindications, DDI — to enable an S1 safety screen
- Preclinical or mechanistic studies specifically linking verteporfin (or Hippo/YAP-TAZ modulation) to nuclear-DNA-related OXPHOS disorders
- At minimum, case reports or in vitro/in vivo data before this candidate can be reconsidered for advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

