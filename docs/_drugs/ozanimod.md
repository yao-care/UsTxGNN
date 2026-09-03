---
layout: default
title: Ozanimod
parent: 僅模型預測 (L5)
nav_order: 1006
evidence_level: L5
indication_count: 1
---

# Ozanimod
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

# Ozanimod: From Relapsing Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

> Ozanimod is a sphingosine-1-phosphate (S1P) receptor modulator originally approved for relapsing forms of multiple sclerosis.
> The TxGNN model predicts it may also be effective for **Progressive Relapsing Multiple Sclerosis**,
> with **8 clinical trials** and **18 publications** currently informing this direction — though most evidence addresses relapsing MS broadly rather than this specific progressive subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of multiple sclerosis (RMS) — per literature evidence (PMID 32385738); Taiwan-specific license data is not yet available |
| Predicted New Indication | Progressive Relapsing Multiple Sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L2 (1 completed Phase 3 RCT — NCT02576717 [RADIANCE], n=2494) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A structured DrugBank mechanism-of-action entry is not available in this evidence pack. However, the accompanying literature and repurposing rationale converge on a well-characterized mechanism: ozanimod is a selective S1P1/S1P5 receptor modulator. By functionally antagonizing S1P1 on lymphocytes, it triggers receptor internalization, trapping autoreactive T and B lymphocytes in lymph nodes and preventing their egress into peripheral circulation and subsequent infiltration into the central nervous system — thereby reducing inflammatory disease activity.

This mechanism is well established for its original indication, relapsing MS, where inflammatory relapses driven by peripheral lymphocyte trafficking are the dominant pathology. "Progressive relapsing multiple sclerosis" (PRMS) was a pre-2013 clinical classification for MS with steady progression punctuated by occasional relapses; under current classification systems, this presentation is largely subsumed into "active secondary progressive MS" (active SPMS) or elements of primary progressive MS (PPMS).

Because ozanimod's mechanism primarily targets peripheral immune cell trafficking — the process driving *relapse activity* — it is mechanistically most applicable when a progressive MS course still shows inflammatory/relapsing activity, and less clearly applicable to pure neurodegenerative progression without relapses. This distinction is the key reason evidence for this specific predicted indication should be regarded as indirect rather than confirmatory, and is reflected in the "Proceed with Guardrails" recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | Completed | 2,494 | RADIANCE trial — RCT of oral ozanimod vs. IFN β-1a in relapsing MS; pivotal trial supporting original approval, but population was general RRMS, not PRMS-specific |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS — compares early intensive vs. escalation DMT strategies in RRMS; strategy comparison, not indication-specific |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A (Pragmatic) | Active, not recruiting | 900 | TREAT-MS — pragmatic trial of early aggressive vs. escalation therapy for relapsing-phase disability prevention |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | Active, not recruiting | 84 | Single-arm, open-label study of oral ozanimod effectiveness/safety in Chinese RMS patients |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Recruiting | 60 | Predicts disease activity and rebound risk after S1P receptor modulator treatment — mechanistically relevant to post-treatment disease course |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Active, not recruiting | 9,000 | ORION — post-authorization, multinational, real-world long-term safety study of ozanimod vs. other S1P modulators/DMTs in RRMS |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by invitation | 323 | STATURE — observational study of treatment burden/adherence across six oral DMTs including ozanimod |
| [NCT05688436](https://clinicaltrials.gov/study/NCT05688436) | N/A | Recruiting | 1,178 | Pregnancy outcomes study for diroximel fumarate (different drug); provides MS population safety background only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network Meta-Analysis (Cochrane) | Cochrane Database Syst Rev | Compares immunomodulators/immunosuppressants specifically in progressive MS; relative efficacy and safety remain unclear due to lack of head-to-head trials |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network Meta-Analysis (Cochrane) | Cochrane Database Syst Rev | Updated Cochrane review of immunomodulators/immunosuppressants for RRMS; confirms relapse reduction and disability benefit vs. no treatment across drug classes |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review | Drugs | "Ozanimod: First Approval" — documents 2020 FDA/EU approval for relapsing forms of MS including active secondary progressive disease |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurology International | Comprehensive review of ozanimod efficacy, disease context, and side-effect profile in relapsing MS |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | Update on S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) for relapsing MS |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Class review of S1P receptor modulators for MS, covering mechanism and comparative development history |
| [30410033](https://pubmed.ncbi.nlm.nih.gov/30410033/) | 2018 | Review | Nat Rev Dis Primers | Foundational MS overview describing disease heterogeneity, immune-mediated pathogenesis, and relapsing vs. progressive phenotypes |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Reviews therapeutic developments specifically for progressive MS, directly relevant to the predicted indication |
| [32059809](https://pubmed.ncbi.nlm.nih.gov/32059809/) | 2020 | Review | Lancet Neurology | Reviews oral immunomodulating therapies (including ozanimod) for relapsing MS |
| [41919069](https://pubmed.ncbi.nlm.nih.gov/41919069/) | 2026 | Real-World Evidence (Registry) | Ther Adv Neurol Disord | MSBase registry study comparing anti-CD20 therapies vs. S1P receptor modulators in late-onset MS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ozanimod's S1P-modulator mechanism and its regulatory approval for relapsing/active MS provide plausible biological rationale, and one completed Phase 3 RCT (RADIANCE) supports efficacy in relapsing disease. However, essentially all trial and literature evidence addresses relapsing MS broadly rather than "progressive relapsing MS" specifically — a classification that is largely obsolete under current diagnostic criteria — so the indication-specific evidence remains indirect.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently a blocking data gap (DG001)
- Structured DrugBank mechanism-of-action confirmation (DG002)
- Clinical clarification on whether TxGNN's "progressive relapsing MS" label maps to current active SPMS/PPMS diagnostic categories before advancing further
- Taiwan market authorization pathway assessment, since the drug is not currently marketed locally (0 NDAs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

