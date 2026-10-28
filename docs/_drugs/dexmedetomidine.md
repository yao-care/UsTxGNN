---
layout: default
title: Dexmedetomidine
parent: Model Prediction Only (L5)
nav_order: 594
evidence_level: L5
indication_count: 5
monitor_inn: "DEXMEDETOMIDINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia"]
last_modified_at: 2026-10-14
description: "Dexmedetomidine: predicted new indication nephrogenic syndrome of inappropriate antidiuresis . The top-ranked prediction by score is nephrogenic… (evidence level L5). Approved use: Not available in the data compiled for this report …"
---

# Dexmedetomidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dexmedetomidine: From Sedation (Approved Indication Not Listed) to Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Dexmedetomidine is an alpha-2 adrenergic agonist, supplied in the US as an injectable product. The data compiled for this report do not include approved indication text.
The TxGNN model predicts it may be effective for **Headache Disorder** (the best-supported of five predictions), with **4 clinical trials** and **7 publications** currently supporting this direction. The evidence is mostly limited to post-dural puncture headache (PDPH), a secondary headache.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the label text is empty) |
| Predicted New Indication | Headache disorder (best-supported prediction). The top-ranked prediction by score is nephrogenic syndrome of inappropriate antidiuresis. |
| TxGNN Prediction Score | 0.9930 for headache disorder (0.9960 for nephrogenic syndrome of inappropriate antidiuresis, which has no supporting evidence) |
| Evidence Level | L5 (headache disorder). Other predictions are L5, except migraine disorder, which is L5 with one ongoing trial. |
| US Market Status | Marketed (valid licenses on record: at least 13) |
| Number of NDAs | 13 (2 NDAs and 11 ANDAs) |
| Recommended Decision | Hold (a focused research question on PDPH is reasonable) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Dexmedetomidine is known to be a highly selective alpha-2 adrenergic agonist with sedative, analgesic and sympatholytic effects. It is approved for ICU and procedural sedation in adults, according to the trial descriptions.

For headache, the proposed rationale is that alpha-2 agonism modulates nociception and sympathetic tone. It may also reduce cerebral blood flow through cerebrovascular vasoconstriction. Nebulized or intranasal delivery allows mucosal absorption. This is plausible for PDPH, where the trials focus. It also fits migraine, where dampened noradrenergic and trigeminovascular signalling and reduced central sensitization are plausible.

The rationale does not extend equally to all predictions:
- **Nephrogenic SIAD:** The disease is caused by gain-of-function mutations in the vasopressin V2 receptor, which act downstream of vasopressin release. Alpha-2 agonism is unlikely to correct this receptor-level defect. The high score of 0.9960 is a model prediction only.
- **Migraine with brainstem aura and trigeminal autonomic cephalalgia:** Any rationale is extrapolated from general migraine or trigeminal pathophysiology and is speculative. No trials or literature exist.
- **Headache disorder:** The evidence applies to PDPH only, not to primary headache disorders.

---

## Clinical Trial Evidence

Trials for headache disorder (the best-supported prediction):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Double-blind RCT comparing nebulized dexmedetomidine, neostigmine/atropine and saline placebo for PDPH after cesarean section |
| [NCT04327726](https://clinicaltrials.gov/study/NCT04327726) | NA | Completed | 43 | Randomized controlled study of nebulized dexmedetomidine for PDPH in parturients under spinal anesthesia |
| [NCT06470854](https://clinicaltrials.gov/study/NCT06470854) | NA | Completed | 50 | Case-control study of nebulized dexmedetomidine versus bilateral greater occipital nerve block for PDPH |
| [NCT03513757](https://clinicaltrials.gov/study/NCT03513757) | Phase 4 | Completed | 40 | Propofol infusion versus bolus dexmedetomidine plus propofol for pediatric MRI sedation. Headache is at most a peripheral outcome, so relevance is indirect. |

Trial for migraine disorder (second-ranked prediction):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07769255](https://clinicaltrials.gov/study/NCT07769255) | NA | Recruiting | 146 | Randomized trial of nebulized dexmedetomidine on central sensitization and chronification in migraine, using CGRP and trigeminal neurophysiological biomarkers. No results yet. |

No clinical trials are registered for nephrogenic SIAD, migraine with brainstem aura, or trigeminal autonomic cephalalgia.

---

## Literature Evidence

Literature for headache disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41120897](https://pubmed.ncbi.nlm.nih.gov/41120897/) | 2025 | Systematic Review | BMC Anesthesiology | Meta-analysis of the efficacy and safety of nebulized dexmedetomidine for PDPH after cesarean delivery |
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT | Minerva Anestesiologica | Double-blind RCT of nebulized dexmedetomidine versus neostigmine/atropine for PDPH after cesarean section |
| [33993346](https://pubmed.ncbi.nlm.nih.gov/33993346/) | 2021 | RCT | Journal of Anesthesia | Randomized study of adding dexmedetomidine to conservative PDPH management, with cerebral hemodynamics assessed by transcranial Doppler |
| [31345663](https://pubmed.ncbi.nlm.nih.gov/31345663/) | 2019 | Editorial/Commentary | International Journal of Obstetric Anesthesia | Commentary asking whether dexmedetomidine nebulization is an answer to PDPH |
| [39799300](https://pubmed.ncbi.nlm.nih.gov/39799300/) | 2025 | Case Report | BMC Anesthesiology | Two case reports of nebulized dexmedetomidine for obstetric PDPH, including refractory cases that might otherwise need an epidural blood patch |

Two further retrieved items are only tangentially related (an ADHD drug overdose review, PMID 23757186, and a posterior reversible encephalopathy syndrome case report, PMID 41700262) and are not counted as supporting evidence.

No literature is available for the other four predicted indications.

---

## US Market Information

All 13 listings are cancelled, and none has approved indication text in the compiled data. The five main listings are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021038 | Precedex (Hospira, Inc.) | Injection, solution | Not available (valid) |
| NDA206628 | Dexmedetomidine in Dextrose (WG Critical Care, LLC) | Injection | Not available (valid) |
| ANDA201072 | Dexmedetomidine Hydrochloride (Fresenius Kabi USA, LLC) | Injection, solution | Not available (valid) |
| ANDA208532 | Dexmedetomidine HCl in 0.9% Sodium Chloride (Baxter Healthcare Company) | Injection | Not available (valid) |
| ANDA209065 | Dexmedetomidine (Avenacy Inc.) | Injection, solution, concentrate | Not available (valid) |

All products are injectables (injection, injection solution, and injection solution concentrate). The nebulized route used in the headache trials is not an approved route in the compiled data.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertensive disorder, hypertension, kidney disease, pyoureter, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, and atrioventricular block. These come from drug-disease contraindication edges in the TxGNN knowledge graph and need confirmation against the label.
- **Drug interactions:** 59 interactions were found. Those with moderate severity include:
  - Opioids and related agents: morphine (including liposomal), opium, diphenoxylate
  - Cannabinoids: dronabinol, nabilone
  - Vasoactive agents: papaverine, amyl nitrite, diazoxide, phentolamine
  - Others: sibutramine, ethanol

  Interactions with unknown severity include pantoprazole, lansoprazole, vancomycin, atropine, amphotericin B, potassium chloride, famotidine, and ursodeoxycholic acid.

Please refer to the package insert for key warnings and formal contraindications, because these were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest signal is for PDPH, a secondary headache: one completed Phase 3 trial (n=90), two completed RCT-type studies, and a 2025 meta-analysis. The trials are small, mostly single-center, mostly labeled NA, and the Phase 3 trial used an active comparator, so evidence is rated L2. Migraine has only one ongoing trial without results. The highest-scoring prediction, nephrogenic SIAD, has no evidence and a mechanism that conflicts with its cause. All US listings are cancelled, and the label safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap), and the approved indications
- Mechanism of action data from DrugBank
- A larger multicenter, placebo-controlled trial of nebulized dexmedetomidine in PDPH, with route and formulation suitability confirmed because current products are injectables
- Results from the ongoing migraine trial (NCT07769255) before considering migraine
- Review of the knowledge-graph contraindication signals (hypotension, atrioventricular block, liver and kidney disease) against the label for the target populations, such as parturients
- No further investment in nephrogenic SIAD, migraine with brainstem aura, or trigeminal autonomic cephalalgia unless new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

