---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 590
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Inflammatory & Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid with established anti-inflammatory and immunosuppressive properties, used across a broad range of inflammatory and autoimmune conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **no dedicated clinical trials registered** but **20 publications** — including 1 RCT and 1 network meta-analysis — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current database (dexamethasone is a well-established corticosteroid for inflammatory and autoimmune conditions) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | Not found in database (query returned 0 results; this is a known database gap — dexamethasone is widely marketed in the US) |
| Number of NDAs | 0 (database gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dexamethasone is a synthetic glucocorticoid with approximately 25–30 times the anti-inflammatory potency of cortisone. It acts via intracellular glucocorticoid receptors (GR) to suppress NF-κB signaling, inhibit T-cell activation, and downregulate key pro-inflammatory cytokines including IFN-γ, IL-1β, and TNF-α. This broad immunosuppressive profile is what makes the TxGNN prediction particularly compelling.

Alopecia areata (AA) is an autoimmune condition driven by CD8+ cytotoxic T cells that breach the immune privilege of the hair follicle. In a healthy follicle, the immune privilege zone shields hair follicle antigens from immune surveillance. In AA, this protection collapses, and the resulting cytokine storm — dominated by IFN-γ — drives progressive, non-scarring hair loss. Dexamethasone directly addresses this mechanism: by suppressing T-cell activity and restoring immune privilege through cytokine downregulation, it targets the core pathophysiology of AA rather than just its symptoms.

The "oral mini-pulse" strategy — 2.5–5 mg on two consecutive days per week — has been specifically developed for AA management to strike a balance between maintaining immunosuppressive efficacy and avoiding hypothalamic–pituitary–adrenal (HPA) axis suppression, the principal risk of chronic corticosteroid use. This practical pharmacological adaptation, supported by multiple published cohort studies and one prospective RCT, makes dexamethasone an accessible and mechanistically well-justified treatment for moderate-to-severe AA, particularly in patients who cannot access or are ineligible for JAK inhibitors.

---

## Clinical Trial Evidence

A ClinicalTrials.gov search for dexamethasone in the context of alopecia areata returned 14 results. Upon review, all identified trials involve dexamethasone as a supportive or co-medication in oncology settings (anti-emetic premedication, steroid component of cancer drug regimens, or supportive care for fatigue), not as a primary treatment for alopecia areata. No dedicated registered trial directly testing dexamethasone for alopecia areata was identified.

**Currently no directly relevant clinical trials registered for dexamethasone in alopecia areata.**

> This does not diminish the overall evidence base. The therapeutic use of dexamethasone in AA is well-documented in the published literature, including one prospective RCT (see Literature Evidence below). The absence of a registered trial likely reflects the historical use of dexamethasone as an off-label treatment, predating the modern era of mandatory trial registration.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Open-label RCT (30 children, severe non-progressive AA) comparing dexamethasone oral mini-pulse vs. DPCP contact sensitization; primary endpoint: effectiveness and safety in patients under 18 years |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Network Meta-Analysis | Archives of Dermatological Research | Systematic review and NMA comparing systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA (SALT ≥50%); positions dexamethasone within the evidence-based treatment hierarchy |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world prospective cohort assessing effectiveness, safety, and predictors of successful response to dexamethasone oral mini-pulse in AA patients |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Cohort | European Journal of Dermatology | Retrospective review of 19 patients with severe AA: stepwise combination of topical corticosteroids with baricitinib, followed by pulse dexamethasone rescue in non-responders |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Cohort | Dermatologic Therapy | Prospective study of 73 children with severe AA (>30% scalp area); compared 1-day vs. 3-day monthly IV dexamethasone pulses; good response defined as ≥50% hair regrowth |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case Series | Journal of Dermatological Treatment | Durable remission of severe AA with dexamethasone oral mini-pulse in patients ineligible for JAK inhibitors; includes focused literature review of corticosteroid pulse regimens |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Systematic Review | Dermatologic Therapy | Multicentric analysis of oral dexamethasone mini-pulse for moderate-to-severe AA across European centers; contextualizes the role of dexamethasone alongside recently FDA-approved baricitinib |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Literature review of pulse dose corticosteroid therapy dosing regimens, administration protocols, and side effect profiles specifically in pediatric AA |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort | Dermatologic Therapy | Long-term follow-up (median 96 months) of 65 children with AA affecting >30% scalp treated with monthly oral dexamethasone pulse; evaluated durable response rates across AA subtypes including totalis/universalis |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Clinical Study | Journal of Dermatology | Foundational study of 30 patients with widespread AA treated with twice-weekly 5 mg dexamethasone oral pulse; assessed terminal hair regrowth at minimum 12-week follow-up |

---

## US Market Information

The current database query returned no US FDA approval records for dexamethasone (0 licenses found). This is a system data gap — dexamethasone is one of the most widely used corticosteroids in the world and is available in the US under multiple brand names and formulations (oral tablets, injectable solutions, ophthalmic preparations, and others). It is included in the WHO Model List of Essential Medicines.

US prescribers should consult the current FDA-approved labeling for authoritative indication, dosing, and safety information. Resolution of this database gap is recommended before proceeding to clinical or regulatory review.

---

## Safety Considerations

Please refer to the package insert for complete safety information.

Relevant class-level considerations for the alopecia areata use case:

- **HPA axis suppression**: The primary concern with systemic dexamethasone. The twice-weekly oral mini-pulse strategy is specifically designed to reduce (but not eliminate) this risk. Long-term monitoring of cortisol suppression is advisable.
- **Immunosuppression**: Risk of opportunistic infections with prolonged systemic immunosuppression; particularly relevant in pediatric populations.
- **Metabolic effects**: Hyperglycemia, weight gain, and fluid retention are dose- and duration-dependent class effects.
- **Bone effects**: Long-term corticosteroid use carries risk of osteopenia/osteoporosis; calcium and vitamin D supplementation may be warranted.
- **Ocular effects**: Prolonged use associated with posterior subcapsular cataracts and elevated intraocular pressure.
- **Pediatric-specific**: Growth suppression is a concern in children — a consideration given that a significant portion of the AA evidence base involves pediatric patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexamethasone's glucocorticoid mechanism is mechanistically precise for alopecia areata — directly targeting the CD8+ T-cell/IFN-γ axis that drives follicular immune privilege collapse. The evidence base includes 1 RCT, 1 network meta-analysis, and multiple prospective cohort studies, justifying an L2 evidence level and supporting careful clinical progression.

**To proceed, the following is needed:**

- **Resolve the database gap**: Retrieve and verify US FDA approval records and current package insert for dexamethasone to complete the regulatory picture
- **Obtain MOA documentation**: Pull formal pharmacology data from DrugBank (DB01234) to support mechanism-of-action narrative in any regulatory filing
- **Head-to-head trial against JAK inhibitors**: JAK inhibitors (baricitinib, ritlecitinib) are now FDA-approved for AA and represent the current standard of care for severe disease; a direct comparative trial is needed to establish dexamethasone's positioning
- **Establish standardized dosing protocol**: The optimal regimen (mini-pulse oral vs. IV pulse vs. combination with topical corticosteroids) remains undefined; protocol harmonization is required
- **Long-term safety data in AA population**: Existing studies are predominantly short-to-medium term; data on relapse rates, HPA axis recovery, and cumulative side effects after treatment cessation are limited
- **Pediatric-specific safety monitoring plan**: Much of the current evidence is in children; formalized safety thresholds for pediatric use should be specified before any clinical implementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

