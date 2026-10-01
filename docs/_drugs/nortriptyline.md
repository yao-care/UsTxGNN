---
layout: default
title: Nortriptyline
parent: High Evidence (L1-L2)
nav_order: 977
evidence_level: L2
indication_count: 2
---

# Nortriptyline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

# Nortriptyline: From Depression to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Nortriptyline is a tricyclic antidepressant, and the supplied literature describes it as widely used for depression. The record itself lists no approved indication text.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**. Support consists of **0 registered clinical trials** and **20 publications**, including a small controlled pediatric study and a Cochrane review of tricyclics.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US label data (depression, per general pharmacology and PMID 24345533) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. From general pharmacology, nortriptyline mainly inhibits norepinephrine reuptake and inhibits serotonin reuptake more weakly. A PET study in the literature (PMID 24345533) describes it as a norepinephrine transporter (NET)-selective tricyclic antidepressant.

This noradrenergic action overlaps with that of non-stimulant ADHD drugs such as atomoxetine. A review of non-stimulant treatments (PMID 15064003) notes that the compounds with documented anti-ADHD activity share noradrenergic/dopaminergic activity. It also names the secondary-amine tricyclics, including nortriptyline, as established alternatives. Depression and ADHD are both treated through monoamine modulation, so the prediction is mechanistically plausible.

The high TxGNN score (0.994) is consistent with this rationale but is not evidence of efficacy. Clinical support comes from the literature: one controlled study in children and adolescents (PMID 11052409), a Cochrane review of tricyclics for ADHD (PMID 25238582), and older uncontrolled studies. Guidelines and safety reviews place tricyclics as second- or third-line options because of cardiovascular and anticholinergic tolerability concerns. The sample size and effect size of the controlled study could not be verified from the supplied data.

The model also predicted the subtype "ADHD, inattentive type" (score 99.33%). It has no trials or literature of its own (Level L5). It should probably be merged with the parent ADHD indication and not evaluated as an independent candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Only the first 10 publications are listed, chosen by study type (RCT > review > uncontrolled study). Where the abstract was not supplied, the summary is based on the title only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT (small, pediatric) | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline's efficacy and tolerability in children and adolescents with ADHD; results not in the supplied abstract |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT (double-blind) | Pediatr Nephrol | Nortriptyline for enuresis in children with ADHD; addresses enuresis, not core ADHD symptoms |
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Cochrane systematic review | Cochrane Database Syst Rev | Reviews tricyclic antidepressants as second-line treatment for reducing ADHD symptoms in children and adolescents |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Clinical practice guideline | Ann Clin Psychiatry | CANMAT recommendations for mood disorders with comorbid adult ADHD |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatr Clin North Am | Nonstimulant treatment of adult ADHD; nortriptyline is a recognized alternative, but a narrow therapeutic index and cardiovascular toxicity limit tricyclic use |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Review | Expert Opin Drug Saf | Safety of non-stimulant ADHD agents; stimulants remain first choice, atomoxetine second-line |
| [7807071](https://pubmed.ncbi.nlm.nih.gov/7807071/) | 1995 | Systematic assessment | J Nerv Ment Dis | Assessment of tricyclic antidepressants in adult ADHD (abstract not supplied) |
| [8444763](https://pubmed.ncbi.nlm.nih.gov/8444763/) | 1993 | Chart review (58 cases) | J Am Acad Child Adolesc Psychiatry | Evaluated potential benefit of nortriptyline in children and adolescents with ADHD |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Uncontrolled clinical study | J Am Acad Child Adolesc Psychiatry | Nortriptyline in children with ADHD and tic disorder or Tourette's syndrome |
| [24345533](https://pubmed.ncbi.nlm.nih.gov/24345533/) | 2014 | PET mechanism study | Int J Neuropsychopharmacol | NET occupancy by nortriptyline in patients with depression; supports its NET-selective action |

---

## US Market Information

Five of the 20 licenses are shown. The supplied data contains no approved indication text for any of them, and all are oral capsules.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA073556 | Nortriptyline Hydrochloride (Asclemed USA, Inc.) | Capsule | Not provided |
| ANDA074132 | Nortriptyline Hydrochloride (Preferred Pharmaceuticals Inc.) | Capsule | Not provided |
| ANDA073556 | Nortriptyline Hydrochloride (PD-Rx Pharmaceuticals, Inc.) | Capsule | Not provided |
| ANDA074132 | Nortriptyline Hydrochloride (Direct Rx) | Capsule | Not provided |
| ANDA073556 | Nortriptyline Hydrochloride (REMEDYREPACK INC.) | Capsule | Not provided |

---

## Safety Considerations

Package insert warnings and contraindications were not captured, and no drug interaction data was found. Please refer to the package insert for safety information.

The literature does flag one class-level concern: tricyclic antidepressants have a narrow therapeutic index and potential cardiovascular toxicity that have limited their use in ADHD (PMID 15064003).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature supports plausibility. It includes a controlled pediatric study and a Cochrane review, but there are no registered trials. Tricyclics are positioned as second- or third-line options in ADHD because of tolerability concerns. Package insert safety data is missing, which blocks the safety screen.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, downloaded and parsed from the FDA label
- Detailed mechanism of action data (query the DrugBank API)
- Full-text review of the controlled study (PMID 11052409) and the Cochrane review (PMID 25238582) to confirm design, sample size and effect size
- A cardiovascular and anticholinergic safety assessment for the ADHD population, especially children
- Merger of the "inattentive type" entry into the parent ADHD indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

