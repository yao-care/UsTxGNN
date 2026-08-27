---
layout: default
title: Difluprednate
parent: 僅模型預測 (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Difluprednate
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

# Difluprednate: From Topical Anti-Inflammatory Agent to Iris Disease

## One-Sentence Summary

> Difluprednate is a potent synthetic corticosteroid currently formulated as a 0.05% ophthalmic emulsion; it is **not yet marketed in Taiwan** and has no recorded original indication in the Taiwan regulatory dataset.
> Among 10 TxGNN-predicted indications, the only one supported by real clinical and literature evidence is **Iris Disease** (anterior segment/uveitic inflammation), backed by **3 relevant clinical trials** (2 of them completed Phase 3 pivotal studies) and **2 publications**.
> The other 9 higher-scoring TxGNN predictions (e.g., rare genetic syndromes, seborrheic keratosis) have no supporting evidence and several are flagged in the source data itself as likely knowledge-graph false positives — they are summarized separately below and excluded from the primary evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory data (drug not marketed); historically documented as a topical anti-inflammatory dermatological agent |
| Predicted New Indication | Iris Disease (anterior segment/uveitic inflammation) |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: This indication was selected from the 10 TxGNN candidates in the evidence pack because it is the only one with actual clinical trial and literature support. See "Other TxGNN-Predicted Indications" below for the remaining 9, all of which are lower-priority or unsupported.*

---

## Why is This Prediction Reasonable?

Detailed, formally sourced mechanism-of-action data is not currently available (flagged as a High-severity data gap pending a DrugBank API query). Based on the available literature, difluprednate is a potent glucocorticoid-receptor agonist that was **historically used as a topical anti-inflammatory dermatological agent**, and is now formulated as a 0.05% ophthalmic emulsion (marketed elsewhere as Durezol) for treating ocular inflammation.

The predicted new indication, "Iris Disease," clinically overlaps with the drug's already-established ophthalmic anti-inflammatory use: difluprednate's approved formulation is specifically designed to treat inflammation and pain following ocular surgery and severe anterior uveitis — both of which fall under the anterior-segment/iris inflammatory disease spectrum. In other words, this is less a novel repurposing hypothesis and more a **confirmation, via TxGNN, of an already-documented pharmacological use** that simply has no corresponding regulatory record in Taiwan (since the product is not yet marketed there).

Mechanistically, this makes the prediction highly plausible rather than speculative: two completed Phase 3 trials directly evaluate difluprednate ophthalmic emulsion against active comparators (prednisolone acetate) for anterior-segment inflammatory conditions, providing direct pharmacological and clinical continuity between the drug's known activity and the predicted indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00407056](https://clinicaltrials.gov/study/NCT00407056) | Phase 3 | Completed | 20 | Open-label study directly evaluating 0.05% difluprednate ophthalmic emulsion for severe anterior uveitis, including panuveitis — direct drug-to-indication match. |
| [NCT01124045](https://clinicaltrials.gov/study/NCT01124045) | Phase 3B | Completed | 80 | Multicenter, randomized, double-masked, active-controlled pivotal trial comparing Durezol (difluprednate) to Pred Forte (prednisolone acetate) for inflammation following cataract surgery in children 0–3 years. |
| [NCT03693989](https://clinicaltrials.gov/study/NCT03693989) | Phase 3 | Completed | 178 | Randomized, double-blind trial of ophthalmic emulsion "PRO-145" vs. prednisolone acetate 1% for post-phacoemulsification inflammation/pain; drug identity relative to branded difluprednate needs confirmation (possible generic/biosimilar formulation). |

*One additional hit (NCT05082415, the "IRIS Registry" study of brolucizumab for wet AMD) was screened out as irrelevant — it matches on the word "IRIS" (a registry name), not on the disease "iris disease," and involves an unrelated anti-VEGF drug.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Preclinical/PK study | J Ocul Pharmacol Ther | Glucocorticoid receptor-binding bioassay in rabbits characterizing difluprednate's pharmacokinetics as an ophthalmic agent; notes its long-standing prior use as a topical anti-inflammatory dermatological agent, supporting high anti-inflammatory potency relative to comparator steroids. |
| [27594198](https://pubmed.ncbi.nlm.nih.gov/27594198/) | 2016 | Case Report | Ophthalmology | Describes long-term management of panuveitis and iris heterochromia in an Ebola survivor (abstract not available; summarized from title — real-world evidence of corticosteroid-based management in iris/uveitic disease). |

---

## Taiwan Market Information

Difluprednate is **not currently marketed in Taiwan** — there are no NDA/license records in the regulatory dataset (`total_licenses = 0`). No approved indication, dosage form, or product name is available for the Taiwan market at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No key warnings, contraindications, or drug-interaction data were retrievable at this time; obtaining the TFDA label is flagged as a Blocking data gap — see Conclusion below.)*

---

## Other TxGNN-Predicted Indications (Not Selected)

For transparency, the remaining 9 predictions in the evidence pack scored higher on raw TxGNN rank but had no supporting clinical trial or literature evidence. Most are explicitly assessed in the source data as likely knowledge-graph artifacts rather than clinically actionable signals:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|
| Familial adrenal hypoplasia w/ absent pituitary LH | 99.96% | L5 | Hold |
| Seborrheic keratosis | 99.96% | L5 | Hold |
| PAGOD syndrome | 99.93% | L5 | Hold |
| Vulvar inverted follicular keratosis | 99.92% | L5 | Hold |
| Adrenocortical insufficiency | 99.67% | L4 | Hold |
| Seborrheic dermatitis | 99.53% | L4 | Research Question |
| 46,XY disorder of sex development | 99.47% | L5 | Hold |
| Necrobiosis lipoidica | 99.24% | L4 | Research Question |
| Nephrotic syndrome | 99.21% | L4 | Hold |

The two "Research Question" candidates (seborrheic dermatitis, necrobiosis lipoidica) have a plausible corticosteroid class-effect rationale but no difluprednate-specific evidence, and the drug's current ophthalmic-only dosage form does not match the dermatologic route these indications would require.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Difluprednate's approved formulation already has direct, completed Phase 3 evidence (NCT00407056, NCT01124045) supporting efficacy in anterior-segment inflammatory conditions closely related to iris disease, giving this specific prediction L1-level evidence. However, the drug is not yet marketed in Taiwan and core safety documentation is entirely missing, so guardrails are required before any regulatory or clinical advancement.

**To proceed, the following is needed:**
- Obtain the TFDA package insert (warnings/contraindications) — currently a **Blocking** data gap preventing the S1 safety pre-assessment
- Obtain formal mechanism-of-action documentation via the DrugBank API (High-priority data gap)
- Confirm whether "PRO-145" (NCT03693989) is difluprednate itself or a distinct generic/biosimilar formulation
- Assess Taiwan market entry pathway, since the product currently has zero NDA/license records
- Deprioritize the 9 lower-evidence TxGNN predictions unless new clinical or mechanistic data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

