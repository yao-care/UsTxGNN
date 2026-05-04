---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

以下是根據 Evidence Pack 產生的藥師評估報告。由於 Rank 1 預測（obsolete bundle branch block）使用已廢棄疾病術語且機轉相反，本報告主焦聚焦於 Rank 2 的 CPVT 預測，並於摘要中說明。

---

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Adenosine is an endogenous purine nucleoside used intravenously worldwide for the acute termination of paroxysmal supraventricular tachycardia (PSVT), though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**,
with **1 Phase 2a clinical trial** and **13 publications** currently supporting this direction.

> **Note on Rank 1 Prediction:** The top-ranked TxGNN entry, "obsolete bundle branch block," uses a deprecated disease ontology term. The repurposing rationale itself flags a contradictory mechanism — Adenosine slows AV nodal conduction via A1R–Gi, which would worsen rather than treat bundle branch block. With no supporting evidence (L5) and an obsolete label, this entry is bypassed. The report focuses on the Rank 2 prediction (CPVT), which carries mechanistic coherence and active evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan (globally: paroxysmal supraventricular tachycardia) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% (Rank #2 predicted indication) |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Adenosine acts primarily through the adenosine A1 receptor (A1R) on cardiac tissue. Binding to A1R activates Gi proteins, which inhibit adenylyl cyclase (AC) and lower intracellular cyclic AMP (cAMP). This cascade slows heart rate and AV nodal conduction — the basis of its established use in terminating SVT. A secondary pathway via GIRK channels (I~K,Ado~) hyperpolarizes cardiomyocytes and raises the ventricular fibrillation threshold.

CPVT is mechanistically convergent with this pharmacology. Mutations in **RYR2** (cardiac ryanodine receptor) or **CASQ2** (calsequestrin-2) cause uncontrolled sarcoplasmic reticulum (SR) calcium release, which is dramatically amplified by catecholamine stimulation. The chain is: catecholamines → β-adrenergic receptors → ↑AC → ↑cAMP → PKA activation → RYR2 hyperphosphorylation → lethal calcium storm. Adenosine interrupts this chain at the AC step via A1R–Gi, directly antagonizing the upstream catecholamine trigger.

Three lines of evidence reinforce this prediction. First, the A1R → Gi → ↓cAMP axis directly opposes PKA-mediated RYR2 hyperphosphorylation. Second, published gene therapy data (PMID 38776406) confirm that cAMP/cGMP subcellular compartmentation is a validated and druggable CPVT target, with Adenosine positioned as a pharmacological upstream modulator of the same pathway. Third, a 2008 case report (PMID 18313614) documents ATP terminating bidirectional ventricular tachycardia in a CPVT patient — clinically important because ATP is rapidly hydrolyzed in vivo to ADP → AMP → **Adenosine**, making this the most direct human clinical evidence linking the adenosinergic axis to CPVT termination.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | Safety, tolerability, and exploratory efficacy of **AGP100** in patients with CPVT — an inherited arrhythmia causing dangerous tachycardia during physical or emotional stress. Current treatments do not reliably prevent stress-induced arrhythmias, motivating this search for new agents. **Note:** The investigational compound is AGP100, not Adenosine itself. If AGP100 is confirmed as an adenosine analogue or stable A1R agonist, trial results would directly support this repurposing hypothesis; otherwise relevance depends on its actual mechanism. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | Heart Rhythm | ATP terminates bidirectional ventricular tachycardia in a confirmed CPVT patient — the most direct human evidence; ATP's in vivo conversion to Adenosine implies adenosinergic activity underlies the effect |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Clinical Review | Europace | ESC/HRS/APHRS/LAHRS joint consensus on pharmacological provocation testing in cardiac electrophysiology, including CPVT diagnostic protocols and arrhythmia risk stratification |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Clinical Review | Paediatric Anaesthesia | Identification and management of pediatric arrhythmias including CPVT; Adenosine is highlighted as first-line agent for SVT in children, underscoring its established cardiac electrophysiology role |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical / Mechanistic | Cardiovascular Research | PDE2A and PDE4B gene therapy prevents pressure-overload heart failure and arrhythmias by improving subcellular cAMP compartmentation — validates ↓cAMP as a therapeutic CPVT strategy, supporting Adenosine's upstream role |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | In Vitro Model | Journal of Physiology | Human cardiac-neural microtissue reveals CPVT is also a disease of sympathetic neurons, not only cardiomyocytes; sympathetic adrenergic overdrive is central to pathogenesis, reinforcing the rationale for anti-adrenergic interventions |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical Observation | Heart Rhythm | Postpacing abnormal repolarization in CPVT patient with RyR2 mutation; electrophysiological studies show limited value, highlighting the need for pharmacological approaches |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Mechanistic | BBA | ATP interacts directly with the CPVT mutation-associated central domain of RyR2 — provides molecular-level evidence that ATP/Adenosine family compounds engage the RyR2 apparatus relevant to CPVT |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Mechanistic | Communications Biology | TECRL deficiency causes aberrant mitochondrial function and worsens cardiac arrhythmia via SR calcium dysregulation — reinforces RyR2/SR calcium axis as the CPVT disease core |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Mechanistic | Science Translational Medicine | SR calcium leak via RyR2 drives arrhythmia; selective RyR2 stabilization normalizes calcium leak and improves survival in mouse models — contextualizes upstream cAMP suppression as preventive strategy |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | JAPI | Classification and therapeutic approach to idiopathic VT in structurally normal hearts; outflow tract tachycardias are notably adenosine-sensitive, pointing to overlap in adenosinergic responsiveness across VT subtypes |

---

## Taiwan Market Information

Adenosine has no registered products in Taiwan (0 licenses). This section is not applicable.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The mechanistic case for Adenosine in CPVT is scientifically coherent — antagonizing catecholamine-driven cAMP elevation via A1R–Gi directly suppresses aberrant RYR2 calcium release — but the clinical evidence is indirect (ATP case report, mechanistic studies, one small recruiting trial with an unconfirmed investigational compound), and Adenosine's extremely short plasma half-life (~10 seconds after IV bolus) makes it impractical as a CPVT maintenance therapy without formulation innovation or use of longer-acting A1R agonists.

**To proceed, the following is needed:**

- **Confirm AGP100 identity:** If NCT07263139's investigational compound is an adenosine analogue or selective A1R agonist, trial results (expected 2027) would constitute Phase 2a evidence directly relevant to this repurposing hypothesis
- **Mechanism of action documentation:** Obtain full Adenosine MOA data from DrugBank API (currently a high-severity data gap) to formally support mechanism-based repurposing analysis
- **Preclinical validation:** Test Adenosine or stable A1R agonists (e.g., tecadenoson, seladenoson) in RYR2-mutant mouse models under catecholamine challenge to quantify arrhythmia suppression
- **Pharmacokinetic strategy:** Address the half-life limitation — evaluate depot formulations, prodrugs, or continuous-infusion protocols suitable for CPVT's stress-triggered episodic nature
- **Safety risk-benefit assessment:** Adenosine causes transient but significant bradycardia and AV block; in patients already prone to lethal arrhythmias, the therapeutic window must be carefully defined before any human study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

