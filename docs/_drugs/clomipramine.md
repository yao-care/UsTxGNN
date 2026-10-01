---
layout: default
title: Clomipramine
parent: Model Prediction Only (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Clomipramine
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

# Clomipramine: From Obsessive-Compulsive Disorder to Anxiety Disorder

## One-Sentence Summary

Clomipramine is a tricyclic antidepressant marketed in the US for obsessive-compulsive disorder (OCD).
The TxGNN model predicts it may be effective for **anxiety disorder**,
with **19 registered clinical trials** and **20 publications** retrieved. Nearly all of the trials are in OCD, and the panic and anxiety data come mainly from older publications.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obsessive-compulsive disorder (from the known US label; the license records supplied contain no indication text) |
| Predicted New Indication | Anxiety disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 (see the note under Clinical Trial Evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not supplied with this record. Based on known pharmacology, clomipramine is a potent serotonin reuptake inhibitor. Its active metabolite, desmethylclomipramine, also inhibits norepinephrine reuptake.

Serotonergic and noradrenergic modulation is the accepted mechanism in OCD, panic disorder and other anxiety-spectrum conditions. The drug's efficacy in OCD is well established. Since OCD shares features with the anxiety disorders, the model's prediction is biologically plausible.

The retrieved literature supports this direction. It includes a 2023 Cochrane network meta-analysis in panic disorder, and older placebo-controlled RCTs in panic disorder.

One caveat: OCD is not strictly classified as an anxiety disorder under DSM-5. Much of the trial evidence therefore reflects the drug's original indication rather than a true new indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Quetiapine vs clomipramine augmentation of SSRIs in SSRI-refractory OCD (open-label, small sample) |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Unknown | 76 | Randomized comparison of intravenous vs oral pulse-loaded clomipramine in OCD |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Completed | 54 | Double-blind trial of fluoxetine alone vs fluoxetine plus quetiapine vs fluoxetine plus clomipramine in OCD non-responders |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Completed | 44 | Quetiapine vs placebo added to SSRI/clomipramine in severe OCD |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Randomization to clomipramine or escitalopram to identify predictors of medication response in OCD |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | N/A | Completed | 144 | Adaptive treatment strategies for pediatric psychiatric disorders, including OCD pharmacotherapy |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Troriluzole vs placebo as add-on in OCD patients with inadequate response to an SSRI, clomipramine or venlafaxine (clomipramine is background therapy) |
| [NCT02431845](https://clinicaltrials.gov/study/NCT02431845) | N/A | Recruiting | 200 | Pharmacogenetic and omics study predicting SSRI response in OCD |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | Not yet recruiting | 80 | Hydroxyzine vs treatment as usual in panic disorder (clomipramine is not clearly an arm) |
| [NCT07488663](https://clinicaltrials.gov/study/NCT07488663) | N/A | Enrolling by invitation | 60 | Mechanistic study of treatment response in OCD using patient-derived stem cells (no efficacy data) |

Only two of the trials (NCT00564564 and NCT00004310) have clomipramine as a direct arm. Both are in OCD. No registered trial tests clomipramine in a classic anxiety disorder such as panic disorder. The assigned evidence level of L2 therefore relies mainly on the published literature. The only registered phase 2 trial has an unknown status.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Compares pharmacological treatments for panic disorder in adults |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week placebo-controlled comparison of paroxetine, clomipramine and cognitive therapy in panic disorder |
| [1474179](https://pubmed.ncbi.nlm.nih.gov/1474179/) | 1992 | Clinical trial | J Clin Psychopharmacol | Clomipramine, clonazepam and clonidine compared with a diphenhydramine control in OCD |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | Meta-analysis | J Am Acad Child Adolesc Psychiatry | Early treatment response to SSRIs and clomipramine in pediatric OCD |
| [8263222](https://pubmed.ncbi.nlm.nih.gov/8263222/) | 1993 | Meta-analysis | J Behav Ther Exp Psychiatry | 25 studies: clomipramine, fluoxetine and behavior therapy were all effective in OCD |
| [10221358](https://pubmed.ncbi.nlm.nih.gov/10221358/) | 1999 | Cohort | J Psychopharmacol | 41 panic disorder patients on clomipramine 50–200 mg/day; 97% were panic-free at 14 weeks (single-blind, uncontrolled) |
| [3887445](https://pubmed.ncbi.nlm.nih.gov/3887445/) | 1985 | Double-blind trial | Psychiatry Res | Clomipramine vs imipramine in 23 OCD outpatients; modest reductions in both groups |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Review | Drugs | Overview of pharmacology and use in OCD and panic disorder |
| [22204483](https://pubmed.ncbi.nlm.nih.gov/22204483/) | 2012 | Review | Curr Top Med Chem | Treatment strategies for OCD and panic disorder/agoraphobia |
| [7795952](https://pubmed.ncbi.nlm.nih.gov/7795952/) | 1995 | Review | J Child Adolesc Psychiatr Nurs | Clomipramine as the first effective agent in OCD, with side-effect management in youth |

## US Market Information

The US has 20 authorizations in total. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA213219 | Clomipramine Hydrochloride (Micro Labs) | Capsule | Not listed in the supplied record |
| NDA019906 | Anafranil (SpecGx) | Capsule | Not listed in the supplied record |
| ANDA208961 | Clomipramine Hydrochloride (Northstar Rx) | Capsule | Not listed in the supplied record |
| ANDA211822 | Clomipramine Hydrochloride (Alembic) | Capsule | Not listed in the supplied record |
| ANDA074694 | Clomipramine Hydrochloride (American Health Packaging) | Capsule | Not listed in the supplied record |

All listed products are oral capsules.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clomipramine's serotonergic mechanism is plausible for anxiety disorders, and older randomized studies in panic disorder and agoraphobia point in the same direction. However, the registered trials are almost all in OCD, none tests clomipramine in a classic anxiety disorder, and the panic evidence is mostly from the 1980s and 1990s. The same graph model also ranked agoraphobia, major depressive disorder and endogenous depression at L2, while the personality-disorder and torticollis predictions have essentially no supporting evidence (Hold).

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism-of-action data from DrugBank
- Confirmation of the approved indication text for the US labels
- A decision on whether OCD counts as the original indication or as part of the predicted anxiety-spectrum indication
- A drug-specific trial or systematic review of clomipramine in panic disorder or generalized anxiety
- A risk-benefit assessment against SSRIs, which are first-line for anxiety disorders, covering cardiac conduction, seizure threshold, suicidality warnings and anticholinergic effects

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

