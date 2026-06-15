---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 482
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabergoline: From Prolactinoma to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a dopamine D2 receptor agonist, clinically established as the first-line medical treatment for prolactin-secreting pituitary adenomas (prolactinomas) and hyperprolactinemia.
The TxGNN model predicts it may have activity against **Pituitary Adenocarcinoma** (TxGNN score 99.06%), a rare and aggressive malignancy sharing pituitary cell origins with the established indication.
However, supporting evidence is limited to **0 clinical trials** and **3 peripherally related case reports**, none of which directly evaluates cabergoline as a treatment for pituitary adenocarcinoma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prolactinoma / Hyperprolactinemia (standard global clinical use; no NDA found in current dataset) |
| Predicted New Indication | Pituitary Adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed (0 NDAs in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established clinical pharmacology, cabergoline acts as a potent, long-acting dopamine D2 receptor (DRD2) agonist. It directly targets pituitary lactotroph cells, suppressing prolactin secretion, inhibiting cAMP signaling, promoting apoptosis, and inducing tumor shrinkage. For prolactinoma, this constitutes first-line therapy with decades of Phase 3 RCT-level evidence globally.

Pituitary adenocarcinoma is an extremely rare and aggressive entity — comprising less than 0.5% of all pituitary tumors — distinguished from benign adenoma by its metastatic potential and markedly worse prognosis. Because both conditions arise from the same pituitary adenohypophyseal cell lineage, the D2-receptor antiproliferative pathway active in prolactinoma theoretically remains relevant in the malignant setting. In related work on non-functioning pituitary adenomas (NFPAs), a systematic review and meta-analysis (PMID 35902444) supports partial tumor control in some patients, and a 2024 translational study (PMID 38989697) identifies HTR2B as a sensitizing target for cabergoline in NFPAs — suggesting cabergoline's applicability may extend beyond prolactinoma.

However, pituitary adenocarcinoma's malignant biology — including resistance mechanisms (see PMID 39891847 on NDFIP1/mTOR-driven DA resistance) and metastatic behavior — represents a fundamentally different challenge. No published clinical evidence demonstrates cabergoline efficacy in confirmed pituitary adenocarcinoma. The TxGNN prediction most likely reflects shared ontological proximity to the well-evidenced benign adenoma indication, not tumor-type-specific signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cabergoline in pituitary adenocarcinoma.

---

## Literature Evidence

The retrieved publications mention cabergoline and pituitary pathology but none directly investigates or demonstrates cabergoline efficacy in pituitary adenocarcinoma specifically.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case Report | Medicine | MEN1 syndrome case with atypical multi-endocrine tumor presentation including pituitary adenoma; cabergoline mentioned as part of management. Highlights rarity and complexity of aggressive pituitary neoplasia. |
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case Report | Endocrine Practice | Long-term cabergoline (or octreotide) administration for ectopic ACTH hypersecretion post-adrenalectomy. Demonstrates cabergoline activity beyond classic prolactinoma in a pituitary-origin hormone excess state. |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case Report | Rev Esp Enferm Dig | Patient with known pituitary adenoma on cabergoline who developed pancreatic adenocarcinoma. Retrieved due to keyword overlap; not relevant to pituitary adenocarcinoma treatment. |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** One case report (PMID 21347189, identified in the rank 5 glaucoma evidence set) describes bilateral acute angle-closure glaucoma following cabergoline administration — a potentially serious adverse ocular event that should be considered in any prospective use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pituitary adenocarcinoma is an extremely rare malignancy with no direct clinical evidence supporting cabergoline as a treatment. All three retrieved publications are case reports that mention cabergoline in the context of benign or ectopic pituitary disease — none studies the drug in confirmed adenocarcinoma. The mechanistic rationale (D2 receptor pathway overlap with benign prolactinoma) is biologically plausible but unvalidated in the malignant setting, and known resistance mechanisms further limit confidence.

> **Contextual note:** The rank 3 predicted indication, **"Pituitary Cancer"** (TxGNN score 99.04%), encompasses the broader pituitary tumor spectrum and carries substantially stronger evidence — including a systematic review + meta-analysis (PMID 35902444) and a translational study (PMID 38989697) — reaching **Evidence Level L2** with a "Proceed with Guardrails" recommendation. If the research question is broadened from adenocarcinoma to pituitary neoplasms generally, the evidentiary basis improves significantly.

**To proceed, the following is needed:**

- Direct preclinical evidence (in vitro / in vivo) in pituitary adenocarcinoma cell models to confirm D2 pathway activity in the malignant phenotype
- Systematic review of any compassionate use, case series, or case reports specifically documenting cabergoline use in confirmed pituitary adenocarcinoma (as distinct from adenoma)
- DrugBank MOA data to formally characterize receptor binding profile and downstream signaling relevant to malignant transformation
- Verification of cabergoline's US regulatory status (Dostinex NDA history), as 0 NDAs in the current dataset may reflect a data pipeline gap rather than absence of approval
- Pituitary tumor specialist consultation to assess whether malignant pituitary cells retain sufficient D2 receptor expression to make cabergoline a viable therapeutic target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

