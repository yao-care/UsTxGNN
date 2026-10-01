---
layout: default
title: Biotin
parent: Moderate Evidence (L3-L4)
nav_order: 461
evidence_level: L4
indication_count: 2
---

# Biotin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Biotin: From Vitamin Supplement to Dyspepsia

## One-Sentence Summary

Biotin (vitamin B7) is a nutritional cofactor sold in the US mostly as supplement and homeopathic-type products. The TxGNN model predicts it may help with **dyspepsia**, but the supporting evidence is thin. The 2 registered clinical trials found are unrelated to dyspepsia, and the 7 publications are mostly indirect (case report, observational studies, a multi-ingredient supplement study).

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no approved indication text is listed for the US products in the supplied data. Biotin is generally known as a cofactor for carboxylase enzymes involved in cellular metabolism, including in the gut lining. Deficiency has been reported in an infant with dyspepsia who was fed only an amino acid formula (PMID 15863846). That report shows a link between digestive problems, restricted diets, and biotin status. It does not show that biotin treats dyspepsia.

The mechanistic link is plausible but indirect. The high model score (0.994) is not backed by any biotin-specific study in dyspepsia. A second prediction, gastroparesis (score 99.42%), has no clinical trials or literature at all, so it rests on model output alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin patches after bariatric surgery, measuring serum micronutrient levels. Not about dyspepsia. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs pregabalin for preemptive postoperative analgesia. Does not involve biotin or dyspepsia. |

Both trials were graded as low relevance (Grade C) and provide no efficacy evidence for dyspepsia.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical study (design unverified) | Minerva Gastroenterol Dietol | Open multicentre study of a multi-ingredient food supplement in functional dyspepsia after H. pylori treatment. Biotin-specific effect not established. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | J Dermatol | Biotin deficiency (skin lesions, low serum and urine biotin) in an infant diagnosed with dyspepsia at birth and fed only amino acid formula. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review/other | Eksperimental'naia i klinicheskaia gastroenterologiia | A prebiotic-plus-vitamin supplement (including biotin) for gut microbiota disorders in patients on antibiotics. Indirect. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Stomach antral endocrine cells in 76 irritable bowel syndrome (IBS) patients versus healthy controls. No biotin data. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endosc | Endocrine cells in the stomach's oxyntic mucosa in IBS patients. No biotin data. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney Int | Small bowel T cells and stress proteins in IgA nephropathy. Indirect. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | J Clin Pathol | Interleukin 10 in H. pylori-associated gastritis. Indirect. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| Not listed | Biotin Drops | Liquid | Professional Complementary Health Formulas |
| Not listed | Biotitum (4 listings) | Pellet | Hahnemann Laboratories, Inc. |

The supplied data lists 20 licenses in total, and the 5 shown here are the main ones. Other listed forms include solution and aerosol foam. No approved indication text is provided for any of them.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no study shows that biotin treats dyspepsia. The two trials are unrelated, and the literature consists of a case report, observational studies, and a multi-ingredient supplement study. The evidence is at the L4 level, and the safety and mechanism data are incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the relevant US products, which is a blocking gap for safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Biotin-specific clinical or mechanistic studies in dyspepsia, since the current supplement study cannot separate biotin's effect from the other ingredients
- Route and formulation compatibility assessment, since current US products are mainly liquid, pellet, solution, and foam forms
- A decision on whether to keep gastroparesis as a candidate, given that it currently has no evidence beyond the model prediction

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

