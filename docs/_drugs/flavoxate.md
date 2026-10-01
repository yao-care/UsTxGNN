---
layout: default
title: Flavoxate
parent: Model Prediction Only (L5)
nav_order: 709
evidence_level: L5
indication_count: 8
---

# Flavoxate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Flavoxate: From Bladder Spasm and Urgency Symptoms to ADHD, Inattentive Type

## One-Sentence Summary

Flavoxate is a smooth-muscle relaxant used for bladder spasm and urgency symptoms.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder, inattentive type**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bladder spasm and urgency symptoms (the US license records contain no indication text) |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both listed under ANDA076835) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Flavoxate is a smooth-muscle relaxant with antimuscarinic, calcium-antagonist and PDE-inhibiting properties. It relaxes bladder detrusor muscle. It has no known primary CNS target relevant to ADHD.

The link between the original indication (bladder symptoms) and ADHD is weak. The 99.75% score most likely reflects a knowledge-graph artifact rather than real biology. The parent term "attention deficit-hyperactivity disorder" (99.39%) and "specific developmental disorder" (99.56%) also score highly, which suggests they are driven by graph proximity to the same ADHD nodes. No clinical or literature evidence supports this prediction.

Other predictions for this drug are more biologically plausible and fit better as research questions:

- **Irritable bowel syndrome** (99.74%): antispasmodic and antimuscarinic action is the rationale for agents such as hyoscine and dicyclomine, and flavoxate's smooth-muscle effect could extend to the gut.
- **Neurogenic bladder** (99.13%): closely related to flavoxate's existing bladder use. The disease term is flagged obsolete and needs mapping to a current ontology term.

Both are still prediction-only, with no trials or publications in the provided data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA076835 | Flavoxate Hydrochloride (Epic Pharma, LLC) | Tablet (oral) | Not listed in the source data |
| ANDA076835 | Flavoxate Hydrochloride (PuraCap Laboratories LLC dba Blu Pharmaceuticals) | Tablet (oral) | Not listed in the source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model-score support (L5) and no trials or publications. Its mechanistic rationale is also weak, since flavoxate has no known CNS target relevant to ADHD. The high score is probably a knowledge-graph artifact.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications, currently a blocking gap for safety screening
- Confirmed mechanism of action data from DrugBank
- Approved indication text from the US license records
- A decision on whether to redirect effort to the more plausible IBS and neurogenic bladder predictions, including mapping the obsolete neurogenic bladder term to a current ontology term
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

