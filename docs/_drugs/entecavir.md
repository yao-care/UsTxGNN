---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 656
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

> Entecavir is a guanosine nucleoside analogue originally developed and used to suppress hepatitis B virus (HBV) reverse transcriptase in chronic hepatitis B. TxGNN's top-ranked prediction proposes **Chronic Hepatitis C Virus Infection** as a new indication with a very high similarity score, but a closer review of the underlying **40 clinical trials** and **20 publications** shows essentially none of them test entecavir against HCV — they are HBV trials and HBV/HCV-coinfection observations linked through knowledge-graph proximity, not a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Taiwan/US regulatory license data available in this evidence pack (drug not currently marketed, 0 licenses); known pharmacological indication is Chronic Hepatitis B (HBV) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original-MOA data was not returned by DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). However, the evidence pack's own mechanistic annotations establish entecavir's core pharmacology: it is a cyclopentyl guanosine analogue that, after intracellular triphosphorylation, competitively inhibits the three functions of HBV reverse transcriptase — DNA priming, negative-strand reverse transcription, and positive-strand DNA synthesis. This is entecavir's primary, approved mechanism against HBV (a DNA virus).

Hepatitis C virus, by contrast, is a single-stranded RNA virus whose replication depends on an RNA-dependent RNA polymerase (NS5B) that is structurally and mechanistically unrelated to HBV's reverse transcriptase. There is no known biochemical basis for entecavir to inhibit HCV replication.

Reviewing the supporting evidence, every clinical trial and nearly every publication returned for this candidate actually studies entecavir in **HBV** patients, or describes HCV *reactivation*/*co-infection* phenomena in HBV patients who happen to be on entecavir — not entecavir being used to treat HCV itself. The evidence pack's own rationale concludes this is most likely a **false positive driven by HBV/HCV knowledge-graph proximity** rather than a real repurposing opportunity. Notably, TxGNN's rank-2 prediction for this same drug — "hepatitis B virus infection" — is scored L1/Proceed-with-Guardrails and is, in fact, entecavir's real, approved indication rather than a novel repurposing candidate (see Conclusion).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | QL-007 combined with entecavir/tenofovir in chronic **HBV** (not HCV); graded C — not relevant to an HCV indication |
| [NCT01179594](https://clinicaltrials.gov/study/NCT01179594) | Phase 4 | Withdrawn | 0 | Pegasys ± entecavir in HBeAg-negative chronic **HBV**; entecavir not the primary study drug; graded C |
| [NCT05005507](https://clinicaltrials.gov/study/NCT05005507) | Phase 2 | Terminated | 1 | JNJ-73763989 + nucleos(t)ide analog + PegIFN in chronic **HBV**; terminated at enrollment of 1 |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Entecavir vs. lamivudine dose-response in Japanese chronic **HBV** patients |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys + entecavir vs. entecavir alone in HBeAg-positive chronic **HBV**; graded C — unrelated to HCV |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Phase 3 | Unknown | 120 | Tenofovir vs. lamivudine for **HBV** with severe acute exacerbation (Taiwan) |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Completed | 160 | RO7020531 safety/PK study, including a 6-week chronic **HBV** treatment arm |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Entecavir vs. adefovir early viral kinetics in nucleoside-naive chronic **HBV** |
| [NCT02589652](https://clinicaltrials.gov/study/NCT02589652) | N/A | Unknown | 294 | Peg-IFN switch/sequential therapy after long-term entecavir in chronic **HBV** |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Telbivudine vs. entecavir HBV DNA kinetics over 12 weeks in **HBV** |

⚠ All 10 trials above study entecavir in Hepatitis B, not Hepatitis C. Of the 40 trials returned by the evidence query for this candidate, none directly test entecavir as an HCV treatment — consistent with the false-positive assessment above.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation in anti-HCV antibody-positive chronic HBV patients undergoing nucleos(t)ide analogue (incl. entecavir) therapy — describes reactivation risk, not HCV treatment |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Overview of chronic Hepatitis B and C treatment landscapes as parallel, separate disease entities |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in managing HBV/HCV co-infection; discusses sequencing of therapy, not entecavir's anti-HCV activity |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World J Gastroenterol | HBV and alcohol as HCC risk factors; HCV mentioned only as a comparator etiology |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Pediatric management of HBV and HCV infection, discussed separately |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Review | Chin Clin Oncol | Timing of HBV/HCV antiviral therapy in patients with hepatocellular carcinoma |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral medications (including entecavir for HBV) and renal effects; HCV therapies listed separately |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Pract Res Clin Gastroenterol | Fibrosis regression under antiviral therapy in chronic viral hepatitis, HBV-focused |
| [38631661](https://pubmed.ncbi.nlm.nih.gov/38631661/) | 2024 | Mechanistic | Antiviral Research | YY1 transcription factor and HBV replication regulation — HBV-specific mechanism, no HCV relevance |
| [39351520](https://pubmed.ncbi.nlm.nih.gov/39351520/) | 2024 | Review | World J Hepatol | Metabolomics for liver disease diagnostics in general, not entecavir/HCV-specific |

⚠ None of the retrieved literature reports entecavir exhibiting antiviral activity against HCV; the recurring theme is HBV/HCV co-infection management or reactivation surveillance.

---

## US Market Information

Entecavir is not currently marketed under this evidence pack's regulatory dataset (`total_licenses: 0`, no license records available), so no authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Entecavir has no known mechanistic basis for treating HCV (an RNA virus reliant on NS5B polymerase, unrelated to HBV reverse transcriptase), and all retrieved clinical trials and literature involve entecavir's actual indication (HBV) or HBV/HCV co-infection contexts rather than HCV treatment itself. The evidence pack's own analysis attributes this prediction to knowledge-graph proximity between HBV and HCV nodes, not a genuine repurposing signal.

**To proceed, the following is needed:**
- In vitro or biochemical evidence of direct anti-HCV activity (e.g., HCV replicon assay data) before this candidate can be reconsidered
- Detailed DrugBank mechanism-of-action data (currently a data gap, DG002) to formally rule out any secondary antiviral activity
- TFDA/FDA label warnings and contraindications (currently a Blocking data gap, DG001), required before any safety pre-assessment (S1) can proceed

**Note:** This evidence pack's rank-2 prediction, "hepatitis B virus infection" (score 99.85%, Evidence Level L1, decision stage S3, recommendation **Proceed with Guardrails**), is supported by multiple completed Phase 3 RCTs (e.g., NCT00410202, DEFINE study, n=629) and reflects entecavir's actual, already-established clinical use rather than a novel candidate. If the goal is to identify a genuinely actionable indication for this drug, that entry — not chronic HCV — is the substantiated one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

