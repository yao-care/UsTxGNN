---
layout: default
title: Denileukin Diftitox
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 4
---

# Denileukin Diftitox
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

# Denileukin Diftitox: From Cutaneous T-Cell Lymphoma to Metastatic Neoplasm

## One-Sentence Summary

Denileukin diftitox (ONTAK) is a recombinant IL-2/diphtheria toxin fusion protein originally approved for cutaneous T-cell lymphoma (CTCL), targeting cells that express the high-affinity IL-2 receptor subunit CD25.
The TxGNN model identifies **Metastatic Neoplasm** as the best-evidenced repurposing candidate (score: 99.01%), supported by **10+ clinical trials** and **7 publications** evaluating its use across metastatic melanoma, renal cell carcinoma, and other solid tumors.
Evidence is rated at **Level L2**, driven primarily by completed Phase 2 trials in metastatic melanoma, yielding a "Proceed with Guardrails" recommendation for this indication.

> **Note on prediction ranking**: The highest TxGNN-scored prediction is plasmacytoma (99.87%, rank #1), but it carries no supporting clinical or preclinical evidence (L5, Hold). Metastatic Neoplasm (99.01%, rank #4) is featured here as the clinically actionable prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cutaneous T-cell lymphoma (CTCL) |
| Top TxGNN Prediction (by score) | Plasmacytoma — 99.87%, no supporting evidence (L5, Hold) |
| Best-Evidenced Prediction | **Metastatic Neoplasm** — 99.01%, L2 evidence |
| TxGNN Prediction Score | 99.01% (Metastatic Neoplasm) |
| Evidence Level | L2 |
| US Market Status | Not currently marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Proceed with Guardrails** (Metastatic Neoplasm) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on known published information, denileukin diftitox is a recombinant fusion protein that couples the cytotoxic domain of diphtheria toxin to human IL-2. It binds to the high-affinity IL-2 receptor complex (CD25/CD122/CD132), which is expressed on malignant T-cells in CTCL as well as on immunosuppressive regulatory T cells (Tregs) broadly across tumor types. After receptor-mediated internalization, the diphtheria toxin moiety blocks protein synthesis and triggers cell death.

The repurposing rationale for metastatic neoplasm extends beyond the original CTCL target. In the tumor microenvironment (TME) of solid tumors such as melanoma and renal cell carcinoma, Tregs accumulate densely, suppress CD8+ effector T-cell activity, and express high levels of CD25. Denileukin diftitox can selectively deplete this Treg population, thereby reshaping the immunosuppressive TME and restoring endogenous anti-tumor immunity — or potentiating concurrently administered vaccines and immunotherapies. Multiple clinical trials have directly tested this hypothesis in patients with metastatic solid tumors.

The mechanistic concept has remained clinically relevant through successive generations: a next-generation reformulation (E7777/Lymphir, with higher purity and reduced immunogenicity) is now in active Phase 1/2 trials combined with pembrolizumab (NCT05200559, n=70), confirming that the CD25-targeting Treg-depletion strategy is a current focus of oncology drug development rather than an abandoned concept.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00299689](https://clinicaltrials.gov/study/NCT00299689) | Phase 2 | Completed | 69 | Denileukin diftitox (ONTAK) monotherapy in Stage IV metastatic melanoma; largest completed Phase 2 trial directly evaluating this agent as a standalone treatment for a metastatic solid tumor |
| [NCT00082914](https://clinicaltrials.gov/study/NCT00082914) | Phase 2 | Completed | N/A | Direct evaluation of denileukin diftitox in metastatic melanoma or metastatic kidney cancer; tests ability to stimulate immune response to kill tumor cells in two major metastatic tumor subtypes |
| [NCT00128622](https://clinicaltrials.gov/study/NCT00128622) | Phase 1 | Completed | 24 | Treg depletion with denileukin diftitox followed by CEA-expressing fowlpox-TRICOM dendritic cell vaccine in advanced or metastatic CEA-expressing malignancies; demonstrates feasibility of sequential Treg-depletion + vaccine strategy across multiple solid tumor types |
| [NCT00278369](https://clinicaltrials.gov/study/NCT00278369) | Early Phase 1 | Completed | 20 | Denileukin diftitox combined with high-dose IL-2 in metastatic renal cell carcinoma; tests the hypothesis that Treg depletion can amplify IL-2-driven cytotoxic T-cell activity |
| [NCT05200559](https://clinicaltrials.gov/study/NCT05200559) | Phase 1/2 | Recruiting | 70 | E7777 (next-generation denileukin diftitox reformulation) combined with pembrolizumab in recurrent or metastatic solid tumors including ovarian cancer; represents the current leading-edge development of this CD25-targeting mechanism |
| [NCT00515528](https://clinicaltrials.gov/study/NCT00515528) | Phase 2 | Terminated | 17 | Randomized evaluation of multipeptide melanoma vaccine with or without denileukin diftitox in metastatic melanoma; terminated early, limiting interpretable outcomes |
| [NCT02009384](https://clinicaltrials.gov/study/NCT02009384) | Phase 2 | Terminated | 2 | Ipilimumab administered after denileukin diftitox Treg depletion in Stage IIIC/IV melanoma; terminated due to very low enrollment |
| [NCT00493129](https://clinicaltrials.gov/study/NCT00493129) | Phase 2 | Completed | 8 | ONTAK in systemic mastocytosis, a CD25-expressing mast cell malignancy; small sample limits generalizability but supports CD25-targeting rationale in non-lymphoma hematologic malignancies |
| [NCT00726037](https://clinicaltrials.gov/study/NCT00726037) | Phase 2 | Terminated | 7 | Treg suppression by denileukin diftitox in metastatic pancreatic cancer to optimize timing of subsequent dendritic cell vaccination; terminated early, suggesting enrollment and feasibility challenges |
| [NCT00945269](https://clinicaltrials.gov/study/NCT00945269) | Phase 1/2 | Terminated | 3 | Autologous CD8+ antigen-specific T cell clones infused after CD25-directed lymphodepletion in metastatic melanoma; early termination with minimal data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308572](https://pubmed.ncbi.nlm.nih.gov/16308572/) | 2005 | Clinical Trial | J Clin Invest | Denileukin diftitox selectively eliminates CD25+ Tregs from cancer patient PBMCs without toxicity to CD25-intermediate/low populations; Treg depletion significantly enhances immunostimulatory efficacy of tumor RNA-transfected DC vaccines — foundational mechanistic evidence |
| [18334033](https://pubmed.ncbi.nlm.nih.gov/18334033/) | 2008 | Clinical Research | J Transl Med | Transient Treg depletion with denileukin diftitox induced regression of melanoma metastases in patients; provides direct in-human evidence that Treg removal can break tumor immune tolerance and produce anti-tumor responses |
| [20664355](https://pubmed.ncbi.nlm.nih.gov/20664355/) | 2010 | Phase 1 Trial | J Immunother | Denileukin diftitox + high-dose IL-2 in metastatic renal cell carcinoma; sequential Treg depletion followed by cytokine immunotherapy explored to overcome Treg-mediated suppression and improve IL-2 response rates |
| [16224276](https://pubmed.ncbi.nlm.nih.gov/16224276/) | 2005 | Clinical/Mechanistic | J Immunother | At standard doses, denileukin diftitox did not reliably eliminate Tregs in melanoma patients; important cautionary finding raising questions about optimal dosing, scheduling, and Treg CD25 expression variability |
| [21770473](https://pubmed.ncbi.nlm.nih.gov/21770473/) | 2011 | Review | Drugs | Review of novel immunotherapeutic approaches for metastatic melanoma; includes denileukin diftitox among Treg-targeting strategies alongside ipilimumab, placing it in the evolving immunotherapy landscape |
| [18410797](https://pubmed.ncbi.nlm.nih.gov/18410797/) | 2008 | Review | Semin Oncol | Review of emerging agents for anthracycline- and taxane-refractory metastatic breast cancer; denileukin diftitox mentioned as a candidate in the broader context of metastatic solid tumor immunotherapy |
| [21990092](https://pubmed.ncbi.nlm.nih.gov/21990092/) | 2011 | Review/Guideline | Am J Hematol | CTCL 2011 diagnostic and management update; provides reference context for denileukin diftitox's original FDA-approved indication and its established role prior to market withdrawal |

---

## US Market Information

Denileukin diftitox is **not currently listed** as an active product in the US regulatory database under DrugBank ID DB00004. The original formulation (ONTAK, Eisai) received FDA approval for CTCL but was withdrawn from the US market in 2014 primarily due to manufacturing concerns. A next-generation, higher-purity reformulation — E7777, commercially known as **Lymphir** — received FDA approval in August 2023 for CTCL under a separate regulatory filing and is currently marketed.

No active NDA entries are available for this drug compound entry.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy / Immunotoxin — recombinant IL-2 receptor–directed diphtheria toxin conjugate; not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Moderate — intended lymphodepletion (Treg and CD25+ lymphocyte depletion) is the primary pharmacological mechanism; monitor for broader lymphopenia |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, lymphocyte subsets (CD4, CD8, Treg/CD25+), serum albumin (vascular leak syndrome surveillance), liver transaminases, creatinine, and fluid balance |
| Handling Protection | As a biologic immunotoxin, handle according to institutional cytotoxic biologic protocols; cold-chain storage required; avoid exposure via needlestick or mucosal contact |

---

## Safety Considerations

Please refer to the package insert for complete safety information, as specific warning and contraindication data were not available in the current dataset.

> **Critical known risk**: Denileukin diftitox carries a well-documented risk of **vascular leak syndrome** (capillary leak syndrome), characterized by hypoalbuminemia, edema, and hypotension. This was a significant clinical concern during the ONTAK era and must be proactively addressed in any new trial design or compassionate-use protocol.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Metastatic Neoplasm indication)*

**Rationale:**
Two completed Phase 2 trials directly evaluate denileukin diftitox in metastatic solid tumors — including one with n=69 in metastatic melanoma (NCT00299689) — and multiple Phase 1 trials confirm mechanistic feasibility of Treg depletion across tumor types. The ongoing Phase 1/2 trial of the next-generation formulation (E7777 + pembrolizumab, n=70) demonstrates continued industry investment in this mechanism, lowering the de-risking burden for a repurposing program.

**To proceed, the following is needed:**

- Full mechanism of action documentation from DrugBank API (currently a data gap)
- US FDA label review — use the Lymphir (E7777) label as the most current reference for safety warnings, dosing, and vascular leak syndrome management guidelines
- Biomarker-driven patient selection strategy: prospective assessment of tumor CD25 expression and Treg density as enrollment criteria
- Vascular leak syndrome risk mitigation protocol embedded in any new clinical trial design
- Evaluation of combination strategy (e.g., with anti-PD-1/PD-L1 checkpoint inhibitors), given that NCT05200559 is already testing this approach with the next-generation analog
- Regulatory pathway clarification: whether to pursue denileukin diftitox (DB00004) directly or position this as foundational evidence for the E7777 (Lymphir) repurposing program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

