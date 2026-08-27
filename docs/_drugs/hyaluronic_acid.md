---
layout: default
title: Hyaluronic Acid
parent: 僅模型預測 (L5)
nav_order: 774
evidence_level: L5
indication_count: 10
---

# Hyaluronic Acid
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

# Hyaluronic Acid: From Unspecified Original Indication to Dry Eye Syndrome

## One-Sentence Summary

Hyaluronic Acid (DrugBank DB08818) has no original indication or NDA license on file in this evidence pack, and is currently **not marketed** as an approved product in the reviewed market.
The TxGNN model predicts it may be effective for **Dry Eye Syndrome**, with **50 clinical trials** and **20 publications** identified in the evidence pack supporting this direction — including two completed Phase 3 RCTs.
Because formal labeling, warnings, and mechanism-of-action data are missing, this candidate has strong efficacy evidence but an incomplete safety dossier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no licenses or original_indications recorded) |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (data gap DG002). Based on the literature captured in this evidence pack, hyaluronic acid is a naturally occurring glycosaminoglycan widely used across ophthalmology, rheumatology, and dermatology because of its water-retention and lubricating properties (PMID 32070808). A dedicated review (PMID 35514082, *Acta Ophthalmologica*, 2022) specifically evaluates HA-containing artificial tears as a treatment for dry eye disease, and a related comparative review (PMID 37042308) uses HA as the reference comparator for other dry-eye active ingredients — indicating HA is already a well-established benchmark therapy for this exact condition.

This raises an important caveat for interpretation: HA eye drops (sodium hyaluronate) are already a standard, widely marketed treatment for dry eye disease in many jurisdictions. The TxGNN prediction here is therefore less a discovery of a *novel* indication and more a confirmation of an established pharmacological use — which is consistent with the very high volume of supporting clinical trial and literature evidence found. The core open question for this specific product/entity is not whether HA works for dry eye (it clearly does, per the evidence below), but whether **this particular DrugBank entity/product** has the regulatory dossier (labeling, warnings, MOA documentation) needed to support a formal submission — which it currently lacks (DG001, DG002).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01382225](https://clinicaltrials.gov/study/NCT01382225) | Phase 3 | Completed | 1936 | Sodium Hyaluronate Ophthalmic Solution 0.18% evaluated for efficacy in signs and symptoms of dry eye disease |
| [NCT01240382](https://clinicaltrials.gov/study/NCT01240382) | Phase 3 | Completed | 332 | 3% DE-089 vs 0.1% sodium hyaluronate; non-inferiority on fluorescein staining, superiority on Rose Bengal score |
| [NCT02777723](https://clinicaltrials.gov/study/NCT02777723) | Phase 3 | Unknown | 138 | CKD-350 eye drops vs comparator for efficacy/safety in dry eye syndrome |
| [NCT06517667](https://clinicaltrials.gov/study/NCT06517667) | Phase 2/3 | Completed | 30 | Randomized single-blind comparison of different hyaluronic acid tear substitute formulations in evaporative dry eye |
| [NCT04704531](https://clinicaltrials.gov/study/NCT04704531) | Phase 2 | Completed | 141 | Three dosing schemes of Sodium Hyaluronate 0.4% (Lagricel Ofteno) evaluated via OSDI in mild-to-moderate dry eye |
| [NCT00938704](https://clinicaltrials.gov/study/NCT00938704) | Phase 4 | Completed | 71 | Non-preserved carboxymethylcellulose/glycerin vs sodium hyaluronate 0.18% for dry eye signs and symptoms |
| [NCT03888183](https://clinicaltrials.gov/study/NCT03888183) | Phase 4 | Unknown | 334 | Randomized, double-blind trial of preservative-free low-dose HA-containing salt solution for dry eye disease |
| [NCT06860659](https://clinicaltrials.gov/study/NCT06860659) | Phase 4 | Enrolling by invitation | 84 | Randomized double-blind trial of 0.28% vs 0.18% preservative-free sodium hyaluronate in moderate-severe dry eye |
| [NCT02510235](https://clinicaltrials.gov/study/NCT02510235) | NA | Completed | 56 | Multicenter non-inferiority trial: Lubricin 150 µg/mL vs 0.13% sodium hyaluronate eye drops |
| [NCT03074344](https://clinicaltrials.gov/study/NCT03074344) | NA | Completed | 40 | Cross-linked hyaluronic acid + coenzyme Q10 eye drops in mild-to-moderate dry eye |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | Non-inferiority RCT of laughter exercise vs 0.1% sodium hyaluronic acid for ocular surface discomfort in dry eye disease |
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | Meta-Analysis | Int J Environ Res Public Health | Compares efficacy of HA- vs non-HA-based eye drops (saline, conventional artificial tears) across 8 databases |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | Systematic Review/Meta-Analysis | Int J Ophthalmol | Compares high vs low concentration HA eye drops for dry eye syndrome |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmologica | Critical evaluation of safety and efficacy literature for HA-containing artificial tears in DED |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Review | Acta Ophthalmologica | Summarizes all single active ingredients directly compared with HA in DED treatment |
| [34843023](https://pubmed.ncbi.nlm.nih.gov/34843023/) | 2022 | Randomized Multicenter Clinical Evaluation | Jpn J Ophthalmol | Sequential application of 0.3% and 0.15% unpreserved HA for dry eye treatment |
| [32070808](https://pubmed.ncbi.nlm.nih.gov/32070808/) | 2020 | Review | Carbohydrate Research | HA applications in ophthalmology (dry eye), rheumatology, and dermatology; describes water-retention/lubricant mechanism |
| [33923222](https://pubmed.ncbi.nlm.nih.gov/33923222/) | 2021 | Review | Molecules | Applications of HA in ophthalmology and contact lenses, including dry eye treatment |
| [27324942](https://pubmed.ncbi.nlm.nih.gov/27324942/) | 2016 | Systematic Review | J Cosmetic Dermatology | Physiochemical properties and cross-specialty medical applications of hyaluronic acid |
| [30510396](https://pubmed.ncbi.nlm.nih.gov/30510396/) | 2018 | Clinical Study | Clinical Ophthalmology (Auckland) | Safety and efficacy of a cross-linked HA gel occlusive device for dry eye syndrome |

---

## US Market Information

No NDA/marketing authorization is on file for this product in the evidence pack (`total_licenses: 0`, market status: Not Marketed). No product/dosage-form/indication data is currently available to populate this table.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/labeling warnings and contraindications data are flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be remediated before an initial safety (S1) assessment can be performed. A drug-drug interaction query also returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for hyaluronic acid in dry eye syndrome is strong (L1: two completed Phase 3 RCTs, one with nearly 2,000 subjects, plus extensive supporting literature), but the Blocking-severity gap in labeling/warnings data (DG001) means this candidate cannot yet clear an initial safety screen, and the product currently has no US market presence (0 NDAs).

**To proceed, the following is needed:**
- Official labeling/warnings and contraindications data (DG001 — download and parse TFDA/FDA label PDF)
- Mechanism of action documentation via DrugBank API (DG002)
- Confirmation of a marketed formulation/route (ophthalmic) suitable for the dry eye indication
- A completed drug-drug interaction review (current status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

