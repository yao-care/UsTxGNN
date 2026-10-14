---
layout: default
title: Palifermin
parent: Model Prediction Only (L5)
nav_order: 1009
evidence_level: L5
indication_count: 6
---

# Palifermin
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

# Palifermin: From Oral Mucositis Supportive Care to Primary Release Disorder of Platelets

## One-Sentence Summary

Palifermin is a recombinant keratinocyte growth factor (KGF/FGF7), and the data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **0 clinical trials** and **0 publications** currently support this prediction.
The prediction rests on a knowledge-graph score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the compiled data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 (BLA 125103, cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Palifermin is known as a recombinant keratinocyte growth factor (FGF7) that acts on epithelial cells through FGFR2b. Its original approved indication could not be confirmed from the data compiled for this report.

No established link was found between this epithelial growth-factor pathway and platelet granule release or platelet function. The very high TxGNN score (99.94%) reflects a knowledge-graph prediction only. It may be driven by network artifacts rather than biology, so the prediction should be treated as a hypothesis with weak biological support.

The other predicted indications show the same pattern. All are inherited platelet or bleeding disorders, and none has a plausible link to FGF7/FGFR2b signaling:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Concern |
|------|------|------|------|------|
| 2 | Glanzmann thrombasthenia | 99.93% | L5 | Caused by integrin αIIbβ3 deficiency or dysfunction; palifermin has no known effect on it |
| 3 | Pseudo-von Willebrand disease | 99.91% | L5 | Gain-of-function GPIb-alpha defect; no plausible pathway connects it to FGF7 signaling |
| 4 | Hemorrhagic disorder due to a constitutional thrombocytopenia | 99.50% | L5 | Inherited defect of platelet production; palifermin is not known to act on the TPO/MPL axis |
| 5 | Bleeding diathesis due to a collagen receptor defect | 99.48% | L5 | Defective GPVI or α2β1 receptors; no known interaction with palifermin |
| 6 | Scott syndrome | 99.38% | L5 | Impaired phosphatidylserine exposure (TMEM16F/ANO6); no known effect of palifermin on this pathway |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA 125103 (cancelled) | KEPIVANCE | Injection, powder, lyophilized, for solution | Not listed in the compiled data |

The manufacturer is Swedish Orphan Biovitrum AB (publ). The only license on record is cancelled, so no currently valid US license was found.

## Cytotoxicity

Palifermin is a growth factor and not a cytotoxic antineoplastic agent, so no cytotoxicity assessment applies.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions in total. All 20 shown in the compiled data are rated **Moderate**, and most are anticancer agents. Examples include paclitaxel, capecitabine, carboplatin, bevacizumab, bortezomib, busulfan, bleomycin, azacitidine, and bendamustine. Aldesleukin and alemtuzumab are also listed. The remaining interactions were not available for review.
- No disease-contraindication edges were found in the knowledge graph.

Please refer to the package insert for warnings and contraindications. Label-based safety data could not be retrieved for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score, with no clinical trials, no literature, and no plausible mechanistic link between FGF7/FGFR2b signaling and platelet function. In addition, the only US license is cancelled, and the label-based safety review could not be completed.

**To proceed, the following is needed:**
- Retrieve the FDA package insert (warnings, contraindications, approved indication), which is required before any safety screening
- Obtain detailed mechanism of action data from DrugBank
- Run a targeted literature search for any link between KGF/FGF7 and platelet function or megakaryopoiesis
- Test the hypothesis in preclinical platelet function assays (e.g., aggregation and granule release) before considering clinical investigation
- Check whether the model's high scores stem from network artifacts, for example by examining the graph paths behind the prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

