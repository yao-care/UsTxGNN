---
layout: default
title: Ecallantide
parent: 僅模型預測 (L5)
nav_order: 639
evidence_level: L5
indication_count: 6
---

# Ecallantide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ecallantide: From Hereditary Angioedema to C1 Inhibitor Deficiency — A Confirmatory, Not Novel, Signal

## One-Sentence Summary

> Ecallantide (DrugBank DB05311) is a recombinant plasma kallikrein inhibitor historically known as Kalbitor, publicly documented as having been developed for acute attacks of Hereditary Angioedema (HAE) — though this evidence pack's own `original_indications` field is empty and cannot confirm that.
> The TxGNN model's top prediction is **C1 inhibitor deficiency**, which is the underlying pathophysiology of HAE itself, supported by **7 clinical trials** (including 2 completed Phase 3 RCTs) and **20 publications**.
> This is best read as the model **rediscovering an existing, well-evidenced use** rather than surfacing a genuinely new indication — and the drug currently shows **zero active market licenses**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (`original_indications` is empty). Publicly known historical use: acute attacks of Hereditary Angioedema (marketed as Kalbitor) |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| US Market Status | ✗ Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note:** C1 inhibitor deficiency is the causal defect behind Hereditary Angioedema — the same disease ecallantide is already publicly known to treat. This prediction should not be treated as a novel repurposing candidate until the discrepancy in the evidence pack's original-indication field is resolved.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as DG002, High severity). Based on established public information, ecallantide is a recombinant protein and potent, selective inhibitor of plasma kallikrein — the enzyme responsible for generating bradykinin via the kallikrein-kinin pathway.

C1 inhibitor deficiency (hereditary or acquired) removes the normal brake on plasma kallikrein activity, leading to excess bradykinin generation, increased vascular permeability, and the recurrent angioedema attacks characteristic of HAE. Ecallantide's kallikrein-inhibiting action addresses this pathophysiology directly, which is consistent with both the very high TxGNN score (99.99%) and the depth of completed Phase 3 evidence below.

Because this mechanistic link is direct rather than inferred through indirect network proximity, and because ecallantide is publicly documented as already used for this exact disease process, the "prediction" here functions more as a validation check on the TxGNN model than as a discovery of new therapeutic potential. The evidence pack's missing `original_indications` field should be filled in to confirm this before the candidate is scored as a true repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00457015](https://clinicaltrials.gov/study/NCT00457015) | Phase 3 | Completed | 96 | EDEMA4: randomized, double-blind, placebo-controlled trial of ecallantide (DX-88) for acute HAE attacks |
| [NCT00262080](https://clinicaltrials.gov/study/NCT00262080) | Phase 3 | Completed | 91 | Double-blind, placebo-controlled study followed by repeat-dosing phase for acute HAE attacks |
| [NCT00456508](https://clinicaltrials.gov/study/NCT00456508) | Phase 3 | Completed | 147 | Open-label continuation of DX-88 for repeated HAE attacks; follow-up cohort of EDEMA4 patients |
| [NCT01826916](https://clinicaltrials.gov/study/NCT01826916) | Phase 2 | Completed | 77 | EDEMA2: open-label dose-ranging study of repeated dosing in HAE patients |
| [NCT01059526](https://clinicaltrials.gov/study/NCT01059526) | N/A (Phase 4) | Completed | 81 | Long-term observational safety study evaluating immunogenicity and hypersensitivity with KALBITOR exposure |
| [NCT01832896](https://clinicaltrials.gov/study/NCT01832896) | Phase 2 | Withdrawn | 0 | Planned tolerability/safety study of single SC dose in children and adolescents with HAE |
| [NCT01253382](https://clinicaltrials.gov/study/NCT01253382) | Phase 2/3 | Withdrawn | 0 | Planned PK, safety, and efficacy study in prepubertal pediatric patients with acute HAE attacks |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21760740](https://pubmed.ncbi.nlm.nih.gov/21760740/) | 2011 | Review | Clin Cosmet Investig Dermatol | Ecallantide as a novel treatment for HAE attacks due to C1 inhibitor deficiency |
| [23406939](https://pubmed.ncbi.nlm.nih.gov/23406939/) | 2013 | Case series | Allergy Asthma Proc | Ecallantide for acute attacks of acquired C1 esterase inhibitor deficiency |
| [22472866](https://pubmed.ncbi.nlm.nih.gov/22472866/) | 2012 | Review | Am J Health Syst Pharm | Pharmacology, efficacy, safety, and place in therapy of ecallantide for HAE |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Overview of current and emerging therapies for C1-INH-HAE |
| [27503784](https://pubmed.ncbi.nlm.nih.gov/27503784/) | 2017 | Consensus | Allergy | International consensus on diagnosis and management of pediatric C1-INH-HAE |
| [26512744](https://pubmed.ncbi.nlm.nih.gov/26512744/) | 2016 | Review | Expert Opin Pharmacother | Current treatment options for HAE due to C1 inhibitor deficiency |
| [29357215](https://pubmed.ncbi.nlm.nih.gov/29357215/) | 2018 | Review | Skin Therapy Lett | New treatments for HAE, including kallikrein-kinin pathway–targeted drugs |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Review | Immunol Allergy Clin North Am | Acquired C1 inhibitor deficiency: diagnosis and disease associations |
| [28687108](https://pubmed.ncbi.nlm.nih.gov/28687108/) | 2017 | Review | Immunol Allergy Clin North Am | Acute management strategies for HAE attacks |
| [26429506](https://pubmed.ncbi.nlm.nih.gov/26429506/) | 2015 | Review | Expert Opin Drug Saf | Safety profile of treatments for angioedema with hereditary C1 inhibitor deficiency |

---

## US Market Information

Currently no marketing authorization records in the evidence pack (`total_licenses: 0`, market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA/FDA label data (warnings, contraindications) is a **Blocking** data gap (DG001) — this must be resolved before the candidate can proceed to safety pre-assessment (S1).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Efficacy evidence is strong (L1: two completed Phase 3 RCTs plus a broad literature base), but the missing `original_indications` data means this may be a rediscovery of an already-known use rather than a new repurposing opportunity, and the drug currently has zero active market licenses.
- The Blocking safety data gap (TFDA label) prevents completion of the S1 safety pre-assessment regardless of efficacy strength.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/FDA package insert (warnings, contraindications) to unblock S1 safety review
- Resolve DG002: confirm mechanism of action via DrugBank API
- Clarify why `original_indications` is empty — confirm whether ecallantide's historical approved indication is in fact the same as this "predicted" indication
- Confirm current market/registration status given 0 active licenses (e.g., discontinued product vs. never registered)
- Drug-drug interaction data (DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

