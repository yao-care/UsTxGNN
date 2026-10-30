---
layout: default
title: Lubiprostone
parent: Model Prediction Only (L5)
nav_order: 875
evidence_level: L5
indication_count: 10
monitor_inn: "LUBIPROSTONE"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "pulmonary hypertension", "kyphoscoliotic heart disease", "Raynaud disease", "pulmonary hypertension, primary, autosomal recessive", "phaeochromocytoma", "peripheral vascular disease"]
last_modified_at: 2026-10-30
description: "Lubiprostone: predicted new indication Alopecia (evidence level L5). Approved use: Chronic constipation and irritable bowel syndrome"
---

# Lubiprostone
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

## Lubiprostone: From Chronic Constipation to Alopecia
{: .text-alpha }

## One-Sentence Summary

Lubiprostone is a ClC-2 chloride channel activator used in the gut, with a pharmacology-database record describing its use in chronic constipation and irritable bowel syndrome.
The TxGNN model predicts it may be effective for **alopecia**, but this is a TxGNN model (deep learning) prediction only.
Currently there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic constipation and irritable bowel syndrome (from a pharmacology database; the US license records contain no indication text) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 4) |
| Number of FDA Applications | 4 authorization records (1 NDA, 3 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From pharmacology records, lubiprostone is a synthetic compound that activates the ClC-2 chloride channel in the gut. It is derived from a prostaglandin E1 metabolite (a bicyclic fatty acid, a "prostone").

No established mechanism links ClC-2 activation to hair growth. The alopecia prediction is therefore best read as a computational artifact. The other highly ranked predictions are also hair disorders (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata). This suggests the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. For alopecia areata specifically, the disease is T-cell mediated and lubiprostone has no recognized immunomodulatory action against it.

A second group of predictions concerns vascular conditions: pulmonary hypertension, kyphoscoliotic heart disease, Raynaud disease, and peripheral vascular disease. Here the only rationale is speculative. The prostaglandin-like structure could suggest vasodilation, as prostacyclin analogs are used in pulmonary arterial hypertension and Raynaud phenomenon. However, lubiprostone's action is gut-localized, its systemic absorption is minimal, and no vascular activity has been demonstrated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021908 (cancelled) | Amitiza (SpecGx LLC) | Capsule, gelatin coated | Not available in the compiled data |
| ANDA218640 (cancelled) | Lubiprostone (Northstar Rx LLC) | Capsule | Not available in the compiled data |
| ANDA214131 (cancelled) | Lubiprostone (Zydus Pharmaceuticals USA Inc.) | Capsule | Not available in the compiled data |
| ANDA209920 (cancelled) | Lubiprostone (Teva Pharmaceuticals, Inc.) | Capsule, gelatin coated | Not available in the compiled data |

All products are oral formulations.

## Safety Considerations

- **Drug Interactions**:
  - Idelalisib: Moderate interaction (DDInter).
  - ClC-2: This is a pharmacological target record (the chloride channel lubiprostone activates), not a drug-drug interaction.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no clinical trials or publications, and no plausible mechanism links ClC-2 activation to hair growth or to the other predicted conditions. The drug is marketed in the US, with 4 valid licenses.

**To proceed, the following is needed:**
- Mechanistic evidence for a plausible link between ClC-2 activation (or prostone pharmacology) and hair follicle biology
- Preclinical studies (for example, in vitro or animal models of hair growth) to move beyond L5
- Package insert warnings and contraindications for safety screening
- Detailed mechanism of action data from DrugBank
- Assessment of route compatibility, since lubiprostone is oral and gut-localized with minimal systemic exposure, and any hair or vascular indication would likely need systemic or topical delivery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

