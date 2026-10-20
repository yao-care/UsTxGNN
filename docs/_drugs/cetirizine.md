---
layout: default
title: Cetirizine
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Cetirizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis (other listed indications include vasomotor rhiniti…"
monitor_inn: "CETIRIZINE"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "rosacea conjunctivitis", "recalcitrant atopic dermatitis"]
---

# Cetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation H1-antihistamine, originally used for allergic rhinitis, conjunctivitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **Allergic Urticaria**,
with **1 clinical trial** (a small Phase 3-labeled pilot study) and **18 publications** currently supporting this direction. Most of the publications are reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other listed indications include vasomotor rhinitis, conjunctivitis, idiopathic urticaria) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (tentative; see note below) |
| US Market Status | Cancelled only (no currently valid licenses in the data compiled for this report) |
| Number of NDAs | 13 (2 NDAs and 11 ANDAs, all cancelled) |
| Recommended Decision | Proceed with Guardrails |

Note on evidence level: the only trial is a 36-patient pilot feasibility study, not a confirmatory efficacy trial. The L1 label is therefore tentative and rests largely on the Phase 3 label and the supporting literature. By the strict rule (at least two completed Phase 3 RCTs), a more conservative reading would be L2 or L3.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. However, cetirizine is a well-established selective peripheral H1-receptor antagonist. In allergic urticaria, histamine released from mast cells drives the wheal-and-flare response, so blocking H1 receptors directly targets the core pathway.

The predicted indication is closely related to a labeled use. Idiopathic urticaria is already among cetirizine's original indications, and both conditions share the same histamine-mediated skin pathology. This makes the model's prediction mechanistically coherent, and the very high score (99.99%) is consistent with that overlap.

The other predictions are weaker. Cold urticaria is plausible by the same mechanism but has only small-scale evidence. "Nasal cavity disease" and "acute laryngopharyngitis" probably reflect existing labeled uses. Rosacea conjunctivitis and recalcitrant atopic dermatitis rest on prediction alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Randomized, double-blind pilot comparing IV cetirizine 10 mg with IV diphenhydramine 50 mg in acute urticaria, run in emergency departments, urgent care and allergy clinics. It tested the feasibility of a larger Phase 3 trial and is not a confirmatory efficacy study. The IV route also differs from the oral labeled use. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Cetirizine is effective and well tolerated in seasonal/perennial allergic rhinitis and chronic idiopathic urticaria |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Pharmacology and clinical potential of cetirizine in allergic rhinitis, pollen-induced asthma and chronic urticaria |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of oral antihistamines in allergic rhinitis and chronic idiopathic urticaria |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Non-sedating antihistamines are the mainstay of treatment for chronic idiopathic urticaria |
| [17017922](https://pubmed.ncbi.nlm.nih.gov/17017922/) | 2006 | Review | Curr Med Chem | Levocetirizine (the R-enantiomer of cetirizine) has favourable pharmacology and minimal hepatic metabolism |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Levocetirizine for allergic rhinitis and chronic idiopathic urticaria in adults and children |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Review | Allergy | Clinical studies of cetirizine in allergic rhinitis and chronic urticaria (no abstract available) |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | J Clin Gastroenterol | Cetirizine-induced cholestasis in a 28-year-old man after long-term use. Transient transaminase elevations occurred in under 2% of trial patients |

Most of these publications are reviews of antihistamines in general or of related drugs (fexofenadine, bilastine, rupatadine, ebastine). They support the drug class rather than cetirizine specifically in allergic urticaria.

## US Market Information

All 13 licenses are listed as cancelled in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021621 | Zyrtec | Chewable tablet | Not listed |
| NDA022155 | Children's Zyrtec Allergy | Syrup | Not listed |
| ANDA078343 | Cetirizine Hydrochloride (Dr. Reddy's) | Film-coated tablet | Not listed |
| ANDA213557 | Cetirizine Hydrochloride (Topco) | Orally disintegrating tablet | Not listed |
| ANDA209107 | Cetirizine Hydrochloride (Hives Relief) | Capsule | Not listed |

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not label text):** hypertension, kidney disease (including chronic and end-stage renal failure), liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, glaucoma (including angle-closure), and hyperthyroidism (including Graves disease). These come from a model-derived graph and need verification against the official labeling.
- **Hepatic signal:** a published case report describes cetirizine-induced cholestasis, in line with the knowledge-graph liver-disease flag.
- **Drug Interactions:** 100 interactions were found. The moderate-level ones include bupropion, dronabinol, loperamide, metoclopramide, morphine (including liposomal), nabilone, opium, sibutramine, difenoxin and diphenoxylate. Several of these involve additive central nervous system effects. Others, such as calcitriol, vitamin A, phentermine, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole and acarbose, have an unknown severity level.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for the official safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Allergic urticaria is mechanistically very close to cetirizine's labeled idiopathic urticaria indication, and H1 blockade is a well-established treatment. The only direct trial is a small IV feasibility pilot, and the literature is mostly reviews, so the evidence does not support a full "Go".

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to confirm the knowledge-graph safety flags
- Detailed mechanism of action data
- A confirmatory efficacy trial (the pilot supports feasibility only), with the route of administration clarified
- Confirmation of current US market status, since all licenses appear cancelled
- For the other predictions: cold urticaria is a research question needing larger controlled studies. The remaining four (nasal cavity disease, acute laryngopharyngitis, rosacea conjunctivitis, recalcitrant atopic dermatitis) should be held, as they rest on model prediction or overlap with existing labeled uses.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

