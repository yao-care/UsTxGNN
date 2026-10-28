---
layout: default
title: Fenbendazole
parent: Model Prediction Only (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
monitor_inn: "FENBENDAZOLE"
predicted_indications: ["urinary bladder carcinoma", "urinary bladder neoplasm", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder squamous papilloma", "bladder signet ring cell adenocarcinoma", "bladder mixed adenocarcinoma", "bladder colonic type adenocarcinoma", "bladder colloid adenocarcinoma"]
last_modified_at: 2026-10-14
description: "Fenbendazole: predicted new indication Urinary bladder carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Fenbendazole
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

## Fenbendazole: Urinary bladder carcinoma
{: .text-alpha }

## One-Sentence Summary

Fenbendazole is a benzimidazole anthelmintic with no approved human indication on record in the data compiled for this report.
The TxGNN model predicts it may be effective for **urinary bladder carcinoma**, but **0 clinical trials** and **0 publications** were found under this exact term.
The closely related term "urinary bladder neoplasm" has **3 publications** (2 relevant preclinical studies), which cannot be counted as direct evidence for the top-ranked entry.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Urinary bladder carcinoma |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (L4 for the related term "urinary bladder neoplasm") |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fenbendazole is a benzimidazole anthelmintic. Drugs in this class bind tubulin and may disrupt microtubule polymerization. Preclinical work has also proposed effects on p53 signaling and glucose metabolism.

These mechanisms are plausible for bladder cancer, since microtubule disruption and cell-stress pathways are established anticancer targets. However, no direct evidence supports this for the top-ranked entry. The high score likely reflects the model's learned associations, and it is not a substitute for experimental or clinical data.

For the related term "urinary bladder neoplasm," two recent preclinical studies (2024 and 2026) examine fenbendazole in bladder cancer models, using intravesical delivery with combination approaches. They are consistent with the proposed mechanisms but are indirect, non-clinical evidence.

Other predicted bladder entries (infiltrating urothelial carcinoma, non-invasive urothelial carcinoma, urachal carcinoma, squamous papilloma, and several adenocarcinoma subtypes) have scores of about 99.985–0.9999. They have no trials or literature, and their scores likely reflect closeness to bladder cancer terms in the ontology rather than independent signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found under "urinary bladder carcinoma." The following were retrieved under the related term "urinary bladder neoplasm." Study types are inferred from titles and abstracts and should be confirmed by reading the full texts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41861111](https://pubmed.ncbi.nlm.nih.gov/41861111/) | 2026 | Preclinical (combination therapy) | Advanced Science | Intravesical nanoplatform (FBZ@BSA@PDA) combining fenbendazole-induced ferroptosis, immunogenic cell death activation, and photothermal therapy for bladder cancer |
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | Preclinical (intravesical combination) | J Exp Clin Cancer Res | Intravesical CRISPR-Cas13a plus fenbendazole combination therapy for bladder cancer |
| [23208426](https://pubmed.ncbi.nlm.nih.gov/23208426/) | 2012 | Preclinical/mechanistic | J Toxicol Sci | Ubiquitin D activation and apoptosis with carcinogens in rats; relevance to fenbendazole is unclear |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Fenbendazole 222 MG (B & L Healthcare Products INC) | Capsule | No indication text (status: cancelled) |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on model score alone, with no clinical trials and no literature under the exact term (L5). Evidence is insufficient to advance. The related "urinary bladder neoplasm" entry is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the 2024 and 2026 preclinical studies to confirm study design and findings
- Human pharmacokinetic and toxicology data, since there is no approved human use
- Assessment of route compatibility, particularly for intravesical delivery
- Independent in vitro and in vivo confirmation in bladder cancer models before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

