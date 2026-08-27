---
layout: default
title: Lovastatin
parent: 僅模型預測 (L5)
nav_order: 874
evidence_level: L5
indication_count: 6
---

# Lovastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lovastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a first-generation HMG-CoA reductase inhibitor (statin), historically used to lower LDL cholesterol in primary hypercholesterolemia. The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, but the supporting evidence base is thin: **3 clinical trials** (none testing lovastatin itself) and **19 publications**, several of which report that lovastatin has *limited or no effect* in the receptor-negative HoFH subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary hypercholesterolemia (well-established statin class indication; no formal license record is present in this evidence pack) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Research Question (data-driven decision stage S1 — insufficient to move toward Go) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for this candidate is not available in the evidence pack (flagged as a High-severity data gap). Based on general pharmacology and the mechanistic notes accompanying this evidence pack, lovastatin inhibits HMG-CoA reductase, the rate-limiting enzyme in hepatic cholesterol synthesis. This reduces intracellular cholesterol, which in turn upregulates LDL-receptor expression on hepatocytes and accelerates clearance of circulating LDL particles — the core mechanism behind lovastatin's established efficacy in hypercholesterolemia.

The link to HoFH is mechanistically plausible on the surface, since HoFH is characterized by extremely elevated LDL-cholesterol. However, the evidence pack's own repurposing rationale flags an important limitation: lovastatin's efficacy depends on the presence of *functional* LDL receptors, and HoFH patients typically carry two defective or absent LDLR alleles. The literature bears this out — receptor-negative HoFH patients show no meaningful LDL-cholesterol reduction on lovastatin, while receptor-defective (partial-function) patients may see a modest, genotype-dependent benefit, likely via reduced hepatic VLDL secretion rather than enhanced LDL clearance.

This means the prediction is directionally reasonable but clinically narrow: any real-world utility would be confined to a genetically defined HoFH subgroup, and would almost certainly require adjunctive therapy (apheresis, bile-acid sequestrants, or newer agents such as PCSK9 inhibitors) rather than lovastatin monotherapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Tested ezetimibe 10 mg added to background atorvastatin or simvastatin in HoFH — not a lovastatin trial; relevant only as background statin-class context |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term (24-month) open-label extension evaluating ezetimibe safety/tolerability on top of atorvastatin/simvastatin in HoFH; again, not lovastatin-specific |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (a PCSK9-targeting monoclonal antibody) in pediatric/adolescent HoFH — a mechanistically distinct drug class from statins |

**Note:** None of the identified trials directly test lovastatin in HoFH; all three test other agents (ezetimibe, alirocumab) added to statin background therapy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Cohort | The Journal of Pediatrics | Lovastatin (2 mg/kg/day) in 3 children with receptor-negative HoFH produced no reduction in LDL-cholesterol or LDL turnover — direct negative evidence for the receptor-negative subtype |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case Report | JAMA | A child with HoFH who underwent liver transplantation (restoring ~60% LDL-receptor activity) achieved normal cholesterol levels; lovastatin's role was adjunctive |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Cohort | Anales Españoles de Pediatría | Two HoFH patients treated with lovastatin plus probucol/cholestyramine; response linked to LDL-receptor analysis findings |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case report | European Journal of Pediatrics | Single HoFH patient on weekly LDL-apheresis (HELP) with lovastatin as adjunct; long-term tolerability and xanthoma regression noted |
| [8637439](https://pubmed.ncbi.nlm.nih.gov/8637439/) | 1996 | Case/family study | Metabolism | Compared lovastatin and cholestyramine effects on plasma sterols in a homozygous sitosterolemia patient with concomitant FH and her heterozygous father |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Cohort | Arteriosclerosis, Thrombosis, and Vascular Biology | Shows HoFH patients with identical LDLR mutations vary in receptor expression, explaining variable drug response — supports genotype-dependence relevant to statin efficacy generally |
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT | Circulation | Multicenter, double-blind RCT of ezetimibe added to atorvastatin/simvastatin in 50 HoFH patients — background-statin context, not lovastatin itself |
| [7229037](https://pubmed.ncbi.nlm.nih.gov/7229037/) | 1981 | Mechanistic (in vitro) | The Journal of Clinical Investigation | Fibroblast studies of compactin (ML-236B, an early statin) characterizing LDL-receptor binding/degradation defects across HoFH genotypes — foundational mechanism work, not lovastatin itself |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | American Journal of Cardiovascular Drugs | General pharmacology review of ezetimibe as a cholesterol-absorption inhibitor; background context only |
| [10146648](https://pubmed.ncbi.nlm.nih.gov/10146648/) | 1993 | Cohort | Transfusion Science | Two girls with FH treated 7 years with plasma exchange/LDL-apheresis, some periods combined with simvastatin (not lovastatin) |

---

## US Market Information

Lovastatin currently has no license records in this evidence pack — market status is "Not Marketed" with 0 registered authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question (Hold pending targeted data)**

**Rationale:**
The mechanistic story is plausible in general terms, but the disease-specific literature actively undercuts it: lovastatin shows no effect in receptor-negative HoFH (the more common and severe genotype) and only a limited, genotype-dependent effect in receptor-defective HoFH. No trial in the evidence pack tests lovastatin itself in this indication — all identified trials study ezetimibe or alirocumab against a statin background. Evidence level L3 (observational/case-level only) is not sufficient to support progression toward Go.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently blocking, required before any S1 safety pre-assessment
- Confirmed mechanism-of-action documentation from DrugBank
- LDL-receptor genotype stratification data (receptor-negative vs. receptor-defective) to define which HoFH subpopulation, if any, could plausibly benefit
- A trial or registry dataset testing lovastatin specifically (not ezetimibe/alirocumab as statin add-ons) in HoFH

*Context note: within the same evidence pack, the model's rank-2 prediction ("hyperlipoproteinemia," L1 evidence, decision stage S3) is markedly stronger — but per its own rationale, that indication largely overlaps with lovastatin's already-approved use and is not true repurposing.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

