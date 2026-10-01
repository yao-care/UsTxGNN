---
layout: default
title: Apixaban
parent: Moderate Evidence (L3-L4)
nav_order: 392
evidence_level: L4
indication_count: 1
---

# Apixaban
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Apixaban: From Anticoagulation (Thromboembolism Prevention) to Migraine Disorder

## One-Sentence Summary

Apixaban is an oral direct factor Xa inhibitor (anticoagulant) that is marketed in the US.
The TxGNN model predicts it may be effective for **migraine disorder**, but the supporting evidence is weak: **1 indirectly related clinical trial** and **4 publications**, mostly case reports, with conflicting signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data; apixaban is an oral anticoagulant |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, apixaban is a direct factor Xa inhibitor used for anticoagulation. It has no known direct effect on migraine pathophysiology (CGRP signalling, cortical spreading depression, trigeminovascular activation).

The link between the original and predicted indications is speculative. One hypothesis is that migraine with aura may involve paradoxical microembolism (for example through a patent foramen ovale) or a prothrombotic state such as antiphospholipid antibodies. Anticoagulation could in theory modify either. The 99.02% TxGNN score is a knowledge-graph prediction only and is not confirmed by clinical data.

The available clinical signals are inconsistent. One case report describes aura worsening after starting apixaban. Another describes aura resolving on warfarin but not on apixaban. Together they argue against a class-wide anticoagulant benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compares PFO closure vs anticoagulants vs antiplatelet therapy to prevent stroke recurrence. Migraine is not the primary condition or endpoint, and apixaban is not confirmed as the anticoagulant studied. Relevance grade C (indirect only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Antithrombotic therapy trials in refractory migraine with antiphospholipid antibodies. The abstract excerpt does not report results, and the specific drugs used (including apixaban) are not verified. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report with literature review | The Neurologist | Migraine with aura worsened after starting apixaban. The review notes that literature on direct oral anticoagulants in migraine is scarce and controversial. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | A 55-year-old woman had 12 years of remission of migraine with aura on warfarin. Symptoms returned within 3 weeks of switching to apixaban and resolved again within days of resuming warfarin. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case report | Headache | Vestibular migraine resolved on warfarin and topiramate. Apixaban was not the effective agent. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA202155 | ELIQUIS (Cardinal Health 107, LLC) | Tablet, film coated | Not listed in source data |
| NDA202155 | ELIQUIS (E.R. Squibb & Sons, L.L.C.) | Tablet, for suspension | Not listed in source data |
| NDA202155 | ELIQUIS (A-S Medication Solutions) | Tablet, film coated | Not listed in source data |
| NDA202155 | ELIQUIS (E.R. Squibb & Sons, L.L.C.) | Tablet, film coated | Not listed in source data |
| NDA202155 | ELIQUIS (A-S Medication Solutions) | Tablet, film coated | Not listed in source data |

The record lists 20 licenses in total, and the five above are the main ones shown. All are oral products.

---

## Safety Considerations

- **Clinical signal in migraine:** One case report (PMID 37582651) describes migraine with aura worsening after starting apixaban. This is an isolated report and causality is not established.

Please refer to the package insert for warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by clinical evidence. The only completed Phase 3 trial is indirect (stroke prevention in a PFO population), and the migraine literature consists of case reports with conflicting direction, including one report of worsening on apixaban. The mechanistic link is speculative.

**To proceed, the following is needed:**
- Apixaban mechanism of action and original indication data (DrugBank), to allow a proper mechanistic-link analysis
- FDA package insert warnings and contraindications, which is a blocking gap for safety screening
- Verification of which antithrombotic agents were used in the antiphospholipid antibody migraine study (PMID 33402037), and confirmation of the anticoagulant in NCT00562289
- Any controlled or prospective data on apixaban in migraine, in particular migraine with aura in PFO or antiphospholipid antibody subgroups
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

