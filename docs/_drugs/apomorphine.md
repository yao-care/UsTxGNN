---
layout: default
title: Apomorphine
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Apomorphine
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

# Apomorphine: From Parkinson's Disease to Schizophrenia

## One-Sentence Summary

Apomorphine is a potent, non-selective dopamine receptor agonist classically used for acute "off" episodes in Parkinson's disease, though no formal regulatory data was captured in this evidence pack (Taiwan: not marketed; US: data not retrieved).
The TxGNN model generated 10 predicted new indications; **Schizophrenia** (rank #5, score 99.69%) is the only prediction carrying any supporting evidence — **2 clinical trials** and **20 publications** — and rests on a mechanistically plausible but pharmacologically complex hypothesis involving presynaptic D2 autoreceptor activation.
All other top-ranked predictions (including rank #1: polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis) carry zero clinical evidence and are uniformly rated **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease "off" episodes (not formally registered in this dataset) |
| Predicted New Indication | Schizophrenia (rank #5 — most evidence-supported among 10 predictions) |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| US/Taiwan Market Status | Not marketed (0 licenses on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Apomorphine is a potent, non-selective dopamine receptor agonist with high affinity for D1, D2, D3, and D4 receptor subtypes. It is best known clinically as a subcutaneous rescue therapy for acute Parkinson's disease "off" episodes, where rapid dopaminergic stimulation restores motor function during levodopa gaps.

The connection to schizophrenia flows from the **dopamine hypothesis**: positive symptoms (hallucinations, delusions) are linked to mesolimbic D2 receptor hyperactivity. On the surface, a dopamine agonist would appear counterindicated — and at high doses, it can indeed worsen psychosis. However, the **presynaptic D2 autoreceptor hypothesis** offers a paradoxical rationale: at low doses, Apomorphine may preferentially activate presynaptic D2 autoreceptors, which serve as negative feedback inhibitors of dopamine synthesis and release. This could theoretically reduce dopamine output in overactive mesolimbic circuits, producing an antipsychotic-like effect without directly blocking postsynaptic receptors.

In practice, studies from the 1970s through early 2000s used Apomorphine almost exclusively as a **pharmacological probe** — the "apomorphine challenge test" — to quantify dopamine system sensitivity in schizophrenia patients by measuring growth hormone secretion, prolactin suppression, cortisol response, and prefrontal activation via PET. Small clinical trials from 1983–1984 (12–25 patients) found no clear therapeutic benefit or harm at low doses. Apomorphine has never advanced to a dedicated antipsychotic development program, and the dose-dependent risk of worsening positive symptoms at higher doses remains the central safety barrier.

---

## Clinical Trial Evidence

The Schizophrenia prediction (rank #5) is the only indication in this evidence pack with registered clinical trials. Neither trial constitutes a therapeutic efficacy study.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03911726](https://clinicaltrials.gov/study/NCT03911726) | N/A | Active, Not Recruiting | 140 | PET/MRI mechanistic study using Apomorphine as a pharmacological probe to detect antipsychotic-induced dopamine receptor supersensitivity in schizophrenia patients. Apomorphine functions here as a research tool to challenge the dopamine system, not as the therapeutic intervention. |
| [NCT00009048](https://clinicaltrials.gov/study/NCT00009048) | Phase 2 | Completed | 30 | Serotoninergic agent (EMD 128130) evaluated for Parkinson's disease symptoms and levodopa-induced dyskinesias. Primary population is Parkinson's disease — Apomorphine likely appears as background medication only. Low relevance to schizophrenia. |

---

## Literature Evidence

Twenty publications were retrieved for the Schizophrenia prediction. The table below lists the 10 most relevant, prioritised by study type. Fifteen additional publications retrieved under the retinal dystrophy prediction (rank #3) were determined to be false-positive retrievals with no relevance to Apomorphine and are excluded.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11394190](https://pubmed.ncbi.nlm.nih.gov/11394190/) | 2001 | Review | J Psychiatry Neurosci | Comprehensive analysis of Apomorphine and the dopamine hypothesis: at postsynaptic-stimulating doses, Apomorphine does not reliably induce psychosis in non-schizophrenic subjects, challenging the simple "DA agonist = pro-psychotic" assumption |
| [12727131](https://pubmed.ncbi.nlm.nih.gov/12727131/) | 2003 | Clinical Challenge | Psychoneuroendocrinology | Prolactin, ACTH, and cortisol responses to Apomorphine vs. d-fenfluramine in 20 drug-free schizophrenic inpatients; distinct DA and 5-HT responsiveness patterns were associated with different positive and negative symptom clusters |
| [8824341](https://pubmed.ncbi.nlm.nih.gov/8824341/) | 1996 | PET Neuroimaging | J Neuroscience | PET study showing Apomorphine modulates fronto-temporal functional connectivity differently in unmedicated schizophrenics vs. healthy controls during a verbal fluency challenge; demonstrates distributed dopaminergic effects on prefrontal circuitry |
| [11166518](https://pubmed.ncbi.nlm.nih.gov/11166518/) | 2001 | Clinical Challenge | Neuropsychopharmacology | Blunted cortisol response to Apomorphine observed in neuroleptic-free schizophrenics vs. healthy controls; degree of blunting predicted better subsequent antipsychotic treatment response |
| [6372737](https://pubmed.ncbi.nlm.nih.gov/6372737/) | 1984 | Clinical Trial (Small) | Arch Gen Psychiatry | Double-blind crossover of Apomorphine 0.75 mg SC vs. placebo in 25 male schizophrenics; no significant improvement or deterioration in psychosis or tardive dyskinesia; prolactin and growth hormone measured concurrently |
| [6682989](https://pubmed.ncbi.nlm.nih.gov/6682989/) | 1983 | Clinical Study | Prog Neuropsychopharmacol Biol Psychiatry | Double-blind Apomorphine 0.01 mg/kg vs. placebo in 12 chronic schizophrenics; no overall antipsychotic benefit; anxiety and depression BPRS subscales showed marginal improvement; CT scan subgrouping explored |
| [2875478](https://pubmed.ncbi.nlm.nih.gov/2875478/) | 1986 | Clinical Biomarker | Psychiatry Research | Growth hormone response to Apomorphine proposed as marker of central dopaminergic activity; 4-cluster symptom model for schizophrenia identified with distinct DA biomarker correlates |
| [1099172](https://pubmed.ncbi.nlm.nih.gov/1099172/) | 1975 | Clinical Observation | J Neurol Neurosurg Psychiatry | Double-blind Apomorphine 1 mg SC three times daily × 14 days in 40 subjects (mainly alcoholics); no schizophrenic symptoms induced at this dose; BPRS and Hamilton scores improved similarly with Apomorphine and placebo |
| [12405516](https://pubmed.ncbi.nlm.nih.gov/12405516/) | 2002 | Animal Model | Behav Genetics | APO-SUS and APO-UNSUS rat lines selectively bred for differential stereotypy response to Apomorphine; described as a polygenic animal model of schizophrenia-spectrum susceptibility and gene-environment interaction |
| [40935232](https://pubmed.ncbi.nlm.nih.gov/40935232/) | 2025 | Animal Model | Prog Neuropsychopharmacol Biol Psychiatry | APO-SUS rat model combined with prenatal immune activation; polygenic schizophrenia susceptibility alters neurodevelopment, synaptic density, and anticipatory behaviour — confirms translational value of the model |

---

## Market Information

No regulatory licenses were found in this dataset.

| Jurisdiction | Status |
|---------|---------|
| Taiwan (TFDA) | Not marketed — 0 licenses on file |
| US (FDA) | Not captured in this evidence pack |

**Note:** Apomorphine is known to be US FDA-approved as **Apokyn®** (subcutaneous injection, US WorldMeds) for the acute, intermittent treatment of hypomobility "off" episodes in Parkinson's disease patients. This approval was not retrieved in the current dataset and should be confirmed through direct FDA label review before any regulatory strategy is developed.

---

## Safety Considerations

No formal safety data (warnings, contraindications, or drug interactions) was retrieved in this evidence pack. Please refer to the Apokyn® prescribing information for complete safety data.

**Key pharmacological safety considerations relevant to a schizophrenia application:**

- **Psychosis risk**: As a dopamine agonist, Apomorphine can worsen or precipitate positive psychotic symptoms at supratherapeutic doses — this is the fundamental safety barrier for any schizophrenia development program
- **Nausea and vomiting**: Severe emesis is common and typically requires antiemetic premedication; domperidone is preferred (ondansetron is contraindicated — see below)
- **Cardiovascular**: Risk of orthostatic hypotension and QT interval prolongation necessitates cardiac monitoring, particularly problematic in antipsychotic co-administration scenarios
- **Critical drug interaction**: Concomitant use with 5-HT₃ antagonists (e.g., ondansetron, granisetron) has been associated with profound hypotension and loss of consciousness — highly relevant if patients are also receiving antiemetics

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Nine of ten TxGNN predictions (including rank #1, polymicrogyria) carry no mechanistic basis and no supporting evidence, warranting immediate Hold without further analysis. Schizophrenia (rank #5) is intellectually interesting — Apomorphine has a genuine pharmacological interaction with the dopaminergic pathways implicated in schizophrenia — but the available evidence positions it solely as a research probe, not a therapeutic candidate. Small 1980s trials showed no efficacy, and the risk of worsening positive symptoms at non-autoreceptor-selective doses represents an unresolved safety problem that blocks clinical progression under the current evidence base.

**To move the Schizophrenia prediction forward, the following is needed:**

- **Close DG001 (Blocking)**: Obtain full TFDA/FDA prescribing information to complete the safety initial screen — this gap currently prevents formal safety evaluation
- **Close DG002 (High)**: Retrieve DrugBank MOA data to formally characterise the D2 presynaptic vs. postsynaptic dose-selectivity profile, which is the mechanistic crux of the autoreceptor hypothesis
- **Dose-response preclinical work**: Define the autoreceptor-selective dose window in validated schizophrenia animal models (e.g., APO-SUS rats) before any human study design
- **Deep literature review**: Obtain full texts of PMID 6372737 and 6682989 to extract patient-level dose, duration, and symptom data — these are the only human therapeutic trials on record
- **Regulatory feasibility check**: Assess whether development for schizophrenia would require a new formulation (the current SC route is impractical for chronic psychiatric use) and whether the existing Parkinson's approval creates a regulatory pathway or a barrier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

