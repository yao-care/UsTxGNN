---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 1043
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (generalized tonic-clonic, partial, status epilepticus…"
monitor_inn: "PHENYTOIN"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenytoin is a long-established anticonvulsant used for epilepsy, including generalized tonic-clonic seizures, partial seizures and status epilepticus.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but the supporting evidence is very weak: **0 clinical trials** and **2 publications** that concern trigeminal neuralgia and Sturge-Weber syndrome rather than tumours.
The more credible signal in the data is for the related condition **trigeminal neuralgia**, which has substantial observational and review-level literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalized tonic-clonic, partial, status epilepticus, Lennox-Gastaut syndrome) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of FDA Applications | 8 (all ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Phenytoin is generally understood to block voltage-gated sodium channels and stabilize hyperexcitable neuronal membranes. This explains its anticonvulsant effect and its relevance to neuropathic pain.

That mechanism does not extend to tumour biology. The high TxGNN score most likely reflects network proximity to trigeminal neuralgia, a pain syndrome of the same nerve, and not an anti-tumour effect. The two papers retrieved cover trigeminal neuralgia treatment and Sturge-Weber syndrome. Neither shows phenytoin treating a neoplasm or giving a symptomatic benefit specific to one.

The same data does support a more plausible nearby candidate. Phenytoin shares its mechanism with carbamazepine, the first-line therapy for trigeminal neuralgia, and the literature recognizes phenytoin as a second-line or rescue option (see the note below the literature table).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

**Trigeminal nerve neoplasm (the predicted indication)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; does not address neoplasm |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 cases of Sturge-Weber syndrome, reviewing clinical features and treatment response; not a neoplasm |

No literature supports an anti-tumour effect of phenytoin.

**Related signal: trigeminal neuralgia (ranked 9th, TxGNN score 0.9997, evidence level L3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on managing trigeminal neuralgia |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort | Cephalalgia | Retrospective analysis of 144 cases of IV lacosamide and phenytoin for acute exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Retrospective cohort | Headache | IV phenytoin as acute rescue treatment in trigeminal neuralgia crisis |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | J Pain Res | Questions the evidence base for phenytoin and carbamazepine in trigeminal neuralgia |
| [7580659](https://pubmed.ncbi.nlm.nih.gov/7580659/) | 1995 | Systematic review | BMJ | Effectiveness and adverse effects of anticonvulsants in pain management |
| [11803299](https://pubmed.ncbi.nlm.nih.gov/11803299/) | 2002 | Review | Clin J Pain | Carbamazepine has controlled-trial support; lamotrigine adds effect in patients with insufficient relief on carbamazepine or phenytoin |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA213834 | Phenytoin Sodium | Capsule, extended release | Not recorded; status valid |
| ANDA040684 | Phenytoin Sodium | Capsule, extended release | Not recorded; status valid |
| ANDA084307 | Phenytoin Sodium | Injection | Not recorded; status valid |
| ANDA084349 | DILANTIN | Capsule, extended release | Not recorded; status valid |
| ANDA200565 | Phenytoin | Chewable tablet | Not recorded; status valid |

The drug is marketed in the US with 8 valid licenses; the table shows the first 5.

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** long QT syndrome and torsades de pointes, liver failure and liver disease, kidney disease, porphyria, thrombocytopenia, neutropenia and agranulocytosis, hyperglycemia, diabetes mellitus and diabetic ketoacidosis, systemic lupus erythematosus, hypotensive disorder, hepatic encephalopathy, sleep apnea syndromes, and substance abuse/dependence.

**Supporting case literature:** thrombocytopenia (PMID 9101005), hyperglycemia and diabetic ketoacidosis (PMID 7294047), porphyria attacks (PMID 98734), and severe skin reactions in patients receiving cranial irradiation (EMPACT syndrome, PMIDs 16353748 and 21675930).

**Drug interactions:** 100 interactions were recorded. Most are moderate in severity, including acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, dexamethasone, metformin, pioglitazone, bupropion, aprepitant, omeprazole, metronidazole and morphine. Acetylsalicylic acid is rated minor.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trigeminal nerve neoplasm is a model output only. It has no clinical trials, no supporting literature on tumours, and no plausible link between sodium channel blockade and tumour biology. Trigeminal neuralgia has meaningful literature, but phenytoin is a second-line option behind carbamazepine and oxcarbazepine. The drug is marketed in the US with 8 valid licenses.

**To proceed, the following is needed:**
- Re-scope the question from trigeminal nerve neoplasm to trigeminal neuralgia, with a focus on IV phenytoin for acute exacerbations
- A controlled study comparing phenytoin with carbamazepine, oxcarbazepine or lacosamide in trigeminal neuralgia
- The package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Clarification of current US marketing status, since 8 valid licenses are listed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

