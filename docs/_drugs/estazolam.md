---
layout: default
title: Estazolam
parent: Moderate Evidence (L3-L4)
nav_order: 673
evidence_level: L4
indication_count: 10
monitor_inn: "ESTAZOLAM"
predicted_indications: ["insomnia (disease)", "visual epilepsy", "alcohol withdrawal delirium", "restless legs syndrome", "myofascial pain syndrome", "thinking seizures", "micturation-induced seizures", "audiogenic seizures", "eating seizures", "orgasm-induced seizures"]
last_modified_at: 2026-10-14
description: "Estazolam: predicted new indication Insomnia (disease) (evidence level L4). Approved use: Not available in the US license records (indication text is blank). I…"
---

# Estazolam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Estazolam: From Insomnia (On-Label Use) to Insomnia (Disease)

## One-Sentence Summary

Estazolam is a triazolo-benzodiazepine sedative-hypnotic. The original indication field for this drug was not populated in the data compiled for this report.
The TxGNN model's top prediction is **insomnia**, which is in fact estazolam's established use, so this is not a true repurposing case.
The prediction is supported by **7 clinical trials** and **19 publications** retrieved for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the US license records (indication text is blank). Insomnia is the established use of the drug. |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L1 (as scored in the compiled data; see the note under Clinical Trial Evidence) |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 3 (all ANDAs, all cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Estazolam is a triazolo-benzodiazepine. It acts as a positive allosteric modulator of GABA-A receptors, enhancing inhibitory neurotransmission and producing sedative-hypnotic effects. This mechanism directly matches the pathophysiology targeted in insomnia. Detailed mechanism-of-action data was not populated in the source record, so this description comes from the mechanistic rationale compiled for the prediction.

Insomnia is the established, on-label use of estazolam, so the "new indication" here largely confirms the known use. The model's other predictions (visual epilepsy, alcohol withdrawal delirium, restless legs syndrome, myofascial pain syndrome, and several reflex seizure types) rest mainly on the general anticonvulsant and sedative effects of benzodiazepines. Their supporting evidence is preclinical or absent (see the table at the end of the report).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Phase 3 | Completed | 253 | Randomized, double-blind, double-dummy, multicenter comparison of brotizolam vs. estazolam in insomnia outpatients (efficacy and safety). Strongest direct evidence. |
| [NCT00956319](https://clinicaltrials.gov/study/NCT00956319) | Phase 4 | Completed | 42 | Zolpidem modified-release in primary insomnia, with estazolam (Eurodin) as the active comparator. |
| [NCT06859190](https://clinicaltrials.gov/study/NCT06859190) | Phase 3 | Recruiting | 60 | Auricular pressure beans plus electroacupuncture combined with estazolam for cancer-related insomnia. No results yet. |
| [NCT06258226](https://clinicaltrials.gov/study/NCT06258226) | NA | Unknown | 108 | Auricular acupressure to reduce estazolam use in drug-dependent insomnia. Informative about dependence and tapering, not efficacy. |
| [NCT03997058](https://clinicaltrials.gov/study/NCT03997058) | Phase 4 | Unknown | 120 | Auricular acupoint pressing vs. oral estazolam for insomnia in maintenance hemodialysis patients. |
| [NCT07306494](https://clinicaltrials.gov/study/NCT07306494) | Phase 4 | Not yet recruiting | 1200 | Compound Ciwujia Granules vs. estazolam (double-dummy) in chronic insomnia. No results. |
| [NCT05452577](https://clinicaltrials.gov/study/NCT05452577) | NA | Completed | 187 | Traditional Chinese medicine (Yin-Yang theory) for chronic insomnia. Estazolam is not evidently the focus. |

**Note on the evidence level:** Only one completed Phase 3 trial (NCT00347295) was found, and it is a comparator study. Strictly applying the level rules (L1 needs at least 2 completed Phase 3 RCTs), the trial evidence would sit closer to L2. The L1 label comes from the scoring in the compiled data and is reinforced by the long-established clinical use of estazolam.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42455420](https://pubmed.ncbi.nlm.nih.gov/42455420/) | 2026 | RCT | Chinese Journal of Integrative Medicine | Acupuncture combined with estazolam for insomnia in hemodialysis patients (single-center RCT). |
| [36571227](https://pubmed.ncbi.nlm.nih.gov/36571227/) | 2022 | RCT | Zhen Ci Yan Jiu | Shallow-needle therapy plus estazolam for insomnia (liver stagnation transforming into fire pattern). |
| [1968721](https://pubmed.ncbi.nlm.nih.gov/1968721/) | 1990 | Review | American Journal of Medicine | US clinical experience: estazolam 1 mg and 2 mg improved sleep latency, total sleep time, awakenings, and sleep quality in chronic insomnia. The 2 mg dose remained effective over at least 6 weeks of nightly use. |
| [31013432](https://pubmed.ncbi.nlm.nih.gov/31013432/) | 2019 | Systematic Review | J Altern Complement Med | Updated systematic review of RCTs on acupuncture for primary insomnia. |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Medical Letter on Drugs and Therapeutics | Overview of drugs for chronic insomnia. |
| [30625124](https://pubmed.ncbi.nlm.nih.gov/30625124/) | 2018 | Review | Medical Letter on Drugs and Therapeutics | Expanded table of oral hypnotics for chronic insomnia. |
| [42343684](https://pubmed.ncbi.nlm.nih.gov/42343684/) | 2026 | Clinical study | Zhen Ci Yan Jiu | Acupuncture combined with estazolam in chronic insomnia. |
| [37697875](https://pubmed.ncbi.nlm.nih.gov/37697875/) | 2023 | Clinical study | Zhongguo Zhen Jiu | Syndrome-differentiation acupuncture vs. estazolam in chronic insomnia, including cognitive function. |
| [33798303](https://pubmed.ncbi.nlm.nih.gov/33798303/) | 2021 | Clinical observation | Zhongguo Zhen Jiu | Baduanjin plus auricular point sticking vs. oral estazolam for COVID-19 patients with insomnia. |
| [40827342](https://pubmed.ncbi.nlm.nih.gov/40827342/) | 2025 | Cross-sectional | Psychiatry and Clinical Psychopharmacology | Drug use for insomnia in a Chinese medicine hospital in Shenzhen. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074818 (Actavis Pharma, Inc.) | Estazolam | Tablet | Not listed (cancelled) |
| ANDA074921 (Dr. Reddy's Laboratories Inc.) | Estazolam | Tablet | Not listed (cancelled) |
| ANDA074826 (Novitium Pharma LLC) | Estazolam | Tablet | Not listed (cancelled) |

All three authorizations are cancelled, so no estazolam product is currently active in the US market.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease contraindication links in the TxGNN knowledge graph, not package-insert text):
anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, liver disease, gallbladder disease, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome, myasthenia gravis, neuromuscular junction disease, substance-related disorder, and substance abuse/dependence.

**Drug Interactions:** The interaction query returned 100 records. Examples from the first 20:
- **Major:** morphine, morphine (liposomal). Additive central nervous system and respiratory depression is the main concern with opioids.
- **Moderate:** bupropion, aprepitant, omeprazole, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, opium, sibutramine, teduglutide.
- **Minor:** antacids and magnesium or calcium salts (magnesium oxide, aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide).

For warnings and label contraindications, please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insomnia is estazolam's established use, and a completed Phase 3 randomized trial plus a body of supportive literature back it. Because this is not a true repurposing opportunity, all licenses are cancelled in the US, and the label safety data is missing, development should proceed only with guardrails. The other nine predictions are rated Hold: the evidence is preclinical or absent, as summarized below.

| Predicted Indication | Evidence Level | Decision |
|------|------|------|
| Visual epilepsy | L4 | Hold |
| Alcohol withdrawal delirium | L5 | Hold |
| Restless legs syndrome | L5 | Hold |
| Myofascial pain syndrome | L5 | Hold |
| Thinking seizures | L5 | Hold |
| Micturition-induced seizures | L5 | Hold |
| Audiogenic seizures | L4 | Hold |
| Eating seizures | L5 | Hold |
| Orgasm-induced seizures | L5 | Hold |

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the original indication from the license records, and clarification of the regulatory status of the cancelled ANDAs
- Confirmation that estazolam is an arm (and not only the comparator) in the key trials, such as NCT00347295 and NCT00956319
- A risk plan for dependence, respiratory depression with opioids, and use in patients with sleep apnea, hepatic or renal disease, or a history of substance abuse
- Confirmation of the mechanism of action from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

