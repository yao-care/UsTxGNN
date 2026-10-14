---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 533
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog originally used to treat hairy cell leukemia and relapsing-remitting multiple sclerosis.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**,
but **no clinical trials** and **no directly relevant publications** currently support this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy cell leukemia; relapsing-remitting multiple sclerosis (the US license records contain no indication text) |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 5 (4 ANDAs and 1 NDA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cladribine is an adenosine deaminase-resistant purine nucleoside analog. It is incorporated into DNA and induces apoptosis, mainly in lymphocytes and monocytes that have high deoxycytidine kinase activity. This explains its efficacy in hairy cell leukemia and its use in multiple sclerosis.

Rhabdomyosarcoma is a solid tumor of mesenchymal origin, and it has no established dependence on this pathway. The very high score (0.998) appears to come from the structure of the knowledge graph rather than a specific mechanism. Seven rhabdomyosarcoma-related entries (several subtypes and the parent class) have nearly identical scores (0.997-0.998), which suggests the score is inherited across the disease class. The mechanistic link is therefore weak and unvalidated.

Other predictions in the same set are similar: botryoid-type embryonal rhabdomyosarcoma of the vagina, embryonal extrahepatic bile duct rhabdomyosarcoma, prostate embryonal rhabdomyosarcoma, extrahepatic bile duct rhabdomyosarcoma, rhabdomyosarcoma (disease) and liver sarcoma. None has clinical trial support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication.

For reference, the only publication linked to the broader prediction set is [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) (2004, case report, Der Hautarzt). It describes successful cladribine therapy in smoldering systemic mastocytosis. It was matched to the "liver sarcoma" prediction, not to rhabdomyosarcoma, and it concerns a mast cell neoplasm, so it is not evidence for the predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA210856 (Hisun Pharmaceuticals USA) | Cladribine | Injection, solution | Not available (cancelled) |
| ANDA218425 (Genvion Corporation) | Cladribine | Tablet | Not available (cancelled) |
| ANDA076571 (Fresenius Kabi USA) | Cladribine | Injection | Not available (cancelled) |
| ANDA075405 (Hikma Pharmaceuticals USA) | Cladribine | Injection | Not available (cancelled) |
| NDA022561 (EMD Serono) | Mavenclad | Tablet | Not available (cancelled) |

All five authorizations are listed as cancelled in the data compiled for this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | High. The knowledge graph lists neutropenia, agranulocytosis, thrombocytopenia and anemia as contraindicated conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function, uric acid, and neurological assessment (peripheral neuropathy) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindicated or high-risk conditions (from knowledge graph relationships, not label text)**: kidney disease, pyoureter, thrombocytopenia, hyperuricemia, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, anemia, macrocytic anemia.
- **Drug Interactions**: 100 interactions were identified. The main ones are:
  - **Major**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone); deferiprone; radiopharmaceuticals (ibritumomab tiuxetan, iobenguane I-131, tositumomab and tositumomab I-131, samarium-153 lexidronam, strontium-89 chloride).
  - **Moderate**: palifermin, dipyridamole, cilostazol, eltrombopag.
  - **Unknown level**: acetylsalicylic acid.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on the model score alone (Evidence Level L5). There are no clinical trials and no relevant publications. The mechanism does not clearly fit rhabdomyosarcoma, the score looks inherited from the disease class, and the drug has substantial myelosuppressive and neurotoxic risks. All US licenses are also cancelled.

**To proceed, the following is needed:**
- Preclinical validation, such as cell-line sensitivity testing in rhabdomyosarcoma models and deoxycytidine kinase expression analysis
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications, to allow safety screening
- A review of whether the liver sarcoma literature match is an indexing artifact
- Route-of-administration compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

