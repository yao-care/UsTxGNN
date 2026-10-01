---
layout: default
title: Ethambutol
parent: Model Prediction Only (L5)
nav_order: 681
evidence_level: L5
indication_count: 5
---

# Ethambutol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is an oral antimycobacterial drug used as a partner drug in tuberculosis regimens. The Evidence Pack does not list an original indication, so this is taken from the drug's known use.
The TxGNN model predicts it may be effective for **epiglottitis**, but **0 clinical trials** and **0 publications** support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (ethambutol is a known antituberculosis drug) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ethambutol inhibits mycobacterial arabinosyl transferases (embA/B/C). This blocks synthesis of arabinogalactan, a key component of the mycobacterial cell wall. The source record contains no formal mechanism-of-action entry, so this description comes from the evidence assessment.

The mechanistic link to epiglottitis is weak. Epiglottitis is usually caused by *Haemophilus influenzae*, streptococci or other non-mycobacterial bacteria. These organisms lack the arabinogalactan pathway that ethambutol targets. The high score (99.90%) most likely reflects closeness in the knowledge graph to other infectious airway diseases, not a real pharmacological relationship. Standard antibacterial therapy is not addressed by any data in this pack.

The only plausible route would be rare mycobacterial involvement of the epiglottis or larynx. That would be an extension of ethambutol's existing anti-TB use, not a new indication. The supplied data does not test this for epiglottitis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Duplicate entries are merged; three distinct authorizations are listed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075095 | Ethambutol Hydrochloride (Epic Pharma) | Film-coated tablet | Not listed in source data |
| NDA016320 | Ethambutol Hydrochloride (Marlex Pharmaceuticals) | Film-coated tablet | Not listed in source data |
| ANDA078939 | Ethambutol Hydrochloride (Lupin Pharmaceuticals) | Tablet | Not listed in source data |

All listed products are oral.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the mechanism does not fit the likely bacterial causes of epiglottitis. The related laryngitis and peritonitis predictions are supported only by case reports and reviews of laryngeal or peritoneal tuberculosis. Those cases show anti-TB use at a different anatomical site, not repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (this blocks safety screening)
- Confirmed original indication and mechanism-of-action data from DrugBank
- Evidence of mycobacterial involvement in epiglottitis, or a documented reason ethambutol would help in non-mycobacterial epiglottitis
- Any registered trial or clinical study directly addressing epiglottitis

This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

