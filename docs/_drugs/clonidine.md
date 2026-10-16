---
layout: default
title: Clonidine
parent: Model Prediction Only (L5)
nav_order: 541
evidence_level: L5
indication_count: 10
monitor_inn: "CLONIDINE"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "migraine disorder", "manic bipolar affective disorder"]
---

# Clonidine
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

# Clonidine: From Hypertension to Faciodigitogenital Syndrome

## One-Sentence Summary

Clonidine is an alpha-2 adrenergic agonist originally used for hypertension, and also for open-angle glaucoma and ADHD.
The TxGNN model gives its highest score to **faciodigitogenital syndrome**, but **no clinical trials and no publications** support this prediction.
The better-supported candidates among the other predictions are **Tourette syndrome** (2 Phase 4 trials, 18 publications) and **manic bipolar affective disorder** (1 terminated trial, 20 publications).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (other listed indications: open-angle glaucoma, ADHD) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 12 (all cancelled; the authorizations listed are ANDAs) |
| Recommended Decision | Hold |

The top-ranked prediction has no supporting evidence. Other predictions have more evidence and are summarised below.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Faciodigitogenital syndrome | 99.999% | L5 | Hold |
| 2 | Specific developmental disorder | 99.999% | L4 | Hold |
| 3 | Chondromyxoid fibroma | 99.997% | L5 | Hold |
| 4 | Trichotillomania | 99.994% | L4 | Hold |
| 5 | Tourette syndrome | 99.976% | L2 | Proceed with Guardrails |
| 6 | Obesity disorder | 99.910% | L3 | Research Question |
| 7 | Hypervitaminosis | 99.868% | L5 | Hold |
| 8 | Proximal 16p11.2 microdeletion syndrome | 99.858% | L5 | Hold |
| 9 | Migraine disorder | 99.814% | L3 | Research Question |
| 10 | Manic bipolar affective disorder | 99.756% | L3 | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clonidine is an alpha-2 adrenergic agonist that reduces noradrenergic outflow. Its efficacy in hypertension and ADHD is established.

For the top-ranked prediction, faciodigitogenital syndrome, no plausible mechanistic link is evident. This is a rare developmental genetic disorder, and the score reflects a graph-based prediction only. The same applies to chondromyxoid fibroma, hypervitaminosis and proximal 16p11.2 microdeletion syndrome. These should not be pursued without new supporting data.

The predictions with a more credible rationale share a noradrenergic or sympathetic mechanism:
- **Tourette syndrome**: Reducing noradrenergic activity is an established way to treat tics, especially with comorbid ADHD. This is close to clonidine's existing ADHD use, so it is closer to an already-recognised use than a novel repurposing.
- **Manic bipolar disorder**: Dampening noradrenergic hyperactivity may reduce mania, agitation and sleep disturbance.
- **Obesity disorder**: The signal concerns obesity-related hypertension and vascular or inflammatory changes. It is not weight loss.
- **Migraine**: Clonidine has been studied for prophylaxis since the 1970s, with inconsistent benefit.

## Clinical Trial Evidence

The top-ranked indication (faciodigitogenital syndrome) has no registered trials. The table below covers the better-supported predictions.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Unknown | 32 | Tourette syndrome with ADHD: tests whether treating night-time sleep with clonidine improves day-time aggression in children |
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Completed | 12 | Tourette syndrome: levetiracetam vs clonidine for tics in children, in a crossover design; very small |
| [NCT01983462](https://clinicaltrials.gov/study/NCT01983462) | Phase 2 | Terminated | 33 | Obesity hypertension: effect of clonidine-based sympathetic blockade on vascular function and muscle nerve activity |
| [NCT04934228](https://clinicaltrials.gov/study/NCT04934228) | Phase 1 | Recruiting | 60 | Obesity: 4 weeks of oral clonidine vs hydrochlorothiazide vs placebo on inflammatory markers; no results yet |
| [NCT03065933](https://clinicaltrials.gov/study/NCT03065933) | Phase 4 | Terminated | 5 | Mania: open-label add-on of extended-release clonidine; terminated, no control arm |

## Literature Evidence

No literature was found for faciodigitogenital syndrome. Selected publications for the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Systematic review / network meta-analysis | Lancet Child & Adolescent Health | Compares drug treatments for Tourette syndrome in children and young adults |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Guideline | Eur Child Adolesc Psychiatry | European guideline update on pharmacological treatment of Tourette syndrome |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic review | Neurology | Treatment of tics in Tourette syndrome and chronic tic disorders |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Clinical study | Psychiatry Investigation | Clonidine patch in Tourette syndrome with comorbid ADHD |
| [37190511](https://pubmed.ncbi.nlm.nih.gov/37190511/) | 2023 | Systematic review | Brain Sciences | Efficacy and safety of clonidine in acute mania |
| [34990968](https://pubmed.ncbi.nlm.nih.gov/34990968/) | 2022 | Randomised, placebo-controlled study | J Psychiatr Res | Adjuvant clonidine in manic bipolar I disorder: effects on mania, sleep and cognition |
| [37350141](https://pubmed.ncbi.nlm.nih.gov/37350141/) | 2023 | Systematic review / meta-analysis | Cephalalgia | Blood-pressure-lowering drugs for episodic migraine prevention |
| [6998250](https://pubmed.ncbi.nlm.nih.gov/6998250/) | 1980 | Double-blind crossover trial | Acta Neurol Scand | Propranolol vs clonidine for migraine prophylaxis: no significant difference |
| [9931163](https://pubmed.ncbi.nlm.nih.gov/9931163/) | 1999 | Animal study | Hypertension | Clonidine prevented insulin resistance and hypertension in obese dogs |
| [18794888](https://pubmed.ncbi.nlm.nih.gov/18794888/) | 2010 | Animal study | Mol Psychiatry | Slitrk1-deficient mice show anxiety-like behaviour and noradrenergic abnormalities (trichotillomania candidate gene) |

## US Market Information

All 12 US authorizations are cancelled; none is currently valid. No approved indication text was available. The first five are listed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA200300 | Clonidine Hydrochloride (Hikma) | Injection, solution | Not available |
| ANDA070974 | Clonidine Hydrochloride (NuCare) | Tablet | Not available |
| ANDA202297 | Clonidine Hydrochloride (Bryant Ranch Prepack) | Tablet | Not available |
| ANDA070925 | Clonidine hydrochloride (Northwind Health) | Tablet | Not available |
| ANDA091368 | Clonidine hydrochloride (Alembic) | Tablet | Not available |

The remaining authorizations include a tablet (several), extended-release tablets, and transdermal patches (standard and extended-release).

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

- **Contraindication signals from the knowledge graph** (not label text): the graph links clonidine with conditions including hypotensive disorder, myocardial infarction and ischemia, heart conduction disease, sudden cardiac arrest, diabetes mellitus (types 1 and 2) and diabetic ketoacidosis, liver failure, pancreatitis, respiratory failure, anxiety and related disorders, and several metabolic conditions. These need verification against the label.
- **Drug interactions**: 100 interactions were found, and the 20 reviewed were all rated Moderate. They include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic drugs (insulin products, sulfonylureas such as glipizide, glimepiride and glyburide, and SGLT2 inhibitors such as canagliflozin, dapagliflozin and empagliflozin), and bupropion, morphine and dronabinol.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, faciodigitogenital syndrome)

**Rationale:**
- The top prediction has a very high model score but no trials, no literature and no plausible mechanism, so it is evidence level L5.
- Among the other predictions, Tourette syndrome has the strongest support (L2, Proceed with Guardrails). However, it rests on small Phase 4 trials, systematic reviews and guidelines, and is already a recognised use rather than a new repurposing finding. Obesity, migraine and manic bipolar disorder are research questions (L3). Specific developmental disorder and trichotillomania are L4, and the rest are L5.
- US authorizations are all cancelled, and label safety data is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which currently block safety screening
- Detailed mechanism of action data
- For Tourette syndrome: confirmation of a controlled Phase 3 trial or equivalent, and a decision on whether it counts as a new indication
- For the other predictions: controlled trial data (for mania, a larger controlled trial than the terminated n=5 study)
- Confirmation of current US market and route availability, since all authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

