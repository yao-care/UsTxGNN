---
layout: default
title: Serotonin
parent: 僅模型預測 (L5)
nav_order: 1156
evidence_level: L5
indication_count: 10
---

# Serotonin
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

Using no additional skill — this is a structured content-generation task; proceeding directly per the provided template and evidence pack.

---

# Serotonin: From Endogenous Neurotransmitter to Insomnia

## One-Sentence Summary

> Serotonin (5-hydroxytryptamine) is an endogenous neurotransmitter with no approved drug indication of its own — it is not currently marketed in the jurisdiction covered by this evidence pack. TxGNN predicts a strong association with **Insomnia** (score 99.90%), but the **50 clinical trials** and **18 publications** identified all study downstream serotonergic drugs (trazodone, mirtazapine, SSRIs, pimavanserin) or non-pharmacological interventions — none administer serotonin itself, and the underlying pharmacology raises serious feasibility concerns for direct use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record — serotonin has no approved therapeutic indication (endogenous neurotransmitter; 0 licenses in dataset) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (mechanistic/preclinical; no interventional trial of serotonin itself) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for serotonin as a drug product is not available in DrugBank for this candidate. Based on known pharmacology, serotonin (5-HT) is an endogenous monoamine synthesized from tryptophan that signals through the 5-HT1–7 receptor family distributed across the central and peripheral nervous system, gut, and vasculature. It has never been developed as a standalone therapeutic — a fact consistent with its extremely short plasma half-life (~2 minutes), inability to cross the blood-brain barrier, and pronounced peripheral vasoactive and gastrointestinal effects when given exogenously.

The mechanistic link to insomnia is real: 5-HT1A/2A/2C receptor signaling helps regulate the sleep-wake cycle, and this is well documented in the literature. However, every one of the 50 clinical trials returned for this indication investigates a **downstream serotonergic drug** — trazodone, mirtazapine, pimavanserin, SSRIs/SNRIs — or a non-pharmacological intervention (acupuncture, probiotics, magnetotherapy). None administer serotonin itself. This is not a coincidence: drugs like SSRIs and trazodone were specifically developed as *indirect* modulators of the serotonin system precisely because direct serotonin administration is not clinically viable (poor CNS penetration, systemic side effects, risk of serotonin syndrome). TxGNN's high score therefore reflects strong network-level association between "serotonin" and "insomnia" concepts, not evidence that serotonin itself is an actionable drug candidate for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04532749](https://clinicaltrials.gov/study/NCT04532749) | Phase 3 | Terminated | 212 | Seltorexant (orexin antagonist) as adjunctive therapy to antidepressants in MDD with insomnia symptoms (MDDIS) inadequately responsive to SSRI/SNRI — not a serotonin agent |
| [NCT06559306](https://clinicaltrials.gov/study/NCT06559306) | Phase 3 | Recruiting | 752 | Ongoing follow-up Seltorexant trial in MDDIS patients; evaluates efficacy/safety and maintenance of effect vs placebo |
| [NCT06056258](https://clinicaltrials.gov/study/NCT06056258) | NA | Completed | 48 | Placebo-controlled trial of nutraceutical VL-NL-02 for sleep quality, restorative sleep, and mood |
| [NCT00765752](https://clinicaltrials.gov/study/NCT00765752) | N/A | Completed | 23 | MRS study of cortical GABA levels in primary insomnia and in MDD patients with SSRI-residual insomnia — mechanistic, not interventional |
| [NCT07229976](https://clinicaltrials.gov/study/NCT07229976) | NA | Not yet recruiting | 198 | Thumbtack-needle acupuncture for chronic insomnia in perimenopausal/menopausal women |
| [NCT05705830](https://clinicaltrials.gov/study/NCT05705830) | NA | Unknown | 400 | Pulse magnetotherapy combined with medication for anxiety and insomnia |
| [NCT03947216](https://clinicaltrials.gov/study/NCT03947216) | Phase 2 | Completed | 117 | Pimavanserin (5-HT2A inverse agonist) for impulse control disorders in Parkinson's disease — graded C relevance, not insomnia-specific |
| [NCT00025740](https://clinicaltrials.gov/study/NCT00025740) | Phase 4 | Completed | 78 | Clonazepam + paroxetine (SSRI) combination for rapid PTSD treatment — graded C, indirect serotonin-pathway support only |
| [NCT03321526](https://clinicaltrials.gov/study/NCT03321526) | Phase 2 | Completed | 107 | JNJ-42847922 vs quetiapine XR as adjunctive therapy in MDD inadequately responsive to SSRI — graded C |
| [NCT03977441](https://clinicaltrials.gov/study/NCT03977441) | Phase 4 | Unknown | 240 | Agomelatine for sleep disorders and depression in Parkinson's disease; notes SSRI/clonazepam adverse effects including serotonin syndrome |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40135470](https://pubmed.ncbi.nlm.nih.gov/40135470/) | 2025 | RCT | Age and Ageing | MIRAGE study: mirtazapine (blocks serotonin/histamine receptors) for chronic insomnia in older adults |
| [34994734](https://pubmed.ncbi.nlm.nih.gov/34994734/) | 2021 | Review | Psychiatria Polska | Compares trazodone vs hypnotics for insomnia; summarizes evidence for serotonergic sedative antidepressants |
| [24685396](https://pubmed.ncbi.nlm.nih.gov/24685396/) | 2014 | Review | Sleep Medicine Reviews | Insomnia pathophysiology framework (predisposing, precipitating, perpetuating factors) |
| [26744739](https://pubmed.ncbi.nlm.nih.gov/26744739/) | 2015 | Review | Drugs of Today | Pharmacology review of pimavanserin (5-HT2A inverse agonist) |
| [41123484](https://pubmed.ncbi.nlm.nih.gov/41123484/) | 2025 | Review | Annals of Medicine | Circadian clock gene dysregulation as a core mechanism in insomnia |
| [21537726](https://pubmed.ncbi.nlm.nih.gov/21537726/) | 2011 | Review | Rev Bras Psiquiatr | Serotonergic transmission linking sleep and depression via sedative antidepressants |
| [37834999](https://pubmed.ncbi.nlm.nih.gov/37834999/) | 2023 | Observational | J Clin Med | Serum 5-HT and SERT expression correlate with depressive/insomnia symptoms in inflammatory bowel disease |
| [41392764](https://pubmed.ncbi.nlm.nih.gov/41392764/) | 2026 | Preclinical | Food & Function | Probiotic strain ameliorates insomnia in a mouse model by restoring GABA and serotonin signaling |
| [39519543](https://pubmed.ncbi.nlm.nih.gov/39519543/) | 2024 | Preclinical | Nutrients | Lactobacillus plantarum reduces stress-induced insomnia/depression-like behavior in mice |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Observational | Medicine | Moxibustion + ear acupuncture + alprazolam improves neurotransmitter levels in coronary heart disease patients with insomnia |

---

## US Market Information

No marketing authorizations were found. Serotonin is not currently registered as an approved drug product in the reviewed dataset (0 licenses; market status: Not Marketed / 未上市). Serotonin is used clinically only as an endogenous biomarker/reference compound, not as a formulated therapeutic.

---

## Safety Considerations

Please refer to the package insert for safety information. No formal drug-safety data (warnings, contraindications, or DDI records) is currently available for this candidate.

**Important caveat surfaced in mechanistic review:** exogenous serotonin has an extremely short plasma half-life, does not cross the blood-brain barrier, and is associated with peripheral vasoactive and gastrointestinal effects — properties that historically made direct serotonin administration clinically impractical and drove development of indirect serotonergic agents (SSRIs, trazodone, triptans) instead.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between serotonin signaling and insomnia is well established, but no clinical evidence tests serotonin itself as a therapeutic agent — all identified trials and most literature concern downstream serotonergic drugs. Combined with the missing TFDA label data (blocking safety gap) and missing MOA confirmation, this candidate cannot yet proceed to a safety-guardrail decision.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap — required before any S1 safety evaluation)
- Confirmed mechanism-of-action data via DrugBank API query
- Clarification of drug identity/strategy: whether "serotonin" here represents a literal exogenous-serotonin candidate, or should instead be reinterpreted as a class-level signal pointing to serotonergic precursors (e.g., 5-HTP) or receptor-selective agents
- Pharmacokinetic/route-of-administration feasibility assessment given known BBB-penetration and half-life limitations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

