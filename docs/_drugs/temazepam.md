---
layout: default
title: Temazepam
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 1
---

# Temazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Temazepam: From Benzodiazepine Hypnotic to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Temazepam is an intermediate-acting benzodiazepine hypnotic established internationally for the pharmacological management of insomnia, particularly sleep-maintenance insomnia; no formal indication record is present in the current system dataset, reflecting a data collection gap rather than a pharmacological unknown.
The TxGNN model predicts it may be effective for **Sleep Disorder, Initiating and Maintaining Sleep**, with a prediction confidence of 99.82%, supported by **0 registered clinical trials** but **20 publications** — including Phase III RCTs and major clinical practice guidelines — currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in system data (known internationally as insomnia / sleep-maintenance hypnotic) |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Temazepam is a benzodiazepine that acts at the GABA-A receptor benzodiazepine (BZ) binding site, potentiating GABAergic inhibitory neurotransmission in the central nervous system. Its hypnotic pharmacological effects include reduction of sleep-onset latency, decrease in nocturnal awakenings, and increase in total sleep time (TST), primarily through enhancement of NREM Stage 2 sleep. The [Data Gap] recorded in the original MOA field is a system-level data collection gap, not a genuine pharmacological unknown — the drug's mechanism is well-characterized in the literature spanning four decades.

With an elimination half-life of approximately 8–20 hours, temazepam occupies a clinically advantageous intermediate position: it avoids the severe rebound insomnia risk associated with short-acting triazolam, while producing less residual daytime sedation than long-acting flurazepam. This kinetic profile makes it a benchmark agent specifically suited to sleep-maintenance insomnia — the exact target captured in the predicted indication "initiating and maintaining sleep."

The TxGNN prediction is therefore mechanistically redundant rather than novel: it validates the drug's established use profile at 99.82% confidence. The value of this prediction lies in its confirmation that TxGNN's knowledge graph correctly captures the temazepam–sleep disorder association, and that the evidence base (including a 2024 Phase III multicenter RCT specifically testing temazepam for cancer-related insomnia) is sufficiently robust to warrant a structured deployment pathway where Taiwan regulatory status is resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for temazepam in this indication.

> The L1 evidence level is derived from published Phase III RCTs in the peer-reviewed literature (see Literature Evidence below), not from prospectively registered trial registries.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39304187](https://pubmed.ncbi.nlm.nih.gov/39304187/) | 2024 | RCT (Phase III, Three-arm, Double-blind) | Journal of Palliative Medicine | Temazepam vs melatonin prolonged-release vs placebo for insomnia in advanced cancer patients; multicenter design directly evaluating temazepam's hypnotic efficacy |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Internal Medicine | Masked dose-taper with cognitive behavioral therapy for insomnia (CBTI) to discontinue BZ receptor agonist hypnotics in older adults; validates the dependence-risk profile of temazepam class |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical Practice Guideline (Evidence-based) | Journal of Clinical Sleep Medicine | AASM pharmacologic treatment guideline for chronic insomnia in adults; individual drug-level recommendations including temazepam |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Systematic Review & Network Meta-analysis | Sleep | Comparative efficacy and safety of hypnotics in older adults; provides head-to-head evidence positioning temazepam relative to newer agents |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Systematic Review | Drugs & Aging | Pharmacological management of chronic insomnia in elderly; quality-of-life burden and pharmacotherapy recommendations |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Systematic Review | Clinical Therapeutics | Safety and efficacy of sleep medicines in older adults; highlights pharmacokinetic alterations relevant to temazepam dosing |
| [2859305](https://pubmed.ncbi.nlm.nih.gov/2859305/) | 1985 | RCT (Double-blind, Multicenter) | Journal of Clinical Psychopharmacology | Midazolam 15 mg vs temazepam 30 mg vs placebo administered mid-night for sleep-maintenance insomnia; primary hypnotic efficacy and next-day residual effects |
| [10533351](https://pubmed.ncbi.nlm.nih.gov/10533351/) | 1999 | Review | Journal of the American Pharmaceutical Association | Pharmacologic and nonpharmacologic management of insomnia; covers patient selection and drug class comparisons |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Insomnia in the elderly: prevalence up to 40%, risk factors, and treatment evidence overview |
| [28992822](https://pubmed.ncbi.nlm.nih.gov/28992822/) | 2017 | Review | The Consultant Pharmacist | Updated treatment options for insomnia in older adults; pharmacokinetic considerations and prescribing guidance |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (key warnings, contraindications, DDI) was not available in this evidence pack. Based on the established pharmacological class, the following considerations are expected to apply and should be verified against the full prescribing information:
>
> - **Dependence and tolerance**: Benzodiazepine class carries Schedule IV controlled substance classification in many jurisdictions; risk of psychological and physical dependence with prolonged use.
> - **Rebound insomnia**: Upon abrupt discontinuation, transient worsening of sleep beyond baseline may occur (particularly relevant given the 2024 RCT on managed tapering, PMID 39374004).
> - **CNS depression**: Additive effects expected with alcohol, opioids, and other CNS depressants.
> - **Special populations**: Elderly patients are at heightened risk for falls, cognitive impairment, and prolonged sedation due to altered clearance; dose reduction and increased monitoring are typically warranted.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Temazepam's mechanism of action directly and specifically targets the neurobiological substrate of sleep-wake dysregulation, making the TxGNN prediction a mechanistic confirmation rather than a novel repurposing signal; the evidence base — anchored by a 2024 Phase III multicenter RCT and major clinical practice guidelines — is L1-grade, supporting a structured pathway forward once regulatory and safety documentation gaps are resolved.

**To proceed, the following is needed:**

- **Taiwan regulatory pathway**: Temazepam is not currently marketed in Taiwan (0 licenses); clarify controlled-substance scheduling classification and approval pathway
- **Package insert / full prescribing information**: Retrieve TFDA-compatible prescribing information to complete the key warnings and contraindications profile
- **DDI profile**: Formal drug-drug interaction data was not retrieved; critical for co-medication risk assessment in target populations (elderly, palliative care)
- **Special population data**: Confirm dose adjustment recommendations for elderly, hepatic impairment, and renal impairment patients
- **Risk management plan**: Address dependence potential, rebound insomnia risk, and tapering protocol consistent with AASM 2017 guideline and 2024 RCT findings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

