---
layout: default
title: Margetuximab
parent: Model Prediction Only (L5)
nav_order: 888
evidence_level: L5
indication_count: 2
---

# Margetuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Margetuximab: From HER2-Positive Metastatic Breast Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Margetuximab (Margenza) is an Fc-engineered anti-HER2 antibody, approved for pretreated HER2-positive metastatic breast cancer.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but this is a model output only, with **0 clinical trials** and **0 publications** supporting it and no plausible mechanistic link.
The model's second-ranked prediction, HER2-positive breast carcinoma, is the drug's existing approved use and is well supported (see the note below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive metastatic breast cancer (the license records list no indication text; taken from the FDA approval summary, PMID 34916216) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both under BLA761150) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Margetuximab is a chimeric anti-HER2 monoclonal antibody. It binds the HER2 extracellular domain and carries an Fc region engineered for higher affinity to CD16A (FcγRIIIa). This strengthens NK-cell-mediated antibody-dependent cellular cytotoxicity (ADCC).

**This prediction is not mechanistically supported.** The drug has no known role in bone remodeling (RANKL/OPG or Wnt/sclerostin signaling), and none in counteracting drug-induced bone loss. The high TxGNN score reflects graph-based model output, not biological or clinical evidence. We found no plausible link between HER2-directed ADCC and osteoporosis.

## Clinical Trial Evidence

Currently no related clinical trials registered for drug-induced osteoporosis.

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

## Note: Rank 2 Prediction (HER2-Positive Breast Carcinoma)

The second TxGNN prediction (score 99.05%) is the drug's own approved use, not a true repurposing candidate. It has Level L1 evidence in the pack and a "Proceed with Guardrails" recommendation. Key evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02492711](https://clinicaltrials.gov/study/NCT02492711) | Phase 3 | Completed | 624 | SOPHIA: margetuximab + chemotherapy vs trastuzumab + chemotherapy in pretreated HER2+ metastatic breast cancer |
| [NCT04425018](https://clinicaltrials.gov/study/NCT04425018) | Phase 2 | Active, not recruiting | 174 | MARGOT: neoadjuvant paclitaxel/pertuzumab with margetuximab vs trastuzumab in stage II-III HER2+ breast cancer |
| [NCT01148849](https://clinicaltrials.gov/study/NCT01148849) | Phase 1 | Completed | 66 | Dose escalation of MGAH22 (margetuximab) in refractory HER2+ cancers |
| [NCT04398108](https://clinicaltrials.gov/study/NCT04398108) | Phase 1 | Completed | 16 | PK, tolerability and safety of margetuximab plus chemotherapy in Chinese patients |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33480963](https://pubmed.ncbi.nlm.nih.gov/33480963/) | 2021 | RCT | JAMA Oncol | Phase 3 efficacy of margetuximab vs trastuzumab in pretreated ERBB2-positive advanced breast cancer |
| [36332179](https://pubmed.ncbi.nlm.nih.gov/36332179/) | 2023 | RCT | J Clin Oncol | SOPHIA final overall survival results |
| [34916216](https://pubmed.ncbi.nlm.nih.gov/34916216/) | 2022 | Regulatory review | Clin Cancer Res | FDA approval summary (Dec 16, 2020): margetuximab plus chemotherapy after ≥2 prior anti-HER2 regimens, at least one for metastatic disease |
| [33761116](https://pubmed.ncbi.nlm.nih.gov/33761116/) | 2021 | Review | Drugs | First approval; Fc engineered for increased CD16A binding and decreased CD32B binding |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761150 (MacroGenics, Inc) | MARGENZA | Injection, solution, concentrate | HER2+ metastatic breast cancer after ≥2 prior anti-HER2 regimens (per PMID 34916216; the license record has no indication text) |
| BLA761150 (TerSera Therapeutics LLC) | MARGENZA | Injection, solution, concentrate | Same as above |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Fc-engineered anti-HER2 monoclonal antibody with immune-mediated ADCC); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | LVEF and cardiac function (HER2-directed antibody class concern); other items per package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold** (for drug-induced osteoporosis)

**Rationale:**
The prediction rests solely on a model score. There are no trials or publications, and the mechanism does not connect anti-HER2 ADCC to bone metabolism. The drug's real value lies in its approved HER2-positive breast cancer use, which is not a repurposing case.

**To proceed, the following is needed:**
- A biologically plausible mechanism linking margetuximab to bone metabolism, with supporting preclinical data
- Complete MOA data from DrugBank
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Correction of the empty original-indication field in the source record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

