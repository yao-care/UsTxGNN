---
layout: default
title: Plecanatide
parent: Model Prediction Only (L5)
nav_order: 1055
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Plecanatide: From Chronic Idiopathic Constipation to Hypertrichosis

## One-Sentence Summary

Plecanatide is an oral guanylate cyclase-C (GC-C) agonist, marketed in the US as Trulance. Its FDA-approved uses are chronic idiopathic constipation and irritable bowel syndrome with constipation.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic idiopathic constipation (CIC) and IBS with constipation (IBS-C), per the pharmacology data compiled for this report. The US license record has no indication text. |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is recorded as cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. Based on the pharmacology data compiled for this report, plecanatide is a peptide agonist of guanylate cyclase-C (GUCY2C) on intestinal epithelium. It raises intracellular cGMP and is approved for constipation-predominant gut disorders.

The link to hypertrichosis is weak. No known pathway connects GC-C agonism to hair follicle regulation. Plecanatide acts locally in the gut with minimal systemic absorption, which makes an effect on hair growth even less plausible. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than a biological rationale.

The other nine top-ranked predictions are similarly unsupported:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Ambras type hypertrichosis universalis congenita | 99.998% | Genomic rearrangement disorder (TRPS1 region); no link to GC-C signaling |
| 3 | Malformation syndrome with odontal/periodontal component | 99.997% | Developmental genetic malformation; no mechanism |
| 4 | Isolated genetic hair shaft abnormality | 99.997% | Structural gene defects; not addressed by intestinal GC-C agonism |
| 5 | Syndrome with Dandy-Walker malformation | 99.997% | Congenital brain malformation; negligible systemic exposure |
| 6 | Idiopathic spontaneous coronary artery dissection | 99.996% | cGMP is relevant to vascular tissue, but the drug is minimally absorbed |
| 7 | Vascular disease | 99.995% | Broad category; speculative |
| 8 | Arterial thoracic outlet syndrome | 99.995% | Mechanical compression disorder |
| 9 | Venous thoracic outlet syndrome | 99.995% | Mechanical compression; identical score to the arterial form suggests a graph artifact |
| 10 | Phaeochromocytoma | 99.995% | No link between intestinal GC-C signaling and this tumour |

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

