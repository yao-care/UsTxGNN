---
layout: default
title: Pembrolizumab
parent: Model Prediction Only (L5)
nav_order: 1024
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pembrolizumab: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab (Keytruda) is a PD-1 immune checkpoint inhibitor, originally used to treat non-small cell lung cancer, lung cancer and metastatic melanoma.
The TxGNN model's top-ranked prediction is **gingival fibromatosis**, but there are **0 clinical trials** and **0 publications** supporting it, so this is a model prediction only.
Among the other nine predictions, only "lung germ cell tumor" has any (indirect) supporting material, with 40 retrieved trials and 20 publications. The trials are generic solid-tumor studies and none is shown to enroll this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer, lung cancer, metastatic melanoma (from the knowledge graph; the US license record has no indication text) |
| Predicted New Indication | Gingival fibromatosis |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single BLA record is marked cancelled) |
| Number of NDAs | 1 (BLA125514) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pembrolizumab is a monoclonal antibody that targets programmed cell death protein 1 (PD-1, CD279). By blocking PD-1, it releases the "brake" on T cells so the immune system can attack tumours. Its efficacy in lung cancer and melanoma is well established.

For gingival fibromatosis, however, no mechanistic link has been established. It is a non-malignant fibrotic condition, and PD-1 blockade has no known rationale in it. The high TxGNN score (0.994) appears to be a knowledge-graph artifact rather than a biologically grounded signal. Note that scores across the top ten predictions are all about 99.3–99.4%, so the score does little to distinguish between candidates.

Other predicted indications fall into three groups:
- **Benign or rare genetic conditions** (inclusion body myopathy with Paget disease, hamartoma of lung, fibroma of lung, lung benign neoplasm, ovarioleukodystrophy, and a rare leukomelanoderma syndrome): no PD-1 rationale. Immune checkpoint inhibitors can themselves cause myopathy and neurologic toxicity, which is a safety concern for some of these.
- **Lung cancer variants** (lung hilum carcinoma, pulmonary sulcus neoplasm): these largely fall under the already-approved NSCLC use, so they are not true repurposing.
- **Lung germ cell tumor**: PD-1 blockade is mechanistically plausible, but there is no disease-specific evidence.

---

## Clinical Trial Evidence

The top-ranked prediction (gingival fibromatosis) has no registered clinical trials. Currently no related clinical trials are registered for it.

For reference, the only predicted indication with retrieved trials is rank 9, **lung germ cell tumor**. These trials were matched by keyword and none is shown to enroll this disease. Representative examples:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02402920](https://clinicaltrials.gov/study/NCT02402920) | Phase 1 | Completed | 83 | Pembrolizumab with chemoradiation in small cell lung cancer; lung-cancer safety data |
| [NCT02628067](https://clinicaltrials.gov/study/NCT02628067) | Phase 2 | Active, not recruiting | 1609 | KEYNOTE-158: pembrolizumab biomarker study in multiple advanced solid tumors |
| [NCT03511391](https://clinicaltrials.gov/study/NCT03511391) | Phase 2 | Completed | 99 | CHEERS: stereotactic radiotherapy added to checkpoint inhibitors in NSCLC, urothelial, renal, melanoma and head-and-neck cancers |
| [NCT04222972](https://clinicaltrials.gov/study/NCT04222972) | Phase 3 | Terminated | 223 | Pralsetinib vs standard of care in RET-fusion NSCLC; pembrolizumab is not the investigational agent |
| [NCT03901378](https://clinicaltrials.gov/study/NCT03901378) | Phase 2 | Withdrawn | 0 | Pembrolizumab plus platinum/etoposide in neuroendocrine carcinoma; no patients enrolled |
| [NCT05708950](https://clinicaltrials.gov/study/NCT05708950) | Phase 1/2 | Completed | 40 | KVA12123 alone or with pembrolizumab in advanced solid tumors; dose escalation only |
| [NCT07160335](https://clinicaltrials.gov/study/NCT07160335) | Phase 1 | Active, not recruiting | 174 | HLX17 vs Keytruda (biosimilar comparison) in resected NSCLC, melanoma or RCC |

---

## Literature Evidence

The top-ranked prediction has no retrieved publications. Currently no related literature is available for gingival fibromatosis.

For reference, the literature retrieved for other predictions is about the approved cancer uses, not the predicted diseases:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29658856](https://pubmed.ncbi.nlm.nih.gov/29658856/) | 2018 | RCT | N Engl J Med | Pembrolizumab plus chemotherapy in metastatic NSCLC (approved indication; listed under "lung benign neoplasm") |
| [30620668](https://pubmed.ncbi.nlm.nih.gov/30620668/) | 2019 | RCT | J Clin Oncol | KEYNOTE-024 updated analysis: pembrolizumab vs chemotherapy in PD-L1 ≥50% NSCLC |
| [26712084](https://pubmed.ncbi.nlm.nih.gov/26712084/) | 2016 | RCT | Lancet | KEYNOTE-010: pembrolizumab vs docetaxel in previously treated PD-L1-positive NSCLC |
| [32468956](https://pubmed.ncbi.nlm.nih.gov/32468956/) | 2020 | RCT | J Clin Oncol | KEYNOTE-604: pembrolizumab plus etoposide/platinum in extensive-stage small-cell lung cancer |
| [40157574](https://pubmed.ncbi.nlm.nih.gov/40157574/) | 2025 | RCT | Ann Oncol | Phase 3 subcutaneous vs intravenous pembrolizumab plus chemotherapy in metastatic NSCLC |
| [35658002](https://pubmed.ncbi.nlm.nih.gov/35658002/) | 2022 | RCT | J Clin Oncol | Lung-MAP S1800A: ramucirumab plus pembrolizumab in NSCLC previously treated with immunotherapy |
| [34895095](https://pubmed.ncbi.nlm.nih.gov/34895095/) | 2022 | Meta-analysis | J Chemother | Pembrolizumab improved PFS, OS and ORR vs chemotherapy in advanced NSCLC |
| [30920617](https://pubmed.ncbi.nlm.nih.gov/30920617/) | 2019 | Case report | Jpn J Clin Oncol | Hyperprogression after pembrolizumab in two urothelial carcinoma patients |

These support pembrolizumab's established use in malignant lung cancer. They are indirect for the benign neoplasms and other predicted diseases.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125514 | KEYTRUDA (Merck Sharp & Dohme LLC) | Injection, solution | Not available in the data compiled; status: cancelled |

The only US license record is marked cancelled, and no indication text was captured. This should be verified against the current FDA label, since pembrolizumab is widely marketed in practice.

---

## Safety Considerations

- **Drug Interactions** (13 records found):
  - **Major**: lenalidomide, pomalidomide, thalidomide.
  - **Moderate**: systemic corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, deflazacort).
  - **Target**: PD-1 (PDCD1) is the pharmacological target of pembrolizumab.
- **Class-related concerns from the retrieved literature**: immune-related adverse events such as endocrinopathies (hypothyroidism, hypoadrenocorticism), neurologic complications, myocarditis/myositis/myasthenia overlap, and hyperprogression in some patients. Immune checkpoint inhibitors may also worsen pre-existing immune-mediated disease (e.g., multiple sclerosis). These are particularly relevant for the predicted neuromuscular and neurologic genetic conditions.

Package insert warnings and contraindications were not available in the data compiled, so please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, gingival fibromatosis, rests on a model score alone, with no trials, no literature and no mechanistic rationale for PD-1 blockade in a benign fibrotic condition. Other high-ranking predictions are either benign or rare genetic diseases with no rationale, or lung cancers already covered by existing use. Lung germ cell tumor (L3, "Research Question") is the only one worth a follow-up, and only as a research question.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Disease-specific preclinical or clinical evidence for any predicted indication, particularly lung germ cell tumor
- A risk-benefit review of immune-related toxicity for non-malignant or neuromuscular conditions
- Confirmation of current US licensing status, since the only record is marked cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

