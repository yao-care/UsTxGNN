---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 1151
evidence_level: L5
indication_count: 1
---

# Selenium
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

# Selenium: From No Approved Indication to Sclerosing Cholangitis

## One-Sentence Summary

Selenium (DB11135) is a trace mineral with no current Taiwan/US market approval and no documented original indication in this evidence pack.
The TxGNN model predicts a possible association with **Sclerosing Cholangitis**,
but this is supported by only **0 clinical trials** and **5 loosely related publications**, none of which test selenium as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on record for this drug |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, selenium is an essential trace mineral typically used as a nutritional supplement or antioxidant cofactor; no approved therapeutic indication is on record in this evidence pack, so its established efficacy profile cannot be used to anchor this prediction.

The literature returned for this pairing does not support a treatment hypothesis. Instead, it describes selenium as a *biomarker of disease state* — for example, altered hepatic selenium retention and poor fat-soluble micronutrient intake observed in patients who already have primary sclerosing cholangitis (PSC). This is fundamentally different from evidence that selenium supplementation could treat or modify the course of PSC.

Given the absence of MOA data and the lack of any interventional study linking selenium to PSC treatment, the high TxGNN score (99.04%) should be interpreted as a knowledge-graph statistical association only — likely driven by co-occurrence of "selenium" and "PSC" in nutritional/deficiency literature — rather than a validated mechanistic or clinical hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Cohort | Liver International | PSC patients show poor fat-soluble vitamin intake and dietary quality; does not address selenium supplementation as therapy |
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Cohort | Scand J Gastroenterol | Describes abnormal hepatic retention of copper and selenium in PSC patients — a disease-associated metabolic finding, not a treatment effect |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | Cohort | Proteomics | Murine hepatic proteome changes in fibrosis/sclerosing cholangitis models; no selenium intervention studied |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Case report | JPEN | Case report on parenteral nutrition (incl. lipid emulsion) in a patient with overlapping PSC and ulcerative colitis; selenium not the focus |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | Review | Eur J Cancer Prev | Review of colorectal cancer chemoprevention agents (aspirin, NSAIDs); unrelated to PSC, low relevance |

## US Market Information

No marketing authorizations on record — market status is 未上市 (not marketed), 0 total licenses.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warnings/contraindications and DDI data are currently unavailable — this is a blocking data gap for any safety evaluation, see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association rests solely on a high TxGNN model score with no mechanistic rationale (MOA data missing) and no interventional evidence — all supporting literature describes selenium as a disease-associated biomarker in PSC, not as a treatment. Combined with the absence of any market approval and a blocking safety data gap, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for selenium, ideally with specific relevance to cholestatic/fibrotic liver pathways
- TFDA/FDA package insert data covering warnings, contraindications, and drug interactions (currently blocking — DG001)
- At least one interventional (not observational) study testing selenium supplementation in PSC or related sclerosing cholangitis models
- Re-evaluation of the TxGNN score's underlying evidence path to rule out spurious biomarker-driven association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

