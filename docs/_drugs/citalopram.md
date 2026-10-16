---
layout: default
title: Citalopram
parent: Model Prediction Only (L5)
nav_order: 532
evidence_level: L5
indication_count: 5
monitor_inn: "CITALOPRAM"
predicted_indications: ["obsessive-compulsive disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "schizotypal personality disorder", "paranoid personality disorder"]
last_modified_at: 2026-10-14
description: "Citalopram: predicted new indication Obsessive-compulsive disorder (evidence level L5). Approved use: Major depressive disorder, unipolar depression, dysthymic disorder…"
---

# Citalopram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Citalopram: From Depression and Anxiety Disorders to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a selective serotonin reuptake inhibitor (SSRI), originally used to treat depressive and anxiety-related disorders.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
with **4 related clinical trials** (none citalopram-specific) and **16 publications** (several citalopram-specific open-label or pilot studies) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder, unipolar depression, dysthymic disorder, anxiety disorder (from the knowledge graph; no approved-indication text was available in the US license records) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 (see note below) |
| US Market Status | Cancelled only (no currently valid licenses in the compiled data) |
| Number of NDAs | 11 records (all cancelled; these are ANDA generic or repackager entries) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level: the L2 grade rests on class-level SSRI evidence plus citalopram-specific open-label and pilot data. None of the listed trials is a citalopram-specific Phase 2/3 RCT, so a strict reading of the criteria would put the evidence closer to L3.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, citalopram belongs to the SSRI class, which increases serotonin availability in the synapse by blocking its reuptake. Its efficacy in depression and anxiety is established, and mechanistically it may be applicable to OCD.

Serotonergic dysfunction is considered central to OCD, and SSRIs are first-line pharmacotherapy for the condition. Depression, anxiety disorders and OCD frequently co-occur and share serotonergic pathways. This is consistent with the very high TxGNN score.

Citalopram-specific support comes from small open-label and comparative studies in adults, treatment-resistant patients, and children and adolescents (see Literature Evidence). The main caveat is that no citalopram-specific randomized controlled trial in OCD was found.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Compares exposure and response prevention (ERP), SSRIs and their combination in OCD, and looks for predictors of response in a Chinese population. Citalopram may be among the SSRIs used. |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Tests whether cognitive behavioral therapy improves outcomes in children with OCD who only partly responded to serotonin reuptake inhibitors. |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | Completed | 158 | Randomized open trial of group CBT vs. fluoxetine in OCD. Indirect evidence, since fluoxetine rather than citalopram was used. |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | N/A | Completed | 43 | Pilot study of gut microbiota in OCD vs. healthy controls and after 12 weeks of open-label SSRI treatment. Background information only. |

None of these trials tests citalopram on its own; they support the SSRI class in OCD.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | Single-blind comparison | J Clin Psychopharmacol | Compared the antiobsessional efficacy of fluvoxamine, paroxetine and citalopram in 30 OCD patients. |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Randomized open-label trial | Eur Psychiatry | Citalopram alone vs. citalopram plus clomipramine in 16 treatment-resistant OCD patients over 90 days. |
| [9395151](https://pubmed.ncbi.nlm.nih.gov/9395151/) | 1997 | Open pilot study | Acta Psychiatr Scand | 24-week open pilot study of citalopram in OCD. |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | Cohort | CNS Drugs | Preliminary look at the relationship between citalopram concentrations and clinical response in OCD. |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | Open trial | J Child Adolesc Psychopharmacol | In 23 children and adolescents, 10 weeks of citalopram significantly improved Y-BOCS/CY-BOCS scores (30 → 21). |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label cohort | Psychiatry Clin Neurosci | 8-week open-label study of citalopram (mean 24 mg/day) in 15 children and adolescents with OCD. |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Review | Int Clin Psychopharmacol | "Beyond depression": reviews citalopram for OCD in the context of serotonin reuptake inhibitor research. |
| [20712565](https://pubmed.ncbi.nlm.nih.gov/20712565/) | 2010 | Review | Curr Med Chem | Past, present and future drugs for OCD, with SSRIs as the central treatment. |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World J Biol Psychiatry | Reviews serotonin and other mechanisms in OCD, which responds to both CBT and serotonergic drugs. |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clin Evid | Overview of OCD epidemiology, course and treatment. |

---

## US Market Information

All 11 US license records in the compiled data are cancelled, and none contained approved-indication text. Several entries are escitalopram products, listed under the citalopram record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078216 | Citalopram (Cardinal Health 107) | Tablet, film coated | Not available |
| ANDA077031 | Citalopram (A-S Medication Solutions) | Tablet, film coated | Not available |
| ANDA077534 | Citalopram (RemedyRepack) | Tablet | Not available |
| ANDA077042 | Citalopram (Bryant Ranch Prepack) | Tablet, film coated | Not available |
| ANDA079121 | Escitalopram (Sun Pharmaceutical) | Solution | Not available |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: long QT syndrome (including familial), torsades de pointes, epilepsy, bipolar disorder / major affective disorder, liver disease, gallbladder disease, potassium deficiency, blood coagulation disease, heart and cardiovascular disease, neuroleptic malignant syndrome, SIADH (including nephrogenic), and serotonin syndrome.
- **Drug Interactions**: 100 interactions were identified. Examples of those rated **Major**: bupropion, omeprazole, cimetidine, lorcaserin, cisapride, clarithromycin, dexfenfluramine, diethylpropion and dolasetron. Several others are rated Moderate (e.g., famotidine, morphine, acetylsalicylic acid, loperamide) or Minor (e.g., aprepitant, clotrimazole). Many of the major interactions involve QT prolongation or serotonergic effects, in line with the knowledge-graph warnings.

Label-based warnings and contraindications were not available; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
OCD has a well-established serotonergic basis, SSRIs are first-line therapy, and citalopram has multiple citalopram-specific open-label and pilot studies in adults and children. However, the supporting trials are class-level or indirect, and no citalopram-specific RCT exists. Cardiac (QT) risk and serotonergic interactions require careful management.

**To proceed, the following is needed:**
- A citalopram-specific randomized controlled trial in OCD, or a systematic review pooling SSRI evidence with citalopram-specific results
- Mechanism of action data and FDA label warnings and contraindications, which are currently missing (the label review is a blocking item for formal safety screening)
- A cardiac safety plan (baseline and follow-up ECG, electrolyte monitoring) and a drug-interaction screening process
- Clarification of current US marketing status, since all records in the compiled data are cancelled

---

*Other predicted indications (histrionic, schizoid, schizotypal and paranoid personality disorders) have only model-based predictions or indirect literature, with no supporting trials. They are rated L4–L5 and should be on **Hold**.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

