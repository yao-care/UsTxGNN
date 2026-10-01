---
layout: default
title: Dactinomycin
parent: Model Prediction Only (L5)
nav_order: 564
evidence_level: L5
indication_count: 9
---

# Dactinomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Dactinomycin: From Cytotoxic Chemotherapy to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin is a cytotoxic DNA-binding chemotherapy agent, marketed in the US as generic lyophilized injection.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but **0 clinical trials** and **0 publications** were found for this pairing, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of Licenses | 5 (all ANDAs; ANDA203385 appears twice) |
| Recommended Decision | Hold |

The supplied US label records contain no approved-indication text, so the original indication is not listed here.

## Why is This Prediction Reasonable?

Dactinomycin intercalates into DNA and inhibits DNA-dependent RNA synthesis, which makes it broadly cytotoxic. No MS-specific mechanism was supplied.

The link between the original use (cancer chemotherapy) and MS is weak. MS is a chronic, non-malignant immune-mediated disease. The only conceivable rationale is a general immunosuppressive or anti-proliferative effect on activated immune cells, and that is a hypothesis, not something the supplied data support. Any such benefit would also have to be weighed against the marked toxicity of a cytotoxic agent in a chronic disease. The high score (0.996) reflects the model's network-based inference only and should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA203385 | Dactinomycin | Lyophilized powder for injection | Eugia US LLC |
| ANDA203999 | Dactinomycin | Lyophilized powder for injection | XGen Pharmaceuticals DJB, Inc. |
| ANDA207232 | Dactinomycin | Lyophilized powder for injection | Hisun Pharmaceuticals USA, Inc. |
| ANDA213463 | Dactinomycin | Lyophilized powder for injection | Meitheal Pharmaceuticals Inc. |

All products are injectable only. No oral or other route is available, and route compatibility for MS has not been assessed.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA intercalator; antitumour antibiotic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function (hepatopathy and veno-occlusive disease have been reported with dactinomycin-containing regimens), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug in the query.
- **Hepatic signal (from supplied literature in other indications)**: Several papers report hepatopathy and veno-occlusive disease with vincristine/dactinomycin/cyclophosphamide, with younger age as a risk factor. This is relevant to any expansion of use.

Please refer to the package insert for warnings and contraindications, which were not available in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The MS prediction is L5. It has no trials, no literature and no mechanistic link beyond general cytotoxicity, and the drug's toxicity profile is a poor fit for a chronic non-malignant disease.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- A drug-specific MOA entry from DrugBank
- Preclinical or clinical evidence linking dactinomycin to MS pathophysiology, plus a risk-benefit argument against existing MS therapies

**Note on other predictions in this Evidence Pack:** The rhabdomyosarcoma entries are far better supported than MS. Parameningeal embryonal rhabdomyosarcoma is graded L2 (provisional, pending full-text confirmation), with a "Proceed with Guardrails" recommendation. There, dactinomycin is a backbone drug in cooperative-group VAC-based regimens, not the variable tested. Prioritising those candidates over MS is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

