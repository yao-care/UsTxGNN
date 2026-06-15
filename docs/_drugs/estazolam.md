---
layout: default
title: Estazolam
parent: 僅模型預測 (L5)
nav_order: 532
evidence_level: L5
indication_count: 10
---

# Estazolam
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

# Estazolam: From Unregistered Hypnotic to Insomnia Treatment

## One-Sentence Summary

Estazolam is a triazolobenzodiazepine hypnotic agent recognized globally for its sedative-hypnotic properties, but it currently has no active registrations in the queried US regulatory database.
The TxGNN model predicts it may be effective for **Insomnia**, with **12 clinical trials** and **18 publications** currently supporting this direction.
With a prediction score of 99.48% and L1 evidence, this is not a novel repurposing discovery but a direct pharmacological confirmation — the primary clinical question is regulatory pathway, not mechanistic feasibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No active license found in database (globally recognized for short-term insomnia) |
| Predicted New Indication | Insomnia (Disease) |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed (0 active licenses in database) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

While formal DrugBank mechanism of action data was not retrieved in this evidence pack cycle, Estazolam's pharmacology is extensively documented in the clinical literature. As a triazolobenzodiazepine, Estazolam acts as a positive allosteric modulator of GABA-A receptors — it increases the frequency of chloride ion channel opening in response to GABA binding, thereby enhancing inhibitory neurotransmission throughout the central nervous system. This produces dose-dependent sedation, sleep induction, reduction in nocturnal awakenings, and improvements in subjective sleep quality. These effects map directly and mechanistically onto the core pathophysiology of insomnia: a state of hyperarousal and failure to initiate or maintain sleep.

The 1990 US clinical experience review (PMID 1968721) establishes that Estazolam 1.0 mg and 2.0 mg significantly improve sleep latency, total sleep time, number of nocturnal awakenings, depth of sleep, and overall sleep quality in adults with chronic insomnia across well-controlled sleep laboratory and outpatient trials. Six-week continuous nightly administration data showed no evidence of clinically meaningful tolerance. This places Estazolam firmly within the same efficacy tier as other approved benzodiazepine hypnotics such as triazolam and temazepam. The TxGNN knowledge graph prediction at 99.48% reflects this tight mechanistic coupling, as GABA-A potentiation is the canonical pathway for pharmacological insomnia management.

The 0 active licenses returned by the regulatory database query likely reflects the discontinuation of the branded product ProSom® rather than a genuine absence of approval history or current generic availability. The key guardrails for proceeding arise not from inadequate evidence but from the class-specific risks of benzodiazepines: physical and psychological dependence with prolonged use, rebound insomnia upon abrupt discontinuation, cognitive impairment particularly in elderly patients, and the drug's Schedule IV controlled substance status requiring prescriber and dispensing oversight.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Phase 3 | Completed | 253 | Double-blind double-dummy multicenter RCT comparing Brotizolam vs Estazolam for insomnia outpatients; the strongest head-to-head controlled evidence directly evaluating Estazolam's efficacy and safety |
| [NCT00956319](https://clinicaltrials.gov/study/NCT00956319) | Phase 4 | Completed | 42 | Randomized open-label active-controlled parallel study evaluating Zolpidem MR against Estazolam (Eurodin) for primary insomnia; post-marketing confirmatory evidence with Estazolam as reference standard |
| [NCT06859190](https://clinicaltrials.gov/study/NCT06859190) | Phase 3 | Recruiting | 60 | Assesses short- and long-term efficacy of auricular acupuncture combined with Estazolam for cancer-induced insomnia; Estazolam is a direct primary intervention, not merely a comparator |
| [NCT03997058](https://clinicaltrials.gov/study/NCT03997058) | Phase 4 | Unknown | 120 | Compares auricular acupoint pressing vs oral Estazolam for insomnia in maintenance hemodialysis patients; evaluates whether TCM can reduce Estazolam dependence in a high-risk population |
| [NCT07306494](https://clinicaltrials.gov/study/NCT07306494) | Phase 4 | Not Yet Recruiting | 1,200 | Large multicenter double-blind double-dummy RCT: Compound Ciwujia Granules vs Estazolam vs combination for chronic insomnia; Estazolam serves as the active pharmacological reference standard |
| [NCT06258226](https://clinicaltrials.gov/study/NCT06258226) | Phase N/A | Unknown | 108 | RCT examining auricular acupressure to reduce Estazolam dose in drug-dependent insomnia patients; directly confirms Estazolam's widespread clinical use and the real-world problem of dependency |
| [NCT04932395](https://clinicaltrials.gov/study/NCT04932395) | Phase 4 | Unknown | 400 | Adaptive enrichment multicenter double-blind placebo-controlled RCT of Anshen Buxin Liuwei Pill for cardiac neurosis with insomnia; Estazolam likely serves as active comparator arm |
| [NCT06212934](https://clinicaltrials.gov/study/NCT06212934) | Phase N/A | Unknown | 96 | Non-inferiority design comparing "Chou's Tiaoshen" acupuncture vs Estazolam for short-term insomnia; further establishes Estazolam as the clinical benchmark in China-based sleep trials |
| [NCT03420105](https://clinicaltrials.gov/study/NCT03420105) | Phase N/A | Completed | 75 | Prospective memory and sleep study in breast cancer patients; Estazolam present as background medication, offering real-world observational data in an oncology-insomnia comorbidity context |
| [NCT04980703](https://clinicaltrials.gov/study/NCT04980703) | Phase N/A | Not Yet Recruiting | 102 | Grain moxibustion for insomnia with possible Estazolam comparator arm; evaluates non-pharmacological alternatives with intent to displace benzodiazepine use |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1968721](https://pubmed.ncbi.nlm.nih.gov/1968721/) | 1990 | Clinical Review | American Journal of Medicine | Definitive US clinical experience summary: Estazolam 1–2 mg significantly improves all sleep parameters in chronic insomnia across sleep laboratory and outpatient RCTs; 6-week data shows no tolerance development |
| [36571227](https://pubmed.ncbi.nlm.nih.gov/36571227/) | 2022 | RCT | Acupuncture Research | Shallow-needle therapy combined with Estazolam outperforms Estazolam monotherapy for liver stagnation-pattern insomnia; also assesses ACTH and cortisol as biomarkers of combined treatment mechanism |
| [37697875](https://pubmed.ncbi.nlm.nih.gov/37697875/) | 2023 | RCT | Chinese Acupuncture & Moxibustion | Syndrome-differentiation acupuncture vs Estazolam for chronic insomnia; specific cognitive function outcomes measured, highlighting benzodiazepine-associated cognitive risk as clinically relevant endpoint |
| [40381125](https://pubmed.ncbi.nlm.nih.gov/40381125/) | 2025 | RCT | Neuromolecular Medicine | Electro-acupuncture alleviates post-stroke insomnia via Sirt1/Nrf2-ARE pathway modulation; Estazolam used as active comparator, demonstrating its utility in neurological comorbidity insomnia contexts |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Medical Letter on Drugs & Therapeutics | Comprehensive pharmacotherapy review for chronic insomnia; positions benzodiazepines including Estazolam within the full therapeutic landscape alongside newer agents |
| [31013432](https://pubmed.ncbi.nlm.nih.gov/31013432/) | 2019 | Systematic Review | Journal of Alternative & Complementary Medicine | Updated systematic review of 11-database acupuncture RCTs for primary insomnia (2008–2017); Estazolam consistently used as active control in Asian trials, confirming its role as clinical reference standard |
| [40896345](https://pubmed.ncbi.nlm.nih.gov/40896345/) | 2025 | Scoping Review | Integrative Medicine Research | Explores transdiagnostic treatment of insomnia comorbid with chronic pain using CHM and acupuncture; Estazolam cited as standard pharmacotherapy comparator in over 20% of adults with comorbid insomnia |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Observational | China Journal of Chinese Materia Medica | Real-world analysis of 1,067 insomnia cases across 20 hospitals; documents Estazolam's prevalent use alongside key comorbidities (hypertension 26.9%, cerebrovascular disease 24.9%), informing safety monitoring priorities |
| [33798303](https://pubmed.ncbi.nlm.nih.gov/33798303/) | 2021 | Case Series | Chinese Acupuncture & Moxibustion | Compares Baduanjin exercise + auricular acupuncture vs oral Estazolam for COVID-19-associated insomnia; Estazolam serves as standard-of-care reference in an emerging comorbidity setting |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | ISI-based survey of insomnia among COVID-19 survivors (Dec 2022–Feb 2023); documents Estazolam use prevalence and identifies risk factors for post-COVID insomnia persistence |

---

## US Market Information

No active licenses were found in the queried US regulatory database for Estazolam (0 records returned). This likely reflects the market withdrawal of the branded product ProSom® (Abbott) rather than a complete absence of regulatory history. Generic estazolam tablets (1 mg, 2 mg) remain available by Schedule IV prescription in the US. A direct query to the FDA Orange Book and the DEA controlled substance registry is recommended to confirm current approval and scheduling status before any regulatory filing.

---

## Safety Considerations

Formal warning and contraindication data were not retrieved in this evidence pack. Based on the available mechanistic rationale and class-level pharmacology, the following considerations are clinically significant:

- **Dependence and Withdrawal Risk**: Prolonged benzodiazepine use produces physical and psychological dependence; abrupt discontinuation may trigger withdrawal seizures, severe rebound insomnia, and anxiety. Treatment duration should be limited (typically 7–10 days; reassess if extended).
- **Cognitive Function in Elderly Patients**: Multiple active comparator trials (PMID 37697875) specifically selected cognitive function as a primary endpoint, reflecting established concern about benzodiazepine-associated memory impairment, daytime sedation, and fall risk in patients aged ≥65.
- **Controlled Substance Requirements**: Estazolam is a DEA Schedule IV substance. Prescribing, dispensing, and inventory management must comply with controlled substance regulations including prescription monitoring program (PMP) enrollment where required.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Estazolam achieved the highest TxGNN prediction score in this evidence pack (99.48%) for insomnia, supported by L1-level evidence — including two completed randomized controlled trials (NCT00347295 Phase 3, NCT00956319 Phase 4) and a well-referenced 1990 US clinical experience review confirming efficacy across all standard sleep parameters. The prediction is a mechanistic confirmation of established pharmacology, not a speculative repurposing hypothesis. Guardrails are warranted due to class-specific risks (dependence, cognitive impact, controlled substance status) and the need to clarify current regulatory standing.

**To proceed, the following is needed:**
- Confirm current US regulatory status via the FDA Orange Book (generic estazolam) and DEA Schedule IV registry to resolve the 0-license gap in the queried database
- Obtain and parse the full package insert (DG001 remediation) to extract complete contraindications, boxed warnings, and drug interaction profile — particularly CYP3A4 inhibitor interactions common to benzodiazepines
- Define and document maximum treatment duration criteria and criteria for reassessment or discontinuation, consistent with AASM or equivalent sleep medicine guidelines
- Specify contraindicated populations (pregnancy, myasthenia gravis, severe respiratory insufficiency, sleep apnea, severe hepatic impairment) once package insert is retrieved
- Establish an elderly patient monitoring protocol covering cognitive screening (e.g., MMSE), fall risk assessment, and dose adjustment for patients ≥65 years
- Confirm Schedule IV controlled substance compliance procedures including PMP enrollment, prescription limits, and institutional dispensing audit requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

