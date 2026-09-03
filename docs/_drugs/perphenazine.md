---
layout: default
title: Perphenazine
parent: 僅模型預測 (L5)
nav_order: 1033
evidence_level: L5
indication_count: 10
---

# Perphenazine
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

# Perphenazine: From Antipsychotic Use to Anxiety Disorder

## One-Sentence Summary

> Perphenazine is a phenothiazine antipsychotic; formal original-indication and mechanism-of-action data are not available in this evidence pack (data gap), but literature references confirm its established use in psychotic/schizophrenia-spectrum treatment.
> Although the TxGNN model's top nine ranked predictions (e.g., retinal dystrophy, syndromic myopia, hydranencephaly) score highest by embedding similarity, they carry **no mechanistic rationale and no supporting clinical or literature evidence** — the evidence pack itself flags them as likely embedding noise.
> The only candidate with genuine supporting evidence is **rank 10: Anxiety Disorder**, backed by **2 clinical trials** and **20 publications**, several dating back to historical use of perphenazine (often combined with amitriptyline) for mixed anxiety-depression states.

**Note on prediction selection:** This report focuses on Anxiety Disorder rather than the nominal #1-ranked prediction, because the evidence pack's own `repurposing_rationale` explicitly labels ranks 1–9 as lacking mechanistic plausibility and evidentiary support ("embedding 相似性雜訊"), while Anxiety Disorder is the only candidate that reached decision stage S1 with an evidence level above L5.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap); perphenazine is classified as a phenothiazine antipsychotic, historically used for psychotic disorders and, in combination with amitriptyline, for mixed anxiety-depression |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known pharmacology, perphenazine is a phenothiazine antipsychotic acting as a multi-receptor antagonist (D2/D1, 5-HT2A, α1, H1). At lower doses these combined sedative and serotonergic-antagonist properties have historically produced anxiolytic-like effects, which is why perphenazine was co-formulated with the tricyclic antidepressant amitriptyline (brand names Triavil/Etrafon) for mixed anxiety-depressive states from the 1960s onward.

This mechanistic link is not anxiety-specific — it is better understood as a secondary sedative/tranquilizing effect of a broad-spectrum antipsychotic rather than a targeted anxiolytic mechanism. Notably, the drug's anticholinergic, extrapyramidal, and QT-prolongation liabilities are significant reasons it has never been positioned as a first-line anxiety treatment, and most supporting literature predates modern SSRI/benzodiazepine-based anxiety treatment paradigms.

By contrast, the model's higher-scoring predictions (retinal dystrophy, syndromic myopia, various rare congenital/neurodevelopmental syndromes) have no plausible pharmacological connection to a CNS receptor-antagonist antipsychotic, and the associated literature consists entirely of unrelated ophthalmology/genetics case reports — consistent with the evidence pack's own assessment that these are likely knowledge-graph embedding artifacts rather than genuine repurposing signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Pharmacovigilance study in gerontopsychiatric inpatients monitoring adverse drug reactions under psychopharmacological treatment (not a dedicated anxiety-efficacy trial; terminated early) |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Evaluates combined antioxidant therapy with Adepsique® (amitriptyline + perphenazine + diazepam) on oxidative stress/inflammatory markers in chronic subjective tinnitus — indirect, not anxiety-focused |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4867598](https://pubmed.ncbi.nlm.nih.gov/4867598/) | 1968 | RCT (double-blind) | Psychosomatics | Double-blind study of perphenazine-amitriptyline for psychical disturbances induced by physical disorders, in anxiety and depression |
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Reviews efficacy of typical and atypical antipsychotics for primary and comorbid anxiety symptoms/disorders |
| [27372312](https://pubmed.ncbi.nlm.nih.gov/27372312/) | 2016 | Review | CNS Drugs | Reviews antipsychotic-induced somnolence incidence and mechanisms, relevant to sedative/anxiolytic-adjacent effects |
| [14149372](https://pubmed.ncbi.nlm.nih.gov/14149372/) | 1964 | Review | Psychosomatics | Phenothiazines in the management of stress and anxiety |
| [9435993](https://pubmed.ncbi.nlm.nih.gov/9435993/) | 1997 | Review | Clin Pharmacokinet | Critical review of SSRI and CNS drug (including antipsychotics) pharmacokinetic interactions relevant to anxiety comorbidity management |
| [14249358](https://pubmed.ncbi.nlm.nih.gov/14249358/) | 1964 | Cohort | J Med Assoc Georgia | Combined amitriptyline and perphenazine in combined depression and anxiety |
| [4886995](https://pubmed.ncbi.nlm.nih.gov/4886995/) | 1969 | Cohort | Dis Nerv Syst | Double-blind clinical study of thiothixene vs. perphenazine-amitriptyline in psychotic and psychoneurotic depression |
| [13405719](https://pubmed.ncbi.nlm.nih.gov/13405719/) | 1957 | Cohort | J Am Geriatr Soc | Preliminary report on trilafon (perphenazine) for treatment of anxiety, agitation and excitement in the aged |
| [3736271](https://pubmed.ncbi.nlm.nih.gov/3736271/) | 1986 | Review | Med Clin North Am | Review of psychiatric emergencies, including anxiolytic/antipsychotic use in acute settings |
| [41093133](https://pubmed.ncbi.nlm.nih.gov/41093133/) | 2025 | Mechanistic/Preclinical | Neurochem Int | Modern mechanistic study on psychotropic/antipsychotic drug modulation of platelet activity via the PAF pathway, relevant to anxiety/depression as systemic inflammatory conditions |

---

## US Market Information

Perphenazine is currently **not marketed** in this jurisdiction (`market_status: 未上市`), with **0 registered licenses/NDAs**. No product, dosage form, or approved indication text is available for tabulation.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug-drug interactions) are not available in this evidence pack. This is flagged as a **Blocking** data gap (DG001 — TFDA/label warnings and contraindications), meaning **this candidate cannot yet complete a safety pre-screen (S1)**.

> Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only prediction with any real evidentiary support — Anxiety Disorder — rests on dated (1950s–1970s), low-quality cohort/case-series and open-label data, plus two clinical trials that do not directly test anxiolytic efficacy. Combined with a **Blocking** safety data gap (no TFDA warnings/contraindications available) and the drug's current non-marketed status, there is insufficient basis to advance beyond a research question.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) to complete the S1 safety pre-screen (resolves DG001)
- Confirmed mechanism-of-action data from DrugBank (resolves DG002)
- Contemporary controlled trial evidence specifically evaluating perphenazine (or perphenazine-amitriptyline) in anxiety disorder, using current diagnostic criteria
- Re-evaluation of market status, since the drug is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

