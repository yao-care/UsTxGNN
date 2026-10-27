---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 897
evidence_level: L5
indication_count: 4
monitor_inn: "MEMANTINE"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-10-14
description: "Memantine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data"
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Memantine: From Alzheimer's-Type Dementia to Migraine Disorder
{: .text-alpha }

Note: The data compiled for this report contains no approved-indication text for memantine, so the original indication is not stated in the regulatory data. The framing above reflects memantine's well-known use as an NMDA receptor antagonist. The report focuses on the best-supported prediction, **migraine disorder** (rank 2), rather than the top-scoring one (pulmonary hypertension), because migraine has far stronger evidence.

## One-Sentence Summary

Memantine is an NMDA receptor antagonist whose original indication could not be confirmed from the regulatory data compiled for this report.
The TxGNN model gave **migraine disorder** a score of 99.5%, and the topic is supported by **1 completed Phase 3 trial** and **about 20 publications**, including systematic reviews and a meta-analysis.
The evidence is real but modest in quality: the only Phase 3 trial is small (33 patients) and compares memantine with another drug rather than with placebo.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data (no approved-indication text was recorded for any license) |
| Predicted New Indication | Migraine disorder (the top-ranked prediction, pulmonary hypertension, has only L5 evidence) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 (rests on one completed Phase 3 trial; quality is modest) |
| US Market Status | Cancelled only (all licenses are listed as cancelled) |
| Number of NDAs | 13 (all are ANDA generic applications, none currently valid) |
| Recommended Decision | Hold (research question; larger placebo-controlled trials are needed) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Memantine is known as an NMDA receptor antagonist, and the literature gathered for this report is consistent with that.

Migraine is thought to involve glutamatergic hyperexcitability and cortical spreading depression. Blocking NMDA receptors is therefore a plausible way to prevent attacks. Reviews describe higher glutamate levels in migraine patients, especially during attacks. Genetic studies also implicate glutamate-signalling genes.

The link between memantine's original use and migraine is the shared target (NMDA receptors) rather than a similar disease. The evidence base is still limited. One commentary is titled "Memantine for migraine: big promise but little evidence" (PMID 34510445).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Memantine vs sodium valproate for preventing episodic migraine. Small, active-comparator design, so it cannot show absolute efficacy. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clin Neuropharmacol | Memantine vs placebo in migraine; the authors note efficacy remains controversial |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic review | Headache | Efficacy and safety of memantine for preventing episodic migraine |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Systematic review | Ann Pharmacother | Data on memantine for preventing primary headache disorders |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network meta-analysis | Front Pharmacol | Comparison of oral migraine preventives in adults aged 18-65 |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn Schmiedebergs Arch Pharmacol | Memantine and ketamine as potential anti-migraine agents |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical guideline | Ann Intern Med | 2023 VA/DoD guideline on treating and preventing migraine and tension-type headache |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective study | J Headache Pain | Memantine as migraine prevention in 60 patients at a headache clinic |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary | Headache | "Big promise but little evidence" |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Glutamate and its receptors as migraine targets |
| [34048395](https://pubmed.ncbi.nlm.nih.gov/34048395/) | 2021 | Review | Continuum | Overview of preventive migraine treatments |

A placebo-controlled RCT in migraine without aura ([PMID 26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/), Headache, 2016) is also in the literature set, but it was retrieved under the brainstem-aura prediction and covers a different migraine subtype.

## US Market Information

All 13 US authorizations are generic applications (ANDAs) and all are listed as cancelled. No approved-indication text was recorded. The first five are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA213985 | Memantine Hydrochloride (Vitruvias) | Extended-release capsule | Not recorded |
| ANDA202840 | Memantine Hydrochloride (Macleods) | Tablet | Not recorded |
| ANDA200022 | Memantine Hydrochloride (Unichem) | Film-coated tablet | Not recorded |
| ANDA200891 | Memantine Hydrochloride (Alembic) | Coated tablet | Not recorded |
| ANDA203293 | Memantine Hydrochloride (Zydus) | Extended-release capsule | Not recorded |

Available forms are oral (extended-release capsule, tablet, film-coated tablet, coated tablet) and an oral solution.

## Safety Considerations

- **Knowledge-graph disease associations (not label text)**: The TxGNN knowledge graph links memantine to contraindication edges for liver disease, gallbladder disease and impaired renal function. These should be checked against the actual label.
- **Drug Interactions**: 100 interactions were found in total; the 20 reviewed here are mostly Minor or Moderate. The Moderate ones are anticholinergic or antispasmodic drugs: hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate. Minor interactions include ranitidine, metformin, cimetidine and potassium citrate. Several others (glimepiride, doxycycline, lansoprazole, loperamide, famotidine, aspirin) have an unknown severity level.

Please refer to the package insert for warnings and contraindications. That label information was not available for this report, which blocks formal safety screening.

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Migraine has a plausible mechanism and a completed Phase 3 trial, which gives it a formal L1 grade. In practice the evidence is weak. The trial is small and uses an active comparator, and the literature itself describes the evidence as limited. The other predictions are weaker still:
- **Pulmonary hypertension** (99.54%) is L5. The linked papers concern a different compound (MN-08) or a metabolic topic, so they do not support memantine.
- **Kyphoscoliotic heart disease** (99.43%) has no trials, no literature and no plausible mechanism. It is likely a knowledge-graph artifact.
- **Migraine with brainstem aura** (99.41%) is L4. It relies on indirect mechanistic reviews and an RCT in a different subtype.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Confirmation of the approved original indication and current US market status, since all licenses show as cancelled
- Larger, adequately powered placebo-controlled trials of memantine in migraine prevention
- A close reading of the meta-analysis and systematic reviews (PMIDs 33961371, 34352118) to judge the true effect size and safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

