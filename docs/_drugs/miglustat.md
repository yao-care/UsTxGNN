---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 929
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Type 1 Gaucher Disease to Tay-Sachs Disease

## One-Sentence Summary

Miglustat is an oral glucosylceramide synthase (UGCG) inhibitor originally developed as substrate reduction therapy for Type 1 Gaucher disease and later extended to Niemann-Pick disease type C. Among 10 TxGNN-predicted indications, **Tay-Sachs disease** is the only candidate backed by actual research — **5 clinical trials** and **20 publications**, including a completed randomized controlled trial. The remaining 9 candidates (highest TxGNN scores) have no supporting evidence and are held at model-prediction-only status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 Gaucher disease (literature-sourced; original_indications field empty in this dataset; drug not locally licensed) |
| Predicted New Indication | Tay-Sachs Disease (GM2 gangliosidosis) |
| TxGNN Prediction Score | 99.75% (rank 6,820 of model output) |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Miglustat is an imino sugar that inhibits glucosylceramide synthase (UGCG), the first committed enzyme in glycosphingolipid biosynthesis. This mechanism — substrate reduction therapy (SRT) — lowers the production rate of glycosphingolipids so that residual catabolic enzyme activity in a deficient patient can keep pace, reducing pathological lysosomal storage. This mechanism is already clinically validated: miglustat is licensed for Gaucher disease and Niemann-Pick type C, both lysosomal storage disorders involving glycosphingolipid accumulation.

Tay-Sachs disease is caused by hexosaminidase A deficiency, leading to accumulation of GM2 ganglioside — a downstream product of the same glycosphingolipid biosynthetic pathway that UGCG initiates. Reducing upstream substrate flux via UGCG inhibition is therefore mechanistically well-aligned with Tay-Sachs pathophysiology, unlike several of the model's other top-ranked predictions (e.g., cholesteryl ester storage disease, adrenal neoplasm), which involve unrelated lipid or unclear pathways and show weak or no mechanistic linkage per the evidence pack's own rationale notes.

This mechanistic logic is reflected in the trial record: multiple sponsor-run pharmacokinetic/safety studies and one randomized controlled trial in late-onset Tay-Sachs disease were conducted specifically because of this shared pathway, making Tay-Sachs disease the best-supported candidate among the ten TxGNN predictions despite not having the single highest similarity score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminated | 30 | Evaluated miglustat's effect on neurological and systemic symptoms in infantile Sandhoff/Tay-Sachs disease; trial terminated before completion |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Completed | 10 | PK, safety and tolerability of Zavesca (miglustat) in infantile-onset GM2 gangliosidosis (single and steady-state oral doses) |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Completed | 5 | PK and tolerability of Zavesca (miglustat) in juvenile GM2 gangliosidosis; single/multiple oral doses |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminated | 16 | "Syner-G" combination of miglustat plus ketogenic diet in infantile/juvenile gangliosidoses; terminated before completion |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Recruiting | 21 | Long-term safety/efficacy study of nizubaglustat (a newer investigational SRT agent, not miglustat) in GM2 gangliosidosis/NPC patients, including those transitioning from prior miglustat treatment — supports disease feasibility but is not direct miglustat evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | 12-month randomized controlled study (with 24-month extension) evaluating miglustat safety and efficacy in late-onset Tay-Sachs/GM2 gangliosidosis |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematic Review | European Journal of Neurology | Systematic review of miglustat efficacy and safety across GM2 gangliosidosis studies; notes prior inconsistent results |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Review | Int J Mol Sciences | Overview of GM2 gangliosidoses clinical features, pathophysiology and current therapies including substrate reduction |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Review | Frontiers in Physiology | Survey of new therapeutic approaches to Tay-Sachs disease |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Cohort/Pilot | J Inherited Metabolic Disease | Neurocognitive testing pilot study in late-onset Tay-Sachs disease as an outcome measure for therapeutic trials |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Cohort (open-label) | Neurology | Substrate reduction therapy with miglustat in two infantile Tay-Sachs patients; could not arrest neurologic decline, but CSF drug levels and macrocephaly prevention observed |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Cohort/Natural history | Molecular Genetics and Metabolism | Natural history timeline of infantile gangliosidoses; notes miglustat SRT tried but limited by GI side effects |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Review (drug profile) | Curr Opin Investig Drugs | Drug profile confirming miglustat's approved use in Gaucher disease and development for Tay-Sachs, Fabry, and Niemann-Pick C |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Review | Expert Rev Endocrinol Metab | Reviews substrate-reduction therapy with miglustat for CNS-affecting glycosphingolipid storage disorders |
| [9572057](https://pubmed.ncbi.nlm.nih.gov/9572057/) | 1998 | Review (basic research) | Molecular Medicine Today | Early review of GM2 gangliosidosis biology and potential treatment strategies |

---

## US Market Information

Currently not marketed in this jurisdiction — 0 NDA/license records on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tay-Sachs disease is supported by L2-level evidence — a completed randomized controlled trial plus multiple completed Phase 2/3 pharmacokinetic studies — and a mechanistically direct link (shared UGCG/glycosphingolipid pathway) to miglustat's already-approved indications. However, two of the five trials were terminated early and enrollments are very small (n=5–30), so efficacy remains unconfirmed rather than established.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official prescribing information (warnings, contraindications) before any S1 safety review can proceed
- Resolve DG002 (High): confirm full mechanism-of-action documentation via DrugBank/label review
- Investigate reasons for early termination of NCT03822013 and NCT02030015 (efficacy failure vs. enrollment/funding issues)
- Since the drug holds no local marketing authorization, define the regulatory/import pathway before any clinical use is considered
- Given very small trial sizes, prioritize a pooled/meta-analytic reassessment or a new adequately powered trial before advancing past S2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

