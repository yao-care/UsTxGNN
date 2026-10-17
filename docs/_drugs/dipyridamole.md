---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 613
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dipyridamole: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["stroke disorder", "thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cavernous sinus thrombosis", "lateral sinus thrombosis"]
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dipyridamole: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilator drug, listed in the knowledge graph for atrial fibrillation.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials** and only **10 publications** are available for this indication, and none of them show therapeutic benefit.
By contrast, the next-ranked predictions of **stroke** and **transient ischemic attack** are already supported by large trials and meta-analyses, although these are established uses rather than new repurposing opportunities.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (from the knowledge graph; the US licence records contain no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (for Prinzmetal angina; stroke and TIA reach L1 but are established uses) |
| US Market Status | Cancelled only (all licences cancelled) |
| Number of NDAs | 8 (all are ANDA generic applications) |
| Recommended Decision | Hold (for Prinzmetal angina); Proceed with Guardrails (for stroke and TIA) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, dipyridamole inhibits adenosine reuptake and phosphodiesterase activity. This raises adenosine and cAMP/cGMP levels, which inhibits platelet aggregation and causes coronary vasodilation.

For Prinzmetal angina, the mechanistic link is weak. The literature mostly describes dipyridamole as a stress-testing agent rather than a treatment. One report (PMID 3421166) describes coronary vasospasm triggered when aminophylline ended dipyridamole stress in variant angina patients. That is a provocative context, not a therapeutic one. Adenosine-mediated vasodilation could also cause coronary steal, so a therapeutic role is uncertain and possibly unfavorable.

The predictions with real support are in cerebrovascular disease. The antiplatelet mechanism is coherent with stroke and TIA secondary prevention, and the combination of aspirin and extended-release dipyridamole is a recognised option. Thrombotic disease in general is mechanistically plausible but supported only by indirect, mostly general-review literature. The other top-10 predictions (sick sinus syndrome, sarcoglycanopathy, Wildervanck syndrome, a macrocephaly syndrome, and cavernous and lateral sinus thrombosis) have no trials or literature, and for several there is no plausible mechanistic rationale.

## Clinical Trial Evidence

**Prinzmetal angina (top prediction):** Currently no related clinical trials registered.

**Stroke disorder (rank 2, the best-supported prediction):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | Completed | 4500 | ESPRIT: aspirin plus dipyridamole or mild anticoagulation vs aspirin alone after cerebral ischaemia of arterial origin |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | Completed | 551 | EARLY: Aggrenox started within 24 hours of stroke vs after 7 days of aspirin in ischaemic stroke |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | Completed | 250 | Feasibility of anticoagulants vs antiplatelets in cervical artery dissection (indirect relevance) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure or anticoagulants vs antiplatelet therapy to prevent stroke recurrence (indirect) |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | Completed | 664 | Gore REDUCE: PFO closure plus antiplatelets vs antiplatelets alone (device trial, indirect) |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | Completed | 240 | Oxidative stress and oxysterol profiling with aspirin plus dipyridamole after carotid revascularization (biomarker study) |
| [NCT06053021](https://clinicaltrials.gov/study/NCT06053021) | N/A | Unknown | 1200 | Antiplatelet therapy in acute ischaemic stroke with thrombocytopenia (indirect) |
| [NCT06983795](https://clinicaltrials.gov/study/NCT06983795) | N/A | Not yet recruiting | 1000 | Asia-Pacific registry of PFO and ischaemic stroke (indirect) |

Transient ischemic attack is supported by the same ESPRIT trial (NCT00161070) and the Gore REDUCE study (NCT00738894).

## Literature Evidence

**Prinzmetal angina:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Jpn Circ J | Drug responses in 26 patients with rest angina, including dipyridamole 50 mg; propranolol tended to aggravate attacks |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Small clinical study | Am J Cardiol | Aminophylline termination of dipyridamole stress triggered vasospasm in variant angina |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Diagnostic study | Br Heart J | Reproducibility of exercise testing in patients with ST elevation and varying dipyridamole test responses |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic study | Jpn Circ J | Dipyridamole-loading thallium imaging for detecting coronary artery disease |

These papers are diagnostic or descriptive and do not show therapeutic benefit.

**Stroke and TIA (the best-supported predictions):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | Individual patient data meta-analysis of dipyridamole, with or without aspirin, for secondary prevention after stroke or TIA |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane review | Cochrane Database Syst Rev | Adding dipyridamole to aspirin was associated with a 22% risk reduction vs aspirin alone in one trial |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | Collaborative meta-analysis of antiplatelet therapy in high-risk patients |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analysis | J Neurol Sci | Aspirin plus dipyridamole vs aspirin in secondary prevention after TIA or stroke |
| [31177983](https://pubmed.ncbi.nlm.nih.gov/31177983/) | 2019 | Network meta-analysis | Stroke | Efficacy and safety of antiplatelet agents after noncardioembolic stroke or TIA |
| [26304937](https://pubmed.ncbi.nlm.nih.gov/26304937/) | 2015 | Network meta-analysis | J Am Heart Assoc | Long-term antiplatelet mono- and dual therapies after ischaemic stroke or TIA |
| [34211246](https://pubmed.ncbi.nlm.nih.gov/34211246/) | 2021 | Review | Aust Prescr | Aspirin, clopidogrel, or aspirin plus dipyridamole are first-line options in the absence of atrial fibrillation |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann N Y Acad Sci | Possible neuroprotective and anti-inflammatory effects of dipyridamole during acute stroke |

## US Market Information

All eight US licences are generic applications and all are cancelled. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040874 | Dipyridamole (Zydus) | Film-coated tablet | Not available |
| ANDA040542 | Dipyridamole (Oxford) | Film-coated tablet | Not available |
| ANDA074521 | Dipyridamole (Henry Schein) | Injection | Not available |
| ANDA040782 | Dipyridamole (Amneal) | Tablet | Not available |
| ANDA207944 | Aspirin and Extended-Release Dipyridamole (Major) | Capsule | Not available |

Three further aspirin/extended-release dipyridamole applications (ANDA209048, ANDA209929, ANDA206392) are also cancelled.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for them.

- **Disease associations from the knowledge graph** (these are graph edges, not label text): kidney disease, liver disease, gallbladder disease, thrombocytopenia, peptic ulcer disease, gout, hypotensive disorder, acute coronary syndrome, myocardial infarction, hemophilia, anemia, and others. Many of these appear to come from the aspirin component of the combination products and need verification against the label.
- **Drug interactions:** 100 interactions were found. Moderate-level ones are dexfenfluramine, sibutramine and fenfluramine. Others, including acetylsalicylic acid, cimetidine, omeprazole, pantoprazole, lansoprazole, metformin, glimepiride, rosiglitazone, simvastatin, prednisone and morphine, are listed at an unknown severity level.
- **Prinzmetal angina specific concern:** adenosine-mediated vasodilation may cause coronary steal, and vasospasm has been reported after dipyridamole stress testing.

## Conclusion and Next Steps

**Decision: Hold** (Prinzmetal angina, the top TxGNN prediction)

For stroke and TIA: **Proceed with Guardrails**, but only as an established indication.

**Rationale:**
- The top prediction, Prinzmetal angina, has no registered trials, only diagnostic or descriptive literature, and a mechanistic argument that is uncertain and possibly unfavorable. The high TxGNN score alone is not enough.
- Stroke and TIA have strong evidence (ESPRIT, meta-analyses), but this is existing use, not new repurposing. All US licences are cancelled, so market availability must be checked before any recommendation.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- For Prinzmetal angina, controlled clinical data on therapeutic benefit and the coronary steal and vasospasm risk
- Confirmation of current US market availability, since all eight licences are cancelled
- Review of the knowledge-graph contraindications, especially thrombocytopenia, bleeding disorders, peptic ulcer, and cardiovascular conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

