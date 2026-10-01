---
layout: default
title: Dantrolene
parent: Moderate Evidence (L3-L4)
nav_order: 568
evidence_level: L3
indication_count: 9
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

# Dantrolene: From Muscle Relaxant to Malignant Hyperthermia (Probably an Already-Labeled Use)

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant. The submitted data do not list its original indications.
The TxGNN model predicts it may be effective for **malignant hyperthermia, susceptibility to**, with **0 registered clinical trials** and **18 publications** (guidelines, reviews and mechanistic papers). This is probably a use dantrolene already has on its label, not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hyperthermia, susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

The US license records provided contain no approved-indication text, so the original indication cannot be confirmed from this data.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the submitted record. The mechanistic link comes from the analysis of the prediction and the literature. Dantrolene inhibits RyR1-mediated calcium release from the sarcoplasmic reticulum. This counters the uncontrolled Ca²⁺ release that drives a malignant hyperthermia (MH) crisis. A 2017 PNAS study (PMID 28373535) reports that dantrolene is given to relieve MH symptoms and that it needs Mg²⁺ to arrest MH.

The 2020 Association of Anaesthetists guideline lists dantrolene as first-line treatment for MH. The prediction therefore matches established standard of care. MH is a rare, life-threatening pharmacogenetic skeletal muscle disorder. It is triggered by volatile anesthetics or succinylcholine, mainly through RYR1 mutations.

No trials are registered and no RCTs exist, and none are expected. A placebo-controlled trial of a life-saving treatment would be unethical. The evidence is guidelines, reviews and historical clinical experience, so it is graded L3 rather than L1. Because the original indication is missing from the data, this may be a labeled use that should be checked against the current label before it is reported as a repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists 2020 MH guideline. Defines MH as a life-threatening hypermetabolic reaction in genetically susceptible people exposed to inhalational anaesthetics or suxamethonium. |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Consensus guideline | Br J Anaesth | European MH Group consensus on perioperative management of suspected or susceptible patients. It notes that no interventional trial evidence exists because MH is rare and trials raise ethical limits. |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic | PNAS | Dantrolene is given to relieve MH symptoms. The study examines its mechanism and finds it requires Mg²⁺ to arrest MH. |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative expert review of the epidemiology and management of critically ill MH patients. |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | MH incidence is 1:10,000 to 1:250,000 anesthetics. Prevalence of the genetic abnormalities may be far higher. |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | Update on MH as a skeletal muscle calcium-release channel disorder. Late diagnosis leads to multi-organ failure and death. |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | Describes dantrolene sodium as the ultimate treatment for MH and lists precautions for susceptible patients. |
| [33863282](https://pubmed.ncbi.nlm.nih.gov/33863282/) | 2021 | Clinical study | BMC Anesthesiol | Looks at MH characteristics where dantrolene is not readily available, for example in China. |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet J Rare Dis | Earlier overview of MH as a pharmacogenetic skeletal muscle disorder. |
| [40597248](https://pubmed.ncbi.nlm.nih.gov/40597248/) | 2025 | Bibliometric analysis | Orphanet J Rare Dis | Maps MH research trends from 1975 to 2024 and gives recommendations for reducing mortality. |

---

## US Market Information

The 5 main authorizations are listed below. None of the records include approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA204762 | Dantrolene | Injection, powder, for solution | Hikma Pharmaceuticals USA Inc. |
| NDA017443 | Dantrolene sodium | Capsule | Bryant Ranch Prepack |
| ANDA076686 | Dantrolene Sodium | Capsule | Elite Laboratories, Inc. |
| ANDA076856 | Dantrolene Sodium | Capsule | Amneal Pharmaceuticals of New York LLC |
| ANDA078378 | Revonto | Injection, powder, lyophilized, for solution | ProPharma Distribution |

Both injectable and oral (capsule) forms are marketed.

---

## Safety Considerations

Please refer to the package insert for safety information. A search of the drug-interaction database returned no entries for dantrolene.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dantrolene's RyR1-blocking mechanism directly matches the cause of MH, and guidelines list it as first-line treatment. The evidence is guidelines, reviews and clinical experience with no registered trials, so it is L3. It is probably a labeled use and not a true new indication.

**To proceed, the following is needed:**
- Confirm the current US label and approved indications, since original indications are missing from the data. This settles whether MH is repurposing or an existing use.
- Obtain the package insert warnings and contraindications. This is a blocking gap for safety screening.
- Obtain detailed mechanism-of-action data from DrugBank.

**Other predictions (not recommended for action):**
The other predicted indications are RYR1-related or muscle ion-channel conditions. These include King-Denborough syndrome, central core myopathy, centronuclear myopathy, multiminicore disease, hypokalemic periodic paralysis and thyrotoxic periodic paralysis. None has trial data or evidence that dantrolene treats the underlying disease. The literature only supports its relevance to MH risk in RYR1-related patients. King-Denborough syndrome and central core myopathy are worth investigating as research questions. The rest stay on hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

