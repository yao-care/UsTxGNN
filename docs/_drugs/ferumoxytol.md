---
layout: default
title: Ferumoxytol
parent: Model Prediction Only (L5)
nav_order: 703
evidence_level: L5
indication_count: 6
---

# Ferumoxytol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ferumoxytol: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferumoxytol is an intravenous iron replacement product. The license fields in the data are blank, so this indication comes from the drug's known use and the Evidence Pack's own rationale. The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but there are currently **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (from the drug's known use and the Evidence Pack rationale; the license text is blank) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 (3 distinct authorizations: 2 NDAs and 1 ANDA; one NDA is listed twice) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, ferumoxytol is an intravenous iron replacement product. Its efficacy in iron-deficiency anemia is established, and mechanistically it may be applicable to the anemia component of Plummer-Vinson syndrome.

Plummer-Vinson syndrome is defined by iron-deficiency anemia together with esophageal webs. Correcting the iron deficiency is therefore biologically plausible. The high score is probably driven by the drug's known iron-deficiency use.

Any benefit would target the anemia, not the esophageal webs. No trial or literature in the data supports this indication, so the score should be read as a model prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered for Plummer-Vinson syndrome.

## Literature Evidence

Currently no related literature available for Plummer-Vinson syndrome.

**Note on other predictions:** The only evidence in the pack is for a different, lower-ranked prediction, "esophageal disease" (rank 6, score 99.51%). It consists of 4 imaging studies in esophageal cancer (2 of them withdrawn with 0 patients enrolled) and 10 publications, mostly on related iron oxide agents. It is diagnostic MRI, not treatment, and does not support Plummer-Vinson syndrome.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022180 | Feraheme | Injection | AMAG Pharmaceuticals, Inc. |
| NDA219868 | FeraBright | Injection | Azurity Pharmaceuticals, Inc. |
| ANDA206604 | Ferumoxytol | Injection | Sandoz Inc |

The approved indication text is blank in the source data, so that column is omitted.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Plummer-Vinson syndrome has no supporting trials or publications (L5), and the plausible benefit is limited to correcting the accompanying iron-deficiency anemia. That use is already covered by existing iron therapy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (MOA)
- A targeted literature search on intravenous iron in Plummer-Vinson syndrome and iron-deficiency anemia with esophageal webs
- A comparison against standard oral iron therapy to establish whether intravenous ferumoxytol adds value
- Confirmation of the original indication from the FDA label, since the license text is blank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

