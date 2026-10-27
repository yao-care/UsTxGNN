---
layout: default
title: Ivosidenib
parent: Model Prediction Only (L5)
nav_order: 822
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Ivosidenib: predicted new indication Bulbar polio (evidence level L5). Approved use: Acute myeloid leukemia"
monitor_inn: "IVOSIDENIB"
predicted_indications: ["bulbar polio"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ivosidenib: From Acute Myeloid Leukemia to Bulbar Polio
{: .text-alpha }

## One-Sentence Summary

Ivosidenib is a targeted oral drug originally used to treat acute myeloid leukemia (AML) and related myeloid cancers.
The TxGNN model's top-ranked prediction is **bulbar polio**, but there are **0 clinical trials** and **0 publications** supporting it, and no plausible biological link was identified.
Two lower-ranked predictions, **AML/MDS related to alkylating agents** and **AML/MDS related to radiation**, are biologically plausible but largely extend the existing AML use rather than representing true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myeloid leukemia (multiple subtypes, per the knowledge graph; no approved-indication text available in the US license record) |
| Predicted New Indication | Bulbar polio (top-ranked) |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (NDA 211192 is listed as cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, ivosidenib is an inhibitor of mutant IDH1. It lowers 2-hydroxyglutarate in IDH1-mutant cancers.

**Bulbar polio (rank 1):** Bulbar polio is a viral infection of motor neurons caused by poliovirus. No plausible mechanistic link to mutant IDH1 inhibition was identified. The very high score (0.993) is a knowledge-graph prediction only and most likely reflects network artifacts rather than biology. This prediction is not considered credible without independent supporting evidence.

**Therapy-related myeloid neoplasms (ranks 2 and 3):** AML/MDS related to alkylating agents and AML/MDS related to radiation are biologically plausible targets. These diseases can carry IDH1 mutations, which ivosidenib targets. Therapy-related AML/MDS and other AML entities already appear among the drug's original indications. Benefit would depend on IDH1 mutation status. These predictions are best viewed as an extension of the existing AML use rather than distinct new indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indications.

---

## Literature Evidence

Currently no related literature available for the predicted indications.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 211192 | TIBSOVO (Servier Pharmaceutical LLC), status: cancelled | Tablet, film coated | Not available in the compiled data |

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

- **Drug Interactions:** The interaction query returned 100 interacting drugs. The 20 shown in the data compiled for this report include:
  - **Major:** Aprepitant, Clarithromycin, Dolasetron, Palonosetron, Cisapride, Granisetron, Levofloxacin
  - **Moderate:** Famotidine, Loperamide, Bisacodyl, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Saxagliptin, Eliglustat, Linagliptin, Sodium sulfate, Castor oil, Glycerin, Lactitol, Lactulose

  Several Major interactions involve antiemetics (5-HT3 antagonists) and QT-prolonging drugs. Pharmacodynamic QT interactions should be reviewed carefully.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (bulbar polio) has no supporting trials or literature, and no plausible mechanism. The high score is likely a knowledge-graph artifact.
- The two plausible predictions (therapy-related AML/MDS) are mainly extensions of the existing AML use, are classified as research questions, and also lack specific trial or literature evidence.
- The US license record shows only a cancelled NDA, and package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- For therapy-related AML/MDS: IDH1 mutation prevalence in these populations, and a review of existing IDH1-mutant AML/MDS trial subgroups
- Clarification of the current US market status, since the only NDA is listed as cancelled
- For bulbar polio: no further investment is recommended unless an independent biological rationale emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

