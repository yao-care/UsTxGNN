---
layout: default
title: Levobunolol
parent: Model Prediction Only (L5)
nav_order: 852
evidence_level: L5
indication_count: 3
---

# Levobunolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Levobunolol: From Ocular Hypertension/Open-Angle Glaucoma (Inferred) to Primary Hereditary Glaucoma

## One-Sentence Summary

Levobunolol is a non-selective beta-blocker eye drop. The published literature shows it is used to lower intraocular pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma** (score 99.98%), but **no trials or publications** were found for that exact term.
The related entries "glaucoma 1, open angle" and "open angle glaucoma" have about **20 publications each** and no registered trials. These look like an existing approved use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license record; the literature indicates ocular hypertension and chronic open-angle glaucoma |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 for the predicted term (no direct studies); provisional L1 for the open-angle glaucoma entries (published randomized trials, no registry records, full-text confirmation needed) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (ANDA074326) |
| Recommended Decision | Hold (for the headline term); Proceed with Guardrails for the open-angle glaucoma entries |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database record. From the literature, levobunolol is a potent non-selective beta-adrenoceptor blocker. It lowers intraocular pressure by reducing aqueous humor production, probably through beta-receptors on the ciliary epithelium.

Primary hereditary glaucoma is a broad label for glaucoma that runs in families. Lowering intraocular pressure is the shared treatment goal across glaucoma types, so the mechanism is plausible. However, the very high TxGNN score most likely reflects the term's closeness to the open-angle glaucoma nodes in the knowledge graph. It is not independent evidence. The term is also a broad or parent-level label, and no studies were retrieved under it.

The open-angle glaucoma literature (mostly head-to-head comparisons with timolol and studies of up to 4 years) points to an established use, not a new one. The license record has no indication text, so this should be confirmed against the current US label.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for "primary hereditary glaucoma" itself. The table below lists the most relevant publications retrieved under the closely related "glaucoma 1, open angle" and "open angle glaucoma" entries. Study types are taken from the retrieved titles and abstracts and need full-text confirmation.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3881032](https://pubmed.ncbi.nlm.nih.gov/3881032/) | 1985 | RCT (levobunolol vs timolol) | Am J Ophthalmol | 162 patients; 0.5% and 1% levobunolol lowered IOP by about 8 mm Hg, with no significant difference from 0.5% timolol |
| [2664628](https://pubmed.ncbi.nlm.nih.gov/2664628/) | 1989 | 4-year randomized, double-masked study | Ophthalmology | 391 patients; IOP fell by 7.1-7.2 mmHg with levobunolol and 7.0 mmHg with timolol, with little loss of effect over 4 years |
| [2865710](https://pubmed.ncbi.nlm.nih.gov/2865710/) | 1985 | Long-term double-masked study | Ophthalmology | 391 patients for up to 2 years; both levobunolol concentrations reduced mean IOP by about 27%, and the effect was sustained |
| [3912600](https://pubmed.ncbi.nlm.nih.gov/3912600/) | 1985 | Comparative trial | Klin Monbl Augenheilkd | 50 patients for 1 year; levobunolol was as effective as timolol, and heart rate fell similarly in both, suggesting systemic absorption |
| [8145982](https://pubmed.ncbi.nlm.nih.gov/8145982/) | 1994 | Randomized, double-masked trial | Ophthalmologica | 59 patients; 0.5% levobunolol lowered IOP by 7.3 mm Hg vs 4.1 mm Hg with 2% carteolol (p = 0.0004) |
| [8123096](https://pubmed.ncbi.nlm.nih.gov/8123096/) | 1993 | RCT (levobunolol vs dipivefrin) | J Ocul Pharmacol | Compared levobunolol with dipivefrin in 38 African American patients with open-angle glaucoma |
| [2883990](https://pubmed.ncbi.nlm.nih.gov/2883990/) | 1987 | Randomized, double-masked trial | Br J Ophthalmol | 46 patients; levobunolol 0.5% and metipranolol 0.6% both lowered IOP by about 7 mmHg |
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic review / network meta-analysis | Ophthalmology | Compares first-line medical treatments for primary open-angle glaucoma and ocular hypertension |
| [2892662](https://pubmed.ncbi.nlm.nih.gov/2892662/) | 1987 | Review | Drugs | Levobunolol 0.5-1% reduced IOP by about 30%, controlled 50-85% of patients, and was superior to placebo and comparable to timolol |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Review | Med Lett Drugs Ther | Recent overview of drugs for open-angle glaucoma (no abstract available) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA074326 | Levobunolol Hydrochloride (Bausch & Lomb Incorporated) | Solution/drops (ophthalmic) | Not stated in the available record |

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the record. Please refer to the package insert for safety information.

Observations from the retrieved literature:
- **Systemic absorption**: A one-year study found that topical levobunolol and timolol decreased heart rate to a similar extent, which suggests absorption after eye-drop use (PMID 3912600). This is a known concern for non-selective beta-blockers.
- **Ocular surface**: One study examined conjunctival changes induced by preserved and unpreserved levobunolol (PMID 18465723).

---

## Conclusion and Next Steps

**Decision: Hold** (for "primary hereditary glaucoma"). For the open-angle glaucoma entries, **Proceed with Guardrails** applies.

**Rationale:**
- There are no trials or publications for primary hereditary glaucoma, and the TxGNN score likely reflects graph proximity to open-angle glaucoma.
- The open-angle glaucoma evidence is extensive, with multiple randomized comparisons against timolol and follow-up of up to 4 years. It most likely describes an existing use, not a repurposing opportunity.

**To proceed, the following is needed:**
- The US package insert (indications, warnings, contraindications), since the license record has no indication text
- Confirmation of on-label status for open-angle glaucoma and ocular hypertension
- Full-text review to confirm randomization and design for the studies graded L1
- Evidence specific to primary hereditary glaucoma (for example, familial or juvenile forms), if that is the intended target
- Detailed mechanism of action data and a drug interaction assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

