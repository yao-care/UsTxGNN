---
layout: default
title: Oxitriptan
parent: 僅模型預測 (L5)
nav_order: 1003
evidence_level: L5
indication_count: 1
---

# Oxitriptan
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

# Oxitriptan: From No Approved Indication to Insomnia

## One-Sentence Summary

> Oxitriptan (5-hydroxytryptophan, 5-HTP) currently has no approved indication and is not marketed in Taiwan.
> The TxGNN model predicts it may be effective for **Insomnia**,
> with **6 clinical trials** and **13 publications** currently identified, though most evidence is preclinical or only indirectly related.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is unmarketed with no recorded approved indication |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA field is a data gap). Based on the information available, oxitriptan (5-HTP) is a direct precursor of serotonin biosynthesis — it is metabolized via the serotonergic pathway and can be further converted to melatonin through N-acetylation and methylation. This pathway provides a theoretical basis for a role in sleep regulation, and is the same rationale underlying over-the-counter 5-HTP supplements marketed for sleep support.

However, since `original_indications` is empty and the drug is not currently marketed in Taiwan, there is no established original indication to compare against. The link to insomnia should therefore be regarded as a mechanistic hypothesis derived from serotonin/melatonin physiology rather than a validated repurposing relationship. Most supporting literature uses PCPA (p-chlorophenylalanine)-induced insomnia animal models to study the serotonergic (5-HT) system broadly, rather than testing oxitriptan itself — this indirect evidence base is consistent with the mechanistic (not clinical) nature of the current support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001918](https://clinicaltrials.gov/study/NCT00001918) | N/A | Completed | 20 | Clinical evaluation of L-5-hydroxytryptophan-related eosinophilia-myalgia syndrome (EMS); provides human exposure/safety data for 5-HTP but not an efficacy trial for insomnia |
| [NCT06893822](https://clinicaltrials.gov/study/NCT06893822) | N/A | Recruiting | 20 | Randomized, double-blind, placebo-controlled crossover study of Griffonia simplicifolia (natural 5-HTP source) on pain and sensitization, not insomnia |
| [NCT04078724](https://clinicaltrials.gov/study/NCT04078724) | N/A | Completed | 33 | RCT assessing 5-HTP supplementation's impact on sleep quality and gut microbiome in older adults with normal cognition vs. mild cognitive impairment |
| [NCT03364101](https://clinicaltrials.gov/study/NCT03364101) | N/A | Completed | 60 | Explored relationship between an experimental "PowerOff" intervention and sleep quality using actigraphy; drug/compound identity unclear |
| [NCT06365801](https://clinicaltrials.gov/study/NCT06365801) | N/A | Not Yet Recruiting | 100 | Acupoint biological characteristics in irritable bowel syndrome — likely keyword mismatch, not directly relevant |
| [NCT06718452](https://clinicaltrials.gov/study/NCT06718452) | N/A | Not Yet Recruiting | 100 | umPEALUT for tinnitus targeting neuroinflammation — not directly relevant to oxitriptan or insomnia |

**Note:** Only NCT00001918 and NCT04078724 involve 5-HTP directly; neither is a controlled efficacy trial of oxitriptan for insomnia specifically. The remaining trials are low-relevance or likely search mismatches.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2962265](https://pubmed.ncbi.nlm.nih.gov/2962265/) | 1987 | Review | Revue medicale de la Suisse romande | Discusses clinical indications for L-5-hydroxytryptophan in neurology, including sleep-related conditions |
| [4128428](https://pubmed.ncbi.nlm.nih.gov/4128428/) | 1974 | Case Report | Electroencephalography and Clinical Neurophysiology | Reports a favorable effect of 5-hydroxytryptophan in a case of severe prolonged insomnia (agrypnia) associated with Morvan's disease |
| [33634088](https://pubmed.ncbi.nlm.nih.gov/33634088/) | 2021 | Review | Frontiers in Bioengineering and Biotechnology | Reviews 5-HTP's physiological roles in sleep, mood, and pain regulation, and its therapeutic use in insomnia, depression, and migraine |
| [32006050](https://pubmed.ncbi.nlm.nih.gov/32006050/) | 2020 | Preclinical | Applied Microbiology and Biotechnology | Describes microbial biosynthesis of 5-HTP, noting its established use for insomnia, depression, and chronic headache |
| [4548556](https://pubmed.ncbi.nlm.nih.gov/4548556/) | 1974 | Case Report | Revue neurologique | Polygraphic/metabolic study of persistent insomnia with hallucinations in a case of Morvan's fibrillar chorea (companion report to NCT-independent 5-HTP case) |
| [40350945](https://pubmed.ncbi.nlm.nih.gov/40350945/) | 2025 | Animal Model | China Journal of Chinese Materia Medica | Fushen Decoction improved PCPA-induced insomnia in mice via modulation of the 5-HT system and GABA expression, supporting serotonergic relevance to sleep |
| [39710185](https://pubmed.ncbi.nlm.nih.gov/39710185/) | 2024 | Animal Model | Neuroscience Letters | Sleep deprivation impaired pineal melatonin secretion via AMPK/FOXO3a-mediated autophagy inhibition, linking the serotonin-melatonin pathway to insomnia-depression comorbidity |
| [40493075](https://pubmed.ncbi.nlm.nih.gov/40493075/) | 2025 | Animal Model | Psychopharmacology | Ginsenoside Rg1 alleviated PCPA-induced insomnia via NLRP3 inflammasome inhibition through the Nrf2/HO-1 pathway |
| [40367689](https://pubmed.ncbi.nlm.nih.gov/40367689/) | 2025 | Animal Model | International Immunopharmacology | Cinnamic acid promoted sleep in a PCPA-induced insomnia rat model |
| [40160035](https://pubmed.ncbi.nlm.nih.gov/40160035/) | 2025 | Animal Model | International Journal of Neuropsychopharmacology | Nuciferine enhanced rodent sleep via modulation of the serotonergic system |

**Note:** No RCTs of oxitriptan for insomnia were identified. Direct drug-relevant evidence (2962265, 4128428, 4548556) is old case-level/review literature; the remaining items are mechanistic animal studies of the broader serotonergic pathway in insomnia, using compounds other than oxitriptan.

---

## Market Information

This drug currently has no approved licenses and is not marketed. No product registration data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** TFDA label warnings/contraindications data is a blocking gap (DG001) — this drug cannot yet complete an S1 safety pre-assessment without this information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to L4 (preclinical/mechanistic studies and indirect case reports); no controlled clinical trial has evaluated oxitriptan specifically for insomnia, and the drug is not currently marketed with no established original indication for comparison.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking — required for S1 safety pre-assessment)
- Mechanism of action (MOA) documentation from DrugBank to support the mechanistic rationale
- Clinical trials or observational studies directly testing oxitriptan (not other serotonergic agents or 5-HTP-containing supplements) for insomnia
- Clarification of market/regulatory status before further development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

