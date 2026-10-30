---
layout: default
title: Linaclotide
parent: Model Prediction Only (L5)
nav_order: 861
evidence_level: L5
indication_count: 3
monitor_inn: "LINACLOTIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
last_modified_at: 2026-10-30
description: "Linaclotide: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Linaclotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Linaclotide: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Linaclotide is a drug originally associated with irritable bowel syndrome, and its marketed form (Linzess) is an oral capsule.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, linaclotide is a guanylate cyclase-C (GC-C) agonist that acts locally on the intestinal epithelium with minimal systemic absorption. Activating GC-C raises intracellular cGMP, which increases intestinal fluid secretion, accelerates transit, and may reduce visceral pain signalling. This explains its use in bowel disorders such as irritable bowel syndrome.

Cauda equina syndrome is a compressive neurological emergency, typically caused by disc herniation, and it requires surgical decompression. No direct mechanistic link to linaclotide has been established. The only plausible connection is indirect: symptomatic relief of neurogenic bowel dysfunction (constipation) that can accompany the condition. That would not treat the underlying disease.

The very high TxGNN score (0.9996) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. With no supporting clinical or literature evidence, it should not be read as evidence of efficacy.

Two other predictions were also generated, both at evidence level L5 with a recommendation of Hold:
- **Obsolete neurogenic bladder (score 0.9989)**: No direct mechanism is evident. Any link would be indirect, through co-existing neurogenic bowel dysfunction. The disease term is also flagged as obsolete in the ontology, which lowers the reliability of this prediction.
- **Insomnia (score 0.9951)**: Linaclotide has negligible systemic exposure and no known action on sleep pathways. Any benefit would be a secondary effect of relieving abdominal symptoms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA202811 (cancelled) | Linzess (Allergan, Inc.) | Capsule, gelatin coated (oral) | Not listed |

## Safety Considerations

**Drug Interactions:** The interaction screen identified 56 interacting drugs. Most are minor. The moderate-level interactions among those listed are:
- Levonorgestrel
- Ethinylestradiol
- Norethisterone
- Levothyroxine
- Thyroid, porcine

Minor interactions include proton pump inhibitors (rabeprazole, esomeprazole, dexlansoprazole), NSAIDs (ibuprofen, diclofenac, ketorolac, oxaprozin, bromfenac), and other laxatives (bisacodyl, docusate, castor oil, polyethylene glycol).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it, and no credible mechanistic link to cauda equina syndrome. The marketed US product is also listed as cancelled. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data
- Preclinical or clinical evidence supporting any benefit in cauda equina syndrome, or in neurogenic bowel dysfunction as a symptom-level target
- Clarification of the current US regulatory status of linaclotide, since the listed NDA is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

