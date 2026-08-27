---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 832
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From No Registered Indication (Not Marketed) to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab (DB14597) has no recorded original indication and is currently **not marketed** in this jurisdiction, so no prior therapeutic use can be extracted from the regulatory data on file. The TxGNN model predicts it may be effective for **C1 Inhibitor Deficiency** (the molecular basis of hereditary angioedema, HAE), a signal already backed by **22 clinical trials** and **20 publications** — including a completed pivotal Phase 3 RCT — making this one of the strongest-evidenced predictions in the pipeline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records on file (drug not marketed in this jurisdiction) |
| Predicted New Indication | C1 Inhibitor Deficiency |
| TxGNN Prediction Score | 99.9955% (rank #248 among all predictions) |
| Evidence Level | L2 (1 completed Phase 3 RCT — HELP Study, NCT02586805 — plus a broad supporting Phase 3/real-world program) |
| Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The `original_moa` field is a confirmed data gap, but the evidence pack's own literature record fills part of that gap: PMID 30267321 describes lanadelumab as "a fully human monoclonal antibody that inhibits plasma kallikrein," acting downstream of mutations in the *SERPING1* gene that cause C1 inhibitor deficiency and the resulting uncontrolled bradykinin generation that drives hereditary angioedema (HAE) attacks. PMID 30539362 corroborates this mechanism across preclinical and Phase I data.

This is notable because the predicted indication — C1 inhibitor deficiency — is not a distant repurposing hypothesis but sits directly on the drug's known pharmacological pathway: plasma kallikrein inhibition is the accepted rationale for treating C1-INH deficiency/HAE. The clinical trial portfolio confirms this is an established, not speculative, use: a completed placebo-controlled Phase 3 trial (HELP Study), a long-term open-label extension (HELP OLE), and regional confirmatory Phase 3 studies in Chinese and Japanese populations, plus real-world registries spanning the US, UK, Argentina, Poland, Romania, Saudi Arabia, South Korea, and China.

In short, the TxGNN signal here largely reflects a mechanistically well-established therapeutic relationship rather than a novel hypothesis — the main gap is administrative (no local license/regulatory filing on record) rather than scientific.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP Study — pivotal randomized, double-blind, placebo-controlled trial of lanadelumab for long-term prophylaxis against HAE attacks |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP Study Extension — open-label long-term safety and efficacy follow-up |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety/efficacy in adolescents/adults with non-histaminergic angioedema with normal C1-INH |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING Study — safety, PK/PD in pediatric subjects 2 to <12 years |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Safety, PK, and efficacy in Chinese subjects with HAE |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Efficacy and safety in Japanese subjects with HAE Type I/II |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan expanded access program prior to local licensure |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | N/A | Completed | 207 | Retrospective chart review of real-world effectiveness/disease management on long-term prophylaxis |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER Study — observational HAE attack rate before/after lanadelumab initiation (US/Canada) |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | ENABLE Study — 3-year prospective real-world effectiveness |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Pivotal randomized trial: lanadelumab vs placebo significantly reduces HAE attack frequency |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | First global approval review; describes plasma kallikrein inhibition mechanism tied to SERPING1/C1-INH deficiency |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | New England Journal of Medicine | General review of hereditary angioedema pathophysiology and management |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs in R&D | Comparative efficacy/safety of lanadelumab vs other long-term prophylaxis agents (garadacimab, C1INH, berotralstat) |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clinical Reviews in Allergy & Immunology | Characterizes breakthrough attacks in patients on long-term prophylaxis, including lanadelumab |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Systematic Review | Journal of Comparative Effectiveness Research | Indirect treatment comparison of lanadelumab vs C1-esterase inhibitor in pediatric HAE |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | Journal of Investigational Allergology & Clinical Immunology | Review of current and emerging HAE therapies including kallikrein-kinin pathway inhibition |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | Journal of Allergy and Clinical Immunology | Disease burden of C1-inhibitor deficiency HAE with Asia-Pacific regional focus |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Long-term Extension Study | Allergy | HELP OLE Study — long-term effectiveness and safety of lanadelumab in patients ≥12 years |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observational | Journal of Allergy and Clinical Immunology: In Practice | INTEGRATED multicountry real-world effectiveness study |

---

## US Market Information

No license records are on file — Lanadelumab is currently **not marketed** in this jurisdiction (0 NDAs). External evidence from the clinical trial registry indicates approved status in other markets (e.g., "Takhzyro is an approved treatment for hereditary angioedema (HAE) in South Korea" per NCT07445087, and Chinese health authority approval per NCT06346899), but no local authorization data is available to populate this table.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `taiwan_regulatory` and `safety` data gaps are flagged as Blocking in the source evidence pack — TFDA label warnings/contraindications and DDI data could not be retrieved.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level (L2) understates the true strength of support — a completed placebo-controlled Phase 3 RCT (HELP Study) is backed by an extensive Phase 3 program across multiple populations (Chinese, Japanese, pediatric) plus large real-world registries, and the drug already appears to hold regulatory approval for this exact indication in other markets. However, a **Blocking** data gap (DG001: no local TFDA label/warnings data) means the drug cannot yet clear an initial safety review (S1) in this jurisdiction, so a full "Go" is not yet warranted.

**To proceed, the following is needed:**
- TFDA (or equivalent local regulator) label data — warnings, precautions, and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank or manufacturer labeling (DG002)
- Drug-drug interaction (DDI) profile, currently returning no results
- Confirmation of local regulatory filing/registration pathway, given the drug is not currently marketed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

