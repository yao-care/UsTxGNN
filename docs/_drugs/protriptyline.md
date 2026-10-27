---
layout: default
title: Protriptyline
parent: Moderate Evidence (L3-L4)
nav_order: 1096
evidence_level: L3
indication_count: 5
monitor_inn: "PROTRIPTYLINE"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "specific developmental disorder", "attention deficit-hyperactivity disorder", "chondromyxoid fibroma", "faciodigitogenital syndrome"]
last_modified_at: 2026-10-14
description: "Protriptyline: predicted new indication Attention deficit-hyperactivity disorder (evidence level L3). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder"
---

# Protriptyline
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
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

## Protriptyline: From Anxiety Disorder to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Protriptyline is a tricyclic antidepressant, listed in the knowledge graph for anxiety disorder, neurotic disorder, and dysthymic disorder.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, with **0 registered clinical trials** and **1 relevant publication** (a 1996 naturalistic study) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Attention deficit-hyperactivity disorder (rank 3 of the model's predictions; the top-ranked prediction, ADHD inattentive type, has no supporting studies) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (both cancelled ANDAs) |
| Recommended Decision | Hold |

**Note on the choice of indication:** The top-ranked prediction, ADHD inattentive type (score 99.95%), has no clinical trials or literature (L5). The report therefore focuses on the closely related general ADHD prediction (score 99.77%), which is the only prediction with direct supporting literature. The other predictions are summarised at the end of the report.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, protriptyline is a tricyclic antidepressant that mainly inhibits norepinephrine reuptake, with weaker serotonin reuptake inhibition. This is background knowledge, not something confirmed by the compiled data.

Enhanced noradrenergic signalling in the prefrontal cortex is a plausible mechanism for improving attention-related symptoms. Other noradrenergic agents, including atomoxetine and other tricyclics such as desipramine, are used in ADHD. Anxiety and dysthymia also commonly co-occur with ADHD, which may partly explain the network proximity behind the prediction.

The evidence is limited. One uncontrolled observational study of protriptyline in children and adolescents with ADHD exists, and no registered clinical trials were found. The link is therefore mostly mechanistic inference.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8936915](https://pubmed.ncbi.nlm.nih.gov/8936915/) | 1996 | Cohort (naturalistic) | J Am Acad Child Adolesc Psychiatry | Naturalistic assessment of protriptyline in children and adolescents with ADHD. The available abstract states only the study aim, so results cannot be summarised. |

Two other retrieved papers (PMIDs 19007502 and 22112053) are urine assay methods for guanfacine that used protriptyline only as an internal standard. They say nothing about protriptyline efficacy and are excluded.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202220 (cancelled) | Protriptyline Hydrochloride (Epic Pharma, LLC) | Film-coated tablet | Not available |
| ANDA090462 (cancelled) | Protriptyline Hydrochloride (Sigmapharm Laboratories, LLC) | Film-coated tablet | Not available |

Both authorizations are cancelled, so no valid US marketing authorization is currently on record. Any development would need a new supply or approval pathway.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Contraindications and cautions from the knowledge graph** (drug-disease links, not label text): epilepsy, bipolar disorder, major affective disorder, schizophrenia, liver disease, gallbladder disease, asthma, benign prostatic hyperplasia, hypotensive disorder, substance abuse/dependence, dementia, glaucoma (including angle-closure and ocular hypertension), hyperthyroidism (Graves disease, thyrotoxicosis), sudden cardiac arrest, heart conduction disease, and gastro-oesophageal conditions (reflux disease, oesophagitis, hiatus hernia).
- **Drug Interactions**: 100 interactions were recorded. Examples of **Major** interactions include epinephrine, bupropion, lorcaserin, potassium citrate, and dolasetron. **Moderate** interactions include famotidine, cimetidine, clarithromycin, morphine, loperamide, and several anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine).
- **Practical concern**: Tricyclic antidepressants are generally associated with anticholinergic effects, cardiac conduction effects, and toxicity in overdose. These are particularly important in children and adolescents, the main ADHD population, though this is general knowledge and not confirmed by the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for ADHD is a single uncontrolled 1996 observational study and a mechanistic inference, with no registered trials. Limited safety data, a heavy interaction burden, and cancelled-only US market status further limit feasibility. The decision stage remains at S0 (initial screening).

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full text and results of the 1996 naturalistic study, plus a search for further observational or controlled studies
- A pediatric and adult safety assessment, including cardiac risk, against existing ADHD therapies
- A plan for drug supply and regulatory pathway, given that both US authorizations are cancelled

## Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 1 | ADHD, inattentive type | 99.95% | L5 | Mechanistic inference only; no trials or literature |
| 2 | Specific developmental disorder | 99.91% | L5 | No clear mechanistic rationale; likely network proximity to ADHD |
| 4 | Chondromyxoid fibroma | 99.66% | L5 | No plausible pharmacological link; likely a graph artifact |
| 5 | Faciodigitogenital syndrome | 99.48% | L5 | No mechanistic rationale for this genetic condition; unsupported |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

