---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From Analgesic Adjuvant to Hypnic Headache

## One-Sentence Summary

Caffeine is a methylxanthine alkaloid with established clinical uses as a CNS stimulant and analgesic adjuvant — currently carrying no approved indications in the regulatory database (0 licenses) despite widespread international pharmaceutical use including FDA-approved caffeine citrate for neonatal apnea of prematurity.
The TxGNN model identifies 10 predicted new indications; while **nasal cavity disease** ranks first by prediction score (99.91%), the evidence pack shows this reflects nasal drug-delivery formulation research rather than a true therapeutic signal — **hypnic headache** (99.17%, rank 9) emerges as the most clinically validated target, with case series spanning 30+ years and international headache guidelines consistently recommending caffeine as first-line off-label therapy.
Across all 10 predictions, only hypnic headache reaches **Evidence Level L3** with a **"Proceed with Guardrails"** decision; all others remain at Hold or Research Question.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved products in regulatory database; internationally: neonatal apnea of prematurity, analgesic adjuvant |
| Primary Featured Indication | Hypnic Headache (highest clinical evidence level among all 10 predictions) |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L3 |
| Market Status | Not marketed (0 licenses in database) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (MOA: Data Gap). Based on established pharmacology, caffeine acts as a **non-selective adenosine receptor antagonist** (primary targets: A1 and A2A subtypes) and a **phosphodiesterase (PDE) inhibitor** at higher concentrations, producing CNS stimulation, cerebral vasoconstriction, enhanced catecholamine release, and modulation of pain signaling pathways.

Hypnic headache disorder is a rare primary headache that exclusively awakens patients from sleep, predominantly affecting individuals over 50 years of age. Its pathophysiology centers on **adenosine accumulation during sleep** — particularly during REM phases — which activates pain-sensitive intracranial structures via A1/A2A receptors. Caffeine's pre-sleep adenosine receptor blockade directly interrupts this REM-linked triggering mechanism. This mechanistic alignment is tight, specific, and supported by observable clinical phenomena: patients consistently report relief when caffeine is consumed before sleep or immediately upon waking with headache, and the effect reverses upon caffeine withdrawal.

This mechanistic rationale is substantially stronger than for caffeine's higher-ranked TxGNN predictions. Nasal cavity disease (rank 1) is supported only by a formulation study using caffeine as a drug-delivery vehicle for brain targeting — not as a therapeutic agent for nasal pathology itself. Hypnic headache, by contrast, has accumulated real-world clinical evidence across hundreds of reported cases in the headache literature, and caffeine is specifically named before lithium carbonate as the preferred first choice in expert consensus — an exceptional status for an off-label indication.

---

## Clinical Trial Evidence

Currently no clinical trials related to caffeine and hypnic headache are registered on ClinicalTrials.gov.

> The absence of registered trials reflects the rare-disease nature of hypnic headache (estimated prevalence <1% of all primary headache disorders) and the long-established informal clinical use of caffeine in this setting, rather than lack of efficacy evidence. Existing support derives from case series and expert consensus compiled over three decades.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22072057](https://pubmed.ncbi.nlm.nih.gov/22072057/) | 2012 | Treatment Review | Current Treatment Options in Neurology | Explicitly designates caffeine as the **preferred first-line therapy** for both acute treatment (strong coffee upon waking) and prophylaxis (40–200 mg tablet before sleep); notes superior tolerability over lithium in the predominantly elderly population |
| [31075680](https://pubmed.ncbi.nlm.nih.gov/31075680/) | 2019 | Case Series Review | Journal of the Neurological Sciences | Systematic review of **348 published hypnic headache cases (1988–2018)**; caffeine among the most frequently cited effective interventions across all case series |
| [24942086](https://pubmed.ncbi.nlm.nih.gov/24942086/) | 2014 | Narrative Review | Cephalalgia | Reviews clinical features, ICHD-3β diagnostic criteria, and treatment outcomes; confirms caffeine 40–300 mg bedtime as effective prophylaxis with the most favorable tolerability profile |
| [25231430](https://pubmed.ncbi.nlm.nih.gov/25231430/) | 2014 | Case Series / Review | Headache | Characterizes HH clinical profile and treatment hierarchy; recommends caffeine as first-line alongside lithium carbonate for prophylaxis |
| [23832130](https://pubmed.ncbi.nlm.nih.gov/23832130/) | 2013 | Case Series / Review | Cephalalgia | Confirms caffeine's role in HH management; notes better tolerability than lithium in elderly patients and highlights the paradox of bedtime caffeine improving rather than disrupting sleep in HH |
| [15111685](https://pubmed.ncbi.nlm.nih.gov/15111685/) | 2004 | Observational (PSG) | Neurology | Polysomnographic monitoring confirms HH attacks arise from both REM and non-REM sleep in the same patients — directly supports adenosine accumulation hypothesis underpinning caffeine's mechanism |
| [33974014](https://pubmed.ncbi.nlm.nih.gov/33974014/) | 2021 | Narrative Review | JAMA | Comprehensive headache management review; contextualizes caffeine's established role across the sleep-related headache spectrum |
| [35574653](https://pubmed.ncbi.nlm.nih.gov/35574653/) | 2023 | Narrative Review | Critical Reviews in Food Science and Nutrition | Reviews caffeine's health benefits and risks including sleep, migraine, and headache interactions; provides updated pharmacological context |

---

## Regulatory & Market Information

No approved pharmaceutical products for caffeine were found in the regulatory database query.

> **Context note:** Caffeine has established regulatory approvals internationally — including FDA-approved caffeine citrate (Cafcit®, NDA 020189) for apnea of prematurity in the United States, and caffeine is present in numerous approved combination analgesic formulations worldwide. The 0-license result reflects this database's specific scope and does not indicate a global absence of regulatory recognition.

---

## Safety Considerations

Please refer to the package insert for safety information. (No formal regulatory warning or contraindication data was available in this evidence pack.)

**Specific considerations for hypnic headache off-label use:**
- **Target population:** Predominantly >50 years; cardiovascular baseline assessment required before initiating
- **Cardiovascular monitoring:** Heart rate and blood pressure — caffeine may exacerbate existing hypertension or precipitate palpitations/arrhythmias
- **Dose range:** Clinical reports typically use 40–200 mg administered 30–60 minutes before sleep
- **Paradoxical effect:** Bedtime caffeine does not worsen sleep in HH patients at therapeutic doses — this is disease-specific and should be communicated to patients
- **Dependence and withdrawal:** Chronic use can produce caffeine dependence; abrupt discontinuation may itself trigger headache, requiring tapering guidance
- **Exclusion criteria:** Rule out secondary hypnic-like headache (space-occupying lesions, sleep apnea, medication-overuse headache) before attributing to primary HH

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for hypnic headache)*

**Rationale:**
Case series spanning over 30 years and headache specialty expert consensus consistently recommend caffeine as the first-choice treatment for hypnic headache, with a mechanistically coherent rationale — adenosine A1/A2A blockade interrupts the REM sleep-linked headache trigger — and a tolerability profile favorable for the elderly target population.

**To proceed, the following is needed:**
- Prospective pilot RCT: caffeine 100 mg vs. 200 mg vs. placebo, administered 30–60 minutes before sleep, minimum 12-week follow-up, primary endpoint: headache attack frequency per month
- Standardized patient selection using ICHD-3 diagnostic criteria for hypnic headache; mandatory neuroimaging to exclude secondary causes
- Cardiovascular safety monitoring protocol: baseline and monthly HR/BP, ECG for patients with arrhythmia history
- Caffeine serum level characterization in elderly patients (CYP1A2 activity varies significantly with age and co-medications)
- Regulatory consultation for formal off-label use documentation or orphan drug designation pathway (rare disease prevalence threshold may apply)

---

### All 10 TxGNN-Predicted Indications — Summary

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|:-----------:|:--------------:|:--------------:|
| 1 | Nasal Cavity Disease | 99.91% | L4 | Hold |
| 2 | Thrombotic Disease | 99.90% | L4 | Research Question |
| 3 | Acute Laryngopharyngitis | 99.89% | L5 | Hold |
| 4 | Papillary Conjunctivitis | 99.79% | L5 | Hold |
| 5 | Neuralgia | 99.34% | L3 | Research Question |
| 6 | Glossodynia | 99.26% | L5 | Hold |
| 7 | Coccygodynia | 99.22% | L5 | Hold |
| 8 | Trigeminal Autonomic Cephalalgia | 99.21% | L4 | Research Question |
| **9** | **Hypnic Headache** ★ | **99.17%** | **L3** | **Proceed with Guardrails** |
| 10 | Vein Disease | 99.06% | L4 | Research Question |

★ Primary featured indication — only entry reaching an actionable decision stage in this evidence pack

> **Why neuralgia (rank 5) is Research Question rather than Hold:** Animal studies in trigeminal pain models (PMID 25710675) and neuropathic pain models (PMID 11711033) show caffeine modulates spinal adenosine A1 receptor-mediated antinociception; caffetin (caffeine + analgesic combination) has historical clinical use in cervicalgia (PMID 9214190). However, the critical counter-evidence — a case report showing that a *low-caffeine diet* resolved trigeminal neuralgia (PMID 1815552) — indicates bidirectional effects and warrants caution before advancing. A focused mechanistic study is warranted before clinical development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

