---
layout: default
title: Mepivacaine
parent: Model Prediction Only (L5)
nav_order: 899
evidence_level: L5
indication_count: 2
---

# Mepivacaine
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

# Mepivacaine: From Local Anesthesia to Gastroduodenitis

## One-Sentence Summary

Mepivacaine is an amide local anesthetic sold as an injectable (infiltration, nerve block and dental use).
The TxGNN model predicts it may be useful for **gastroduodenitis**, with a second prediction for **peptic ulcer disease**.
There are currently **0 clinical trials** and **0 publications** supporting either prediction, so both rest on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (inferred from the injectable formulations; the license records list no indication text) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Mepivacaine is an amide local anesthetic that blocks voltage-gated sodium channels. A plausible link is a temporary reduction of pain signaling from nerves in the stomach and duodenal lining. Local anesthetics such as lidocaine appear in symptomatic "GI cocktail" practice. This link is indirect and has not been established for mepivacaine.

Any benefit would be symptom relief, not treatment of the underlying disease. The TxGNN score (0.995) is a knowledge-graph prediction only. The input has no recorded original indications and no drug-interaction data, so the mechanism cannot be checked against the source record.

For the second prediction, **peptic ulcer disease** (score 99.41%), no direct mechanism links sodium channel blockade to ulcer healing, acid suppression or *H. pylori* eradication. At most, ulcer pain might be relieved. Standard therapies (proton pump inhibitors, *H. pylori* eradication) are well established, so a candidate with no efficacy evidence has no clear unmet need to justify further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The five main authorizations are listed below. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA089406 | POLOCAINE(R)-MPF (Mepivacaine HCl) | Injection, solution | HF Acquisition Co LLC, DBA HealthFirst |
| ANDA088387 | Mepivacaine | Injection, solution | Benco Dental |
| ANDA089410 | Polocaine | Injection, solution | Fresenius Kabi USA, LLC |
| ANDA088387 | IQ Dental Mepivacaine | Injection, solution | IQ Dental |
| ANDA088387 | Mepivacaine Hydrochloride | Injection, solution | Safco Dental Supply Co. |

All available products are injectables. No oral or topical gastrointestinal formulation is listed, so route compatibility with the predicted indications is unresolved.

## Safety Considerations

- **Systemic or oral exposure:** Mepivacaine is formulated for injection. Systemic or oral use raises concerns about methemoglobinemia and cardiac and CNS toxicity.
- **Drug Interactions:** No interaction records were found in the query.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are supported only by a knowledge-graph score, with no clinical trials or publications (evidence level L5). The mechanism is indirect and limited to possible symptom relief. Only injectable products exist, and systemic exposure carries safety risks.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Any preclinical or clinical evidence for gastroduodenitis or peptic ulcer disease
- Assessment of route feasibility, since no oral or topical gastrointestinal formulation exists
- For peptic ulcer disease, a clear unmet need beyond current standard therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

