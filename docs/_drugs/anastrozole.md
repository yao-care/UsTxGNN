---
layout: default
title: Anastrozole
parent: Model Prediction Only (L5)
nav_order: 348
evidence_level: L5
indication_count: 5
monitor_inn: "ANASTROZOLE"
predicted_indications: ["neuroblastoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "monocytic leukemia"]
last_modified_at: 2026-11-24
description: "Anastrozole: predicted new indication neuroblastoma (evidence level L5). In the US: 21 FDA applications (10 active)"
---

# Anastrozole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Anastrozole: aromatase inhibitor → neuroblastoma (neuroblastoma)
{: .text-alpha }

## One-Sentence Summary

Anastrozole is an aromatase inhibitor, a hormone-lowering drug with a marketed oral tablet form in the United States.
The TxGNN model predicts it may be relevant to **neuroblastoma** with a score of 0.9953, but **no clinical trials and no publications** currently support this prediction.
This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | neuroblastoma |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 10 of 21) |
| Number of FDA Applications | 21 (active: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for anastrozole: "The growth of many cancers of the breast is stimulated or maintained by estrogens. In postmenopausal women, estrogens are mainly derived from the action of the aromatase enzyme, which converts adrenal androgens (primarily androstenedione and testosterone) to estrone and estradiol. […] Anastrozole is a selective non-steroidal aromatase inhibitor." ([DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de), label version 2026-03-02; accessed 2026-11-19.) Anastrozole belongs to the aromatase inhibitor class, which lowers estrogen production.

Neuroblastoma is a childhood tumour arising from neural crest cells and is not typically driven by estrogen. No clear mechanistic link between aromatase inhibition and neuroblastoma was identified. The high score reflects a computational pattern only, and it should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA078058 | ANASTROZOLE | TEVA PHARMS | Tablet; oral | Valid |
| ANDA078921 | ANASTROZOLE | ZYDUS PHARMS USA INC | Tablet; oral | Valid |
| ANDA078944 | ANASTROZOLE | KENTON | Tablet; oral | Valid |
| ANDA079220 | ANASTROZOLE | NATCO PHARMA LTD | Tablet; oral | Valid |
| ANDA090568 | ANASTROZOLE | ACCORD HLTHCARE | Tablet; oral | Valid |

Showing 5 of 21 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

The list may be partial; further records exist beyond those shown (NDA020541, ARIMIDEX, is also on file).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (aromatase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were retrieved, all with an unspecified severity level. Examples include bupropion, pantoprazole, glimepiride, morphine, metformin, omeprazole, rosiglitazone, simvastatin, prednisone and acetylsalicylic acid. Their clinical significance needs to be checked.
- **Other recorded cautions**: Relations with myocardial ischemia and coronary artery disease are recorded as contraindication-type signals in the data compiled for this report. They are not taken from label text and need confirmation against the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high score but no supporting trials or literature, and no plausible mechanism links aromatase inhibition to neuroblastoma. The evidence level is L5.

**To proceed, the following is needed:**
- Preclinical evidence, such as cell or animal studies, showing an effect on neuroblastoma
- A defined mechanistic hypothesis for aromatase inhibition in this tumour
- Package insert warnings and contraindications, and mechanism of action data
- A safety review for paediatric use, since neuroblastoma mainly affects children

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

