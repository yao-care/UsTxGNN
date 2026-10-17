---
layout: default
title: Riluzole
parent: Model Prediction Only (L5)
nav_order: 1124
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Riluzole: predicted new indication Bilateral parasagittal parieto-occipital polymicrogyria (evidence level L5). Approved use: Amyotrophic lateral sclerosis"
monitor_inn: "RILUZOLE"
predicted_indications: ["bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome", "autosomal dominant mitochondrial myopathy with exercise intolerance", "amyotrohpic lateral sclerosis type 22"]
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole is a drug originally used to treat amyotrophic lateral sclerosis (ALS).
The TxGNN model predicts it may be effective for **bilateral parasagittal parieto-occipital polymicrogyria**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amyotrophic lateral sclerosis |
| Predicted New Indication | Bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all listed authorizations are cancelled) |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From general knowledge, riluzole is thought to act by reducing glutamate release and modulating persistent sodium currents. This is the basis for its modest survival benefit in ALS.

Polymicrogyria is a cortical malformation, which is often associated with epilepsy and neurodevelopmental problems. A glutamate-modulating drug could plausibly relate to such conditions, but this link is speculative. No trial or publication in the data directly supports it. The high TxGNN score (99.99%) reflects a knowledge-graph association only and should not be read as clinical evidence.

Other top-ranked predictions are closer to riluzole's original use, such as lower motor neuron syndrome with late-adult onset, monomelic amyotrophy, Mills syndrome, and genetic ALS subtypes. They are more biologically plausible by analogy to ALS, but they also have no direct trials or literature in the data. Several others, such as axial spondylometaphyseal dysplasia and trichomegaly-retina pigmentary degeneration-dwarfism syndrome, show no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the eighth-ranked prediction, "amyotrophic lateral sclerosis, susceptibility to", has literature. It overlaps with riluzole's original indication, so it is not a true repurposing case. Selected records:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42161327](https://pubmed.ncbi.nlm.nih.gov/42161327/) | 2026 | Cohort/Association study | Brain | CYP2D6 variants studied in relation to ALS risk and survival. Notes that riluzole's survival benefit is modest and variable between patients |
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | J Neurol | Glutamate excitotoxicity hypothesis in ALS, the mechanistic basis for riluzole |
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | ALS pathophysiology and management. Riluzole is the only medication shown to modestly prolong survival |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Rev Mol Med | Proposed ALS mechanisms (oxidative stress, excitotoxicity, mitochondrial dysfunction) and routes to treatment |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | Preclinical | Neuroreport | Neuroprotective effects of riluzole against ALS cerebrospinal fluid toxicity in cultured neurons |
| [32040174](https://pubmed.ncbi.nlm.nih.gov/32040174/) | 2020 | Modelling study | Toxicol Sci | DILIsym modelling of liver effects of a sublingual riluzole formulation vs 50 mg oral tablets. About 50% of ALS patients on oral tablets have ALT above the upper limit of normal |

These records are indirect evidence. They do not show efficacy for the predicted new indication.

## US Market Information

All six authorizations are cancelled. No approved-indication text is available in the data.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA204048 | Riluzole (Ascend Laboratories) | Tablet | Cancelled |
| ANDA091417 | Riluzole (Sun Pharmaceutical) | Tablet, film coated | Cancelled |
| ANDA091394 | Riluzole (Glenmark) | Tablet, film coated | Cancelled |
| ANDA206045 | Riluzole (AvKARE) | Tablet, film coated | Cancelled |
| NDA209080 | TIGLUTIK (EDW Pharma) | Liquid | Cancelled |

A sixth entry, Teglutik (EDW Pharma, liquid), is also cancelled and has no valid authorization number.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** neutropenia, agranulocytosis, substance abuse/dependence, hyperbilirubinemia, hereditary hyperbilirubinemia, Gilbert syndrome, interstitial lung disease, and drug-induced liver injury.
- **Liver safety:** A modelling study reports that about 50% of ALS patients on oral riluzole have ALT above the upper limit of normal, 8% above 3× ULN, and 2% above 5× ULN.
- **Drug Interactions:** 44 interactions were identified. Examples at Moderate level include obeticholic acid, naltrexone, deferasirox, osilodrostat, anagrelide, asparaginase, brentuximab vedotin, clofarabine, methotrexate, and epirubicin. Minor-level examples include omeprazole, caffeine, theophylline, and aminophylline.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for bilateral parasagittal parieto-occipital polymicrogyria is supported only by a model score. There are no trials or literature, and the mechanistic link is speculative. All US authorizations are also cancelled. The more plausible candidates are the ALS-related motor neuron conditions, which could be framed as research questions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Preclinical or case-level evidence of riluzole's effect in cortical malformation or epilepsy models
- Review of the higher-plausibility ALS-spectrum candidates (lower motor neuron syndrome, monomelic amyotrophy, Mills syndrome) as separate research questions
- Clarification of current US availability, since all listed authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

