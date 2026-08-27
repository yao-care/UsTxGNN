---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 855
evidence_level: L5
indication_count: 10
---

# Levofloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibacterial, historically used to treat bacterial infections of the respiratory tract, urinary tract, skin, and eye. The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but this direction is currently supported by only **0 clinical trials** and **1 publication**, and that single publication describes an outbreak caused by a pathogen (microsporidia) that levofloxacin does not directly target — the evidence base is preliminary and requires clarification before further investment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibacterial class); no specific approved‑indication text is available in this Evidence Pack — market authorization records for this drug are empty |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this candidate (`original_moa: [Data Gap]`). Based on generally known pharmacology, levofloxacin is a third‑generation fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, and levofloxacin ophthalmic formulations are already approved for bacterial conjunctivitis/keratitis. Its efficacy against susceptible bacterial ocular pathogens is well established, which is the mechanistic basis for TxGNN linking it to keratoconjunctivitis-type diseases.

However, the single supporting publication for this specific prediction (PMID 30055152) describes an outbreak of **microsporidial** keratoconjunctivitis — microsporidia are parasites, not bacteria, and are not a target of levofloxacin's direct antimicrobial mechanism. In that report, levofloxacin (if used at all) would function only as adjunctive prophylaxis against secondary bacterial infection, not as primary therapy for the causative organism. This raises the possibility that the TxGNN association reflects a broad disease-category overlap (bacterial vs. non-bacterial keratoconjunctivitis) rather than a genuine pathogen-matched treatment opportunity, and this ambiguity should be resolved before the candidate advances.

**Note:** This Evidence Pack also contains other TxGNN-predicted indications for levofloxacin with substantially stronger evidence — infection prophylaxis in multiple myeloma/monoclonal gammopathy (Evidence Level L1, driven by the TEAMM Phase 3 RCT) and treatment of septicemic plague (Evidence Level L2, an FDA-approved indication under the Animal Rule). Those candidates may warrant separate, higher-priority evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak/cohort report (pathogen mismatch) | American Journal of Ophthalmology | Reports an outbreak of microsporidial keratoconjunctivitis linked to swimming pool water contamination in Taiwan; the causative organism is a parasite, not a bacterium levofloxacin directly targets |

---

## US Market Information

No marketing authorization (NDA) records are currently on file for this candidate — `taiwan_regulatory.market_status` is reported as **Not Marketed**, with 0 total licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Data gap flag:** TFDA label warnings/contraindications (`DG001`) are marked as a **Blocking** severity data gap in this Evidence Pack, meaning the candidate cannot yet proceed to an S1 safety pre-assessment. This gap must be resolved (via TFDA label retrieval) before any further clinical development discussion.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level (L4) rests on a single non-clinical-trial publication whose causative pathogen (microsporidia) does not match levofloxacin's known antibacterial mechanism, and no clinical trials support this specific indication. Combined with a Blocking-severity data gap on TFDA safety labeling (`DG001`), this candidate does not yet meet the bar to proceed past the research-question stage.

**To proceed, the following is needed:**
- TFDA package insert / label warnings and contraindications (`DG001`, Blocking)
- Detailed mechanism of action (MOA) data (`DG002`, High)
- Clarification of whether the causative pathogen in the reported case is bacterial (levofloxacin-susceptible) or purely parasitic (microsporidial), to confirm or rule out a TxGNN prediction artifact
- Preclinical or in vitro susceptibility data specific to the ocular pathogens implicated in punctate epithelial keratoconjunctivitis
- If pursued, a dedicated literature/clinical-trial search restricted to bacterial etiologies of punctate epithelial keratoconjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

