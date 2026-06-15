---
layout: default
title: Alpine Strawberry Arsenic Trioxide Atropa Belladon
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 0
---

# Alpine Strawberry Arsenic Trioxide Atropa Belladon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Multi-Ingredient Combination (13 Components): Evaluation Incomplete — No TxGNN Repurposing Prediction Available

## One-Sentence Summary

This submission describes a 13-component mixture — containing botanical, mineral, and chemically hazardous ingredients such as Arsenic Trioxide, Atropa Belladonna, Mercuric Chloride, and Strychnos Nux-Vomica Seed — whose original therapeutic indication is not recorded and which is not marketed in the United States.
The TxGNN model generated **no repurposing predictions** for this entry, and no US NDA was found.
**This case cannot be evaluated under the standard drug repurposing framework until the formulation identity and indication are clarified.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unknown — no regulatory record found |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no prediction generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This submission is a multi-ingredient entry containing 13 distinct substances:

> Alpine Strawberry · Arsenic Trioxide · Atropa Belladonna · Cajuput Oil · Capsicum · Cinchona Officinalis Bark · Frangula Purshiana Bark · Lycopodium Clavatum Spore · Mercuric Chloride · Nitric Acid · Phosphorus · Phytolacca Americana Root · Strychnos Nux-Vomica Seed

The TxGNN knowledge graph operates on single active pharmaceutical ingredients (APIs) mapped to DrugBank IDs. A compound mixture submitted as a single INN string cannot be resolved to a node in the knowledge graph, which explains why no predictions were returned. Additionally, no DrugBank ID was assigned (`drugbank_id: null`), confirming that the system was unable to identify a canonical drug entity.

The formulation profile is consistent with a **homeopathic or traditional compound preparation**, where multiple low-dose botanical and mineral ingredients are combined. Such preparations fall outside the TxGNN model's training domain and cannot be assessed using the standard pipeline.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this multi-ingredient combination as a unified formulation.

---

## Literature Evidence

Currently no related literature available for this multi-ingredient combination as a unified formulation.

---

## US Market Information

No US marketing authorizations found.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No records found in US regulatory database |

---

## Safety Considerations

**This formulation contains multiple high-risk substances that warrant immediate safety review before any further evaluation.**

- **Arsenic Trioxide**: An approved antineoplastic agent (used in acute promyelocytic leukaemia at therapeutic doses), but also a potent toxin at uncontrolled doses. Cardiotoxicity (QT prolongation), peripheral neuropathy, and myelosuppression are known risks.
- **Mercuric Chloride**: A highly toxic inorganic mercury compound; nephrotoxic and corrosive. Not approved for systemic use.
- **Nitric Acid**: A corrosive mineral acid; no established therapeutic use as a systemic agent.
- **Atropa Belladonna**: Contains atropine and scopolamine (anticholinergic alkaloids); narrow therapeutic index, significant overdose risk.
- **Strychnos Nux-Vomica Seed**: Source of strychnine; a potent neurotoxin causing tetanic convulsions.
- **Phosphorus**: Elemental phosphorus is hepatotoxic and nephrotoxic.

The co-presence of multiple toxic substances in a single preparation raises serious safety concerns that cannot be assessed without knowing the dose, form (homeopathic dilution vs. full concentration), and regulatory classification of the finished product.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline requires a single, DrugBank-resolvable active ingredient to generate repurposing predictions. This entry was submitted as a 13-component mixture with no assigned DrugBank ID, no original indication, no US regulatory approval, and no safety data — none of the minimum requirements for evaluation are met. Additionally, the presence of Arsenic Trioxide, Mercuric Chloride, and Strychnine in the same formulation triggers a mandatory safety review before any further analysis.

**To proceed, the following is needed:**

- **Formulation clarification**: Confirm whether this is a homeopathic product (with ultra-dilute ingredients per pharmacopoeial standards) or a conventional multi-herb/mineral preparation; the regulatory and safety implications differ fundamentally.
- **Target API identification**: If the intent is to evaluate a single active ingredient (e.g., Arsenic Trioxide for oncology repurposing), resubmit that ingredient individually with its DrugBank ID (DB01169).
- **Regulatory status verification**: Confirm the country of origin and applicable regulatory framework; homeopathic OTC products may be registered under different pathways (e.g., FDA OTC monograph, homeopathic drug ANDA).
- **Safety data for component substances**: Obtain package insert or equivalent toxicology data for each ingredient, particularly the four high-risk compounds identified above.
- **Dose and concentration data**: Homeopathic preparations (e.g., 6C, 30C dilutions) carry different risk profiles than conventional concentrations; this information is essential before any safety conclusion can be drawn.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

