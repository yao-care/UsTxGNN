---
layout: default
title: Phenoxybenzamine
parent: Model Prediction Only (L5)
nav_order: 1039
evidence_level: L5
indication_count: 2
---

# Phenoxybenzamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenoxybenzamine: From Pheochromocytoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Phenoxybenzamine is an irreversible, non-selective alpha-adrenergic blocker, originally used for pheochromocytoma and related adrenal and paraganglioma tumours.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** (and, as a second prediction, open-angle glaucoma),
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pheochromocytoma (adrenal gland pheochromocytoma), sympathetic paraganglioma and related tumours (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, phenoxybenzamine is an irreversible, non-selective alpha-adrenergic antagonist. Its use in pheochromocytoma is consistent with blocking catecholamine-driven vasoconstriction and hypertension.

In principle, alpha blockade could affect aqueous humor dynamics, for example through changes in ocular vascular tone or uveoscleral outflow. This gives a theoretical link to intraocular pressure regulation. Adrenergic modulation is a recognised route in glaucoma care: alpha-2 agonists such as brimonidine lower intraocular pressure.

However, the link is weak and speculative:
- Primary hereditary glaucoma (congenital and juvenile forms) is driven mainly by developmental or genetic defects of the trabecular meshwork and anterior chamber angle (for example, CYP1B1 or MYOC variants). Alpha blockade is not expected to correct these structural defects.
- For open-angle glaucoma, the second prediction (score 99.48%), the direction of effect is not established. Systemic alpha blockade may lower ocular perfusion pressure, which could be unfavourable for the optic nerve.
- Many established topical glaucoma therapies already exist, which limits the need for a systemic oral agent with significant side effects.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA212568 | Phenoxybenzamine hydrochloride (Amneal Pharmaceuticals NY LLC) | Capsule | Not listed (license cancelled) |
| ANDA215042 | Phenoxybenzamine Hydrochloride (Novitium Pharma LLC) | Capsule | Not listed (license cancelled) |
| ANDA215600 | Phenoxybenzamine Hydrochloride (Aurobindo Pharma Limited) | Capsule | Not listed (license cancelled) |

All three licenses are for single-ingredient oral capsules, and all are cancelled. Availability of the drug in the US is therefore limited.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (model-derived, not from label text): kidney disease, pyoureter, hypotensive disorder, coronary artery disease.
- **Drug Interactions**: 32 interactions were identified, all of those listed at Moderate level (DDInter). Main examples include:
  - Opioids and related agents: morphine, codeine, hydrocodone, opium
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Prostacyclin-pathway drugs: epoprostenol, iloprost, selexipag, treprostinil
  - Others: bupropion, dronabinol, nabilone, amifostine, promethazine, mepyramine, iobenguane (I-123), nitrous acid
- **Expected class effects** (general pharmacology, not from the compiled data): orthostatic hypotension, reflex tachycardia and nasal congestion are typical of systemic alpha blockade.

Official warnings and contraindications from the package insert were not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score, with no clinical trials or publications (Evidence Level L5). The mechanistic link is speculative, especially for a genetically driven condition such as primary hereditary glaucoma. In addition, all US licenses are cancelled and systemic alpha blockade carries safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Preclinical or literature evidence on the effect of phenoxybenzamine on intraocular pressure and aqueous humor dynamics
- Assessment of ocular perfusion risk and a feasibility review of the route of administration (for example, a topical ophthalmic formulation versus systemic oral use)
- Clarification of drug supply, given that the US market status is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

