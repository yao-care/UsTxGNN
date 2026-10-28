---
layout: default
title: Secnidazole
parent: Model Prediction Only (L5)
nav_order: 1148
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Secnidazole: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). Approved use: Bacterial vaginosis, trichomoniasis, giardiasis, vaginitis, vulvitis…"
monitor_inn: "SECNIDAZOLE"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vaginal discharge", "vulvar neoplasm", "trichomonal vulvovaginitis", "leukoplakia of vagina", "vulvovaginal candidiasis"]
---

# Secnidazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Secnidazole: From Bacterial Vaginosis and Trichomoniasis to Postmenopausal Atrophic Vaginitis
{: .text-alpha }

## One-Sentence Summary

Secnidazole is a 5-nitroimidazole antimicrobial, originally used to treat bacterial vaginosis, trichomoniasis, giardiasis and related vaginal and vulvar infections.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial vaginosis, trichomoniasis, giardiasis, vaginitis, vulvitis, vulvovaginitis |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Secnidazole belongs to the 5-nitroimidazole class. In anaerobic bacteria and protozoa, its nitro group is reduced to radicals that damage DNA. Its efficacy in bacterial vaginosis and trichomoniasis is established.

The mechanistic link to the predicted indication is weak. Postmenopausal atrophic vaginitis is driven mainly by estrogen deficiency rather than infection. An antimicrobial would not be expected to address the underlying cause. The high score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, such as the approved vaginitis and vulvovaginitis indications, not biological evidence or a true therapeutic relationship. This prediction should therefore be treated as a model artifact until shown otherwise.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209363 | Solosec (status: valid) | Granule | Not specified in the compiled data |

## Safety Considerations

- **Drug Interactions**: 92 interactions were identified. All of those listed are rated Moderate. Main ones include:
  - Other nitroimidazoles: metronidazole, tinidazole
  - Statins: simvastatin, atorvastatin, rosuvastatin
  - Cardiac and neurological drugs: amiodarone, levodopa
  - Oncology agents: paclitaxel, cabazitaxel, carboplatin, bortezomib, carfilzomib, brentuximab vedotin, trastuzumab emtansine
  - Others: adalimumab, certolizumab pegol, auranofin, picosulfuric acid, radioactive iodide (I-123, I-131)

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no plausible mechanism, since atrophic vaginitis is hormone-driven rather than infectious. The product's only US license is cancelled.

Other predictions in the same data are better supported, though they largely extend existing indications rather than being true repurposing:
- **Vaginal discharge** (score 0.9941, L1, Proceed with Guardrails): supported by a completed Phase 3 placebo-controlled trial in trichomoniasis (NCT03935217, n=147), a Phase 3 trial in bacterial vaginosis (PMID 28867602), and a meta-analysis of single-dose secnidazole in bacterial vaginosis (PMID 31129560).
- **Trichomonal vulvovaginitis** (score 0.9937, L1, Proceed with Guardrails): supported by a Phase 3 randomized trial (PMID 33768237).
- **Ulceration of vulva, vulvar neoplasm, leukoplakia of vagina** (all L5, Hold): no evidence and no plausible mechanism.
- **Vulvovaginal candidiasis** (L3, Research Question): secnidazole has no direct antifungal activity, and the only clinical signal comes from a fluconazole combination trial.

**To proceed, the following is needed:**
- Preclinical or clinical rationale for any non-infectious benefit in atrophic vaginitis, compared against standard estrogen-based therapy
- Package insert warnings and contraindications
- Detailed mechanism of action data
- Confirmation of product availability, given the cancelled US license
- A DDI screening plan, including the alcohol and disulfiram-type precautions common to nitroimidazoles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

