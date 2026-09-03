---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 1126
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Psoriasis to Dermatitis

## One-Sentence Summary

> Risankizumab (Skyrizi) is an anti-IL-23p19 monoclonal antibody originally approved for moderate-to-severe **psoriasis** (first approved in Japan in 2019, per literature record).
> The TxGNN model predicts it may also be effective for **Dermatitis** — with the strongest signal pointing to atopic dermatitis —
> supported by **7 clinical trials** (including one completed Phase 2 RCT specifically in atopic dermatitis) and **20 publications**, though this remains a secondary, less mechanistically typical signal compared to its established psoriasis indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this jurisdiction (drug not marketed locally); per literature (PMID 31098898), first global approval was for psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis, and erythrodermic psoriasis |
| Predicted New Indication | Dermatitis (evidence concentrated in atopic dermatitis) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was flagged as a data gap in this evidence pack. Based on information recovered from the accompanying literature (PMID 31098898), risankizumab is a humanized IgG monoclonal antibody that targets the p19 subunit of interleukin-23 (IL-23), blocking downstream Th17-pathway signaling. This mechanism is well established as pathogenic in plaque psoriasis, which is why risankizumab is already an approved biologic for that condition (confirmed by Phase 4 trials NCT05969223 and NCT04908475 in this pack, both of which test risankizumab against its *existing* psoriasis indication rather than a new one).

The predicted indication "dermatitis" is a broad category, and the clinical/literature evidence in this pack is concentrated almost entirely on **atopic dermatitis (AD)**, a distinct disease driven primarily by the Th2/Th22 axis rather than Th17/IL-23. This is mechanistically less typical than psoriasis, but not implausible — IL-22 and, to a lesser extent, IL-23 have been implicated in AD pathophysiology, providing rationale for testing IL-23 blockade in this population.

The strongest piece of direct evidence is a completed Phase 2, randomized, double-blind, placebo-controlled trial (NCT03706040 / PMID 36588137) that directly evaluated risankizumab in moderate-to-severe AD in adults and adolescents. This is a genuine repurposing signal — a real interventional trial outside the approved psoriasis indication — but it is a single Phase 2 study, and other trials in the evidence pack (e.g., real-world psoriasis cohort studies, pediatric biologics reviews) are only indirectly relevant, since they describe risankizumab's use in its already-approved psoriasis indication or discuss it alongside other biologics rather than testing it in AD.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomized, double-blind, placebo-controlled trial assessing safety/efficacy of risankizumab in moderate-to-severe atopic dermatitis in adults and adolescents — the key direct repurposing evidence. |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Randomized, double-blind study of risankizumab for genital and scalp psoriasis; confirms existing psoriasis indication, not a new-indication signal. |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Open-label study comparing risankizumab to apremilast in moderate plaque psoriasis; existing-indication comparative effectiveness data. |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completed | 240 | Taiwan-based prospective observational cohort on durability of risankizumab response (PASI90) vs other biologics in chronic plaque psoriasis. |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Multi-center observational biomarker study profiling six immune-mediated inflammatory skin diseases including atopic dermatitis; provides mechanistic/biomarker context rather than treatment efficacy. |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective pharmacogenetic study on biologic drug survival in cutaneous psoriasis; indirect relevance via genetic/metabolic predictors. |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Exploratory microdevice study testing FDA-approved atopic dermatitis/psoriasis drugs via intradermal delivery; small, early-stage, low evidentiary weight. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2 RCT results: risankizumab tested in moderate-to-severe AD, rationale based on Th2/Th22/Th17 pathway overlap and IL-23/IL-22 blockade. |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/small molecules for pediatric alopecia areata, psoriasis, AD, and hidradenitis suppurativa. |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opin Biol Ther | Review of current/emerging biologics for pediatric atopic dermatitis, including IL-23-targeted agents in trials. |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Review | Am J Clin Dermatol | Systematic review of systemic therapies (including risankizumab) for erythrodermic psoriasis management. |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Reappraisal of systemic immunomodulators for psoriasis and eczema, relevant to service-member populations. |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Review | Inflammopharmacology | Systematic review of IL-inhibitor therapeutic and paradoxical effects in lichen planus, an inflammatory dermatosis. |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "First Global Approval" review — confirms mechanism (anti-IL-23p19 mAb) and original psoriasis-family approval. |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Cohort | Int J Dermatol | Effectiveness/safety of combined dupilumab and risankizumab in patients with concomitant AD and psoriasis. |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Cohort | Experimental Dermatology | Retrospective study of risankizumab in patients with history of erythrodermic psoriasis; predictors of response. |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case Report | J Dermatolog Treat | Case report of acrodermatitis continua of Hallopeau successfully and rapidly treated with risankizumab. |

---

## US Market Information

Risankizumab has **no marketing authorizations recorded in this jurisdiction** (market status: Not Marketed; 0 total licenses). No license-level data (authorization number, product name, dosage form, approved indication text) is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT directly tested risankizumab in atopic dermatitis (NCT03706040 / PMID 36588137), giving this candidate real interventional evidence (L2) rather than prediction alone. However, the predicted category "dermatitis" is broad, the mechanistic fit to AD (Th2-driven) is weaker than to psoriasis (Th17/IL-23-driven, already approved), and most of the surrounding trial/literature evidence in this pack pertains to risankizumab's *existing* psoriasis indication rather than new-indication support.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a blocking data gap — required before any S1 safety pre-assessment)
- Confirmed mechanism-of-action documentation from DrugBank (currently a data gap affecting mechanistic-linkage confidence)
- Clarification of which specific dermatitis subtype (atopic dermatitis vs. broader category) the prediction targets, since evidence strength varies substantially by subtype
- Later-phase (Phase 3) confirmatory trial data in atopic dermatitis before considering this beyond a guardrailed/exploratory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

