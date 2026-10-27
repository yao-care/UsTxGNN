---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 1026
evidence_level: L5
indication_count: 10
monitor_inn: "PEMIGATINIB"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "amyotrophic lateral sclerosis, susceptibility to", "axial spondylometaphyseal dysplasia"]
last_modified_at: 2026-10-14
description: "Pemigatinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the compiled data"
---

# Pemigatinib
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

## Pemigatinib: From an Unspecified Original Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Pemigatinib is an oral FGFR1-3 kinase inhibitor, marketed in the US as PEMAZYRE tablets. The label indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Pemigatinib is known to be an FGFR1-3 inhibitor, a targeted kinase-inhibitor class used in oncology. Because the original MOA entry is empty, this mechanism could not be cross-checked against the data.

The link to multiple endocrine neoplasia is weak. These syndromes are typically driven by MEN1 or RET alterations, and the compiled data shows no direct connection between FGFR signaling and these syndromes. The high TxGNN score (0.997) reflects a pattern in the knowledge graph rather than demonstrated biology, and a high score alone should not be read as evidence of efficacy.

For context, the other top-ranked predictions are also unsupported. Several are implausible for an FGFR inhibitor or are not relevant to human medicine: amenorrhea, cytomegalovirus infection, and two bovine diseases (infectious bovine rhinotracheitis and malignant catarrhal fever). The two bovine diseases share an identical score, which suggests a graph-based artifact. Among the others, HER2-positive breast carcinoma, ALS, and axial spondylometaphyseal dysplasia have some biological plausibility via FGFR signaling, but none has trial or disease-specific literature support in the data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213736 | PEMAZYRE (Incyte Corporation) | Tablet | Not available; status: cancelled |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 50 potential interactions. The 20 listed in the data compiled for this report include these **Major** interactions:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Cobicistat
  - Lumacaftor
  - Chloramphenicol
  - Erythromycin
  - Ketoconazole
  - Fluconazole

  The pattern, with many CYP3A-related agents such as macrolides, azoles, and cobicistat, suggests that strong CYP3A inhibitors and inducers need careful management. Moderate interactions include cimetidine, clotrimazole, deferasirox, ivacaftor, zafirlukast, griseofulvin, elagolix, osilodrostat, metreleptin, glycerol phenylbutyrate, and troglitazone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials or literature, no demonstrated mechanistic link between FGFR inhibition and multiple endocrine neoplasia, and the only US license is cancelled. The safety review also cannot proceed without the label warnings and contraindications.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text
- A mechanistic rationale, or preclinical data, linking FGFR signaling to multiple endocrine neoplasia
- Review of the cancelled NDA status and its implications for any development path
- Consideration of better-supported alternatives, such as HER2-positive breast carcinoma, where FGFR-mediated resistance is biologically plausible, though disease-specific evidence is still lacking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

