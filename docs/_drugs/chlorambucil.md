---
layout: default
title: Chlorambucil
parent: Model Prediction Only (L5)
nav_order: 518
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Chlorambucil: From an Alkylating Chemotherapy to CLL/SLL with IGHV Somatic Hypermutation

## One-Sentence Summary

Chlorambucil is an oral nitrogen mustard alkylating agent that is marketed in the United States as LEUKERAN tablets.
The TxGNN model predicts it may be effective for **chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL) with immunoglobulin heavy chain variable-region gene somatic hypermutation**.
This prediction has **0 clinical trials** and **0 publications** linked to it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | CLL/SLL with immunoglobulin heavy chain variable-region gene somatic hypermutation |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

The approved-indication text for the US license is blank in the Evidence Pack, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorambucil is a DNA-alkylating nitrogen mustard, and its cytotoxicity against lymphocytes makes activity in CLL/SLL biologically plausible. The very high TxGNN score (0.997) is consistent with that.

The Evidence Pack has no original indication or mechanism data for chlorambucil, and no trials or literature for this IGHV-mutated subtype. It therefore contains no evidence beyond the model score to support the prediction. Any link between the original indication and this subtype would have to be confirmed against the label and current CLL standards of care, which have shifted toward targeted agents.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA010669 | LEUKERAN | Tablet, film coated (oral) | Waylis Therapeutics LLC |

---

## Cytotoxicity

Route and classification below come from general drug-class knowledge, because the Evidence Pack does not include DrugBank categories or toxicity data. Please confirm them against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High (dose-related bone marrow suppression is expected for this class) |
| Emetogenicity Classification | Low (at usual oral doses) |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a high model score but no linked trials or literature (L5). The package insert warnings and contraindications are missing, which blocks safety screening.

**Other predicted indications in the pack:**
- **Primary pulmonary lymphoma** (rank 4, L3) has the most literature. That literature is indirect and confounded by radiotherapy, rituximab-based and surgical approaches. Only 10 of its 16 linked papers were provided, so the rest need review for chlorambucil-specific data. It is the most reasonable candidate for follow-up as a research question.
- **Acute lymphoblastic leukemia** (rank 7) has three Phase 3 trials linked, but all are CLL studies with chlorambucil as comparator or backbone. They do not support chlorambucil in ALL and should not be read as L1.
- **Small cell lung carcinoma** (rank 8) has only old, non-specific phase II studies and hypothesis-generating preclinical work. Platinum-etoposide regimens remain the standard of care.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently blocking)
- Mechanism of action data from DrugBank
- The approved indication text for NDA010669, to establish the original-to-new indication link
- Review of the remaining pulmonary lymphoma papers for chlorambucil-specific efficacy
- Comparison against current CLL/SLL and lymphoma standards of care

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

