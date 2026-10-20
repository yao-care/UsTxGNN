---
layout: default
title: Gemfibrozil
parent: Moderate Evidence (L3-L4)
nav_order: 749
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Gemfibrozil: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Hypertriglyceridemia"
monitor_inn: "GEMFIBROZIL"
predicted_indications: ["rheumatoid arthritis", "multiple endocrine neoplasia", "HIV infectious disease", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "methemoglobinemia, alpha type", "obsolete familial combined hyperlipidemia", "sclerosing cholangitis", "methemoglobin reductase deficiency"]
---

# Gemfibrozil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Gemfibrozil: From Hypertriglyceridemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a lipid-lowering drug originally used to treat hypertriglyceridemia.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials** are registered and only **4 publications** were found, all preclinical or indirect. Evidence for this prediction is therefore weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia (from knowledge-graph indication data; no approved-indication text is listed for the US licenses) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all generic ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for gemfibrozil are not available in the data compiled for this report. Based on the mechanistic analysis, gemfibrozil is a PPAR-alpha agonist. This is how it lowers triglycerides in hypertriglyceridemia. PPAR-alpha activation has also been linked to anti-inflammatory effects, including lower pro-inflammatory cytokines and modulation of T-cell responses.

Hypertriglyceridemia and rheumatoid arthritis are quite different diseases, so the link is indirect and runs through inflammation rather than lipids. Supporting evidence comes from animal work. The related pan-PPAR agonist bezafibrate attenuated experimental arthritis, and gemfibrozil combined with a reduced steroid dose performed similarly to a full steroid dose in a rat arthritis model. Neither result has been shown in humans, so the plausibility is real but unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclinical (rat model) | Modern Rheumatology | In rats with adjuvant-induced arthritis, gemfibrozil plus reduced-dose prednisolone gave a management picture similar to full-dose steroid |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical (animal model) | International Immunopharmacology | Bezafibrate, a related pan-PPAR agonist, attenuated experimental rheumatoid arthritis through PPAR-dependent modulation of inflammatory pathways, with emphasis on PPAR-γ; supports the drug class rather than gemfibrozil itself |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical (mechanistic) | Journal of Immunology | Mechanistic study of how myelin basic protein priming reduces Foxp3 expression in regulatory T cells via nitric oxide; indirect relevance to autoimmunity |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review / other | American Journal of Clinical Dermatology | General review of palmar erythema and its causes; no direct evidence on gemfibrozil |

## US Market Information

All five US licenses are generic tablets and are now cancelled. The compiled data do not list approved-indication text for them.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA204189 | Gemfibrozil (Viona Pharmaceuticals) | Tablet | Cancelled |
| ANDA214603 | Gemfibrozil (Proficient Rx) | Tablet | Cancelled |
| ANDA078012 | Gemfibrozil (Bryant Ranch Prepack) | Tablet | Cancelled |
| ANDA077836 | Gemfibrozil (RemedyRepack) | Tablet | Cancelled |
| ANDA202726 | Gemfibrozil (Vangard Labs) | Tablet, film coated | Cancelled |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text): liver disease, gallbladder disease, cholelithiasis, cholecystolithiasis, choledocholithiasis, primary biliary cholangitis, impaired renal function, thrombocytopenia, leukopenia, anemia (including macrocytic anemia), and Reynolds syndrome.
- **Drug interactions:** 100 interactions were recorded; the 20 shown here are mostly with other lipid-lowering and antidiabetic drugs.
  - **Major:** rosuvastatin, simvastatin, pioglitazone, repaglinide, eluxadoline, loperamide.
  - **Moderate:** chenodeoxycholic acid, chlorpropamide, tolazamide, nateglinide, rosiglitazone, rifaximin, and multiple insulins (aspart, degludec, detemir, glargine, glulisine, human regular and isophane, inhaled human).

Please refer to the package insert for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but support is limited to animal and mechanistic studies, with no registered human trials. Gemfibrozil also has substantial interaction and hepatobiliary safety concerns, and its US licenses are all cancelled. This is a hypothesis, not yet a development candidate.

For context, two other predicted indications for gemfibrozil have more human evidence. These are protease inhibitor-associated hypertriglyceridemia in HIV patients (randomized double-blind data, though this is largely an extension of its original lipid indication) and hypoalphalipoproteinemia (small older crossover studies using lipid surrogate endpoints).

**To proceed, the following is needed:**
- Confirmation in additional arthritis models, ideally with gemfibrozil itself rather than related fibrates.
- Formal mechanism-of-action data and package-insert warnings and contraindications.
- A safety assessment for rheumatoid arthritis patients, who commonly take interacting or hepatically relevant drugs such as methotrexate.
- A small proof-of-concept clinical study design, if the preclinical results are confirmed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

