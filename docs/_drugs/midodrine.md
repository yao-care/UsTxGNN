---
layout: default
title: Midodrine
parent: 僅模型預測 (L5)
nav_order: 926
evidence_level: L5
indication_count: 10
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Broader Hypotensive Disorder Management

## One-Sentence Summary

Midodrine is an established peripheral alpha-1 adrenergic agonist used internationally for neurogenic orthostatic hypotension. The evidence pack's top TxGNN-ranked predictions (prion disease, faciodigitogenital syndrome, ADHD, monogenic obesity, developmental disorder, hypertelorism, sinoatrial disorders) are explicitly flagged by the pack's own rationale notes as high-score false positives with no mechanistic or clinical support, so this report instead evaluates the one candidate with substantive evidence: **Hypotensive Disorder**, a broader category covering dialysis-associated, perioperative, spinal-cord-injury (SCI)-associated, and heart-failure-associated hypotension, supported by **9 clinical trials** and **19 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this market's regulatory data (drug not locally marketed); internationally established for (neurogenic) orthostatic hypotension |
| Predicted New Indication | Hypotensive Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

`original_moa` is flagged as a data gap in this evidence pack. However, literature within the pack itself (McTavish & Goa, 1989, PMID 2480881) describes midodrine as a peripheral alpha-adrenergic agonist whose active metabolite, desglymidodrine, raises standing blood pressure through vasoconstriction. This is independently corroborated by the pack's own rationale notes on the discarded predictions (e.g., "midodrine 本身無中樞作用，僅為周邊 alpha-1 促效劑"), which consistently describe it as a peripherally-restricted, non-CNS-penetrant vasopressor.

"Hypotensive disorder" is not a mechanistically novel target — it is the broader disease category that midodrine's established pharmacology already addresses. The clinical trial evidence shows the model correctly recovering related, more specific hypotensive syndromes: intradialytic hypotension in critically ill AKI patients, orthostatic hypotension after spinal-cord injury, post-spinal-anesthesia hypotension in hip arthroplasty, and hypotension in HFrEF. Because these all share the same vasoconstrictive mechanism as midodrine's known indication, the prediction reads as a mechanistically coherent extension rather than a speculative new use — unlike the other nine ranked candidates in this pack, which have no plausible pharmacological link and are explicitly labeled as noise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03431194](https://clinicaltrials.gov/study/NCT03431194) | NA | Completed | 80 | Randomized trial of oral midodrine for intradialytic hypotension in critically ill AKI patients |
| [NCT05548985](https://clinicaltrials.gov/study/NCT05548985) | NA | Completed | 58 | RCT of oral midodrine for prophylaxis against post-spinal-anesthesia hypotension in elderly hip arthroplasty patients |
| [NCT02307565](https://clinicaltrials.gov/study/NCT02307565) | Phase 3 | Completed | 19 | Midodrine-driven BP elevation improves cerebral blood flow and cognition in SCI |
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | Completed | 21 | Normalizing BP improves cerebral blood flow in chronic hypotensive SCI patients |
| [NCT03037879](https://clinicaltrials.gov/study/NCT03037879) | NA | Completed | 10 | 30-day midodrine-driven BP elevation to treat cognitive deficits in SCI |
| [NCT01030874](https://clinicaltrials.gov/study/NCT01030874) | NA | Completed | 356 | Multidisciplinary intervention for orthostatic hypotension in rehabilitation unit patients |
| [NCT02307526](https://clinicaltrials.gov/study/NCT02307526) | Phase 2 | Completed | 10 | Acetylcholinesterase inhibition as an alternative approach to orthostatic hypotension in SCI (comparator context, not midodrine itself) |
| [NCT06405555](https://clinicaltrials.gov/study/NCT06405555) | Phase 2/3 | Not yet recruiting | 56 | Pilot open-label RCT of midodrine for hypotension in HFrEF |
| [NCT05839652](https://clinicaltrials.gov/study/NCT05839652) | Phase 4 | Recruiting | 25 | Pharmacological and non-pharmacological treatment of orthostatic hypotension in SCI |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | RCT | Hepatology | Randomized trial: midodrine + octreotide + albumin vs. terlipressin + albumin for hepatorenal syndrome |
| [39619823](https://pubmed.ncbi.nlm.nih.gov/39619823/) | 2024 | RCT | Topics in Spinal Cord Injury Rehabilitation | 30-day midodrine vs. placebo on BP, cerebral blood flow, and cognition in SCI |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Review | Drugs | Foundational review of midodrine pharmacology and use in orthostatic and secondary hypotension |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Guideline | Hypertension | AHA scientific statement on orthostatic hypotension in adults with hypertension |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Expert Position Statement | Revue Neurologique | Review and expert consensus on orthostatic hypotension management |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | Consensus Panel | Journal of Neurology | Consensus recommendations for screening, diagnosis, and treatment of neurogenic OH |
| [31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/) | 2020 | Review | Continuum (Minneapolis, Minn.) | Management of orthostatic hypotension, emphasis on neurogenic OH |
| [35029940](https://pubmed.ncbi.nlm.nih.gov/35029940/) | 2022 | Review | American Family Physician | Practical diagnostic and treatment approach to orthostatic hypotension |
| [12180246](https://pubmed.ncbi.nlm.nih.gov/12180246/) | 2002 | Review | Clinics in Geriatric Medicine | Orthostatic hypotension in elderly patients: evaluation and management |
| [28092986](https://pubmed.ncbi.nlm.nih.gov/28092986/) | 2017 | Review | The Annals of Pharmacotherapy | Efficacy and safety of pharmacological/non-pharmacological treatment of primary OH |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available for this candidate — this is a **blocking gap** for safety review (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The extension from established orthostatic-hypotension use to the broader "hypotensive disorder" category is mechanistically coherent and supported by multiple completed trials, including RCTs of midodrine itself in dialysis-associated, perioperative, and SCI-associated hypotension. However, the drug is not currently marketed in this jurisdiction, and safety labeling (warnings, contraindications) is entirely absent, which blocks a full safety evaluation.

**To proceed, the following is needed:**
- TFDA (or local) package insert with warnings and contraindications — currently a blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Drug interaction (DDI) data, particularly for cardiac conduction risk — none found in current query
- A registration/import pathway assessment, since the product holds zero local licenses
- No further work on the TxGNN top-ranked candidates (prion disease, faciodigitogenital syndrome, ADHD, monogenic obesity, developmental disorder, hypertelorism, sinoatrial node disease/block) — the evidence pack's own rationale confirms these are model artifacts with no clinical or mechanistic support, and sinoatrial conduction disease in particular is a plausible relative *contraindication* (bradycardia risk) rather than an indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

