---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 1
---

# Fexofenadine
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

# Fexofenadine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Fexofenadine is an antihistamine originally used to treat allergic rhinitis, allergic and other forms of conjunctivitis, and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (also vasomotor rhinitis, atopic, papillary and vernal conjunctivitis, idiopathic urticaria) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, fexofenadine is a selective peripheral histamine H1-receptor antagonist. Its efficacy in allergic, atopic, papillary and vernal conjunctivitis suggests a possible, indirect link to histamine-mediated inflammation of the ocular surface.

However, the mechanistic rationale for rosacea conjunctivitis is weak. Ocular rosacea is driven mainly by meibomian gland dysfunction, Demodex colonization, innate immune activation and neurovascular dysregulation, with limited histamine involvement. The very high TxGNN score (99.85%) is a computational result that likely reflects network proximity to the approved conjunctivitis indications. It is not backed by clinical or literature evidence. Route compatibility and similarity to the original indications have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204507 (cancelled) | Fexofenadine HCl | Tablet, film coated | Not listed |
| ANDA211075 (cancelled) | Allergy relief | Tablet | Not listed |
| ANDA204097 (cancelled) | Fexofenadine HCL | Tablet | Not listed |
| ANDA212971 (cancelled) | Fexofenadine Hydrochloride | Tablet, film coated | Not listed |
| ANDA076502 (cancelled) | Allergy Relief | Tablet | Not listed |

All five authorizations are cancelled, and no valid single-ingredient or combination licenses remain in the compiled data.

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph (not label text)**: hypertension/hypertensive disorder, kidney disease, pyoureter, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease, coronary atherosclerosis, arteriosclerosis/atherosclerosis, angle-closure glaucoma, hyperthyroidism, Graves disease and thyrotoxicosis. These come from a computational knowledge graph and should be verified against the package insert.
- **Drug Interactions** (100 interactions recorded; examples shown):
  - Moderate: eliglustat, eluxadoline, rolapitant, magnesium hydroxide, aluminum hydroxide, magaldrate, magnesium carbonate. The antacids are notable because aluminum- and magnesium-containing products may reduce fexofenadine absorption.
  - Minor: clarithromycin, miconazole, clotrimazole.
  - Severity not classified: calcitriol, doxycycline, cimetidine, levocarnitine, epinephrine, dolasetron, dicyclomine, chlorhexidine, famotidine, acetylsalicylic acid.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, the mechanistic link to rosacea-associated conjunctivitis is weak, and all US licenses in the data are cancelled.

**To proceed, the following is needed:**
- Retrieval and review of the FDA package insert warnings and contraindications
- Confirmed mechanism of action data (DrugBank)
- A literature and trial search specific to ocular rosacea and antihistamines
- Assessment of route compatibility (oral drug versus the ocular surface target) and similarity to the original indications
- Preclinical or mechanistic evidence for any histamine role in ocular rosacea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

