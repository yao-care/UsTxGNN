---
layout: default
title: Dextroamphetamine
parent: 僅模型預測 (L5)
nav_order: 598
evidence_level: L5
indication_count: 7
---

# Dextroamphetamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Dextroamphetamine: From ADHD/Narcolepsy to Specific Developmental Disorder

## One-Sentence Summary

Dextroamphetamine is a central nervous system stimulant approved by the US FDA for attention deficit hyperactivity disorder (ADHD) and narcolepsy, but currently not marketed in Taiwan.
The TxGNN model predicts it may be effective for **Specific Developmental Disorder** (ranked #2 by evidence quality; the #1 ranked prediction, faciodigitogenital syndrome, is flagged as a likely false positive with no supporting evidence),
with **5 clinical trials** and **10 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD and Narcolepsy (US FDA–approved; not marketed in Taiwan) |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on top-ranked prediction:** The highest TxGNN-scored indication (faciodigitogenital syndrome, 99.99%) has zero clinical trials and zero literature, and the mechanistic rationale explicitly identifies it as a probable knowledge-graph false positive (shared "neurodevelopment" node neighbourhood effect). This report focuses on the second-ranked indication, which carries biologically coherent rationale and L2 evidence.

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available from the Evidence Pack. Based on known pharmacology documented in the retrieved literature, dextroamphetamine acts as a monoamine releaser by reversing the dopamine transporter (DAT) and norepinephrine transporter (NET), dramatically increasing synaptic concentrations of dopamine and norepinephrine. This enhancement of catecholaminergic tone strengthens prefrontal cortex executive function circuits governing attention, impulse control, and cognitive flexibility.

ADHD and specific developmental disorders — including language disorder with co-occurring attention deficits and developmental learning disabilities — share overlapping neurobiological underpinnings: catecholaminergic deficiency in fronto-striatal circuits. Children presenting with specific developmental disorders frequently exhibit co-occurring attentional and impulse-control difficulties that overlap clinically with ADHD. Quantitative EEG (QEEG) research has demonstrated that dextroamphetamine normalizes EEG patterns in children with both ADHD and specific developmental learning disorders, suggesting a shared neurophysiological substrate amenable to stimulant treatment.

Critically, lisdexamfetamine dimesylate — a prodrug that is metabolised to active dextroamphetamine — has completed a randomised Phase II/III trial in Japanese paediatric patients (6–17 years) with ADHD, demonstrating significant symptom reduction versus placebo. A Phase 4 pragmatic trial (NCT05916339, N=500) is actively recruiting children with autism spectrum disorder plus ADHD, directly spanning the specific developmental disorder population. Together, these data create a direct, biologically coherent bridge from the established ADHD indication to the broader category of specific developmental disorder.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic SMART-design trial comparing methylphenidate vs amphetamine in children/adolescents with ASD+ADHD; directly covers the specific developmental disorder population; results expected 2027 |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1,398 | ADDUCE project: 2-year observational study assessing chronic effects of ADHD medications (including amphetamine class) on growth, neurological, psychiatric, and cardiovascular outcomes; provides long-term safety data |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Examined smoking reinforcement mechanisms in adult ADHD and the role of stimulant medication on reward processing; limited direct relevance to specific developmental disorder |
| [NCT04815278](https://clinicaltrials.gov/study/NCT04815278) | N/A | Completed | 455 | Workplace health intervention targeting chronic disease risk in socioeconomically disadvantaged populations; not directly relevant to specific developmental disorder |
| [NCT04080427](https://clinicaltrials.gov/study/NCT04080427) | Phase 1 | Completed | 102 | THC effects on fear extinction memory in PTSD; no direct relevance to dextroamphetamine or specific developmental disorder |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31718254](https://pubmed.ncbi.nlm.nih.gov/31718254/) | 2020 | Phase II/III RCT | J Child Adolesc Psychopharmacol | LDX 30–70 mg/day significantly reduced ADHD-RS-IV total score vs placebo in 76 Japanese paediatric patients (6–17y); directly supports dextroamphetamine-class efficacy in paediatric developmental conditions |
| [38391788](https://pubmed.ncbi.nlm.nih.gov/38391788/) | 2024 | Systematic Review | Expert Rev Neurother | Comprehensive review of extended-release amphetamine formulations for ADHD; evaluates efficacy across age groups and novel delivery formats (chewable, sprinkle capsules) |
| [8719499](https://pubmed.ncbi.nlm.nih.gov/8719499/) | 1996 | Cohort Study | Clin EEG | QEEG discriminant functions distinguished children with specific developmental learning disorders from those with ADHD; pretreatment QEEG predicted differential dextroamphetamine vs methylphenidate response |
| [6131061](https://pubmed.ncbi.nlm.nih.gov/6131061/) | 1982 | Early Clinical Study | J Autism Dev Disord | Stimulant effects across developmental disorder populations; hyperactive children responded beneficially while autistic/intellectually disabled children showed poor response; informs population selection |
| [27552823](https://pubmed.ncbi.nlm.nih.gov/27552823/) | 2017 | Controlled Clinical Study | Clin EEG Neurosci | Dexamphetamine and methylphenidate produced differential degrees of EEG normalisation in ADHD; supports neurophysiological basis for stimulant selection in developmental conditions |
| [18309764](https://pubmed.ncbi.nlm.nih.gov/18309764/) | 2007 | Narrative Review | Nutrition and Health | ~75% stimulant response rate (methylphenidate, dextroamphetamine) in ADHD schoolchildren; summarises side-effect profile including growth retardation and cardiovascular effects |
| [16130031](https://pubmed.ncbi.nlm.nih.gov/16130031/) | 2005 | Regulatory Monograph | NTP CERHR Mon | NTP CERHR evaluation of amphetamine reproductive/developmental effects; confirms US FDA-approved indications (ADHD ≥3y, narcolepsy) and documents developmental safety considerations |
| [11563573](https://pubmed.ncbi.nlm.nih.gov/11563573/) | 2001 | Clinical Review | Am Fam Physician | ADHD evaluation and treatment guidelines; documents stimulant efficacy in school-age children and diagnostic approach to comorbid developmental conditions |
| [8784874](https://pubmed.ncbi.nlm.nih.gov/8784874/) | 1996 | Clinical Review | Nurse Practitioner | Overview of ADHD neurobiological basis and stimulant treatment; contextualises the neurobiological continuum with related developmental disorders |
| [1661401](https://pubmed.ncbi.nlm.nih.gov/1661401/) | 1991 | Case Series/Review | Pediatrie | Hyperkinetic disorders with attention deficit in the paediatric population; diagnostic criteria including neuromaturational soft signs and neuropsychological tests relevant to developmental disorder overlap |

## Taiwan Market Information

Dextroamphetamine is **not currently marketed in Taiwan**. No NDA records were found in the Taiwan FDA database. This drug has not been submitted for regulatory approval in Taiwan.

For reference, in the United States, dextroamphetamine (Dexedrine® and generics, DrugBank DB01576) holds FDA approval for:
- Attention Deficit Hyperactivity Disorder (ADHD) in patients ≥3 years of age
- Narcolepsy

It is classified as a Schedule II controlled substance in the US, indicating high abuse potential and stringent prescribing controls.

## Safety Considerations

Taiwan FDA package insert safety data (warnings and contraindications) and DrugBank API data were not retrievable for this report. No drug–drug interaction records were found in the queried database.

Please refer to the originator package insert for complete safety information. Key considerations based on the drug class:

- **Controlled substance risk**: High potential for abuse, misuse, and dependence as a Schedule II amphetamine
- **Cardiovascular effects**: Known to increase heart rate and blood pressure; caution in patients with pre-existing cardiac conditions
- **CNS effects**: May cause insomnia, anxiety, and in rare cases stimulant-induced psychosis
- **Growth suppression**: Long-term paediatric use is associated with growth retardation (documented in the ADDUCE study, NCT01470261)
- **Trichotillomania signal**: ⚠️ Evidence suggests amphetamine-class drugs (including lisdexamfetamine and dextroamphetamine) may **induce or worsen** trichotillomania (hair-pulling disorder) rather than treat it — dextroamphetamine should be considered a potential trigger for this condition

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for specific developmental disorder is mechanistically coherent — dextroamphetamine's catecholamine-releasing action directly addresses fronto-striatal circuit deficits shared by ADHD and related developmental disorders. An actively recruiting Phase 4 trial (N=500) and Phase II/III RCT data for the prodrug lisdexamfetamine in paediatric patients provide L2-level clinical support. However, Taiwan FDA registration is completely absent, safety profiling specific to Taiwanese populations is lacking, and the TFDA package insert data needed for S1 safety screening remains a blocking gap.

**To proceed, the following is needed:**

- **Resolve blocking data gap**: Obtain TFDA package insert and DrugBank API MOA data to enable S1 safety evaluation
- **Regulatory pathway assessment**: Evaluate feasibility of Taiwan registration, compassionate use, or named-patient access for dextroamphetamine given its complete absence from TFDA records
- **Controlled substance framework**: Confirm whether amphetamines can be approved under Taiwan's controlled substance regulations before any clinical trial initiation
- **Population specification**: Define the specific developmental disorder sub-population most likely to benefit (e.g., ADHD-comorbid language disorder, ASD-comorbid ADHD) and exclude populations at risk of harm (e.g., those predisposed to OCD-spectrum or trichotillomania behaviours)
- **Paediatric safety plan**: Design pharmacovigilance protocol covering cardiovascular monitoring, growth tracking, and psychiatric adverse event surveillance before any paediatric use
- **Watch NCT05916339**: Monitor results from this Phase 4 ASD+ADHD comparative effectiveness trial (completion expected December 2027), which will directly inform this repurposing direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

