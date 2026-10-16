---
layout: default
title: Pilocarpine
parent: Model Prediction Only (L5)
nav_order: 1044
evidence_level: L5
indication_count: 1
monitor_inn: "PILOCARPINE"
predicted_indications: ["primary hereditary glaucoma"]
last_modified_at: 2026-10-14
description: "Pilocarpine: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma, ocular hypertension"
---

# Pilocarpine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Pilocarpine: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine was originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction currently rests on model output and general pharmacology alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma, ocular hypertension (from the TxGNN knowledge graph; no approved indication text in the US license records) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 license records (all cancelled; includes 4 NDAs and 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, pilocarpine is a muscarinic (M3) agonist. It contracts the ciliary muscle and increases trabecular outflow, which lowers intraocular pressure (IOP). This is the basis of its established use in open-angle glaucoma and ocular hypertension.

Primary hereditary glaucoma is also characterised by raised IOP from impaired aqueous outflow, so a mechanistic fit is plausible. The very high TxGNN score (0.998) is likely driven largely by the close similarity to the original glaucoma indications in the knowledge graph, rather than by independent evidence.

There are important caveats. Primary hereditary forms (for example congenital or juvenile-onset glaucoma) are often caused by developmental abnormalities of the trabecular meshwork or anterior chamber angle. In these cases miotics may work poorly, and they are typically second-line to surgery such as goniotomy or trabeculotomy. Use in children also raises safety concerns, including cholinergic side effects, myopic shift and brow ache.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 10 US license records are cancelled, and none contain approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020237 | Salagen (Advanz Pharma) | Film-coated tablet | Not listed |
| NDA214028 | VUITY (AbbVie) | Solution/drops | Not listed |
| NDA217836 | Qlosi (Orasis) | Solution | Not listed |
| NDA200890 | Pilocarpine Hydrochloride (Sandoz) | Solution/drops | Not listed |
| ANDA214193 | Pilocarpine Hydrochloride (Amneal) | Solution/drops | Not listed |

Five further records are cancelled generic film-coated tablets (ANDA077220, ANDA076963, ANDA077248, ANDA212377, ANDA076746).

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links pilocarpine to contraindications in several disease groups:
  - Eye: angle-closure (closed-angle) glaucoma, uveitis, iritis, iridocyclitis, keratitis, keratoconjunctivitis, retinal detachment.
  - Respiratory: asthma, COPD (including severe early-onset), bronchial disease.
  - Biliary: cholelithiasis, cholecystolithiasis, choledocholithiasis, cholecystitis, biliary tract disease, obstructive jaundice.
  - Kidney and liver: nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, liver failure.
- **Drug Interactions**: 100 interactions were found. The ones with a listed level of Moderate are antimuscarinic or anticholinergic agents, which may oppose pilocarpine's cholinergic effect:
  - Atropine (systemic and ophthalmic)
  - Hyoscyamine
  - Scopolamine (systemic and ophthalmic)
  - Glycopyrronium (systemic and topical)
  - Clidinium
  - Dicyclomine
  - Mepenzolate
  - Methscopolamine
  - Propantheline
  - Trospium
  
  Other listed interactions, such as pantoprazole, omeprazole, lansoprazole, clotrimazole, morphine, metformin and epinephrine, have an unknown severity level.

Please refer to the package insert for formal warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model support (L5) with no registered trials or publications. Primary hereditary glaucoma is often anatomical, and miotics are generally second-line to surgery. There are also paediatric safety concerns, and no US licenses are currently valid.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for pilocarpine in congenital, juvenile and other hereditary glaucomas
- Assessment of efficacy relative to surgery and current first-line medical therapy
- Paediatric safety and dosing evaluation
- Review of formulation and route (ophthalmic) compatibility, and of the cancelled US market status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

