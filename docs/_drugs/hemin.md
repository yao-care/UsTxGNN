---
layout: default
title: Hemin
parent: Model Prediction Only (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
monitor_inn: "HEMIN"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
---

# Hemin
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

# Hemin: From Acute Intermittent Porphyria to Thrombocytopenic Purpura

## One-Sentence Summary

Hemin was originally used to treat acute intermittent porphyria.
The TxGNN model predicts it may be effective for **thrombocytopenic purpura**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute intermittent porphyria |
| Predicted New Indication | Thrombocytopenic purpura |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (BLA101246, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hemin is a heme preparation used in acute intermittent porphyria, a disorder of heme biosynthesis. Hemin supplies heme and induces heme oxygenase-1, but the data compiled for this report show no established link between these actions and platelet disorders.

The high TxGNN score (99.79%) reflects a knowledge-graph association only. No trials or publications were found to explain why a porphyria treatment would help thrombocytopenic purpura, so the mechanistic link remains unconfirmed.

Other top predictions are mostly coagulation or bleeding disorders (hemophilia, von Willebrand disease, factor XI deficiency, C1 inhibitor deficiency, and others). They appear to share the same graph signal and are not independent evidence. Hemin has also been reported to cause coagulopathy or thrombophlebitis at high doses, which is a safety concern and argues against these indications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for thrombocytopenic purpura.

For the second-ranked prediction (hemophilia), three publications were retrieved. They concern givosiran, an RNAi therapy, in acute hepatic porphyria. They are not about hemin in hemophilia and give no support for that repurposing.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA101246 (cancelled) | Panhematin (Recordati Rare Diseases, Inc.) | Powder, for solution | Not available |

## Safety Considerations

- **Drug Interactions**: 74 interactions were identified in total. The first 20 listed include the following.
  - **Major**: ethinylestradiol, estradiol, conjugated estrogens, and the barbiturates butalbital, amobarbital and phenobarbital.
  - **Moderate**: mainly antithrombotic or bleeding-risk agents, including acetylsalicylic acid, abciximab, alteplase, anagrelide, apixaban, betrixaban, dipyridamole, antithrombin preparations, and acalabrutinib. Also moderate: ibritumomab tiuxetan, tositumomab (I-131), trastuzumab emtansine and avapritinib.
- The interaction pattern with antithrombotic drugs is especially relevant in a bleeding or platelet disorder.
- Hemin's reported coagulation effects (coagulopathy, thrombophlebitis at high doses) should be considered in any coagulation-related use.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no relevant literature, and no mechanistic link to thrombocytopenic purpura. The product's US license is cancelled, and hemin's known coagulation effects raise safety concerns for bleeding and platelet disorders.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical or mechanistic evidence linking heme or heme oxygenase-1 induction to platelet disorders
- Clarification of the regulatory status of the product and available routes of administration
- A safety assessment of hemin's coagulation effects and its interactions with antithrombotic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

