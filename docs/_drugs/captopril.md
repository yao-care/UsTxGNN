---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is a first-generation ACE (angiotensin-converting enzyme) inhibitor long established for treating hypertension, heart failure, and diabetic nephropathy. The TxGNN model predicts potential efficacy for **Malignant Hypertensive Renal Disease**, with **0 registered clinical trials** and **1 case report** directly supporting this direction — though a closely related indication (malignant renovascular hypertension, Rank 2) carries stronger supporting literature (20 publications, evidence level L3).

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Heart Failure, Diabetic Nephropathy (US regulatory records not available in this dataset — known long-established generic) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 |
| US Market Status | Not found in dataset (data gap — Captopril / Capoten® is a long-established FDA-approved generic) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Captopril inhibits the angiotensin-converting enzyme, blocking the conversion of Angiotensin I (Ang I) to Angiotensin II (Ang II). This reduces systemic vascular resistance, suppresses aldosterone secretion, and — critically for renal physiology — dilates the efferent arteriole, lowering intraglomerular hydraulic pressure. This mechanism confers nephroprotective effects that extend well beyond simple blood pressure reduction and explains why Captopril became the cornerstone treatment in diabetic nephropathy trials.

Malignant hypertensive renal disease represents severe end-organ damage driven by RAAS overactivation: elevated Ang II triggers afferent arteriolar hypertrophy, fibrinoid necrosis, and thrombotic microangiopathy in the glomeruli. Captopril's direct blockade of Ang II synthesis is mechanistically the most on-target intervention in this cascade, making the TxGNN high-score prediction (99.28%) biologically coherent. The closely related Rank 2 indication — **malignant renovascular hypertension** — further reinforces this rationale: renovascular hypertension results from renal artery stenosis causing renin hypersecretion and RAAS overactivation, precisely the pathway Captopril was designed to block. Historical clinical literature from 1984–1991 (PMID 6145432, PMID 2040938) documents direct therapeutic use of Captopril in malignant hypertension courses, and the "Captopril test" / "Captopril renogram" are themselves standard diagnostic tools that embody the drug's intimate mechanistic relationship with this disease class.

A critical limitation must be noted: the sole publication retrieved for Rank 1 (PMID 28902735) describes Captopril renography as a **diagnostic imaging procedure** — not a therapeutic intervention. It does not constitute evidence of treatment efficacy in malignant hypertensive renal disease. Additionally, ACE inhibitors carry a known risk of precipitating acute renal failure in patients with bilateral renal artery stenosis, making pre-treatment vascular imaging essential before use in any renovascular indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for Captopril in malignant hypertensive renal disease.

## Literature Evidence

*(Top indication: Malignant Hypertensive Renal Disease)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | Positive captopril renography in a patient with chromophobe renal cell carcinoma (not renal artery stenosis); confirms renin-dependent hypertension can occur without classical renovascular anatomy; hypertension resolved after nephrectomy |

---

*(Rank 2 indication — Malignant Renovascular Hypertension — carries substantially stronger literature support; selected highlights below)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical Observational | Biull Vsesoiuz Kardiol Nauch Tsentra | Direct use of Captopril in both stable and malignant hypertension courses — earliest direct therapeutic evidence |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | Journal of Pediatrics | Malignant hypertension management review including ACE inhibitor therapy |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Experimental/Observational | Japanese Heart Journal | Neurohormonal characterization of benign vs. malignant Goldblatt hypertension phases; RAAS role confirmed |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinol Metab Clin North Am | Renin-secreting tumors; blood pressure drops under ACE inhibitor treatment (converting enzyme treatment) documented |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Renovascular hypertension clinical concepts; ACE inhibitors as first-line intervention with bilateral stenosis caveat |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Observational | Clinical Science | Captopril and SQ 20881 induced plasma renin activity rises >14 ng/h/ml in 43/44 renovascular hypertension patients — key diagnostic and mechanistic validation |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Cohort | Japanese Journal of Medicine | Population-level evaluation of renovascular hypertension tests; captopril test clinical utility confirmed |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | 27 NF1 pediatric patients studied with captopril test and Doppler for secondary hypertension screening |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report | Clinical Nephrology | Renovascular hypertension + neurofibromatosis; captopril stimulation showed PRA rise from 2.8 to 12.6 ng/mL/h confirming renin-dependent mechanism |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | Malignant hypertension with false-positive captopril renal scintigraphy; bilateral equal renovascular pattern without anatomical stenosis |

## US Market Information

No US regulatory license records are available in this Evidence Pack dataset (0 NDAs retrieved). This represents a likely **data gap**: Captopril (brand name Capoten®) received original FDA approval and has been widely available as a generic in the United States. Verification against FDA Drugs@FDA is recommended.

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Clinically critical note directly relevant to predicted indications:** ACE inhibitors including Captopril are contraindicated or require extreme caution in patients with **bilateral renal artery stenosis or stenosis of a solitary functioning kidney**. Use in this setting can precipitate acute renal failure by removing the Ang II-dependent efferent arteriolar tone that maintains glomerular filtration pressure. Given that both top predicted indications (malignant hypertensive renal disease and malignant renovascular hypertension) occur in a renovascular context, pre-treatment imaging to exclude bilateral stenosis is a prerequisite before clinical use.

## Conclusion and Next Steps

**Decision: Research Question** *(Rank 1 — Malignant Hypertensive Renal Disease)*
**Decision: Proceed with Guardrails** *(Rank 2 — Malignant Renovascular Hypertension)*

**Rationale:**

The Rank 1 indication (malignant hypertensive renal disease) has a mechanistically compelling TxGNN prediction (99.28%), but the single retrieved publication documents only diagnostic rather than therapeutic use of Captopril. This places evidence at L4 — mechanism plausibility with insufficient clinical confirmation. The Rank 2 indication (malignant renovascular hypertension) is better supported: historical observational and review literature from 1979–2006 documents direct therapeutic application, and the "Captopril test" / renogram are gold-standard diagnostic tools specifically designed around Captopril's RAAS-blocking mechanism, demonstrating deep drug-disease integration at L3 evidence level.

**To proceed, the following is needed:**

- **Resolve US regulatory data gap:** Pull Captopril NDA records directly from FDA Drugs@FDA to confirm approval history, labeled indications, and any renovascular hypertension language
- **Retrieve full-text MOA:** Query DrugBank API (DB01197) to obtain pharmacodynamics, pharmacokinetics, and toxicity profile
- **Obtain package insert warnings:** Download FDA-approved labeling PDF to extract contraindications (especially bilateral renal artery stenosis warning) and boxed warnings
- **Targeted literature search:** Conduct a systematic PubMed search for *("captopril" OR "ACE inhibitor") AND ("malignant hypertension" OR "hypertensive nephropathy" OR "hypertensive emergency")* with treatment as the focus — not diagnosis
- **Pre-clinical evidence review:** Identify animal model data on ACE inhibitor nephroprotection in malignant hypertension to support a translational path
- **Bilateral stenosis exclusion protocol:** Define mandatory pre-treatment imaging criteria (CT angiography or Doppler ultrasound) before any clinical use in renovascular indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

