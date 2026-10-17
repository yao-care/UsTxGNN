---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Keratitis, keratoconjunctivitis, blepharoconjunctivitis"
monitor_inn: "BACITRACIN"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: From Keratitis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical polypeptide antibiotic, originally used for eye infections such as keratitis, keratoconjunctivitis and blepharoconjunctivitis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Keratitis, keratoconjunctivitis, blepharoconjunctivitis (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, bacitracin inhibits bacterial cell wall synthesis by blocking dephosphorylation of C55-isoprenyl pyrophosphate. It is mainly active against Gram-positive bacteria and is used in ophthalmic ointments.

The predicted indication lies very close to the original ones, since all are inflammatory conditions of the cornea and conjunctiva. This closeness likely explains the very high model score. However, punctate epithelial keratoconjunctivitis is often viral or non-infectious, in which case an antibacterial agent may offer little benefit. The mechanism would only be relevant if bacterial infection or secondary infection were present.

Other predictions for this drug are weaker or are model artifacts. For example, "non-human animal disease" is a non-specific category, and indications such as Chagas cardiomyopathy and infection-related hemolytic uremic syndrome have no plausible mechanistic basis. The only prediction with any literature support is otitis externa (rank 4, evidence level L4). That support is indirect, coming mostly from combination-product studies and a veterinary susceptibility study.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M004 | Bacitracin (A-S Medication Solutions) | Ointment | Not specified (cancelled) |
| 333B | Bacitracin (Preferred Pharmaceuticals, Inc) | Ointment | Not specified (cancelled) |
| ANDA061212 | Bacitracin (Padagis US LLC) | Ointment | Not specified (cancelled) |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: The drug-disease contraindication data flag several conditions, including:
  - eye conditions: herpes simplex virus keratitis, viral eye infection, fungal eye infection, conjunctivitis, open-angle glaucoma and ocular hypertension
  - kidney disease and liver disease
  - neuromuscular conditions: myasthenia gravis and neuromuscular junction disease
  - cardiac conduction disorders: atrioventricular block
  - metabolic and endocrine conditions: diabetes, diabetic ketoacidosis and adrenocortical insufficiency
  
  Some of these entries (for example glaucoma and skin atrophy) look like they may come from other drugs in the same knowledge graph, so they should be verified against the actual label. The listing of conjunctivitis and eye infection is notable because it overlaps with the proposed ophthalmic use.
- **Drug Interactions**: 84 interactions were recorded. The major-level interactions include:
  - aminoglycosides: kanamycin, neomycin and streptomycin
  - deferasirox
  - iodinated contrast agents: diatrizoate, iodipamide, iodixanol and iohexol
  
  Moderate-level interactions include mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, exenatide and picosulfuric acid. Systemic bacitracin is nephrotoxic, which is likely why nephrotoxic and ototoxic agents appear on this list.

Please refer to the package insert for label warnings and contraindications, since these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (evidence level L5), with no trials or publications. The condition is frequently viral or non-infectious, and all US licenses for the drug are cancelled.

**To proceed, the following is needed:**
- Retrieval and review of the FDA package insert (warnings and contraindications), which is currently a blocking data gap
- Mechanism of action data from DrugBank
- Clinical evidence that punctate epithelial keratoconjunctivitis in the target population has a bacterial component
- Evaluation of whether any currently marketed ophthalmic bacitracin product exists, given that all three US licenses are cancelled
- Verification of the knowledge-graph contraindication signals against the label, particularly the eye infection entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

