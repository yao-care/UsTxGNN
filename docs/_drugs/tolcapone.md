---
layout: default
title: Tolcapone
parent: Model Prediction Only (L5)
nav_order: 1239
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "TOLCAPONE"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome", "paralysis agitans, juvenile, of Hunt"]
description: "Tolcapone: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tolcapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Tolcapone: Rasmussen subacute encephalitis
{: .text-alpha }

## One-Sentence Summary

Tolcapone is an oral COMT inhibitor, originally used for Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tolcapone is known as a catechol-O-methyltransferase (COMT) inhibitor. It is used as an add-on to levodopa in Parkinson disease, where it prolongs the action of dopamine-related therapy. Detailed mechanism of action data is not available in the data compiled for this report, so this description relies on general knowledge of the drug class.

Rasmussen encephalitis is a chronic, inflammatory and probably autoimmune brain disease. Based on the data compiled, no plausible link between COMT inhibition and this pathology can be established. The high TxGNN score (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or clinical validation. The prediction should be regarded as a hypothesis only.

For context, the other top predictions also lack trial or literature support. Two are worth noting:
- **Lewy body dementia** (score 0.9964): shares dopaminergic and alpha-synuclein pathology with Parkinson disease, so there is a plausible indirect rationale. The only publication is a preclinical organoid study, which did not test tolcapone.
- **Paralysis agitans, juvenile, of Hunt** (score 0.9952): a juvenile parkinsonian syndrome that may largely overlap with existing labeled indications rather than representing true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Rasmussen subacute encephalitis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA020697 | Tolcapone (Oceanside Pharmaceuticals) | Tablet, film coated | Valid |
| ANDA208937 | Tolcapone (Ingenus Pharmaceuticals, LLC) | Tablet | Valid |

Approved indication text was not available for either authorization. Neither is currently valid.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): liver disease, gallbladder disease, melanoma, hypotensive disorder, rhabdomyolysis, nodular fasciitis, tardive dyskinesia, lingual-facial-buccal dyskinesia.
- **Drug Interactions**: 65 interactions were identified. The most notable:
  - **Major**: methylene blue
  - **Moderate**: epinephrine (including ophthalmic and topical forms), morphine (including liposomal), opium, codeine, dronabinol, nabilone, naltrexone, metoclopramide, promethazine, chlorpheniramine, cetirizine, dextromethorphan, ethanol
  - **Minor**: warfarin, dicoumarol
  - **Unknown severity**: omeprazole

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Safety signals (liver disease, among others) further argue against advancing without supporting data.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical or mechanistic evidence linking COMT inhibition to Rasmussen encephalitis pathology
- Consideration of a better-supported candidate, such as Lewy body dementia, as a research question
- Review of the cancelled US licensing status and its reasons
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

