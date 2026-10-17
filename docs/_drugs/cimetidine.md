---
layout: default
title: Cimetidine
parent: Model Prediction Only (L5)
nav_order: 530
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Cimetidine: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Gastric ulcer, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "CIMETIDINE"
predicted_indications: ["duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
---

# Cimetidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Cimetidine: From Gastric Ulcer to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is a histamine H2-receptor antagonist originally used for acid-related conditions such as gastric and duodenal ulcer, gastroesophageal reflux disease and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **Smouldering systemic mastocytosis**, but this prediction currently has **0 clinical trials** and **0 publications** supporting it.
The prediction therefore rests on model output alone (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, gastroesophageal reflux disease, esophagitis, dyspepsia, duodenal ulcer, Zollinger-Ellison syndrome (the data compiled for this report also lists systemic mastocytosis and mastocytosis) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 9 (all cancelled; 1 NDA and 8 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cimetidine blocks histamine H2 receptors and reduces gastric acid secretion. In mast-cell disease, excess histamine release drives gastric hypersecretion and related symptoms, so H2 blockade may relieve these.

The high TxGNN score most likely reflects that systemic mastocytosis and mastocytosis already appear among cimetidine's known indications in the knowledge graph. Smouldering systemic mastocytosis is a subtype of the same disease family, so the link is plausible. However, H2 blockade would only control symptoms. It would not modify the underlying mast-cell disease.

No trials or literature specific to this subtype were found, so the prediction remains unverified.

### Other Predicted Indications (Lower Priority)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Active peptic ulcer disease | 99.79% | L4 | Essentially an original indication, so not true repurposing. Most literature consists of reviews of other drugs. |
| 3 | Gastrojejunal ulcer | 99.77% | L4 | Acid suppression is plausible, but no specific trial was found. |
| 4 | Peptic ulcer perforation | 99.77% | L4 | Case reports describe perforation occurring during cimetidine therapy, which argues against benefit. |
| 5 | Lymphoadenopathic mastocytosis with eosinophilia | 99.76% | L5 | Rare condition. No studies found. |
| 6 | Duodenogastric reflux | 99.49% | L4 | Poor mechanistic fit (bile reflux is not mainly acid-driven). Evidence is indirect or preclinical. |
| 7 | Duodenal obstruction | 99.44% | L4 | Only a small uncontrolled 1978 report of response in ulcer-related gastric outlet obstruction. |
| 8 | Acne | 99.33% | L4 | Possible anti-androgenic effect, but evidence is indirect. Labelled a research question. |
| 9 | Abnormality of glucagon secretion | 99.14% | L5 | The single paper is an unrelated imaging study. The signal appears spurious. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for smouldering systemic mastocytosis.

---

## US Market Information

All nine US authorizations are cancelled. No approved indication text was available in the data compiled for this report. The table below lists the five main authorizations.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA020238 | TAGAMET (Prestige Brands Holdings, Inc.) | Tablet | Cancelled |
| ANDA074329 | Cimetidine (Chartwell RX, LLC) | Film-coated tablet | Cancelled |
| ANDA074251 | Cimetidine hydrochloride (Chartwell RX, LLC) | Solution | Cancelled |
| ANDA074151 | Cimetidine (Teva Pharmaceuticals USA, Inc.) | Film-coated tablet | Cancelled |
| ANDA074664 | Cimetidine hydrochloride (PAI Pharma) | Solution | Cancelled |

---

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text)**: Liver disease, gallbladder disease, impaired renal function, and gastric cancer (including gastric neoplasm, diffuse gastric adenocarcinoma, gastric linitis plastica and gastric carcinoma).
- **Drug Interactions**: 100 interactions were recorded in total. The first 20 returned include mostly Minor and Moderate levels. Moderate-level examples include paclitaxel, fentanyl, acalabrutinib, lidocaine, acebutolol, dihydrocodeine, codeine, tramadol, nifedipine and alfentanil. Minor-level examples include dolutegravir, zidovudine, acetaminophen, ibuprofen, ketorolac, ethinylestradiol, albendazole, ethanol, alendronic acid and cholecalciferol.

Please refer to the package insert for full warnings and precautions, as label-based safety data were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and the drug's existing association with mastocytosis. No trials or publications address smouldering systemic mastocytosis, and H2 blockade would be symptomatic rather than disease-modifying. All US authorizations are cancelled, and label-based safety information is missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational evidence of cimetidine in smouldering systemic mastocytosis, including comparison with standard H1/H2 antihistamine and mast-cell-directed therapy
- Clarification of US regulatory pathway, given that all current authorizations are cancelled
- Interaction review for patients on concurrent therapies, especially those with Moderate-level interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

