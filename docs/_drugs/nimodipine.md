---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 967
evidence_level: L5
indication_count: 2
monitor_inn: "NIMODIPINE"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-10-14
description: "Nimodipine: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid h…"
---

# Nimodipine
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

# Nimodipine: From Subarachnoid Hemorrhage to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a dihydropyridine calcium channel blocker, originally used for subarachnoid hemorrhage (including aneurysmal subarachnoid hemorrhage).
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid hemorrhage) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 4 (all cancelled; 1 NDA and 3 ANDAs) |
| Recommended Decision | Hold |

A second prediction, **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, scored 99.05% and is also at evidence level L5 with a Hold recommendation. It is discussed briefly below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nimodipine is an L-type calcium channel blocker of the dihydropyridine class, used for its effects on cerebral blood vessels in subarachnoid hemorrhage.

**Homozygous familial hypercholesterolemia (HoFH)** is caused by defects in the LDL receptor pathway (LDLR, APOB, PCSK9, LDLRAP1), which impair LDL clearance. No established mechanistic link to calcium channel blockade exists. Some calcium channel blockers have been reported in preclinical settings to have minor effects on vascular lipid deposition or atherosclerosis progression. This is indirect and does not address the primary defect. The high TxGNN score is a computational output only and should not be read as evidence of efficacy.

**Second prediction, NSIAD:** This condition arises from gain-of-function mutations in the vasopressin V2 receptor (AVPR2), causing water retention independent of vasopressin. Nimodipine's calcium channel blockade has no direct connection to the V2 receptor signaling pathway (Gs-cAMP-AQP2). Any link, such as calcium modulation affecting aquaporin-2 trafficking, would be speculative. Nimodipine's blood-pressure-lowering effect also raises additional safety questions in a renal/electrolyte disorder.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA216937 | Nimodipine (Camber Pharmaceuticals) | Solution | Not specified; status cancelled |
| ANDA076740 | Nimodipine (Bionpharma) | Capsule, liquid filled | Not specified; status cancelled |
| NDA203340 | Nymalize (Azurity Pharmaceuticals) | Solution | Not specified; status cancelled |
| ANDA077811 | Nimodipine (Heritage/Avet Pharmaceuticals) | Capsule, liquid filled | Not specified; status cancelled |

Available dosage forms are an oral liquid-filled capsule and a solution. Route compatibility with the predicted indications has not been assessed.

## Safety Considerations

**Contraindications / cautions from the knowledge graph** (drug-disease edges, not label text): liver disease, gallbladder disease, hypotensive disorder.

**Drug Interactions:** 100 interactions were identified. Those listed below are from the first 20 records.
- **Major:** clarithromycin, dolasetron
- **Moderate (examples):** bupropion, aprepitant, morphine, acetylsalicylic acid, cimetidine, miconazole, magnesium sulfate, canagliflozin, dapagliflozin, empagliflozin, kanamycin, neomycin, and several calcium salts (carbonate, chloride, acetate, phosphate)

Please refer to the package insert for key warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions have only a computational basis (L5), with no clinical trials or literature. Neither has a plausible mechanistic link to nimodipine's calcium channel blockade. All US licenses are cancelled, and the safety profile (hypotension risk, liver disease caution, major interactions with CYP3A4 inhibitors such as clarithromycin) adds further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or mechanistic evidence linking calcium channel blockade to LDL metabolism (HoFH) or to V2 receptor/aquaporin-2 signaling (NSIAD)
- A systematic literature and trial search for either indication
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

