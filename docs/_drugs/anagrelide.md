---
layout: default
title: Anagrelide
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 2
---

# Anagrelide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is a platelet-reducing agent used globally for essential thrombocythemia (ET) and related myeloproliferative neoplasms, though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Reactive Thrombocytosis**, with **0 clinical trials** and **10 publications** currently available — most of which discuss the distinction between ET and reactive thrombocytosis rather than anagrelide's therapeutic use in the reactive form.
The high prediction score likely reflects a shared high-platelet phenotype in the model rather than genuine therapeutic applicability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Essential Thrombocythemia (no TFDA license on file; drug not marketed in Taiwan) |
| Predicted New Indication | Reactive Thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological literature, anagrelide selectively inhibits megakaryocyte maturation and differentiation, thereby reducing platelet production. This mechanism underlies its efficacy in clonal thrombocytosis — conditions such as ET, polycythemia vera, and other myeloproliferative neoplasms where platelet overproduction originates from an intrinsic bone marrow clonal disorder.

Reactive thrombocytosis, however, is a fundamentally different condition. It is a secondary, transient response to external stimuli — infection, inflammatory disease, iron deficiency, post-splenectomy state, or malignancy — and typically resolves once the underlying cause is treated. Clinical guidelines worldwide do not recommend platelet-lowering agents for reactive thrombocytosis; the treatment priority is the root cause, not the elevated platelet count itself.

The high TxGNN score (99.83%) most likely reflects the model's recognition of shared phenotypic features — specifically, elevated platelet counts — between ET and reactive thrombocytosis, rather than a true mechanistic or therapeutic overlap. The retrieved literature consistently uses reactive thrombocytosis as a differential diagnosis to be excluded before initiating anagrelide, reinforcing the conclusion that this prediction represents a model limitation rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective Cohort | Pediatric Blood & Cancer | 12 pediatric cases comparing ET vs reactive thrombocythemia; highlights the critical importance of differential diagnosis before initiating platelet-lowering therapy |
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Narrative Review | Expert Review of Anticancer Therapy | Comprehensive update on anagrelide's mechanism and role in clonal thrombocytosis; explicitly distinguishes reactive thrombocytosis (no treatment needed) from clonal forms |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Critical Review | Leukemia & Lymphoma | Critical evaluation of anagrelide in ET and related disorders; reactive thrombocytosis explicitly excluded from indications for cytoreductive therapy |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Narrative Review | Medical Journal of Australia | Overview of ET diagnosis and management; underscores that diagnosis requires exclusion of reactive thrombocytosis before treatment |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Narrative Review | Leukemia Research | Case-based review of thrombocytapheresis in myeloproliferative neoplasms; medical cytoreduction (including anagrelide) discussed only for clonal, not reactive, thrombocytosis |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | European Journal of Case Reports in Internal Medicine | Acute MI in an ET patient on anagrelide; illustrates thrombotic risk management challenges in myeloproliferative disorders |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski arhiv za celokupno lekarstvo | First reported case of ET concurrent with ankylosing spondylitis; reactive mild thrombocytosis from spondylitis contrasted with true ET requiring anagrelide |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | Digital replantation in a post-splenectomy patient with extreme thrombocytosis; anagrelide considered for peri-operative platelet control in a reactive (post-splenectomy) context — one of the few scenarios where the boundary between reactive and clonal management blurs |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Narrative Review | Japanese Journal of Clinical Hematology | Japanese review of ET treatment options including anagrelide; reactive thrombocytosis listed as a key differential to exclude |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Narrative Review | American Journal of the Medical Sciences | Early characterization of the clinical spectrum of thrombocytosis; describes cytokine regulation of platelet production and the distinct biology of reactive vs clonal forms |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Reactive thrombocytosis is a secondary, typically self-limiting condition treated by addressing its underlying cause; cytoreductive therapy with anagrelide has no established guideline support for this indication, and the existing literature uses it as a differential to be excluded rather than a treatment target. The high TxGNN score reflects phenotypic similarity at the model level, not biological plausibility.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve anagrelide's full mechanism from DrugBank to identify any edge-case links to secondary thrombocytosis pathways (e.g., inflammatory megakaryopoiesis)
- **Safety baseline**: Download and parse the TFDA package insert (or FDA Agrylin® label) to complete the S1 safety screening blocked by the current data gap
- **Specific clinical hypothesis**: Identify whether any patient subgroup with reactive thrombocytosis (e.g., extreme thrombocytosis post-splenectomy with thrombotic risk) might benefit — and whether this constitutes a meaningful new indication or an off-label extension of existing ET use
- **Prospective evidence**: Any preclinical or mechanistic study specifically evaluating anagrelide in secondary/reactive thrombocytosis models would be required before advancing beyond Hold status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

