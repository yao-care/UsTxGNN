---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 6
---

# Cetirizine
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

以下是根據 Evidence Pack 生成的完整評估報告：

---

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation, selective H1 receptor antagonist historically established for allergic rhinitis and chronic urticaria treatment.
The TxGNN model predicts it may be effective for **Allergic Urticaria** with an exceptionally high confidence score,
supported by **3 clinical trials** and **18 publications** — with strong direct mechanistic alignment between the drug's pharmacology and the target indication's pathophysiology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / Chronic urticaria (class-established; no US license data on file) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | No US license record found |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, cetirizine is a piperazine derivative and the carboxylated metabolite of hydroxyzine, classified as a second-generation H1 receptor antagonist. It competitively and selectively blocks histamine binding to peripheral H1 receptors, markedly reducing the wheal-and-flare response without the central nervous system depression associated with first-generation agents. Importantly, cetirizine also inhibits histamine release and eosinophil chemotaxis during the late-phase allergic response — conferring anti-inflammatory properties beyond simple receptor blockade.

Allergic urticaria is characterized by IgE-mediated mast cell degranulation triggered by allergen cross-linking, releasing histamine as the primary driver of vascular permeability, pruritus, and characteristic whealing and erythema. The mechanistic link between cetirizine's selective H1 antagonism and the histamine-driven pathophysiology of allergic urticaria is direct and biologically coherent, making TxGNN's near-maximal prediction score scientifically well-founded.

It is worth noting that cetirizine's utility in urticaria is already documented in published literature, meaning this TxGNN prediction largely validates an established pharmacological use rather than uncovering a novel indication. The principal value of this analysis lies in quantifying the evidence base, identifying evidence tiers, and highlighting gaps in the current US regulatory record that would need to be resolved before formal indication support can be claimed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicenter, parallel-group, double-blind pilot RCT comparing IV cetirizine (10 mg) vs. IV diphenhydramine (50 mg) in patients with acute urticaria presenting to emergency departments, urgent care centers, and allergy clinics; most directly relevant evidence for cetirizine in this indication |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomized, double-blind trial evaluating whether adding a short burst of corticosteroid to conventional H1 antihistamine treatment improves outcomes in urticaria; cetirizine serves as the standard background therapy, indirectly affirming its foundational role |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Investigated levocetirizine (cetirizine's pharmacologically active R-enantiomer) on skin-level inflammatory mediators in dermatographism and chronic idiopathic urticaria; terminated early due to insufficient enrollment, providing indirect mechanistic data only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Critical review of clinical evidence on antihistamine up-dosing (up to 4× licensed dose) in chronic spontaneous urticaria; supports stepwise escalation before escalating to biologics such as omalizumab |
| [35593100](https://pubmed.ncbi.nlm.nih.gov/35593100/) | 2022 | Systematic Review / Meta-Analysis | Am J Rhinol Allergy | RCT-level meta-analysis of bilastine (a new-generation H1 antihistamine) in allergic rhinitis and chronic urticaria; confirms class-level H1 antagonist superiority over placebo for urticaria endpoints |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Trial Summary | Allergy | Direct summary of clinical studies with cetirizine specifically in allergic rhinitis and chronic urticaria; establishes efficacy and tolerability profile for the drug |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Comparative PK/PD Study | Clin Pharmacokinet | Comparative pharmacokinetic and pharmacodynamic analysis of desloratadine, fexofenadine, and levocetirizine for allergic rhinitis and chronic idiopathic urticaria; contextualizes the cetirizine class among modern antihistamines |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Comparative Review | Drugs | Comprehensive evaluation of second-generation antihistamines including cetirizine across sedation, anticholinergic burden, and clinical efficacy; positions cetirizine as a benchmark agent in the class |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Narrative Review | Drugs | Foundational pharmacological review of cetirizine; establishes its potent peripheral H1 antagonism, antiallergic properties, and clinical efficacy in chronic urticaria at the standard 10 mg/day dose |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Narrative Review | Drugs | Reappraisal of cetirizine as a long-acting, specific H1 receptor antagonist with eosinophil chemotaxis inhibition; confirms well-tolerated efficacy in chronic idiopathic urticaria in adults |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Narrative Review | Drugs | Comprehensive review of urticaria pathophysiology, causes, and management; positions nonsedating antihistamines (including cetirizine) as the established mainstay for chronic idiopathic urticaria |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Pharmacy-focused efficacy and safety review of first- and newer-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria; reinforces cetirizine's class standing in clinical practice |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | Level 1 evidence for H1 antagonist efficacy in pediatric allergic rhinoconjunctivitis; supports extrapolation of cetirizine utility across adult and pediatric populations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
TxGNN assigns a 99.99% prediction score grounded in direct mechanistic alignment — H1 receptor antagonism precisely counteracts the histamine-driven pathophysiology of allergic urticaria — and the evidence base includes a completed Phase 3 pilot RCT (NCT02023164), multiple systematic reviews, and decades of published clinical literature. The primary barrier to advancement is the absence of US FDA license data in the current Evidence Pack and the lack of formal safety documentation.

**To proceed, the following is needed:**
- Verify actual US FDA approval status: the current data shows 0 NDAs for cetirizine, which likely reflects a data retrieval gap rather than true non-approval (Zyrtec® is a well-known FDA-approved product); confirm and retrieve NDA/ANDA records
- Obtain and review the full US prescribing information, including boxed warnings, contraindications, and drug interaction profile
- Clarify the target indication subtype — acute allergic urticaria vs. chronic spontaneous urticaria — as regulatory pathway, trial design, and evidence requirements differ substantially between subtypes
- Evaluate dose optimization evidence: systematic review (PMID 33030434) supports up-dosing to 4× standard dose in refractory CSU; a dosing strategy should be pre-specified
- Assess pediatric eligibility and any age-stratified efficacy data required for label coverage in children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

