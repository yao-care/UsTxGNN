---
layout: default
title: Hydromorphone
parent: Moderate Evidence (L3-L4)
nav_order: 777
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Hydromorphone: predicted new indication Pharyngitis (evidence level L4). Approved use: Common cold, nasopharyngitis"
monitor_inn: "HYDROMORPHONE"
predicted_indications: ["pharyngitis", "allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Hydromorphone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

## Hydromorphone: From Common Cold to Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Hydromorphone is an opioid medicine. In the knowledge graph its listed original indications are the common cold and nasopharyngitis, while its actual US products are opioid analgesics.
The TxGNN model predicts it may be effective for **Pharyngitis**, but the **3 related clinical trials** are all post-tonsillectomy pain studies and **no publications** directly address pharyngitis.
The strongest signal in the data is for **headache disorder**, where evidence exists but does not favor hydromorphone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common cold, nasopharyngitis (from the knowledge graph; no approved indication text is available for the US licenses) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all cancelled; includes ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, hydromorphone is a mu-opioid receptor agonist that produces central analgesia. In principle it could relieve the pain of an inflamed throat.

The link to the original indications is weak. Pharyngitis is closely related to the common cold and nasopharyngitis, which likely explains the high model score. However, the three trials found are post-tonsillectomy pain studies, not pharyngitis treatment trials. They show opioids are used for pain in a related throat-surgery setting, but they give no evidence that hydromorphone treats the infection or inflammation. Non-opioid analgesics are preferred for routine pharyngitis pain, and the 0.998 score is a computational prediction only.

Other predicted indications rank similarly on score but have even less support:
- **Allergic urticaria, nasal cavity disease, trigeminal autonomic cephalalgia:** no trials or literature. For urticaria, opioids can cause histamine release, so the pharmacology points toward an adverse effect.
- **Acute laryngopharyngitis:** no clinical evidence, and the risks (respiratory depression, dependence) outweigh benefit in a self-limiting condition.
- **Headache disorder:** the only other prediction with trials and literature (see below).

---

## Clinical Trial Evidence

Trials for the top prediction (pharyngitis):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Early Phase 1 | Completed | 189 | Hydromorphone vs fentanyl for pain control in children after tonsillectomy. Indirect evidence (postoperative pain, not pharyngitis). |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Phase 2 | Completed | 66 | Short-acting opioids (fentanyl/hydromorphone) vs methadone for pediatric post-tonsillectomy pain. The study drug is methadone; little relevance. |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Phase 4 | Recruiting | 440 | Intraoperative methadone vs short-acting opioids in pediatric tonsillectomy. No results yet; not relevant to pharyngitis. |

Trial for the headache disorder prediction (the most direct comparative data):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02389829](https://clinicaltrials.gov/study/NCT02389829) | Phase 4 | Completed | 127 | Emergency department RCT of hydromorphone vs prochlorperazine + diphenhydramine for acute migraine. Directly relevant, but a head-to-head comparison against active non-opioid therapy that does not favor hydromorphone. |

---

## Literature Evidence

No literature is available for pharyngitis. The literature below relates to the headache disorder prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29046364](https://pubmed.ncbi.nlm.nih.gov/29046364/) | 2017 | RCT | Neurology | IV prochlorperazine + diphenhydramine vs IV hydromorphone for migraine in the emergency department |
| [34363617](https://pubmed.ncbi.nlm.nih.gov/34363617/) | 2021 | RCT (post hoc analysis) | Headache | Effect of hydromorphone vs prochlorperazine on migraine-associated symptoms |
| [17981511](https://pubmed.ncbi.nlm.nih.gov/17981511/) | 2008 | Cohort (retrospective) | J Pain | Metoclopramide vs hydromorphone for initial emergency department migraine treatment, comparing pain score changes |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 American Headache Society update on parenteral treatment of acute migraine in the emergency department |
| [27300483](https://pubmed.ncbi.nlm.nih.gov/27300483/) | 2016 | Guideline | Headache | Original American Headache Society evidence assessment of parenteral drugs for acute migraine in the emergency department |
| [29461426](https://pubmed.ncbi.nlm.nih.gov/29461426/) | 2018 | Review | Curr Opin Neurol | Review of emergency management of primary headache |
| [39924451](https://pubmed.ncbi.nlm.nih.gov/39924451/) | 2025 | Systematic review/meta-analysis | Addiction | Relative risks of adverse effects across opioid agonist treatments |
| [29516486](https://pubmed.ncbi.nlm.nih.gov/29516486/) | 2018 | Observational | Headache | Opioid-induced "likeability" and "feeling good" were not associated with return ED visits among migraine patients given IV hydromorphone |
| [24948146](https://pubmed.ncbi.nlm.nih.gov/24948146/) | 2015 | Survey analysis | Cephalalgia | Current medication use for acute migraine in US emergency departments compared with 1998 |
| [32781832](https://pubmed.ncbi.nlm.nih.gov/32781832/) | 2020 | Retrospective database analysis | Cephalalgia | Patterns and predictors of opioid use among migraine patients in emergency departments |

---

## US Market Information

All 10 US authorizations are cancelled. No approved indication text is available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019892 | Hydromorphone Hydrochloride (Rhodes Pharmaceuticals) | Tablet | Not available |
| NDA200403 | Hydromorphone Hydrochloride (Hospira) | Injection, solution | Not available |
| ANDA204278 | Hydromorphone Hydrochloride (Padagis) | Tablet, extended release | Not available |
| ANDA205814 | Hydromorphone Hydrochloride (Aurolife) | Tablet | Not available |
| ANDA212133 | Hydromorphone Hydrochloride (Camber) | Tablet, extended release | Not available |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Contraindications suggested by the knowledge graph (not label text):** liver failure and liver disease, kidney disease, respiratory failure, epilepsy, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), hypothyroidism and myxedema, inflammatory bowel disease and ulcerative colitis, constipation, benign prostatic hyperplasia, hypotensive disorder, sudden cardiac arrest, heart conduction disease, gallbladder disease, substance-related disorder and drug dependence, and butyrylcholinesterase deficiency.
- **Drug interactions:** 100 interactions were found; the first 20 reviewed include several rated Major:
  - Alvimopan
  - Bupropion
  - Morphine
  - Naltrexone
  - Moderate interactions include anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium), loperamide, cimetidine, naloxone, eluxadoline, antiemetics (dolasetron, palonosetron), cannabinoids (dronabinol, nabilone), and bowel-preparation agents.
- **Literature signals:** the headache-related publications highlight dependence, medication-overuse and rebound headache, and neuropsychiatric effects with opioids.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The pharyngitis prediction rests on a high model score only. The three trials study post-tonsillectomy pain, not pharyngitis, and two of them test methadone. Opioids are not recommended for routine pharyngitis pain, and all US licenses are cancelled.
- The headache disorder prediction has direct trial data (L3), but they show hydromorphone is inferior to non-opioid alternatives, and current guidance recommends against routine opioid use for acute migraine. It is best framed as a research question about safety and place in therapy.

**To proceed, the following is needed:**
- Mechanism of action data and FDA package insert warnings and contraindications (blocking gap for safety screening)
- Trials of hydromorphone in pharyngitis itself, not postoperative pain
- A comparison against standard non-opioid analgesics, with a benefit-risk analysis covering respiratory depression, dependence and medication-overuse headache
- Confirmation of the current US regulatory status, since all licenses are listed as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

