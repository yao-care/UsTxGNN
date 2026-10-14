---
layout: default
title: Levetiracetam
parent: Moderate Evidence (L3-L4)
nav_order: 850
evidence_level: L4
indication_count: 10
---

# Levetiracetam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levetiracetam: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is an antiseizure medication originally used to treat **partial epilepsy**.
The TxGNN model predicts it may be effective for **visual epilepsy** (seizures triggered by visual stimuli) with a very high score. However, **no clinical trials** are registered for this indication, and none of the **20 publications** retrieved addresses it specifically. The prediction therefore rests mainly on the drug's general antiseizure activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (0 active licenses, 12 cancelled) |
| Number of NDAs | 12 (all generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Levetiracetam binds to synaptic vesicle protein 2A (SV2A) and modulates neurotransmitter release. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from the retrieved literature. Reducing excitatory neurotransmitter release is plausibly relevant to seizures that are triggered by visual stimuli, such as photosensitive seizures.

Partial epilepsy and visual epilepsy are both epileptic seizure disorders, and levetiracetam is an established antiseizure drug. This likely explains the very high TxGNN score. The retrieved papers, however, cover neonatal seizures, seizure prophylaxis in neurocritical care, post-stroke seizures and adverse effects. None of them tests levetiracetam in visual epilepsy, so the mechanistic link remains an extrapolation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The papers below are the most relevant of the 20 retrieved. They concern general seizure management rather than visual epilepsy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam versus phenobarbital for neonatal seizures |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet. Neurology | PEACH trial: prophylactic levetiracetam to prevent early seizures after intracerebral haemorrhage, double-blind and placebo-controlled |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT (open label) | Seizure | Phenytoin versus levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in neurocritical care |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Network meta-analysis | Neurology | Comparison of antiseizure medications for post-stroke seizures |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalized epilepsy |
| [40975024](https://pubmed.ncbi.nlm.nih.gov/40975024/) | 2025 | Meta-analysis | Clinical Neurology and Neurosurgery | Levetiracetam versus phenobarbitone for neonatal seizures |
| [39899098](https://pubmed.ncbi.nlm.nih.gov/39899098/) | 2025 | Review | Continuum | First seizures, acute repetitive seizures and status epilepticus |
| [35848684](https://pubmed.ncbi.nlm.nih.gov/35848684/) | 2022 | Case report | Journal of Postgraduate Medicine | Levetiracetam-induced gingival hyperplasia in a 14-year-old |
| [28755154](https://pubmed.ncbi.nlm.nih.gov/28755154/) | 2018 | Report | Acta Neurologica Belgica | Levetiracetam-induced hyponatremia |

---

## US Market Information

All 12 US licenses are cancelled and none is currently active. The five below are listed as examples. The source record does not give approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090261 (Mylan Pharmaceuticals) | Levetiracetam | Tablet, film coated | Not specified in the source record |
| ANDA090515 (Quallent Pharmaceuticals Health) | Levetiracetam | Tablet, film coated | Not specified in the source record |
| ANDA091491 (Cranbury Pharmaceuticals) | Levetiracetam | Tablet | Not specified in the source record |
| ANDA091261 (Golden State Medical Supply) | Levetiracetam | Tablet, film coated, extended release | Not specified in the source record |
| ANDA201157 (PAI Pharma) | Levetiracetam | Solution | Not specified in the source record |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug–disease links, not package insert text): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, liver disease, gallbladder disease, psychotic disorder, schizophreniform disorder, mental disorder, schizoaffective disorder, neutropenia, agranulocytosis, leukopenia, pancytopenia, anxiety and depersonalization disorder.
- **Drug interactions:** 100 interactions were found. The moderate-level ones include morphine (including liposomal), dronabinol, metoclopramide, nabilone, opium and sibutramine. These mostly involve additive central nervous system effects. Many other entries have an unknown severity level.
- **Adverse effects in the retrieved literature:** gingival hyperplasia, hyponatremia, and seizure aggravation (reported in some users).

Please refer to the package insert for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high TxGNN score is not backed by any trial or specific publication for visual epilepsy. The evidence is L4, and the retrieved literature concerns other seizure settings. The US licenses are all cancelled, and the package insert safety data are missing.

Among the other model predictions, **status epilepticus** has far stronger support. It has Phase 3 RCT evidence, including ESETT (NCT01960075, n=478, PMID 31774955) and an IV levetiracetam plus clonazepam trial (NCT01150331, n=203). **Startle epilepsy** has small open-label and case-report evidence. These are better candidates for further evaluation than visual epilepsy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking data gap)
- Detailed mechanism-of-action data
- Targeted evidence for levetiracetam in photosensitive or visually triggered epilepsy, such as controlled studies using photic stimulation
- A decision on whether to prioritize status epilepticus, given its stronger evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

