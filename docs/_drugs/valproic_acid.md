---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 1280
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Valproic Acid: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy, manic bipolar affective disorder, absence epilepsy"
monitor_inn: "VALPROIC ACID"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "eating seizures", "audiogenic seizures", "orgasm-induced seizures", "micturation-induced seizures", "thinking seizures", "reading seizures"]
---

# Valproic Acid
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

# Valproic Acid: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Valproic acid is an established antiseizure medication, originally used for epilepsy (including absence epilepsy) and manic episodes of bipolar disorder.
The TxGNN model ranks **trigeminal nerve neoplasm** as its top predicted new indication, but there are **0 clinical trials** and only **1 publication** (a case series on a different condition), so the evidence is essentially model prediction only.
Of the other nine predictions, **startle epilepsy** has the most relevant supporting data (small observational studies and case reports).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, manic bipolar affective disorder, absence epilepsy (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorization in the compiled data) |
| Number of NDAs | 7 (all cancelled; all are ANDA generic applications) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, valproic acid enhances GABAergic transmission and modulates sodium and T-type calcium channels, and it is a histone deacetylase (HDAC) inhibitor that has been hypothesized to have antineoplastic effects.

For the top prediction, trigeminal nerve neoplasm, **no direct mechanistic link is supported by the data.** The only retrieved paper is a 1997 case series on Sturge-Weber syndrome, a neurocutaneous vascular disorder rather than a tumour. The very high TxGNN score most likely reflects proximity in the knowledge graph (seizure and neurological disease neighbours) rather than real evidence.

Other predictions are more plausible because they are extensions of valproic acid's seizure indication:

- **Startle epilepsy** has the strongest support. A small clinical study examined valproate's effect on the auditory startle reflex, and a case report describes complete resolution of startle disease (hyperekplexia) on valproate.
- **Visual epilepsy** and **reading seizures** are reflex seizure types related to idiopathic generalized epilepsies, where valproate is a first-line agent. Evidence is indirect.
- **Trigeminal neuralgia** is supported by older reviews listing valproate as a second-line anticonvulsant, but most retrieved papers concern carbamazepine.
- **Audiogenic seizures** are supported by animal studies only.
- **Eating seizures**, **micturition-induced seizures**, **thinking seizures** and **orgasm-induced seizures** have little or no relevant evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication or for any of the other nine predicted indications.

---

## Literature Evidence

**Top prediction: trigeminal nerve neoplasm**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases; not about trigeminal tumours, so not relevant evidence |

**Most relevant literature across the other predictions** (shown for context)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20200383](https://pubmed.ncbi.nlm.nih.gov/20200383/) | 2010 | RCT | N Engl J Med | Ethosuximide, valproic acid and lamotrigine compared in childhood absence epilepsy (supports the original indication; indirect for the predictions) |
| [29262725](https://pubmed.ncbi.nlm.nih.gov/29262725/) | 2018 | Clinical study | Clin EEG Neurosci | Small observational study of whether valproate suppresses the auditory startle reflex (startle epilepsy) |
| [2496695](https://pubmed.ncbi.nlm.nih.gov/2496695/) | 1989 | Case report | Pediatr Neurol | Adolescent-onset startle disease (hyperekplexia) fully resolved on valproic acid |
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Curr Neuropharmacol | Molecular mechanisms and clinical evidence of valproic acid in epilepsy |
| [1774173](https://pubmed.ncbi.nlm.nih.gov/1774173/) | 1991 | Review | Headache | Valproic acid listed among anticonvulsants reported effective in trigeminal neuralgia |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Cohort/Review | Future Oncol | Levetiracetam and valproic acid in glioma: antiseizure and possible antineoplastic effects (indirect) |
| [33551767](https://pubmed.ncbi.nlm.nih.gov/33551767/) | 2020 | Preclinical | Front Behav Neurosci | Cannabidiol and valproate in the GASH/Sal audiogenic seizure hamster model |
| [38117708](https://pubmed.ncbi.nlm.nih.gov/38117708/) | 2023 | Review | Medicina | Reflex triggers in juvenile myoclonic epilepsy (indirect for reading seizures) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075782 (cancelled) | Valproic Acid (Chartwell RX) | Solution | Not available |
| ANDA073178 (cancelled) | Valproic Acid (ANI Pharmaceuticals) | Solution | Not available |
| ANDA075379 (cancelled) | Valproic Acid (PAI Pharma) | Solution | Not available |
| ANDA073484 (cancelled) | Valproic Acid (Vangard Labs) | Capsule, liquid filled | Not available |
| ANDA077960 (cancelled) | Valproic Acid (Lannett) | Solution | Not available |

Two further cancelled authorizations (ANDA070868, ANDA073229) are not listed. All 7 authorizations are cancelled, and none is currently valid in the compiled data.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from drug-disease graph relationships, not from package insert text): anxiety disorder, neurotic disorder, dysthymic disorder, carbamoyl phosphate synthetase I deficiency, inherited porphyria / porphyria / porphyrin metabolism disease, kidney disease, pyoureter, hyperargininemia, haematologic disease, pancreatitis, citrullinemia, cognitive disorder, liver disease, gallbladder disease, thrombocytopenia.

**Drug Interactions:** 100 interactions were found in total. The first 20 returned include:
- **Major:** glycerol phenylbutyrate
- **Moderate:** bupropion, morphine (including liposomal), acetylsalicylic acid, clarithromycin, difenoxin, diphenoxylate, activated charcoal, dronabinol, metoclopramide, nabilone
- **Minor:** cimetidine, esomeprazole, and several antacids (magnesium oxide, aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide)

**Literature-based safety notes:** the retrieved papers discuss hepatotoxicity, hyperammonaemic encephalopathy, teratogenicity and neurodevelopmental effects with prenatal exposure, and a notable interaction with carbapenem antibiotics. Overdose toxicity is also reported.

Please refer to the package insert for the full key warnings and contraindications, which were not available in the compiled data. This is a blocking gap for safety screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, has no trials and no supporting literature. Its very high score appears to reflect graph proximity rather than evidence. Valproic acid currently has no valid US authorization in the compiled data, and label safety information is missing. The seizure-related predictions are better candidates but are extensions of the existing indication rather than novel repurposing. Startle epilepsy (evidence level L3) is the strongest of them.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data to support analysis of the mechanistic link
- Direct preclinical or clinical evidence for valproate in trigeminal nerve tumours (for example HDAC-inhibitor antitumour data)
- Confirmation of current US marketing status, since all 7 authorizations are cancelled
- Consideration of startle epilepsy or trigeminal neuralgia as more evidence-supported alternatives, ideally with a controlled study
- A safety plan addressing hepatotoxicity, pregnancy and women of childbearing potential, and the major and moderate interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

