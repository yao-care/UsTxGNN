---
layout: default
title: Lovastatin
parent: Model Prediction Only (L5)
nav_order: 874
evidence_level: L5
indication_count: 1
monitor_inn: "LOVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-20
description: "Lovastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hyperlipidemia, including hypertriglyceridemia…"
---

# Lovastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lovastatin: From Hyperlipidemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Lovastatin is a statin that lowers cholesterol. The TxGNN model (deep learning) gives it a score of 0.9942 for cholesterol-ester transfer protein deficiency; this score may reflect similarities the model learned between related diseases, not biological evidence.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**,
but there are currently **0 clinical trials** and **1 publication** (a mouse study with no direct link to this disease), so the prediction rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia, including hypertriglyceridemia, familial hyperlipidemia, atherosclerosis and hypoalphalipoproteinemia (relations recorded in the knowledge graph; no approved-indication text available in the data compiled for this report) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 7 of 12) |
| Number of FDA Applications | 12 (active: 7) |
| Number of approvals | At least 3 ANDAs (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the FDA-approved prescribing information for lovastatin: "The mechanism of the LDL-lowering effect of lovastatin may involve both reduction of VLDL-C concentration, and induction of the LDL receptor, leading to reduced production and/or increased catabolism of LDL-C. Apolipoprotein B also falls during treatment with lovastatin. Lovastatin is a specific inhibitor of HMG-CoA reductase, the enzyme which catalyzes the conversion of HMG-CoA to mevalonate." ([DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34), label version 2026-11-13; accessed 2026-11-19.) Based on general knowledge, lovastatin is a statin that inhibits HMG-CoA reductase and lowers LDL cholesterol. CETP deficiency alters lipoprotein remodeling and raises HDL cholesterol, so a biological link through lipid metabolism is plausible.

However, CETP deficiency is mainly a laboratory or genetic phenotype with high HDL and usually does not need treatment. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as lipid-metabolism disorders already linked to lovastatin, not biological evidence. It is not a validated therapeutic signal. The one retrieved publication concerns a mouse model and has no apparent direct relevance to lovastatin or to CETP deficiency in humans.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | Preclinical (animal model) | Journal of Lipid Research | Targeted disruption of StARD4 in mice led to modest weight reduction and minor changes in lipid metabolism; no direct study of lovastatin or CETP deficiency |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078296 | Lovastatin (Lupin Pharmaceuticals, Inc.) | Tablet | Not provided |
| ANDA075991 | Lovastatin (NuCare Pharmaceuticals, Inc.) | Tablet | Not provided |
| ANDA075551 | Lovastatin (REMEDYREPACK INC.) | Tablet | Not provided |

The list of authorizations may be partial.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: The knowledge graph lists contraindication relations with the following conditions, among others: liver disease, gallbladder disease, thrombocytopenia, hyperglycemia, peptic ulcer disease, myopathy and other muscle diseases, rhabdomyolysis, diabetes mellitus, diabetic ketoacidosis, gout, blood coagulation disease, acute coronary syndrome, coronary artery disease, myocardial infarction, hypotensive disorder and hypophosphatemia. These must be checked against the official label.
- **Drug Interactions**: 100 interactions are recorded in total. Examples:
  - Major: clarithromycin
  - Moderate: aprepitant, omeprazole, esomeprazole, lansoprazole, pantoprazole, metronidazole, tinidazole, cimetidine, clotrimazole, miconazole, eluxadoline, naltrexone, pectin, rosuvastatin, simvastatin, troglitazone
  - Minor: exenatide

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no directly relevant literature, so it stays at evidence level L5. CETP deficiency is mainly a phenotype that usually does not require treatment, so the clinical need is also unclear.

**To proceed, the following is needed:**
- Clarify whether CETP deficiency is a disease that needs treatment, and what a meaningful clinical endpoint would be
- Search for studies that directly examine lovastatin or statins in CETP deficiency
- Obtain the FDA package insert warnings and contraindications for safety screening
- Obtain detailed mechanism-of-action data from DrugBank

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

