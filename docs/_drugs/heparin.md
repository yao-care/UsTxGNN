---
layout: default
title: Heparin
parent: Model Prediction Only (L5)
nav_order: 769
evidence_level: L5
indication_count: 2
monitor_inn: "HEPARIN"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
last_modified_at: 2026-10-14
description: "Heparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
---

# Heparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Heparin: From Pulmonary Embolism to Protein C Deficiency Thrombophilia
{: .text-alpha }

## One-Sentence Summary

Heparin is an injectable anticoagulant, originally used for pulmonary embolism, disseminated intravascular coagulation, and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but **no clinical trials and no publications** currently support this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans (the US label text was not available in the compiled data) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 13 (all cancelled; includes both NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, heparin potentiates antithrombin-mediated inhibition of thrombin and factor Xa. This could plausibly offset the hypercoagulable state caused by protein C deficiency.

The link to the original indications is biologically coherent. Heparin is already used in purpura fulminans, a severe manifestation of homozygous protein C deficiency, so the predicted indication is closely related to an existing use.

However, there are no clinical trials or publications for this specific indication. The high TxGNN score is a computational prediction only. Standard care for severe congenital protein C deficiency relies on protein C concentrate plus anticoagulation, and the available data do not allow an independent assessment of heparin's role.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090808 | Heparin Sodium (Sagent Pharmaceuticals) | Injection, solution | Not available (cancelled) |
| NDA018916 | Heparin Sodium (Hospira, Inc.) | Injection, solution | Not available (cancelled) |
| NDA019953 | Heparin Sodium in Sodium Chloride (B. Braun Medical Inc.) | Injection | Not available (cancelled) |
| NDA017037 | Heparin Sodium (Hikma Pharmaceuticals USA Inc.) | Injection | Not available (cancelled) |
| NDA018609 | Heparin Sodium in Sodium Chloride (Baxter Healthcare Corporation) | Injection, solution | Not available (cancelled) |

Of the 13 authorizations listed, all are cancelled and none is currently valid. Only 5 are shown here.

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease edges, not label text):** liver failure, hematologic disease, thrombocytopenia, heparin-induced thrombocytopenia, blood coagulation disease, hemophilia, antithrombin III deficiency, Glanzmann thrombasthenia, qualitative platelet defect, intracranial or intracerebral hemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, biliary tract disease, obstructive jaundice, infective endocarditis, diabetic and hypertensive retinopathy, retinal disease, osteoporosis, and arteriosclerosis obliterans.
- **Drug Interactions:** 100 interactions were identified. Those listed as moderate include acetylsalicylic acid, the sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide, acetohexamide), the meglitinides (repaglinide, nateglinide), and the weight-loss agents fenfluramine, dexfenfluramine, and sibutramine. Others (levocarnitine, mannitol, calcitriol, vitamin A, pantoprazole, mesalazine, doxycycline) have unknown severity.

Official label warnings and contraindications were not available in the compiled data. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and close to heparin's existing use in purpura fulminans. However, there are no trials or publications for this indication, the evidence level is L5, and all US heparin licenses are cancelled. The label safety review is also incomplete.

**To proceed, the following is needed:**
- Download and review the FDA package insert for warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A targeted literature search on heparin in congenital protein C deficiency and purpura fulminans, compared with protein C concentrate
- Confirmation of the current US market and licensing status, since all listed licenses are cancelled

---

**Note on the second predicted indication (primary release disorder of platelets, score 99.06%):** This is not recommended (Hold, L5). Heparin is an anticoagulant that increases bleeding risk and can cause heparin-induced thrombocytopenia. The 20 associated publications are indirect (cirrhosis coagulation, HIT, cancer-associated VTE) and none evaluates heparin as a treatment for this disorder. The high score is likely an artifact of shared coagulation and platelet terms in the knowledge graph.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

