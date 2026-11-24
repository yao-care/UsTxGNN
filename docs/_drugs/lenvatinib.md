---
layout: default
title: Lenvatinib
parent: Moderate Evidence (L3-L4)
nav_order: 846
evidence_level: L3
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "LENVATINIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax", "endocrine-cerebro-osteodysplasia syndrome"]
description: "Lenvatinib: predicted new indication Liposarcoma (evidence level L3). In the US: 2 FDA applications (2 active)"
---

# Lenvatinib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
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

## Lenvatinib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Lenvatinib is an oral multi-kinase inhibitor that blocks VEGFR1-3, FGFR1-4, PDGFRα, RET and KIT.
The TxGNN model predicts it may be effective for **liposarcoma**, and the supporting evidence is **1 completed single-arm Phase Ib/II trial** and **1 matching publication** (evidence level L3), with no randomized trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L3 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Lenvatinib inhibits several receptor tyrosine kinases involved in angiogenesis and tumour-stroma signalling (VEGFR1-3, FGFR1-4, PDGFRα, RET, KIT). Blocking these pathways may suppress the blood supply and growth signals that sarcomas depend on. This description rests on the known target profile. According to the Mechanism of Action section of the FDA-approved prescribing information for lenvatinib: "Lenvatinib is a kinase inhibitor that inhibits the kinase activities of vascular endothelial growth factor (VEGF) receptors VEGFR1 (FLT1), VEGFR2 (KDR), and VEGFR3 (FLT4). Lenvatinib inhibits other kinases that have been implicated in pathogenic angiogenesis, tumor growth, and cancer progression in addition to their normal cellular functions, including fibroblast growth factor (FGF) receptors FGFR1, 2, 3, and 4; platelet derived growth factor receptor alpha (PDGFRA), KIT, and RET." ([DailyMed: Lenvima (lenvatinib) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4bedd21-efde-44c6-9d9c-b48b78d7ed1e), label version 2026-10-14; accessed 2026-11-19.)

Eribulin, a microtubule inhibitor, is already used in liposarcoma, and preclinical work showed that eribulin combined with agents of different mechanisms has broad antitumour activity. Combining it with an anti-angiogenic kinase inhibitor such as lenvatinib is therefore a reasonable strategy. Because the clinical data come from a combination study without a randomized comparison, lenvatinib's own contribution cannot be separated from eribulin's.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | LEADER study: single-arm test of lenvatinib plus eribulin in inoperable or metastatic adipocytic sarcoma and leiomyosarcoma, assessing safety and efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II single-arm trial | Clin Cancer Res | Lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma, where treatment options are limited (LEADER study) |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/biomarker study | Exp Hematol Oncol | CDK4 as a prognostic biomarker in soft tissue sarcoma; CDK4 inhibition has a synergistic effect in dedifferentiated liposarcoma |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical study | Anticancer Res | Eribulin shows broad antitumour activity in combination with agents of differing mechanisms |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Rep Oncol | Marked tumour shrinkage in a patient with dedifferentiated liposarcoma and lung metastasis given individualized multimodal treatment |

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA213092 | LENVATINIB | SUN PHARM INDS INC | Capsule; oral | Valid |
| NDA206947 | LENVIMA | EISAI INC | Capsule; oral | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Major-level examples include dolasetron and cisapride. Moderate-level examples include clarithromycin, levofloxacin, granisetron, palonosetron, famotidine, loperamide, naltrexone and several laxatives or bowel-preparation agents (bisacodyl, polyethylene glycol, magnesium citrate, lactulose). Metronidazole is rated minor. Several of these are linked to QT-interval concerns or electrolyte disturbance, so combined use needs review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The only direct clinical evidence is one completed single-arm Phase Ib/II study (30 patients) of lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma, so the evidence level is L3. There is no randomized trial, and the contribution of lenvatinib alone is not isolated.

**To proceed, the following is needed:**
- A randomized comparison, for example lenvatinib plus eribulin versus eribulin alone in liposarcoma
- Reported efficacy and safety results from the completed LEADER study
- Package insert warnings and contraindications
- A drug-interaction and monitoring plan, particularly for QT-prolonging agents

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "A formal mechanism-of-action entry was not available in the data compiled for this report, so this description rests on the known target profile" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Lenvima (lenvatinib) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4bedd21-efde-44c6-9d9c-b48b78d7ed1e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

