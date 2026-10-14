---
layout: default
title: Baclofen
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist, described in the published literature as a treatment for spasticity. The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but this rests on the model score alone: **0 clinical trials** are registered, and none of the **9 retrieved publications** studies baclofen in ADHD.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spasticity (from published literature; the data compiled for this report contain no approved-indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 11 (all generic ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Baclofen is known to be a GABA-B receptor agonist. A plausible but unproven link to ADHD is that GABA-B activation modulates the balance of cortical excitation and inhibition and dopaminergic signalling, both of which are relevant to impulsivity.

The retrieved literature gives no direct support for this link. It deals mainly with Tourette syndrome and tic treatment, where ADHD is a common comorbidity. It also includes preclinical rodent studies on noradrenergic, hippocampal, habenular and cingulate circuits involved in impulsive decision-making. Even the one baclofen-related tic report is indirect, and it does not address ADHD symptoms. The TxGNN score is therefore the main support for this prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications tests baclofen in ADHD. They are listed because they provide indirect context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | International Review of Neurobiology | Emerging treatment strategies for Tourette syndrome, a condition often accompanied by ADHD and OCD |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Clinical features and management of Tourette syndrome, including tic suppression and comorbid psychiatric illness |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic review/meta-analysis | Cureus | Behavioural intervention, antipsychotics and alpha agonists for tics in Tourette syndrome (not baclofen-specific) |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | Journal of Child Neurology | Reports 450 patients with tics/Tourette syndrome treated with baclofen/botulinum toxin A and rated with the Yale Global Tic Severity Scale; does not address ADHD |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Preclinical (rat EEG) | Brain Research | EEG responses to neurotransmitter agonists in a rat model of ADHD versus a model of epilepsy |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical (rat) | Psychopharmacology | α2A-adrenergic stimulation in the ventral hippocampus reduces impulsive decision-making (guanfacine) |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical practice report | L'Encéphale | Supervised off-label methylphenidate prescribing in adult ADHD (not baclofen) |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Preclinical (rat) | European Journal of Neuroscience | Habenula function is necessary for social play behaviour |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Preclinical (rat) | Neuropsychopharmacology | Roles of the anterior cingulate cortex and basolateral amygdala in cognitive effort decisions, relevant to ADHD |

## US Market Information

All 11 US licenses (10 oral tablets and 1 injection) are listed as cancelled, and none is currently valid. No approved-indication text is available for any of them. The five main licenses are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|-----------|------|
| ANDA209102 | Baclofen | Tablet | Direct_Rx | Cancelled |
| ANDA211659 | Baclofen | Tablet | A-S Medication Solutions | Cancelled |
| ANDA214374 | Baclofen | Tablet | Rising Pharma Holdings, Inc. | Cancelled |
| ANDA217324 | Baclofen | Injection | Advagen Pharma Limited | Cancelled |
| ANDA215885 | Baclofen | Tablet | Major Pharmaceuticals | Cancelled |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** The TxGNN knowledge graph links baclofen to the following conditions through contraindication edges:
  - epilepsy
  - kidney disease
  - psychotic and schizophrenia-spectrum disorders (including schizoaffective and schizophreniform disorders)
  - stroke and cerebrovascular disorders, including cerebral infarction
  - autonomic nervous system disease, including autonomic dysreflexia and Horner syndrome
  - pyoureter
  - disease of the neck of the urinary bladder

  Epilepsy and psychiatric disorders matter especially for an ADHD population, where comorbidity is common.
- **Drug interactions:** 100 interaction records were found.
  - **Major:** morphine, including liposomal morphine.
  - **Moderate:** dronabinol, nabilone, metoclopramide, opium, sibutramine, difenoxin and diphenoxylate.
  - The remaining records are of unknown severity, for example pantoprazole, omeprazole, metformin and glimepiride.

For label warnings and full contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.32%), but it is not backed by any registered clinical trial or any publication that tests baclofen in ADHD. The indirect literature concerns Tourette syndrome and rodent models. All US licenses are also cancelled, and the knowledge graph flags epilepsy and psychotic disorders as contraindication signals.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence of baclofen's effect on ADHD symptoms or impulsivity
- Detailed mechanism-of-action data linking GABA-B agonism to ADHD pathophysiology
- The current package insert warnings and contraindications, to complete the safety screen
- A safety plan for ADHD patients with comorbid epilepsy or psychiatric illness
- Consideration of the second-ranked prediction, **nicotine dependence** (TxGNN score 99.19%). It has three registered Phase 2 trials in smokers (one completed, two terminated early) and supporting preclinical studies, so it has stronger evidence (L2) than ADHD.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

