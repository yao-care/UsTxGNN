---
layout: default
title: Penciclovir
parent: Model Prediction Only (L5)
nav_order: 1027
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Penciclovir: From Herpes Labialis to Fascioliasis

## One-Sentence Summary

Penciclovir is a topical antiviral (cream) that is marketed in the US. The license records do not state the approved indication, but the drug is known for treating recurrent herpes labialis (cold sores).
The TxGNN model predicts it may be effective for **fascioliasis** (a liver fluke infection), but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no biological or clinical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (penciclovir cream is generally used for recurrent herpes labialis) |
| Predicted New Indication | Fascioliasis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (records list 5 entries: NDA020629 appears twice, plus 3 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, penciclovir is a guanosine nucleoside analogue antiviral. Viral thymidine kinase (HSV/VZV) phosphorylates it. Its triphosphate form then inhibits viral DNA polymerase.

**The mechanistic link to fascioliasis is not supported.** Fascioliasis is caused by the trematodes *Fasciola hepatica* or *F. gigantica*. These parasites have no viral thymidine kinase or comparable activation pathway. The standard treatment, triclabendazole, works through a different mechanism.

The high score (99.06%) is probably driven by similarity in the knowledge-graph neighborhood, not by biological or clinical evidence. The prediction cannot be cross-checked against the drug's known pharmacology, because the original indications and mechanism data are missing from the input.

Route compatibility is also unresolved. All US products are topical creams, while fascioliasis is a systemic hepatobiliary parasitic infection. A cream is unlikely to reach the site of infection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020629 | Denavir (Mylan Pharmaceuticals Inc.) | Cream | Not listed in the record |
| NDA020629 | Penciclovir (Mylan Pharmaceuticals Inc.) | Cream | Not listed in the record |
| ANDA214100 | Penciclovir (Amneal Pharmaceuticals NY LLC) | Cream | Not listed in the record |
| ANDA216981 | Penciclovir (Torrent Pharmaceuticals Limited) | Cream | Not listed in the record |
| ANDA212710 | Penciclovir (Teva Pharmaceuticals USA, Inc.) | Cream | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or publications, and the known antiviral mechanism does not apply to a parasitic fluke. The topical-only formulation also makes systemic use unlikely.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are needed before any safety screening
- Confirmed original indications and mechanism of action data
- Preclinical evidence (for example, in vitro anti-*Fasciola* activity) that would support any biological link
- A route and formulation assessment, since only topical creams are marketed
- A literature and trial search that includes fascioliasis and related trematode infections
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

