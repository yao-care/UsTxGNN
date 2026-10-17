---
layout: default
title: Tolvaptan
parent: Model Prediction Only (L5)
nav_order: 1241
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tolvaptan: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Inappropriate ADH syndrome"
monitor_inn: "TOLVAPTAN"
predicted_indications: ["renal-hepatic-pancreatic dysplasia", "karyomegalic interstitial nephritis", "thoracic malformation", "Joubert syndrome with renal defect", "adult familial nephronophthisis-spastic quadriparesia syndrome", "Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Tolvaptan
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

# Tolvaptan: From Inappropriate ADH Syndrome to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

Tolvaptan was originally used for conditions of excess antidiuretic hormone (SIADH and nephrogenic syndrome of inappropriate antidiuresis) and for polycystic kidney disease.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**,
with **0 registered clinical trials** and **20 publications** (including 2 RCTs and 1 Cochrane systematic review on ADPKD) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inappropriate ADH syndrome; nephrogenic syndrome of inappropriate antidiuresis; polycystic kidney disease (the data compiled for this report contain no approved-indication text from the US labels) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (based on the pivotal ADPKD RCTs; see note below) |
| US Market Status | Cancelled only (all licences listed as cancelled) |
| Number of NDAs | 8 licences in total (2 NDAs and 6 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The RCTs (TEMPO 3:4 and REPRISE) were conducted in ADPKD generally, not in the GANAB-associated PKD3 form. No clinical trials specific to the predicted indication are registered, so the L1 rating applies to the closely related parent disease, and the direct evidence for PKD3 is weaker.

## Why is This Prediction Reasonable?

Tolvaptan is a selective vasopressin V2 receptor antagonist. In polycystic kidney disease, vasopressin-driven cAMP signalling promotes cyst cell proliferation and fluid secretion. Blocking the V2 receptor lowers cAMP and slows cyst growth and the loss of kidney function. This is already the established mechanism in ADPKD (PKD1/PKD2). Detailed mechanism-of-action data from DrugBank were not available for this report, so this explanation relies on the published literature.

The PKD3 form (GANAB-associated, with or without polycystic liver disease) is a related genetic condition that converges on the same cystogenic pathway, so the link is plausible. However, it has not been proven specifically for GANAB variants. A review in the literature set also notes that polycystic liver disease is the most common extrarenal manifestation of ADPKD, and that tolvaptan can slow the deterioration of renal function and cyst growth.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | Tolvaptan in ADPKD (TEMPO 3:4); V2 antagonism slowed total kidney volume growth and kidney function decline |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | Tolvaptan in later-stage ADPKD; the earlier trial had shown more aminotransferase and bilirubin elevations |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review | Cochrane Database Syst Rev | Interventions for preventing progression of ADPKD |
| [41771281](https://pubmed.ncbi.nlm.nih.gov/41771281/) | 2026 | Review | Lancet | Strong evidence base for tolvaptan as disease-modifying treatment, supporting early use in patients at high risk of kidney failure |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic kidney/liver disease; tolvaptan can slow renal function decline and cyst growth |
| [40268755](https://pubmed.ncbi.nlm.nih.gov/40268755/) | 2025 | Review | Renal Failure | Overview of recent genetic and clinical advances in ADPKD |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Tolvaptan remains the only FDA-approved therapy targeting disease progression; new therapies are in the pipeline |
| [40844441](https://pubmed.ncbi.nlm.nih.gov/40844441/) | 2025 | Review | Am J Kidney Dis | Core curriculum; disease-modifying therapy recommended for patients at high risk of progression |
| [32392574](https://pubmed.ncbi.nlm.nih.gov/32392574/) | 2021 | Review | Pediatr Res | Tolvaptan use in adolescents and young adults with rapidly progressing ADPKD |
| [33376103](https://pubmed.ncbi.nlm.nih.gov/33376103/) | 2020 | Commentary | Clin J Am Soc Nephrol | Long-term safety of tolvaptan in ADPKD |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204441 | JYNARQUE | Tablet | Not available (status: cancelled) |
| NDA022275 | SAMSCA | Tablet | Not available (status: cancelled) |
| ANDA206119 | Tolvaptan (Endo USA) | Tablet | Not available (status: cancelled) |
| ANDA216949 | Tolvaptan (Novadoz) | Tablet | Not available (status: cancelled) |
| ANDA207605 | Tolvaptan (Apotex) | Tablet | Not available (status: cancelled) |

Three more generic ANDAs (Camber, Ascend and Lupin) are also listed, all with cancelled status.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not taken from label text): liver failure, cirrhosis of liver, substance abuse/dependence, active peptic ulcer disease, demyelinating disease.
- **Liver safety signal from the literature:** the earlier ADPKD trial reported more elevations in aminotransferase and bilirubin levels with tolvaptan, and long-term safety in ADPKD is a topic of ongoing discussion.
- **Drug interactions:** 100 interactions were found in total. Notable examples include:
  - **Major:** clarithromycin
  - **Moderate:** aprepitant, dexamethasone, empagliflozin, naltrexone, rifaximin, rolapitant, and potassium supplements (citrate, bicarbonate, chloride, gluconate)
  - **Minor:** fidaxomicin, naloxegol, prucalopride

Please refer to the package insert for the full warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tolvaptan has strong RCT and systematic review evidence in ADPKD, and its V2-antagonism mechanism plausibly extends to the related PKD3 form. However, there is no evidence specific to GANAB-associated disease, and the liver safety signal is a concern, especially in a form that may involve polycystic liver disease.

**To proceed, the following is needed:**
- Full FDA package insert warnings and contraindications (a blocking gap for safety screening), particularly the liver injury warning and any restricted-access programme requirements
- Detailed mechanism-of-action data from DrugBank
- Genotype-specific (GANAB) evidence, or at least subgroup data, to confirm that the ADPKD benefit applies to PKD3
- A liver monitoring plan, given the knowledge-graph contraindications for liver failure and cirrhosis
- Clarification of the cancelled licence status, since all 8 US licences are listed as cancelled and current availability should be verified

### Other Predicted Indications (Lower Priority)

| Rank | Predicted Indication | Evidence Level | Decision | Comment |
|---|---|---|---|---|
| 2 | Renal-hepatic-pancreatic dysplasia | L5 | Hold | No evidence; speculative |
| 3 | Karyomegalic interstitial nephritis | L5 | Hold | No vasopressin-dependent mechanism |
| 4 | Thoracic malformation | L4 | Hold | Only a neonatal case report of symptomatic fluid management |
| 5 | Joubert syndrome with renal defect | L4 | Research Question | Indirect cAMP rationale; needs preclinical work |
| 6 | Adult familial nephronophthisis-spastic quadriparesia syndrome | L5 | Hold | Indirect rationale only |
| 7–10 | Hypertrichosis-related, odontal/periodontal malformation and Dandy-Walker-related syndromes | L5 | Hold | No plausible mechanism; likely model artifacts |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

