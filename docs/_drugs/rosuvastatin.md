---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 1136
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-29
monitor_inn: "ROSUVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
description: "Rosuvastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Rosuvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rosuvastatin: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Rosuvastatin is a statin (HMG-CoA reductase inhibitor) originally used for hyperlipidemia, hypertriglyceridemia, homozygous familial hypercholesterolemia, and atherosclerosis-related conditions such as stroke.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein deficiency** (the top-ranked prediction). The best-supported prediction is **Familial Hypercholesterolemia**, with **12 clinical trials** and **12 publications** compiled for this report, although this overlaps heavily with its existing indications.

> Note: The top-ranked prediction (rank 1) has no trials or literature at all. This report therefore also covers the best-supported prediction (rank 2, familial hypercholesterolemia) in detail and summarises the other candidates.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 (CETP deficiency); L1 (familial hypercholesterolemia) |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | 9 (all ANDAs, all cancelled) |
| Recommended Decision | Hold (CETP deficiency); Proceed with Guardrails (familial hypercholesterolemia) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, rosuvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis, upregulates hepatic LDL receptors, and increases clearance of LDL cholesterol.

**Familial hypercholesterolemia (FH):** This condition involves impaired LDL clearance, which is exactly the pathway rosuvastatin acts on. It also overlaps with the original labeled indications (homozygous FH), so it is closer to an on-label use than true repurposing.

**CETP deficiency (top-ranked):** CETP deficiency raises HDL-C and alters lipoprotein metabolism. A lipid-pathway link is plausible, but it is unsupported: there are no trials and no literature in the compiled data. The high score is a computational prediction only.

Other predictions have weaker links. Hepatic lipase deficiency and CYP7A1 deficiency are plausible lipid-pathway fits but lack direct evidence. Brain stem infarction relies on indirect statin pleiotropic effects. HIV-associated cardiovascular risk is relevant mainly as dyslipidemia and cardiovascular risk management, not infection treatment. ABri amyloidosis and the rare neurodevelopmental disorder show no evident mechanistic rationale.

---

## Clinical Trial Evidence

### Familial hypercholesterolemia (best-supported prediction)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | Completed | 1500 | 48-week open-label study of rosuvastatin efficacy and safety in type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Randomised study of renal effects of rosuvastatin vs simvastatin in dyslipidaemia, including heterozygous FH |
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | Completed | 315 | 2-year open-label efficacy and safety study in children and adolescents (6 to <18 years) with FH |
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | Completed | 173 | Double-blind, placebo-controlled study of LDL-C reduction in children aged 10-17 with heterozygous FH, with 40-week open-label follow-up |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Completed | 20 | Double-blind, placebo-controlled crossover study in children and adolescents with homozygous FH |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | Completed | 9 | Open-label long-term safety extension in children with homozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs placebo in heterozygous FH; whether rosuvastatin is the studied agent or background therapy is not confirmed |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab in children with heterozygous FH on background statin therapy; rosuvastatin is not the studied agent |
| [NCT06910098](https://clinicaltrials.gov/study/NCT06910098) | N/A | Completed | 195 | Dose-response of rosuvastatin on LDL, CPK, and AST levels |
| [NCT07474649](https://clinicaltrials.gov/study/NCT07474649) | Phase 3 | Not yet recruiting | 103 | Bempedoic acid/ezetimibe/high-intensity statin (atorvastatin or rosuvastatin) on coronary plaque; no results |

### Other predicted indications (summary)

- **HIV infectious disease:** 15 trials compiled. The most direct is [NCT01218802](https://clinicaltrials.gov/study/NCT01218802), a Phase 2 randomised placebo-controlled trial (n=147) of rosuvastatin for cardiovascular risk and inflammation in HIV-infected people. Several others are Phase 1/2 pharmacokinetic interaction studies with antiretrovirals, and [NCT00673582](https://clinicaltrials.gov/study/NCT00673582) was terminated.
- **Hyperlipidemia:** more than 30 trials compiled, including large Phase 3 comparisons such as [NCT00653744](https://clinicaltrials.gov/study/NCT00653744) (rosuvastatin vs atorvastatin, n=1700) and [NCT04669041](https://clinicaltrials.gov/study/NCT04669041) (ezetimibe/rosuvastatin combination, n=305). This is on-label use.
- **Hypoalphalipoproteinemia:** two trials were compiled, but neither tests rosuvastatin for this condition ([NCT04776889](https://clinicaltrials.gov/study/NCT04776889) concerns prostate cancer; [NCT07629999](https://clinicaltrials.gov/study/NCT07629999) is an unrelated first-in-human study).
- **CETP deficiency, CYP7A1-deficiency hypercholesterolemia, brain stem infarction, hepatic lipase deficiency, ABri amyloidosis, and the neurodevelopmental disorder:** no related clinical trials registered.

---

## Literature Evidence

### Familial hypercholesterolemia

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | RCT | J Am Coll Cardiol | Efficacy and safety of rosuvastatin in children with familial hypercholesterolemia |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | Rosuvastatin efficacy in children with homozygous FH and its association with underlying genetic mutations |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | Pharmacokinetic study | Eur J Clin Pharmacol | Population pharmacokinetics in paediatric heterozygous FH (CHARON study) |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin superior to atorvastatin, simvastatin, and pravastatin in lipid profile improvement; low propensity for drug interactions |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in primary hypercholesterolemia, mixed dyslipidemia, and homozygous FH |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Laboratory study | Toxicology | Statin-induced myotoxicity in iPSC-derived muscle cells from FH patients; lipophilic vs hydrophilic statins |
| [24849689](https://pubmed.ncbi.nlm.nih.gov/24849689/) | 2014 | Review | Consult Pharm | Statin-associated incident diabetes |
| [20531065](https://pubmed.ncbi.nlm.nih.gov/20531065/) | 2010 | Case report | South Med J | Rosuvastatin-induced severe thrombocytopenia |
| [36928267](https://pubmed.ncbi.nlm.nih.gov/36928267/) | 2023 | Cohort | J Atheroscler Thromb | LDL-C goal achievement in high-risk patients in Japan |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia management |

### Other predicted indications (summary)

- **HIV infectious disease:** 2024 report [39088828](https://pubmed.ncbi.nlm.nih.gov/39088828/) found rosuvastatin did not reduce arterial stiffness and may be associated with cardiometabolic adverse events in men with HIV; [26157049](https://pubmed.ncbi.nlm.nih.gov/26157049/) found it worsened insulin resistance; [25514794](https://pubmed.ncbi.nlm.nih.gov/25514794/) reported reduced vascular inflammation and T-cell/monocyte activation. Several reviews cover statins in HIV.
- **Hyperlipidemia:** large body of evidence, including the STELLAR RCT [12860216](https://pubmed.ncbi.nlm.nih.gov/12860216/) and a Cochrane review [25415541](https://pubmed.ncbi.nlm.nih.gov/25415541/).
- **Brain stem infarction:** only indirect evidence, including a rat stroke study of exosomes plus rosuvastatin ([31974756](https://pubmed.ncbi.nlm.nih.gov/31974756/)).
- **CYP7A1-deficiency hypercholesterolemia:** one indirect mechanistic study ([15583480](https://pubmed.ncbi.nlm.nih.gov/15583480/)).
- **Hypoalphalipoproteinemia:** a review, a commentary, and a genetic case report only.
- **CETP deficiency, hepatic lipase deficiency, ABri amyloidosis, neurodevelopmental disorder:** currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206465 | Rosuvastatin (Quallent Pharmaceuticals Health LLC) | Tablet, film coated | Valid |
| ANDA079172 | Rosuvastatin calcium (RemedyRepack Inc.) | Tablet, film coated | Valid |
| ANDA212059 | Rosuvastatin Calcium (Zhejiang Yongtai Pharmaceutical Co., Ltd.) | Tablet, film coated | Valid |
| ANDA206381 | Rosuvastatin (RemedyRepack Inc.) | Tablet, film coated | Valid |
| ANDA207062 | Rosuvastatin Calcium (Westminster Pharmaceuticals, LLC) | Tablet, film coated | Valid |

Indication text is not available in these records. Dosage forms are oral tablets (film coated and uncoated).

---

## Safety Considerations

- **Contraindications (knowledge-graph derived, not label text):** liver disease, gallbladder disease, hypothyroidism, myxedema, congenital hypothyroidism, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, injury, proteinuria.
- **Drug Interactions:** 100 interactions were recorded. Notable examples:
  - **Major:** fenofibrate, atazanavir
  - **Moderate:** amiodarone, atorvastatin, ezetimibe, bempedoic acid, paclitaxel, alpelisib, apalutamide, zidovudine, adalimumab, ethanol, among others
  - **Minor:** levonorgestrel, norethisterone, desogestrel
- **Literature-reported safety signals:** new-onset diabetes risk, insulin resistance in HIV-infected adults, rare severe thrombocytopenia, and statin-associated muscle symptoms.

Please refer to the package insert for full warnings, as label text was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision:**
- **Familial hypercholesterolemia: Proceed with Guardrails**
- **CETP deficiency (top-ranked), CYP7A1 deficiency, brain stem infarction, hypoalphalipoproteinemia, hepatic lipase deficiency, ABri amyloidosis, neurodevelopmental disorder: Hold**
- **HIV infectious disease:** Research Question (cardiovascular risk and dyslipidemia management, not infection treatment)

**Rationale:**
- Familial hypercholesterolemia is supported by multiple completed Phase 3 trials (including paediatric studies) and RCT literature, giving an L1 evidence level. However, it overlaps with existing labeled indications, so it is closer to on-label use than true repurposing.
- The highest TxGNN-ranked prediction (CETP deficiency) has no clinical trials or literature (L5), so it cannot be advanced on the current evidence. A high model score alone is not sufficient.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking data gap)
- Mechanism of action data from DrugBank
- Guardrails for FH use: paediatric dosing with growth and maturation monitoring, CK and liver enzyme monitoring, renal dose adjustment, new-onset diabetes surveillance, and a management plan for the 100 recorded drug interactions (especially fenofibrate and atazanavir)
- For HIV-related use: protease-inhibitor interaction assessment and review of mixed findings on cardiometabolic effects
- For CETP deficiency: mechanistic and preclinical or case-based evidence before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

