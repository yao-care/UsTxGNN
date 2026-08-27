---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Psychotic Disorders to Manic Episodes in Bipolar Affective Disorder

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic, pharmacologically established as a potent D2 dopamine receptor antagonist used for schizophrenia and acute psychosis. Among the 10 TxGNN-predicted candidates in this evidence pack, only one — **Manic Bipolar Affective Disorder** — is backed by substantive evidence, with **9 clinical trials** and **20 publications** currently on file; the other 9 higher-scoring candidates (e.g., congenital glycosylation disorders, retinal dystrophy, myopia subtypes) have zero supporting trials/literature and are flagged in the evidence pack itself as algorithmic noise with no plausible mechanistic link.

> **Note on candidate selection**: This report focuses on the mania indication (TxGNN rank 10) rather than the top-scoring rank 1 candidate, because rank 1–9 show no mechanistic rationale and no corroborating evidence (0 trials / 0 literature each), while rank 10 is the only candidate meeting a real evidence bar.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and other psychotic disorders (general pharmacological consensus; no TFDA-approved label text currently on file — data gap) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field is currently a data gap (DG002, High severity). Based on known pharmacology, however, Haloperidol is a butyrophenone-class typical antipsychotic and a potent dopamine D2 receptor antagonist. Its efficacy in psychotic disorders comes from blocking mesolimbic dopamine transmission.

The repurposing rationale supplied with this candidate explains the mechanistic link directly: by blocking D2 receptors in the limbic system, Haloperidol reduces the excessive arousal, grandiosity, and psychomotor agitation characteristic of manic episodes. This is not a novel repurposing hypothesis in the scientific sense — Haloperidol has long been used clinically as an antimanic agent and appears repeatedly as the **active comparator** in pivotal atypical-antipsychotic trials (risperidone, olanzapine, aripiprazole) for bipolar mania. The open question for this evidence pack is therefore one of **local market availability** (Taiwan/reference jurisdiction shows "Not Marketed," 0 licenses) rather than scientific plausibility.

By contrast, the 9 other TxGNN-ranked candidates (congenital disorders of glycosylation, retinal dystrophy, hydranencephaly, myopia subtypes, Charcot-Marie-Tooth disease, polymicrogyria, glycine encephalopathy) are all genetic/structural developmental disorders with no dopaminergic pathophysiology, zero clinical trials, and zero literature — consistent with the evidence pack's own annotation of these as prediction noise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs. placebo vs. haloperidol as add-on to mood stabilizers for manic episodes in bipolar disorder |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs. placebo in acute mania (bipolar I); haloperidol's role as comparator not confirmed from available summary |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Flexible-dose risperidone vs. placebo or haloperidol in manic episodes of bipolar I disorder, including 12-week maintenance comparison |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate+amisulpride vs. valproate+haloperidol in bipolar I manic episode, efficacy and safety comparison |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Olanzapine vs. placebo and haloperidol (active comparator) in manic/mixed bipolar I episode |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs. conventional antipsychotics (incl. haloperidol) for acute mania in Sweden; terminated due to low enrollment |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure and infant development; haloperidol not the primary focus |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient/fish-oil adjunct trial for bipolar disorder; no direct haloperidol comparison |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic + adherence program for chronic psychotic disorders in Tanzania; haloperidol likely local standard-of-care comparator |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Network Meta-Analysis | Molecular Psychiatry | Systematic review/NMA of double-blind RCTs comparing efficacy, acceptability, tolerability and safety of pharmacological treatments (including haloperidol) for acute bipolar mania |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomized, double-blind, placebo- and haloperidol-controlled study of olanzapine in Japanese patients with bipolar I manic/mixed episode |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review/Meta-Analysis | Human Psychopharmacology | Short-term pharmacological interventions (incl. haloperidol) for acute agitation associated with psychotic and bipolar disorder |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | Controlled Trial | Archives of General Psychiatry | Double-blind five-week controlled trial of lithium carbonate plus haloperidol vs. placebo plus haloperidol in excited schizo-affective patients |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | Journal of Clinical Psychopharmacology | Comparison of antipsychotic-induced extrapyramidal side effects (incl. haloperidol) in bipolar disorder vs. schizophrenia |
| [15147609](https://pubmed.ncbi.nlm.nih.gov/15147609/) | 2004 | Systematic Review/Economic Evaluation | Health Technology Assessment | Clinical and cost-effectiveness of newer drugs (vs. haloperidol as reference) for mania associated with bipolar disorder |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Review | BMJ Mental Health | Comparison of antipsychotic dose equivalents (incl. haloperidol) for acute bipolar mania and schizophrenia |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based treatment options for bipolar mania, including choice of antipsychotic (haloperidol among options) |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Refractoriness in bipolar disorder; add-on haloperidol among strategies for partial responders to lithium/valproate/carbamazepine |
| [19454110](https://pubmed.ncbi.nlm.nih.gov/19454110/) | 2007 | Review | BMJ Clinical Evidence | General overview of bipolar disorder treatment landscape |

---

## US Market Information

No approved licenses or NDAs are currently on file for Haloperidol in the reference jurisdiction (`total_licenses = 0`, market status: **Not Marketed**). Market entry/registration status should be confirmed with the local regulatory authority before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are currently not on file — see DG001, a Blocking-severity data gap preventing formal S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mania indication is supported by Evidence Level L1 (multiple completed Phase 3 RCTs, plus a 2022 network meta-analysis, with haloperidol repeatedly used as the active comparator), and the mechanism is well established rather than speculative. However, this is a market-availability question rather than a novel-science question — the drug currently shows 0 NDAs/Not Marketed status — and the local safety dossier (TFDA warnings/contraindications, DG001) is a **Blocking** gap that must be resolved before any S1 safety review can proceed. The other 9 TxGNN-ranked candidates should remain on **Hold** — they have no clinical, literature, or mechanistic support and are best treated as prediction noise, not as active leads.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — DG001, currently blocking
- Formal DrugBank-sourced mechanism-of-action documentation — DG002
- Completed DDI profile (current query status: not found)
- Confirmation of local market/registration pathway given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

