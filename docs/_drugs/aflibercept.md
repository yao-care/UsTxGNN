---
layout: default
title: Aflibercept
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 1
monitor_inn: "AFLIBERCEPT"
predicted_indications: ["esotropia"]
last_modified_at: 2026-11-12
description: "Aflibercept: predicted new indication Esotropia (evidence level L5). Approved use: Metastasis from malignant tumor of colon"
---

# Aflibercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Aflibercept: From Metastatic Colon Cancer and Retinal Disease to Esotropia
{: .text-alpha }

## One-Sentence Summary

Aflibercept is a recombinant fusion protein that blocks VEGF, originally used for metastatic colorectal cancer and retinal diseases such as macular degeneration, diabetic macular edema, and retinal artery occlusion.
The TxGNN model predicts it may be effective for **esotropia**, but **no clinical trials and no publications** currently support this direction. This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastasis from malignant tumor of colon; macular degeneration; retinal artery occlusion; diabetic macular edema |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 0.9938 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 9 of 9) |
| Number of FDA Applications | 9 (active: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for aflibercept: "Vascular endothelial growth factor-A (VEGF-A) and placental growth factor (PlGF) are members of the VEGF family of angiogenic factors that can act as mitogenic, chemotactic, and vascular permeability factors for endothelial cells. VEGF acts via two receptor tyrosine kinases, VEGFR-1 and VEGFR-2, present on the surface of endothelial cells. […] Aflibercept products act as a soluble decoy receptor that binds VEGF - A and PlGF, and thereby can inhibit the binding and activation of these cognate VEGF receptors." ([DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06), label version 2026-10-29; accessed 2026-11-19.) Based on general pharmacology, aflibercept traps VEGF-A, VEGF-B, and placental growth factor (PlGF), which reduces abnormal blood vessel growth and vascular leakage. This is why it is used in retinal vascular diseases and in colorectal cancer.

The link to esotropia is weak. Esotropia is a form of strabismus (inward eye turning) caused by neuromuscular, refractive, or accommodative factors. The data compiled for this report establish no direct biological connection between VEGF inhibition and these causes. One possible indirect link is that anti-VEGF agents are used in retinal diseases, such as retinopathy of prematurity, which can co-occur with or lead to secondary strabismus. That would be a link to a comorbidity, not a treatment effect on esotropia, and it remains speculative.

The high TxGNN score (0.9938) reflects a model-based computational association. It should not be read as evidence of clinical efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin us-lic-20261106-aflibercept-1 -->

> **Review correction (2026-11-06)**: Originally stated: "A sixth license, BLA125418 (ZALTRAP, solution concentrate, sanofi-aventis U.S. LLC), is also listed as valid. All 6 licenses are valid in the compiled data." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 9 FDA applications or NDC listings for this drug, 9 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-aflibercept-1 -->

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA125387 | EYLEA | REGENERON PHARMACEUTICALS | Injectable; injection | Valid |
| BLA125418 | ZALTRAP | SANOFI AVENTIS US | Injectable; injection | Valid |
| BLA761274 | YESAFILI | BIOCON BIOLOGICS INC | Injectable; injection | Valid |
| BLA761298 | PAVBLU | AMGEN INC | Injectable; injection | Valid |
| BLA761350 | OPUVIZ | SAMSUNG BIOEPIS CO LTD | Injectable; injection | Valid |

Showing 5 of 9 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF fusion protein), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions:** The interaction screening completed and identified **78 interacting drugs**. Examples of the interactions rated **Major** include:
- Deferiprone
- Samarium (153Sm) lexidronam
- Adalimumab
- Baricitinib
- Certolizumab pegol
- Cladribine
- Clozapine

Examples rated **Moderate** include strontium chloride Sr-89, roflumilast, chloramphenicol (systemic and ophthalmic), zidovudine, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, and several vaccines (tetanus toxoid, anthrax, live cholera).

Only a subset of the 78 interactions is shown here. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trials or publications support aflibercept for esotropia, and no direct mechanistic link between VEGF inhibition and esotropia is established. In addition, the drug is marketed in the US, and label-based safety data are missing.

<!-- review:begin us-lic-20261106-aflibercept-2 -->

> **Review correction (2026-11-06)**: Originally stated: "In addition, the drug is marketed in the US with all 6 licenses valid, and label-based safety data are missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The FDA data list 9 FDA applications or NDC listings for this drug, 9 active; the Quick Overview and the table under US Market Information show the current figures. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-aflibercept-2 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or mechanistic evidence linking VEGF signalling to esotropia or its causes
- A literature and trial search for anti-VEGF use in strabismus and retinopathy of prematurity–related strabismus
- Clarification of current US licensing and market status
- Assessment of route compatibility, since intravitreal or intravenous injection may not suit a strabismus indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "A sixth license, BLA125418 (ZALTRAP, solution concentrate, sanofi-aventis U.S. LLC), is also listed as valid. All 6 licenses are valid in th" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with all 6 licenses valid" | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

