---
layout: default
title: Suvorexant
parent: Model Prediction Only (L5)
nav_order: 1190
evidence_level: L5
indication_count: 1
---

# Suvorexant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Suvorexant: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Suvorexant (marketed in the US as Belsomra) is a sleep medication. The Evidence Pack has no approved-indication text for it, but the published literature on the drug is entirely about insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially insomnia. This is close to a re-discovery of its known use rather than a true new indication.
Support consists of **1 registered clinical trial (withdrawn, never enrolled)** and **20 publications**, mostly systematic reviews and network meta-analyses.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (all license records have empty indication text). The literature consistently describes suvorexant as an insomnia treatment. |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 records, all under the same NDA (NDA204569) |
| Recommended Decision | Proceed with Guardrails |

Evidence level note: the trial registry entry is a withdrawn Phase 4 study, so it cannot count toward the L1 rule. L1 rests on a published paper reporting two pivotal 3-month Phase 3 RCTs (PMID 25526970). I did not verify the registry records for those trials, so the rating is provisional.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. The literature describes suvorexant as an orexin receptor antagonist. Orexin is a hypothalamic neuropeptide that promotes wakefulness, and heightened orexin signaling is linked to chronic insomnia. Blocking it is meant to reduce arousal and help sleep. Several reviews place suvorexant among the dual orexin receptor antagonists (DORAs), alongside lemborexant and daridorexant.

The predicted indication, difficulty falling asleep and staying asleep, is the core definition of insomnia. The prediction therefore matches suvorexant's established use and is mechanistically coherent, but it adds little that is new. The potentially novel angle is insomnia that occurs with psychiatric conditions. A 2024 systematic review examined DORAs, including suvorexant, for insomnia comorbid with psychiatric disorders. A trial in bipolar depression with insomnia was registered but withdrawn.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03764683](https://clinicaltrials.gov/study/NCT03764683) | Phase 4 | Withdrawn | 0 | Double-blind sequential parallel study of suvorexant added to usual treatment in bipolar depression with insomnia. It was planned to assess benefit and side effects. No participants were enrolled, so there are no results. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [25526970](https://pubmed.ncbi.nlm.nih.gov/25526970/) | 2016 | RCT (two pivotal Phase 3 trials) | Biological Psychiatry | Results from two 3-month randomized controlled trials of suvorexant, an orexin receptor antagonist, in insomnia. |
| [40555730](https://pubmed.ncbi.nlm.nih.gov/40555730/) | 2025 | Network meta-analysis | Translational Psychiatry | Compares the risk-benefit balance of daridorexant, lemborexant, and suvorexant in adults with insomnia. |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Network meta-analysis | Drugs | Compares the effectiveness, safety, and tolerability of insomnia drugs across 153 randomized trials. |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Comparative effectiveness of drugs for acute and long-term treatment of adult insomnia disorder. |
| [32531478](https://pubmed.ncbi.nlm.nih.gov/32531478/) | 2020 | Network meta-analysis | Journal of Psychiatric Research | Lemborexant vs suvorexant; four double-blind RCTs (n = 3237) compared for efficacy and safety. |
| [37257468](https://pubmed.ncbi.nlm.nih.gov/37257468/) | 2023 | Network meta-analysis | Arquivos de Neuro-Psiquiatria | Asks whether one DORA is superior to the others for chronic insomnia. |
| [39277609](https://pubmed.ncbi.nlm.nih.gov/39277609/) | 2024 | Systematic review | Translational Psychiatry | Evidence for lemborexant and suvorexant in insomnia comorbid with psychiatric disorders. |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical practice guideline | Journal of Clinical Sleep Medicine | American Academy of Sleep Medicine recommendations on drug treatment of chronic insomnia in adults, drug by drug. |
| [37086045](https://pubmed.ncbi.nlm.nih.gov/37086045/) | 2023 | Review | Journal of Sleep Research | History of orexin and the role of orexin receptor antagonists in insomnia. |
| [40943625](https://pubmed.ncbi.nlm.nih.gov/40943625/) | 2025 | Review | International Journal of Molecular Sciences | Compares DORAs (suvorexant, lemborexant, daridorexant) with GABAergic hypnotics and reviews efficacy and safety. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA204569 | BELSOMRA | Tablet, film coated (oral) | Merck Sharp & Dohme LLC |

The four license records are identical entries under NDA204569. Approved-indication text is empty in the source data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication matches suvorexant's established use in insomnia, and it is backed by Phase 3 trial publications, network meta-analyses, and clinical guidelines. It is a marketed drug, so this is not a new repurposing opportunity. The one registered trial is withdrawn, and the safety data in the pack is empty.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications) to complete safety screening
- Detailed mechanism-of-action data from DrugBank
- The approved-indication text for NDA204569, to confirm the original indication and that the prediction is not simply the approved use
- Registry confirmation of the two pivotal Phase 3 trials behind PMID 25526970, to firm up the L1 rating
- If a genuinely new use is intended, such as insomnia comorbid with bipolar disorder or other psychiatric conditions, a prospective trial, since NCT03764683 never enrolled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

