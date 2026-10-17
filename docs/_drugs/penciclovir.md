---
layout: default
title: Penciclovir
parent: Model Prediction Only (L5)
nav_order: 1027
evidence_level: L5
indication_count: 1
monitor_inn: "PENCICLOVIR"
predicted_indications: ["fascioliasis"]
last_modified_at: 2026-10-14
description: "Penciclovir: predicted new indication Fascioliasis (evidence level L5). Approved use: Herpes labialis"
---

# Penciclovir
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

# Penciclovir: From Herpes Labialis to Fascioliasis

## One-Sentence Summary

Penciclovir is a topical antiviral nucleoside analog, originally used to treat herpes labialis (cold sores).
The TxGNN model predicts it may be effective for **fascioliasis**, but this rests on a model score alone, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes labialis |
| Predicted New Indication | Fascioliasis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (1 NDA and 4 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, penciclovir is a guanosine nucleoside analog. After phosphorylation by viral thymidine kinase, it inhibits viral DNA polymerase in herpesviruses. This explains its effect in herpes labialis.

The predicted link to fascioliasis is hard to justify mechanistically. Fascioliasis is caused by the trematode parasites *Fasciola hepatica* and *Fasciola gigantica*. These parasites have no known viral-type thymidine kinase activation pathway, so the antiviral mechanism of penciclovir has no clear counterpart. The high score (0.991) most likely reflects proximity in the knowledge-graph network rather than true biological relevance.

There is also little unmet need to justify prioritizing this candidate. Triclabendazole is a well-established standard therapy for fascioliasis. In addition, penciclovir is marketed only as a topical cream, which is a poor fit for a liver-dwelling parasitic infection. A route-compatibility assessment has not yet been done.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020629 | Denavir (Mylan Pharmaceuticals Inc.) | Cream | Not listed (cancelled) |
| ANDA214100 | Penciclovir (Amneal Pharmaceuticals NY LLC) | Cream | Not listed (cancelled) |
| ANDA216981 | Penciclovir (Torrent Pharmaceuticals Limited) | Cream | Not listed (cancelled) |
| ANDA212710 | Penciclovir (Teva Pharmaceuticals USA, Inc.) | Cream | Not listed (cancelled) |
| ANDA212368 | Penciclovir (Padagis Israel Pharmaceuticals Ltd) | Cream | Not listed (cancelled) |

All five authorizations are cancelled, and all are topical creams.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical or literature support (L5). No plausible mechanistic link exists between a herpesvirus-specific nucleoside analog and a trematode parasite. The only available formulation is a topical cream, and an effective standard therapy already exists.

**To proceed, the following is needed:**
- Mechanistic evidence that penciclovir or its metabolites act on *Fasciola* species (for example, in vitro activity assays)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications, to enable safety screening
- Route-compatibility assessment, since systemic exposure would be needed for fascioliasis and only topical products have been marketed
- Justification of unmet need relative to triclabendazole
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

