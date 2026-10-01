---
layout: default
title: Atorvastatin
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Atorvastatin: From Hyperlipidemia (label text not supplied) to Familial Hypercholesterolemia

## One-Sentence Summary

Atorvastatin is a statin (HMG-CoA reductase inhibitor) marketed in the US as many generic products. The supplied license data do not include the approved indication text.
The TxGNN model predicts it may be effective for **familial hypercholesterolemia (FH)**, with **35 clinical trials** (most of them combination or background-therapy studies) and **19 publications** currently supporting this direction.
This is probably an already-established use rather than true repurposing, so the label status should be verified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (all approved-indication fields in the license data are empty) |
| Predicted New Indication | Familial hypercholesterolemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 (see caveat under Clinical Trial Evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all five listed licenses are ANDA generics) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The supplied mechanism-of-action field is empty. Based on the pack's mechanistic analysis, atorvastatin inhibits HMG-CoA reductase, which upregulates hepatic LDL receptors and lowers LDL cholesterol. This is a direct, established mechanism for FH caused by LDL-receptor dysfunction.

The relationship between the original and new indication is close. Both are disorders of elevated LDL cholesterol, and FH is the genetic form of the same problem statins are designed to treat. Because the original-indication field is empty, this is probably an already-labeled use rather than a true repurposing case.

There is one mechanistic limit. Response in homozygous FH is limited because statins depend on residual LDL-receptor function. This is why trials in that population add ezetimibe, PCSK9 inhibitors, or other agents on top of atorvastatin.

## Clinical Trial Evidence

Atorvastatin is usually background therapy or a comparator in these trials, so they mainly show the combination or the population rather than atorvastatin alone. The ten most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | 3-year open-label study of atorvastatin in children and adolescents with heterozygous FH, tracking growth, development and cholesterol reduction |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Completed | 39 | 8-week open-label PK/PD and safety study of atorvastatin in pediatric heterozygous FH (supports dosing and safety, not efficacy) |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Phase 3 | Completed | 400 | Torcetrapib/atorvastatin vs maximally tolerated atorvastatin alone in heterozygous FH; the torcetrapib program was terminated for safety findings |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Completed | 800 | 24-month carotid ultrasound trial of torcetrapib/atorvastatin vs atorvastatin alone in heterozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Up to 24 months of long-term safety follow-up of ezetimibe plus atorvastatin or simvastatin in homozygous FH |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Double-blind trial of ezetimibe added to atorvastatin 10 mg in heterozygous FH, CHD, or multiple risk factors |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | Completed | 432 | Up to 12 months of long-term safety of ezetimibe plus atorvastatin 10–80 mg |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Alirocumab added to atorvastatin vs ezetimibe added vs atorvastatin dose increase vs switch to rosuvastatin |
| [NCT02460159](https://clinicaltrials.gov/study/NCT02460159) | Phase 3 | Completed | 135 | Long-term safety of ezetimibe/atorvastatin fixed-dose combination in Japanese patients with hypercholesterolemia |

**Evidence-level caveat:** L1 is met by the number of completed Phase 3 trials, but most are randomized combination or add-on designs. The only atorvastatin-focused Phase 3 study in the list, NCT00827606, is open-label and single-arm. Direct atorvastatin-alone efficacy evidence in FH therefore comes mostly from the literature below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical study (not classified) | J Clin Lipidol | 3-year study of atorvastatin in children and adolescents (from age 6) with heterozygous FH; extends prior trials of up to 1 year on efficacy and safety |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative study (not classified) | Nutr Metab Cardiovasc Dis | Atorvastatin vs simvastatin for reaching the NCEP LDL-C goal in heterozygous FH, with effects on fibrinogen and coagulation variables |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Study (not classified) | J Am Coll Cardiol | Quantifies statin-related reduction in coronary artery disease events and mortality in heterozygous FH |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Clinical study (not classified) | Echocardiography | Atorvastatin effects on myocardial and peripheral blood flow in FH patients without coronary atherosclerosis |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | Review of novel LDL-C-lowering therapies in homozygous FH |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Review of atorvastatin efficacy and safety in primary hypercholesterolemia and mixed dyslipidemias |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia management and cardiovascular prevention |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | Retrospective study | Atherosclerosis | Real-world FH treatment in Slovakia; maximal-dose potent statins are the cornerstone, yet many patients miss LDL-C goals |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic study | Pharmacogenomics J | Combines FH gene panel with statin pharmacogenomics for genotype-guided prescribing |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Preclinical | Toxicology | Lipophilic vs hydrophilic statin myotoxicity in iPSC-derived muscle cells from FH patients with statin-associated muscle symptoms |

## US Market Information

The license data show 20 licenses in total; five are listed. All are ANDA generics, and none includes approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091226 | Atorvastatin Calcium (Mylan Pharmaceuticals Inc.) | Tablet, film coated | Not provided |
| ANDA206536 | atorvastatin calcium (Zydus Pharmaceuticals USA Inc.) | Tablet | Not provided |
| ANDA205300 | Atorvastatin Calcium (Teva Pharmaceuticals USA, Inc.) | Tablet, film coated | Not provided |
| ANDA206536 | atorvastatin calcium (Zydus Lifesciences Limited) | Tablet | Not provided |
| ANDA204991 | Atorvastatin Calcium (Bryant Ranch Prepack) | Tablet | Not provided |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atorvastatin has a direct, well-established mechanism for lowering LDL-C in FH, and many completed Phase 3 trials and clinical studies involve it in FH populations. Most trials test add-on or combination regimens, however, and the missing label and safety data mean this should not be treated as a clean repurposing finding yet.

**To proceed, the following is needed:**
- Verify the current US label to confirm whether FH is already an approved indication. If it is, this is not a repurposing candidate.
- Obtain the package insert warnings and contraindications (blocking data gap DG001), and complete the safety screen.
- Obtain the mechanism-of-action record (DG002), for example from the DrugBank API.
- Separate atorvastatin-alone efficacy from combination-therapy evidence, especially for homozygous FH, where the effect depends on residual LDL-receptor function.
- Consider a pediatric-specific safety review, since much of the atorvastatin-focused evidence is in children and adolescents.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

