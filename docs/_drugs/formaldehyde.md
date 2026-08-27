---
layout: default
title: Formaldehyde
parent: 僅模型預測 (L5)
nav_order: 735
evidence_level: L5
indication_count: 10
---

# Formaldehyde
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

# Formaldehyde: From No Approved Therapeutic Indication to Diffuse Cutaneous Leishmaniasis (Low-Confidence Signal)

## One-Sentence Summary

Formaldehyde (DrugBank DB03843) has no approved therapeutic indication and is not marketed as a drug in the US — its recognized uses are as a laboratory fixative, disinfectant, and embalming agent. The TxGNN model assigns its top prediction to **Diffuse Cutaneous Leishmaniasis** with a **99.93%** score, but this is supported by only **1 publication**, which is a diagnostic-methodology paper (comparing tissue-fixation techniques for parasite detection) rather than treatment evidence — the evidence pack's own analysis flags this as a likely data artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record — formaldehyde has no approved therapeutic indication; known uses are as an industrial/laboratory fixative and disinfectant |
| Predicted New Indication | Diffuse Cutaneous Leishmaniasis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only; the one available reference is non-therapeutic) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for formaldehyde is not available (flagged as a High-severity data gap). Formaldehyde has no recorded therapeutic indication to compare against — its only well-established biological uses are as a fixative/cross-linking agent for tissue and specimen preservation, and as a disinfectant/sterilant.

The single literature reference behind the top prediction (PMID 9830259) compares formalin-fixed, ethanol-fixed, and frozen specimen preservation methods for PCR-based detection of *Leishmania* parasites — it is a diagnostic methodology study, not evidence of therapeutic effect. The rationale field in the evidence pack states this explicitly: the TxGNN score most likely reflects co-occurrence of "formalin" with the disease node in a specimen-processing context in the knowledge graph, not a genuine pharmacological relationship. The same confound pattern recurs across most of the other top-10 predictions in this pack (vaccine antigen inactivation, FFPE tissue methodology, embalming/anatomical studies), so this is not an isolated case.

One partial exception exists further down the ranked list: **pyelonephritis** (rank 4, evidence level L3, decision stage S1, "Research Question") is linked through methenamine (hippurate/mandelate salts), a prodrug that releases formaldehyde in acidic urine and is an established UTI-prophylaxis agent (e.g., NCT04077580, Phase 4, n=289, completed). This is a mechanistically plausible signal, but it applies to methenamine as a distinct chemical entity, not to formaldehyde administered directly.

It is also important to note an opposite-direction safety signal present in the same evidence pack: for the X-linked lymphoproliferative syndrome candidate (rank 6), the supporting literature instead documents formaldehyde as an IARC Group 1 occupational carcinogen associated with lymphohematopoietic malignancies (PMID 31870335, 14600094, 19933446, 3770995) — i.e., a risk factor, not a treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9830259](https://pubmed.ncbi.nlm.nih.gov/9830259/) | 1998 | Diagnostic methodology | The Journal of Dermatology | Compares formalin-fixed, ethanol-fixed, and frozen skin specimens for PCR/Southern blot detection of *Leishmania* parasites; a specimen-preparation study, not a treatment study |

---

## US Market Information

Formaldehyde is not currently marketed as an approved drug product in the US (market status: Not Marketed; 0 NDA licenses on record). No authorization table applies.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, DDI) is on record for formaldehyde — this is itself flagged as a **Blocking** data gap (DG001: TFDA label warnings/contraindications not yet retrieved), meaning this candidate cannot pass initial safety screening (S1) as currently documented.

Separately, literature surfaced elsewhere in this evidence pack (in the context of an unrelated predicted indication) documents formaldehyde as an **IARC Group 1 human carcinogen**, with occupational-exposure studies linking it to myeloid leukemia, non-Hodgkin lymphoma, and nasopharyngeal/sinonasal cancer. This is a known hazard signal that should inform any further evaluation of this candidate, even though it does not appear in the structured `safety` fields.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No approved indication, no MOA data, and no direct clinical or mechanistic evidence supports formaldehyde itself as a treatment for any of its top-ranked predicted indications; the top-ranked prediction (diffuse cutaneous leishmaniasis) rests on a single diagnostic-methodology paper unrelated to treatment, and the pattern repeats across most other candidates. The one indirect signal (pyelonephritis, via the methenamine prodrug) does not establish a case for formaldehyde itself.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Verified mechanism-of-action data (DG002)
- A route-of-administration and dosing feasibility assessment for formaldehyde as a therapeutic agent, given its known carcinogenicity
- If the pyelonephritis/UTI-prophylaxis signal is worth pursuing, it should be scoped as a separate repurposing evaluation of **methenamine** (not formaldehyde)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

