---
layout: default
title: Eptifibatide
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
monitor_inn: "EPTIFIBATIDE"
predicted_indications: ["rheumatoid arthritis", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin d disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hemoglobinopathy", "female breast carcinoma", "beta-thalassemia with other manifestations", "partial deletion of the short arm of chromosome 16"]
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Hemoglobinopathy (Sickle Cell Disease)

## One-Sentence Summary

Eptifibatide is an injectable platelet inhibitor originally used to treat acute coronary syndrome.
Among the 10 predicted new indications, the best-supported is **hemoglobinopathy (mainly sickle cell disease)**, backed by **1 clinical trial** (Phase 1/2, terminated early) and **4 publications**.
The evidence is early and does not establish efficacy.

*Note: The first-ranked TxGNN prediction is rheumatoid arthritis, but it has no trials or literature. This report focuses on hemoglobinopathy, the prediction with the most direct evidence, and briefly compares the other candidates.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (from the knowledge graph; the US licenses contain no indication text) |
| Predicted New Indication | Hemoglobinopathy (sickle cell disease); the top-ranked prediction by score is rheumatoid arthritis |
| TxGNN Prediction Score | 99.98% for hemoglobinopathy (rheumatoid arthritis: 99.99%) |
| Evidence Level | L2 (hemoglobinopathy; the single Phase 1/2 trial was terminated and is underpowered) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 (all cancelled; these are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, eptifibatide is a glycoprotein IIb/IIIa (alpha-IIb-beta-3 integrin) antagonist. It blocks the final common pathway of platelet aggregation, which is why it works in acute coronary syndrome.

Platelet activation and GP IIb/IIIa-mediated adhesion are also thought to contribute to **vaso-occlusion and inflammation in sickle cell disease**. Blocking this pathway could, in theory, reduce the occlusion that drives painful crises. This is the logic behind the early clinical studies in sickle cell patients.

The mechanistic link is plausible, but efficacy is not established. Bleeding risk is a key concern in this population.

**Other predicted indications (all Hold):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Rheumatoid arthritis | 99.99% | L5 | Platelet involvement in synovial inflammation is plausible but indirect; no trials or literature |
| Other sickle cell genotypes (HbSE, S-beta-thal, HbSD, HPFH-sickle, HbSC) | 99.98% | L5 (HbSC: L4) | Extrapolated from sickle cell studies; the one paper listed for HbSC is an ACS tolerability study of unclear relevance |
| Female breast carcinoma | 99.97% | L4 | In vitro and organ-on-chip studies only; no clinical oncology data |
| Beta-thalassemia with other manifestations | 99.97% | L5 | Conceptually plausible (hypercoagulable state); no data |
| Partial deletion of the short arm of chromosome 16 | 99.96% | L5 | Likely a knowledge-graph artifact (alpha-globin deletion); not a plausible target |

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Terminated | 13 | Randomized, double-blind, placebo-controlled study of eptifibatide safety and effect during acute pain episodes in sickle cell disease. Underpowered because of early termination, so it cannot show efficacy. It is still the most direct clinical evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase I study | Br J Haematol | Safety and pharmacodynamics of eptifibatide in 4 sickle cell anaemia patients in a steady, non-crisis state. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot clinical study | Thromb Res | Evaluated safety and efficacy of eptifibatide in SCD patients during acute painful episodes. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Secondary / biomarker analysis | Am J Hematol | Effect of eptifibatide on inflammation during acute pain episodes in SCD. |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In vitro model | J Clin Invest | Microfluidic model of microvascular occlusion and thrombosis in hematologic diseases such as SCD. |

---

## US Market Information

All seven authorizations are generic ANDAs with a cancelled status. No approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206127 (Eugia US LLC) | Eptifibatide | Injection | Not recorded |
| ANDA208554 (Baxter Healthcare) | Eptifibatide | Injection | Not recorded |
| ANDA203258 (Mylan Institutional) | Eptifibatide | Injection, solution | Not recorded |
| ANDA213081 (Avenacy Inc.) | Eptifibatide | Injection, solution | Not recorded |
| ANDA213599 (Meitheal Pharmaceuticals) | Eptifibatide | Injection, solution | Not recorded |

*Two further cancelled ANDAs (Sagent, ANDA204693; Slate Run, ANDA209864) are not shown.*

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: thrombocytopenia, blood coagulation disease, impaired renal function disease.
- **Drug Interactions** (100 interactions found; main ones shown):
  - **Major**: deferasirox, ibritumomab tiuxetan, tositumomab (I-131)
  - **Moderate**: acetylsalicylic acid, dexfenfluramine, fenfluramine, sibutramine
  - Many other interactions have an unclassified level (for example proton pump inhibitors, morphine, simvastatin, prednisone).
- **Bleeding risk** is a key concern in sickle cell populations, as noted in the rationale for the hemoglobinopathy prediction.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct clinical evidence is a small, terminated Phase 1/2 trial (13 patients) plus early pilot and Phase I studies in sickle cell disease. Efficacy is not shown, bleeding risk is a concern, and no US licenses are currently valid. The other predictions are computational only or preclinical.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Full results and the reason for early termination of NCT00834899, along with the efficacy and bleeding outcomes from the pilot study (PMID 23973010)
- A bleeding-risk mitigation plan for sickle cell patients, especially those with thrombocytopenia, coagulation disorders, or renal impairment
- Review of the route of administration (injectable only) for a chronic or recurrent condition
- Clarification of the current US market and supply situation, since all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

