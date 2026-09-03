---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 1124
evidence_level: L5
indication_count: 10
---

# Riluzole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Riluzole: From No Approved Indication in Taiwan to Amyotrophic Lateral Sclerosis

## One-Sentence Summary

Riluzole (DrugBank DB00740) is not currently licensed for marketing in Taiwan, and no approved indication is on file in this dataset. Among the 10 candidate indications the TxGNN model returned, only one — **Amyotrophic Lateral Sclerosis (ALS)** — is backed by substantial literature (20 publications identified, all mechanistic/review-level), while the remaining 9 candidates, including the model's numerically top-ranked prediction, have zero clinical trial or literature support and carry a "Hold" or "Research Question" status. This report therefore focuses on ALS as the only actionable candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — riluzole has no approved indication recorded in the Taiwan regulatory dataset |
| Predicted New Indication | Amyotrophic Lateral Sclerosis (susceptibility to) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data from DrugBank is not available in this record. However, the evidence pack's own literature and rationale fields describe riluzole as a **glutamate-release inhibitor and voltage-gated sodium-channel blocker**, producing anti-excitotoxic neuroprotection of motor neurons.

Because no original indication is on file for the Taiwan market, this is less a case of "repurposing from A to B" than a case of **the knowledge graph independently recovering riluzole's globally established therapeutic role for ALS**, even though the local dataset has no record of it. Multiple reviews in the evidence pack state this directly — e.g., "just one medication, riluzole, has been shown to modestly prolong survival" in ALS (PMID 21128691), and "riluzole remains the only drug with proven efficacy" (PMID 19593125).

Mechanistically this fits: glutamate-mediated excitotoxicity is one of the three major recognized pathophysiological mechanisms of motor neuron injury in ALS (the "glutamate hypothesis," PMID 9178165). Riluzole's anti-excitotoxic action directly targets this pathway, which is why the prediction is biologically coherent rather than incidental.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack. (Note: the pivotal Phase 3 trials establishing riluzole's ALS efficacy — Bensimon 1994 and Lacomblez 1996 — are industry-recognized but are not captured as structured trial records in this dataset; see "Next Steps" below.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | Riluzole is the only medication shown to modestly prolong ALS survival; overview of ALS pathophysiology and management |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Review | Current Opinion in Neurology | Despite intensive research, riluzole "remains the only drug with proven efficacy" in ALS |
| [20942785](https://pubmed.ncbi.nlm.nih.gov/20942785/) | 2010 | Review | CNS Neurol Disord Drug Targets | Riluzole extends ALS survival by 2–3 months; discusses genetic determinants as future therapeutic targets |
| [22646982](https://pubmed.ncbi.nlm.nih.gov/22646982/) | 2011 | Review | Expert Opin Drug Discov | Riluzole is the only approved ALS drug, improving survival by 2–3 months; reviews preclinical drug discovery efforts |
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | Journal of Neurology | Establishes the "glutamate hypothesis" of motor neuron injury as a core ALS pathomechanism |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Rev Mol Med | Reviews proposed ALS mechanisms (excitotoxicity, oxidative stress, mitochondrial dysfunction) and treatment pathways |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Review | CNS Neurol Disord Drug Targets | Reviews ALS diagnosis, pathogenesis, and therapeutic targets |
| [20698807](https://pubmed.ncbi.nlm.nih.gov/20698807/) | 2011 | Review | Amyotroph Lateral Scler | Riluzole (glutamate-pathway drug) is the only agent improving survival; critiques trial methodology across ALS studies |
| [31108504](https://pubmed.ncbi.nlm.nih.gov/31108504/) | 2019 | Basic Research | Human Molecular Genetics | iPSC-derived motor neuron study; notes riluzole minimally extends life expectancy via inhibition of glutamatergic transmission and calcium overload |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | Preclinical Study | Neuroreport | Early study showing riluzole's neuroprotective effect against ALS CSF-mediated excitotoxic neuronal death |

---

## Other Predicted Indications (Lower Priority)

The remaining candidates from this TxGNN run lack clinical or literature evidence and are not recommended for action at this time:

| Disease | TxGNN Score | Evidence Level | Recommendation |
|---------|------------|-----------------|-----------------|
| Bilateral parasagittal parieto-occipital polymicrogyria (rank 1 by score) | 99.99% | L5 | Hold — no mechanistic or evidentiary link |
| Axial spondylometaphyseal dysplasia | 99.99% | L5 | Hold — no mechanistic or evidentiary link |
| Lower motor neuron syndrome, late-adult onset | 99.99% | L4 | Research Question — plausible mechanism, no direct evidence |
| Trichomegaly–retina pigmentary degeneration–dwarfism syndrome | 99.99% | L5 | Hold — no mechanistic or evidentiary link |
| Lethal arthrogryposis–anterior horn cell disease syndrome | 99.99% | L5 | Hold — mechanism direction plausible but population mismatch |
| Monomelic amyotrophy (Hirayama disease) | 99.99% | L4 | Research Question — plausible mechanism, no direct evidence |
| Mills syndrome | 99.98% | L4 | Research Question — plausible mechanism, no direct evidence |
| Autosomal dominant mitochondrial myopathy with exercise intolerance | 99.98% | L5 | Hold — no mechanistic or evidentiary link |
| Amyotrophic lateral sclerosis type 22 | 99.98% | L4 | Research Question — same disease family as ALS, no subtype-specific evidence |

---

## Taiwan Market Information

Riluzole currently holds **no marketing authorization in Taiwan** (0 licenses on file; market status: 未上市 / Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not yet available in this dataset — see Next Steps.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Literature consistently and independently confirms riluzole's anti-excitotoxic mechanism aligns with ALS's core pathophysiology, and riluzole is globally recognized as the standard (if modestly effective) treatment for ALS — yet it is currently unregistered in Taiwan. The other 9 model-generated predictions in this dataset have no supporting evidence and should not be pursued.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank — currently a High-severity data gap (DG002)
- Structured clinical trial records for the pivotal ALS trials (Bensimon 1994, Lacomblez 1996) currently missing from this evidence pack
- Drug-drug interaction profile
- A regulatory pathway assessment for Taiwan market entry, given riluzole's established international approval status for ALS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

