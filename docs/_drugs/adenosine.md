---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 216
evidence_level: L5
indication_count: 1
monitor_inn: "ADENOSINE"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-10-28
description: "Adenosine: predicted new indication obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Adenosine: adenosine receptor agonist (antiarrhythmic) → obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Adenosine is a cardiac drug that acts on adenosine receptors and slows conduction through the atrioventricular node.
The TxGNN model predicts it may be relevant to **obsolete bundle branch block**, but **no clinical trials and no publications** were found to support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete bundle branch block |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of NDAs | at least 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on general pharmacology, adenosine acts on cardiac A1 receptors, which slows or transiently blocks conduction through the AV node. It is used diagnostically and for terminating supraventricular tachycardia.

A plausible rationale for treating bundle branch block is not apparent. Bundle branch block is a disorder of conduction below the AV node, and a drug that slows conduction could in principle worsen conduction disease rather than improve it. The disease term is also flagged as obsolete in the ontology, so the high score (0.9994) may reflect an artifact of the model's training data rather than a real therapeutic signal. The mechanistic link and similarity to the original use are still pending review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The data compiled for this report list 8 US records (ANDA generic injectables and one cosmetic cream record). The list may be partial, and the records carry no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090212 | Adenosine | Injection, solution | Mylan Institutional LLC |
| ANDA077425 | Adenosine | Injection, solution | Meitheal Pharmaceuticals Inc. |
| ANDA206778 | Adenosine | Solution | Gland Pharma Limited |
| ANDA077133 | Adenosine | Injection, solution | Henry Schein, Inc. |
| ANDA202313 | Adenosine | Injection, solution | Heritage Pharmaceuticals Inc. (Avet) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. Major-level examples include cisapride, dolasetron and papaverine. Moderate-level examples include famotidine, clarithromycin, granisetron, levofloxacin, ondansetron and palonosetron. Several QT-prolonging drugs appear in this list.
- Package insert warnings and contraindications were not available; please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for this disease, and the evidence level is L5. The mechanism (slowing cardiac conduction) does not clearly support benefit in bundle branch block and may be harmful. The disease term is obsolete, so the prediction is likely an artifact.

**To proceed, the following is needed:**
- Review of whether the disease term maps to a current, clinically meaningful condition
- Mechanism-of-action data and a mechanistic analysis for conduction disorders
- FDA package insert warnings and contraindications for a safety review
- Any clinical or preclinical studies directly addressing this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

