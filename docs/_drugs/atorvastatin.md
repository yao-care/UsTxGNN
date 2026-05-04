---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

---

# Atorvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Atorvastatin is a potent HMG-CoA reductase inhibitor (statin) used globally as first-line therapy for hypercholesterolemia and cardiovascular risk reduction, though no US FDA approval records were retrieved in the current data snapshot.
The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)** — this is consistent with atorvastatin's established global clinical use, making this prediction a strong validation of known efficacy rather than a novel repurposing hypothesis.
The prediction is supported by **35 clinical trials** and **19 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No US FDA records in current data snapshot |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| US Market Status | No records retrieved |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atorvastatin inhibits HMG-CoA reductase, the rate-limiting enzyme in the mevalonate pathway for hepatic cholesterol synthesis. By reducing intracellular cholesterol in hepatocytes, it triggers compensatory upregulation of LDL receptor expression on the hepatocyte surface, dramatically increasing clearance of circulating LDL particles. The net result is a 35–55% reduction in plasma LDL-C depending on dose (10–80 mg/day), alongside reduced VLDL production, lower triglycerides, and modest HDL-C elevation.

Familial Hypercholesterolemia (FH) is caused by loss-of-function mutations primarily in the *LDLR* gene — heterozygous FH (HeFH) and homozygous FH (HoFH) — leading to severely elevated LDL-C from birth and dramatically accelerated atherosclerotic cardiovascular disease. In HeFH, where residual LDL receptor function remains, atorvastatin achieves substantial LDL-C reduction and is universally recognized as the cornerstone of first-line treatment. In HoFH, the benefit is more limited due to near-absent receptor activity, but atorvastatin at maximum tolerated dose still forms the backbone of combination therapy with ezetimibe, PCSK9 inhibitors (alirocumab, evolocumab), lomitapide, or evinacumab.

**Critical context for this report:** The mechanistic rationale confirms that familial hypercholesterolemia is **atorvastatin's original, globally FDA/EMA-approved indication**, not a novel repurposing target. The TxGNN prediction score of 99.42% reflects this well-validated association. The complete absence of US FDA records in the current data snapshot (0 NDAs retrieved) represents a data collection gap — atorvastatin (Lipitor®) received US FDA approval in 1996 and is among the most prescribed drugs in history. This report should be read primarily as a data completeness flag rather than a scientific repurposing evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | Three-year prospective study of atorvastatin in children and adolescents (including ages 6–9) with HeFH; characterized long-term LDL-C reduction alongside growth, weight, and Tanner stage development |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Ezetimibe 10 mg added to atorvastatin 10 mg in HeFH or high-CV-risk patients with inadequate LDL-C control on atorvastatin monotherapy; assessed incremental lipid-lowering efficacy and safety |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe co-administered with atorvastatin or simvastatin in HoFH; demonstrated additive LDL-C reduction with acceptable tolerability in a genetically severe population |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab (PCSK9 inhibitor) add-on to maximally tolerated statin in HeFH; achieved significant LDL-C reduction vs placebo at 24 weeks |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab add-on to stable statin therapy in HeFH or high-CV-risk hypercholesterolemia; double-blind placebo-controlled design confirmed superiority for LDL-C reduction at 24 weeks |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab Q2W and Q4W vs placebo in HeFH children/adolescents (ages 8–17) on background statin; included 24-week double-blind and open-label extension to 104 weeks |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | Completed | 432 | Long-term safety and tolerability (up to 12 months) of ezetimibe added to atorvastatin 10–80 mg/day in HeFH patients with CHD or multiple cardiovascular risk factors |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Four-arm RCT comparing alirocumab vs ezetimibe added to atorvastatin vs atorvastatin dose escalation vs switch to rosuvastatin in patients uncontrolled on atorvastatin (HeFH and non-FH) |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Completed | 39 | Pharmacokinetics, pharmacodynamics, safety, and tolerability of atorvastatin over 8 weeks in children and adolescents with HeFH; informed pediatric dosing recommendations |
| [NCT02460159](https://clinicaltrials.gov/study/NCT02460159) | Phase 3 | Completed | 135 | Long-term safety of ezetimibe 10 mg/atorvastatin 10 mg and 10/20 mg fixed-dose combination in Japanese patients with hypercholesterolemia uncontrolled on statin or ezetimibe monotherapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocrine Practice | AACE/ACE dyslipidemia and CVD prevention guidelines; statins are first-line therapy for all FH phenotypes with defined LDL-C targets |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort Study | JACC | Statin therapy in HeFH registry cohort significantly reduced coronary artery disease events and all-cause mortality; confirms cardiovascular benefit beyond LDL-C reduction |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Prospective Study | J Clin Lipidol | Three-year atorvastatin treatment in HeFH children and adolescents confirmed sustained LDL-C reduction without adverse effects on growth, puberty staging, or laboratory safety |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Trial | Nutr Metab Cardiovasc Dis | Atorvastatin was superior to simvastatin in achieving NCEP LDL-C goals in HeFH patients; also produced significant reductions in plasma fibrinogen |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Clinical Study | Echocardiography | Atorvastatin improved coronary flow reserve and peripheral blood flow in FH patients without overt atherosclerosis, demonstrating pleiotropic vascular benefits beyond cholesterol lowering |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Clinical Trial Review | Ann Pharmacother | Early comprehensive review of atorvastatin efficacy and safety across primary hypercholesterolemia and mixed dyslipidemias; established the dose–response LDL-C reduction profile |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | JACC | Recommendations for improving FH monitoring and care; emphasized maximizing statin dose before adding ezetimibe or PCSK9 inhibitors |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | Novel therapies for HoFH (inclisiran, evinacumab, gene therapy approaches) reviewed; statins remain the essential treatment backbone regardless of new add-ons |
| [36928267](https://pubmed.ncbi.nlm.nih.gov/36928267/) | 2023 | Cohort Study | J Atheroscler Thromb | Real-world LDL-C goal achievement in high-risk Japanese patients; identified significant gaps in statin utilization and titration in clinical practice |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic Cohort Study | Pharmacogenomics J | Combined NGS panel integrating FH genetic diagnosis with statin pharmacogenomic variants enables personalized statin selection and dose optimization |

---

## US Market Information

No US FDA approval records were retrieved for atorvastatin in the current data snapshot (0 NDAs on file). This does not reflect the actual regulatory status. Atorvastatin calcium (Lipitor®, Pfizer) received US FDA approval in December 1996 and is one of the most widely prescribed medications in history, with both branded and numerous generic approvals. The absence of records is a **data pipeline gap** and does not indicate a filing or approval issue.

Supplemental data retrieval from the FDA Drugs@FDA database (NDA 020702 and associated ANDAs) is required to populate this section correctly.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Familial hypercholesterolemia is atorvastatin's established, globally approved original indication, backed by L1-level evidence from multiple completed Phase 3 RCTs and over 25 years of post-marketing clinical experience. The "guardrails" in this case are not driven by scientific uncertainty — they reflect critical gaps in the current data capture (missing FDA records, missing safety and DDI data) that must be resolved before any downstream decision-making or clinical use.

**To proceed, the following is needed:**

- **FDA record retrieval:** Pull US NDA and ANDA records for atorvastatin from FDA Drugs@FDA (NDA 020702 as starting point) to complete the US market information section
- **Package insert safety data:** Obtain full US prescribing information including warnings (myopathy, hepatotoxicity), contraindications (active liver disease, pregnancy), and drug interactions (CYP3A4 inhibitors, fibrates, cyclosporine)
- **DrugBank MOA data:** Complete the DrugBank API query to formally document the HMG-CoA reductase inhibition mechanism and pharmacokinetics
- **DDI database query:** Re-run drug interaction search against a complete DDI source; atorvastatin has clinically significant interactions with multiple antiretrovirals, antifungals, and immunosuppressants that require documentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

