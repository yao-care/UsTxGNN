---
layout: default
title: Latanoprostene Bunod
parent: Model Prediction Only (L5)
nav_order: 840
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Latanoprostene Bunod: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "LATANOPROSTENE BUNOD"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "idiopathic spontaneous coronary artery dissection", "angiodysplasia of stomach", "lymphangiectasis", "hemangioendothelioma"]
---

# Latanoprostene Bunod
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

## Latanoprostene Bunod: From Open-Angle Glaucoma and Ocular Hypertension to Visceral Calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Latanoprostene bunod is an ophthalmic prostaglandin analog and nitric oxide-donating drug, originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (1 NDA and 1 ANDA, both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Based on known information, latanoprostene bunod is converted into latanoprost acid (a prostaglandin F2-alpha analog acting on the FP receptor) and nitric oxide (NO). Its efficacy in lowering intraocular pressure is established: it increases aqueous humor outflow through the uveoscleral pathway and the trabecular meshwork.

The link to visceral calciphylaxis is weak. NO-mediated vasodilation and cGMP signaling could theoretically influence vascular calcification, but this is a hypothesis only. Calciphylaxis is a systemic microvascular disease, while this drug is a topical eye drop with negligible systemic exposure. The high TxGNN score is a computational prediction and should not be read as clinical support.

For context, the other top-ranked predictions are also weakly supported:
- **Primary hereditary glaucoma** (99.71%) is the most mechanistically plausible, but it is an extension of the approved glaucoma class rather than true repurposing. Pediatric and developmental glaucomas often respond poorly to medical therapy and would need separate evaluation.
- **Thoracic outlet syndromes** (venous, arterial and neurogenic), **spontaneous coronary artery dissection**, **angiodysplasia of the stomach**, and **lymphangiectasis** have no identified mechanistic link, and each has no trials or literature.
- **Vascular disease** and **hemangioendothelioma** have minimal indirect evidence, described below.

## Clinical Trial Evidence

No clinical trials are registered for visceral calciphylaxis. Currently no related clinical trials registered.

For reference, the only trial linked to any of the top 10 predictions is for "vascular disease" (rank 6), and its relevance is indirect:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03931317](https://clinicaltrials.gov/study/NCT03931317) | Not applicable | Completed | 70 | Randomized, masked crossover study comparing latanoprostene bunod and timolol on eye pressure and retinal blood vessel density in ocular hypertension or primary open-angle glaucoma. It is an ocular study, not a test of a systemic vascular disease. |

## Literature Evidence

No publications are available for visceral calciphylaxis. Currently no related literature available.

For reference, the only publications linked to other top-10 predictions are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30028313](https://pubmed.ncbi.nlm.nih.gov/30028313/) | 2018 | Review | Neural Regeneration Research | Overview of treatment options for glaucomatous optic neuropathy (linked to "vascular disease"). Indirect relevance. |
| [38113361](https://pubmed.ncbi.nlm.nih.gov/38113361/) | 2023 | Case report | Ophthalmic Surgery, Lasers & Imaging Retina | An 11-year-old girl with a port-wine birthmark, diffuse choroidal hemangioma and glaucoma developed serous retinal detachment on prostaglandin analog therapy (bimatoprost, then latanoprostene bunod). Vision and the detachment improved after stopping the drug. This is an adverse event, not evidence of benefit (linked to "hemangioendothelioma"). |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA207795 | Vyzulta (Bausch & Lomb Incorporated) | Ophthalmic solution/drops | Not listed; cancelled |
| ANDA217387 | Latanoprostene Bunod Ophthalmic Solution, 0.024% (Gland Pharma Limited) | Ophthalmic solution/drops | Not listed; cancelled |

Both authorizations are in cancelled status, and there are no currently valid single-ingredient or combination licenses. The drug was approved by the FDA in November 2017 for open-angle glaucoma and ocular hypertension.

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology record: latanoprostene bunod acts on the prostanoid FP receptor (PTGFR). No clinically graded drug-drug interactions were reported.
- **Signal from the literature**: A case report describes serous retinal detachment in a child with a port-wine birthmark and choroidal hemangioma after prostaglandin analog therapy, which may signal caution in patients with ocular vascular anomalies.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for visceral calciphylaxis rests on model output alone (L5), with no trials or publications. The mechanistic link is speculative, and a topical ocular product has negligible systemic exposure for a systemic microvascular disease. None of the other top-ranked predictions has direct supporting evidence either.

**To proceed, the following is needed:**
- Detailed mechanism of action data, to assess whether NO/cGMP and FP receptor signaling are relevant to vascular calcification
- Package insert warnings and contraindications (currently missing, and a blocking gap for safety screening)
- Preclinical evidence that this drug affects calcification or calciphylaxis models
- Evidence that a systemic route or formulation could achieve relevant exposure, since only an ophthalmic solution exists
- Separate evaluation of primary hereditary glaucoma in a pediatric or developmental glaucoma context, as it is the most plausible prediction
- Clarification of the regulatory status, since both US licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

