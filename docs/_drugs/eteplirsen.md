---
layout: default
title: Eteplirsen
parent: 僅模型預測 (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Eteplirsen
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

# Eteplirsen: From Exon 51-Skip-Amenable DMD to Duchenne and Becker Muscular Dystrophy

## One-Sentence Summary

Eteplirsen (Exondys 51) is an antisense oligonucleotide originally developed and approved for Duchenne muscular dystrophy (DMD) patients whose dystrophin gene mutations are amenable to exon 51 skipping. The TxGNN model's top prediction — **Duchenne and Becker muscular dystrophy** — is not a novel repurposing signal but a confirmation of the drug's own core indication, supported by **12 clinical trials** and **19 publications**, including two pivotal Phase 3 studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Taiwan (no NDA on file); per trial/mechanistic evidence, approved use is DMD amenable to exon 51 skipping |
| Predicted New Indication | Duchenne and Becker muscular dystrophy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced MOA text is not yet available (data gap), but the mechanism is well documented in the clinical evidence itself. Eteplirsen is a phosphorodiamidate morpholino oligomer (PMO) that binds dystrophin pre-mRNA and induces skipping of exon 51. In patients with frame-shift deletions near this region, this restores the reading frame and enables production of a truncated but partially functional dystrophin protein — the underlying deficiency in DMD.

Critically, the TxGNN "predicted" indication of Duchenne and Becker muscular dystrophy is not a cross-indication extrapolation: it is essentially the drug's own approved therapeutic niche (exon 51 skip-amenable mutations, ~13% of the DMD population). Becker muscular dystrophy shares the same dystrophin gene defect in a milder phenotype, so the mechanistic rationale extends naturally to that population.

Because the prediction converges with the drug's real-world indication, this case functions more as a validation check on the model than a genuine repurposing opportunity — evidence strength is high, but the "new use" framing should be interpreted cautiously.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01396239](https://clinicaltrials.gov/study/NCT01396239) | Phase 2 | Completed | 12 | Randomized, double-blind, placebo-controlled dose study (30/50 mg/kg) over 24 weeks in ambulant DMD subjects |
| [NCT03992430](https://clinicaltrials.gov/study/NCT03992430) | Phase 3 | Active, not recruiting | 160 | Randomized, double-blind comparison of high-dose (100/200 mg/kg) vs. standard 30 mg/kg eteplirsen in exon 51 skip-amenable DMD |
| [NCT02255552](https://clinicaltrials.gov/study/NCT02255552) | Phase 3 | Completed | 109 | Open-label, multi-center pivotal trial with untreated control arm; key efficacy evidence supporting FDA accelerated approval |
| [NCT00844597](https://clinicaltrials.gov/study/NCT00844597) | Phase 1/2 | Completed | 19 | First-in-human IV safety study of AVI-4658 (eteplirsen) in exon 51 skip-amenable DMD |
| [NCT01540409](https://clinicaltrials.gov/study/NCT01540409) | Phase 2 | Completed | 12 | Open-label extension (212 additional weeks) evaluating ongoing efficacy, safety and biomarker correlation |
| [NCT02286947](https://clinicaltrials.gov/study/NCT02286947) | Phase 2 | Completed | 24 | Safety and tolerability in advanced-stage DMD patients amenable to exon 51 skipping |
| [NCT02420379](https://clinicaltrials.gov/study/NCT02420379) | Phase 2 | Completed | 33 | Safety, efficacy, tolerability and PK in early-stage DMD |
| [NCT03218995](https://clinicaltrials.gov/study/NCT03218995) | Phase 2 | Completed | 15 | Safety, tolerability and PK of weekly IV eteplirsen in very young patients (6–48 months) |
| [NCT06606340](https://clinicaltrials.gov/study/NCT06606340) | Phase 4 (N/A) | Enrolling by invitation | 300 | Long-term real-world observational study of eteplirsen, golodirsen and casimersen in routine practice |
| [NCT04179409](https://clinicaltrials.gov/study/NCT04179409) | Phase 2 | Completed | 3 | Comparative efficacy/safety of AMONDYS 45, EXONDYS 51, VYONDYS 53 across exon 45/51/53 duplications (small sample) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23907995](https://pubmed.ncbi.nlm.nih.gov/23907995/) | 2013 | Double-blind placebo-controlled study | Annals of Neurology | Pivotal report testing eteplirsen's ability to induce dystrophin production and improve 6-minute walk distance |
| [34120909](https://pubmed.ncbi.nlm.nih.gov/34120909/) | 2021 | Cohort (Open-label extension) | J Neuromuscul Dis | PROMOVI trial: Phase 3, multicenter, open-label efficacy/safety results in a larger DMD cohort (30 mg/kg/week x 96 weeks) |
| [38669554](https://pubmed.ncbi.nlm.nih.gov/38669554/) | 2024 | Systematic Review/Meta-Analysis | J Neuromuscul Dis | Predictors of loss of ambulation in DMD |
| [40831143](https://pubmed.ncbi.nlm.nih.gov/40831143/) | 2026 | Cohort | J Neuromuscul Dis | Propensity-matched analysis of LVEF decline comparing eteplirsen-treated vs. control DMD patients |
| [29254734](https://pubmed.ncbi.nlm.nih.gov/29254734/) | 2018 | Pooled Analysis | J Clin Neurosci | Pooled analysis of eteplirsen outcomes in paediatric DMD patients |
| [38482981](https://pubmed.ncbi.nlm.nih.gov/38482981/) | 2024 | Cohort | Muscle & Nerve | Survival among patients receiving eteplirsen up to 8 years, contextualized against natural history controls |
| [37207382](https://pubmed.ncbi.nlm.nih.gov/37207382/) | 2023 | Open-label dose-escalation study | Neuromuscular Disorders | Safety, tolerability and PK of eteplirsen in boys aged 6–48 months (NCT03218995) |
| [40308063](https://pubmed.ncbi.nlm.nih.gov/40308063/) | 2025 | Review | Molecular Therapy | Clinical applications of exon-skipping ASOs (eteplirsen, golodirsen, viltolarsen, casimersen) in neuromuscular disease |
| [28280301](https://pubmed.ncbi.nlm.nih.gov/28280301/) | 2017 | Review | Drug Des Devel Ther | Overview of eteplirsen's accelerated FDA approval and treatment context |
| [31794463](https://pubmed.ncbi.nlm.nih.gov/31794463/) | 2019 | Review | Continuum (Minneap Minn) | Broader review of dystrophinopathies including DMD/BMD management and emerging therapies |

## US Market Information

Eteplirsen is not currently marketed in this jurisdiction — 0 licenses/authorizations are on file, and `market_status` is recorded as "Not Marketed." No NDA-level product detail is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not retrievable at this data cutoff (TFDA labeling not yet obtained — flagged as a blocking data gap).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 2/3 trials, including a pivotal controlled study (NCT02255552) that underpinned FDA accelerated approval, plus 19 supporting publications. However, this is effectively confirmation of eteplirsen's existing approved indication rather than a new repurposing opportunity, and formal safety/labeling data for this jurisdiction is still missing.

**To proceed, the following is needed:**
- TFDA (or local regulatory) label — warnings and contraindications (DG001, blocking)
- Confirmed DrugBank/product MOA documentation (DG002)
- Clarification that this candidate reflects label-consistent use rather than off-label repurposing, before any S1 safety review proceeds
- Genotype confirmation requirement (exon 51 skip-amenable mutation) noted explicitly in any downstream guidance, since efficacy is restricted to that subgroup
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

