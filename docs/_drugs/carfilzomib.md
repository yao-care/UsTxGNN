---
layout: default
title: Carfilzomib
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Carfilzomib: From Multiple Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib is a proteasome inhibitor marketed in the US as KYPROLIS. The license text in the source data is blank, but the literature in this pack describes it as an anti-myeloma drug. TxGNN ranks five new indications above 99% score, mostly melanoma subtypes, but there are **0 clinical trials** and only **5 preclinical or computational publications**. The evidence is currently at the "research question" stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma (inferred from the literature; the license record has no indication text) |
| Predicted New Indication | Rank 1 is "CMM7", an unresolved identifier. The evidence-bearing prediction is **melanoma** (rank 5), and ranks 2 to 4 are melanoma subtypes. |
| TxGNN Prediction Score | 99.37% for CMM7 (rank 1); 99.03% for melanoma (rank 5) |
| Evidence Level | L5 for CMM7 and the three melanoma subtypes; L4 for melanoma |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 records, all for NDA202714 |
| Recommended Decision | Hold |

**Other predicted indications**

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Pediatric leptomeningeal melanoma | 99.30% | L5 | No trials or literature. CNS penetration and pediatric safety are unknown. |
| 3 | Epithelioid cell uveal melanoma | 99.23% | L5 | Biologically distinct from cutaneous melanoma. |
| 4 | Vulvar melanoma | 99.19% | L5 | Any support is inherited from the generic melanoma node. |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Carfilzomib is generally known as an irreversible proteasome inhibitor. This comes from general knowledge, not from this dataset. Blocking the proteasome causes misfolded proteins to accumulate, which triggers apoptotic stress in cancer cells. That is why the drug works in multiple myeloma.

Myeloma and melanoma are different diseases, but the proteasome pathway is a plausible shared vulnerability. The only direct support is an in vitro study (PMID 33671902) in B16-F1 murine melanoma cells. In it, carfilzomib combined with bortezomib enhanced apoptosis and activated several caspases.

Three cautions apply:
- The high scores across melanoma subtypes likely reflect graph proximity to the parent melanoma node. They are not independent evidence.
- Murine cutaneous melanoma data should not be extrapolated to uveal, vulvar, or pediatric leptomeningeal melanoma.
- The top-ranked entity, "CMM7", cannot be resolved to a disease, so no mechanistic link can be assessed for it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical | Biology | Carfilzomib plus bortezomib enhanced apoptosis in B16-F1 melanoma cells, with activation of caspases 3, 8, 9 and 12. This is the only paper directly on carfilzomib in melanoma. |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic | Matrix Biology | Bortezomib and carfilzomib activate NF-κB and upregulate heparanase in tumor cells, which is linked to a more aggressive tumor phenotype. The study is in myeloma, not melanoma. |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico | J Biomol Struct Dyn | Docking and dynamics screening of clinical drugs against kinase targets across ten cancer types, including melanoma. Only tangentially related to carfilzomib. |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical mechanistic | Mol Cancer Res | ZFAND2A (AIRAP) regulates cell survival in human melanoma via the E3 ligase cIAP2. A mechanistic paper, only tangentially related to carfilzomib. |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical mechanistic | Leukemia | BET-targeting PROTACs are active in multiple myeloma models. Only tangentially related to carfilzomib. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA202714 | KYPROLIS (Onyx Pharmaceuticals, Inc.) | Injection, powder, lyophilized, for solution | Not provided in the source data |

The pack lists three identical license records for this NDA. They are shown once here.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with differential), liver and renal function; confirm against the package insert |
| Handling Protection | Follow institutional hazardous or cytotoxic drug handling procedures for parenteral anticancer agents |

The classification comes from general knowledge, since the pack has no DrugBank toxicity data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are model output only. There are no registered trials and no human efficacy or safety data. The one directly relevant study is an in vitro murine cutaneous melanoma experiment. The top-ranked entity is unresolved, and the melanoma subtype scores likely come from graph proximity. Melanoma itself can be treated as a preclinical research question (L4), not as a candidate for clinical development.

**To proceed, the following is needed:**
- Resolve what "CMM7" refers to in the TxGNN knowledge graph.
- Obtain the KYPROLIS package insert (warnings, contraindications, approved indications) for safety screening.
- Retrieve the mechanism of action from DrugBank (DB08889) to support mechanistic-link analysis.
- Run preclinical validation in human melanoma models, ideally including uveal melanoma. Assess CNS penetration before considering leptomeningeal disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

