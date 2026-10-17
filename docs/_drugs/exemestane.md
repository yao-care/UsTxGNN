---
layout: default
title: Exemestane
parent: Moderate Evidence (L3-L4)
nav_order: 689
evidence_level: L4
indication_count: 7
monitor_inn: "EXEMESTANE"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura"]
last_modified_at: 2026-10-14
description: "Exemestane: predicted new indication Amenorrhea (evidence level L4). Approved use: Not available in the compiled data"
---

# Exemestane
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Exemestane: From Breast Cancer to Amenorrhea

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor that lowers estrogen levels. Its original approved indication is not listed in the data compiled for this report.
The TxGNN model predicts it may be effective for **Amenorrhea**, the highest-ranked prediction that has any supporting literature.
There are **0 clinical trials** and **5 publications** (1 cohort study, 4 reviews). These papers describe amenorrhea as a treatment-related state, not a condition that exemestane treats, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Amenorrhea (the top-ranked prediction is antithrombin deficiency type 2, which has no evidence at all) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all listings cancelled) |
| Number of NDAs | 7 (1 NDA and 6 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, exemestane is a steroidal aromatase inhibitor that blocks the conversion of androgens to estrogens and so lowers circulating estradiol.

This is where the prediction becomes questionable. Amenorrhea is a consequence of estrogen and ovarian function suppression, so it is a pharmacological effect of exemestane and not something it would treat. The retrieved papers discuss chemotherapy-induced amenorrhea, ovarian suppression and ovarian function recovery in premenopausal breast cancer patients. In these papers amenorrhea is an outcome or a treatment-related state. The direction of effect (induction rather than treatment) argues against repurposing for this indication.

The other predictions are weaker still. The thrombophilia cluster (antithrombin deficiency type 2, factor 5 excess, heparin cofactor 2 deficiency and thrombophilia) has no clinical or literature support and no plausible mechanism. These scores most likely come from graph propagation. Aromatase inhibitors also carry a thromboembolic risk signal in breast cancer, so the safety direction is a concern. The migraine predictions have only a speculative link through estrogen fluctuation, and estrogen depletion could plausibly worsen headaches.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohort | Annals of Oncology | Incidence and predictors of ovarian function recovery in breast cancer patients with chemotherapy-induced amenorrhea who switched from tamoxifen to exemestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Review | Oncology (Williston Park) | Role of ovarian suppression in premenopausal women with hormone receptor-positive early breast cancer; chemotherapy-induced amenorrhea is linked to improved survival |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Review | Journal of Clinical Oncology | Oncology Grand Rounds on whether estradiol monitoring is needed in women receiving ovarian suppression for breast cancer |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Review | Recenti Progressi in Medicina | Current role of LHRH analogs in premenopausal breast cancer; ovarian suppression raises outcomes by lowering estrogen |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klinicka Onkologie | Aromatase inhibitor treatment in postmenopausal breast cancer and ways to manage side effects; contraindicated in women with functional ovaries |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020753 | Aromasin | Tablet | Not available |
| ANDA209208 | Exemestane (Upsher-Smith) | Tablet | Not available |
| ANDA210323 | Exemestane (Cipla USA) | Tablet | Not available |
| ANDA216454 | Exemestane (NorthStar Rx) | Film-coated tablet | Not available |
| ANDA213547 | Exemestane (Florida Pharmaceutical Products) | Film-coated tablet | Not available |

All 7 listings are cancelled. Two further ANDAs (Zydus, Breckenridge) are not shown above.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (steroidal aromatase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs, and the 20 shown to us include two rated Moderate: **dexamethasone** and **troglitazone**. The rest are rated Unknown, including pantoprazole, morphine, metformin, omeprazole, simvastatin, aspirin and rosuvastatin.
- **Other considerations**: Aromatase inhibitors carry a thromboembolic risk signal in breast cancer, which matters for the thrombophilia predictions. Estrogen depletion may also alter headache patterns, which matters for the migraine predictions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN scores are very high (99.8%), but there are no clinical trials and the only literature is indirect. Amenorrhea is an effect of exemestane, not a condition it treats, and the thrombophilia and migraine predictions have no plausible mechanism and raise safety concerns.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text, which is missing from the license records
- Clarification of whether amenorrhea could have any therapeutic rationale, or whether this prediction should be discarded
- Any direct clinical or mechanistic evidence for the other predicted indications before reconsidering them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

