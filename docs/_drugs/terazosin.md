---
layout: default
title: Terazosin
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
---

# Terazosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Terazosin: From Hypertension/BPH to Raynaud Disease

## One-Sentence Summary

Terazosin is a selective alpha-1 adrenergic receptor (α1-AR) blocker, globally established for hypertension and benign prostatic hyperplasia (BPH), though not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **10 conditions** across vascular, neurological, and hair-related disorders.
Of these, **Raynaud disease** emerges as the most actionable candidate — backed by **1 direct clinical study** and the strongest mechanistic rationale — reaching a **"Proceed with Guardrails"** recommendation at evidence level L3.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Benign Prostatic Hyperplasia (global use; not registered in Taiwan) |
| Top Actionable Indication | Raynaud disease |
| TxGNN Prediction Score (Raynaud) | 99.83% |
| Evidence Level | L3 (observational/clinical pilot study) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Proceed with Guardrails** (Raynaud disease) |

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Recommendation |
|------|---------|-------------|---------------|----------|---------------|
| 1 | Hypotrichosis simplex of the scalp | 99.97% | L5 | S0 | Hold |
| 2 | Congenital hypotrichosis milia | 99.97% | L5 | S0 | Hold |
| 3 | Diffuse alopecia areata | 99.96% | L5 | S0 | Hold |
| 4 | Alopecia | 99.95% | L4 | S0 | Research Question |
| 5 | Migraine disorder | 99.92% | L3 | S1 | Research Question |
| 6 | Migraine with brainstem aura | 99.91% | L4 | S1 | Research Question |
| **7** | **Raynaud disease** | **99.83%** | **L3** | **S2** | **Proceed with Guardrails** |
| 8 | Ambras type hypertrichosis universalis congenita | 99.65% | L5 | S0 | Hold |
| 9 | Manic bipolar affective disorder | 99.55% | L5 | S0 | Hold |
| 10 | Kyphoscoliotic heart disease | 99.49% | L5 | S0 | Hold |

> **Note:** Ranks 1–3 and 8 (hair quantity disorders) are flagged as ontology spillover — TxGNN places them in graph proximity to alopecia-related nodes, but α1-AR pharmacology has no direct mechanistic link to structural hair or keratin gene defects. These are artifact predictions.

---

## Why is This Prediction Reasonable?

Terazosin belongs to the quinazoline class of selective α1-adrenergic receptor antagonists. By blocking postsynaptic α1-AR in vascular smooth muscle, it prevents norepinephrine-induced vasoconstriction, resulting in vasodilation and blood pressure reduction. In BPH, the same mechanism relaxes smooth muscle in the prostate and bladder neck, improving urinary flow.

Raynaud disease is mechanistically the most direct translation of this pharmacology. The condition is defined by episodic peripheral vasospasm — triggered by cold or emotional stress — driven by excessive sympathetic α1-AR activation in digital arteries and arterioles. Blocking α1-AR directly interrupts this spasm cascade, restoring perfusion to fingers and toes. This is not extrapolation; it is the same receptor, the same tissue response, in a different clinical context. Related drugs in the same class — prazosin and doxazosin — already have documented clinical use in Raynaud's phenomenon, establishing a class-level precedent.

For migraine (ranks 5–6), the rationale is more speculative: α1-AR activation in extracranial vessels may contribute to the vascular component of migraine, and terazosin's vasodilatory effect could theoretically blunt this. However, modern migraine pathophysiology centers on CGRP signaling and trigeminal neurovascular activation, making α1 blockade a peripheral and incomplete mechanism. The alopecia cluster (ranks 1–4) represents TxGNN graph topology artifacts for the genetic/structural subtypes (L5), with only a weak indirect hypothesis for the generic "alopecia" node — scalp microvascular expansion is biologically plausible but has never been tested.

---

## Literature Evidence — Raynaud Disease

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Clinical Study (open-label pilot) | Minerva cardioangiologica | Terazosin significantly reduced the number, intensity, and duration of vasospastic attacks in both idiopathic and secondary Raynaud's phenomenon; telethermography and ultrasonography findings also improved |

---

## Literature Evidence — Migraine Disorder

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Clinical Study (non-randomized pilot) | La Clinica terapeutica | Open trial in 46 migraine-without-aura patients; terazosin group (n=10) showed prophylactic activity against paroxysmal headache; also studied buflomedil and combination |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review / Commentary | Headache | Personal experience series (n=10) placing patients on terazosin or doxazosin; 9/10 showed reduction in migraine frequency or severity; 5 discontinued due to side effects (mainly dizziness/orthostatic hypotension) |

---

## Literature Evidence — Alopecia

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Narrative Review | Current Cardiology Reviews | Review of extracardiac effects of cardiovascular medications; mentions minoxidil's hirsutism side effect as a drug repurposing example — does not directly study terazosin for alopecia; included as contextual background on vasodilator-hair follicle biology |

---

## Clinical Trial Evidence

No registered clinical trials were identified for terazosin in any of the 10 predicted indications.

---

## Taiwan Market Information

Terazosin is not currently registered in Taiwan (0 approved licenses). Safety and prescribing information should be obtained from the originator's global package insert (Hytrin® / Abbott Laboratories).

---

## Safety Considerations

No Taiwan-specific package insert data, drug interaction data, or formal contraindication records were retrieved in this Evidence Pack.

> Please refer to the originator's package insert (Hytrin® global label) for complete safety information, including warnings on first-dose orthostatic hypotension, syncope risk (especially in combination with PDE5 inhibitors), and use in patients with hepatic impairment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails — for Raynaud disease only**

**Rationale:**
Terazosin's mechanism of α1-AR blockade directly addresses the sympathetically-driven vasospasm that defines Raynaud disease, and a published clinical pilot demonstrates measurable benefit in both idiopathic and secondary forms. Class-level evidence from prazosin and doxazosin further supports feasibility.

**To proceed, the following is needed:**

- **Controlled trial design:** The existing evidence (PMID 9273472) is open-label with no control arm; a randomized, placebo-controlled crossover study is required to establish efficacy
- **Dose optimization:** Raynaud management doses for other α1 blockers are typically lower than antihypertensive doses; appropriate dosing for terazosin needs prospective evaluation
- **Taiwan regulatory pathway:** Terazosin has no Taiwan license; regulatory strategy (off-label use protocol vs. NDA filing) must be defined before clinical application
- **Orthostatic hypotension monitoring plan:** The most clinically significant safety concern — patients with Raynaud often have lower baseline blood pressure; fall-risk protocol needed
- **Comparison arm consideration:** Calcium channel blockers (nifedipine) are first-line for Raynaud's; any study should benchmark against current standard of care
- **MOA data retrieval:** Full DrugBank pharmacology record should be obtained to confirm receptor selectivity profile and complete the mechanistic documentation

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

