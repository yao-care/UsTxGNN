---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 332
evidence_level: L5
indication_count: 2
---

# Ammonium Chloride
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

# Ammonium Chloride: From an Unlisted Original Indication to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride is marketed in the US in smelling salts, homeopathic pellets and similar products, and is known in general pharmacology as an oral expectorant. No approved indication text is recorded in the Evidence Pack.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the US licence data) |
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is used as an expectorant in cough and cold preparations. It is thought to irritate the gastric mucosa and reflexively increase respiratory tract fluid secretion. Mechanistically, this may be relevant to upper airway conditions.

The link to acute laryngopharyngitis is plausible but unverified. Expectorant activity does not establish benefit for inflammation of the larynx and pharynx. The very high TxGNN score is a model output only and has no trial or literature evidence behind it. The connection should be treated as hypothesis-level.

A second prediction, **nasal cavity disease** (score 99.94%), has the same limitations. It is also evidence level L5 with a Hold recommendation. The term is too broad to frame a testable question, and would need to be narrowed (for example, to rhinitis or sinusitis) first.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Bardown Smelling Salts | Liquid | Not listed |
| Not listed | Ammonium Muriaticum | Pellet | Not listed |
| 505G(a)(3) | LRNASH SMELLING SALTS | Granule | Not listed |
| Not listed | Ammonium carbonicum | Pellet | Not listed |
| Not listed | Ammonium Muriaticum | Pellet | Not listed |

Other dosage forms in the data include an inhalant and a soluble oral tablet.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). It has no registered trials or publications, no curated mechanism of action, and no recorded original indication. The expectorant rationale is plausible but does not support laryngopharyngeal benefit.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A literature and trial search targeted at ammonium chloride in pharyngitis or laryngitis
- Clarification of the original indication, given that the marketed products are mostly smelling salts and homeopathic items
- Narrowing of the "nasal cavity disease" term before that prediction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

