---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 923
evidence_level: L5
indication_count: 1
---

# Micafungin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Micafungin: From Invasive Candidiasis to Urinary Tract Infection (Candiduria)

## One-Sentence Summary

Micafungin is an echinocandin antifungal established for invasive and esophageal candidiasis. The TxGNN model predicts it may be effective for **urinary tract infection (candiduria)**, a prediction currently supported by **13 publications** (case reports, case series, and two retrospective/prospective cohort studies) but **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive candidiasis (echinocandin antifungal class) — no Taiwan license text available, as the drug is not currently marketed there |
| Predicted New Indication | Urinary Tract Infection (Candiduria) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 (observational/cohort studies + case series; no RCTs) |
| US Market Status | Not Marketed (0 Taiwan NDA/licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the current evidence pack. Based on known pharmacology, micafungin belongs to the echinocandin class, which acts by inhibiting β-(1,3)-D-glucan synthase, disrupting fungal cell wall synthesis. Its fungicidal activity against a broad range of *Candida* species — including azole-resistant strains such as *C. krusei* and *C. glabrata* — is well established and underlies its approved use in invasive and esophageal candidiasis.

The predicted new indication, urinary tract infection, is caused by the same pathogen class (*Candida* spp.) simply localized to the urinary tract rather than the bloodstream or systemic sites. Mechanistically, the antifungal activity that clears systemic candidiasis is directly applicable to candiduria, provided adequate drug concentration reaches the urine.

Historically, echinocandins were considered poor choices for candiduria due to low renal excretion and low unbound urinary drug levels. However, the literature evidence below (e.g., Grau 2016) specifically challenges this assumption, reporting that urinary micafungin concentrations are in practice sufficient to eradicate *Candida* UTIs, including fluconazole-resistant isolates. This mechanistic reappraisal is a plausible basis for the TxGNN prediction, even though it runs counter to traditional prescribing guidance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | International Urology and Nephrology | Micafungin achieved candiduria eradication in the majority of hospitalized patients treated |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Retrospective Cohort | Antimicrobial Agents and Chemotherapy | Characterized candiduria management in 305 hospitalized patients; flagged antifungal overtreatment of asymptomatic candiduria |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Case Series | International Journal of Antimicrobial Agents | 6 UTI cases (including fluconazole-resistant *Candida*) successfully treated; urinary levels sufficient despite low renal excretion |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Medical Mycology Case Reports | 5 candiduria cases resolved with parenteral micafungin within 30 days |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Case Series | Pediatrics International | Pediatric ICU patients with hospital-acquired *Candida* UTI treated with micafungin; species-specific success rates reported |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report / Review | Transplant Infectious Disease | Successful eradication of fluconazole-resistant *C. krusei* UTI with increased-dose micafungin in a liver-kidney transplant recipient |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report | Frontiers in Pediatrics | Micafungin successfully treated *C. glabrata* urinary infection in a premature neonate |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | Multidrug-resistant *C. auris* UTI managed in a nursing-home patient with multiple comorbidities |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Case Report | Journal of Pharmaceutical Health Care and Sciences | *C. glabrata* pyelonephritis and bacteremia in an SGLT2-inhibitor patient, successfully treated with micafungin |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case Report | Medical Mycology Case Reports | Unilateral renal fungus ball caused by *C. glabrata*, sensitive to micafungin, treated with antifungal therapy and endoscopic extraction |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and supported by a consistent body of case-level and small cohort evidence, but there are no registered clinical trials for this indication, the drug is not currently marketed in Taiwan, and safety data (warnings, contraindications, DDI) are entirely unavailable — including a **Blocking**-severity gap on TFDA label information that prevents a safety pre-screen (S1) from being completed.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety pre-screen
- Mechanism of action confirmation from DrugBank (DG002)
- A prospective or registry-based study (ideally a controlled cohort) specifically evaluating micafungin for candiduria, to move beyond case-report-level evidence
- Confirmation of Taiwan market/import pathway, since the drug currently has zero local licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

