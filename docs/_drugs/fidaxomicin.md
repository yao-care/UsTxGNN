---
layout: default
title: Fidaxomicin
parent: Model Prediction Only (L5)
nav_order: 706
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Fidaxomicin: From Clostridioides difficile-Associated Diarrhea to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is an oral, narrow-spectrum macrocyclic antibiotic, originally used to treat *C. difficile*-associated diarrhea.
The TxGNN model predicts it may be effective for **staphylococcal scalded skin syndrome (SSSS)**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *C. difficile*-associated diarrhea (the license records in the source data have blank indication text) |
| Predicted New Indication | Staphylococcal scalded skin syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (2 NDAs and 3 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on general pharmacology, fidaxomicin inhibits bacterial RNA polymerase and shows some in vitro activity against Gram-positive organisms, including *Staphylococcus aureus*. This is the only mechanistic basis for the prediction.

SSSS is caused by exfoliative toxins from *S. aureus* and normally requires systemic antistaphylococcal therapy. The link between the two diseases is therefore the shared organism. Fidaxomicin's original use is in a gut infection, while SSSS is a skin and blood-borne toxin disease.

There is also a major practical obstacle: oral fidaxomicin is minimally absorbed, so it does not reach the skin or bloodstream in meaningful amounts. No topical or injectable formulation is marketed. The high score is a graph-based prediction, not a signal backed by clinical data.

The other top-ranked predictions look similar: all nine are L5 and Hold, and several appear to be graph artifacts, such as botulism and candidiasis. One retrieved reference (PMID 31634096, a general hospital medicine literature update) was linked to the *S. aureus* pneumonia prediction, not to SSSS. It does not appear to provide fidaxomicin-specific evidence for that indication, though the full text was not reviewed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA201699 | Dificid (Merck Sharp & Dohme LLC) | Film-coated tablet | Not listed in source data |
| NDA213138 | DIFICID (Merck Sharp & Dohme LLC) | Granule for suspension | Not listed in source data |
| ANDA219559 | Fidaxomicin (Apotex Corp.) | Film-coated tablet | Not listed in source data |
| ANDA208443 | Fidaxomicin (Teva Pharmaceuticals, Inc.) | Film-coated tablet | Not listed in source data |
| ANDA220374 | Fidaxomicin (Torrent Pharmaceuticals Limited) | Film-coated tablet | Not listed in source data |

All marketed forms are oral. No topical or injectable product exists.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5), and fidaxomicin's minimal oral absorption makes it pharmacologically unlikely to treat a toxin-mediated skin disease that needs systemic therapy. Established standard treatments already exist for SSSS.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (needed before any safety screening)
- Detailed mechanism of action data (DrugBank)
- In vitro susceptibility data for fidaxomicin against SSSS-causing *S. aureus* strains
- Evidence that a formulation or route could deliver adequate systemic or skin exposure
- Any preclinical or clinical study of fidaxomicin in staphylococcal skin or toxin-mediated disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

