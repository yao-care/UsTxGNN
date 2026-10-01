---
layout: default
title: Anagrelide
parent: Moderate Evidence (L3-L4)
nav_order: 336
evidence_level: L4
indication_count: 2
---

# Anagrelide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Anagrelide: From Thrombocythemia (Myeloproliferative Disorders) to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is an oral platelet-lowering drug. The retrieved reviews describe it mainly for clonal thrombocytosis such as essential thrombocythemia, but the US labeling records in this pack contain no indication text.
The TxGNN model predicts it may be effective for **reactive thrombocytosis**, with **0 clinical trials** and **10 publications** (none testing anagrelide in reactive thrombocytosis).
The high score most likely reflects its established use in essential thrombocythemia rather than independent evidence for this new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the retrieved US license records. The retrieved reviews describe use in essential thrombocythemia and related myeloproliferative disorders. |
| Predicted New Indication | Reactive thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 licenses in total (1 NDA, the rest ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this record. From general knowledge and the retrieved reviews (PMID 15270658, 16019501), anagrelide lowers platelet counts mainly by inhibiting megakaryocyte maturation. PDE3 inhibition is also described. That is a plausible pharmacological fit for any condition with excess platelets.

The link to reactive thrombocytosis is weak, however. Reactive thrombocytosis is driven by inflammation, iron deficiency, splenectomy or malignancy. It usually carries a low thrombotic risk and is managed by treating the underlying cause, not with platelet-lowering drugs. One retrieved review states that reactive thrombocytosis does not require therapeutic intervention, while clonal thrombocytosis may. The retrieved literature mostly *distinguishes* reactive from clonal thrombocytosis. None of it shows anagrelide benefiting reactive thrombocytosis.

The TxGNN score of 0.998 most likely comes from the drug's well-established use in essential thrombocythemia, a closely related platelet disorder. It is not independent support for this prediction.

The second predicted indication, inverse Klippel-Trenaunay syndrome (score 99.59%), has no trials or literature. No mechanistic link to anagrelide was identified, so it is not evaluated further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | Update on anagrelide's mechanisms and therapeutic potential. Reactive thrombocytosis needs no therapy, while clonal thrombocytosis may. |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leuk Lymphoma | Critical review of anagrelide in essential thrombocythemia and related disorders. Compares it with hydroxyurea, which has controlled-trial evidence of reducing thrombosis in high-risk patients. |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Aust | Essential thrombocythemia is diagnosed by excluding other myeloproliferative disorders and reactive thrombocytosis. Platelet-lowering therapy is advised above 1000 x 10⁹/L. |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leuk Res | Case-based review of thrombocytapheresis in hyperthrombocytosis in myeloproliferative neoplasms. Medical cytoreduction remains the mainstay. |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | Clinical spectrum of thrombocytosis and thrombocythemia, including the cytokine regulation of platelet production. |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | Diagnosis and treatment of essential thrombocythemia. Anagrelide is listed among the agents that suppress megakaryocyte proliferation. |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective cohort | Pediatr Blood Cancer | Retrospective analysis of 12 children comparing essential versus reactive thrombocythemia. |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case report | Eur J Case Rep Intern Med | Acute myocardial infarction in a patient with essential thrombocythemia treated with anagrelide. |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case report | Srp Arh Celok Lek | Essential thrombocythemia with ankylosing spondylitis, treated with anagrelide, DMARDs and etanercept. |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case report | Medicine | Digit replantation in a patient with thrombocytosis after splenectomy. Offers a guideline for replantation when thrombocytosis is expected. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020333 | Agrylin | Capsule | Takeda Pharmaceuticals America, Inc. |
| ANDA076683 | Anagrelide | Capsule | Chartwell RX, LLC |
| ANDA076811 | Anagrelide | Capsule | ANI Pharmaceuticals, Inc. |
| ANDA209151 | Anagrelide | Capsule | Torrent Pharmaceuticals Limited |

The records list 7 licenses in total. Only the four unique authorizations above are shown, because ANDA076683 appears twice. Approved indication text is not included in the retrieved records. All products are oral capsules.

---

## Safety Considerations

Please refer to the package insert for safety information.

One retrieved case report (PMID 38455691) describes an acute myocardial infarction in a patient with essential thrombocythemia who was on anagrelide. This is a single case and does not establish causality.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the retrieved literature contains no study of anagrelide in reactive thrombocytosis. The condition is usually managed by treating the underlying cause. The high TxGNN score most likely reflects the drug's use in essential thrombocythemia. The prediction is therefore supported by model output and pharmacological plausibility only.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are needed before any safety screening
- Mechanism of action data (for example from DrugBank)
- Evidence that any subgroup with reactive thrombocytosis has a thrombotic risk high enough to justify platelet-lowering therapy
- Clinical or observational data on anagrelide in reactive thrombocytosis
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

