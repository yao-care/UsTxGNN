---
layout: default
title: Fluorescein
parent: Model Prediction Only (L5)
nav_order: 720
evidence_level: L5
indication_count: 10
monitor_inn: "FLUORESCEIN"
predicted_indications: ["Prinzmetal angina", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "hemoglobinopathy", "heparin cofactor 2 deficiency", "thrombophilia", "hyperthyroidism", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
last_modified_at: 2026-10-14
description: "Fluorescein: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Diagnostic use"
---

# Fluorescein
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

## Fluorescein: From Diagnostic Angiography to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Fluorescein is a diagnostic fluorescent dye used in ophthalmic angiography and ocular surface staining, not a treatment for disease.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials** and **no supporting publications** exist for this prediction.
The prediction is graph-based only, and the evidence does not support a therapeutic role.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic use (ophthalmic angiography and ocular surface staining); no approved indication text is available in the compiled data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 6 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Fluorescein is a fluorescent dye used diagnostically, chiefly to visualize retinal and choroidal vasculature (angiography) and to reveal corneal and conjunctival surface damage (staining). It is not known to act on a therapeutic target.

For Prinzmetal angina, no mechanistic link could be identified. Prinzmetal angina is caused by coronary vasospasm, and fluorescein has no known vasodilatory or anti-vasospastic activity. The high TxGNN score most likely reflects network proximity in the knowledge graph rather than a real pharmacological relationship.

The other top-ranked predictions show the same pattern. These include antithrombin deficiency type 2, factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, and partial deletion of the short arm of chromosome 16. None has any trial or publication linking it to fluorescein. For rheumatoid arthritis, hemoglobinopathy, thrombophilia, and hyperthyroidism, the retrieved literature describes ocular complications of these diseases in which fluorescein is a diagnostic tool, so it does not support a therapeutic indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

Literature was retrieved for other lower-ranked predictions, but it concerns fluorescein as a diagnostic tool (for example, in sickle cell retinopathy or dry eye in rheumatoid arthritis), not as a treatment.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021980 | FLUORESCITE (Alcon) | Injection, solution | Not available (cancelled) |
| ANDA215709 | Fluorescein (Nexus Pharmaceuticals) | Injection | Not available (cancelled) |
| NDA022186 | AK-FLUOR (Long Grove Pharmaceuticals) | Injection | Not available (cancelled) |
| NDA211039 | Fluorescein Sodium and Benoxinate Hydrochloride (Bausch & Lomb) | Solution/drops | Not available (cancelled) |
| NDA208582 | ALTAFLUOR (Altaire Pharmaceuticals) | Solution | Not available (cancelled) |

A sixth authorization, for fluorescein sodium ophthalmic strips (Vistamerica USA), is also cancelled.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials, no supporting literature, and no plausible mechanism linking a diagnostic dye to coronary vasospasm. All US authorizations are cancelled, and package insert safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank)
- Package insert warnings and contraindications from FDA
- Any preclinical or clinical evidence of a therapeutic effect in Prinzmetal angina, which is currently absent
- Confirmation of whether a therapeutic (rather than diagnostic) role is pharmacologically credible before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

