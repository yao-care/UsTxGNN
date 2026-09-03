---
layout: default
title: Secnidazole
parent: 僅模型預測 (L5)
nav_order: 1148
evidence_level: L5
indication_count: 7
---

# Secnidazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Secnidazole: From Bacterial Vaginosis to Vaginal Discharge

## One-Sentence Summary

Secnidazole is a 5-nitroimidazole antimicrobial/antiprotozoal agent, marketed internationally (as Solosec®) for bacterial vaginosis and trichomoniasis, but not yet marketed in Taiwan.
The TxGNN model's best-supported prediction is that Secnidazole effectively resolves **Vaginal Discharge**, the hallmark symptom of bacterial vaginosis/trichomoniasis, with **5 clinical trials (including 2 pivotal Phase 3 RCTs)** and **17 publications** currently supporting this direction.

> This evidence pack contains 7 TxGNN-predicted indications for secnidazole. This report focuses on **Vaginal Discharge** (the candidate with the strongest, decision-ready evidence — L1, Proceed with Guardrails). A closely related, already-confirmed indication (trichomonal vulvovaginitis) and several low-plausibility, unsupported predictions (postmenopausal atrophic vaginitis, vulvar neoplasm, vulvar ulceration, vaginal leukoplakia) are addressed in the Conclusion.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in Taiwan; internationally approved for bacterial vaginosis (Solosec®, US FDA 2017) |
| Predicted New Indication | Vaginal Discharge (bacterial vaginosis / trichomoniasis symptom) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The formal DrugBank mechanism-of-action field for secnidazole is currently a data gap. However, based on its established pharmacological class, secnidazole is a second-generation 5-nitroimidazole (same family as metronidazole and tinidazole, but with a longer half-life of ~17 hours). After reduction by anaerobic bacterial or protozoal nitroreductases, it generates reactive intermediates that damage pathogen DNA, giving it activity against anaerobic bacteria (e.g., *Gardnerella vaginalis*) and protozoa (*Trichomonas vaginalis*).

Abnormal vaginal discharge is the defining clinical symptom of bacterial vaginosis and trichomoniasis — the two conditions secnidazole is already approved to treat internationally. The TxGNN prediction therefore does not represent a novel biological mechanism, but rather links the drug to the downstream symptom of an indication it already treats. This makes the mechanistic rationale direct and well-established, rather than speculative.

A closely related prediction in the same evidence pack, **trichomonal vulvovaginitis**, is even stronger in this respect: the FDA approved Solosec® for trichomoniasis in adult women in 2021 based on a pivotal Phase 3 RCT (PMID 33768237). From a global regulatory standpoint this is a confirmed indication, not merely a model prediction; it only appears here because secnidazole is not yet registered in Taiwan.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Phase 3 | Completed | 147 | Randomized, double-blind, placebo-controlled pivotal trial of single-dose Solosec® granules; key registration evidence for symptomatic relief (incl. discharge) |
| [NCT02147899](https://clinicaltrials.gov/study/NCT02147899) | Phase 2 | Completed | 215 | Randomized, double-blind, placebo-controlled trial of secnidazole (SYM-1219) for BV; symptom endpoints included discharge |
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Phase 3 | Completed | 118 | Secnidazole + fluconazole combination for symptomatic vaginal discharge in mixed BV/Candida infections |
| [NCT05033743](https://clinicaltrials.gov/study/NCT05033743) | Phase 2/3 | Completed | 24 | Pilot study of weekly secnidazole granules for suppression of recurrent BV over 18 weeks |
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Phase 4 | Completed | 40 | Post-marketing safety study of single-dose Solosec® 2g in adolescent girls with BV |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | RCT (Phase 3) | Am J Obstet Gynecol | Pivotal double-blind, placebo-controlled trial establishing efficacy/safety of single-dose secnidazole 2g granules for BV |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | RCT (Phase 3) | Infect Dis Obstet Gynecol | Multicenter double-blind, double-dummy noninferiority trial: secnidazole vs. metronidazole for BV |
| [22529484](https://pubmed.ncbi.nlm.nih.gov/22529484/) | 2012 | Comparative RCT | Indian J Pharmacol | Compared single-dose metronidazole, tinidazole, secnidazole, and ornidazole cure rates in BV |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Systematic Review/Meta-analysis | Eur J Obstet Gynecol Reprod Biol | Pooled efficacy/safety of single-dose oral secnidazole 2g for BV |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Systematic Review/Network Meta-analysis | Front Cell Infect Microbiol | Comparative efficacy/safety of multiple drugs (incl. secnidazole) for BV |
| [29323627](https://pubmed.ncbi.nlm.nih.gov/29323627/) | 2018 | Phase 3, Open-label | J Womens Health | Safety of single-dose secnidazole 2g granules in US women/adolescents with BV |
| [29132478](https://pubmed.ncbi.nlm.nih.gov/29132478/) | 2017 | RCT | J Coll Physicians Surg Pak | Compared vaginal clindamycin vs. single oral-dose secnidazole for symptomatic BV |
| [15733882](https://pubmed.ncbi.nlm.nih.gov/15733882/) | 2005 | Clinical Study | Int J Gynaecol Obstet | Evaluated whether low-dose (1g) secnidazole cures BV |
| [31499057](https://pubmed.ncbi.nlm.nih.gov/31499057/) | 2020 | Review | Am J Obstet Gynecol | Discharge/malodor as the hallmark BV symptom; treatment reduces post-surgical infection risk |
| [9617020](https://pubmed.ncbi.nlm.nih.gov/9617020/) | 1998 | Comparative Study | Ginecol Obstet Mex | Oral itraconazole + secnidazole vs. topical ovules for symptomatic vaginitis |

## US Market Information

Secnidazole currently has **no marketing authorization on file in Taiwan** — this evidence pack records 0 licenses. Internationally, it is marketed as **Solosec®** (single-dose oral granule formulation), FDA-approved in the United States (2017 for bacterial vaginosis; 2021 for trichomoniasis). No Taiwan NDA data is available for tabulation.

## Safety Considerations

No verified prescribing warnings, contraindications, or drug-drug interaction data are currently available for secnidazole in this evidence pack. This is flagged as a **blocking data gap**, meaning a formal safety pre-assessment cannot yet proceed. Please refer to the package insert (once a Taiwan label exists) or the current Solosec® US prescribing information for interim safety guidance.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs plus consistent supportive literature (including systematic reviews) establish that secnidazole resolves the discharge symptom of bacterial vaginosis, an indication already FDA-approved internationally. The main barriers are administrative (no Taiwan license) rather than scientific.

**To proceed, the following is needed:**
- Resolve the blocking safety data gap: obtain TFDA-equivalent prescribing warnings/contraindications (or adopt Solosec® US labeling as interim reference)
- Obtain formal DrugBank/MOA documentation to close the mechanism data gap
- Assess Taiwan regulatory pathway for market entry (new drug application vs. named-patient/off-label use)
- Confirm secnidazole's independent contribution to vulvovaginal candidiasis efficacy (current evidence is confounded by fluconazole co-administration) — treat as a **Research Question**, not an actionable indication yet
- No further action needed on postmenopausal atrophic vaginitis, vulvar neoplasm, vulvar ulceration, or vaginal leukoplakia — these predictions have no supporting trials or literature and show no plausible mechanistic link to secnidazole's antimicrobial/antiprotozoal activity; **Hold**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

