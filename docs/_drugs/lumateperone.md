---
layout: default
title: Lumateperone
parent: 僅模型預測 (L5)
nav_order: 877
evidence_level: L5
indication_count: 9
---

# Lumateperone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Lumateperone: Original Indication Not Documented → Predicted Signal for Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Lumateperone's original indication and mechanism of action are not available in this Evidence Pack (both flagged as data gaps, one of them Blocking). The TxGNN model predicts a possible link to **retinal dystrophy with or without extraocular anomalies**, but this is supported by **0 clinical trials** and **15 publications that do not mention lumateperone at all** — the evidence pack's own mechanistic assessment concludes there is no known or plausible biological link between the drug and this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licenses or indication text in this Evidence Pack (Data Gap, drug's original use is not documented) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.97% (rank 1345 among all predictions) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lumateperone in this Evidence Pack (DG002, High severity). Based on the repurposing rationale supplied alongside the prediction, lumateperone is understood to act as a modulator of 5-HT2A, D1, and D2 receptors and an inhibitor of the serotonin transporter (SERT) — a centrally-acting neurotransmission-modulating profile typically associated with psychiatric indications.

Retinal dystrophy with or without extraocular anomalies, however, is a congenital/structural developmental eye disorder, not a disease driven by neurotransmitter imbalance. The Evidence Pack's own mechanistic assessment is explicit on this point: **there is no known or biologically plausible connection** between lumateperone's receptor-modulation mechanism and this disease. The very high TxGNN score (99.97%) is not corroborated by any clinical, literature, or mechanistic support — it should be treated as a raw model output rather than a validated signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 15 publications returned by the search co-mention the drug and disease terms but, on review of their abstracts, are general ophthalmology/orbital-disease reviews and case reports — **none discuss lumateperone specifically**. They are listed here for transparency, not as evidence of drug efficacy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | General review of orbital infections; no mention of lumateperone or retinal dystrophy treatment |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Clinical approach to diplopia; unrelated to the drug |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging review of pediatric ocular pathologies including congenital retinal/vitreous conditions |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape; developmental eye disorder background only |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis review; unrelated to the drug |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Case report of unilateral cryptophthalmia; unrelated to the drug |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome vitreoretinal degeneration review |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Review | Int J Mol Sci | Retinal abnormalities in congenital fibrosis of extraocular muscles (genetic disorder) |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders review |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Pathogenesis/treatment of maculopathy with cavitary optic disc anomalies |

## US Market Information

No market authorization records are available. `market_status` is recorded as "Not Marketed" with 0 licenses on file.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this Evidence Pack; DG001 — TFDA label warnings/contraindications — is rated Blocking severity, meaning it must be resolved before any safety pre-assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at Evidence Level L5 — a model score with no supporting clinical trials, no relevant literature, and no plausible mechanistic link (the drug's presumed neurotransmitter-modulating mechanism does not align with a congenital structural eye disorder). This same pattern (very high TxGNN score, zero trials/literature, Hold recommendation) also holds for all other ranked candidates for this drug (ranks 2–9: polymicrogyria/cerebellar hypoplasia, hydranencephaly, CMT1G, X-linked myopia variants, glycosylation disorder, atypical glycine encephalopathy), suggesting the model is not currently producing a differentiated, actionable repurposing signal for lumateperone.

**To proceed, the following is needed:**
- Original indication and mechanism of action data for lumateperone (currently undocumented in this pack)
- TFDA label warnings/contraindications (DG001, Blocking — required before any safety pre-assessment)
- Drug-specific clinical or preclinical evidence connecting lumateperone to retinal dystrophy or any other candidate indication before advancing past S0
- Reassessment of whether this drug/indication pair merits continued monitoring, given the absence of a plausible mechanistic hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

