---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Efavirenz: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used as part of combination antiretroviral therapy for HIV-1 infection in humans. The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome** (FIV infection in cats), but this is currently supported only by **1 in vitro biochemical/structural study**; the 2 associated clinical trials in the evidence pack involve a different drug (dolutegravir) and are not directly relevant.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — inferred from trial context (e.g., comparator "Atripla" = efavirenz/emtricitabine/tenofovir); no formal Taiwan/US license record available |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (data gap). Based on the surrounding clinical trial and literature context, efavirenz is known to be an NNRTI used within combination antiretroviral regimens (e.g., Atripla: efavirenz/emtricitabine/tenofovir disoproxil fumarate) for HIV-1 infection, and its efficacy in that indication is well established.

Feline immunodeficiency virus (FIV) causes an AIDS-like immunodeficiency syndrome in cats and is, like HIV-1, a lentivirus that depends on a reverse transcriptase enzyme for replication — this is the conceptual basis for the TxGNN link. However, FIV reverse transcriptase is structurally distinct from HIV-1 reverse transcriptase, and NNRTIs have historically shown poor activity against FIV. The single supporting publication (PMID 38031646) is an in vitro biochemical/structural comparison examining whether efavirenz, nevirapine, and rilpivirine could bind FIV reverse transcriptase — it demonstrates a theoretical structural interaction, not antiviral efficacy in infected cells or animals.

No cellular antiviral assay, animal efficacy study, or veterinary safety/dosing data exist for efavirenz in FIV. The two clinical trials associated with this candidate involve dolutegravir in human ART-naive HIV-1 patients and were flagged as low relevance (grade C) — likely TxGNN knowledge-graph noise from disease-node proximity rather than genuine efavirenz evidence for this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Compared dolutegravir + abacavir/lamivudine vs. Atripla (contains efavirenz) in ART-naive human HIV-1 patients. **Low relevance (grade C)**: studies dolutegravir, not efavirenz; unrelated to feline AIDS. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dolutegravir dose-selection study in ART-naive human HIV-1 patients. **Low relevance (grade C)**: does not involve efavirenz or feline AIDS. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural study | Journal of Veterinary Science | Compared NNRTIs (nevirapine, efavirenz, rilpivirine) against feline vs. human immunodeficiency virus reverse transcriptase to assess theoretical potential for treating FIV infection in cats; no infected-cell or animal efficacy data. |

## US Market Information

Efavirenz currently has no marketing authorization record in this evidence pack (market status: not marketed; 0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a single in vitro structural/biochemical study, with no infected-cell, animal, or veterinary safety/dosing data for efavirenz in FIV; the associated clinical trials in the evidence pack are unrelated (different drug, human indication) and likely reflect knowledge-graph noise rather than genuine support.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action via DrugBank API — currently high priority gap (DG002)
- In vitro antiviral (cell-based) and in vivo animal efficacy data specific to FIV
- Veterinary pharmacokinetic, dosing, and safety data (no existing feline formulation or exposure data)
- Note: a related candidate, simian immunodeficiency virus infection (rank 2, L3/S1, "Research Question"), has stronger supporting evidence (multiple in vivo primate studies directly testing efavirenz) and may be a more productive line of investigation if a lentivirus-model indication is of interest.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

