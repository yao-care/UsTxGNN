---
layout: default
title: Flavoxate
parent: Model Prediction Only (L5)
nav_order: 709
evidence_level: L5
indication_count: 8
monitor_inn: "FLAVOXATE"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "irritable bowel syndrome", "specific developmental disorder", "attention deficit-hyperactivity disorder", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "peptic ulcer disease"]
last_modified_at: 2026-10-14
description: "Flavoxate: predicted new indication Attention deficit hyperactivity disorder, inattentive type (evidence level L5). Approved use: Not stated in the available license data"
---

# Flavoxate
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

# Flavoxate: From Urinary Tract Spasm to Attention Deficit Hyperactivity Disorder, Inattentive Type

## One-Sentence Summary

Flavoxate is a smooth muscle relaxant with antimuscarinic properties. It is generally used for urinary symptoms, but the US license data compiled for this report contain no approved indication text.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder, inattentive type**, but **0 clinical trials** and **0 publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available license data |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (an ANDA, cancelled) |
| Recommended Decision | Hold |

Other predicted indications, all L5 with a Hold recommendation:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Plausibility |
|------|------|------|------|
| 2 | Irritable bowel syndrome | 99.74% | Plausible (the most credible candidate): antispasmodic activity resembles hyoscine and dicyclomine |
| 3 | Specific developmental disorder | 99.56% | No plausible link |
| 4 | Attention deficit-hyperactivity disorder | 99.39% | Doubtful: anticholinergic activity would be expected to impair attention |
| 5 | Cauda equina syndrome | 99.27% | At most symptomatic bladder relief; does not address the underlying compression |
| 6 | Neurogenic bladder (obsolete term) | 99.13% | Plausible: detrusor relaxation overlaps with the symptoms; the term should be updated (e.g., neurogenic detrusor overactivity) |
| 7 | Gastroduodenitis | 99.12% | Theoretical only; no evidence against mucosal inflammation |
| 8 | Peptic ulcer disease | 99.10% | Low priority given modern standard of care |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacological knowledge, flavoxate is a smooth muscle relaxant with antimuscarinic, phosphodiesterase-inhibiting and calcium-antagonizing properties.

For the top-ranked prediction, ADHD (inattentive type), no established mechanistic link is supported. ADHD pathophysiology centres on dopaminergic and noradrenergic dysregulation, and flavoxate is not known to act on these pathways. Anticholinergic activity would more likely impair than improve attention and cognition. The high TxGNN score is probably driven by network-level similarity to anticholinergic or CNS-active drugs rather than by biological evidence. The same reasoning applies to the ADHD (unspecified) and specific developmental disorder predictions.

Among the eight predictions, **irritable bowel syndrome** is the most mechanistically credible. Antimuscarinic antispasmodics such as hyoscine and dicyclomine are already used there. Neurogenic bladder is also plausible, but only as an extension of flavoxate's existing urinary use. Neither has supporting trials or literature in the compiled data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA076835 (cancelled) | Flavoxate Hydrochloride (Epic Pharma, LLC) | Tablet (oral) | Not available |

## Safety Considerations

- **Disease contraindications from the knowledge graph** (derived from drug-disease contraindication edges, not from label text): angle-closure glaucoma, pyloric stenosis, paralytic ileus, intestinal obstruction, familial visceral myopathy, active peptic ulcer disease, urinary tract obstruction. Notably, active peptic ulcer disease is both a listed contraindication and a predicted indication, which is a direct conflict.
- **Drug Interactions**: 74 interactions were identified. Two are rated **Major**, both involving potassium salts (potassium citrate and potassium chloride). Most others are rated Moderate, including other antimuscarinics (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, scopolamine, propantheline), opioids and GI motility-related drugs (morphine, loperamide, eluxadoline, metoclopramide, prucalopride), and cannabinoids (dronabinol, nabilone). Additive anticholinergic effects are the main concern.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All eight predictions are supported only by model scores (L5), with no clinical trials or literature. The top-ranked ADHD predictions lack biological plausibility and conflict with flavoxate's anticholinergic profile. The US license is cancelled, and key safety and mechanism data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A literature and trial search for the more plausible candidates: irritable bowel syndrome and neurogenic detrusor overactivity (using current terminology)
- Assessment of route compatibility and similarity to the original indication, which are still pending
- Clarification of the original approved indication, since no indication text is available in the license data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

