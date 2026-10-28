---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 1049
evidence_level: L5
indication_count: 10
monitor_inn: "PIRFENIDONE"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
last_modified_at: 2026-10-14
description: "Pirfenidone: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Idiopathic pulmonary fibrosis (also acute interstitial pneumonia and…"
---

# Pirfenidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma
{: .text-alpha }

## One-Sentence Summary

Pirfenidone is an anti-fibrotic drug, originally used to treat idiopathic pulmonary fibrosis and related interstitial pneumonias.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**,
but **no clinical trials** and **no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (also acute interstitial pneumonia and idiopathic interstitial pneumonia) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 11) |
| Number of NDAs | 11 (1 NDA and 10 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pirfenidone is generally described as an anti-fibrotic and anti-inflammatory agent that modulates TGF-beta signaling. Its efficacy in idiopathic pulmonary fibrosis is established.

For extracutaneous mastocytoma, however, no direct mechanistic link is supported. Mast cell neoplasms are typically driven by KIT mutations, and pirfenidone's anti-fibrotic activity does not target that pathway. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be treated as a hypothesis, not as evidence of efficacy.

**Other top-ranked predictions** (all L5 or L4, none supported by trials):

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Dermatofibrosarcoma protuberans | 0.9941 | L5 | Plausible but unvalidated link via PDGF/TGF-beta signaling in fibroblasts |
| 3 | Aggressive systemic mastocytosis | 0.9933 | L5 | KIT-driven; no supported mechanism |
| 4 | Heart fibrosarcoma | 0.9929 | L5 | Nominal fibroblast-lineage association only |
| 5 | Conventional fibrosarcoma | 0.9926 | L5 | Anti-fibrotic effect does not imply anti-tumor activity |
| 6 | Autosomal recessive familial Mediterranean fever | 0.9925 | L5 | Conceivable link via anti-inflammatory effects (TNF-alpha, IL-1beta) |
| 7 | Kidney fibrosarcoma | 0.9924 | L5 | Same rationale as other fibrosarcomas |
| 8 | Hepatic infarction | 0.9924 | L5 | Ischemic event; only preclinical liver fibrosis data |
| 9 | Fibroblastic neoplasm | 0.9923 | L5 | Only indirect in vitro evidence, plus safety signals |
| 10 | Low grade fibromyxoid sarcoma | 0.9919 | L5 | Nominal fibroblastic-lineage association only |

## Clinical Trial Evidence

Currently no related clinical trials registered for extracutaneous mastocytoma.

## Literature Evidence

Currently no related literature available for extracutaneous mastocytoma.

For reference, the closest-ranked prediction with literature is *fibroblastic neoplasm* (rank 9). Its publications are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot clinical study | Am J Gastroenterol | Pilot project testing pirfenidone, a noncytotoxic oral anti-fibrotic, in desmoid tumors of familial adenomatous polyposis. No efficacy conclusion is evident from the available text |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro study | BMC Musculoskelet Disord | Pirfenidone inhibited TGF-β1-mediated activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro study | BMC Musculoskelet Disord | Examined pirfenidone's effect on TGF-β1-stimulated non-SMAD signaling in Dupuytren's fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical/Review | Pharm Dev Technol | Explores pirfenidone as a locally injected anti-fibrotic for Dupuytren's disease |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Perm J | Undifferentiated pleomorphic sarcoma reported after pirfenidone use (safety signal) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis (safety signal) |

## US Market Information

The drug is marketed in the US, with 11 valid licenses. Approved indication text is not available for these records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA208780 | ESBRIET | Tablet, coated | Legacy Pharma USA Inc. |
| ANDA212722 | Pirfenidone | Tablet, film coated | Laurus Labs Limited |
| ANDA212709 | Pirfenidone | Tablet | Apotex Corp. |
| ANDA212708 | Pirfenidone | Tablet, coated | Alembic Pharmaceuticals Inc. |
| ANDA212570 | Pirfenidone | Tablet, film coated | Amneal Pharmaceuticals NY LLC |

Other cancelled licenses include generic tablets and capsules from Cipla, ScieGen, Laurus, Sandoz, Teva and Amneal. All dosage forms are oral.

## Safety Considerations

Label-based warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Drug Interactions**: 100 interactions were identified, and the main ones listed are all of Moderate severity. Examples include:
  - Bupropion
  - Omeprazole
  - Esomeprazole
  - Lansoprazole
  - Cimetidine
  - Eliglustat
  - Obeticholic acid
  - Naltrexone
  - Miconazole
  - Disulfiram
  - Ticlopidine
  - Ivacaftor
- **Literature safety signals**: Case reports describe undifferentiated pleomorphic sarcoma after pirfenidone use and aggravation of eruptive dermatofibromas. These are anecdotal but argue for caution in any fibroblast-lineage neoplasm setting.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for extracutaneous mastocytoma is supported only by a TxGNN model (deep learning) score (L5), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications, and no plausible mechanistic link: mast cell neoplasms are typically KIT-driven, which pirfenidone does not target. The drug is marketed in the US, with 11 valid licenses.

**To proceed, the following is needed:**
- Mechanism of action data for pirfenidone, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications, which are required before any safety screening
- Preclinical evidence (for example, mast cell line or KIT-mutant model data) showing any activity in mast cell neoplasia
- Review of alternative candidates among the top predictions (such as dermatofibrosarcoma protuberans or fibroblastic neoplasm), which have somewhat more plausible fibroblast-related rationale, while weighing the reported sarcoma and dermatofibroma safety signals
- Clarification of the cancelled US license status if a US development path is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

