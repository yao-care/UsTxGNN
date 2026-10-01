---
layout: default
title: Ferric Maltol
parent: Model Prediction Only (L5)
nav_order: 702
evidence_level: L5
indication_count: 3
---

# Ferric Maltol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Ferric Maltol: From Iron Deficiency to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferric maltol is an oral ferric iron product marketed in the US as ACCRUFER. The supplied data lists no approved indication, so iron deficiency is inferred from general pharmacology.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but **no clinical trials and no publications** currently support this pairing. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (generally used for iron deficiency) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Ferric maltol is an oral ferric iron complex, and it is generally used to replenish iron in iron deficiency.

Plummer-Vinson syndrome combines iron deficiency anemia, difficulty swallowing, and esophageal webs. Iron repletion is the established management. The link is therefore biologically plausible. Any benefit would most likely come from correcting the iron deficiency, not from a disease-specific effect. This reasoning rests on general pharmacology, not on the supplied data.

Two other TxGNN predictions were weaker:
- **Vitamin B12- and folate-independent constitutional megaloblastic anemia** (score 99.98%): No clear mechanistic rationale. Megaloblastic anemia reflects impaired DNA synthesis, and iron is not its recognized treatment. The high score likely reflects proximity to other anemia nodes in the knowledge graph.
- **IRIDA syndrome** (score 99.33%): This condition is defined by poor response to oral iron because of high hepcidin. An oral iron product working here is speculative and arguably runs against the indication.

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
| NDA212320 | ACCRUFER (Shield TX (UK) Ltd) | Capsule (oral) | Not listed in the supplied data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is not backed by any clinical trial or publication (evidence level L5). Plummer-Vinson syndrome is a plausible fit through iron repletion, yet the benefit would likely be no different from standard iron therapy. Package insert safety data and the approved indication are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication text for NDA212320 and the mechanism of action (query DrugBank)
- A literature and trial search for ferric maltol or oral iron in Plummer-Vinson syndrome
- An assessment of whether ferric maltol offers any advantage over existing iron therapy
- Route compatibility and similarity-to-original-indication analyses, both still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

