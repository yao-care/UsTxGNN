---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 1192
evidence_level: L5
indication_count: 8
monitor_inn: "Tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-10-14
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Erectile dysfunction, benign prostatic hyperplasia…"
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Tadalafil: From Erectile Dysfunction and Pulmonary Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia, and pulmonary hypertension.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **0 clinical trials** and **0 publications** currently support this direction. The prediction is a model output only, and it may reflect an adverse-effect association rather than a therapeutic one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction, benign prostatic hyperplasia, pulmonary hypertension, psychologic dyspareunia, premature ejaculation (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 11 licenses cancelled) |
| Number of NDAs | 11 (all generic ANDAs; no NDA among them) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Tadalafil is generally known as a PDE5 inhibitor that raises cGMP and causes vasodilation. Its efficacy in erectile dysfunction and pulmonary hypertension is established.

The predicted disease is a congenital condition driven by genetic (chromosomal or regulatory) abnormalities, and a biological link to PDE5 inhibition is not evident. The high score likely comes from knowledge-graph proximity to hypertrichosis-related phenotypes. Hypertrichosis is a known adverse effect of vasodilators such as minoxidil, so the association may point in the wrong direction (inducing rather than treating). The therapeutic rationale is unsupported.

The other top-ranked predictions show the same pattern, and the compiled data provides no evidence for any of them:
- Hypertrichosis (99.98%): likely a shared vasodilatory or cGMP-pathway signal, with an unclear direction of effect.
- Malformation syndrome with odontal and/or periodontal component (99.97%): no plausible mechanism.
- Syndrome with a Dandy-Walker malformation as major feature (99.97%): a structural brain anomaly that a PDE5 inhibitor would not be expected to reverse.
- Isolated genetic hair shaft abnormality (99.96%): no established rationale.
- Familial isolated trichomegaly (99.65%): a genetic trait with no plausible therapeutic mechanism.
- Kyphoscoliotic heart disease (99.43%): the most biologically plausible, because kyphoscoliosis can cause chronic hypoxia and secondary pulmonary hypertension. This is a hypothesis only and has not been tested.
- Migraine with brainstem aura (99.08%): the only evidence is a case report suggesting tadalafil may trigger aura (an adverse-event signal).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the only publication found among the top predictions relates to migraine with brainstem aura (rank 8):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache, an adverse-event signal rather than evidence of benefit |

## US Market Information

All 11 US licenses are listed as cancelled, and none has approved-indication text on record. Five of them are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA205885 | Tadalafil (Teva Pharmaceuticals) | Tablet, film coated | Not available |
| ANDA209654 | Tadalafil (Preferred Pharmaceuticals) | Tablet | Not available |
| ANDA210609 | Tadalafil (Preferred Pharmaceuticals) | Tablet | Not available |
| ANDA211298 | Tadalafil (Proficient Rx) | Tablet, film coated | Not available |
| ANDA209908 | Tadalafil (Camber Pharmaceuticals) | Tablet, film coated | Not available |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** liver failure, epilepsy, aortic stenosis and other aortic valve disease, hypotensive disorder, blood coagulation disease, acute coronary syndrome, myocardial infarction, stroke and other cerebrovascular disorders, sickle cell anemia and other hemoglobinopathies, plasma cell myeloma, leukemia, priapism, Peyronie disease, hearing loss disorders, and hypertrophic cardiomyopathy.
- **Drug Interactions:** 100 interactions were found in total. The main moderate-level ones include aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole, clotrimazole, lorcaserin, sapropterin, troglitazone, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Papaverine is a minor interaction.
- **Additional signal:** A case report linked tadalafil to migraine aura, which should be noted in any neurological indication work.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or publications (Evidence Level L5). The biological rationale is weak, and the signal may reflect an adverse-effect association (hypertrichosis from vasodilation) rather than a therapeutic one. All US licenses are also cancelled, and the official safety label data is missing.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications, needed for safety screening
- A literature review to clarify the direction of effect for hypertrichosis (therapeutic vs. adverse)
- Consider a targeted review of PDE5 inhibitors in secondary pulmonary hypertension, which could assess kyphoscoliotic heart disease, the most plausible of the predictions
- Confirmation of current US market and licensing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

