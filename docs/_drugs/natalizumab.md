---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 956
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a monoclonal antibody marketed in the US as TYSABRI and TYRUKO, and the literature in the Evidence Pack places it in multiple sclerosis (MS) treatment.
The TxGNN model predicts it may be effective for **bronchitis**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (inferred from the literature; the licence records contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both are BLAs: BLA125104, BLA761322) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Natalizumab is known to block α4-integrin, which limits leukocyte trafficking into tissues. In theory, this could dampen inflammation driven by immune cell infiltration.

The link to bronchitis is weak. Bronchitis is mostly infectious or self-limited, and it is not a disease of pathological immune-cell trafficking. Systemic immunosuppression would raise infection risk rather than help. The high score (0.995) reflects a graph-based association only, and no specific mechanistic link has been identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125104 | TYSABRI | Injection | Biogen Inc. |
| BLA761322 | TYRUKO | Injection | Sandoz Inc |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trial or literature support (L5). Bronchitis is mostly infectious or self-limited, so a systemic immunomodulatory antibody offers little plausible benefit. Its known risks, such as infection and progressive multifocal leukoencephalopathy (PML), make exploratory use unattractive.

Among the other predictions, psoriasis has the most literature (L4). That evidence is contradictory, and most of it describes psoriasis induced or worsened by natalizumab. One 2021 series reported improvement in comorbid psoriasis, so it may merit follow-up before bronchitis does.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from the DrugBank API)
- The US package insert with warnings and contraindications, for safety screening
- Any preclinical or clinical signal for natalizumab in bronchitis
- A risk-benefit rationale for systemic immunosuppression in a mostly self-limited condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

