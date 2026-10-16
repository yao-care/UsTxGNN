---
layout: default
title: Cabergoline
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 5
monitor_inn: "CABERGOLINE"
predicted_indications: ["pituitary adenocarcinoma (disease)", "progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma"]
---

# Cabergoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Cabergoline: From Hyperprolactinemia to Pituitary Cancer

## One-Sentence Summary

Cabergoline is a dopamine D2 receptor agonist, originally used to treat hyperprolactinemia and prolactin-producing pituitary tumors.
The TxGNN model predicts it may be effective for **pituitary cancer**, with **12 clinical trials** and **21 publications** compiled for this direction.
Most of this evidence concerns benign pituitary adenomas rather than true pituitary carcinoma, so the evidence for the predicted indication itself is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinemia; prolactin-producing pituitary tumor (the US license records contain no indication text) |
| Predicted New Indication | Pituitary cancer (the top-ranked prediction, pituitary adenocarcinoma, has only case-report support, so the third-ranked prediction with the most evidence is evaluated here) |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L1 on paper (adenoma-level evidence only; not directly applicable to carcinoma) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 6 (1 NDA, 5 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cabergoline is a D2 dopamine receptor agonist. It suppresses prolactin secretion and shrinks prolactin-secreting pituitary adenomas.

D2 receptors are also expressed in corticotroph, somatotroph, and some nonfunctioning pituitary tumors. This gives a biological basis for using dopaminergic suppression of hormone secretion and tumor growth beyond prolactinoma. Preclinical work also suggests cabergoline has direct antitumor effects, and HTR2B inhibition may sensitize nonfunctioning adenomas to it.

There is an important limitation. The clinical evidence applies mainly to **benign pituitary adenomas** (nonfunctioning adenoma, Cushing disease), not metastatic pituitary carcinoma. Pituitary carcinoma is rare and usually refractory to dopamine agonists. The L1 grade therefore should not be extrapolated to carcinoma. Prolactinoma is already an original indication, so only the nonfunctioning and corticotroph adenoma uses are truly repurposed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | Not reported | Cabergoline for Cushing disease from corticotroph pituitary adenoma; results not provided |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Randomized open-label trial of cabergoline in residual nonfunctioning adenoma after transsphenoidal surgery; results not provided |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Randomized trial of dopamine agonist in nonfunctioning pituitary adenomas |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in nonfunctioning adenomas and resistant prolactinomas, with in vitro and in vivo responses |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline vs no treatment for 48 weeks in nonfunctioning adenoma; tumor size outcome |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Single-arm study of octreotide plus cabergoline in partially responsive acromegaly |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or with cabergoline in Cushing disease |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Phase 3 | Recruiting | 70 | High-dose vs standard-dose cabergoline in microprolactinoma (original indication; dosing and safety) |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | Recruiting | 60 | Glucose metabolism under dopamine agonist therapy in prolactinoma |
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | N/A | Completed | 50 | Observational study of cardiac abnormalities and valve regurgitation in prolactinoma patients on long-term cabergoline |

No registered trial addresses true pituitary carcinoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Diagnosis and management of pituitary adenomas |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Review | Lancet Diabetes Endocrinol | Pathogenesis, diagnosis, and management of prolactin-secreting adenomas |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Approach to the patient with prolactinoma |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | New antitumor mechanisms of cabergoline and potential broader applications |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Preclinical | Neuro-oncology | Targeting HTR2B suppresses nonfunctioning adenoma growth and sensitizes it to cabergoline |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Review | Pituitary | Cabergoline in acromegaly |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline in pituitary tumors and valvular disorders; most studies show no significant increase in valvulopathy |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | Medicina (Kaunas) | Treatment of prolactinoma, including aggressive prolactinomas |
| [34034260](https://pubmed.ncbi.nlm.nih.gov/34034260/) | 2022 | Review | Neuroendocrinology | MicroRNAs in dopamine agonist-resistant prolactinoma (about 10% resistance with cabergoline) |
| [41781297](https://pubmed.ncbi.nlm.nih.gov/41781297/) | 2026 | Review | Best Pract Res Clin Endocrinol Metab | Surgery for prolactinoma; notes psychiatric adverse reactions to dopamine agonists |

The literature found is reviews and preclinical work. No randomized trial publication was retrieved.

---

## US Market Information

All six US licenses are oral tablets and are currently cancelled. No indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020664 | Cabergoline | Tablet | Mylan Pharmaceuticals Inc. |
| ANDA076310 | Cabergoline | Tablet | Strides Pharma Science Limited |
| ANDA077750 | Cabergoline | Tablet | Teva Pharmaceuticals USA, Inc. |
| ANDA204735 | Cabergoline | Tablet | A-S Medication Solutions |
| ANDA218109 | Cabergoline | Tablet | Somerset Therapeutics, LLC |

One further license (ANDA218618, Amneal Pharmaceuticals NY LLC) is also cancelled, making six in total.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindication signals (not label text)**: liver disease, gallbladder disease, heart valve disease, pulmonary fibrosis (including postinflammatory), IgG4-related retroperitoneal fibrosis, and preeclampsia (including severe).
- **Valvulopathy**: Cardiac valve damage has been reported with ergot-derived dopamine agonists. Evidence in pituitary tumor patients is mixed, but most studies show no significant increase in risk.
- **Eye safety**: A case report links cabergoline to bilateral angle-closure glaucoma.
- **Drug interactions** (60 recorded; main ones shown):
  - **Major**: lorcaserin, clarithromycin
  - **Moderate**: metoclopramide
  - The remaining interactions are of unknown severity (for example calcitriol, proton pump inhibitors, metformin, and corticosteroids).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99%), and completed Phase 3 trials exist in nonfunctioning and corticotroph adenomas. However, their results are not provided, and no evidence addresses true pituitary carcinoma, which is typically refractory to dopamine agonists. Other top predictions are weaker: pituitary adenocarcinoma has only case reports, and progeria-short stature-pigmented nevi syndrome and spastic quadriplegic cerebral palsy have no evidence. Glaucoma carries a safety signal (angle closure). All US licenses are also cancelled.

**To proceed, the following is needed:**
- Published results from NCT00889525, NCT03271918, and NCT02288962
- Clarify the target indication: benign adenoma (nonfunctioning or corticotroph) versus true pituitary carcinoma
- Package insert warnings and contraindications
- Mechanism of action data
- Current US marketing status and a supply pathway, since all licenses are cancelled
- A safety monitoring plan for heart valve and fibrotic risks in long-term use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

