---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 216
evidence_level: L5
indication_count: 2
monitor_inn: "ADENOSINE"
predicted_indications: ["obsolete bundle branch block", "catecholaminergic polymorphic ventricular tachycardia"]
last_modified_at: 2026-10-14
description: "Adenosine: predicted new indication Catecholaminergic polymorphic ventricular tachycardia . The rank 1 pr… (evidence level L5). Approved use: Ventricular tachycardia"
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Adenosine: From Ventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Adenosine was originally used to treat ventricular tachycardia (as recorded in the knowledge graph used for this report).
The TxGNN model's top-ranked prediction is "obsolete bundle branch block", which looks like an ontology artifact. This report therefore focuses on the second-ranked and more plausible prediction, **catecholaminergic polymorphic ventricular tachycardia (CPVT)**.
Evidence is limited: **0 clinical trials** and **10 publications**, of which only **1 case report** (using ATP, not adenosine) directly addresses CPVT.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular tachycardia (from knowledge graph; no approved-indication text in the license records) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia (rank 2). The rank 1 prediction, "obsolete bundle branch block" (score 99.94%, L5), is not pursued because the term is obsolete and the mechanism is implausible. |
| TxGNN Prediction Score | 99.42% (CPVT); 99.94% (obsolete bundle branch block) |
| Evidence Level | L4 (CPVT); L5 (obsolete bundle branch block) |
| US Market Status | Cancelled only |
| Number of NDAs | 8 license records (all cancelled; all listed under ANDA numbers or without a number) |
| Recommended Decision | Hold (CPVT treated as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known pharmacology, adenosine acts on A1 receptors in the heart, slowing AV nodal conduction and opposing catecholamine-driven cAMP signaling.

CPVT is caused by abnormal sarcoplasmic reticulum calcium leak (RYR2, CASQ2, TECRL variants), producing delayed afterdepolarizations and triggered activity during adrenergic stimulation. Because adenosine and ATP can counter adrenergic cAMP signaling and suppress triggered activity, a mechanistic link to CPVT is plausible. It is also consistent with the original ventricular tachycardia indication.

The direct clinical signal is thin: a single case report in which adenosine triphosphate terminated bidirectional ventricular tachycardia in a CPVT patient. Standard CPVT care (beta-blockers, flecainide, sympathetic denervation, ICD) would not be replaced. At most, adenosine might serve an acute, adjunctive, or diagnostic role.

For the top-ranked prediction, obsolete bundle branch block, no plausible therapeutic rationale is apparent. The term is flagged as obsolete, so the score likely reflects a graph artifact. Slowing conduction could in principle worsen conduction disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The abstracts supplied were truncated, so the findings below are based on titles and the available abstract text only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case report | Heart Rhythm | ATP terminated bidirectional ventricular tachycardia in a CPVT patient (the only direct clinical signal; ATP, not adenosine) |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review (consensus statement) | Europace | Role of pharmacological provocation testing in cardiac electrophysiology for diagnosing causes of sudden cardiac arrest and arrhythmias |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Recognition and management of ventricular tachycardia in structurally normal hearts |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | Paediatr Anaesth | Pediatric arrhythmias for anesthesiologists, including risk in inherited channelopathies |
| [15324613](https://pubmed.ncbi.nlm.nih.gov/15324613/) | 2004 | Review | Curr Treat Options Cardiovasc Med | Syncope treatment alternatives (indirect context) |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical observational | Heart Rhythm | Abnormal post-pacing repolarization in CPVT with an RYR2 mutation; electrophysiological studies of limited value |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Preclinical/mechanistic | Commun Biol | TECRL deficiency causes aberrant mitochondrial function in cardiomyocytes |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical/mechanistic | Cardiovasc Res | PDE2A and PDE4B gene therapy improves heart failure and arrhythmias via cAMP compartmentation in mice |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical/mechanistic | Sci Transl Med | SR calcium leak contributes to arrhythmia but not heart failure progression |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclinical/mechanistic | J Physiol | Human cardiac-neural microtissues suggest CPVT also involves the sympathetic neuron |

No literature was retrieved for the rank 1 prediction (obsolete bundle branch block).

---

## US Market Information

All 8 license records are cancelled; none is currently valid. No approved-indication text is available in these records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090212 | Adenosine (Mylan Institutional LLC) | Injection, solution | Not available |
| ANDA077425 | Adenosine (Meitheal Pharmaceuticals Inc.) | Injection, solution | Not available |
| ANDA206778 | Adenosine (Gland Pharma Limited) | Solution | Not available |
| ANDA077133 | Adenosine (Henry Schein, Inc.) | Injection, solution | Not available |
| ANDA202313 | Adenosine (Heritage Pharmaceuticals / Avet) | Injection, solution | Not available |

Three further cancelled records exist (ANDA078686, ANDA205568, and a cosmetic cream product, "The Skinhouse Wrinkle Collagen", with no license number).

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for authoritative safety information.

- **Knowledge-graph contraindication signals** (not label text): chronic obstructive pulmonary disease, asthma (including intrinsic and allergic forms), aortic stenosis and aortic valve disease, hypotensive disorder, acute coronary syndrome, coronary artery disease, atrioventricular block, sick sinus syndrome, pulmonary emphysema, respiratory failure, pericarditis, mitral valve stenosis, pulmonary valve insufficiency, autonomic nervous system disease, and Horner syndrome. The AV block and sick sinus syndrome signals are consistent with adenosine's conduction-slowing effect, which also argues against the bundle branch block prediction.
- **Drug Interactions** (100 interactions found; examples shown):
  - **Major**: cisapride, dolasetron, papaverine
  - **Moderate**: famotidine, clarithromycin, granisetron, levofloxacin, ondansetron, palonosetron
  - Many other listed interactions (e.g. pantoprazole, morphine, metformin, epinephrine) have an unknown severity level.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank 1 prediction (obsolete bundle branch block) has no evidence and no plausible mechanism, and it relies on an obsolete ontology term, so it should not be pursued.
- The rank 2 prediction (CPVT) is mechanistically plausible but supported only by one case report involving ATP and by indirect preclinical and review literature. It is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, and a safety screening based on them
- Mechanism of action data for adenosine
- Review of the full text of the CPVT-related papers, particularly the ATP case report
- Preclinical or small exploratory clinical data testing adenosine in CPVT models or patients, including acute termination and diagnostic roles
- Clarification of current US marketing status, since all license records are cancelled
- Route compatibility assessment, since the injectable form is the relevant one for acute use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

