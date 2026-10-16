---
layout: default
title: Pitavastatin
parent: Model Prediction Only (L5)
nav_order: 1051
evidence_level: L5
indication_count: 10
monitor_inn: "PITAVASTATIN"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "familial hypercholesterolemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia, autosomal dominant", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "feline acquired immunodeficiency syndrome"]
---

# Pitavastatin
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

# Pitavastatin: From Familial Combined Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pitavastatin is a statin (HMG-CoA reductase inhibitor) originally used for familial combined hyperlipidemia.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, but the evidence is indirect: **no clinical trials** and only **2 loosely related publications** (an HIV dyslipidaemia RCT and a case report) currently support this top-ranked prediction.
Other predicted indications, especially hyperlipoproteinemia and cardiovascular prevention in HIV, have much stronger support and are summarised below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Familial combined hyperlipidemia (the US license records contain no indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 by the rules in this prompt (no trials, no direct studies); the compiled data assign L4 |
| US Market Status | Cancelled only (all 9 licenses cancelled) |
| Number of NDAs | 9 licenses (2 NDAs and 7 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pitavastatin inhibits HMG-CoA reductase, lowers hepatic cholesterol synthesis and upregulates hepatic LDL receptors, which lowers LDL-C.

Familial combined hyperlipidemia and HoFH are both inherited lipid disorders with elevated atherogenic lipoproteins, so a graph-based model links them. However, the mechanism is only partly applicable. Patients with HoFH have null or defective LDL receptors on both alleles, so little residual receptor activity remains for statins to upregulate. A partial response at best is expected, and the drug would most likely serve as an add-on rather than a primary therapy.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for homozygous familial hypercholesterolemia.

For context, the table below lists the most relevant trials for the closely related prediction **hyperlipoproteinemia** (rank 2), which is the best-supported indication in the data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01386853](https://clinicaltrials.gov/study/NCT01386853) | Phase 3 | Unknown | 200 | 12-week double-blind non-inferiority study, pitavastatin vs atorvastatin in high-risk hypercholesterolemia |
| [NCT01256476](https://clinicaltrials.gov/study/NCT01256476) | Phase 4 | Completed | 328 | Double-blind, pitavastatin 4 mg vs pravastatin 40 mg in primary hyperlipidemia or mixed dyslipidemia |
| [NCT01166633](https://clinicaltrials.gov/study/NCT01166633) | Phase 4 | Completed | 200 | Pitavastatin vs atorvastatin dose titration in hypercholesterolemia with mild to moderate hepatic damage |
| [NCT02056847](https://clinicaltrials.gov/study/NCT02056847) | Phase 4 | Completed | 313 | Pitavastatin 2 mg vs 4 mg and HbA1c in hyperlipidemia with impaired fasting glucose |
| [NCT00711919](https://clinicaltrials.gov/study/NCT00711919) | Not applicable | Unknown | 300 | Intensive vs conventional lipid lowering and carotid intima-media thickness |
| [NCT01695954](https://clinicaltrials.gov/study/NCT01695954) | Phase 1 | Completed | 34 | Pharmacokinetic interaction with efavirenz and darunavir/ritonavir |
| [NCT02634034](https://clinicaltrials.gov/study/NCT02634034) | Phase 1 | Completed | 18 | Pharmacokinetics of a controlled-release formulation in healthy volunteers |
| [NCT01764178](https://clinicaltrials.gov/study/NCT01764178) | Phase 1 | Completed | 52 | Pitavastatin plus valsartan co-administration vs fixed combination, pharmacokinetics |
| [NCT01406431](https://clinicaltrials.gov/study/NCT01406431) | Phase 1 | Completed | 48 | Pitavastatin plus valsartan co-administration vs fixed combination, pharmacokinetics |

---

## Literature Evidence

Publications retrieved directly for HoFH are limited to two, both indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Phase 4) | Lancet HIV | INTREPID: pitavastatin vs pravastatin in HIV-infected adults with dyslipidaemia (not HoFH) |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Case report | J Clin Lipidol | Rapid lipid-lowering response in two cases of autosomal recessive hypercholesterolemia, a condition clinically indistinguishable from HoFH |

Supporting literature from the related predictions (familial hypercholesterolemia and HIV):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37486775](https://pubmed.ncbi.nlm.nih.gov/37486775/) | 2023 | RCT (Phase 3) | N Engl J Med | REPRIEVE: pitavastatin to prevent cardiovascular disease in people with HIV |
| [38381407](https://pubmed.ncbi.nlm.nih.gov/38381407/) | 2024 | RCT substudy | JAMA Cardiol | Pitavastatin effects on coronary plaque and inflammatory biomarkers in HIV |
| [25891210](https://pubmed.ncbi.nlm.nih.gov/25891210/) | 2016 | Clinical trial | J Atheroscler Thromb | Efficacy and safety of pitavastatin in Japanese male children with heterozygous FH |
| [29187694](https://pubmed.ncbi.nlm.nih.gov/29187694/) | 2018 | Clinical trial | J Atheroscler Thromb | Pitavastatin in children and adolescents with FH in Japan and Europe |
| [17957184](https://pubmed.ncbi.nlm.nih.gov/17957184/) | 2008 | Randomized crossover | Clin Pharmacol Ther | Pitavastatin vs atorvastatin on coenzyme Q10 in 19 patients with heterozygous FH, with comparable LDL-C reductions |
| [12048134](https://pubmed.ncbi.nlm.nih.gov/12048134/) | 2002 | Long-term study | Atherosclerosis | 25 heterozygous FH patients, total cholesterol down about 31% over long-term treatment |
| [16733299](https://pubmed.ncbi.nlm.nih.gov/16733299/) | 2006 | Open-label | J Atheroscler Thromb | Low-dose pitavastatin vs atorvastatin in primary hyperlipidemia |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022363 | Livalo (Kowa Pharmaceuticals America) | Film-coated tablet | Not recorded; cancelled |
| NDA208379 | ZYPITAMAG (Medicure International) | Film-coated tablet | Not recorded; cancelled |
| ANDA205932 | Pitavastatin (AvKARE) | Film-coated tablet | Not recorded; cancelled |
| ANDA205977 | Pitavastatin calcium (Camber) | Film-coated tablet | Not recorded; cancelled |
| ANDA206015 | Pitavastatin (Aurobindo) | Film-coated tablet | Not recorded; cancelled |

Four more ANDAs (Zydus, Upsher-Smith, Mylan, Amneal) are also recorded as cancelled, for 9 licenses in total.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease, hypothyroidism, myxedema, congenital hypothyroidism, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, rhabdomyolysis, nodular fasciitis, impaired renal function, injury.
- **Drug Interactions**: 86 interactions are recorded. The main ones are:
  - **Major**: erythromycin.
  - **Moderate**: rosuvastatin and simvastatin (duplicate statin therapy), cobicistat, eltrombopag, metronidazole, tinidazole, secnidazole, benznidazole, disulfiram, ethanol, chloroquine, hydroxychloroquine, zafirlukast, chloramphenicol, dapsone, eluxadoline and naltrexone.
  - **Minor**: warfarin and dicoumarol.
  - The prediction rationale also flags CYP/OATP interactions with cyclosporine and gemfibrozil for review.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For the top-ranked prediction (HoFH) there are no clinical trials and only indirect literature. The expected statin response is limited because HoFH patients have little residual LDL receptor function. In addition, all US licenses are cancelled.

Other predictions fare better:
- **Hyperlipoproteinemia**: Phase 3 and Phase 4 randomized comparator trials exist, but this is essentially on-label use rather than true repurposing (Proceed with Guardrails).
- **Cardiovascular prevention in HIV**: supported by the large Phase 3 REPRIEVE trial, which reduced major adverse cardiovascular events. The indication is cardiovascular risk reduction, not treatment of the infection itself (Proceed with Guardrails).
- **Heterozygous or autosomal dominant FH**: supported by pediatric trials and case series (Proceed with Guardrails).
- **Predictions with no evidence**: CETP deficiency, CYP7A1 deficiency, the neurodevelopmental disorder, hepatic lipase deficiency and feline AIDS (Hold). The feline condition is a veterinary artifact outside the scope of human repurposing.

**To proceed, the following is needed:**
- Direct clinical data for pitavastatin in HoFH, ideally with genotype-stratified LDL receptor activity.
- Verification of US market availability and the reasons for license cancellation.
- Package insert warnings and contraindications (a blocking data gap).
- Detailed mechanism of action data.
- A review of the 86 drug interactions, especially with erythromycin, cyclosporine, gemfibrozil and antiretroviral regimens.
- For the HIV indication, a defined target population (low to moderate cardiovascular risk) and glucose monitoring.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

