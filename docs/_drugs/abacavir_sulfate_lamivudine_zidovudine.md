---
layout: default
title: Abacavir Sulfate Lamivudine Zidovudine
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 0
---

# Abacavir Sulfate Lamivudine Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Abacavir Sulfate + Lamivudine + Zidovudine: Antiretroviral Combination — No Repurposing Prediction Available

## One-Sentence Summary

Abacavir sulfate, lamivudine, and zidovudine form a triple nucleoside reverse transcriptase inhibitor (NRTI) combination (known internationally as Trizivir), originally used for HIV-1 infection treatment.
The TxGNN model **did not generate any repurposing predictions** for this combination, as the drug is not registered in Taiwan's regulatory database and the DrugBank ID could not be resolved.
Without a mapped candidate or predicted indication, a meaningful repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (triple NRTI antiretroviral regimen) |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — pipeline did not produce candidates |
| Market Status | Not marketed in Taiwan |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction is available for this drug combination. The TxGNN pipeline requires a resolvable DrugBank ID to anchor a compound in the knowledge graph; because neither the combination product nor its components were matched from the Taiwan FDA database, the model returned zero candidates.

Mechanistically, abacavir, lamivudine, and zidovudine are all NRTIs. They competitively inhibit HIV-1 reverse transcriptase and act as chain terminators, blocking viral RNA-to-DNA transcription. Lamivudine additionally inhibits hepatitis B virus (HBV) polymerase, an activity that has been independently leveraged for HBV treatment. Zidovudine was the first antiretroviral approved anywhere in the world (US FDA, 1987); abacavir requires pre-treatment HLA-B\*5701 screening to avoid life-threatening hypersensitivity.

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known clinical information, this triple-NRTI combination's activity is confined to RNA-dependent DNA polymerases (reverse transcriptases), limiting direct extrapolation to non-viral oncology or metabolic disease targets without additional mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are linked to a TxGNN-predicted indication, as no prediction was generated for this drug combination.

---

## Literature Evidence

Currently no related literature is linked to a TxGNN-predicted indication for this combination.

---

## Market Information

This drug combination is **not registered in Taiwan**. No Taiwan FDA licenses were found.

> **Reference context (from public regulatory knowledge):**
> Trizivir (abacavir 300 mg + lamivudine 150 mg + zidovudine 300 mg) holds US FDA approval (NDA 021205) for HIV-1 infection in adults whose regimen would otherwise include these three agents. It is not commonly preferred in current guidelines due to inferior virologic performance compared to INSTI-based regimens, but remains available.

---

## Safety Considerations

Package insert data for the Taiwan market is unavailable (drug not registered). The following warnings are drawn from established clinical knowledge for this combination:

- **Abacavir**: Carries a Black Box Warning for potentially fatal hypersensitivity reactions. HLA-B\*5701 genotyping is required before initiation. Cardiovascular risk increase has been reported in observational studies.
- **Abacavir + Zidovudine**: Both carry Black Box Warnings for lactic acidosis and severe hepatomegaly with steatosis (rare but fatal).
- **Zidovudine**: Black Box Warning for hematologic toxicity (severe anemia, neutropenia); prolonged use associated with symptomatic myopathy.
- **Lamivudine**: Severe acute exacerbation of hepatitis B has been reported upon discontinuation in HBV/HIV co-infected patients.

No drug interaction data was returned from the DDI query (query status: not found). Please refer to the US FDA package insert for comprehensive interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero repurposing candidates because this combination product could not be mapped to a DrugBank node in the knowledge graph, making it impossible to generate or evaluate any predicted indication. The drug is also not marketed in Taiwan, removing the regulatory pathway context needed for a repurposing assessment.

**To proceed, the following is needed:**

- Resolve DrugBank IDs for each individual active ingredient (Abacavir: DB01048; Lamivudine: DB00709; Zidovudine: DB00495) and re-run TxGNN predictions at the component level
- Determine whether the evaluation target is the fixed-dose combination (Trizivir) or one of the individual components; individual component predictions may be more tractable
- If Taiwan registration is being considered, obtain TFDA package insert (仿單) data via the TFDA website PDF download method to address the Blocking data gap (DG001)
- Retrieve mechanism of action data from DrugBank API for each component to address data gap DG002 and enable the mechanistic plausibility analysis
- Re-run the Evidence Pack generation pipeline after DrugBank mapping is resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

