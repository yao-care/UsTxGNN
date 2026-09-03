---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 1119
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

> Ribavirin is a guanosine-analog antiviral, established clinically in combination with peginterferon for chronic hepatitis C (HCV).
> The TxGNN model predicts it may be effective for **Chronic Hepatitis B Virus Infection**, with **63 clinical trials** and **20 publications** retrieved as candidate evidence —
> however, close review shows most of this evidence actually describes HCV or HCV/HBV co-infection, not HBV monoinfection, and the signal likely reflects knowledge-graph node proximity rather than a genuine mechanistic finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C (HCV), in combination with peginterferon *(TFDA-approved indication text unavailable — see Data Gap DG001)* |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed formal MOA data from DrugBank is not yet available (Data Gap DG002), but based on well-established pharmacology, ribavirin is a guanosine nucleoside analog that inhibits IMPDH (inosine monophosphate dehydrogenase) and interferes with viral RNA polymerase / RNA-capping activity. This gives it broad activity against **RNA viruses**, and its only clinically validated use is in combination with peginterferon for chronic **hepatitis C**, which is an RNA virus.

Hepatitis B virus, by contrast, is a DNA virus that replicates via reverse transcriptase, not RNA-dependent RNA polymerase. This is a fundamental mechanistic mismatch: ribavirin's core antiviral mechanism does not have a clear molecular target in HBV replication. Reviewing the retrieved clinical trial evidence confirms this concern — the large majority of trials tagged to this prediction are actually chronic hepatitis C trials (genotype 1, 2, 3, 4 HCV DAA/interferon combination studies), and several were flagged during grading as likely knowledge-graph mislabeling arising from the shared "chronic viral hepatitis" node neighborhood rather than true HBV studies.

That said, a small number of trials and one supporting publication (PMID 10832679, "Is ribavirin treatment really effective for chronic hepatitis B?") directly address ribavirin/peginterferon-ribavirin use in genuine HBV populations, including one completed Phase 3 RCT (PARC study, NCT00114361) in HBeAg-negative chronic HBV. This keeps the signal from being a pure artifact, but it is not strong enough on its own to justify high confidence — the evidence base is dominated by co-infection and mislabeled HCV studies rather than a coherent HBV-specific efficacy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | PARC study: PegIFN alfa-2a + ribavirin vs. PegIFN monotherapy in HBeAg-negative chronic HBV — the only trial in the evidence set with an unambiguous HBV-monoinfection population. |
| [NCT02339337](https://clinicaltrials.gov/study/NCT02339337) | Phase 4 | Completed | 203 | "Pioneer" study: tailored PegIFN alfa + ribavirin regimen in chronic Hepatitis C/Hepatitis B co-infected (HBeAg-negative) patients. |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | PegIFN alfa-2a + ribavirin in HCV/HBV co-infection vs. chronic HCV alone; treatment optimized primarily for the HCV component. |
| [NCT01401400](https://clinicaltrials.gov/study/NCT01401400) | N/A | Completed | 1350 | GIANT-B study: genetic determinants of response to peginterferon (not ribavirin-specific) in chronic hepatitis B patients. |
| [NCT02731131](https://clinicaltrials.gov/study/NCT02731131) | Phase 2 | Completed | 12 | PegIFN alfa-2a ± ribavirin in chronic Hepatitis D (HDV, a satellite virus dependent on HBV) — relevant to HBV-associated disease but not HBV monoinfection itself. |
| [NCT00944684](https://clinicaltrials.gov/study/NCT00944684) | Phase 2 | Completed | 32 | PegIFN alfa-2a + serum-level-adapted vs. weight-based ribavirin, genotype 1 chronic hepatitis C — HBV relevance unconfirmed; flagged for manual verification. |
| [NCT00378599](https://clinicaltrials.gov/study/NCT00378599) | Phase 3 | Completed | 125 | PROTECT study: PegIFN alfa-2b + ribavirin after liver transplant for hepatitis C recurrence — title suggests HCV, not HBV; flagged for verification. |
| [NCT00630084](https://clinicaltrials.gov/study/NCT00630084) | Phase 4 | Completed | 120 | PegIFN + ribavirin outcomes in chronic hepatitis with concomitant malignancy — virus type (HBV vs. HCV) unclear from title alone. |

*Note: the remaining ~55 trials returned by the search (e.g., NCT00637923, NCT01296451, NCT01852604) describe HCV-specific direct-acting antivirals, HCV vaccines, or HCV genotype studies and were assessed as likely mislabeled to this HBV prediction; they are omitted here as non-informative.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | Review | J Gastroenterol | Directly addresses the question "Is ribavirin treatment really effective for chronic hepatitis B?" — most disease-specific reference in the evidence set. |
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection review; notes pegIFN + ribavirin historically used for the HCV component in dual infection. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment updates and outcomes in dual chronic HCV/HBV infection. |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | Reviews IFN-α ± ribavirin as prototype therapy for both HBV and HCV, contrasted with modern DAA approaches. |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatol Int | Overview of dual chronic HBV and HCV infection, viral interaction dynamics under treatment. |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | Treatment of HBV/HCV co-infection described as "still a challenge for the hepatologist." |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Current treatment strategies for chronic hepatitis B and C, contrasting IFN/lamivudine (HBV) with IFN/ribavirin (HCV). |
| [18414457](https://pubmed.ncbi.nlm.nih.gov/18414457/) | 2008 | Review | Nat Clin Pract Gastroenterol Hepatol | Hepatitis B and C in children — treatment selection criteria discussed separately by virus type. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children. |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Case Report/Review | Nihon Rinsho | HCV-HBV infection overview (Japanese); confirms most effective IFN regimen is combined with ribavirin specifically for the HCV component. |

*Note: nearly all retrieved literature discusses ribavirin's established role in the **HCV component** of HBV/HCV co-infection, not as monotherapy or adjunct for HBV itself — this is a recurring pattern across the evidence set.*

---

## US Market Information

Ribavirin currently has **no marketing authorization records** in this dataset (market status: Not Marketed; 0 licenses on file). No NDA/product table can be generated from available data.

---

## Safety Considerations

Please refer to the package insert for safety information. *(TFDA label warnings/contraindications and DDI data are currently unavailable — see Data Gap DG001, marked Blocking severity.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication carries a high TxGNN score (99.86%, evidence level L2), but the supporting evidence is dominated by HCV or HCV/HBV co-infection studies where ribavirin's role targets the HCV component — not a genuine HBV-specific efficacy signal. Only one trial (NCT00114361, PARC) and one publication (PMID 10832679) directly interrogate ribavirin's effect in HBV monoinfection, and the mechanistic basis (RNA-virus-directed IMPDH inhibition applied to a DNA/reverse-transcriptase virus) is weak.
- The other nine predicted indications for this drug (rank 2–10, e.g., portal vein thrombosis, IgG4-related disease) have no supporting trials or literature and are assessed as likely knowledge-graph node-proximity artifacts rather than genuine repurposing candidates; none warrant further action at this time.

**To proceed, the following is needed:**
- Manual re-adjudication of the ~55 "pending"/Grade-C trials to confirm actual disease population (HBV vs. HCV) before counting them as supporting evidence
- Full-text review of the PARC study (NCT00114361) virologic outcome data to assess whether ribavirin added meaningful benefit over peginterferon monotherapy
- Confirmed DrugBank MOA record (DG002) to formally support or refute mechanistic plausibility for HBV
- TFDA package insert / label data (DG001, Blocking) before any safety-related decision can be made
- Clarification from the KG vendor on whether "chronic viral hepatitis" is being treated as a single node, which would explain the apparent HCV/HBV label bleed-through
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

