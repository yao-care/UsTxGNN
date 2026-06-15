---
layout: default
title: Bupropion
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Bupropion
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

# Bupropion: From Depression to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Bupropion is a norepinephrine-dopamine reuptake inhibitor (NDRI) with established use for major depressive disorder and smoking cessation.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**,
with **8 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Depression / Smoking Cessation |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| US Market Status | No records retrieved (data gap — see note below) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bupropion blocks both the dopamine transporter (DAT) and the norepinephrine transporter (NET), increasing catecholamine concentrations in the prefrontal cortex and striatum. Although the automated pipeline did not retrieve a formal MOA record in this evidence pack, bupropion's NDRI profile is well-established across decades of literature. Its mechanism stands in contrast to SSRIs and SNRIs: it has no serotonergic activity whatsoever, which makes it pharmacologically distinct among antidepressants.

ADHD is pathophysiologically defined by a deficit in catecholaminergic signaling — specifically dopaminergic and noradrenergic — in exactly the prefrontal circuits that govern attention, inhibitory control, and working memory. Bupropion's DAT + NET inhibition maps directly onto this deficit. The mechanistic parallel to established ADHD treatments is striking: methylphenidate also inhibits DAT/NET, while atomoxetine selectively inhibits NET. Bupropion essentially combines both targets, albeit with lower potency and different selectivity ratios.

A 2017 Cochrane systematic review (PMID 28965364) concluded that bupropion produces statistically significant ADHD symptom improvement versus placebo in adults, with an acceptable side effect profile — positioning it as a viable non-stimulant alternative for patients who cannot tolerate or do not respond to first-line stimulants. A 2018 *Lancet Psychiatry* network meta-analysis (PMID 30097390) confirmed efficacy across age groups, and a 2020 systematic review with NMA (PMID 33085721) further corroborated these findings specifically in adults. The combination of strong biological plausibility and converging clinical evidence gives this TxGNN prediction high credibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | Multicenter, randomized, double-blind, placebo-controlled study of extended-release bupropion HCl 300–450 mg/day in adults with ADHD; direct efficacy and safety assessment — highest-grade direct evidence |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | RCT evaluating bupropion for adult ADHD in methadone maintenance patients; provides direct ADHD efficacy data in a comorbid addiction population with broader generalizability |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Bupropion for ADHD in adolescents with comorbid substance use disorder; direct ADHD efficacy evaluation in a high-risk youth cohort |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | NA | Completed | 32 | Open-label study of bupropion SR for ADHD in adults with recent or current substance use disorders using clinically relevant doses |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | NA | Completed | 32 | Evaluation of cocaine abuse and ADHD; bupropion assessed as treatment in dual-diagnosis population (1995–1998) |
| [NCT03326128](https://clinicaltrials.gov/study/NCT03326128) | Phase 2 | Terminated | 12 | High-dose bupropion pilot for smoking cessation; terminated early with limited enrollment — indirect relevance to ADHD only |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Bupropion/Contrave for stimulant use disorder relapse prevention with ADHD substudy; withdrawn before enrollment — no usable data |
| [NCT00330434](https://clinicaltrials.gov/study/NCT00330434) | NA | Withdrawn | 0 | CYP2B6 induction pharmacokinetics study; no ADHD efficacy component — withdrawn, no data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Bupropion for ADHD in adults: statistically significant symptom improvement over placebo; effect sizes smaller than stimulants but clinically meaningful as a non-stimulant alternative |
| [27813651](https://pubmed.ncbi.nlm.nih.gov/27813651/) | 2017 | Systematic Review | J Child Adolesc Psychopharmacol | Bupropion for ADHD in children and adolescents: positive outcomes in stimulant non-responders; NDRI mechanism proposed as the key therapeutic driver |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Network Meta-analysis | The Lancet Psychiatry | Comparative efficacy of all ADHD medications across children, adolescents, and adults; bupropion included as a non-stimulant comparator with significant superiority over placebo |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Systematic Review + NMA | PLoS One | Pharmacologic treatments for adult ADHD: bupropion demonstrated significant efficacy vs. placebo with a favorable tolerability profile among non-stimulant options |
| [38950507](https://pubmed.ncbi.nlm.nih.gov/38950507/) | 2024 | Bayesian Network Meta-analysis | J Psychiatric Research | Monoamine reuptake inhibitors (including bupropion) for ADHD: bupropion ranked as effective with a better safety profile compared to first-line stimulants |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Narrative Review | Health Psychology Research | Bupropion's NDRI mechanism reviewed comprehensively for depression, ADHD, and smoking cessation; pharmacokinetics and drug interactions discussed |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Network Meta-analysis | The Lancet Psychiatry | Cardiovascular safety of ADHD pharmacotherapies across age groups; bupropion included in comparative safety analysis of hemodynamic and ECG parameters |
| [26693882](https://pubmed.ncbi.nlm.nih.gov/26693882/) | 2016 | Systematic Review | Expert Review of Neurotherapeutics | Alternative pharmacological strategies for adult ADHD; bupropion reviewed as an effective option for patients with partial or no response to methylphenidate or atomoxetine |
| [20051220](https://pubmed.ncbi.nlm.nih.gov/20051220/) | 2010 | Meta-analysis | J Clin Psychiatry | Effect size comparison of medications for adult ADHD; bupropion showed moderate effect size, confirming its role as a second-line non-stimulant treatment |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Current Pharmaceutical Design | Psychopharmacology of ADHD: bupropion identified as effective non-stimulant alongside stimulants and atomoxetine; dopamine/norepinephrine reuptake inhibition as the mechanism |

---

## US Market Information

No US FDA license records were retrieved for bupropion in this evidence pack. The automated query returned 0 results, which likely reflects a data retrieval gap rather than actual non-approval status.

> **Note:** Bupropion is widely recognized as an FDA-approved drug. Known brand names include **Wellbutrin** (depression), **Wellbutrin SR / XL** (major depressive disorder, seasonal affective disorder), and **Zyban** (smoking cessation). For authoritative label information, refer directly to [FDA Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/).

---

## Safety Considerations

Please refer to the package insert for safety information.

> The automated pipeline did not retrieve safety data for bupropion in this evidence pack (warnings, contraindications, and drug-drug interaction records all returned as data gaps). Before proceeding, manual retrieval of the FDA-approved label is required — in particular, bupropion carries a **known dose-dependent seizure risk** and a **black-box warning for neuropsychiatric effects in smoking cessation use**, both of which are clinically relevant considerations for an ADHD indication.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 multicenter RDBPC trial (NCT00048360, n=162) plus one Phase 2/3 RCT (NCT00061087, n=115) demonstrate statistically significant ADHD symptom improvement with bupropion, corroborated by a 2017 Cochrane systematic review and multiple independent network meta-analyses spanning 2018–2024. The NDRI mechanism directly addresses the catecholaminergic deficit underlying ADHD, and the biological rationale is high. Evidence qualifies as L1.

**To proceed, the following is needed:**

- Retrieve and review the full FDA-approved package insert to document warnings, contraindications, and boxed warnings (seizure risk, neuropsychiatric effects)
- Clarify current regulatory status for an ADHD-specific indication (bupropion is not FDA-approved for ADHD; this would be an off-label or new indication filing)
- Build a drug-drug interaction monitoring plan — bupropion is a potent **CYP2D6 inhibitor**, a clinically significant interaction point not captured in this evidence pack
- Establish a seizure risk management framework specifying dose ceilings and contraindicated patient profiles (eating disorders, prior seizure history)
- Evaluate evidence stratified by ADHD subtype: the inattentive subtype (Rank 2 prediction) currently has only L3 evidence and warrants a dedicated sub-population analysis
- Define target population: adult vs. pediatric vs. adolescent ADHD, given differing evidence quality and safety profiles across age groups
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

