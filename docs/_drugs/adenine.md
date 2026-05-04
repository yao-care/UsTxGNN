---
layout: default
title: Adenine
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 1
---

# Adenine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

The txgnn-pipeline skill confirms this is standard TxGNN report work. Now I'll generate the full evaluation report per the v5 prompt format.

---

# Adenine: From Purine Nucleobase to Drug-Induced Osteoporosis

## One-Sentence Summary

Adenine (DB00173) is a naturally occurring purine nucleobase and fundamental structural component of nucleotides (AMP/ADP/ATP), with no established therapeutic indications and no US market authorisation on record.
The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis** with a score of **99.16%**; however, this prediction is very likely a **false positive** — all retrieved evidence describes adenine *analogues* (Adefovir, Tenofovir) as *causative agents* of drug-induced bone loss, not as treatments.
Currently only **1 registry study** (Grade C, unrelated) and **4 indirect publications** (all Tier 3) are available, yielding an evidence level of **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None established |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

This prediction is **not supported by mechanistic evidence** — the available data points decisively in the opposite direction, and the high TxGNN score most likely reflects a model artefact rather than a genuine therapeutic signal.

Adenine (DB00173) is a purine nucleobase: one of the four bases in DNA and RNA, and the structural core of energy-carrying molecules such as AMP, ADP, and ATP. It is not an approved drug in the US, and no mechanism of action data is available for clinical therapeutic use. There is no established pharmacological pathway by which adenine itself would reverse or prevent drug-induced osteoporosis.

The high TxGNN score (0.9916) almost certainly arises from **semantic confusion** in the knowledge graph between *adenine* and *adenine nucleotide analogues* — specifically Adefovir dipivoxil and Tenofovir, which are structurally derived from adenine. These antiretroviral/antiviral drugs are well-documented *causes* of drug-induced osteoporosis: they inhibit mitochondrial DNA polymerase and impair renal tubular phosphate reabsorption, triggering Fanconi syndrome, hypophosphataemia, and ultimately hypophosphatemic osteomalacia or osteoporosis. Every piece of literature retrieved for this indication describes this toxicity pathway. The model appears to have linked "adenine → bone disease" co-occurrences in the literature without distinguishing therapeutic agent from causative agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06065852](https://clinicaltrials.gov/study/NCT06065852) | N/A | Recruiting | 35,000 | National Registry of Rare Kidney Diseases (RaDaR) — an observational data-collection registry for rare renal conditions; entirely unrelated to Adenine as a treatment for drug-induced osteoporosis. Inclusion is likely a retrieval artefact from the known adenine-nephropathy rat model. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41924521](https://pubmed.ncbi.nlm.nih.gov/41924521/) | 2026 | Case Report | Frontiers in Endocrinology | Adefovir dipivoxil (an adenine *analogue*) induced Fanconi syndrome → hypophosphatemic osteomalacia in a 67-year-old woman. Describes the adenine analogue as the **cause** of drug-induced bone disease, not a treatment. |
| [22943210](https://pubmed.ncbi.nlm.nih.gov/22943210/) | 2012 | PK/PD Review | Expert Opinion on Drug Metabolism & Toxicology | PK/PD review of emtricitabine/tenofovir for HIV; explains how nucleotide analogues act as chain terminators of viral reverse transcriptase. Not relevant to adenine as a therapeutic agent. |
| [20026012](https://pubmed.ncbi.nlm.nih.gov/20026012/) | 2010 | In Vitro Mechanistic Study | Biochemical and Biophysical Research Communications | Tenofovir downregulates *Gnas*, *Got2*, and *Snord32a* in primary osteoclasts, providing a mechanistic basis for **tenofovir-induced** bone density loss — again describing an adenine analogue as the causative agent. |
| [31026554](https://pubmed.ncbi.nlm.nih.gov/31026554/) | 2019 | Animal Study | Journal of Ethnopharmacology | Xian-Ling-Gu-Bao herbal formula hepatotoxicity in rats; used clinically to treat osteoporosis. No connection to adenine or drug-induced osteoporosis as a target indication. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Adenine → Drug-Induced Osteoporosis is assessed as a **false positive driven by semantic conflation**: adenine nucleotide analogues (Adefovir, Tenofovir) co-occur with drug-induced osteoporosis in the literature precisely because they *cause* the condition, and the model has not distinguished this from a therapeutic relationship. There is no mechanistic hypothesis, no clinical trial evidence, and no published literature supporting adenine itself as a treatment for drug-induced osteoporosis.

**To proceed, the following would be needed:**

- A credible mechanistic hypothesis explaining how free adenine (not its phosphonate analogues) could therapeutically reverse or prevent drug-induced osteoporosis
- Preclinical evidence (cell-based or animal model) specifically testing adenine — not adefovir or tenofovir — in a bone loss model
- Knowledge graph audit to flag and correct the adenine ↔ adenine-analogue semantic conflation in TxGNN, to prevent similar false-positive propagation to other candidates
- If no mechanistic rationale can be established after literature review, this candidate should be formally **deprioritized** and recorded as a confirmed model artefact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

