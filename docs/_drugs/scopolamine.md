---
layout: default
title: Scopolamine
parent: Model Prediction Only (L5)
nav_order: 1145
evidence_level: L5
indication_count: 6
monitor_inn: "SCOPOLAMINE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
last_modified_at: 2026-10-14
description: "Scopolamine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Motion sickness, peptic ulcer disease, irritable bowel syndrome…"
---

# Scopolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Scopolamine: From Motion Sickness and Anticholinergic Indications to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine is an antimuscarinic drug originally used for conditions such as motion sickness, peptic ulcer disease, irritable bowel syndrome, and cycloplegia.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but **no clinical trials and no publications** currently support this prediction; it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness, peptic ulcer disease, irritable bowel syndrome, allergic rhinitis, uveitis, cycloplegia, and others (from the knowledge graph; no approved indication text in the US license records) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 9 license records (1 NDA, 7 ANDAs, 1 record without a number), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, scopolamine is a non-selective muscarinic antagonist. Blocking muscarinic receptors can reduce detrusor (bladder muscle) overactivity, and that is the link to the bladder dysfunction seen in cauda equina syndrome.

The relationship to the original indications is loose. Scopolamine's known uses are mostly related to reducing smooth muscle spasm and secretions, and to blocking cholinergic signalling in the gut, eye, and vestibular system. Cauda equina syndrome, however, is caused by compression of the nerve roots at the base of the spine and needs surgical decompression. Any effect of scopolamine would at most relieve bladder symptoms, not treat the underlying injury.

The prediction should be read as a model-based hypothesis only.

Other predicted indications were also reviewed. All are at evidence level L5 with no trials or literature:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Obsolete neurogenic bladder (disease) | 99.98% | Mechanism is plausible (antimuscarinics are an established approach for neurogenic detrusor overactivity), but scopolamine has central nervous system effects and better-studied alternatives exist, such as oxybutynin and solifenacin. The disease term is obsolete in the ontology and needs mapping to a current concept. |
| Papillary conjunctivitis | 99.98% | Driven by allergic or mechanical inflammation; no established antimuscarinic role. |
| Atopic conjunctivitis | 99.80% | Mainly IgE/mast cell mediated; antimuscarinic action does not address the core pathology and may cause dry eye. |
| Rosacea conjunctivitis | 99.40% | Antimuscarinics may reduce tear production and worsen dryness; poor mechanistic fit. |
| Vernal conjunctivitis | 99.08% | Th2/mast cell driven; at most symptomatic relief of ciliary spasm. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All nine US license records for scopolamine are cancelled. No approved indication text is available in these records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017874 | Transderm Scop (Baxter Healthcare Corporation) | Patch, extended release | Not listed (cancelled) |
| ANDA215329 | Scopolamine (Bryant Ranch Prepack) | Patch, extended release | Not listed (cancelled) |
| ANDA218384 | Scopolamine (Amneal Pharmaceuticals NY LLC) | Patch, extended release | Not listed (cancelled) |
| ANDA212342 | Scopolamine (Ingenus Pharmaceuticals, LLC) | Patch, extended release | Not listed (cancelled) |
| ANDA217893 | Scopolamine (Zydus Pharmaceuticals USA Inc.) | Patch, extended release | Not listed (cancelled) |

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from drug-disease relationship data, not from package insert text):
hypertension, liver failure and liver disease, hepatic coma, epilepsy, chronic obstructive pulmonary disease, gastric ulcer, anxiety and neurotic disorders, psychotic and other mental disorders, porphyria, kidney disease, pancreatitis, gallbladder disease, thrombocytopenia, neutropenia and agranulocytosis, open-angle glaucoma, diabetes mellitus and diabetic ketoacidosis, and benign prostatic hyperplasia.

Two of these are relevant to the predicted uses. Benign prostatic hyperplasia and urinary retention risk are a concern for any bladder-related use of an antimuscarinic. Glaucoma is a concern for ocular use.

**Drug Interactions:** 100 interactions were found; most of those listed are Moderate. Main ones include:
- Other anticholinergic agents: hyoscyamine, aclidinium, amantadine, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine (additive anticholinergic effects)
- Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol (additive sedation)
- Others: botulinum toxin type A, phenylephrine, acebutolol, acetylcholine, loperamide
- Minor: acetaminophen, hydrochlorothiazide

Please refer to the package insert for label warnings, as they were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or literature (evidence level L5). Cauda equina syndrome is a surgical emergency, so any drug effect would be symptomatic only. All US licenses are cancelled, and the data compiled for this report lack label safety information and mechanism data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- A literature and trial search for scopolamine or antimuscarinics in neurogenic bladder dysfunction related to cauda equina syndrome
- Mapping of the obsolete neurogenic bladder term to a current disease concept
- A comparison with established peripherally acting antimuscarinics, and an assessment of route of administration compatibility (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

