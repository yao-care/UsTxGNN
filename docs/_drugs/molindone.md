---
layout: default
title: Molindone
parent: 僅模型預測 (L5)
nav_order: 939
evidence_level: L5
indication_count: 10
---

# Molindone
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

# Molindone: From Schizophrenia (Antipsychotic Class) to Manic Bipolar Affective Disorder

## One-Sentence Summary

Molindone is a first-generation (typical) antipsychotic; its own approved-indication data is not on file in this evidence pack (Taiwan/US: unmarketed), so the original indication above reflects its known pharmacological class rather than a verified label claim. Of the ten TxGNN-ranked predictions, nine (including the top-scoring "retinal dystrophy" candidate) were reviewed and judged to be model noise with no mechanistic plausibility or supporting evidence; the only candidate with independent literature support is **Manic Bipolar Affective Disorder** (rank 10, score 99.98%), backed by **5 publications** and a class-effect mechanistic argument, though with **zero molindone-specific trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug unmarketed; no NDA/license record). Molindone is pharmacologically classified as a dihydroindolone (typical) antipsychotic — external reference, not verified in this dataset |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% (rank 864 of model output) |
| Evidence Level | L4 (mechanism/class-effect + non-drug-specific literature, no direct RCT) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for molindone is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacological classification, molindone is a dihydroindolone-class typical antipsychotic acting primarily as a central dopamine D2 receptor antagonist — this is external background knowledge, not a finding verified within this dataset.

Other D2-antagonist antipsychotics (both typical and atypical, e.g. olanzapine) are established treatments for acute manic/mixed episodes in bipolar disorder, which supports a *class-effect* argument for molindone's plausibility in mania. However, no clinical trial or publication in this evidence pack tests molindone directly against bipolar mania — the supporting literature addresses antipsychotics as a drug class (anxiety symptoms, adolescent bipolar treatment with olanzapine) or documents molindone's use/safety in schizophrenia and NMS-history patients, not efficacy in mania specifically.

By contrast, the model's top nine ranked predictions (retinal dystrophy, congenital glycosylation disorders, hydranencephaly, CMT1G, multiple myopia subtypes, polymicrogyria, glycine encephalopathy) show no mechanistic overlap with a central D2 antagonist and are supported only by literature that never mentions molindone — these were assessed as TxGNN embedding noise (likely driven by disease-entity clustering artifacts) rather than genuine repurposing signals, and are not carried forward in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31922663](https://pubmed.ncbi.nlm.nih.gov/31922663/) | 2020 | RCT | World Psychiatry | IMPACT trial: metformin add-on vs. antipsychotic switch vs. continued antipsychotic in overweight/obese youth with severe mental illness — addresses antipsychotic metabolic management, not mania efficacy directly |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Review of typical and atypical antipsychotic efficacy for anxiety symptoms/disorders in major depression and bipolar disorder |
| [21127693](https://pubmed.ncbi.nlm.nih.gov/21127693/) | 2010 | Review | Neuropsychiatric Disease and Treatment | Olanzapine approved for acute manic/mixed episodes in adolescent bipolar I disorder — supports class-effect but not molindone-specific |
| [15516311](https://pubmed.ncbi.nlm.nih.gov/15516311/) | 2004 | Case Report | J Analytical Toxicology | Postmortem tissue distribution of molindone in a multidrug overdose case — pharmacokinetic/toxicology data, not efficacy evidence |
| [2507394](https://pubmed.ncbi.nlm.nih.gov/2507394/) | 1989 | Case Report | General Hospital Psychiatry | Successful reinstitution of molindone in a patient with prior neuroleptic malignant syndrome — supports molindone's usability profile, not mania efficacy |

---

## US Market Information

Molindone is not currently marketed in Taiwan or the US (market status: unmarketed; 0 licenses on file). No NDA/authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA warning/contraindication data is currently unavailable (flagged as a Blocking data gap — DG001), which prevents a complete S1 safety review.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Evidence for molindone in bipolar mania rests on class-effect reasoning and non-drug-specific literature, not on any molindone-specific trial or study — evidence level L4, insufficient for a Go decision. The drug's unmarketed status and the Blocking-severity absence of TFDA warning/contraindication data (DG001) mean a safety initial screen (S1) cannot yet be completed.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (resolve DG001, currently Blocking)
- Verified mechanism of action documentation from DrugBank (resolve DG002)
- Molindone-specific preclinical or clinical evidence in bipolar mania, since current support is class-level only
- Regulatory feasibility assessment given unmarketed status in Taiwan/US
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

