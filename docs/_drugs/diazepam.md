---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 600
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety & Seizure Management to Insomnia

## One-Sentence Summary

Diazepam is a classic benzodiazepine historically established for anxiety disorders, alcohol withdrawal, muscle spasms, and seizure control.
The TxGNN model predicts it may be effective for **Insomnia**, with **24 clinical trials** and **18 publications** currently supporting this direction.
The mechanistic basis is well-founded, though meaningful long-term safety concerns — including dependence, disrupted sleep architecture, and cognitive impairment — substantially constrain its therapeutic application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Regulatory data not retrieved (known pharmacological uses: anxiety disorders, seizures, muscle spasms, alcohol withdrawal) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L2 |
| US Market Status | Data retrieval gap (0 NDA records found; Valium/Diazepam historically FDA-approved since 1963) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although the formal DrugBank mechanism of action record was not retrieved for this dataset, Diazepam's pharmacology is thoroughly characterized in published literature. Diazepam acts as a positive allosteric modulator (PAM) of the GABA-A receptor, binding to the benzodiazepine site between the α and γ subunits. This enhances the frequency of chloride channel opening in response to GABA, causing neuronal hyperpolarization and generalized CNS depression. The net effects include reduced sleep latency, increased total sleep time, and prolonged Stage 2 NREM sleep — making the hypnotic application pharmacologically straightforward and mechanistically inevitable.

The connection between Diazepam's established anxiolytic properties and insomnia is clinically meaningful because insomnia frequently co-occurs with anxiety. The hyperarousal state that delays sleep initiation is directly addressed by GABAergic inhibition. This is why benzodiazepines were historically the standard of care for insomnia before z-drugs (zolpidem, zaleplon) and dual orexin receptor antagonists became available. PMID 6113175, the most direct RCT in this dataset, confirms Diazepam's measurable hypnotic efficacy in patients with sleep-onset disorders — establishing it as the active benchmark comparator in subsequent insomnia research.

However, the prediction's near-perfect score (99.9997%) reflects mechanistic inevitability rather than unexplored potential. The principal concern is not short-term efficacy but long-term risk. Chronic use suppresses REM sleep and slow-wave sleep, disrupts NREM slow oscillations and spindle coupling critical for memory consolidation in older adults (PMID 40570297, 2025, *Sleep*), and impairs dendritic spine structural plasticity via mitochondrial TSPO activation, causing persistent cognitive decline in animal models (PMID 35228700, 2022, *Nature Neuroscience*). Current clinical guidelines position benzodiazepines as short-term bridging agents only, with CBTi (Cognitive Behavioral Therapy for Insomnia) as the preferred first-line treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Baclofen (GABA-B agonist) as adjunct to optimize Diazepam titration during BZD dependence treatment; Diazepam used as the reference standard, providing direct dosing and safety data relevant to insomnia management |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, Not Recruiting | 260 | Blinded vs. open-label BZD tapering combined with CBTi for chronic insomnia; evaluates discontinuation rates and the placebo contribution to hypnotic-dependent patients — defines boundary conditions for BZD use |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Ramelteon adjunct during (non-)BZD dose reduction algorithm for chronic insomnia; addresses transitional strategy from BZD to safer hypnotic alternatives |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | Acceptance and Commitment Therapy (ACT) vs. standard support added to BZD withdrawal program in adults with hypnotic-dependent insomnia; optimal withdrawal modalities assessed |
| [NCT07417813](https://clinicaltrials.gov/study/NCT07417813) | N/A | Recruiting | 121 | Lemborexant (dual orexin antagonist) for insomnia comorbid with psychiatric disorders; benchmarks next-generation agents against BZD/Z-drug background |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective Taiwanese cohort examining risk-benefit of BZD hypnotics in elderly patients; pharmacokinetics, clinical outcomes, and long-term safety — directly relevant to chronic insomnia management with BZDs |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel cognitive mechanisms for helping older adults discontinue hypnotics; demonstrates that tapering alone is insufficient — motivational and cognitive targets must also be addressed |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | Completed | 114 | PASSE-65+ psychosocial program for gradual BZD weaning in elderly; 12-week randomized trial demonstrating feasibility of structured discontinuation with psychological support |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Comparison of fast vs. slow BZD tapering in treatment-seeking insomnia patients; individual traits (anxiety sensitivity, personality) predicted successful discontinuation |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Antioxidant therapy combined with Adepsique® (amitriptyline + perphenazine + **diazepam**) for chronic tinnitus; direct diazepam-containing intervention arm with inflammatory cytokine and oxidative stress outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Double-blind 7-day trial (n=100): Lormetazepam 1 mg vs. **Diazepam 5 mg** for sleep disorders; Diazepam meaningfully reduced sleep latency and prolonged uninterrupted sleep, confirming direct hypnotic efficacy |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chem | Comprehensive review of GABA-A receptor modulators; Diazepam identified as the prototypical PAM with established activity for anxiety, epilepsy, and insomnia; sedation, tolerance, and dependence highlighted as key clinical limitations |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | Cohort Study | Sleep | Chronic BZD/BZRA use in older adults with insomnia significantly disrupts NREM slow oscillations and spindle coupling — functions critical for memory consolidation; supports strict short-term use only |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Preclinical | Nature Neuroscience | Long-term diazepam impairs dendritic spine structural plasticity via mitochondrial TSPO, increasing microglial engulfment and causing persistent cognitive impairment in mice; raises dementia risk concern for chronic use |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | Review | J Fam Pract | Systematic review of BZD therapy for insomnia in community-dwelling elderly; short-term sleep lab efficacy confirmed across 10 trials; long-term use associated with increased fall and injury risk |
| [6135990](https://pubmed.ncbi.nlm.nih.gov/6135990/) | 1983 | Review | N Engl J Med | Landmark NEJM review establishing clinical pharmacokinetics and rational prescribing of BZDs; forms the foundational evidence base for Diazepam as a hypnotic agent |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | Review/Guidelines | Drugs | Evidence-based guidelines for rational BZD use; recommends limiting hypnotic prescriptions to transient or short-term insomnia; longer half-life agents (including Diazepam) associated with greater daytime residual sedation and hangover |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Study | Cell Mol Biol Lett | Retrospective clinical analysis: prolonged BZDR use (Diazepam and Zolpidem) significantly exacerbates breast cancer risk; mechanistic evidence via GABA-A receptor signaling — safety signal for long-term use in women |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Review/Meta-analysis | Front Pharmacol | Meta-analysis of Suanzaoren formulae for insomnia RCTs; Diazepam consistently used as active comparator, affirming its benchmark hypnotic status in controlled insomnia research |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Animal Study | J Pharm Biomed Anal | Naoling Pian vs. Diazepam (positive control) in PCPA-induced insomnia rats; Diazepam produced significant sleep prolongation and behavioral normalization, validating its preclinical sedative-hypnotic efficacy profile |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diazepam has a well-established mechanistic basis for treating insomnia (GABA-A positive allosteric modulation → CNS inhibition → reduced sleep latency and increased sleep duration), confirmed by a direct RCT (PMID 6113175) and endorsed in multiple guideline-level reviews spanning four decades. The L2 evidence level is grounded in real clinical data. However, the core clinical evidence is aging (1980s–1990s), and more recent findings document significant long-term risks: disrupted sleep architecture, cognitive impairment, dependency, and potential oncological associations. Current clinical practice has largely transitioned to CBTi and newer pharmacological agents for chronic insomnia.

**To proceed, the following is needed:**
- Retrieve the US FDA package insert and complete NDA records via the FDA Orange Book (NDA 013263 for Valium and associated generics) to fill the US regulatory data gap
- Obtain formal DrugBank MOA documentation (DG002) for standardized mechanistic reporting
- Define a strict duration limit for any proposed use (2–4 weeks per current international guidelines)
- Establish clear patient exclusion criteria: adults aged ≥65 years, patients with prior or current substance use disorder, obstructive sleep apnea, and pregnant or nursing individuals
- Develop a pre-planned dose-tapering exit protocol to minimize discontinuation syndrome and rebound insomnia
- Evaluate whether this repurposing pathway provides incremental clinical value over already-approved alternatives (z-drugs, ramelteon, lemborexant/suvorexant) before committing to a formal development program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

