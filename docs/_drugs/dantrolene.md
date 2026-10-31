---
layout: default
title: Dantrolene
parent: Model Prediction Only (L5)
nav_order: 568
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
monitor_inn: "DANTROLENE"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
description: "Dantrolene: predicted new indication Moderate multiminicore disease with hand involvement (evidence level L5). Approved use: Not recorded in the local data"
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Dantrolene: Moderate multiminicore disease with hand involvement
{: .text-alpha }

## One-Sentence Summary

Dantrolene was originally used to treat malignant hyperthermia during anaesthesia, including the exercise-induced form.
This is essentially an on-label use rather than a true repurposing; the other predicted diseases (RYR1-related myopathies, periodic paralyses) have much weaker support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Moderate multiminicore disease with hand involvement |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of FDA Applications | at least 7 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the compiled data. Based on the literature supplied, dantrolene inhibits RyR1-mediated calcium release from the sarcoplasmic reticulum in skeletal muscle. A 2017 PNAS study (PMID 28373535) further reports that dantrolene requires Mg2+ to arrest malignant hyperthermia.

Malignant hyperthermia susceptibility is caused mainly by gain-of-function variants in the RYR1 gene, which lead to uncontrolled calcium release in muscle after exposure to volatile anaesthetics or succinylcholine. Dantrolene therefore acts directly on the underlying pathophysiology. Consensus guidelines (Association of Anaesthetists 2020; European Malignant Hyperthermia Group 2021) support its role.

The predicted indication is closely related to the original indication, and the evidence base is guidelines, reviews and long-standing clinical practice rather than registered trials. The prediction is therefore reasonable, but it largely restates the existing use.

**Other predicted diseases (summary):**

| Predicted Disease | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Moderate multiminicore disease with hand involvement | 0.9990 | L5 | RYR1 link plausible; no trials or literature. Hold |
| King-Denborough syndrome | 0.9987 | L4 | Case-level evidence; benefit would be for MH risk, not the myopathy. Research question |
| Congenital multicore myopathy with external ophthalmoplegia | 0.9987 | L5 | Only a genetic study; no efficacy evidence. Hold |
| Central core myopathy | 0.9986 | L5 | Mechanistic and review-level evidence; relates to MH prophylaxis. Research question |
| Hypokalemic periodic paralysis | 0.9978 | L5 | Indirect link; no evidence. Hold |
| Thyrotoxic periodic paralysis | 0.9967 | L5 | Speculative; no evidence. Hold |
| Centronuclear myopathy | 0.9966 | L5 | Indirect evidence incl. a prophylactic-use case report in central core disease. Research question |

## Clinical Trial Evidence

Currently no related clinical trials registered. The published guidelines note that, because of the rarity of the condition and ethical limits, there is no interventional trial evidence to guide perioperative management.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists guideline on malignant hyperthermia (2020) |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Guideline | Br J Anaesth | European consensus on perioperative management of MH-suspected or susceptible patients; notes no interventional trial evidence |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | MH is a pharmacogenetic skeletal muscle disorder; incidence 1:10,000 to 1:250,000 anaesthetics |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative review of epidemiology and management of critically ill MH patients |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | MH update; mortality has improved |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Review | Korean J Anesthesiol | Autosomal dominant inheritance with variable expression and incomplete penetrance |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | Dantrolene sodium described as the ultimate treatment for MH |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic study | PNAS | Dantrolene requires Mg2+ to arrest MH |
| [31166228](https://pubmed.ncbi.nlm.nih.gov/31166228/) | 2019 | Position statement | Anesth Analg | MH-susceptible adults can be safely treated in ambulatory surgery centres with proper precautions |
| [25989378](https://pubmed.ncbi.nlm.nih.gov/25989378/) | 2015 | Review | Acta Anaesthesiol Scand | Scandinavian update; RYR1 mutations in most cases |

## US Market Information


| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018264 | Dantrium | Injection | Not available |
| NDA205579 | RYANODEX | Injection, suspension | Not available |
| NDA017443 | Dantrolene sodium | Capsule | Not available |
| ANDA078378 | Revonto | Injection, powder, lyophilized, for solution | Not available |
| ANDA204762 | Dantrolene | Injection, powder, for solution | Not available |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, lung disease and an obsolete rare pulmonary disease are flagged as contraindication-related conditions. These need confirmation against the package insert.
- **Drug Interactions**: 72 interactions were identified in total. Major interactions include **morphine** and **liposomal morphine**. Moderate interactions include dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol and promethazine. Several others (e.g. omeprazole, metformin, simvastatin, clopidogrel) have an unclassified severity.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For malignant hyperthermia susceptibility, dantrolene directly targets the disease mechanism and is recommended in consensus guidelines. The L3 level reflects the absence of registered Phase 3 RCTs, not weak clinical support. The remaining predictions (RYR1 myopathies and periodic paralyses) rest on indirect or no clinical evidence and should be treated as research questions or held.

**To proceed, the following is needed:**
- Obtain the package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism-of-action data from DrugBank
- Review the major morphine interaction and the liver, muscle and lung cautions
- For RYR1 myopathies, define whether the goal is MH prophylaxis or disease treatment before any further study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

