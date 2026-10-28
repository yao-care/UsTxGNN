---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
monitor_inn: "BACITRACIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
last_modified_at: 2026-10-27
description: "Bacitracin: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Bacitracin: Topical polypeptide antibiotic (cell wall synthesis inhibitor) → punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Bacitracin is a topical polypeptide antibiotic that blocks bacterial cell wall synthesis and is supplied as an ointment.
The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** directly support this prediction at present.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 3) |
| Number of NDAs | at least 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bacitracin inhibits bacterial cell wall synthesis by blocking dephosphorylation of C55-isoprenyl pyrophosphate. It is active mainly against Gram-positive organisms and is used topically, in ointment form.

The predicted disease is an inflammatory condition of the cornea and conjunctiva, which sits close to the eye conditions for which bacitracin ointments have been used. That proximity is the main reason the model's prediction is plausible.

There is an important caveat. Punctate epithelial keratoconjunctivitis is frequently viral or non-infectious in origin, so an antibacterial mechanism may not address the underlying cause. At best, bacitracin might help prevent or treat secondary bacterial infection. Detailed mechanism-of-action data were not available in the data compiled for this report, and the rationale above rests on general knowledge of the drug class.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this specific disease.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M004 | Bacitracin (A-S Medication Solutions) | Ointment | Not recorded |
| 333B | Bacitracin (Preferred Pharmaceuticals, Inc) | Ointment | Not recorded |
| ANDA061212 | Bacitracin (Padagis US LLC) | Ointment | Not recorded |

The data compiled for this report are partial, so this list may not be complete.

## Safety Considerations

- **Disease-level cautions (not label text):** The data compiled for this report flag several conditions as potential cautions, including herpes simplex virus keratitis, viral and fungal eye infections, ocular hypertension and open-angle glaucoma, kidney disease, myasthenia gravis and other neuromuscular junction disorders, liver disease, and diabetes. These should be confirmed against the official package insert.
- **Drug Interactions:** 84 interactions are recorded. Those rated **Major** include:
  - Kanamycin, neomycin and streptomycin (aminoglycosides)
  - Deferasirox
  - Iodinated contrast agents (diatrizoate, iodipamide, iodixanol, iohexol)

  Moderate interactions include mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, exenatide and picosulfuric acid.

Warnings and contraindications from the package insert were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model, with no trials or publications addressing this disease. The disease is often viral or non-infectious, which weakens the antibacterial rationale.

**To proceed, the following is needed:**
- Clinical or observational evidence in punctate epithelial keratoconjunctivitis, including how often bacterial involvement occurs
- Mechanism-of-action data and a clearer link between bacitracin and the disease
- Package insert warnings and contraindications, especially for ophthalmic use
- A route and formulation check for ophthalmic delivery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

