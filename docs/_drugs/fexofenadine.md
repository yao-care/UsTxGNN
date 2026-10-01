---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 1
---

# Fexofenadine
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

# Fexofenadine: From Allergy Relief to Rosacea Conjunctivitis

## One-Sentence Summary

Fexofenadine is marketed in the US in oral tablet products labeled for allergy relief. The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the knowledge-graph score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (product names indicate allergy relief) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed authorizations are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. Fexofenadine is a second-generation, peripherally acting H1-receptor antagonist (general pharmacological knowledge, not taken from the Evidence Pack). A plausible but unverified hypothesis is that it could relieve histamine-mediated ocular surface symptoms such as itching and redness.

The relationship between the original and predicted indications is weak. Ocular rosacea is driven mainly by meibomian gland dysfunction, innate-immune and inflammatory dysregulation, and ocular surface microbiome changes. An antihistamine is unlikely to address this core pathology. At most it might ease allergic-type symptoms that coexist with the condition.

The score of 0.998 (graph rank 4573) is a hypothesis-generating signal, not evidence of efficacy. No mechanism could be verified from the supplied data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204507 | Fexofenadine HCl | Tablet, film coated | Not listed in source data |
| ANDA211075 | allergy relief | Tablet | Not listed in source data |
| ANDA204097 | Fexofenadine HCL | Tablet | Not listed in source data |
| ANDA211075 | Allergy Relief | Tablet | Not listed in source data |
| ANDA204097 | 24HR Allergy Relief | Tablet | Not listed in source data |

All listed products are oral tablets. No ocular or topical formulation appears in the data. Route compatibility with an ocular indication has not been assessed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model prediction (Evidence Level L5), with no trials, no literature and no verified mechanism. The plausible mechanism, symptomatic antihistamine effect, does not address the main drivers of ocular rosacea. The prediction is a hypothesis only and does not justify advancing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed for safety screening
- Mechanism of action data (e.g., from DrugBank) and an analysis of its link to ocular rosacea pathology
- Original approved indication text
- A systematic literature and trial search for antihistamines in ocular rosacea or blepharoconjunctivitis
- A route and formulation assessment, since the marketed products are oral tablets and an ocular indication may need a different route

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

