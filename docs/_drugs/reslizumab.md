---
layout: default
title: Reslizumab
parent: Model Prediction Only (L5)
nav_order: 1117
evidence_level: L5
indication_count: 2
---

# Reslizumab
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

# Reslizumab: From Eosinophilic Asthma to Immune Thrombocytopenia

## One-Sentence Summary

Reslizumab (CINQAIR) is an injectable anti-IL-5 antibody that depletes eosinophils. The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data. CINQAIR is generally known as an anti-IL-5 therapy for severe eosinophilic asthma (background knowledge, not from the Evidence Pack) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761033) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Based on known information, reslizumab is an anti-IL-5 monoclonal antibody that lowers eosinophil levels.

The mechanistic link to the predicted indication is weak. Immune thrombocytopenia is driven mainly by autoantibody-mediated platelet destruction and impaired platelet production (megakaryopoiesis). No established IL-5 or eosinophil pathway explains it. The high TxGNN score (99.53%) is a graph-based prediction only and cannot be verified against a documented mechanism. Similarity to the original indication has not been assessed.

The model's second-ranked prediction, primary release disorder of platelets (score 99.25%), also has no direct mechanistic support. Its only linked paper is a review of hypereosinophilic syndrome management that covers mepolizumab, a different anti-IL-5 antibody ([PMID 20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/), 2010). It does not address platelet disorders or reslizumab.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761033 | CINQAIR (Teva Respiratory, LLC) | Injection, solution, concentrate | Not listed in the source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or literature for immune thrombocytopenia, and no plausible IL-5 or eosinophil mechanism explains it. The drug's safety profile and mechanism data are also missing from the inputs.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data, for example from DrugBank
- Confirmed approved indication text for BLA761033
- Any preclinical or clinical evidence linking IL-5 blockade to platelet destruction
- A route compatibility assessment (injectable) for the new indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

