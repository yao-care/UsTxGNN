---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 858
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levothyroxine: predicted new indication Nodular goiter (evidence level L5). Approved use: Hypothyroidism"
monitor_inn: "LEVOTHYROXINE"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
---

# Levothyroxine
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

# Levothyroxine: From Hypothyroidism to Nodular Goiter

## One-Sentence Summary

Levothyroxine is a synthetic thyroid hormone, originally used to treat hypothyroidism and other thyroid conditions such as congenital hypothyroidism, goiter, Hashimoto thyroiditis and thyroid cancer.
The TxGNN model predicts it may be effective for **nodular goiter**, with **2 clinical trials** and **18 publications** currently supporting this direction.
The evidence is mixed: levothyroxine gives modest volume reduction, and other treatments are often preferred.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (the data compiled for this report does not include approved indication text from US labels; this comes from the knowledge-graph indication list) |
| Predicted New Indication | Nodular goiter |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L1 (rests on randomized controlled designs; the main trial is Phase 4 rather than a classic Phase 3) |
| US Market Status | Cancelled only (all 11 listed authorizations are cancelled) |
| Number of NDAs | 11 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, levothyroxine replaces thyroid hormone and suppresses pituitary TSH secretion. TSH is a main growth stimulus for thyroid tissue.

Hypothyroidism and goiter are both thyroid disorders, and goiter is already among the drug's known indications. Nodular goiter is closely related. Lowering TSH may limit the growth of nodular thyroid tissue and help prevent recurrence after surgery.

The evidence is mixed. Suppression gives modest volume reduction, nodules often regrow after treatment stops, and long-term TSH suppression carries risks, including bone loss and cardiac effects such as atrial fibrillation. Radioiodine and surgery are often preferred alternatives.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277589](https://clinicaltrials.gov/study/NCT00277589) | Phase 4 | Completed | 1024 | Randomized, observer-blind, placebo-controlled trial of TSH-adapted therapy in nodular goiter. The primary objective was change in total nodule volume. This trial tests the indication directly. |
| [NCT00941551](https://clinicaltrials.gov/study/NCT00941551) | N/A | Completed | 150 | Five-year follow-up of a randomized trial of unilateral lobectomy with or without postoperative levothyroxine. Compares recurrence of nodular goiter in the contralateral lobe. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11238476](https://pubmed.ncbi.nlm.nih.gov/11238476/) | 2001 | RCT | J Clin Endocrinol Metab | 64 patients with sporadic nontoxic nodular goiter randomized to radioiodine or suppressive levothyroxine, compared over 2 years |
| [10426591](https://pubmed.ncbi.nlm.nih.gov/10426591/) | 1999 | Clinical study | Endocrine Journal | Six months of levothyroxine in 35 patients with diffuse and 35 with nodular euthyroid goiter, assessing thyroid and nodule volume |
| [8299711](https://pubmed.ncbi.nlm.nih.gov/8299711/) | 1993 | Clinical study | Exp Clin Endocrinol | Suppressive levothyroxine in 104 patients with nontoxic benign multinodular goiter |
| [10382684](https://pubmed.ncbi.nlm.nih.gov/10382684/) | 1999 | Retrospective cohort | Endocr Res | Suppressive versus replacement levothyroxine in solitary nodular disease and multinodular goiter |
| [20683172](https://pubmed.ncbi.nlm.nih.gov/20683172/) | 2010 | Clinical study | Endocr J | Short-term levothyroxine effects in 71 pre-menopausal women with multinodular disease |
| [19636201](https://pubmed.ncbi.nlm.nih.gov/19636201/) | 2009 | Retrospective study | J Endocrinol Invest | Levothyroxine for preventing nodular recurrence after hemithyroidectomy |
| [27242669](https://pubmed.ncbi.nlm.nih.gov/27242669/) | 2016 | Review | Front Endocrinol | Levothyroxine for goiter volume reduction is controversial; compares radioiodine and surgery |
| [34961921](https://pubmed.ncbi.nlm.nih.gov/34961921/) | 2021 | Cochrane review | Cochrane Database Syst Rev | rhTSH-aided radioiodine for non-toxic multinodular goitre; levothyroxine is one of the alternatives |
| [8844728](https://pubmed.ncbi.nlm.nih.gov/8844728/) | 1996 | Review | Otolaryngol Clin North Am | Evaluation and management of multinodular goiter |
| [19106244](https://pubmed.ncbi.nlm.nih.gov/19106244/) | 2009 | Review | Eur J Endocrinol | Levothyroxine is no longer recommended for routine use because of low efficacy and potential side effects |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021402 | Synthroid (AbbVie) | Tablet | Not available |
| NDA021924 | Tirosint (IBSA Pharma) | Capsule | Not available |
| NDA202231 | Levothyroxine Sodium (Fresenius Kabi) | Lyophilized powder for injection | Not available |
| NDA021116 | Levothyroxine sodium (Preferred Pharmaceuticals) | Tablet | Not available |
| NDA021342 | Levothyroxine Sodium (Bryant Ranch Prepack) | Tablet | Not available |

All 11 authorizations in the data are listed as cancelled. Only 5 are shown here.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension, pituitary hormone deficiencies (including hypopituitarism and Sheehan syndrome), osteoporosis (including postmenopausal), diabetes mellitus and diabetic ketoacidosis, coronary artery disease and myocardial infarction, and thymus gland disease.
- **Drug Interactions**: 100 interactions were identified. Most are Moderate. Examples include diabetes drugs (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, dulaglutide, albiglutide), acid-lowering drugs (omeprazole, rabeprazole, dexlansoprazole), calcium and magnesium products (calcium acetate, calcium phosphate, magnesium oxide) and epinephrine. Cimetidine is Minor.
- **Risks of long-term TSH suppression**: bone loss and atrial fibrillation or other cardiac effects, as described in the literature.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A large randomized, placebo-controlled Phase 4 trial (n=1024) and a randomized RCT comparing levothyroxine with radioiodine support the prediction, and the drug is already used clinically for goiter. However, efficacy is modest, nodules regrow after withdrawal, and long-term suppression has bone and cardiac risks. Alternatives are often preferred. Use should be limited to selected patients with TSH monitoring.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications
- Published results and outcomes of NCT00277589
- Patient selection criteria and a TSH and bone/cardiac monitoring plan
- Confirmation of current US marketing status, since all listed authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

