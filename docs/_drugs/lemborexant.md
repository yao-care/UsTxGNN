---
layout: default
title: Lemborexant
parent: High Evidence (L1-L2)
nav_order: 843
evidence_level: L1
indication_count: 1
---

# Lemborexant
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Lemborexant: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Lemborexant (DAYVIGO) is a dual orexin receptor antagonist that was first approved in the US in December 2019 for adult insomnia.
The TxGNN model predicts it is effective for **sleep disorder, initiating and maintaining sleep**, which is essentially the same condition as its approved use.
The prediction is supported by **1 registered clinical trial** and **20 publications**, including several Phase 3 RCTs and network meta-analyses.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia in adults (from published literature; the license records carry no indication text) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license records (both NDA212028, so 1 unique NDA) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Lemborexant blocks both orexin receptors (OX1R and OX2R), with higher affinity for OX2R. Orexin is a key signal that promotes wakefulness and arousal. Blocking it lowers wake drive, which helps people fall asleep and stay asleep.

The predicted indication, difficulty initiating and maintaining sleep, is the same problem the drug was approved to treat. The high TxGNN score most likely reflects this existing approved use rather than a genuinely new repurposing signal. This should be confirmed against the US label. The Evidence Pack has no structured mechanism-of-action field, so the mechanism above comes from the published literature, not from DrugBank.

Related work points to possible extensions, not new indications. These include insomnia with mild obstructive sleep apnea, insomnia with psychiatric comorbidity, and use in older adults.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not yet recruiting | 15 | Double-blind, placebo-controlled trial of eszopiclone and lemborexant in obstructive sleep apnoea with a low arousal threshold and difficulty falling or staying asleep. No results yet. It concerns a comorbid subgroup and adds no direct evidence for primary insomnia. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant vs placebo and zolpidem ER in older adults with insomnia disorder |
| [32585700](https://pubmed.ncbi.nlm.nih.gov/32585700/) | 2020 | RCT (Phase 3, SUNRISE 2) | Sleep | Long-term efficacy and safety of lemborexant vs placebo in adults with insomnia disorder |
| [33636648](https://pubmed.ncbi.nlm.nih.gov/33636648/) | 2021 | RCT (long-term extension) | Sleep Med | Effectiveness and safety of up to 12 months of continuous lemborexant treatment (SUNRISE-2) |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic review / network meta-analysis | Lancet | Comparative effects of drug treatments for acute and long-term insomnia in adults |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Systematic review / network meta-analysis | Transl Psychiatry | Risk-benefit comparison of the three DORAs (daridorexant, lemborexant, suvorexant) |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Systematic review / network meta-analysis | Sleep Med Rev | Efficacy and tolerability ranking of 20 insomnia drugs in adults |
| [32531478](https://pubmed.ncbi.nlm.nih.gov/32531478/) | 2020 | Network meta-analysis | J Psychiatr Res | Lemborexant vs suvorexant on efficacy and safety outcomes, based on 4 double-blind RCTs |
| [39120786](https://pubmed.ncbi.nlm.nih.gov/39120786/) | 2024 | Pooled analysis of 3 trials | Drugs Aging | Efficacy and safety of lemborexant in older adults |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Post-hoc analysis | Sleep Med | Effect of lemborexant on sleep architecture in insomnia with mild obstructive sleep apnea |
| [32096020](https://pubmed.ncbi.nlm.nih.gov/32096020/) | 2020 | Drug profile | Drugs | "First Approval" article: dual OXR antagonist, approved in the USA in December 2019 for adult insomnia |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212028 | DAYVIGO (Eisai Inc.) | Tablet, film coated (oral) | Adult insomnia with sleep-onset and/or sleep-maintenance difficulty (from literature; label text not in the pack) |

The two license records are duplicates of the same NDA, so only one row is shown.

## Safety Considerations

Please refer to the package insert for safety information. The pack has no label warnings or contraindications, and the drug-interaction query returned no results. That should be read as missing data, not as evidence of no interactions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3 RCTs and several network meta-analyses support lemborexant for insomnia, and the drug is already marketed in the US. The prediction largely restates the approved use, so the main task is confirming the label and setting safety guardrails.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indication text), which is currently a blocking data gap
- Structured mechanism-of-action data from DrugBank
- A complete drug-interaction check, especially for CNS depressants and CYP3A inhibitors or inducers
- Safety guardrails to verify against the label:
  - next-day somnolence and impaired driving
  - complex sleep behaviors
  - caution in older adults, narcolepsy, and respiratory impairment
- Follow-up on NCT06928766 for any extension to insomnia with obstructive sleep apnea

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

