---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 2
---

# Dicyclomine
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

# Dicyclomine: From Functional Bowel/Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antispasmodic used for gastrointestinal smooth-muscle spasm, commonly functional bowel/irritable bowel syndrome.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.
Cauda equina syndrome is a surgical emergency, so any symptomatic use of an anticholinergic carries a safety concern.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Functional bowel/irritable bowel syndrome (general drug knowledge; the approved-indication text is blank in all provided US license records) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDAs, i.e. generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Dicyclomine is generally described as an antimuscarinic (anticholinergic) antispasmodic with a direct smooth-muscle relaxant effect, but the provided data does not confirm this.

Cauda equina syndrome is caused by compression of the lumbosacral nerve roots and often causes bladder and bowel dysfunction. In principle, anticholinergic drugs could relieve some of these symptoms. This link is only theoretical.

The drug would not treat the underlying cause, which is nerve root compression that needs urgent surgical decompression. Anticholinergics can also worsen urinary retention, which is common in this condition. That could mask or delay recognition of a surgical emergency.

The model's second-ranked prediction, "obsolete neurogenic bladder (disease)" (score 99.50%), also has no trials or literature. Its mechanistic rationale is somewhat more plausible, because antimuscarinics are established for neurogenic detrusor overactivity. However, the disease term is flagged as obsolete in the ontology and would need to be re-mapped to a current concept before further assessment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The approved-indication text is blank in all license records, so the manufacturer is listed instead.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA084285 | Dicyclomine Hydrochloride | Capsule | NuCare Pharmaceuticals, Inc. |
| ANDA216736 | Dicyclomine hydrochloride | Tablet | Northwind Health Company, LLC |
| ANDA040319 | Dicyclomine Hydrochloride | Capsule | REMEDYREPACK INC. |
| ANDA084285 | Dicyclomine Hydrochloride | Capsule | A-S Medication Solutions |
| ANDA040319 | Dicyclomine Hydrochloride | Capsule | Preferred Pharmaceuticals Inc. |

Dosage forms on record include oral capsules and tablets, and injectable solutions.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score (99.66%), with no clinical trials or literature (Evidence Level L5). Cauda equina syndrome is a surgical emergency, and an anticholinergic could worsen urinary retention and delay diagnosis.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A review of the urinary retention risk in patients with nerve root compression
- Any clinical or preclinical evidence linking dicyclomine to cauda equina syndrome or neurogenic bladder
- Re-mapping of the obsolete neurogenic bladder term to a current disease concept before assessing that indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

