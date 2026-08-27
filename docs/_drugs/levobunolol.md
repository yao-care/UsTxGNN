---
layout: default
title: Levobunolol
parent: 僅模型預測 (L5)
nav_order: 852
evidence_level: L5
indication_count: 3
---

# Levobunolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Levobunolol: From Established Glaucoma Therapy to Primary Hereditary Glaucoma

## One-Sentence Summary

> Levobunolol is a non-selective topical β-adrenergic blocker whose real-world, well-established use is lowering intraocular pressure in open-angle glaucoma and ocular hypertension — though this evidence pack has no formal license record confirming that indication. TxGNN's top-ranked *new* signal is **Primary Hereditary Glaucoma**, a genetically-defined glaucoma subtype, but this specific link is currently supported by **0 clinical trials and 0 publications** — the score rests on knowledge-graph proximity, not direct evidence. Two lower-ranked predictions from the same model run (open-angle glaucoma entities) are, in effect, re-discoveries of the drug's already-confirmed indication, backed by **20 publications** including multiple Phase-equivalent RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no license on file); literature indicates an established real-world use as a topical β-blocker for open-angle glaucoma / ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature retrieved for this specific term) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, drug-record-level mechanism-of-action data is flagged as a gap (DG002) in this pack. However, the model's own rationale and the supporting literature converge on a clear pharmacological story: Levobunolol is a potent, non-selective β-adrenoceptor antagonist that acts on β2 receptors in the ciliary body epithelium, suppressing cAMP-mediated aqueous humor production and thereby lowering intraocular pressure (IOP). This is the textbook mechanism by which topical β-blockers treat glaucoma, and it is directly documented across the literature retrieved for the closely related terms "glaucoma 1, open angle" and "open angle glaucoma" (see below).

Primary Hereditary Glaucoma is, ontologically, closely related to — and in many knowledge graphs overlaps with — open-angle glaucoma, often linked through shared gene loci (e.g., *MYOC*/*GLC1A*). TxGNN's very high score (0.9998) for this term most likely reflects that graph proximity rather than an independent, disease-specific efficacy signal: no clinical trials or publications targeting hereditary/congenital glaucoma populations were retrieved for this drug.

Mechanistically, IOP-lowering therapy could plausibly apply to hereditary glaucoma as well, since elevated IOP is a shared pathological feature. However, hereditary and juvenile-onset glaucomas frequently involve structural angle abnormalities and are often managed primarily with surgery, with medical IOP-lowering therapy used adjunctively at best. This is an important caveat: the prediction is mechanistically plausible but clinically unverified for this specific subtype, which is why it is scored L5 (model prediction only) rather than benefiting from the strong evidence base that exists for the drug's established open-angle glaucoma use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(No clinical trial or ICTRP records were found for Levobunolol in "primary hereditary glaucoma," nor in the two related open-angle glaucoma terms in this evidence pack.)*

---

## Literature Evidence

Currently no related literature available for Primary Hereditary Glaucoma specifically.

**Note — supporting evidence exists, but for a related (already-established) indication, not the novel prediction above.** The same TxGNN run also ranked "glaucoma 1, open angle" (score 99.58%, rank #2) and "open angle glaucoma" (score 99.46%, rank #3) very highly, each reaching **Evidence Level L1** on the strength of 20 retrieved publications (largely overlapping between the two terms). These are not new-use hypotheses — they document Levobunolol's long-confirmed role as a standard glaucoma therapy. Selected highlights:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic Review / Network Meta-analysis | Ophthalmology | Comparative effectiveness ranking of first-line POAG medications, including β-blockers |
| [2664628](https://pubmed.ncbi.nlm.nih.gov/2664628/) | 1989 | RCT (4-yr, multicenter, double-masked) | Ophthalmology | 391 patients; levobunolol 0.5%/1% vs timolol 0.5% — sustained IOP reduction of ~7 mmHg over 4 years, comparable efficacy |
| [3881032](https://pubmed.ncbi.nlm.nih.gov/3881032/) | 1985 | RCT | Am J Ophthalmol | 162 patients, up to 15 months; levobunolol reduced IOP by 8–8.2 mmHg, no significant difference vs timolol |
| [2653592](https://pubmed.ncbi.nlm.nih.gov/2653592/) | 1989 | RCT | Can J Ophthalmol | Once-daily levobunolol controlled IOP in 78% of patients vs 89% with timolol over 3 months |
| [33397657](https://pubmed.ncbi.nlm.nih.gov/33397657/) | 2022 | Systematic Review / Network Meta-analysis | Br J Ophthalmol | Comparative efficacy of newer PGA (latanoprostene bunod) vs other agents including β-blockers for IOP lowering |
| [3883971](https://pubmed.ncbi.nlm.nih.gov/3883971/) | 1985 | RCT (3-month, double-masked) | Arch Ophthalmol | 42 patients; both levobunolol concentrations significantly reduced IOP vs vehicle |
| [3881033](https://pubmed.ncbi.nlm.nih.gov/3881033/) | 1985 | Dose-ranging RCT | Am J Ophthalmol | Titration study establishing minimum effective levobunolol concentration for IOP control |
| [2892662](https://pubmed.ncbi.nlm.nih.gov/2892662/) | 1987 | Review (pharmacology) | Drugs | Comprehensive review of levobunolol pharmacodynamics/kinetics; ~30% IOP reduction, controlled in 50–85% of patients |
| [40261315](https://pubmed.ncbi.nlm.nih.gov/40261315/) | 2025 | Treatment guideline review | The Medical Letter | Current review of drug classes for open-angle glaucoma |
| [8773166](https://pubmed.ncbi.nlm.nih.gov/8773166/) | 1996 | Review (comparative) | Ann Pharmacother | Comparison of systemic adverse effects, tolerability, and cost among ocular β-blockers |

---

## US Market Information

No licenses/NDAs are on file for this drug in the current evidence pack (`total_licenses = 0`); market status is recorded as **Not Marketed**. No product name, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this pack. Note DG001 — TFDA label warnings/contraindications — is marked **Blocking**: without it, a formal S1 safety pre-assessment cannot proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The headline prediction — Levobunolol for Primary Hereditary Glaucoma — carries an extremely high TxGNN score but zero direct clinical trial or literature support (L5), and the mechanistic case relies on ontological overlap with open-angle glaucoma rather than evidence specific to hereditary/congenital glaucoma populations, where surgical management often predominates. The strong L1 evidence in this pack belongs to closely related but distinct terms (open-angle glaucoma) that reflect the drug's already-established use rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/US label warnings and contraindications before any safety pre-assessment can begin.
- Resolve DG002: confirm formal DrugBank/FDA-label mechanism-of-action text to support a rigorous mechanistic-relevance analysis.
- Targeted literature/clinical search specifically for "hereditary," "congenital," or "juvenile" glaucoma populations to test whether the TxGNN signal reflects real disease-specific data or pure ontology overlap with open-angle glaucoma.
- Clarify market/regulatory status (drug is currently unmarketed per this pack) before considering any development or label-expansion pathway.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

