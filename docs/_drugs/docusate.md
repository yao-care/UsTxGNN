---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 2
---

# Docusate
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

# Docusate: From Constipation to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is a stool-softening surfactant, originally used to treat constipation (the knowledge graph also links it to several anemias).
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder (the knowledge graph also lists folic acid deficiency anemia, iron deficiency anemia, hypochromic anemia, deficiency anemia and microcytic anemia) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, docusate is a stool-softening surfactant, and its efficacy in constipation is established. The data compiled for this report do not support a direct mechanistic link to Plummer-Vinson syndrome.

Plummer-Vinson syndrome combines iron deficiency anemia, dysphagia and esophageal webs. Docusate's listed original indications include iron deficiency anemia and related anemias, so the high score most likely reflects shared anemia annotations in the knowledge graph (a network-proximity artifact). Docusate does not correct iron deficiency, esophageal webs or dysphagia.

At most, docusate could play a supportive role, such as easing constipation associated with oral iron therapy. That is not a repurposing indication.

A second prediction, vitamin B12- and folate-independent constitutional megaloblastic anemia (score 99.15%), was also evaluated. It likewise has no supporting trials or literature and no plausible pharmacologic rationale. Such conditions are typically driven by inherited defects in nucleotide synthesis or metabolism, so it is not pursued further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M007 (cancelled) | Stool Softener | Capsule, liquid filled | Not specified |
| M334 (cancelled) | Docusate Sodium | Liquid | Not specified |

Both authorizations are cancelled, and no valid licenses are currently held.

## Safety Considerations

- **Drug Interactions** (4 found; none rated major):
  - Lactulose: Moderate
  - Mineral oil: Moderate
  - Phenolphthalein: Moderate
  - Linaclotide: Minor
- **Knowledge-graph contraindication signals** (not label text): peptic ulcer disease, potassium deficiency disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, hemolytic anemia, appendicitis, chronic atrophic gastritis, Leber hereditary optic neuropathy, gastroenteritis.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score, with no clinical trials, no literature and no plausible mechanism. It is most likely an artifact of shared anemia annotations. Both US authorizations are cancelled, and the label safety review is blocked by missing package insert data.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- FDA package insert warnings and contraindications
- Evidence of a plausible pharmacologic link to iron deficiency, esophageal webs or dysphagia
- Any clinical or preclinical study relevant to Plummer-Vinson syndrome
- Route compatibility and similarity-to-original-indication assessments (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

