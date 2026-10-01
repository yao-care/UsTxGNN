---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
---

# Ambrisentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is an oral endothelin type A (ETA) receptor antagonist used for pulmonary arterial hypertension (PAH). The TxGNN model predicts it may be effective for **pulmonary arteriovenous malformation (PAVM)**, but the only supporting evidence is **1 case report** and **0 clinical trials**, and that report concerns PAH, not the malformation itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (taken from the pack's mechanistic notes; the license records contain no indication text) |
| Predicted New Indication | Pulmonary arteriovenous malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 (very weak: a single case report, no trials) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are all generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ambrisentan blocks the ETA receptor, which reduces endothelin-1-driven vasoconstriction and vascular remodeling. Detailed mechanism-of-action data are not available in the input, so this description rests on the drug's known class and the pack's mechanistic notes.

The prediction is **not well supported**. PAVMs are structural vascular malformations, typically seen in hereditary hemorrhagic telangiectasia (HHT), and the endothelin pathway is not an established driver of them. The only literature hit is a case report of PAH coexisting with HHT. In that setting the drug would act on the PAH component, not on the malformation. The high TxGNN score is therefore not backed by mechanism or clinical data and is best treated as a graph-based artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World J Clin Cases | A patient with HHT who also had PAH, with a family gene analysis. It raises awareness of this rare co-occurrence and is not evidence that ambrisentan treats PAVM. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA208354 | Ambrisentan | Tablet, film coated | Sigmapharm Laboratories, LLC |
| ANDA208441 | Ambrisentan | Tablet, film coated | Mylan Pharmaceuticals Inc. |
| ANDA210701 | Ambrisentan | Tablet, film coated | Apotex Corp. |
| ANDA210058 | Ambrisentan | Tablet, film coated | Zydus Pharmaceuticals USA Inc. |
| ANDA216531 | Ambrisentan | Tablet, film coated | A-S Medication Solutions |

The registry provides no approved-indication text for these entries. The only route is oral.

---

## Safety Considerations

- **Key Warnings**: Ambrisentan carries an embryo-fetal toxicity boxed warning (noted in the pack's analysis, not in structured label data).

Please refer to the package insert for full warnings, contraindications and drug interactions. No interaction data were returned in the input.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, one off-target case report, and no established mechanistic link between ETA antagonism and PAVM. The pack rates it evidence level L4 (S0, Hold), and the case report describes PAH in an HHT patient, not treatment of the malformation.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence that endothelin signaling contributes to PAVM formation or growth
- Any interventional or observational data of ambrisentan specifically for PAVM or HHT-related vascular malformations
- Package insert warnings and contraindications, which are currently missing

**Note on other predictions in this pack:** Higher-evidence candidates exist and would be better subjects for their own reports. PAH associated with connective tissue disease (rank 4) is rated L2 with Proceed with Guardrails. It has ambrisentan-specific trials and trial subgroup analyses, plus a meta-analysis and a systematic review. PAH associated with congenital heart disease (rank 2) is also rated L2 with Proceed with Guardrails. Both are Group 1 PAH subtypes, so they sit close to the drug's core indication. Label coverage should be confirmed, since the original-indication data are missing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

