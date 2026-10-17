---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
monitor_inn: "FLUOROURACIL"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome"]
last_modified_at: 2026-10-14
description: "Fluorouracil: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Superficial multifocal basal cell carcinoma, actinic keratosis…"
---

# Fluorouracil
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

# Fluorouracil: From Skin Conditions and Gastrointestinal Cancers to Rhabdomyosarcoma

## One-Sentence Summary

Fluorouracil is an antimetabolite chemotherapy drug, originally used for skin conditions (such as actinic keratosis and basal cell carcinoma) and gastrointestinal cancers (colon, pancreatic and gastric).
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina** (the top-ranked prediction), but **no clinical trials** and **no relevant literature** currently support this specific prediction.
The broader rhabdomyosarcoma prediction is supported only by a few old reviews and a single case report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial multifocal basal cell carcinoma, actinic keratosis, gastric cancer, colorectal metastasis, pancreatic adenocarcinoma (from the knowledge graph; the US label text was not available in the data compiled for this report) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licences are cancelled) |
| Number of NDAs | 12 (1 NDA and 11 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, fluorouracil inhibits thymidylate synthase and is incorporated into RNA and DNA, which makes it cytotoxic to rapidly dividing cells. Its efficacy in gastrointestinal cancers and in skin lesions is well established.

The link to rhabdomyosarcoma is weak. It rests on the general idea that an antimetabolite may act against proliferating sarcoma cells. Standard rhabdomyosarcoma regimens (such as VAC/VDC-based) do not include fluorouracil, so the prediction is not backed by current clinical practice. The model's graph-based prediction may partly reflect fluorouracil's use in related tumours such as biliary tract carcinoma, but that is a different histology.

The same pattern applies to the other top-ranked predictions. These are rhabdomyosarcoma subtypes (parameningeal, prostate and extrahepatic bile duct), liver sarcoma, and three sickle cell disease syndromes. The sickle cell predictions are speculative, since they would depend on fetal haemoglobin induction by cytotoxic agents, and fluorouracil's toxicity is unfavourable in a chronic non-malignant disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked prediction (vaginal botryoid-type rhabdomyosarcoma). The closest available evidence is for the broader "rhabdomyosarcoma" prediction (rank 2):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Adjuvant chemotherapy for childhood sarcomas, about half of which are rhabdomyosarcomas; no fluorouracil-specific evidence is evident in the excerpt |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | General overview of curable cancers with chemotherapy, including childhood rhabdomyosarcoma |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Rep Oncol Med | Adult lingual rhabdomyosarcoma; cisplatin plus 5-fluorouracil was followed by disease progression, and a later vincristine/actinomycin D-based regimen was used |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | Childhood nasopharyngeal carcinoma outcomes; not specific to rhabdomyosarcoma |

These sources are old, indirect or anecdotal. The only recent report (2026) describes progression on a fluorouracil-containing regimen, so it does not support efficacy.

## US Market Information

All 12 licences are cancelled and none is currently valid. The approved indication text was not available in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217295 | Fluorouracil | Injection, solution | Alembic Pharmaceuticals Limited |
| ANDA210124 | Fluorouracil | Injection, solution | Xiromed LLC |
| ANDA040278 | Fluorouracil | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA090368 | Fluorouracil | Cream | Northstar Rx LLC |
| NDA022259 | TOLAK | Cream | Hill Dermaceuticals, Inc. |

Seven further cancelled ANDAs exist (injection, solution, cream and topical solution forms). Fluorouracil has both injectable and topical (cream) formulations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high for systemic use. The knowledge graph lists neutropenia, leukopenia, thrombocytopenia and agranulocytosis as contraindication-linked conditions |
| Emetogenicity Classification | Low to moderate (by drug class) |
| Monitoring Items | CBC with differential, liver and renal function, and DPD deficiency considerations |
| Handling Protection | Follow cytotoxic drug handling regulations for injectable formulations |

Please refer to the package insert warnings and precautions for full details.

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. The knowledge graph links fluorouracil to the following conditions as contraindications (these come from graph edges, not label text):

- **Haematological:** thrombocytopenia, neutropenia, agranulocytosis, leukopenia
- **Organ disease:** kidney disease, liver disease, gallbladder disease
- **Gastrointestinal and mucosal:** diarrhoeal disease, active peptic ulcer disease, stomatitis, pharyngitis, pyoureter
- **Genetic:** dihydropyrimidine dehydrogenase (DPD) deficiency

**Drug interactions:** 100 interactions were identified. The main ones with a stated severity are:
- **Moderate:** metronidazole, tinidazole
- **Minor:** cimetidine, levofloxacin

Many other interactions have an unknown severity level (for example calcitriol, doxycycline, pantoprazole, omeprazole, metformin, morphine and triamcinolone).

Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.75%), but the evidence is at the model-prediction-only level (L5). There are no clinical trials and no relevant literature for the top-ranked indication. Fluorouracil is not part of standard rhabdomyosarcoma regimens, and all US licences are currently cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic search for fluorouracil use in rhabdomyosarcoma, including preclinical data and pediatric oncology protocols
- A comparison against current standard-of-care regimens, to show a plausible added benefit
- A route and formulation assessment (injectable versus topical), since this has not yet been evaluated
- A DPD deficiency screening plan and a haematological monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

