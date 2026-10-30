---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 1242
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "TOPIRAMATE"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Topiramate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Topiramate
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

## Topiramate: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Topiramate is an antiseizure medication, originally used for generalized tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, with a score of 0.9970, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a computational prediction only. The data compiled for this report support more strongly a group of related reflex epilepsies, which are discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of FDA Applications | 10 (all ANDAs, all listed as cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, topiramate is a broad-spectrum antiseizure drug acting through voltage-gated sodium channel blockade, enhancement of GABA-A activity, antagonism of AMPA/kainate glutamate receptors, and weak carbonic anhydrase inhibition.

These mechanisms explain its effect on seizures, but they do not address tumor biology. There is no known mechanistic rationale for treating a neoplasm of the trigeminal nerve. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as neurological terms like trigeminal neuralgia, not biological evidence of a real anti-tumor effect. The prediction should be treated as a hypothesis with no supporting evidence at present.

**Other predictions in the same list.** The ranked predictions include eight reflex or stimulus-triggered seizure types, which are much more plausible because they fall within the epilepsy spectrum topiramate already treats:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|

Among these, **thinking seizures** has the strongest indirect support, because the retrieved Cochrane systematic reviews (for example PMID 24570033 and 31642054) cover topiramate add-on therapy in drug-resistant focal epilepsy. That support carries over from approved indications and is not specific to this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm. No clinical trials were found for any of the other predicted indications either.

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

For reference, the strongest literature found for the top-ranked epilepsy-related predictions (not specific to the predicted indications) is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24570033](https://pubmed.ncbi.nlm.nih.gov/24570033/) | 2014 | Systematic review (Cochrane, RCTs) | Cochrane Database Syst Rev | Topiramate add-on therapy in drug-resistant partial epilepsy |
| [31642054](https://pubmed.ncbi.nlm.nih.gov/31642054/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Topiramate add-on therapy in drug-resistant focal epilepsy |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic review / network meta-analysis | J Neurol | Comparison of antiseizure medications in idiopathic generalized epilepsies |
| [39854828](https://pubmed.ncbi.nlm.nih.gov/39854828/) | 2025 | Review / consensus | Epilepsy Behav | Antiseizure medications for Lennox-Gastaut syndrome, including topiramate |
| [34817852](https://pubmed.ncbi.nlm.nih.gov/34817852/) | 2021 | Cochrane review | Cochrane Database Syst Rev | Topiramate for juvenile myoclonic epilepsy |
| [35421622](https://pubmed.ncbi.nlm.nih.gov/35421622/) | 2022 | Review | Seizure | Molecular mechanisms of topiramate and its clinical value in epilepsy |
| [10666508](https://pubmed.ncbi.nlm.nih.gov/10666508/) | 2000 | Preclinical | Eur J Pharmacol | Topiramate antagonized audiogenic seizures in DBA/2 mice and potentiated other anticonvulsants |
| [12581224](https://pubmed.ncbi.nlm.nih.gov/12581224/) | 2003 | Preclinical | Epilepsia | Topiramate effects in GAERS and audiogenic Wistar AS rat models |

## US Market Information

All 10 US authorizations in the compiled records are generic applications (ANDAs) with status "cancelled". No approved indication text is available in these records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078235 | Topiramate (Zydus Pharmaceuticals USA) | Tablet, film coated | Not available |
| ANDA090278 | Topiramate (Proficient Rx) | Tablet, film coated | Not available |
| ANDA216683 | Topiramate (Advagen Pharma) | Capsule | Not available |
| ANDA207382 | Topiramate (Zydus Pharmaceuticals USA) | Capsule, extended release | Not available |
| ANDA090162 | Topiramate (A-S Medication Solutions) | Tablet, film coated | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

- **Knowledge-graph contraindication signals** (not label text): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, diarrheal disease, ocular hypertension, nephrolithiasis (including susceptibility caused by SLC26A1), acute urate nephropathy, acidosis disorder, metabolic acidosis, amnestic disorder, retrograde amnesia.
- **Drug interactions:** 100 interactions were found in the database query. Examples of **Major** interactions include metformin, and anticholinergic agents such as hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline and trospium. **Moderate** interactions include pioglitazone, glyburide, morphine, dronabinol, nabilone, phentermine, metoclopramide, phenylbutyric acid and glycerol phenylbutyrate.
- **Literature-reported safety observations:** a safety review of the double-blind studies (PMID 9706735) noted renal stones among the observed effects, and case reports describe psychotic or manic exacerbation. Pregnancy-related complications are also discussed in the literature (PMID 40716154).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, has a very high model score but no clinical trials, no literature and no plausible mechanism, so it is a computational prediction only (L5). The related reflex epilepsy predictions are mechanistically plausible but rest on indirect, class-level evidence, and the best of them (thinking seizures) is L3 at most.

**To proceed, the following is needed:**
- Mechanism of action data and package insert warnings and contraindications (both are currently missing)
- For trigeminal nerve neoplasm: any biological rationale or preclinical data; otherwise deprioritise
- For the reflex epilepsies: indication-specific case series or trials, and consideration of whether these are clinically distinct enough from already-approved epilepsy indications to merit a separate development path
- Clarification of current US marketing status, since all licenses in the compiled records are listed as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

