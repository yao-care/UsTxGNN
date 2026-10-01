---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 1136
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Lipid-Lowering Statin to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Rosuvastatin is a statin (HMG-CoA reductase inhibitor) used to lower cholesterol. The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**, but there are **0 clinical trials** and only **2 publications**. Both are case reports on related lipid disorders that do not test rosuvastatin in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data (approved indication text is empty in all US licenses) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Rosuvastatin is a statin that lowers LDL-C by inhibiting HMG-CoA reductase and upregulating hepatic LDL receptors.

CETP deficiency is characterized by markedly raised HDL-C. Nothing links LDL-lowering by statins to correcting that disorder. The high TxGNN score reflects proximity in the knowledge graph, not demonstrated biology or clinical benefit.

The two retrieved papers concern Apo AI deficiency and hepatic lipase deficiency, not CETP deficiency, and neither tests rosuvastatin. The prediction is therefore best treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case report / review | Journal of Clinical Lipidology | Complete Apo AI deficiency in an Iraqi Mandaean family (new APOA1 nonsense mutation). The two homozygotes differed markedly in clinical presentation. Rosuvastatin and CETP are not studied. |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case report | BMJ Case Reports | Hepatic lipase deficiency in a young Middle-Eastern male, with the first report of CETP activity and mass in this setting. Rosuvastatin is not tested. |

## US Market Information

The approved indication text is empty in the source data, so it is omitted below. Duplicate entries are merged.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA206465 | Rosuvastatin | Tablet, film coated | Quallent Pharmaceuticals Health LLC |
| ANDA206465 | Rosuvastatin Calcium | Tablet, film coated | A-S Medication Solutions |
| ANDA079172 | Rosuvastatin calcium | Tablet, film coated | REMEDYREPACK INC. |
| ANDA212059 | Rosuvastatin Calcium | Tablet, film coated | Zhejiang Yongtai Pharmaceutical Co., Ltd. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests on model score alone (L5). There are no trials, the literature is two unrelated case reports, and the mechanism does not support benefit in a disease defined by high HDL-C.

Other predictions in the same pack have much stronger evidence. Familial hypercholesterolemia and hyperlipidemia are both L1 with "Proceed with Guardrails". Both are established uses of rosuvastatin, so they confirm the existing indication rather than repurpose the drug.

**To proceed, the following is needed:**
- Any direct clinical or mechanistic data on statins in CETP deficiency
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications
- Original indication text from the approved labels
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

