---
layout: default
title: Ceftazidime
parent: Model Prediction Only (L5)
nav_order: 507
evidence_level: L5
indication_count: 9
monitor_inn: "CEFTAZIDIME"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "epiglottitis", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
last_modified_at: 2026-11-20
description: "Ceftazidime: predicted new indication polyclonal hyperviscosity syndrome (evidence level L5). In the US: 17 FDA applications (4 active)"
---

# Ceftazidime
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

## Ceftazidime: third-generation cephalosporin antibiotic → polyclonal hyperviscosity syndrome
{: .text-alpha }

## One-Sentence Summary

Ceftazidime is an injectable cephalosporin antibiotic that kills bacteria by blocking cell wall synthesis. The TxGNN model predicts it may be relevant to **polyclonal hyperviscosity syndrome**, with a score of 0.9951. **No clinical trials and no publications** in the data compiled for this report address this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 4 of 17) |
| Number of FDA Applications | 17 (active: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for ceftazidime: "Ceftazidime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftazidime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93), label version 2026-08-03; accessed 2026-11-19.) As a cephalosporin, ceftazidime is known to bind penicillin-binding proteins and block bacterial cell wall synthesis.

Polyclonal hyperviscosity syndrome is a condition of abnormally thick blood, linked to elevated immunoglobulin levels. It is not a bacterial disease, and it has no cell wall target for an antibiotic to act on. The data compiled for this report found no plausible mechanistic link. The high score looks like a statistical output of the model rather than a biologically grounded signal. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Ceftazidime is marketed in the United States as an injectable (powder for solution) dosage form, under single-ingredient products from more than one manufacturer. No indication text is recorded in the local data for these products.

## Safety Considerations

- **Drug Interactions**: 100 interaction records were retrieved. The main moderate-level interactions are:
  - Amphotericin B (including the cholesteryl sulfate, lipid complex and liposomal forms)
  - Kanamycin
  - Neomycin
  - Streptomycin
  - Picosulfuric acid

  Several other pairings, such as vancomycin, metformin, omeprazole and morphine, are listed at an unknown severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and no plausible link between ceftazidime's antibacterial action and a hyperviscosity condition was found. A high model score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence that directly studies ceftazidime in polyclonal hyperviscosity syndrome
- A biological rationale for how a cell wall-targeting antibiotic could affect this condition
- Full mechanism-of-action data
- Safety information from the current package insert

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for ceftazidime is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

