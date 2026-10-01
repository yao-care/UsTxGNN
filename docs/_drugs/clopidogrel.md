---
layout: default
title: Clopidogrel
parent: Model Prediction Only (L5)
nav_order: 542
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Clopidogrel: From Cardiovascular Thrombotic Events to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is an oral P2Y12 platelet inhibitor used to prevent blood-clot-related cardiovascular events. This general use comes from background knowledge, because the US license records retrieved contain no indication text.
The TxGNN model predicts it may help **migraine with brainstem aura** (score 99.4%). No clinical trial is registered for this specific subtype, and the 16 retrieved publications are mostly about migraine with aura in general or PFO-associated migraine.
The stronger evidence is for the broader condition, **migraine disorder**, where a completed Phase 4 RCT and several observational studies exist.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the retrieved US license records (background knowledge: antiplatelet therapy for thrombotic cardiovascular events) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 (observational studies and a systematic review; no subtype-specific trial) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all retrieved records are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available. Based on general pharmacology, clopidogrel blocks the platelet P2Y12 receptor and reduces platelet activation.

The working hypothesis is that platelet activation and small paradoxical emboli crossing a right-to-left shunt, such as a patent foramen ovale (PFO), can trigger aura. Platelet-derived serotonin release may also contribute. Several reports describe migraine appearing or worsening after septal-defect closure and improving with clopidogrel.

This reasoning applies to migraine with aura and PFO-associated migraine in general. None of the retrieved clopidogrel data is specific to the brainstem-aura subtype, so the prediction is an extrapolation. The very high TxGNN score is a model output, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials are registered for migraine with brainstem aura specifically.

The parent condition, migraine disorder, has the trials below. They are shown as indirect evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA: clopidogrel added to aspirin to prevent new-onset migraine after transcatheter ASD closure |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Clopidogrel as migraine prophylaxis in patients with right-to-left shunt |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1000 | COMPETE: anticoagulant vs antiplatelet vs standard migraine therapy in PFO-associated migraine (clopidogrel is one arm) |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING: PFO closure vs medication for migraine (clopidogrel is not the tested intervention) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Pilot randomised trial of clopidogrel as migraine prophylaxis; the retrieved abstract does not give results |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT (indirect) | European Heart Journal | PRIMA: PFO closure in medically refractory migraine with aura (device trial, not clopidogrel) |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic review | Headache | Reviews the role of antithrombotic drugs in migraine prevention |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | J Investig Med | Clopidogrel 75 mg/day added for 3 and 6 months in drug-refractory migraine; PFO found in 56.8% of those tested |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective review | Cephalalgia | Clopidogrel as primary therapy in migraineurs with right-to-left shunt |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine therapy in migraine with PFO |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after transcatheter PFO/ASD closure |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | TRACTOR: ticagrelor (not clopidogrel) in refractory migraine with PFO |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case series | J Interv Cardiol | Severe migraine in 5 of 13 patients after ASD closure; relief after 300 mg clopidogrel |
| [33815258](https://pubmed.ncbi.nlm.nih.gov/33815258/) | 2021 | Case report | Frontiers in Neurology | Migraine-like headache with visual aura after coiling of a posterior cerebral artery aneurysm (no clopidogrel data) |

For the broader migraine indication, the CANOA RCT ([26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/), JAMA 2015; 1-year follow-up [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/), JAMA Cardiology 2021) tests clopidogrel plus aspirin against aspirin alone after ASD closure. The retrieved abstracts do not state the primary outcome, so it must be checked before drawing conclusions.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202928 | Clopidogrel (Macleods Pharmaceuticals) | Tablet | Not stated in record |
| ANDA213351 | Clopidogrel (Polygen Pharmaceuticals) | Tablet | Not stated in record |
| ANDA090540 | Clopidogrel (Legacy Pharmaceutical Packaging) | Tablet, film coated | Not stated in record |
| ANDA090540 | Clopidogrel (RemedyRepack) | Tablet, film coated | Not stated in record |
| ANDA076274 | Clopidogrel (American Health Packaging) | Tablet, film coated | Not stated in record |

Only 5 of the 20 authorizations are listed. All are oral products.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is indirect: no trial or publication tests clopidogrel in migraine with brainstem aura. The data that exist concern migraine with aura or PFO-associated migraine, and results across studies are mixed and limited to specific subgroups. The safety review is also blocked because the package insert data is missing.

The other predicted indications (osteoarthritis, tendinitis, granulomatous myositis, myositis fibrosa, rheumatoid arthritis, osteoarthritis susceptibility) have no supporting evidence and should also be held.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (this data gap blocks safety screening)
- DrugBank mechanism-of-action data
- Verification of the primary outcomes of the CANOA RCT and the pilot RCT (PMID 24836213)
- Review of NCT02938182 and NCT05546320 (COMPETE) results, both currently marked "Unknown"
- Evidence for the brainstem-aura subtype specifically, or a decision to pursue the broader migraine-with-aura/PFO question instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

