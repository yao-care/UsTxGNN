---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

Using `txgnn-pipeline` to orient context — this is a US TxGNN evidence pack (candidate `TW-DB00537-multi`) for ciprofloxacin. Now generating the report per v5 format.

---

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic used to treat a wide range of bacterial infections, including urinary tract, respiratory, and skin infections.
The TxGNN model predicts it may be effective for **Diffuse Scleroderma**, supported by a **dual antifibrotic and gut microbiome mechanism hypothesis**,
with **0 registered clinical trials** and **2 publications** currently available for this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (urinary tract, respiratory tract, skin, bone, and gastrointestinal infections) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Taiwan Market Status | Not found in TFDA database (0 licenses retrieved) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured data source. Based on well-established pharmacological knowledge, ciprofloxacin is a second-generation fluoroquinolone antibiotic that inhibits bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV, thereby blocking bacterial DNA replication and causing cell death. Its broad-spectrum bactericidal activity against both Gram-negative and Gram-positive organisms is extensively documented.

The mechanistic link to diffuse scleroderma (SSc) rests on a **dual-mechanism hypothesis**. The first is an **antifibrotic effect**: ciprofloxacin has been shown to inhibit dermal fibroblast proliferation and collagen synthesis independently of its antibacterial activity, likely through modulation of the TGF-β signaling pathway. This is mechanistically relevant because SSc is fundamentally a disease of excessive fibrosis — overactivated fibroblasts drive the hallmark skin thickening and visceral organ involvement. The second mechanism involves **gut microbiome modulation**: SSc patients have a high prevalence of small intestinal bacterial overgrowth (SIBO), and ciprofloxacin's ability to suppress intestinal bacterial burden may indirectly attenuate the systemic immune-inflammatory cascade that perpetuates SSc pathology.

Both mechanistic arms offer moderate biological plausibility. A 2010 pilot double-blind randomized controlled trial (PMID 20507401) provides initial human-level evidence that oral ciprofloxacin can reduce fibrosis severity in SSc skin — making this TxGNN prediction scientifically interesting. However, the evidence base remains thin, with no registered Phase 2 or 3 trials, and substantial validation work is required before this can be considered a viable clinical repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ciprofloxacin in diffuse scleroderma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Pilot RCT | The Journal of Dermatology | Controlled double-blind randomized trial evaluating oral ciprofloxacin as an antifibrotic agent in SSc patients; assessed whether it reduces skin fibrosis severity via mechanisms independent of antibacterial activity |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Clinical Study | British Journal of Rheumatology | Investigated SIBO detection (jejunal aspiration) and treatment outcomes in 24 SSc patients with malabsorption symptoms; supports the gut microbiome modulation rationale for ciprofloxacin use in systemic sclerosis |

---

## Taiwan Market Information

No Taiwan FDA (TFDA) licenses were retrieved for ciprofloxacin in the current database query (result count: 0). This likely reflects a data retrieval or nomenclature limitation rather than actual non-availability, as ciprofloxacin is a globally ubiquitous antibiotic available in multiple formulations. **Verification against the full TFDA database is recommended.**

---

## Safety Considerations

Full safety data (warnings, contraindications, drug interactions) was not available in this evidence pack.

> ⚠️ **Clinically Critical Note**: Fluoroquinolones, including ciprofloxacin, carry an **FDA Black Box Warning** for peripheral neuropathy that may be irreversible. This is especially relevant to this evaluation: rank #9 in the predicted indication list involves a hematological disease with acquired peripheral neuropathy — ciprofloxacin use in that context would represent a **direct mechanistic contraindication** and should be actively excluded from further evaluation.

Please refer to the package insert for complete warnings, contraindications, and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological hypothesis (antifibrotic + gut microbiome dual mechanism) is scientifically coherent and supported by one small pilot RCT, but with no registered Phase 2/3 trials and only 2 publications directly relevant to SSc, the current evidence base (L4) is insufficient to justify active development investment. Additional mechanistic and clinical validation must precede any resource commitment.

**To proceed, the following is needed:**

- **Phase 2 proof-of-concept trial**: A properly powered RCT evaluating ciprofloxacin's antifibrotic efficacy in SSc patients, with skin biopsy endpoints (collagen density, fibroblast activity)
- **Mechanistic validation**: In vitro and in vivo studies confirming TGF-β pathway involvement independent of antibacterial activity
- **MOA data completion**: Retrieve full DrugBank mechanism data (DrugBank ID: DB00537) to close the current High-severity data gap
- **Taiwan regulatory verification**: Re-query TFDA database using alternative search terms (brand names, CAS number) — current 0-result return is likely a search artifact
- **Safety profiling**: Formal assessment of fluoroquinolone-class risks (tendinopathy, QT prolongation, peripheral neuropathy, phototoxicity) in the context of SSc patient population
- **SIBO sub-study**: Enrich trial population for SSc patients with confirmed SIBO to test the gut microbiome mechanism arm separately

---

> 📌 **Cross-Indication Note**: Among the 10 predicted indications evaluated in this pack, two findings stand out:
>
> - **Septicemic Plague** (rank #10, 99.64%): Already **FDA-approved** with L1 evidence (1 completed Phase 2 RCT + multiple non-inferiority RCTs including NEJM 2025). This validates TxGNN's ability to correctly identify known high-confidence associations.
> - **Monoclonal Gammopathy** (rank #8, 99.71%): L3 evidence for ciprofloxacin as **infection prophylaxis** in multiple myeloma/lymphoma patients undergoing autologous stem cell transplantation. The scoring panel rates this as "Proceed with Guardrails" — note that this is an *infection prevention* application, not a disease-modifying therapy for the gammopathy itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

