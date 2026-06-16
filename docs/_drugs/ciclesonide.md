---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 528
evidence_level: L5
indication_count: 6
---

# Ciclesonide
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

Using the `txgnn-pipeline` skill to guide the report structure, and now generating the evaluation report from the Evidence Pack.

---

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled/intranasal corticosteroid (ICS) globally approved for asthma maintenance and allergic rhinitis, though it currently has no registered products in Taiwan.
The TxGNN model predicts it may be effective for **Atopic Eczema**, based on its glucocorticoid receptor (GR) agonism overlapping with the Th2-driven inflammatory pathway central to this condition.
However, **no clinical trials and no publications** have been identified to support this specific pairing — this prediction is entirely model-driven at this stage (L5 evidence).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / Allergic Rhinitis (global approvals; no Taiwan registration) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (Model prediction only — no clinical studies identified) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this dataset. Based on established pharmacology, ciclesonide is a **pro-drug** activated by tissue esterases into its active metabolite **des-ciclesonide**. Des-ciclesonide is a potent glucocorticoid receptor (GR) agonist that suppresses expression of pro-inflammatory cytokines — particularly **IL-4, IL-13, IL-31, and TNF-α** — by binding to GR in target tissue and blocking NF-κB and AP-1 transcription.

Atopic eczema (atopic dermatitis, AD) is driven by a Th2-skewed immune response, in which IL-4 and IL-13 are the dominant mediators of epidermal barrier dysfunction and chronic inflammation. IL-31 is the primary itch-signalling cytokine in AD. This mechanistic overlap is direct and substantial — suppressing precisely the cytokines that drive AD pathology is the same mechanism by which corticosteroids exert their effect on respiratory inflammation. As a drug class, **topical corticosteroids (TCS) are the global first-line standard of care for AD**, making the TxGNN model's cross-disease prediction mechanistically coherent.

The critical practical barrier, however, is **route of administration**. Ciclesonide currently exists only as an inhaled metered-dose inhaler (MDI) and intranasal spray. There is no approved topical skin formulation. While skin esterases are capable of activating ciclesonide prodrug in theory, this has not been demonstrated in a dermatological delivery system. Until a topical formulation is validated, the mechanistic link — though strong on paper — cannot be translated into clinical practice.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on adjacent predictions:** While the top indication (atopic eczema) has no captured evidence, a closely related prediction — **bronchitis (rank 4)** — has one supporting guideline (PMID [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/), Finnish COPD guideline, 2015), consistent with ciclesonide's known role as an approved asthma ICS and the mechanistic overlap with chronic airway inflammation. Additionally, **contact dermatitis (rank 5)** has one captured case report (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), 2012) — notably a **negative safety signal**: a patient sensitised to budesonide showed cross-reactivity with ciclesonide on patch testing, suggesting ciclesonide may itself trigger corticosteroid contact allergy in sensitised individuals.

---

## Taiwan Market Information

Ciclesonide currently has no registered products in Taiwan. No license information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Additional signal from adjacent evidence:** PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) (Contact Dermatitis, 2012) documents a case of **systemic allergic dermatitis caused by inhaled budesonide with positive patch test cross-reactivity to ciclesonide**. This is relevant if ciclesonide is considered for any dermatological indication — patients with prior corticosteroid sensitisation (Group B corticosteroids including budesonide) should be considered at risk for cross-reaction. This is a clinically important safety flag that distinguishes ciclesonide from other TCS options in AD.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for ciclesonide in atopic eczema is pharmacologically sound — GR agonism suppressing Th2/IL-4/IL-13/IL-31 inflammation is precisely the target in AD — but no clinical trials, observational studies, or publications have been identified to validate this application. Critically, no topical skin formulation exists, which is a prerequisite for dermatological use. The existing literature also raises a cross-reactivity safety concern in corticosteroid-sensitised patients.

**To proceed, the following is needed:**

- **Formulation feasibility study**: Assess whether a topical des-ciclesonide or ciclesonide cream/ointment can be developed with adequate skin penetration and local activation
- **Preclinical evidence**: In vitro and in vivo (AD mouse model) studies demonstrating anti-inflammatory efficacy via topical delivery
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB01410) to complete mechanistic linkage analysis
- **Safety profiling**: Obtain Taiwan (and US FDA) package insert data; document corticosteroid cross-reactivity class membership to assess dermatitis sensitisation risk
- **Patch test sensitivity screen**: If clinical development proceeds, include corticosteroid patch test panel screening as an eligibility criterion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

