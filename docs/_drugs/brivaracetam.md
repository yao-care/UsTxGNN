---
layout: default
title: Brivaracetam
parent: Model Prediction Only (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
monitor_inn: "BRIVARACETAM"
predicted_indications: ["visual epilepsy", "status epilepticus", "audiogenic seizures", "micturation-induced seizures", "thinking seizures", "eating seizures", "startle epilepsy", "orgasm-induced seizures", "beta-ketothiolase deficiency", "adolescent/adult onset autosomal dominant epilepsy with auditory features"]
---

# Brivaracetam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Brivaracetam: From Partial Epilepsy to Status Epilepticus

## One-Sentence Summary

Brivaracetam is an antiseizure medicine originally used to treat partial (focal) epilepsy.
The TxGNN model predicts it may be effective for **Status Epilepticus** (the highest-ranked prediction with clinical evidence; the top-scoring prediction overall is visual epilepsy, which has no trials),
with **1 clinical trial** and **19 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy / partial motor epilepsy (the US label text for the licenses was not available) |
| Predicted New Indication | Status epilepticus (selected from the 10 predictions because it has the strongest evidence; the rank 1 prediction is visual epilepsy) |
| TxGNN Prediction Score | 99.40% (visual epilepsy, rank 1: 99.51%) |
| Evidence Level | L3 (systematic reviews and observational or registry data; no completed Phase 3 RCT) |
| US Market Status | Cancelled only (all 10 licenses are listed as cancelled) |
| Number of NDAs | 10 licenses in total (2 NDAs and 8 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The literature does describe brivaracetam as a high-affinity ligand of synaptic vesicle protein 2A (SV2A), with 15- to 30-fold higher affinity than levetiracetam. Binding to SV2A is thought to reduce synaptic vesicle release and neuronal hyperexcitability.

Status epilepticus is a prolonged or repeated seizure emergency, and it is closely related to the focal seizures for which brivaracetam is already used. Brivaracetam crosses the blood-brain barrier quickly and has an intravenous formulation, which suits acute seizure termination. Systematic reviews of IV brivaracetam in status epilepticus report efficacy and tolerability, but they draw mainly on observational and case-series data.

Other predictions are weaker:
- **Visual epilepsy** (highest score) has no trials. The link to brivaracetam is indirect and inferred from the shared seizure mechanism.
- **Audiogenic seizures** are supported only by animal-model studies.
- **Rare reflex epilepsies** (micturition-induced, thinking, eating, startle and orgasm-induced seizures) have no specific evidence.
- **Beta-ketothiolase deficiency** is a metabolic disorder whose seizures are secondary to ketoacidosis. SV2A modulation does not address the enzyme defect, so this prediction is not plausible.
- **Adolescent/adult onset autosomal dominant epilepsy with auditory features** is a genetic focal epilepsy, so a symptomatic benefit is plausible, but there are no specific studies.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) | NA | Completed | 152 | Compares IV brivaracetam with levetiracetam in children with status epilepticus. Results were not provided, and the design and outcomes need verification. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41838218](https://pubmed.ncbi.nlm.nih.gov/41838218/) | 2026 | Systematic review | J Neurol | Brivaracetam as a potential treatment for status epilepticus. Its efficacy and safety profile remains inadequately characterized. |
| [32278203](https://pubmed.ncbi.nlm.nih.gov/32278203/) | 2020 | Systematic review | J Neurol Sci | IV brivaracetam may be an alternative anticonvulsant in status epilepticus. Controlled studies are sparse, which limits recommendation. |
| [31342405](https://pubmed.ncbi.nlm.nih.gov/31342405/) | 2019 | Systematic review | CNS Drugs | Reviews IV brivaracetam in status epilepticus. Its high brain permeability and rapid onset suit emergency use. |
| [32822230](https://pubmed.ncbi.nlm.nih.gov/32822230/) | 2020 | Guideline/Review | Epilepsy Curr | American Epilepsy Society review of parenteral antiseizure drugs for refractory convulsive status epilepticus. |
| [31260101](https://pubmed.ncbi.nlm.nih.gov/31260101/) | 2019 | Registry | Epilepsia | Multicenter registry on IV brivaracetam use in status epilepticus. |
| [33561784](https://pubmed.ncbi.nlm.nih.gov/33561784/) | 2021 | Retrospective study | Seizure | Italian multicenter study of the use, effectiveness and adverse events of IV brivaracetam in status epilepticus. |
| [41043236](https://pubmed.ncbi.nlm.nih.gov/41043236/) | 2025 | Real-world study | Epilepsy Behav | Efficacy of switching from IV to oral brivaracetam after status epilepticus and cluster seizures. |
| [32480279](https://pubmed.ncbi.nlm.nih.gov/32480279/) | 2020 | Case report/series | Seizure | Brivaracetam in absence status epilepticus. |
| [36528008](https://pubmed.ncbi.nlm.nih.gov/36528008/) | 2023 | Review | Epilepsy Behav | Compares brivaracetam and levetiracetam in status epilepticus using the photosensitivity model. |
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | RCT (Phase 3) | Epilepsia Open | Adjunctive brivaracetam in adult Asian patients with focal-onset seizures. This supports the original indication, not status epilepticus. |

## US Market Information

All 10 licenses are listed as cancelled, and the data compiled for this report do not include approved indication text. The five listed below are examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205836 | Briviact (UCB, Inc.) | Film-coated tablet | Not available |
| NDA205838 | Briviact (UCB, Inc.) | Solution | Not available |
| ANDA214921 | Brivaracetam (Novadoz) | Film-coated tablet | Not available |
| ANDA218249 | Brivaracetam (Hainan Poly Pharm) | Injection | Not available |
| ANDA214875 | Brivaracetam (Apotex) | Tablet | Not available |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 69 records. The 20 retrieved records are mostly moderate or minor in severity.
  - Moderate: morphine (including liposomal), opium, ethanol, promethazine, metoclopramide, dronabinol, nabilone, difenoxin, diphenoxylate, sibutramine and clopidogrel. Many of these are central nervous system depressants, so additive sedation is a practical concern.
  - Minor: proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole), chlorpropamide, tolbutamide and cilostazol.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Status epilepticus is the best-supported prediction. Several systematic reviews, registry data and one completed pediatric trial point the same way, and brivaracetam has an IV formulation and rapid brain penetration. However, there is no completed Phase 3 RCT, so the evidence stays at L3. The other predictions are research questions (visual epilepsy and audiogenic seizures, L4) or should be held (the remaining reflex and genetic epilepsies, L5, and beta-ketothiolase deficiency, which is mechanistically implausible).

**To proceed, the following is needed:**
- Verify the design and results of NCT07163572 (the phase is listed as NA, and no results were provided).
- A well-designed randomized controlled trial of IV brivaracetam in status epilepticus.
- FDA package insert warnings and contraindications, which are currently missing and block formal safety screening.
- Detailed mechanism of action data from DrugBank.
- Clarify the regulatory position. All US licenses are currently cancelled, so product availability and regulatory pathway need to be confirmed.
- A plan for monitoring additive sedation when brivaracetam is combined with central nervous system depressants in an acute-care setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

