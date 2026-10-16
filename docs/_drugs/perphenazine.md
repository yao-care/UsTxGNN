---
layout: default
title: Perphenazine
parent: Model Prediction Only (L5)
nav_order: 1033
evidence_level: L5
indication_count: 10
monitor_inn: "PERPHENAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "hydranencephaly (disease)", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "atypical glycine encephalopathy", "anxiety disorder"]
last_modified_at: 2026-10-14
description: "Perphenazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
---

# Perphenazine
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

# Perphenazine: From Schizophrenia to Retinal Dystrophy (With or Without Extraocular Anomalies)

## One-Sentence Summary

Perphenazine is a phenothiazine antipsychotic, originally used for schizophrenia and mixed anxiety and depressive disorder.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and only **1 publication** for this prediction. That publication reports a retinal toxicity signal for a related drug, not a benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; mixed anxiety and depressive disorder |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 7 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, perphenazine is a phenothiazine antipsychotic that mainly blocks dopamine D2 receptors, with additional serotonin 5-HT2A, adrenergic and histamine activity. Its efficacy in schizophrenia and in mixed anxiety and depression (in combination with amitriptyline) is established.

For this prediction, however, **no plausible therapeutic link was found**. The only retrieved publication describes pigmentary retinopathy as an *adverse effect* of thioridazine, a different phenothiazine. Phenothiazines are known to be associated with retinal toxicity. The high TxGNN score therefore most likely reflects a graph-based association between this drug class and retinal pathology, not a therapeutic effect. Perphenazine is not expected to treat inherited retinal dystrophy, and the prediction should be read as a likely model artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14129300](https://pubmed.ncbi.nlm.nih.gov/14129300/) | 1964 | Case report (adverse drug effect, different drug) | The American Journal of Psychiatry | Pigmentary retinopathy associated with thioridazine, reported at a maximum daily dose of 1400 mg. This is a safety signal, not evidence of benefit, and it concerns a different drug. |

---

## US Market Information

All 7 US authorizations are generic (ANDA) tablet products and all are cancelled. No approved indication text was available for these licenses.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA210163 | Perphenazine (RemedyRepack) | Tablet | Not listed |
| ANDA205973 | Perphenazine (Bryant Ranch Prepack) | Tablet, film coated | Not listed |
| ANDA040226 | Perphenazine (Endo USA) | Tablet, film coated | Not listed |
| ANDA205232 | Perphenazine (Golden State Medical Supply) | Tablet | Not listed |
| ANDA205056 | Perphenazine (Proficient Rx) | Tablet, film coated | Not listed |

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: These include cardiac and rhythm conditions (long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, myocardial infarction), blood disorders (neutropenia, agranulocytosis, thrombocytopenia, anemia), neurological conditions (epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm), orthostatic hypotension and related autonomic disorders, liver and gallbladder disease, hyperglycemia, open-angle glaucoma, benign prostatic hyperplasia, manic bipolar affective disorder, substance abuse/dependence, and obesity disorders.
- **Drug Interactions**: 100 interactions were recorded. Major-level interactions include **bupropion**, **morphine** and **potassium citrate**. Moderate-level interactions include antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, acarbose, chlorpropamide, albiglutide), anticholinergics (atropine, hyoscyamine, glycopyrronium), epinephrine, clarithromycin, famotidine and loperamide.
- **Relevance to this prediction**: The only literature on the predicted indication points to a retinal toxicity risk with phenothiazines. This would need careful evaluation before any ocular use.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). No trials exist, and the single publication describes retinal harm from a related drug rather than benefit. No credible mechanism links perphenazine's receptor pharmacology to inherited retinal dystrophy. All US licenses are also cancelled. Among the other predicted indications in this analysis, only "anxiety disorder" has meaningful supporting literature (L3). That indication overlaps with perphenazine's existing use in mixed anxiety and depression, so it is not a true repurposing signal.

**To proceed, the following is needed:**
- A plausible mechanistic rationale and preclinical data supporting benefit in retinal dystrophy
- Evaluation of the retinal toxicity risk of phenothiazines, including perphenazine specifically
- Detailed mechanism of action (MOA) data
- Package insert warnings and contraindications for formal safety screening
- Confirmation of current US marketing availability, since all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

