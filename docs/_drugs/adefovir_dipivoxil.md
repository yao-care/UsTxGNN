---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

---

# Adefovir Dipivoxil: From Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Adefovir dipivoxil is an oral nucleotide analogue antiviral historically approved for chronic hepatitis B virus (HBV) infection, whose US market authorization has since been withdrawn.
The TxGNN model ranks **chronic hepatitis C virus infection** as its top new indication with a prediction score of **99.97%**;
however, critically, **zero clinical trials** directly evaluate adefovir against HCV, and no mechanistic basis exists for cross-activity against an RNA virus — suggesting this high-scoring prediction reflects knowledge graph co-infection linkages rather than genuine antiviral efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatitis B virus infection (historically approved; withdrawn from US market) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology documented across the retrieved literature, adefovir dipivoxil is a prodrug hydrolyzed in vivo to adefovir, which is then phosphorylated intracellularly to its active form — adefovir diphosphate (PMEApp). PMEApp competitively inhibits the HBV DNA polymerase (viral reverse transcriptase), causing DNA chain termination and blocking the pgRNA→rcDNA replication step central to HBV persistence. This mechanism was validated in multiple Phase 3 trials and led to FDA approval as Hepsera. The drug has since been largely superseded by tenofovir and entecavir.

Hepatitis C virus (HCV) is a positive-sense single-stranded RNA virus whose replication depends entirely on the NS5B RNA-dependent RNA polymerase (RdRp) — an enzyme with no structural homology to HBV DNA polymerase. Adefovir diphosphate has no known inhibitory activity against NS5B RdRp, and there is no published preclinical or clinical evidence of adefovir reducing HCV viral load.

The TxGNN score of 99.97% most likely arises from indirect epidemiological linkages in the training knowledge graph: patients co-infected with HBV and HCV frequently appear in clinical trial records alongside adefovir, creating spurious disease–drug proximity. This interpretation is strongly supported by the evidence retrieval results — all 9 clinical trials and all 15 literature records returned for this predicted indication are HBV-focused, with none demonstrating anti-HCV activity of adefovir.

---

## Clinical Trial Evidence

> ⚠️ No clinical trials directly evaluating adefovir dipivoxil for chronic hepatitis C were identified. All retrieved trials involve adefovir in HBV or HBV/HIV co-infection contexts.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00051077](https://clinicaltrials.gov/study/NCT00051077) | Phase 2 | Withdrawn | 0 | Adefovir + PEG-IFN + ribavirin in HBV/HCV/HIV triple-infected patients — the only trial explicitly including HCV, but withdrawn with zero enrollment; no efficacy data generated |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Interferon α-2b + ribavirin in chronic hepatitis B; the combination mirrors standard HCV therapy but adefovir is not the study drug and the population is HBV |
| [NCT00973219](https://clinicaltrials.gov/study/NCT00973219) | N/A | Completed | 151 | Peg-IFN alfa-2a + adefovir vs. peg-IFN + tenofovir in HBeAg-negative HBV patients with low viral load; no HCV relevance |
| [NCT00371761](https://clinicaltrials.gov/study/NCT00371761) | Phase 3 | Completed | 25 | PegIntron vs. adefovir in HBeAg-positive chronic hepatitis B (Taiwan); comparative efficacy, no HCV component |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys + entecavir vs. entecavir vs. Pegasys in HBeAg-negative HBV; adefovir cited as one of seven approved CHB agents only |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | Completed | 104 | Antiviral effect of adefovir at 12 and 52 weeks in Korean patients with compensated chronic HBV |
| [NCT00645294](https://clinicaltrials.gov/study/NCT00645294) | Phase 1/2 | Completed | 47 | Pharmacokinetics and safety of a single adefovir dose in children and adolescents aged 2–17 with chronic HBV |
| [NCT02560649](https://clinicaltrials.gov/study/NCT02560649) | Phase 4 | Unknown | 324 | Response-guided therapy (RGT) strategy in HBV patients on nucleoside analogues to improve HBsAg clearance |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | Unknown | 600 | Ten-year observational study on the impact of early vs. conventional antiviral treatment on HBV long-term prognosis |

---

## Literature Evidence

> ⚠️ All retrieved publications discuss adefovir exclusively in the context of HBV treatment. None provide direct evidence of anti-HCV activity.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral medications for HBV and HCV and renal effects; adefovir and tenofovir discussed solely as HBV agents; FDA-approved HCV therapies listed separately |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatments for chronic hepatitis B and C; pegylated interferon reviewed as therapy of choice for both, adefovir only for HBV |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | Chronic viral hepatitis treatment strategies; adefovir and lamivudine for HBV, interferon + ribavirin for HCV — no cross-indication evidence |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Med Chem | Bicyclol as a novel candidate for HBV and HCV; adefovir cited only as a benchmark HBV comparator |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Review | Dig Dis | Established and emerging therapies for HBV and HCV; adefovir dipivoxil listed exclusively under licensed HBV drugs |
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Pat Anti-Infect Drug Discov | Five approved HBV drugs including adefovir reviewed; HCV treatment discussed separately with distinct drug classes |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orvosi Hetilap | Hungarian consensus guidelines for diagnosis and treatment of hepatitis B, C, and D; adefovir cited within HBV section |
| [25892855](https://pubmed.ncbi.nlm.nih.gov/25892855/) | 2015 | Clinical Study | Mediators Inflamm | Differential B-cell subtype expression in chronic HBV and HCV patients before and after antiviral therapy |
| [32289307](https://pubmed.ncbi.nlm.nih.gov/32289307/) | 2020 | Case Report | Am J Med | Adefovir-induced Fanconi syndrome causing hypophosphatemic osteomalacia — key signal for renal proximal tubule toxicity during long-term adefovir use |
| [16880074](https://pubmed.ncbi.nlm.nih.gov/16880074/) | 2006 | Review | Gastroenterol Clin N Am | Pathway to recovery from HBV through antiviral treatment; new nucleotide analogues including adefovir evaluated for HBV outcomes |

---

## Safety Considerations

Please refer to the package insert for safety information.

A clinically important safety signal identified in the retrieved literature: long-term adefovir use (10 mg/day for HBV) is associated with **renal proximal tubule toxicity**, including Fanconi syndrome and hypophosphatemic osteomalacia (PMID [32289307](https://pubmed.ncbi.nlm.nih.gov/32289307/)). This toxicity is dose-dependent and was severe enough at HIV-required doses (60–120 mg/day) to prompt FDA rejection of the HIV indication despite demonstrated antiviral activity. Any repurposing effort must account for this renal risk, particularly in long-duration treatment scenarios.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Adefovir dipivoxil inhibits HBV DNA polymerase (a reverse transcriptase), but HCV replicates exclusively via the NS5B RNA-dependent RNA polymerase — a fundamentally different enzyme with no structural homology to HBV's target. No clinical trials, preclinical studies, or direct literature support anti-HCV activity of adefovir. The TxGNN score of 99.97% reflects knowledge-graph co-infection proximity, not biological plausibility.

**To proceed, the following is needed:**

- **Mechanistic investigation:** In vitro biochemical assays to determine whether PMEApp (adefovir diphosphate) has any measurable inhibitory activity against HCV NS5B RdRp
- **Structural analysis:** Assessment of any structural homology between HBV DNA polymerase and HCV NS5B that might support cross-reactivity
- **Model audit:** Review of TxGNN knowledge graph edges to determine whether the HBV/HCV co-infection context is inflating prediction scores for mechanistically unrelated disease–drug pairs
- **Alternative redirection:** For a clinically actionable repurposing target, the evidence within this pack strongly favors **hepatitis B virus infection** (rank 6, L1 evidence, multiple Phase 3 RCTs, "Proceed with Guardrails" recommendation) as the focus of any further regulatory or formulary work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

