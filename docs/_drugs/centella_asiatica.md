---
layout: default
title: Centella Asiatica
parent: Model Prediction Only (L5)
nav_order: 512
evidence_level: L5
indication_count: 3
---

# Centella Asiatica
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Centella Asiatica: From Topical Skin Products to Insomnia

## One-Sentence Summary

Centella asiatica is a botanical ingredient found in topical products (gels, creams, cleansers). The data compiled for this report show no approved indication text for these products.
The TxGNN model predicts it may be effective for **Insomnia**, but there are **0 clinical trials** and only **1 publication** (a zebrafish study) supporting this direction, so the prediction is purely hypothesis-level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified (no approved indication text on any of the listed products) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Centella asiatica is a traditional medicinal plant whose triterpenoid constituents (such as asiatic acid and madecassoside) are widely studied. Its known uses are mainly in skin and wound care, and none of the listed products carries an approved indication.

The only supporting evidence for insomnia is a 2024 zebrafish larvae study. It reported that an ethanol extract of Centella asiatica was associated with inhibition of orexin, ERK, Akt and p38 signalling in an insomnia model. Orexin is a key wake-promoting signal, so this is a plausible hypothesis. However, it has not been tested in mammals or humans, and the high TxGNN score is a computational prediction only.

Two related predictions appear in the data: a sleep initiation/maintenance disorder (score 99.03%) that rests on the same zebrafish study, and anxiety (score 99.08%). The anxiety prediction has more indirect support, including mouse studies, reviews, one small human study in generalised anxiety disorder, and work on GABA-A receptor modulation. However, one 2025 mouse study found that the triterpene and caffeoylquinic acid constituents did not account for the extract's anxiolytic effects. Extract composition also varies between preparations, which complicates standardisation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (insomnia):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Preclinical (zebrafish) | F1000Research | Ethanol extract of Centella asiatica studied in a zebrafish larvae insomnia model, linked to inhibition of orexin, ERK, Akt and p38 signalling |

Indirect evidence from the anxiety-related literature (a secondary prediction):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20677602](https://pubmed.ncbi.nlm.nih.gov/20677602/) | 2010 | Clinical study | Nepal Med Coll J | 33 participants with generalised anxiety disorder took 500 mg of a hydro-ethanolic extract twice daily |
| [26848139](https://pubmed.ncbi.nlm.nih.gov/26848139/) | 2016 | Preclinical (mouse) | Phytother Res | Extract protected against anxiety-like behaviour, oxidative damage and neuroinflammation after sleep deprivation, possibly via nitric oxide pathways |
| [38770167](https://pubmed.ncbi.nlm.nih.gov/38770167/) | 2024 | Preclinical (mouse) | Front Aging | Water extract improved age-related cognitive decline and anxiety; effects varied by sex, dose and mode of administration |
| [41097248](https://pubmed.ncbi.nlm.nih.gov/41097248/) | 2025 | Preclinical (mouse) | Nutrients | Triterpene and caffeoylquinic acid constituents contributed to cognitive enhancement but not to anxiolytic effects |
| [16488124](https://pubmed.ncbi.nlm.nih.gov/16488124/) | 2006 | Preclinical (rat) | Phytomedicine | Extracts and asiaticoside evaluated for anxiolytic properties in rat behavioural models |
| [27062315](https://pubmed.ncbi.nlm.nih.gov/27062315/) | 2016 | In vitro | Chem Biol Drug Des | Asiatic acid and madecassic acid showed selective negative modulation of GABA-A receptor subtypes |
| [40932246](https://pubmed.ncbi.nlm.nih.gov/40932246/) | 2025 | Review | Annals of Medicine | Review of neuroprotective, antioxidant and anti-inflammatory properties |
| [42391143](https://pubmed.ncbi.nlm.nih.gov/42391143/) | 2026 | Scoping review | Complement Med Res | Reviewed gotu kola in combination with phosphatidylcholine and taurine in mood disorders; Centella's own contribution is hard to isolate |
| [23653088](https://pubmed.ncbi.nlm.nih.gov/23653088/) | 2013 | Review | CNS Drugs | Narrative review of plant-based anxiolytics with clinical and preclinical evidence |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M014 | JAYSUING Silicone Scar Gel | Gel | Not specified (cancelled) |
| M020 | EELHOE Bio Sun Stick | Cream | Not specified (cancelled) |
| M016 | IntenseClarifyingCleanserRepairToner | Liquid | Not specified (cancelled) |
| Not available | MADECASSOL | Gel | Not specified (cancelled) |

All four authorizations are cancelled, and all listed products are topical or other non-oral forms. Route compatibility with an insomnia indication has not been assessed.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found, and no disease contraindications were identified from the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on a single zebrafish study, with no clinical trials and no mammalian or human data. The drug has no currently valid US authorization, no approved indication text, and no mechanism of action or label safety data. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- FDA package insert warnings and contraindications for safety screening
- Replication of the insomnia finding in mammalian sleep models
- Standardised, characterised extract and a suitable (likely oral) formulation, since all listed products are topical
- Controlled human studies, if preclinical results are confirmed
- Review of the anxiety indication as an alternative research question, given its broader (though mostly preclinical) support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

