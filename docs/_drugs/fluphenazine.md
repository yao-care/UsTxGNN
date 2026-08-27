---
layout: default
title: Fluphenazine
parent: 僅模型預測 (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
---

# Fluphenazine
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

# Fluphenazine: From Psychotic Disorders to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Fluphenazine is a first-generation (typical) phenothiazine antipsychotic and potent D2 receptor antagonist, historically used to treat psychotic disorders such as schizophrenia. The TxGNN model predicts a high association with **Retinal Dystrophy with or without Extraocular Anomalies**, but this pairing is supported by **0 clinical trials** and **15 publications**, none of which discuss fluphenazine in relation to this disease — the literature instead reflects general ophthalmology topics that co-occur by keyword rather than by mechanism. Detailed mechanism-of-action data and TFDA label information are currently unavailable (data gaps DG001, DG002), and the evidence pack itself flags this candidate as likely a false-positive/keyword-noise signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack; fluphenazine is pharmacologically known as a typical antipsychotic (per mechanistic notes elsewhere in this pack) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.99% (rank 321) |
| Evidence Level | L5 |
| US Market Status | Not Marketed (no license records on file) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, fluphenazine is a typical phenothiazine antipsychotic and strong D2 dopamine receptor antagonist, used clinically for psychotic disorders. There is no established or plausible mechanistic pathway connecting D2 receptor antagonism to retinal dystrophy with or without extraocular anomalies, which is a congenital/genetic ophthalmic condition.

Notably, phenothiazine-class drugs — particularly chlorpromazine and thioridazine — carry a well-documented **adverse effect** risk of pigmentary retinopathy at high doses. This is a toxicity signal, not a therapeutic mechanism, and it raises the possibility that the TxGNN model may have picked up a drug-disease association driven by an adverse-effect relationship rather than a genuine treatment opportunity.

The accompanying 15 literature citations further weaken the case: their titles and abstracts cover unrelated general ophthalmology topics (orbital infections, diplopia, congenital lens/ptosis anomalies, cryptophthalmia, extraocular muscle fibrosis syndromes) with no direct mention of fluphenazine. This pattern is consistent with literature co-occurrence noise rather than substantive evidence, and should be treated as a low-confidence, model-only signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review (unrelated) | Seminars in Ultrasound, CT, and MR | Overview of orbital infections/cellulitis; no mention of fluphenazine or retinal dystrophy — likely co-occurrence noise |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review (unrelated) | Seminars in Neurology | Diagnostic approach to diplopia; unrelated to fluphenazine |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review (unrelated) | Pediatric Radiology | Pediatric orbital lesion imaging differential; unrelated to fluphenazine |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review (unrelated) | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies overview; unrelated to fluphenazine |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review (unrelated) | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis clinical features; unrelated to fluphenazine |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report (unrelated) | American Journal of Ophthalmology | Unilateral cryptophthalmia case series; unrelated to fluphenazine |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review (unrelated) | Documenta Ophthalmologica | Wagner-Stickler syndrome vitreoretinal degeneration; unrelated to fluphenazine |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Case Series (unrelated) | International Journal of Molecular Sciences | Optic nerve/retinal abnormalities in congenital extraocular muscle fibrosis (CFEOM); unrelated to fluphenazine |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review (unrelated) | Journal of Binocular Vision and Ocular Motility | Ophthalmoplegia and congenital cranial dysinnervation disorders overview; unrelated to fluphenazine |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review (unrelated) | American Journal of Ophthalmology | Maculopathy pathogenesis with cavitary optic disc anomalies; unrelated to fluphenazine |

---

## US Market Information

Currently no US market license records on file for fluphenazine in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic, clinical, or literature-based support connecting fluphenazine's D2-antagonist pharmacology to retinal dystrophy with or without extraocular anomalies — a congenital genetic eye disorder. The 15 associated publications are topically unrelated to fluphenazine, and the only biologically plausible phenothiazine-retina link found in the class (retinopathy as an adverse effect) argues against, rather than for, a therapeutic role. This candidate should be treated as a low-confidence model artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — currently blocking safety assessment (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank (DG002)
- If pursued further, independent mechanistic or preclinical rationale specifically linking phenothiazines to retinal dystrophy, beyond keyword co-occurrence

**Note:** Rank 10 in this evidence pack (manic bipolar affective disorder) shows a substantially stronger signal — established D2-antagonist mechanistic rationale, drug-class-level clinical review evidence, and 20 literature hits including fluphenazine-specific case reports — and may warrant a separate evaluation report rather than being folded into this one.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

