---
layout: default
title: Eflornithine
parent: Model Prediction Only (L5)
nav_order: 643
evidence_level: L5
indication_count: 2
monitor_inn: "EFLORNITHINE"
predicted_indications: ["esotropia", "neurotrophic keratopathy"]
---

# Eflornithine
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

# Eflornithine: From Human African Trypanosomiasis to Esotropia

## One-Sentence Summary

Eflornithine was originally used to treat human African trypanosomiasis (sleeping sickness). The TxGNN model predicts it may be effective for **esotropia**, but this is a computational prediction only: **0 clinical trials** and **0 publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Human African trypanosomiasis (trypanosomiasis) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Eflornithine irreversibly inhibits ornithine decarboxylase (ODC, encoded by *ODC1*), the enzyme that controls polyamine biosynthesis. This is the basis of its use in trypanosomiasis, and also of its other uses: topical treatment of facial hirsutism, oral maintenance therapy for high-risk neuroblastoma (FDA authorisation in December 2023), and a proposed role in the skin manifestations of Bachmann-Bupp syndrome. Detailed mechanism-of-action data beyond this target information are not available.

For esotropia, no established mechanistic link was found. Esotropia is a disorder of ocular alignment driven by extraocular muscle, neural, or refractive factors, and no plausible pathway connecting polyamine depletion to ocular motor alignment is supported by the data compiled for this report. The high TxGNN score is therefore best treated as a hypothesis-generating signal, not as supporting evidence.

A second prediction, **neurotrophic keratopathy** (score 99.38%), is also at the L5 level with no trials or literature. A speculative link exists through polyamines' role in corneal epithelial proliferation and wound healing. However, ODC inhibition would be expected to suppress rather than promote epithelial proliferation, and the disease is driven by impaired corneal innervation and loss of trophic support. This prediction is likewise unvalidated and recommended as Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA215500 (cancelled) | Iwilfin (USWM, LLC) | Tablet (oral) | Not listed in the data compiled |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: exanthem (rash) and dermatitis.
- **Drug Interactions**: The interaction query completed with one record, which is only the drug's pharmacological target (ornithine decarboxylase, ODC1), not a drug-drug interaction with a graded level. No clinically graded interactions were identified.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications, and no plausible mechanistic link between ODC inhibition and ocular alignment. The only US NDA is cancelled, and label safety data were not available.

**To proceed, the following is needed:**
- Retrieve the FDA package insert to obtain warnings and contraindications (this blocks safety screening)
- Obtain complete mechanism-of-action data from DrugBank
- Establish a biological rationale linking polyamine metabolism to extraocular muscle or neural control of ocular alignment, supported by preclinical evidence
- Assess route compatibility (the available product is an oral tablet; ocular indications may need a different route)
- Search for preclinical or clinical studies in esotropia (and neurotrophic keratopathy) before reconsidering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

