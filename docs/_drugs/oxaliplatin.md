---
layout: default
title: Oxaliplatin
parent: Model Prediction Only (L5)
nav_order: 999
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a platinum-based chemotherapy drug, best known for treating colorectal cancer. The source label data did not include an indication text, so that original use comes from the literature (PMID 10936465) and general knowledge. The TxGNN model predicts it may be effective for **malignant pleural mesothelioma**. Support is **2 directly relevant clinical trials** (Phase 2, small, single-arm or unknown status) and about **20 publications**, which include several Phase 2 studies with mixed results.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (not stated in the U.S. license data, which has no indication text; taken from PMID 10936465) |
| Predicted New Indication | Malignant pleural mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 (as assigned in the pack; the Phase 2 studies are single-arm, not randomized, so this is at the low end) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source data. Oxaliplatin is a DNA-crosslinking platinum agent (a third-generation cisplatin analogue, per PMID 10936465). Platinum cytotoxicity is already the backbone of mesothelioma chemotherapy. The current standard first-line regimen is pemetrexed plus a platinum compound, as described in PMID 26526504.

Colorectal cancer and pleural mesothelioma are different diseases. The link is the drug class rather than shared biology. Phase 2 studies combined oxaliplatin with gemcitabine, raltitrexed or vinorelbine in mesothelioma, and an in vitro study (PMID 25028262) suggests platinum agents can be potentiated in pleural mesothelioma cells.

The evidence is not uniformly positive. A second-line raltitrexed-oxaliplatin study was closed for lack of objective responses (PMID 15893013). Review articles note that response rates above 30% have rarely been achieved in this disease. The high TxGNN score therefore points to a plausible research question, not proven benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin + gemcitabine as first- or second-line chemotherapy in pleural or peritoneal mesothelioma. Primary question is response rate. Single-arm and small; no results in the pack. |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib (Velcade) + oxaliplatin (Eloxatin) in previously treated pleural or peritoneal mesothelioma. The combination confounds attribution to oxaliplatin. |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1000 | International PIPAC/PITAC registry for peritoneal and pleural malignancies. Not specific to mesothelioma or oxaliplatin. |

The search also returned three trials that do not evaluate oxaliplatin in mesothelioma: NCT06310473 (esophagogastric cancer), NCT05107674 and NCT07532902 (Phase 1 basket trials). They are omitted from the table.

---

## Literature Evidence

No randomized controlled trials were found. The table lists Phase 2 clinical studies first, then reviews and preclinical work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 | J Clin Oncol | Raltitrexed + oxaliplatin in 70 patients (15 pretreated, 55 chemo-naive); the authors describe it as an active regimen. |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 (multicenter) | Clin Lung Cancer | Gemcitabine + oxaliplatin in 25 patients, up to 6 cycles. |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 | Lung Cancer | Second-line raltitrexed-oxaliplatin in 14 patients: no objective responses, stable disease in 4 (28.6%); trial closed. |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 | Lung Cancer | Vinorelbine + oxaliplatin as first-line therapy in untreated patients. |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase 2 pilot | Tumori | Oxaliplatin + raltitrexed in inoperable disease, following an earlier Phase 1 signal of activity. |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Observational | J Occup Med Toxicol | Oxaliplatin ± gemcitabine in patients pretreated with pemetrexed. |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Institutional review | Eur J Cancer | Gustave Roussy experience in 163 patients across seven trials, including raltitrexed-oxaliplatin. |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | Chemotherapy for mesothelioma; response rates above 30% rarely achieved with established drugs. |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review / lab study | Int J Mol Sci | Effect of cisplatin, oxaliplatin and pemetrexed on immune checkpoint expression, relevant to chemo-immunotherapy design. |
| [25028262](https://pubmed.ncbi.nlm.nih.gov/25028262/) | 2015 | Preclinical (in vitro) | Hum Exp Toxicol | EF24 and RAD001 potentiated platinum agents in MSTO-211H mesothelioma cells. |

Note: PMID 15261443 appears to be a duplicate record of the 2003 review (12610498) and is not counted separately.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA207325 | Oxaliplatin (Gland Pharma Limited) | Injection, solution | — |
| ANDA078817 | Oxaliplatin (Sandoz Inc) | Injection, solution | — |
| ANDA204368 | Oxaliplatin (BluePoint Laboratories) | Injection, solution | — |
| ANDA091358 | Oxaliplatin (Mylan Institutional LLC) | Injection, solution | — |

All 20 licenses are injectables (solution, lyophilized powder, and concentrate). The source data contains no approved indication text.

---

## Cytotoxicity

This section is based on general knowledge of the platinum class, not on data in the pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum, DNA-crosslinking) |
| Myelosuppression Risk | Medium (neutropenia and thrombocytopenia are expected with platinum combinations) |
| Emetogenicity Classification | Medium |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, and neurological assessment (peripheral neuropathy is a recognized class concern) |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for authoritative details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Phase 2 studies show some activity for oxaliplatin combinations in mesothelioma, but they are small and single-arm. At least one second-line study was negative, and there is no randomized comparison against the standard pemetrexed-platinum regimen. Package insert safety data is missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (download and parse the FDA label)
- Mechanism-of-action data from DrugBank
- Confirmation of the approved indication text, which is empty in the current license records
- Full-text review of the Phase 2 studies (response rate, survival, toxicity) and results from NCT00859469
- Comparison against the pemetrexed-platinum standard, ideally in a randomized design

Other predicted indications are weaker. Malignant epithelioid mesothelioma (score 99.49%) rests mainly on peritoneal HIPEC/PIPAC data. Sarcomatoid mesothelioma and malignant visceral pleura tumor are both on Hold with L4 evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

