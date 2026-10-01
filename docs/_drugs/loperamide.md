---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 869
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is an over-the-counter and prescription antidiarrheal, marketed in the US under 20 authorizations.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis** with a very high score, but this prediction has **0 clinical trials** and **0 publications** behind it.
It rests on model output alone and does not withstand a pharmacological check.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhea (inferred from the "anti-diarrheal" product labeling; approved indication text is not provided in the source data) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Loperamide is a peripherally restricted mu-opioid receptor agonist that slows gut motility. Its use in diarrhea is well established.

The prediction does not hold up mechanistically. Loperamide acts on the gut, and nothing links a gut-restricted opioid agonist to inflammation or infection of the ocular surface. It has no antimicrobial or antiparasitic activity. The high TxGNN score most likely reflects a knowledge-graph neighborhood artifact. Several conjunctivitis subtypes appear together in the top 10 with near-identical scores, which points to the same artifact.

The rest of the top 10 is weak too. Amebic dysentery (rank 2) conflicts with known risk, because slowing gut transit in invasive amebic colitis may worsen outcomes. Gastroduodenitis (rank 4) is the only candidate with a plausible symptomatic rationale. It is considered a research question, not an efficacy signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021855 | anti-diarrheal | Capsule, liquid filled | Albertsons Companies |
| ANDA072741 | Loperamide Hydrochloride | Capsule | Bryant Ranch Prepack |
| ANDA091292 | Equate Loperamide Hydrochloride | Suspension | Wal-Mart Stores Inc |
| ANDA206548 | Loperamide Hydrochloride | Tablet | Amerisource Bergen |
| ANDA076497 | Anti-Diarrheal | Tablet, coated | First Aid Direct |

Available forms are oral (capsule, tablet, film-coated tablet) plus suspension and solution. No ophthalmic formulation is listed.

## Safety Considerations

Please refer to the package insert for safety information. Drug interaction data was not found in the source record.

Literature retrieved for the lower-ranked predictions points to safety signals worth knowing:
- **Toxic megacolon and fulminant colitis:** A 2007 case report describes fulminant amoebic colitis after heavy loperamide use. Antimotility agents have been implicated in toxic megacolon in infectious gastroenteritis.
- **Central opioid effects with a damaged gut lining:** A 2026 case report describes respiratory depression with therapeutic loperamide in severe gastrointestinal inflammation after chemotherapy. Mucosal injury may increase systemic absorption.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acute contagious conjunctivitis) has no trials, no literature, and no plausible mechanism. The score of 99.97% therefore carries no practical weight. There is also no ophthalmic formulation, and the source record lacks package insert safety data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any credible preclinical or clinical evidence for an ocular indication. Without it, this prediction should not advance.
- Consider redirecting effort to gastroduodenitis (rank 4), the only prediction with a plausible symptomatic rationale. It would need a controlled study and a review of the mucosal-permeability safety concern.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

