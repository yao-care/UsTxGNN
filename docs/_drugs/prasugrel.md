---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 1075
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is an oral P2Y12 platelet inhibitor. The retrieved literature describes it as used after percutaneous coronary intervention (PCI) in acute coronary syndrome (ACS), although the US licence records in the data have no indication text.
The TxGNN model ranks **pulmonary hypertension** as its top prediction, but **no retrieved clinical trial or paper actually tests prasugrel in this disease**.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data. Retrieved literature places prasugrel in ACS patients undergoing PCI |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 (the listed licences are all generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Prasugrel is a thienopyridine prodrug that irreversibly blocks the platelet P2Y12 receptor, which reduces platelet activation and aggregation. Its established use is preventing thrombosis after coronary stenting.

The proposed link to pulmonary hypertension is that platelet activation and in-situ thrombosis are thought to contribute to pulmonary vascular remodeling. This is plausible in theory, but it is **speculative**. The pack contains no study of prasugrel or any other P2Y12 inhibitor in pulmonary hypertension, and the graph score is the only support.

**A better-supported direction in the same pack is migraine, especially migraine with patent foramen ovale (PFO).** A retrospective review of thienopyridines (PMID 30478066) and an open-label ticagrelor pilot (PMID 30478067) suggest antiplatelet therapy may reduce migraine symptoms in these patients. The evidence is class-level, not prasugrel-specific, and is graded L3 (Research Question). It is discussed here as context and is not the primary prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study of how many cancer-associated thrombosis patients would be ineligible for the CARAVAGGIO trial. Not about prasugrel or pulmonary hypertension |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Cross-sectional study of NOAC management in elderly Spanish patients with atrial fibrillation. Unrelated to prasugrel or pulmonary hypertension |

Both trials were graded low relevance (C). Neither provides evidence for this prediction.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | Registry analysis of how pre-infection drug therapy for comorbidities relates to COVID-19 outcomes. Not specific to prasugrel or pulmonary hypertension |
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Factors associated with clopidogrel use and adherence in ACS patients after PCI. Mentions prasugrel only as a guideline-recommended alternative |

Neither paper studies prasugrel in pulmonary hypertension.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA213315 | Prasugrel (Unichem Pharmaceuticals) | Film-coated tablet | Not provided in the data |
| ANDA205913 | Prasugrel (Amneal Pharmaceuticals) | Film-coated tablet | Not provided in the data |
| ANDA205897 | Prasugrel (Apotex Corp.) | Film-coated tablet | Not provided in the data |

The pack reports 18 licences in total. Only 3 unique authorizations appear in the list (two were duplicated). All are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction is supported only by a high model score (99.88%). No relevant trial or publication was retrieved, and the mechanistic link is speculative. The Evidence Pack does not include package insert warnings or contraindications, so safety screening cannot start.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, obtained from the FDA label
- Mechanism of action data (for example from DrugBank) to support the mechanistic analysis
- Preclinical or clinical evidence specific to prasugrel in pulmonary hypertension, since none was retrieved
- A separate evaluation of the migraine/PFO direction, including prasugrel-specific efficacy and bleeding risk, since it has the strongest indirect support in this pack

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

