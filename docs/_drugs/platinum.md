---
layout: default
title: Platinum
parent: Model Prediction Only (L5)
nav_order: 1053
evidence_level: L5
indication_count: 10
monitor_inn: "PLATINUM"
predicted_indications: ["urinary bladder carcinoma", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder signet ring cell adenocarcinoma", "bladder colonic type adenocarcinoma", "bladder colloid adenocarcinoma", "bladder mixed adenocarcinoma", "bladder clear cell adenocarcinoma", "urinary bladder neoplasm"]
last_modified_at: 2026-10-14
description: "Platinum: predicted new indication Urinary bladder carcinoma (evidence level L5). Approved use: Not available"
---

# Platinum
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

## Platinum: From an Unspecified Original Indication to Urinary Bladder Carcinoma
{: .text-alpha }

## One-Sentence Summary

Platinum (DrugBank DB12257) is a generic or elemental entry. Its only US record is a cancelled homeopathic pellet product, and no approved indication is on file.
The TxGNN model predicts it may be effective for **Urinary Bladder Carcinoma**, with **5 clinical trials** and **20 publications** currently supporting this direction.
The evidence mostly reflects platinum-class drugs (cisplatin, carboplatin) rather than this specific entry, so it should be read with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only US license has no approved indication text) |
| Predicted New Indication | Urinary bladder carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L1 (as assigned in the data compiled for this report; see note below) |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note: the L1 rating rests on platinum-class evidence, including a Phase 3 trial that is still recruiting. By the strict rule (at least 2 completed Phase 3 RCTs), the trial data for this entry alone would not reach L1. Only one completed randomised Phase 2 trial is listed, and its platinum backbone is present in both arms. Treat L1 as applying to the platinum class, not to this entry.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this entry. Based on known pharmacology, platinum agents such as cisplatin and carboplatin form DNA intrastrand and interstrand crosslinks. These block replication and transcription and trigger apoptosis in rapidly dividing tumour cells.

Platinum-based chemotherapy is already a guideline-endorsed backbone for urothelial carcinoma (ESMO and EAU guidelines). The Phase 3 POUT trial supports adjuvant platinum use in upper tract disease. Response is modulated by DNA damage response and repair status, as well as by TP53 and APOBEC-related biology.

The DrugBank entry "PLATINUM" is a placeholder with no meaningful market status. The supporting evidence therefore applies to platinum-class drugs, not to this specific entry.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02567409](https://clinicaltrials.gov/study/NCT02567409) | Phase 2 | Completed | 87 | Cisplatin/gemcitabine with or without berzosertib in metastatic urothelial cancer. Cisplatin is in both arms, so the platinum effect is not isolated. |
| [NCT07097142](https://clinicaltrials.gov/study/NCT07097142) | Phase 3 | Recruiting | 486 | ARCHER: adaptive radiation plus standard chemotherapy (cisplatin, gemcitabine, or mitomycin and 5-FU) in muscle-invasive bladder cancer. No results yet. |
| [NCT06820255](https://clinicaltrials.gov/study/NCT06820255) | Phase 4 | Recruiting | 135 | Tests whether DNA repair gene alterations predict response to platinum chemotherapy in advanced urothelial cancer. |
| [NCT04909775](https://clinicaltrials.gov/study/NCT04909775) | Phase 2 | Unknown | 40 | Cisplatin/gemcitabine plus tislelizumab as bladder-sparing treatment in muscle-invasive disease. Small single-centre study. |
| [NCT06770582](https://clinicaltrials.gov/study/NCT06770582) | Phase 2 | Recruiting | 160 | PARRC: pembrolizumab plus radiation versus radiation plus concurrent chemotherapy in high-grade T1 bladder cancer. Platinum is the comparator. |
| [NCT03582475](https://clinicaltrials.gov/study/NCT03582475) | Phase 1 | Active, not recruiting | 15 | Pembrolizumab with platinum chemotherapy in small cell/neuroendocrine cancers of the urothelium and prostate. Rare variant, small sample. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32145825](https://pubmed.ncbi.nlm.nih.gov/32145825/) | 2020 | RCT (Phase 3) | Lancet | POUT trial: adjuvant platinum-based chemotherapy in upper tract urothelial carcinoma. |
| [34051178](https://pubmed.ncbi.nlm.nih.gov/34051178/) | 2021 | RCT (Phase 3) | Lancet Oncol | KEYNOTE-361: pembrolizumab alone or with chemotherapy versus chemotherapy as first-line therapy in advanced urothelial carcinoma. |
| [37071838](https://pubmed.ncbi.nlm.nih.gov/37071838/) | 2023 | RCT (Phase 3) | J Clin Oncol | JAVELIN Bladder 100: avelumab maintenance after first-line platinum chemotherapy, with 2 or more years of follow-up. |
| [15939524](https://pubmed.ncbi.nlm.nih.gov/15939524/) | 2005 | Meta-analysis | Eur Urol | Individual patient data meta-analysis of neoadjuvant chemotherapy in invasive bladder cancer. |
| [34861372](https://pubmed.ncbi.nlm.nih.gov/34861372/) | 2022 | Guideline | Ann Oncol | ESMO clinical practice guideline for bladder cancer. |
| [36967359](https://pubmed.ncbi.nlm.nih.gov/36967359/) | 2023 | Guideline | Eur Urol | EAU guidelines on upper urinary tract urothelial carcinoma, 2023 update. |
| [32767764](https://pubmed.ncbi.nlm.nih.gov/32767764/) | 2020 | Review | CA Cancer J Clin | Platinum-based chemotherapy has been the mainstay of systemic treatment for muscle-invasive and advanced bladder cancer for over 4 decades. |
| [38702396](https://pubmed.ncbi.nlm.nih.gov/38702396/) | 2024 | Review | Nat Rev Urol | Cisplatin-based chemotherapy is first-line standard care in metastatic urothelial cancer, but up to 50% of patients are cisplatin-ineligible. |
| [40829180](https://pubmed.ncbi.nlm.nih.gov/40829180/) | 2025 | Biomarker study | J Clin Invest | ERCC2 mutations (about 10% of bladder tumours) may predict cisplatin sensitivity. |
| [38535994](https://pubmed.ncbi.nlm.nih.gov/38535994/) | 2024 | Preclinical | Cancer Res | NPEPPS is a druggable driver of platinum resistance. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available (cancelled) | Platinum Metallicum (Hahnemann Laboratories, Inc.) | Pellet | Not stated |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class, DNA-crosslinking agents) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Platinum-class antineoplastics generally require handling under cytotoxic drug regulations. Please refer to the package insert. |

---

## Safety Considerations

No drug-interaction records were found for this entry. Please refer to the package insert for safety information.

---

## Other Predicted Indications (Brief)

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Infiltrating bladder urothelial carcinoma | 99.22% | L2 | Proceed with Guardrails |
| Non-invasive bladder urothelial carcinoma | 99.22% | L3 | Research Question |
| Urinary bladder neoplasm (broad category) | 99.13% | L1 | Proceed with Guardrails |
| Bladder urachal urothelial carcinoma | 99.19% | L4 | Hold |
| Bladder mixed or clear cell adenocarcinoma | 99.18% | L4 | Hold |
| Bladder signet ring cell, colonic type, and colloid adenocarcinoma | 99.18% | L5 | Hold |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Platinum-based chemotherapy is guideline-endorsed standard care in urothelial carcinoma, supported by Phase 3 and meta-analysis evidence. That evidence belongs to platinum-class drugs such as cisplatin and carboplatin, not to this placeholder entry. The only Phase 3 bladder trial directly relevant here (ARCHER) is still recruiting and has no results.

**To proceed, the following is needed:**
- Decide which specific platinum agent (cisplatin or carboplatin) is the actual repurposing candidate, and re-anchor the evidence and regulatory review on it.
- Obtain the package insert, including warnings and contraindications. This gap currently blocks safety screening.
- Obtain mechanism of action data from DrugBank.
- Define patient selection, for example cisplatin eligibility and DNA repair gene biomarkers such as ERCC2.
- Review results from ARCHER and the Phase 4 DNA repair biomarker study as they become available.
- Treat the non-invasive and rare adenocarcinoma histologies as research questions or on hold until direct evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

