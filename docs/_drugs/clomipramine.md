---
layout: default
title: Clomipramine
parent: 僅模型預測 (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Clomipramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Clomipramine: From Obsessive-Compulsive Disorder to Anxiety Disorder

## One-Sentence Summary

Clomipramine is a tricyclic antidepressant (TCA) with the most potent serotonin reuptake inhibition among its class, historically established internationally as a first-line pharmacotherapy for obsessive-compulsive disorder (OCD) and depression, though it carries no current US FDA-approved NDA on record.
The TxGNN model predicts it may be effective for **Anxiety Disorder**, with **19 clinical trials** and **20 publications** currently supporting this direction.
Evidence strength is rated L1, anchored by completed Phase 3/4 randomized controlled trials, two Cochrane systematic reviews, and a 2023 Cochrane network meta-analysis in panic disorder.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | OCD and depression (established internationally; no current US FDA NDA on file) |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank MOA query returned no data). Based on established pharmacology, clomipramine is the tricyclic antidepressant with the strongest serotonin reuptake inhibition (SRI) activity in its class. Its efficacy in OCD — an anxiety-spectrum disorder — has been proven through landmark Phase 3 randomized controlled trials (notably the Clomipramine Collaborative Study Group), cementing its first-line status globally. In addition to 5-HT reuptake blockade, clomipramine inhibits norepinephrine (NE) reuptake, which contributes to suppression of generalized anxiety symptoms beyond OCD.

The mechanistic link between OCD and the broader anxiety disorder category is well-supported: 5-HT reuptake inhibition reduces fear responses mediated by the amygdala and modulates the orbitofrontal cortex–caudate nucleus circuit central to OCD. The same 5-HT/NE dual mechanism applies directly to panic disorder, where multiple direct RCTs spanning 1984–1999 and a 2023 Cochrane network meta-analysis (PMID 38014714) confirm clinical benefit. Agoraphobia, often comorbid with panic disorder, has also been directly studied with clomipramine (PMID 6373161, PMID 2651491).

The TxGNN prediction of 99.93% likelihood reflects the knowledge graph's recognition of this mechanistic proximity — clomipramine's established efficacy across OCD, panic disorder, and phobic anxiety creates a well-connected node cluster that maps naturally onto the broader anxiety disorder category.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Open-label RCT directly comparing quetiapine augmentation vs. clomipramine augmentation of SSRI in OCD patients with inadequate SSRI response; supports clomipramine as an evidence-based augmentation strategy |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Unknown | 76 | RCT evaluating IV pulse-loading vs. oral clomipramine followed by 12-week maintenance in OCD; specifically targets treatment-resistant cases with high relevance to refractory anxiety disorder |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Completed | 54 | Double-blind, double-dummy RCT comparing fluoxetine + quetiapine vs. fluoxetine + clomipramine augmentation in SSRI-nonresponsive OCD; provides controlled efficacy data for clomipramine combination use |
| [NCT02431845](https://clinicaltrials.gov/study/NCT02431845) | NA | Recruiting | 200 | Pharmaco(epi)genetic, proteomic, and microbiomic study in OCD; clomipramine as one of the study medications, providing mechanistic insight into biomarkers of treatment response |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | NA | Completed | 26 | RCT comparing clomipramine vs. escitalopram in OCD to identify clinical and biological predictors of medication response; informs personalized prescribing |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Double-blind, placebo-controlled RCT of troriluzole adjunct therapy in OCD patients with inadequate response to SSRI, clomipramine, or venlafaxine; large trial confirming clomipramine as standard comparator |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Completed | 44 | Placebo-controlled pilot RCT evaluating quetiapine added to SSRI/clomipramine baseline in adult OCD; supports clomipramine as backbone therapy |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | RCT testing whether CBT improves SRI (including clomipramine) treatment outcomes in pediatric OCD partial responders; demonstrates clomipramine utility in younger population |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | NA | Completed | 144 | Adaptive treatment strategies for pediatric OCD and psychiatric disorders; clomipramine and SSRIs as approved pharmacotherapy options; up to 30% of patients may not respond, highlighting need for alternatives |
| [NCT04708834](https://clinicaltrials.gov/study/NCT04708834) | Phase 3 | Terminated | 772 | Long-term open-label safety study of troriluzole adjunct in OCD with clomipramine as permitted background therapy; largest OCD trial in evidence pack (terminated early, safety data partially available) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Comprehensive network meta-analysis of all pharmacological treatments for adult panic disorder; evaluates relative efficacy and acceptability of clomipramine vs. SSRIs and other agents |
| [34582562](https://pubmed.ncbi.nlm.nih.gov/34582562/) | 2021 | Cochrane Systematic Review | Cochrane Database Syst Rev | Updated Cochrane review on pharmacotherapy for trichotillomania (OCD-spectrum disorder); systematic evaluation of clomipramine efficacy and tolerability vs. comparators |
| [24214100](https://pubmed.ncbi.nlm.nih.gov/24214100/) | 2013 | Cochrane Systematic Review | Cochrane Database Syst Rev | Earlier Cochrane review on pharmacotherapy for trichotillomania; first systematic evaluation establishing evidence base for clomipramine in OCD-spectrum conditions |
| [1474179](https://pubmed.ncbi.nlm.nih.gov/1474179/) | 1992 | RCT | J Clin Psychopharmacol | Placebo-controlled 4-arm RCT comparing clomipramine, clonazepam, clonidine, and diphenhydramine (control) in OCD; demonstrates significant clomipramine superiority over control |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week, placebo-controlled RCT directly comparing paroxetine, clomipramine, and cognitive therapy in DSM-III-R panic disorder with or without agoraphobia |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | Meta-analysis | J Am Acad Child Adolesc Psychiatry | Meta-analysis of early treatment response to SSRIs and clomipramine in pediatric OCD; clomipramine shows numerically superior efficacy with distinct time course |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Pharmacological Review | Drugs | Comprehensive overview of clomipramine pharmacological properties and clinical use in OCD and panic disorder; short-term trials confirm superiority over older TCAs for these indications |
| [3887336](https://pubmed.ncbi.nlm.nih.gov/3887336/) | 1985 | Review | Psychiatr Clin North Am | Foundational review establishing clomipramine as the first effective pharmacotherapy for OCD; discusses biological basis including serotonergic mechanism and genetic factors |
| [7795952](https://pubmed.ncbi.nlm.nih.gov/7795952/) | 1995 | Review | J Child Adolesc Psychiatr Nurs | Review of clomipramine in pediatric OCD management; covers dosing, SRI mechanism, response assessment, and clinical monitoring including cardiac and hepatic considerations |
| [22204483](https://pubmed.ncbi.nlm.nih.gov/22204483/) | 2012 | Review | Curr Top Med Chem | Review of treatment strategies for OCD and panic disorder/agoraphobia; positions clomipramine within the full pharmacotherapy landscape including SSRIs and combination approaches |

---

## US Market Information

Clomipramine (DrugBank ID: DB01242) currently holds no FDA-approved New Drug Applications (NDAs) in the United States. The drug is not marketed in the US market as of the data cutoff (2026-06-15). Clomipramine is approved and marketed in numerous other jurisdictions — including European Union member states and Japan — for indications including OCD, depressive illness, and panic disorder. Any clinical development or use in the US would require an Investigational New Drug (IND) application or equivalent regulatory pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence for clomipramine across the anxiety disorder spectrum is robust and spans multiple levels: completed Phase 3/4 RCTs in OCD, direct placebo-controlled RCTs in panic disorder and agoraphobia, two Cochrane systematic reviews in OCD-spectrum conditions, and a 2023 Cochrane network meta-analysis in panic disorder — collectively placing the evidence at L1. The dual 5-HT/NE reuptake mechanism provides strong, well-characterized biological plausibility for the TxGNN prediction. The "Guardrails" designation reflects the lack of US FDA approval, the well-known TCA safety profile (QTc prolongation, anticholinergic burden, seizure threshold lowering), and the need for structured safety monitoring.

**To proceed, the following is needed:**
- Detailed MOA data from DrugBank (remediation: DrugBank API query)
- US-equivalent package insert or authoritative safety labeling from a jurisdiction where clomipramine is approved (EU SmPC or Japan package insert) — required to complete key warnings and contraindications assessment
- Drug–drug interaction profile (DDI query returned no results; manual review or alternative DDI database query recommended)
- Cardiac safety monitoring protocol: baseline ECG with QTc assessment, periodic monitoring during titration
- Population-specific dosing guidance for high-risk groups (elderly patients, pediatric patients, those with pre-existing cardiac disease or seizure disorders)
- Regulatory pathway assessment for potential US IND filing, given zero current NDA holders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

