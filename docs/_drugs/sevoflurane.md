---
layout: default
title: Sevoflurane
parent: Model Prediction Only (L5)
nav_order: 1158
evidence_level: L5
indication_count: 10
monitor_inn: "SEVOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
last_modified_at: 2026-10-14
description: "Sevoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not specified in the data compiled for this report (used as an inhale…"
---

# Sevoflurane
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

## Sevoflurane: From General Anesthesia to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Sevoflurane is an inhaled general anesthetic. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials and no publications** currently support this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report (used as an inhaled general anesthetic) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 6 (1 NDA and 5 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, sevoflurane is a volatile anesthetic that has some vasodilatory and calcium-channel-modulating effects. These could theoretically relate to coronary vasospasm, the underlying problem in Prinzmetal angina.

This link is speculative. No supporting data were provided, and the relationship between general anesthesia and a chronic cardiac condition is not established. Sevoflurane is also an inhaled agent given under medical supervision to induce and maintain anesthesia. It is not a practical option for long-term management of a recurrent condition such as vasospastic angina.

The other top predictions (Tourette syndrome, fibromyalgia, tendinitis, trichotillomania, migraine and several myopathies) show the same pattern. They have high model scores but little or no direct clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For context, the next-ranked predictions have only incidental literature. For example, the fibromyalgia report (PMID 26419112) describes sevoflurane used as part of anesthesia in a patient who has the condition. It does not show treatment of the condition. The tendinitis papers are perioperative studies in which sevoflurane is the anesthetic or comparator, and the migraine and inclusion body myositis papers are an anesthesia experience report and a case report. None shows therapeutic benefit.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020478 | Ultane (AbbVie Inc.) | Liquid | Not listed (cancelled) |
| ANDA077867 | Sojourn (Piramal Critical Care Inc) | Liquid | Not listed (cancelled) |
| ANDA075895 | Sevoflurane (Baxter Healthcare Corporation) | Liquid | Not listed (cancelled) |
| ANDA078650 | Sevoflurane (Halocarbon Life Sciences, LLC) | Liquid | Not listed (cancelled) |
| ANDA203793 | Sevoflurane (Sandoz Inc.) | Liquid | Not listed (cancelled) |

One further authorization (ANDA214382, Lannett Company, Inc.) is also cancelled. All six authorizations are cancelled.

## Safety Considerations

- **Disease-related contraindication signals (from a knowledge graph, not label text)**: epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, hypotensive disorder, malignant hyperthermia of anesthesia, exercise-induced malignant hyperthermia, pseudotumor cerebri, intracranial hypertension, Duchenne and Becker muscular dystrophy (muscular dystrophy in general), and proteinuria. Hypotensive disorders are of particular concern for a cardiovascular use.
- **Drug Interactions**: 100 interactions were found. Major-level interactions include **epinephrine**, **dolasetron** and **cisapride**. Many moderate interactions were also found, including famotidine, morphine, loperamide, clarithromycin, levofloxacin, ondansetron, palonosetron, exenatide and several laxatives and bowel-preparation agents.

For label warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials and no supporting literature. Sevoflurane is an inhaled general anesthetic with no plausible route to chronic use in vasospastic angina, and all US authorizations are cancelled. The kidney disease, liver disease and hypotension signals add to the concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Preclinical or mechanistic evidence on coronary vasospasm
- An assessment of whether any feasible route or formulation could suit a chronic cardiac indication
- Clarification of current US availability, since all authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

