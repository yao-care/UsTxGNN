---
layout: default
title: Evolocumab
parent: Model Prediction Only (L5)
nav_order: 688
evidence_level: L5
indication_count: 6
---

# Evolocumab
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

# Evolocumab: From Homozygous Familial Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9-inhibiting monoclonal antibody, originally used to lower cholesterol in homozygous familial hypercholesterolemia and related dyslipidemia.
The TxGNN model predicts it may be effective for **symptomatic form of hemophilia in female carriers**, but **no clinical trials and no publications** currently support this prediction.
The top-ranked prediction is a knowledge-graph signal only, with no identified biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Homozygous familial hypercholesterolemia; syndromic dyslipidemia |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single BLA is cancelled) |
| Number of NDAs | 1 (BLA125522) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. From pharmacology data, evolocumab is an antibody that targets PCSK9 (proprotein convertase subtilisin/kexin type 9). By blocking PCSK9, it increases LDL receptor availability on the liver and lowers LDL cholesterol. It has been approved for patients, including those with heterozygous and homozygous familial hypercholesterolemia, who cannot control LDL-C with existing therapy.

The predicted indication is a different kind of disease. Symptomatic hemophilia in female carriers arises from reduced factor VIII or IX activity, caused by X-linked gene variants and skewed X-inactivation. PCSK9 inhibition has no known effect on coagulation factor production or function, so **no plausible mechanistic link was identified**. The high score (0.998) reflects a knowledge-graph prediction only and is not supported by biological rationale or clinical data.

### Other Predictions Reviewed

All other top predictions also have no trials or literature and are Level L5 with a "Hold" recommendation.

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Familial apolipoprotein C-II deficiency | 99.50% | Weak, indirect link as a lipid disorder. Evolocumab mainly lowers LDL-C and does not address the primary defect (impaired lipolysis causing severe hypertriglyceridemia). Benefit is speculative. |
| 3 | Thrombocytopenic purpura | 99.42% | No established link; the disease involves autoimmune platelet destruction or ADAMTS13 dysfunction, unrelated to PCSK9. |
| 4 | Factor XI deficiency | 99.29% | No plausible link; PCSK9 inhibition does not change factor XI levels or activity. |
| 5 | Hemophilia A with vascular abnormality | 99.22% | No plausible link; evolocumab does not affect factor VIII or von Willebrand factor biology. |
| 6 | Disease of catalytic activity | 99.08% | A non-specific ontology category, not a defined clinical indication; not actionable. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125522 (cancelled) | REPATHA (Amgen USA Inc.) | Injection, solution | Not listed in the data compiled |

## Safety Considerations

- **Drug Interactions**: One pharmacology entry was recorded, the drug's own target, PCSK9 (human, gene PCSK9). It is a target interaction, not a drug-drug interaction, and no severity level was assigned.

For other safety information (warnings and contraindications), please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest solely on model scores. There are no clinical trials or publications, and the mechanistic review found no plausible link for the top-ranked bleeding or coagulation indications. The only weak, indirect link is for familial apolipoprotein C-II deficiency, and its benefit is speculative. The US BLA is also listed as cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank to support mechanistic analysis
- Any preclinical or clinical evidence for the predicted indications, with priority on familial apolipoprotein C-II deficiency, the only prediction with a plausible lipid-related link
- Clarification of the cancelled US regulatory status of BLA125522
- Route compatibility and similarity-to-original-indication assessments, currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

