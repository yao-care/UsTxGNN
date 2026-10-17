---
layout: default
title: Demeclocycline
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Demeclocycline: predicted new indication Chronic ethmoidal sinusitis (evidence level L5). Approved use: Bacterial infections (urinary tract infection, bronchitis, anthrax…"
monitor_inn: "DEMECLOCYCLINE"
predicted_indications: ["paranasal sinus neoplasm (disease)"]
---

# Demeclocycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Demeclocycline: From Bacterial Infections to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Demeclocycline is a tetracycline-class antibiotic, originally used to treat a range of bacterial infections such as urinary tract infection, bronchitis, gonorrhea and anthrax.
The TxGNN model predicts it may be effective for **chronic ethmoidal sinusitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, bronchitis, anthrax, staphylococcal infection, gonorrhea, pharyngitis, among others). The US label indication text is not available. |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 2 (both cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

Two other predictions were also generated, both with L5 evidence and a Hold recommendation:
- Chronic rhinosinusitis (score 99.09%)
- Paranasal sinus neoplasm (score 99.05%)

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, demeclocycline is a tetracycline antibiotic whose efficacy in bacterial infections of the respiratory tract and other sites is established. Mechanistically, it may be applicable to chronic sinusitis, where bacterial involvement is possible.

Tetracyclines have also been reported to have anti-inflammatory and matrix metalloproteinase-inhibiting effects, which could be relevant to chronic sinus inflammation. These are hypotheses and are not supported by data compiled for this report.

The other two predictions are weaker. Chronic rhinosinusitis shares the same rationale as ethmoidal sinusitis. The paranasal sinus neoplasm prediction is very different from the drug's anti-infective uses and likely reflects network proximity to sinus-related terms rather than a true therapeutic effect. It should not be advanced without supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065425 (cancelled) | Demeclocycline Hydrochloride (American Health Packaging) | Tablet | Not available |
| ANDA065447 (cancelled) | Demeclocycline Hydrochloride (Epic Pharma, LLC) | Tablet, film coated | Not available |

Both authorizations are cancelled, which limits practical feasibility for any repurposing effort.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and diabetes insipidus (including neurohypophyseal and central forms).
- **Drug Interactions**: 100 interactions were identified; the first 20 are listed in the data compiled for this report.
  - **Major**: Vitamin A.
  - **Moderate**: Amoxicillin, balsalazide, and polyvalent cation products (calcium phosphate, calcium acetate, magnesium oxide, magnesium sulfate, magnesium chloride, zinc sulfate, zinc acetate, potassium citrate). Several insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, and inhaled rapid-acting) are also Moderate.
  - **Minor**: Mannitol.

Please refer to the package insert for full warnings and precautions, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.14%), but there are no clinical trials or publications, so evidence is L5 (model prediction only). Demeclocycline has no valid US marketing authorization, and safety label data and mechanism of action are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A literature and trial search for tetracycline-class drugs in chronic sinusitis
- Assessment of route compatibility and whether a marketed product is available
- Clarification of why the predicted indication sits far from the original anti-infective profile, particularly for the paranasal sinus neoplasm prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

