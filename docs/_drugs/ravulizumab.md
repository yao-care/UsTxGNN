---
layout: default
title: Ravulizumab
parent: Model Prediction Only (L5)
nav_order: 1112
evidence_level: L5
indication_count: 10
monitor_inn: "RAVULIZUMAB"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
---

# Ravulizumab
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

# Ravulizumab: From Paroxysmal Nocturnal Hemoglobinuria to Autosomal Recessive Severe Congenital Neutropenia (G6PC3 Deficiency)

## One-Sentence Summary

Ravulizumab is a long-acting C5 complement inhibitor, originally used to treat paroxysmal nocturnal hemoglobinuria (PNH).
The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single BLA is listed as cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, ravulizumab is a long-acting inhibitor of complement component C5. Its efficacy in PNH, a disease of complement-mediated hemolysis, is the basis of its original indication.

The predicted disease is different in nature. G6PC3 deficiency is a defect in glucose-6-phosphatase catalytic subunit 3, which causes neutrophil apoptosis and endoplasmic reticulum stress. No established link exists between terminal complement activation and this neutropenia. The high TxGNN score appears to reflect network proximity within the knowledge graph rather than a biologically validated mechanism.

The other top-ranked predictions show the same pattern. These include cyclic hematopoiesis, severe congenital neutropenia, CXCR2 deficiency, primary hyperoxaluria, and pseudo-von Willebrand disease. None has a recognized role for C5 inhibition, and none has supporting trials or literature. Primary hyperoxaluria is the only one with even a speculative indirect link, through complement-related secondary renal injury from calcium oxalate crystals. Its primary disease driver is not addressed by C5 blockade.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761108 | Ultomiris (Alexion Pharmaceuticals Inc.) | Solution, concentrate | Not listed in the compiled data (status: cancelled) |

## Safety Considerations

- **Contraindication signal from the knowledge graph**: Meningococcal infection is listed as a contraindicated disease. This comes from knowledge graph edges, not from package insert text. It is consistent with the known infection risk from terminal complement blockade, and the risk is greater in patients with immunodeficiency.
- **Drug Interactions**: Four interactions were found, all rated Minor. They involve human immunoglobulin G in its intravenous, subcutaneous, intramuscular, and combined intravenous/subcutaneous forms.

Please refer to the package insert for other warnings and contraindications. The label text was not available when this report was compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (Evidence Level L5), and no plausible mechanistic link between C5 inhibition and G6PC3-deficiency neutropenia. Complement blockade also carries a serious risk of meningococcal and other encapsulated-organism infection, which is a particular concern in neutropenic or immunodeficient patients. In addition, the only US license is listed as cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence for complement involvement in G6PC3-deficiency neutropenia, such as preclinical or biomarker studies
- Detailed mechanism-of-action data for ravulizumab
- The full package insert, to review warnings and contraindications
- Clarification of the US regulatory status and the reason for cancellation
- A risk-benefit assessment of infection risk (including meningococcal vaccination and prophylaxis) in neutropenic patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

