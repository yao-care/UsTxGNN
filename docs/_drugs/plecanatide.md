---
layout: default
title: Plecanatide
parent: Model Prediction Only (L5)
nav_order: 1055
evidence_level: L5
indication_count: 10
monitor_inn: "PLECANATIDE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "syndrome with a Dandy-Walker malformation as major feature", "idiopathic spontaneous coronary artery dissection", "vascular disease", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "phaeochromocytoma"]
last_modified_at: 2026-10-28
description: "Plecanatide: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Plecanatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Plecanatide: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Plecanatide is an oral guanylate cyclase-C (GC-C) agonist, marketed in the US as Trulance. Its FDA-approved uses are chronic idiopathic constipation and irritable bowel syndrome with constipation.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. Based on the pharmacology data compiled for this report, plecanatide is a peptide agonist of guanylate cyclase-C (GUCY2C) on intestinal epithelium. It raises intracellular cGMP and is approved for constipation-predominant gut disorders.

The link to hypertrichosis is weak. No known pathway connects GC-C agonism to hair follicle regulation. Plecanatide acts locally in the gut with minimal systemic absorption, which makes an effect on hair growth even less plausible.

The other nine top-ranked predictions are similarly unsupported:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Ambras type hypertrichosis universalis congenita | 1.0000 | Genomic rearrangement disorder (TRPS1 region); no link to GC-C signaling |
| 3 | Malformation syndrome with odontal/periodontal component | 1.0000 | Developmental genetic malformation; no mechanism |
| 4 | Isolated genetic hair shaft abnormality | 1.0000 | Structural gene defects; not addressed by intestinal GC-C agonism |
| 5 | Syndrome with Dandy-Walker malformation | 1.0000 | Congenital brain malformation; negligible systemic exposure |
| 6 | Idiopathic spontaneous coronary artery dissection | 1.0000 | cGMP is relevant to vascular tissue, but the drug is minimally absorbed |
| 7 | Vascular disease | 1.0000 | Broad category; speculative |
| 8 | Arterial thoracic outlet syndrome | 1.0000 | Mechanical compression disorder |
| 10 | Phaeochromocytoma | 1.0000 | No link between intestinal GC-C signaling and this tumour |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208745 (cancelled) | Trulance (Salix Pharmaceuticals Inc.) | Tablet (oral) | Not stated in the license record |

## Safety Considerations

- **Drug Interactions**: Two interaction records were compiled. Idelalisib has a **Moderate** interaction level (DDInter). The second record is a pharmacology entry for the target Guanylyl cyclase-C (GUCY2C), which is the drug's intended target rather than an interacting drug, and it carries no severity level.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or publications exist, and there is no plausible mechanism linking a locally acting intestinal GC-C agonist to hair growth. The US license is also recorded as cancelled.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Any preclinical or clinical evidence for a hair or follicle effect of GC-C/cGMP signaling
- Clarification of the cancelled NDA status and the approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

