---
layout: default
title: Nelarabine
parent: Model Prediction Only (L5)
nav_order: 960
evidence_level: L5
indication_count: 1
monitor_inn: "NELARABINE"
predicted_indications: ["relapsing-remitting multiple sclerosis"]
last_modified_at: 2026-10-14
description: "Nelarabine: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L5). Approved use: Acute lymphoblastic/lymphocytic leukemia…"
---

# Nelarabine
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

# Nelarabine: From T-Cell Acute Lymphoblastic Leukemia to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine was originally used to treat T-cell acute lymphoblastic leukemia and T-lymphoblastic lymphoma.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output and mechanistic analogy alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic/lymphocytic leukemia, precursor T-cell acute lymphoblastic leukemia, T-cell leukemia, T-lymphoblastic lymphoma |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 10 authorizations are cancelled) |
| Number of NDAs | 10 (1 NDA and 9 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nelarabine is a prodrug of ara-G, a deoxyguanosine analog. It is converted to ara-GTP and incorporated into DNA, causing preferential cytotoxicity in T-lymphoblasts.

Relapsing-remitting multiple sclerosis is driven in part by pathogenic autoreactive lymphocytes. Selectively depleting lymphocytes is the same rationale behind cladribine, a purine analog approved for MS. This gives the prediction a plausible mechanistic basis.

However, this link is inferred by analogy and from the high TxGNN score (0.994), not from direct evidence. A major concern is that nelarabine carries a boxed warning for severe neurologic toxicity (somnolence, neuropathy, demyelination, Guillain-Barré-like syndromes). This is a serious problem in a demyelinating CNS disease and may argue against use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The 10 US authorizations are all injectable products and all currently have cancelled status. Approved indication text was not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021877 | Arranon | Injection | Sandoz Inc |
| ANDA216038 | Nelarabine | Injection | Meitheal Pharmaceuticals Inc |
| ANDA215037 | Nelarabine | Injection | Zydus Lifesciences Limited |
| ANDA216934 | Nelarabine | Injection | Dr. Reddy's Laboratories, Inc. |
| ANDA212605 | Nelarabine | Injection | Gland Pharma Limited |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph links nelarabine to neutropenia, thrombocytopenia, anemia and agranulocytosis. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver and renal function, bilirubin, and neurologic status |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: Liver failure, epilepsy, thrombocytopenia, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, anemia, macrocytic anemia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), impaired renal function, learning disability, intellectual disability, demyelinating disease, and inflammatory demyelinating polyradiculoneuropathy. The demyelinating disease signals are particularly relevant to multiple sclerosis.
- **Drug Interactions**: 100 interactions were found in total. Major-level interactions in the data shown include bupropion, deferiprone, iopamidol, iohexol, and samarium (153Sm) lexidronam. Moderate-level interactions include metronidazole, tinidazole, secnidazole, benznidazole, chloroquine, hydroxychloroquine, disulfiram, rosuvastatin, simvastatin, palifermin, strontium chloride Sr-89, lindane, and bowel preparations (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).
- **Boxed warning (from pharmacological knowledge, not the compiled data)**: Severe neurologic toxicity. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5). Nelarabine's known neurotoxicity, including demyelination, and the knowledge-graph contraindication with demyelinating disease run directly against use in multiple sclerosis. All US authorizations are also currently cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data to support the mechanistic link analysis
- Preclinical evidence (for example, an EAE model) showing benefit in autoimmune demyelination
- A neurotoxicity risk assessment specific to a demyelinating CNS disease population
- Comparison against cladribine, which has an established MS indication and a more suitable safety profile
- Route and formulation compatibility assessment (nelarabine is injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

