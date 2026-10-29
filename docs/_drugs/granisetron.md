---
layout: default
title: Granisetron
parent: Model Prediction Only (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
monitor_inn: "GRANISETRON"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
last_modified_at: 2026-10-30
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not stated in the compiled regulatory data (granisetron is generally…"
---

# Granisetron
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

## Granisetron: From Chemotherapy-Associated Nausea and Vomiting to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist. The data compiled for this report do not list an approved indication text, but the drug is widely known as an antiemetic.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled regulatory data (granisetron is generally known as an antiemetic for chemotherapy-induced nausea and vomiting) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 8 of 10) |
| Number of NDAs | 10 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known pharmacology, granisetron is a selective 5-HT3 receptor antagonist, and its efficacy in nausea and vomiting is established through blockade of serotonin signaling.

Mechanistically, 5-HT3 modulation has been hypothesized to influence dopaminergic and serotonergic signaling relevant to mood disorders. This link is speculative. The very high TxGNN score (0.9962) is a model prediction only, and no clinical trials or literature were found to support it. The original indication (nausea and vomiting) and the predicted indication (mania) are not closely related clinically, so the similarity between them has not yet been assessed.

### Other Predicted Indications

The model also produced nine other predictions. None has clinical trial or literature support, and all are rated L5 with a Hold recommendation.

| Rank | Predicted Indication | TxGNN Score | Mechanistic Plausibility |
|------|------|------|------|
| 2 | Tourette syndrome | 0.9952 | Plausible but unproven: 5-HT3 antagonism may modulate basal ganglia dopamine release |
| 3 | Acute contagious conjunctivitis | 0.9949 | No clear link: the disease is pathogen-driven; the score likely reflects similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence |
| 4 | Angioedema | 0.9936 | Weak: possible role in neurogenic inflammation; hypersensitivity to 5-HT3 antagonists is a concern |
| 5 | Allergic urticaria | 0.9932 | Weak: serotonin may contribute to pruritus, but antihistamines remain standard |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 0.9932 | None apparent: caused by AVPR2 gain-of-function mutations; likely an artifact |
| 7 | Trichotillomania | 0.9923 | Plausible but unproven: OCD-spectrum disorder with serotonergic involvement |
| 8 | Bronchitis | 0.9918 | Speculative: vagal afferents express 5-HT3 receptors |
| 9 | Cold urticaria | 0.9910 | Indirect: mast cell signaling or pruritus |
| 10 | Conjunctivitis | 0.9909 | Weak: no demonstrated ocular activity; overlaps with rank 3 |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA022445 | SUSTOL (Heron Therapeutics) | Injection | NDA (Discontinued in Drugs@FDA) |
| NDA022198 | SANCUSO (Cumberland Pharmaceuticals) | Patch | Valid |
| ANDA091136 | Granisetron Hydrochloride (Mylan Institutional) | Injection, solution | Valid |
| ANDA204238 | Granisetron Hydrochloride (Eugia US) | Injection, solution | ANDA (Discontinued in Drugs@FDA) |
| ANDA219282 | Granisol (Intra-Sana Laboratories) | Solution | Valid |

The compiled records contain no approved indication text for these licenses. Five more licenses (all cancelled) are on file, covering tablets, film-coated tablets and additional injections.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease, sudden cardiac arrest, heart conduction disease. These point to a QT-prolongation and arrhythmia concern.
- **Drug Interactions**: 100 interactions were found. The first 20 retrieved include these major ones:
  - **Opioids and serotonergic agents**: fentanyl, alfentanil, tramadol, dextromethorphan (serotonergic or additive risk)
  - **Triptans**: almotriptan, sumatriptan
  - **QT-prolonging or antiarrhythmic agents**: amiodarone, amisulpride, amitriptyline, anagrelide
  - Moderate interactions include abiraterone, famotidine, formoterol, salbutamol, adenosine, propofol, codeine, dihydrocodeine, alfuzosin and abametapir (topical).
- **Hypersensitivity**: reactions to 5-HT3 antagonists have been reported, which matters especially for angioedema and urticaria predictions.

Please refer to the package insert for complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (manic bipolar affective disorder) has a very high model score but no supporting clinical trials or literature (Evidence Level L5). The drug is marketed in the US, with 10 valid licenses out of 10, and the mechanistic link is speculative. QT-related safety signals and many major drug interactions add further caution, especially in a psychiatric population that often takes QT-prolonging drugs.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA (needed for safety screening)
- Detailed mechanism of action data
- A systematic search of clinical trials and literature for granisetron or other 5-HT3 antagonists in mania, bipolar disorder, and Tourette syndrome or trichotillomania
- A QT-risk and drug-interaction assessment for the target population
- Clarification of the original approved indication and of route and formulation compatibility with the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

