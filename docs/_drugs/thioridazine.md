---
layout: default
title: Thioridazine
parent: 僅模型預測 (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
---

# Thioridazine
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

# Thioridazine: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Thioridazine is a first-generation phenothiazine antipsychotic historically prescribed for schizophrenia and psychotic agitation, withdrawn from the US market in 2005 due to life-threatening ventricular arrhythmias caused by QTc prolongation.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
with **0 clinical trials** and **20 publications** currently supporting this direction — though most evidence is indirect, class-level, or historical in nature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No active US regulatory record (historically: schizophrenia and psychotic agitation — drug withdrawn 2005) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (Withdrawn 2005) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, thioridazine is a phenothiazine-class compound acting primarily as a D2 dopamine receptor antagonist, with additional activity at muscarinic, histaminergic, and alpha-adrenergic receptors. Its antipsychotic and sedative effects arise from dopaminergic blockade in mesolimbic and nigrostriatal pathways — the same pharmacological signature that makes this TxGNN prediction biologically coherent.

Manic bipolar disorder and schizophrenia share a core pathophysiological thread: dopamine hyperactivation in mesolimbic circuits underlies both psychotic symptoms and acute manic episodes. D2 antagonism that suppresses psychosis in schizophrenia is mechanistically expected to dampen dopamine-driven manic excitation as well. This is not merely theoretical: a 1980 controlled study (PMID 6155678) directly compared pimozide, chlorpromazine, and thioridazine in manic patients and found comparable clinical improvement across all three agents, explicitly attributing the effect to D2 receptor blockade. Clinical reports from 1964 (PMID 14252012) also document combined thioridazine regimens specifically for psychomotor excitation and manic reactions, and a 2026 review (PMID 40926568) cites phenothiazines' documented clinical use in mania within bipolar disorder.

The critical constraint here is safety, not mechanistic plausibility. Thioridazine prolongs the QTc interval dose-dependently, raising the risk of Torsades de Pointes and sudden cardiac death — the reason it was withdrawn from global markets. This concern is especially acute in bipolar disorder patients, a population known to carry elevated cardiac genetic risk through CACNA1C variants (PMID 38560725). Additionally, lithium — the cornerstone of bipolar disorder maintenance therapy — carries a documented severe neurotoxic interaction with thioridazine (PMID 106047), further limiting combination use. Modern atypical antipsychotics (quetiapine, aripiprazole, olanzapine) achieve equivalent D2 antagonism with substantially superior cardiovascular safety, making them the current standard of care for acute mania.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for thioridazine in manic bipolar affective disorder.

> **Relevant Safety Trial Note:** A completed trial ([NCT00538122](https://clinicaltrials.gov/study/NCT00538122), N=12) specifically assessed T-wave abnormalities and arrhythmia/sudden death risk in thioridazine patients via 24-hour Holter ECG monitoring. While not a therapeutic efficacy trial, its findings directly confirm thioridazine's cardiac liability and were pivotal to its market withdrawal — this is a blocking finding for any bipolar repurposing pathway.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6155678](https://pubmed.ncbi.nlm.nih.gov/6155678/) | 1980 | Controlled Study | Psychopharmacology | Direct comparison of pimozide vs. phenothiazines (including thioridazine) in manic patients; comparable clinical improvement across agents confirms dopamine blockade as anti-manic mechanism |
| [14252012](https://pubmed.ncbi.nlm.nih.gov/14252012/) | 1964 | Early Clinical Report | Annales Médico-Psychologiques | Combined thioridazine-Nembutal with electroshock therapy for psychomotor excitation and manic reactions — earliest direct clinical record of thioridazine in mania |
| [8448267](https://pubmed.ncbi.nlm.nih.gov/8448267/) | 1993 | Observational | Biological Psychiatry | Case study of a woman on maintenance thioridazine hydrochloride for schizoaffective mania; 11-year circannual tracking of manic episodes demonstrates long-term use in mood disorder |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review | J Applied Toxicology | Comprehensive review of phenothiazine derivatives (including thioridazine) across schizophrenia, mania in bipolar disorder, and psychosis; discusses cancer-inhibiting potential via apoptosis pathways |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Systematic Review | J Clinical Psychiatry | Systematic review of typical and atypical antipsychotics for anxiety symptoms comorbid with major depression and bipolar disorder; class-level support for antipsychotics in mood disorder |
| [11910256](https://pubmed.ncbi.nlm.nih.gov/11910256/) | 2002 | Pharmacokinetics Study | J Clinical Psychopharmacology | Quetiapine co-administered with thioridazine in 36 patients with schizophrenia, schizoaffective disorder, or bipolar disorder; documents pharmacokinetic interactions relevant to combination therapy |
| [106047](https://pubmed.ncbi.nlm.nih.gov/106047/) | 1979 | Case Series | J Clinical Psychiatry | Four cases of severe neurotoxicity — delirium, seizures, encephalopathy, abnormal EEG — when lithium was combined with thioridazine; critical safety warning given lithium's central role in bipolar treatment |
| [11336615](https://pubmed.ncbi.nlm.nih.gov/11336615/) | 2001 | Review | Expert Opinion on Pharmacotherapy | History of phenothiazines in non-psychotic psychiatric disorders; thioridazine cited as key class member, contextualizing use beyond schizophrenia |
| [38560725](https://pubmed.ncbi.nlm.nih.gov/38560725/) | 2024 | In Vitro Study | Biological Psychiatry Global Open Science | CACNA1C mutation in bipolar disorder patients causes cardiac conduction slowing in iPSC-derived cardiomyocytes; directly relevant to thioridazine's QTc risk in genetically vulnerable bipolar patients |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatric Practice | Safety and pharmacology of antipsychotics (including thioridazine) during pregnancy; highlights phenothiazine class risk profile in vulnerable populations |

---

## US Market Information

No active US regulatory authorizations are on record for thioridazine. Thioridazine was historically marketed in the United States as **Mellaril®** (Novartis) for schizophrenia. It was voluntarily withdrawn from the US market in 2005 following FDA safety communications regarding fatal ventricular arrhythmias associated with QTc interval prolongation. No NDA data is available for tabulation from this Evidence Pack.

---

## Safety Considerations

While formal FDA labeling data is unavailable in this Evidence Pack, the following safety signals are directly documented in the reviewed clinical evidence:

- **Cardiac Arrhythmia / QTc Prolongation**: NCT00538122 (completed, N=12) specifically assessed T-wave abnormalities and arrhythmia/sudden death risk in thioridazine patients via 24-hour Holter ECG monitoring. This is the primary basis for the 2005 market withdrawal and constitutes a blocking safety barrier for any repurposing pathway in bipolar disorder — a population that may carry additional cardiac genetic vulnerability (CACNA1C, PMID 38560725).
- **Severe Lithium–Thioridazine Neurotoxic Interaction**: PMID 106047 documents four cases of delirium, seizures, encephalopathy, and grossly abnormal EEGs when thioridazine was co-administered with lithium. Given that lithium is a cornerstone first-line therapy for bipolar disorder, this interaction is especially critical to flag.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for thioridazine in manic bipolar disorder is pharmacologically valid — D2 receptor antagonism demonstrably suppresses dopamine-driven manic excitation, as shown in direct historical clinical studies — but thioridazine's well-documented QTc prolongation risk and its resulting 2005 US market withdrawal represent a fundamental blocking safety concern. In a patient population with known cardiac genetic vulnerabilities and lithium as the standard co-treatment, the risk-benefit calculus is unfavorable, and safer alternatives with equivalent efficacy already exist.

**To proceed, the following would be needed:**
- Identification of a clearly defined patient subpopulation where all approved atypical antipsychotics are contraindicated or inadequate, justifying thioridazine's risk profile
- Complete formal MOA data from DrugBank (Data Gap DG002) to assess whether thioridazine offers any mechanistic advantage over available agents
- Full historical FDA labeling and contraindication documentation (Data Gap DG001)
- Regulatory pathway assessment for a withdrawn drug seeking a new indication
- Prospective cardiac monitoring protocol (continuous Holter ECG, electrolyte management) as a prerequisite for any early-phase study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

