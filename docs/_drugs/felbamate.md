---
layout: default
title: Felbamate
parent: Model Prediction Only (L5)
nav_order: 695
evidence_level: L5
indication_count: 2
monitor_inn: "FELBAMATE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
last_modified_at: 2026-10-28
description: "Felbamate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (partial epilepsy, Lennox-Gastaut syndrome)"
---

# Felbamate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Felbamate: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Felbamate is an antiepileptic drug originally used to treat epilepsy, including partial seizures and Lennox-Gastaut syndrome.
The TxGNN model ranks **Trigeminal Neuralgia** as the most clinically meaningful new indication (the top-ranked prediction, trigeminal nerve neoplasm, has no supporting evidence and is not mechanistically credible).
Support for trigeminal neuralgia is thin: **0 registered clinical trials** and **4 publications**, only one of which (a 1995 case report) directly addresses the drug in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial epilepsy, Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal neuralgia (the top-ranked prediction, trigeminal nerve neoplasm, is discussed below) |
| TxGNN Prediction Score | 0.9918 (trigeminal neuralgia); 0.9962 (trigeminal nerve neoplasm) |
| Evidence Level | L5 (trigeminal neuralgia); L5 (trigeminal nerve neoplasm) |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of NDAs | 8 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on what is known about the drug, felbamate is an antiepileptic that modulates NMDA receptors (glycine-site antagonism) and potentiates GABA-A receptors. Sodium-channel modulation is also described in the available analysis.

**Trigeminal neuralgia.** This condition causes sudden, severe, one-sided facial pain attacks that resemble seizures in their timing. This similarity led to the discovery that several anticonvulsants work against it. Carbamazepine is the drug of choice, and oxcarbazepine, lamotrigine, baclofen, phenytoin and valproate are also used. Felbamate's mechanisms are plausibly relevant to neuropathic pain, which makes the prediction reasonable on mechanistic grounds.

**Trigeminal nerve neoplasm.** This is the highest-scoring prediction (0.9962), but it is purely computational. No mechanism links felbamate to antitumour activity. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (such as trigeminal neuralgia), not biological evidence. At most, felbamate might relieve tumour-associated facial pain, which is not tumour-directed treatment. It is not evaluated further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either trigeminal neuralgia or trigeminal nerve neoplasm.

---

## Literature Evidence

Publications identified for trigeminal neuralgia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Case report | Clin J Pain | Reports that felbamate relieved trigeminal neuralgia; the analgesic efficacy of this anticonvulsant was evaluated in the condition |
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Review | CNS Drugs | Drug-choice guide for trigeminal neuralgia: carbamazepine is the drug of choice, with baclofen, phenytoin and valproate also effective |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Preclinical (animal study) | Indian J Pharmacol | Compared carbamazepine, gabapentin and lamotrigine for neuropathic pain in rats; notes felbamate among antiepileptics reported effective in neuropathic pain and trigeminal neuralgia |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Case report (safety) | Ann Pharmacother | Reports delayed anaphylaxis associated with felbamate |

No publications were found for trigeminal nerve neoplasm.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020189 | Felbatol (Viatris Specialty LLC) | Tablet | Not listed (valid) |
| ANDA208970 | Felbamate (Zydus Lifesciences) | Tablet | Not listed (valid) |
| ANDA201680 | Felbamate (Amneal Pharmaceuticals) | Tablet | Not listed (valid) |
| ANDA207093 | Felbamate (Taro Pharmaceuticals U.S.A.) | Tablet | Not listed (valid) |
| ANDA211333 | Felbamate (Novitium Pharma) | Suspension | Not listed (valid) |

Eight authorizations are on record in total, and all are cancelled. The table shows five of them.

---

## Safety Considerations

- **Key Warnings**: Felbamate carries serious boxed-warning risks, namely aplastic anemia and hepatic failure, according to the analysis compiled for this report. A published case report also describes delayed anaphylaxis.
- **Contraindications (from the knowledge graph, not label text)**: long QT syndrome (including familial form), torsades de pointes, liver failure, liver disease, kidney disease, hematologic disease, aplastic anemia (including idiopathic), gallbladder disease, porphyria (inherited porphyria and porphyrin metabolism disease), anxiety disorder, neurotic disorder, dysthymic disorder, and pyoureter.
- **Drug Interactions**: 100 interactions were identified; the 20 reviewed are all of Moderate severity. Examples include morphine (including liposomal), opium, naltrexone, naloxegol, aprepitant, rolapitant, metoclopramide, dronabinol, nabilone, repaglinide, saxagliptin, linagliptin, eliglustat, nitisinone, and vitamin D analogues (cholecalciferol, ergocalciferol, calcifediol, calcitriol, dihydrotachysterol).

Package insert warnings and contraindications were not available for this report. Please refer to the current package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Trigeminal neuralgia is mechanistically plausible, but the only direct clinical evidence is a single 1995 case report, and no trials are registered. Safer, established alternatives (carbamazepine, oxcarbazepine, lamotrigine) exist, while felbamate's risks of aplastic anemia and hepatic failure make its risk-benefit profile unfavorable. Felbamate is marketed in the US, with 8 valid licenses.
- Trigeminal nerve neoplasm has a very high model score but no evidence and no plausible antitumour mechanism, so it should not be pursued.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Controlled clinical data in trigeminal neuralgia, ideally comparing felbamate with carbamazepine or oxcarbazepine
- A risk-benefit justification, such as use only in patients refractory to standard therapy, with a hematologic and liver monitoring plan
- Clarification of the regulatory and commercial status, since felbamate is marketed in the US with 8 valid licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

