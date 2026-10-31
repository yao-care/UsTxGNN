---
layout: default
title: Iron
parent: Model Prediction Only (L5)
nav_order: 811
evidence_level: L5
indication_count: 6
monitor_inn: "IRON"
predicted_indications: ["vitamin B12- and folate-independent constitutional megaloblastic anemia", "Plummer-Vinson syndrome", "non-syndromic esophageal malformation", "biotin metabolic disease", "vitamin deficiency disorder", "esophageal disease"]
last_modified_at: 2026-10-31
description: "Iron: predicted new indication Vitamin B12- and folate-independent constitutional megaloblastic anemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Iron
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Iron: Vitamin B12- and folate-independent constitutional megaloblastic anemia
{: .text-alpha }

## One-Sentence Summary

Iron is an essential mineral, originally used to treat iron deficiency anemia and related nutritional anemias.
The TxGNN model predicts it may be effective for **vitamin B12- and folate-independent constitutional megaloblastic anemia**, but this rests on the prediction alone, with **0 clinical trials** and **0 publications** supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vitamin B12- and folate-independent constitutional megaloblastic anemia |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 2) |
| Number of FDA Applications | at least 2 |
| Recommended Decision | Hold |

*Note: the US authorization records contain no approved-indication text, so the original indications come from the drug-disease knowledge base used by the TxGNN model.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iron is an essential mineral that supports hemoglobin synthesis, and its efficacy in iron deficiency anemia is well established.

The link to the predicted indication is weak. Megaloblastic anemia is driven by impaired DNA synthesis, not by a lack of iron. Iron is therefore not expected to correct this condition. The high TxGNN score (0.9989) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

For comparison, the model's second-ranked prediction, **Plummer-Vinson syndrome**, is much better grounded. It is defined by iron deficiency anemia, dysphagia and esophageal webs, and iron repletion is already its established first-line treatment. This is largely standard care, not a new repurposing signal. The data compiled for it consist of reviews, case reports and one retrospective multicenter study, and no registered trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Ferrum Metallicum (Hahnemann Laboratories, Inc.) | Pellet | Not listed (cancelled) |
| NDA217347 | Sofdra (Botanix SB Inc.) | Gel | Not listed (valid) |

Neither record states an approved indication. The Sofdra record should be verified against the source label, because a topical gel is an unusual match for an iron product.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** peptic ulcer disease, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, hemolytic anemia, gastroenteritis.
- **Drug Interactions:** 79 interactions were recorded. The main ones are:
  - **Major:** dolutegravir, bictegravir.
  - **Moderate:**
    - Antibiotics: doxycycline, tetracycline, ciprofloxacin, delafloxacin, cefdinir, chloramphenicol.
    - Acid suppressants and antacids: omeprazole, rabeprazole, sodium citrate, magnesium oxide.
    - Bisphosphonates: alendronic acid, risedronic acid, ibandronate.
    - Others: levodopa, deferiprone, pancrelipase, baloxavir marboxil.
  - **Minor:** cimetidine.
- Many of these interactions involve reduced absorption of iron or of the co-administered drug, so dose separation is typically needed.

For label warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the mechanism is implausible: megaloblastic anemia is caused by impaired DNA synthesis, not iron deficiency. The high model score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Iron is marketed in the US, with 2 valid licenses on record.

**To proceed, the following is needed:**
- Mechanistic evidence that iron affects this form of megaloblastic anemia, or a rationale for the model's prediction.
- Any clinical or case-level data on iron in constitutional megaloblastic anemia.
- Detailed mechanism of action data (MOA) and FDA label warnings and contraindications.
- If the team wants a more tractable lead, a separate evaluation of Plummer-Vinson syndrome, which would need prospective controlled data to add value beyond current standard care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

