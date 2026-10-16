---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 1290
evidence_level: L5
indication_count: 10
monitor_inn: "VILAZODONE"
predicted_indications: ["dysthymic disorder", "neurotic disorder", "neurotic depression", "melancholia", "obsessive-compulsive disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "Keppen-Lubinsky syndrome", "Ohdo syndrome and variants", "schizoid personality disorder"]
last_modified_at: 2026-10-14
description: "Vilazodone: predicted new indication Dysthymic disorder (evidence level L5). Approved use: Major depressive disorder"
---

# Vilazodone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Vilazodone: From Depression to Dysthymic Disorder

## One-Sentence Summary

Vilazodone is an antidepressant that combines serotonin reuptake inhibition with 5-HT1A partial agonism, originally used for major depressive disorder and related depressive and anxiety conditions.
The TxGNN model predicts it may be effective for **Dysthymic Disorder** (persistent depressive disorder).
However, **no clinical trials and no publications** were retrieved for this specific indication, so the support is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (also unipolar depression, endogenous depression, anxiety disorder, per the knowledge graph; the US license records contain no indication text) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (all 6 licenses are cancelled) |
| Number of NDAs | 6 licenses in total (1 NDA and 5 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, vilazodone is a serotonin reuptake inhibitor and a 5-HT1A receptor partial agonist. It is approved in the US for major depressive disorder in adults.

Dysthymic disorder is a chronic, milder form of depression and is biologically close to major depressive disorder. A drug that works through serotonergic pathways could plausibly help in chronic depressive states as well.

The very high TxGNN score (99.79%) is a computational prediction. It is not backed by trials or publications for dysthymic disorder, so it should be treated as a hypothesis rather than as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dysthymic disorder.

For context, other predicted indications had very little trial evidence. The only trial found across the top 10 predictions was NCT01916824 (Phase 4, completed, n=53), a decision-making study in major depression listed under melancholia. It is only indirectly relevant and was not shown to involve vilazodone.

---

## Literature Evidence

Currently no related literature available for dysthymic disorder.

General vilazodone literature exists for major depression. Examples include a 2022 review (PMID 35726313, "Vilazodone for Major Depression in Adults"), which describes four positive short-term (8–10 weeks) placebo-controlled trials in adults with major depressive disorder. This supports the original indication, not the predicted one.

---

## US Market Information

All six licenses are cancelled, so no valid license is currently listed. Indication text is not available in the license records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022567 | VIIBRYD (Allergan, Inc.) | Tablet | Not listed (cancelled) |
| ANDA208200 | Vilazodone hydrochloride (Cipla USA Inc.) | Tablet, film coated | Not listed (cancelled) |
| ANDA208212 | Vilazodone Hydrochloride (Teva Pharmaceuticals, Inc.) | Tablet, film coated | Not listed (cancelled) |
| ANDA208202 | Vilazodone Hydrochloride (Alembic Pharmaceuticals Limited) | Tablet, film coated | Not listed (cancelled) |
| ANDA208228 | Vilazodone hydrochloride (Northstar Rx LLC) | Tablet | Not listed (cancelled) |

One further license (ANDA208209, Accord Healthcare Inc., tablet) is also cancelled.

---

## Safety Considerations

**Contraindications from the knowledge graph** (derived from drug-disease relationships, not from label text): epilepsy, bipolar disorder, major affective disorder, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome (SIADH), nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.

**Drug Interactions:** 100 interactions were recorded. The major-level ones among those listed include:
- Bupropion
- Lorcaserin
- Clarithromycin
- Diethylpropion
- Dolasetron
- Palonosetron
- Phentermine

Moderate-level interactions include pioglitazone, aprepitant, morphine, acetylsalicylic acid (aspirin), dexamethasone, glimepiride and several insulins. The aspirin signal is consistent with the bleeding-related contraindication flag.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, since dysthymic disorder is close to the approved depressive indication. However, there are no trials or publications for it, and the evidence level is L5. The predicted indication also overlaps heavily with the existing one, which limits the repurposing value.

**To proceed, the following is needed:**
- Retrieval of the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted search for vilazodone studies in dysthymia or persistent depressive disorder
- Confirmation of why all US licenses are cancelled and of the current regulatory status
- If pursued, a pilot or Phase 2 trial in persistent depressive disorder

**Other predictions in the top 10:** Obsessive-compulsive disorder is the only one rated as a research question (L4). Class-level evidence supports serotonergic antidepressants in OCD, but nothing is specific to vilazodone. Neurotic depression and melancholia (L4) are relabelings or subtypes of the existing indication. Several predictions (benign paroxysmal torticollis of infancy, Keppen-Lubinsky syndrome, Ohdo syndrome) have no plausible mechanistic link and are likely graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

