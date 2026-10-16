---
layout: default
title: Ketamine
parent: Model Prediction Only (L5)
nav_order: 824
evidence_level: L5
indication_count: 1
monitor_inn: "KETAMINE"
predicted_indications: ["headache disorder"]
---

# Ketamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ketamine: From an Anesthetic/Analgesic Injectable to Headache Disorder

## One-Sentence Summary

Ketamine is an injectable drug marketed in the United States under the brand Ketalar and several generic labels, but all six U.S. authorizations in the data compiled for this report are now listed as cancelled.
The TxGNN model predicts it may be effective for **headache disorder**, with **9 clinical trials** and **20 publications** currently supporting this direction.
The evidence includes one completed Phase 3 trial (THINK), but no trial results are available in the data, so efficacy cannot yet be confirmed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved-indication text in the U.S. license records) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L2 (see note below) |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 6 authorizations (1 NDA, 5 ANDAs), all cancelled |
| Recommended Decision | Hold |

*Note on evidence level:* Only one Phase 3 trial (THINK, NCT03081416) is completed, and the other Phase 3 trial (KetHead) is still recruiting. This does not meet L1 (≥2 completed Phase 3 RCTs). Because no results are available, the evidence is conservatively classed as L2. The upstream scoring labelled this L1, which I have not adopted.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from the source record is not available. Based on general pharmacology, ketamine is an NMDA receptor antagonist. Central sensitization and glutamatergic signaling are thought to contribute to migraine, cluster headache, and chronic headache pain. Blocking NMDA receptors is therefore a plausible way to relieve pain and to interrupt pain amplification in the trigeminovascular pathway.

The original approved indication is not recorded in the data. Ketamine is a well-known anesthetic and analgesic agent, and headache is a pain condition, so the link between the two is plausible. The very high TxGNN score (99.33%) is consistent with this rationale, but it is a model prediction and not clinical evidence.

Published reviews support the direction, including a systematic review of ketamine in migraine and other primary headaches and a review of NMDA antagonists as anti-migraine agents. A retrospective cohort study also examined lidocaine and ketamine infusions for headache disorders.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK trial: intranasal sub-dissociative ketamine vs standard care for primary headache in the ED; no results in data |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead: placebo-controlled RCT of high-dose IV ketamine (1 mg/kg/h for 6 hours) in chronic daily headache; expected completion 2027 |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | Low-dose ketamine vs prochlorperazine (Compazine) for headache in the ED |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | NA | Completed | 34 | Placebo-controlled trial of sub-dissociative ketamine for acute migraine in the ED |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine spray in chronic cluster headache |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Completed | 93 | Single ketamine infusion plus magnesium sulfate in refractory chronic cluster headache; the combination confounds the ketamine-specific effect |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs ketorolac in acute tension-type headache; completion and reporting uncertain |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine plus aspirin vs rimegepant in ED headache; too small to be informative |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Completed | 300 | PACE study: observational analgesic study, not clearly headache-specific (indirect relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society 2025 update on parenteral drugs for acute migraine in the ED |
| [34703891](https://pubmed.ncbi.nlm.nih.gov/34703891/) | 2021 | Systematic review | J Dent Anesth Pain Med | Efficacy of ketamine in migraine and other primary headaches vs placebo and active comparators |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedeberg's Arch Pharmacol | Memantine and ketamine (NMDA antagonists) as potential anti-migraine agents |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective cohort | Front Neurol | IV lidocaine and ketamine infusions for headache disorders: efficacy, duration and safety |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Systematic review / meta-analysis | J Neurol | Preventive treatments for refractory chronic cluster headache |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Drug treatment of cluster headache (acute and preventive) |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Pharmacotherapy for trigeminal neuralgia; ketamine named as a possible adjuvant option |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Curr Neurol Neurosci Rep | ED and inpatient management of headache in children and adolescents |
| [37806714](https://pubmed.ncbi.nlm.nih.gov/37806714/) | 2023 | Review | Prog Brain Res | Migraine and treatment-resistant depression, including their comorbidity |
| [35416105](https://pubmed.ncbi.nlm.nih.gov/35416105/) | 2022 | Review | Expert Opin Drug Saf | Long-term safety of ketamine and esketamine (studied in depression) |

Many other retrieved papers concern ketamine in depression, which is not the target indication, so they are not listed here.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016812 (cancelled) | Ketalar | Injection | Not specified |
| ANDA074549 (cancelled) | Ketamine Hydrochloride | Injection, solution, concentrate | Not specified |
| ANDA216809 (cancelled) | Ketamine Hydrochloride | Injection, solution | Not specified |
| ANDA074524 (cancelled) | Ketamine Hydrochloride | Injection | Not specified |
| ANDA215808 (cancelled) | Ketamine hydrochloride | Injection | Not specified |

A sixth authorization, ANDA076092 (Eugia US LLC, injection), is also cancelled. All six authorizations are listed as cancelled, so no valid U.S. authorization appears in the data compiled for this report.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (drug-disease edges from the TxGN knowledge graph, not label text):
- Cardiovascular: hypertension, hypertensive disorder, myocardial infarction, myocardial ischemia, coronary artery disease, coronary thrombosis
- Cerebrovascular: stroke, cerebrovascular disorder, cerebral infarction, susceptibility to ischemic stroke
- Intracranial and ocular pressure: intracranial hypertension, pseudotumor cerebri, ocular hypertension
- Other: substance abuse/dependence, delirium, respiratory failure, thyrotoxicosis/hyperthyroidism/Graves disease, hemoglobinopathy

Several of these (hypertension, cardiovascular and cerebrovascular disease) are relevant to a headache population and would need careful screening.

**Drug Interactions** (100 interactions were found; examples shown):
- Moderate: morphine, diphenoxylate, dronabinol, nabilone, opium (additive CNS/respiratory depression is plausible), metoclopramide, sibutramine, phentermine, ephedrine, fenfluramine, isometheptene, topical epinephrine
- Unknown severity: atropine, amphotericin B, famotidine, omeprazole, potassium chloride, ondansetron, ursodeoxycholic acid

Some of these are commonly used with headache treatments (e.g., metoclopramide, ondansetron), which makes co-medication review important.

Please refer to the package insert for key warnings and contraindications; this label information was not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Several trials directly test ketamine in headache, and the mechanistic rationale is plausible. However, no trial results are available, the one completed Phase 3 trial is small (n=80), and the other Phase 3 trial is still recruiting. In addition, all U.S. authorizations are cancelled and the package insert safety data is missing, which blocks safety screening. Ketamine also carries a substantial set of cardiovascular and neurological contraindication signals.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap for safety screening)
- Results from THINK (NCT03081416) and other completed trials, plus the outcome of KetHead (NCT05306899, expected 2027)
- Mechanism of action data from DrugBank
- Clarification of the current U.S. regulatory and supply status, given that all authorizations are cancelled
- Route and formulation assessment (IV vs intranasal vs oral) for the headache setting
- A safety plan for patients with cardiovascular or cerebrovascular disease, raised intracranial pressure, or substance-use history
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

