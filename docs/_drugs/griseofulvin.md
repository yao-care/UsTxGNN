---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 762
evidence_level: L5
indication_count: 5
monitor_inn: "GRISEOFULVIN"
predicted_indications: ["myiasis", "wound myiasis", "creeping myiasis", "furuncular myiasis", "echinococcus granulosus infectious disease"]
---

# Griseofulvin
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

# Griseofulvin: From Tinea Infections to Myiasis

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used to treat dermatophyte (tinea) infections of the skin, scalp, nails and groin.
The TxGNN model predicts it may be effective for **myiasis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction is model-only and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea unguium, tinea barbae, dermatophytosis of the groin/perianal area and of the scalp or beard (from the knowledge graph; no approved-indication text is available from the US licence records) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 10 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, griseofulvin is a fungistatic agent that is understood to disrupt microtubule function and mitosis in fungal cells. Its efficacy in dermatophyte infections is established.

The link to myiasis is weak. Myiasis is an infestation of tissue by fly (Diptera) larvae, which is a parasitic rather than fungal condition. No established mechanism connects griseofulvin to larvicidal activity. Standard care is already in place: larval removal, and ivermectin in selected cases.

The nearly identical scores across the myiasis subtypes (wound, creeping and furuncular myiasis all score 99.34%) suggest the signal comes from shared disease-ontology relationships in the knowledge graph rather than independent biological evidence. The high score should therefore be read as a model-level association, not proof of plausibility.

**Other predictions in the list:**

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Wound myiasis | 99.34% | Likely inherited from the parent term "myiasis"; no evidence |
| 3 | Creeping myiasis | 99.34% | Treated with ivermectin or albendazole; no antiparasitic mechanism for griseofulvin |
| 4 | Furuncular myiasis | 99.34% | Managed by larval extraction or occlusion; no larvicidal mechanism |
| 5 | Echinococcus granulosus infection | 99.32% | The most conceivable mechanistically (tubulin targeting, as with benzimidazoles), but no demonstrated anthelmintic activity |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All ten US licences for griseofulvin are cancelled, and no approved-indication text was recorded for them. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091592 | Griseofulvin (Sandoz Inc) | Tablet | Not recorded |
| ANDA061996 | Ultramicrosize Griseofulvin (Chartwell RX) | Tablet | Not recorded |
| ANDA204371 | Ultramicrosize Griseofulvin (Amneal) | Tablet, coated | Not recorded |
| ANDA065354 | Griseofulvin (Cipla USA) | Suspension | Not recorded |
| ANDA065200 | Griseofulvin (Chartwell RX) | Suspension | Not recorded |

The remaining five licences are also cancelled. Available dosage forms were oral tablets (including coated tablets) and suspensions.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): liver failure; porphyria (including inherited porphyria and porphyrin metabolism disease); systemic lupus erythematosus (including the paediatric form); substance abuse/dependence; and agranulocytosis and neutropenia (including cyclic hematopoiesis and congenital neutropenia syndromes).
- **Drug interactions:** The interaction screening returned 100 records. Most of those listed are of Moderate severity, with a few Minor. Notable moderate interactions include:
  - Anticoagulants and antiplatelets: warfarin, dicoumarol, apixaban, rivaroxaban, ticagrelor
  - Antidiabetic agents: saxagliptin, linagliptin, repaglinide
  - Antimalarials and antiparasitics: artemether, mefloquine, praziquantel
  - Others: aprepitant, rolapitant, eliglustat, naloxegol, nitisinone, fostamatinib, macimorelin
  - Minor: acetylsalicylic acid, liraglutide

Please refer to the package insert for label warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials or publications and no plausible mechanism for activity against fly larvae. Established treatments already exist. All US licences are cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data for griseofulvin and a documented mechanistic rationale for myiasis
- FDA package insert warnings and contraindications, needed for safety screening
- In vitro or animal data showing larvicidal activity (for myiasis), or protoscolicidal or cyst-model data (for echinococcosis, the most conceivable alternative)
- A review of whether the identical subtype scores reflect an ontology artefact
- Assessment of the formulation and route needed for any new indication, including the implications of the cancelled US marketing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

