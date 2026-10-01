---
layout: default
title: Defibrotide
parent: Model Prediction Only (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Pseudo-von Willebrand Disease

## One-Sentence Summary

Defibrotide is an injectable endothelial-protective, antithrombotic agent marketed in the US as DEFITELIO. The pack lists no approved-indication text, so the original use is taken from the drug's known label (hepatic veno-occlusive disease after stem cell transplant), not from the pack. The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease**, but there are **0 clinical trials** and **0 publications** supporting this direction, and the mechanism points the wrong way.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data (known label use: hepatic veno-occlusive disease after HSCT) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the pack. The available rationale describes defibrotide as a profibrinolytic, antithrombotic, endothelial-protective agent.

Pseudo-von Willebrand disease is a platelet-type bleeding disorder caused by a gain-of-function defect in platelet GPIb-alpha. A drug that reduces clotting and promotes fibrinolysis has no evident therapeutic role here. It could plausibly worsen bleeding.

The high graph score therefore looks like a statistical artefact of the knowledge graph, not a mechanistically grounded prediction. Most other top-ranked predictions (ranks 2, 3, 5-9) are also bleeding or platelet disorders with the same problem.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA208114 | DEFITELIO | Injection, solution | Jazz Pharmaceuticals, Inc. |

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records, so the data are incomplete, not evidence of no interactions.
- **Mechanism-based concern**: Defibrotide's antithrombotic and profibrinolytic activity carries a theoretical bleeding risk, which matters in a bleeding disorder.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). The proposed mechanism is opposite to what a bleeding disorder needs, and no trials or publications support it.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap)
- Mechanism of action data from DrugBank
- A plausible mechanistic argument for GPIb-alpha gain-of-function disease, or deprioritisation of this candidate

**Note on other predictions:** The only direction with literature support in this pack is **thrombotic thrombocytopenic purpura** (rank 4, L4, "Research Question"). It rests on small, mostly 1990s case reports and transplant-associated thrombotic microangiopathy studies. One 1994 report describes TTP occurring after defibrotide, which is a safety signal. This direction is worth reviewing separately.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

