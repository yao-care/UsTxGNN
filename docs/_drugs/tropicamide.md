---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 1269
evidence_level: L5
indication_count: 3
monitor_inn: "TROPICAMIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Tropicamide
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

# Tropicamide: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting topical antimuscarinic eye drop, originally used for cycloplegia and pupil dilation during eye examinations.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all ANDA, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tropicamide is a topical antimuscarinic (anticholinergic) agent. Pharmacology data show it binds muscarinic receptors M2, M3, M4 and M5, and it is used as a short-acting mydriatic for examining the lens, vitreous humor and retina.

The possible link to cauda equina syndrome is indirect. Antimuscarinic drugs can suppress detrusor overactivity, so a drug of this class could in theory help with bladder dysfunction secondary to cauda equina syndrome. However, cauda equina syndrome is mainly a surgical emergency treated by decompression. Any drug role would be limited to symptomatic bladder management, not treatment of the underlying nerve root compression.

There are also practical limits. Tropicamide is formulated only as an ophthalmic solution with minimal systemic exposure, so reaching meaningful levels in the bladder at topical doses is unlikely. The very high model score (0.995) is a computational prediction only.

Two other predictions from the same model show the same pattern, both with no trials or literature and both rated Hold:
- **Obsolete neurogenic bladder** (score 99.13%): the class rationale is coherent (antimuscarinics such as oxybutynin are established), but tropicamide has low systemic absorption and a short duration of action, and the disease term is obsolete in the ontology.
- **Irritable bowel syndrome** (score 99.12%): antispasmodic antimuscarinics such as dicyclomine are used, but tropicamide has no oral formulation, negligible gut exposure, and better-characterized alternatives exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA040064 | Tropicamide (Bausch & Lomb) | Ophthalmic solution/drops | Cancelled |
| ANDA084306 | Mydriacyl (Alcon) | Ophthalmic solution/drops | Cancelled |
| ANDA040067 | Tropicamide (Bausch & Lomb) | Ophthalmic solution/drops | Cancelled |
| ANDA207524 | Tropicamide (Sportpharm) | Ophthalmic solution/drops | Cancelled |
| ANDA084305 | Tropicamide (Sandoz) | Ophthalmic solution/drops | Cancelled |

Approved indication text is not available for these authorizations. All five are cancelled, and none is currently valid.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (contraindication edges, not label text):** hypertension and hypertensive disorder, open-angle glaucoma, angle-closure (closed-angle) glaucoma, ocular hypertension, diabetes mellitus, diabetic ketoacidosis, sudden cardiac arrest, heart conduction disease, hyperthyroidism, Graves disease, thyrotoxicosis, myocardial ischemia, and coronary artery disease.
- **Drug Interactions:** 14 records were found. Ten are drug-drug interactions with no severity level assigned: atropine, potassium chloride, vancomycin, simvastatin, prednisolone, famotidine, warfarin, lidocaine, fluconazole, and brimonidine. Atropine is the most pharmacologically plausible (additive antimuscarinic effects). The remaining four records are muscarinic receptor targets (M2, M3, M4, M5), which are binding targets rather than interactions.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications. Tropicamide is a topical ophthalmic drug with minimal systemic exposure, so reaching bladder, gut or nerve targets is implausible. In addition, all US licenses are cancelled, and the disease would be treated surgically, with any drug role limited to symptoms.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Evidence that a systemically active formulation could reach relevant tissues safely
- Preclinical or clinical data for any of the predicted indications
- A review of whether existing antimuscarinics already cover the bladder-symptom use, which would make tropicamide redundant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

