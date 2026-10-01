---
layout: default
title: Selumetinib
parent: Model Prediction Only (L5)
nav_order: 1154
evidence_level: L5
indication_count: 10
---

# Selumetinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Selumetinib: From NF1 Plexiform Neurofibromas to Familial Generalized Lentiginosis

## One-Sentence Summary

Selumetinib is a MEK1/2 inhibitor of the RAS-MAPK pathway, marketed in the US as KOSELUGO and used for NF1-related plexiform neurofibromas.
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**, but **no clinical trials and no publications** currently support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NF1-related plexiform neurofibromas (the license records carry no indication text, so this comes from the drug's known approved use) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (2 unique NDAs: NDA213756, NDA219943) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Selumetinib inhibits MEK1/2 in the RAS-MAPK pathway. The Evidence Pack has no detailed mechanism-of-action entry, so this description comes from the mechanistic notes attached to the prediction.

Lentiginosis phenotypes overlap with RASopathies. For example, café-au-lait macules are a hallmark of NF1. Selumetinib is already used in NF1, so a pathway-level link to pigmentary phenotypes is plausible.

This link is only a hypothesis. No disease-specific mechanism has been established for familial generalized lentiginosis, and no supporting studies were retrieved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications with Evidence

The top-ranked prediction has no evidence. Two lower-ranked predictions for selumetinib do:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Key Evidence |
|------|------|------|------|------|
| 9 | Peripheral nerve schwannoma | 99.95% | L3 | [NCT03095248](https://clinicaltrials.gov/study/NCT03095248): Phase 2 single-arm trial in NF2-related tumors, terminated early with 10 patients. Preclinical data ([PMID 19804833](https://pubmed.ncbi.nlm.nih.gov/19804833/)) show MEK1/2 inhibition reduces ERK activation and proliferation in primary human schwannoma cells. A case report ([PMID 38058737](https://pubmed.ncbi.nlm.nih.gov/38058737/)) describes a partial response in an NF2-associated ependymoma. |
| 3 | Rhabdoid tumor | 99.96% | L4 | [NCT03155620](https://clinicaltrials.gov/study/NCT03155620): NCI-COG Pediatric MATCH screening protocol (Phase 2, n=1377) with a selumetinib subprotocol, not specific to rhabdoid tumor. Preclinical ATRT work ([PMID 25638158](https://pubmed.ncbi.nlm.nih.gov/25638158/)) suggests MAPK pathway dependence. |

The other seven predictions (ranks 2, 4–8 and 10) are L5, model prediction only.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA213756 | KOSELUGO (AstraZeneca Pharmaceuticals LP) | Capsule |
| NDA219943 | KOSELUGO (AstraZeneca Pharmaceuticals LP) | Granule |

The source data lists each NDA twice and gives no approved-indication text.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, familial generalized lentiginosis, is supported only by the model score (L5). It has no trials, no literature, and no established mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Any disease-specific biological evidence linking familial generalized lentiginosis to MAPK signaling
- For the better-supported predictions, treat peripheral nerve schwannoma (L3) and rhabdoid tumor (L4) as separate research questions. Schwannoma has an early-terminated Phase 2 trial in NF2-related tumors and preclinical data. Rhabdoid tumor has preclinical MAPK evidence and indirect support from a pediatric umbrella trial.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

