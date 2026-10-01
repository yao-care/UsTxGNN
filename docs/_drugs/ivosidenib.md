---
layout: default
title: Ivosidenib
parent: Model Prediction Only (L5)
nav_order: 822
evidence_level: L5
indication_count: 3
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutated Cancers to Bulbar Polio

## One-Sentence Summary

Ivosidenib is a mutant IDH1 inhibitor, used in IDH1-mutated myeloid and biliary cancers.
The TxGNN model predicts it may be effective for **bulbar polio**, but **no clinical trials and no publications** support this prediction.
The link is most likely a knowledge-graph artifact, so the prediction should be treated as low-credibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not reasonable on biological grounds. Ivosidenib inhibits mutant IDH1, which lowers 2-hydroxyglutarate (2-HG) and relieves the differentiation block in IDH1-mutated myeloid and biliary cancers.

Bulbar polio is a poliovirus infection of motor neurons, and no IDH1-driven pathway is involved. The high score (0.993) most likely comes from neighborhood proximity in the knowledge graph, not from real biology. The original-indication and mechanism-of-action fields are also missing from the input, which weakens the prediction further.

**Other predictions for this drug.** Two lower-ranked predictions are biologically plausible:
- AML/MDS related to alkylating agents
- AML/MDS related to radiation

Both are therapy-related myeloid neoplasms, where IDH1 mutations can occur. Any benefit would probably be limited to IDH1-mutated cases. Both have the same score (0.9926), which suggests the graph collapsed them into one signal. They also have no supporting trials or literature, so they are research questions rather than new repurposing findings until existing AML/MDS labeling and trial subgroups are checked.

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
| NDA 211192 | TIBSOVO (Servier Pharmaceutical LLC) | Film-coated tablet (oral) | Not listed in the supplied record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bulbar polio prediction has no plausible mechanism and no trial or literature support, and the high score is likely a graph artifact. The evidence is L5 only, and the package insert safety data has not been retrieved.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indications from DrugBank
- For the therapy-related AML/MDS predictions: an IDH1 mutation-stratified evidence review, and a check of whether current labeling already covers these cases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

