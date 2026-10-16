---
layout: default
title: Ganirelix
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
monitor_inn: "GANIRELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial male-limited precocious puberty", "persistent fetal circulation syndrome", "aromatase excess syndrome", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Ganirelix
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

# Ganirelix: From Fertility Treatment (Ovarian Stimulation) to Hypertrichosis

## One-Sentence Summary

Ganirelix is a GnRH receptor antagonist used to prevent premature ovulation in women undergoing ovarian stimulation during fertility treatment.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output alone and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of premature ovulation during controlled ovarian stimulation (from pharmacology reference data; the US license records contain no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all 7 authorizations cancelled) |
| Number of NDAs | 7 (1 NDA, 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known pharmacology, ganirelix is a peptide antagonist of the GnRH receptor (GNRHR). It suppresses pituitary LH and FSH release and, indirectly, gonadal sex steroids.

The link to hypertrichosis is speculative. Hypertrichosis is not primarily driven by gonadotropins. Any connection would be through indirect modulation of sex steroids acting on hair follicles. The very high TxGNN score is a model output only. It likely reflects proximity in the knowledge graph rather than a biological rationale, and no clinical or literature data support it.

**Other predictions in the top 10.** None has clinical trial or literature support (all L5):
- **Central precocious puberty (score 99.75%)** is the most biologically coherent. It is driven by premature activation of the hypothalamic-pituitary-gonadal axis, so GnRH receptor blockade makes sense. However, GnRH agonists such as leuprolide and triptorelin are already standard care. Ganirelix's short-acting formulation with no depot form limits its practicality.
- **Aromatase excess syndrome (99.80%)** is a hypothesis only. Ganirelix could reduce gonadal steroid production, but extragonadal (adipose) aromatization would remain, and aromatase inhibitors are the more direct approach.
- **Familial male-limited precocious puberty (99.85%)** is caused by activating LHCGR mutations, which drive testosterone production independently of pituitary LH. A GnRH antagonist would therefore be expected to have little effect.
- **Other predictions** (Ambras syndrome, malformation syndromes, Dandy-Walker-associated syndromes, hair shaft abnormalities, persistent fetal circulation syndrome, familial trichomegaly) have no plausible GnRH-antagonist mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA021057 | Ganirelix Acetate (Organon LLC) | Injection, solution | Cancelled |
| ANDA204246 | Fyremadel (Ferring Pharmaceuticals) | Injection, solution | Cancelled |
| ANDA212613 | Ganirelix Acetate (Amphastar) | Injection | Cancelled |
| ANDA214996 | Ganirelix Acetate (Meitheal) | Injection, solution | Cancelled |
| ANDA215658 | Ganirelix Acetate (Gland Pharma) | Injection, solution | Cancelled |

Two further cancelled ANDAs (ANDA216075, Lupin; ANDA218855, Qilu) are also on record. The license records contain no approved-indication text. All products are injectables.

## Safety Considerations

- **Drug Interactions:** 7 interaction records were found. Six are rated Moderate (DDInter): gonadorelin, chorionic gonadotropin (human), menotropins, triptorelin, follitropin, and urofollitropin. The seventh is a pharmacology entry confirming ganirelix binds the GnRH1 receptor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypertrichosis has no supporting trials, no literature, and no plausible mechanism. The evidence level is L5. In addition, all US authorizations for ganirelix are cancelled, and no label-based safety information is available.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Any preclinical or clinical evidence linking GnRH antagonism to hypertrichosis
- Confirmation of the current US market and supply status
- If a lead is wanted from this prediction set, a focused literature review of ganirelix in central precocious puberty (the most plausible candidate) and a route and formulation assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

