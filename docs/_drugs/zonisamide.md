---
layout: default
title: Zonisamide
parent: Model Prediction Only (L5)
nav_order: 1312
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Zonisamide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not available"
monitor_inn: "ZONISAMIDE"
predicted_indications: ["Tourette syndrome", "trichotillomania", "methemoglobinemia, alpha type", "methemoglobinemia", "Prinzmetal angina", "methemoglobin reductase deficiency", "manic bipolar affective disorder", "fibromyalgia", "conjunctivitis"]
---

# Zonisamide
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

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

Zonisamide is an oral anticonvulsant (a sulfonamide-class antiepileptic). The data compiled for this report do not include its approved indication text, but the literature identifies it as an antiepileptic drug.
The TxGNN model's top-ranked prediction is **Tourette syndrome**, but this prediction has **0 clinical trials** and **0 publications** behind it. It is a model prediction only.
Among the other top-10 predictions, **absence epilepsy** has the most supporting literature (about 20 publications, mostly small studies, reviews and guidelines), and **manic bipolar affective disorder** has about 20 publications, which are mixed and largely indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is empty in the compiled license data; literature describes zonisamide as an antiepileptic drug) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 authorizations in total (1 NDA, 6 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From general pharmacology, zonisamide blocks voltage-gated sodium channels and T-type calcium channels and may modulate dopaminergic and serotonergic transmission. These actions could plausibly relate to the neural circuits involved in tics, but this link is speculative.

There is also a safety concern. A 2022 pragmatic review (PMID 36005856) reports that antiseizure medications can induce obsessive-compulsive disorder and tic disorder. This raises a risk signal rather than supporting efficacy.

Other top-10 predictions, for context:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Tourette syndrome | 99.85% | L5 | No evidence; tic-induction risk |
| 2 | Trichotillomania | 99.78% | L5 | No evidence; speculative link |
| 3 | Methemoglobinemia, alpha type | 99.64% | L5 | No plausible mechanism; sulfonamide oxidative risk |
| 4 | Methemoglobinemia | 99.63% | L5 | Correlated duplicate of rank 3 |
| 5 | Prinzmetal angina | 99.55% | L5 | Speculative T-type calcium channel link |
| 6 | Methemoglobin reductase deficiency | 99.53% | L5 | Genetic enzyme deficiency; no mechanism |
| 7 | Manic bipolar affective disorder | 99.35% | L4 | Mixed, indirect evidence |
| 8 | Absence epilepsy | 99.24% | L4 | Strongest mechanistic rationale |
| 9 | Fibromyalgia | 99.20% | L5 | Only trial withdrawn |
| 10 | Conjunctivitis | 99.16% | L5 | No credible rationale |

The methemoglobinemia-related predictions (ranks 3, 4 and 6) are likely artifacts of the knowledge graph. Because zonisamide is a sulfonamide, they point to a potential risk rather than a benefit.

Among the ten, **absence epilepsy** is the most mechanistically credible. T-type calcium channels are central to the thalamocortical spike-wave discharges seen in absence seizures, and zonisamide already has an established place in other epilepsy types. However, this is close to the drug's existing use rather than a true repurposing to a new disease area.

---

## Clinical Trial Evidence

For the top-ranked prediction (Tourette syndrome), no related clinical trials are registered.

Across the other top-10 predictions, only one trial was found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00259636](https://clinicaltrials.gov/study/NCT00259636) | Phase 4 | Withdrawn | 0 | Planned placebo-controlled randomized study of zonisamide in fibromyalgia and migraine (2004–2008). Withdrawn with zero enrollment, so it provides no efficacy or safety data. |

---

## Literature Evidence

For the top-ranked prediction (Tourette syndrome), no related literature is available.

The most relevant publications for the other candidate indications are listed below. The tier column is the preliminary classification from the compiled data; items marked "design not confirmed" were classified from titles and abstracts only.

**Absence epilepsy (rank 8)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | Chart review | Epilepsy Research | 45 patients aged 18 or younger with absence seizures; 51.1% (23) became seizure-free, and 2 discontinued. |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | Case series (design not confirmed) | Epilepsy Research | Examined zonisamide in drug-resistant juvenile absence epilepsy. |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | Retrospective study | Epileptic Disorders | 15 patients with juvenile myoclonic epilepsy (a related syndrome) treated with zonisamide; efficacy and tolerability evaluated. |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network meta-analysis | Cochrane Database Syst Rev | General epilepsy monotherapy comparison; zonisamide efficacy in absence epilepsy not confirmed. |
| [23350722](https://pubmed.ncbi.nlm.nih.gov/23350722/) | 2013 | Evidence review (ILAE) | Epilepsia | Initial monotherapy evidence across epilepsy types; not specific to zonisamide in absence epilepsy. |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES update on new-onset epilepsy treatment; general. |
| [16321507](https://pubmed.ncbi.nlm.nih.gov/16321507/) | 2006 | Review | Epilepsy Research | Japanese experience; benefit across a range of seizure types and ages. |
| [16341290](https://pubmed.ncbi.nlm.nih.gov/16341290/) | 2005 | Review | Drugs of Today | Zonisamide effective in several seizure types, including absence seizures in patients unresponsive to other anticonvulsants. |

**Manic bipolar affective disorder (rank 7)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17163811](https://pubmed.ncbi.nlm.nih.gov/17163811/) | 2007 | Clinical study (likely open-label pilot) | Expert Opin Pharmacother | Evaluates an open-label pilot of zonisamide in bipolar **depression** (not mania), observing tolerability and switch to mania. |
| [2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/) | 1990 | Case report | Psychosomatics | Zonisamide-induced mania (a safety signal). |
| [22575611](https://pubmed.ncbi.nlm.nih.gov/22575611/) | 2013 | Systematic review | Int J Neuropsychopharmacol | Anticonvulsants in acute bipolar depression; not specific to zonisamide mania. |
| [16503812](https://pubmed.ncbi.nlm.nih.gov/16503812/) | 2006 | Review | Expert Opin Pharmacother | Anticonvulsants in bipolar mania, including zonisamide. |
| [12938867](https://pubmed.ncbi.nlm.nih.gov/12938867/) | 2003 | Review | Ann Clin Psychiatry | Notes topiramate and zonisamide can yield weight loss in bipolar disorders. |

**Safety-relevant literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/) | 2022 | Review | Expert Rev Neurother | Antiseizure medication-induced obsessive-compulsive disorder and tic disorder. |

**Fibromyalgia (rank 9):** the two supplied publications are general antiepileptic drug reviews (chemical properties and sleep effects) and do not address fibromyalgia efficacy.

---

## US Market Information

All seven authorizations are cancelled, and no approved indication text is available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020789 | Zonegran (Advanz Pharma (US) Corp.) | Capsule | Not available (cancelled) |
| ANDA077651 | Zonisamide (Glenmark Pharmaceuticals Inc., USA) | Capsule | Not available (cancelled) |
| ANDA077634 | Zonisamide (Sun Pharmaceutical Industries, Inc.) | Capsule | Not available (cancelled) |
| ANDA077645 | Zonisamide (Aurobindo Pharma Limited) | Capsule | Not available (cancelled) |
| ANDA077625 | Zonisamide (Zydus Lifesciences Limited) | Capsule | Not available (cancelled) |

Two further generic authorizations (ANDA214492, Unichem; ANDA077869, Exelan) are also cancelled.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (derived from drug-disease relationships in the TxGNN knowledge graph, not from label text): psychiatric conditions (anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder); kidney and urinary conditions (kidney disease, nephrolithiasis, acute urate nephropathy, pyoureter); liver and gallbladder disease; diarrheal disease; acidosis (metabolic acidosis); and a broad group of blood disorders involving agranulocytosis and neutropenia, including several congenital neutropenia syndromes.
- **Drug interactions** (100 interactions recorded; examples from the first 20 listed):
  - **Major:** anticholinergic agents (methscopolamine, hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, propantheline) and metformin.
  - **Moderate:** aprepitant, morphine, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, miconazole.
- **Literature-based safety signals:** induced mania (PMID 2109869), and obsessive-compulsive and tic disorder induction by antiseizure medications (PMID 36005856). As a sulfonamide, zonisamide may also carry a risk of drug-induced methemoglobinemia.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, Tourette syndrome, rests on a model score alone (L5) with no trials or literature, and the available literature points to a tic-induction risk rather than benefit. The strongest candidate, absence epilepsy (L4), has a credible mechanism and small supportive studies, but it is essentially an extension within epilepsy and lacks Phase 2/3 randomized evidence. Bipolar mania evidence is indirect and mixed, including a case of zonisamide-induced mania. All US authorizations are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Full-text review of the absence epilepsy and juvenile myoclonic epilepsy studies to confirm study design (retrospective versus prospective) and whether the evidence can reach L3
- Controlled trial data for any indication under consideration; none is currently registered except one withdrawn fibromyalgia trial
- A safety assessment of the tic, OCD, mania and methemoglobinemia signals before any psychiatric repurposing is considered
- Clarification of the US regulatory status, given that all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

