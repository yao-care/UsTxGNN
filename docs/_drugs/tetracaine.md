---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Tetracaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is an ester-type local anesthetic with decades of clinical use in surface, spinal, and ophthalmic anesthesia, working by blocking voltage-gated sodium channels to prevent nerve signal conduction.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans (ACA)**, a late-stage Lyme disease skin manifestation,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia (surface, spinal, ophthalmic) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Market Status | Not marketed (TFDA records: 未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the sources queried. Based on well-established pharmacology, tetracaine is an ester-type local anesthetic. It reversibly blocks voltage-gated sodium channels (Nav channels) on sensory neurons, preventing action potential initiation and propagation. This mechanism underpins its clinical utility in surface anesthesia (eye drops, mucous membrane application), spinal anesthesia, and topical pain relief.

Acrodermatitis chronica atrophicans (ACA) is a rare, late-stage cutaneous manifestation of Lyme disease caused by persistent *Borrelia burgdorferi* infection. The disease progresses through an inflammatory phase (edema, bluish-red discoloration) into an atrophic phase characterized by paper-thin skin and collagen loss. First-line treatment is antibiotic therapy — primarily doxycycline for 28–30 days. The direct mechanistic connection between sodium channel blockade and bacterial clearance or fibrosis reversal is not established.

Local anesthetics as a class do exhibit secondary anti-inflammatory properties in preclinical models — for example, inhibiting leukocyte activation and reducing pro-inflammatory cytokine release — which could theoretically dampen the chronic inflammation component of ACA. However, the TxGNN score of 99.93% here most likely reflects network-level proximity within skin disease subgraphs rather than a pharmacologically actionable mechanism. The algorithm may be picking up on tetracaine's frequent co-occurrence with dermatological conditions in the knowledge graph, without distinguishing anesthetic use from therapeutic use. This prediction should be treated with caution until a biologically plausible pathway is identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tetracaine in acrodermatitis chronica atrophicans.

---

## Literature Evidence

Currently no related literature available for Tetracaine in acrodermatitis chronica atrophicans.

---

## US Market Information

No authorized products found. Tetracaine returned 0 records in the TFDA registry query (query date: 2026-03-25). No license table available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical Safety Note from Broader Evidence Review:** Although safety data could not be retrieved for this Evidence Pack (DG001: package insert warnings not obtained; DG002: MOA not available), the literature collected under the cauda equina syndrome indication (Rank 8, 9 publications) documents a well-recognized serious adverse event: high-concentration intrathecal tetracaine administration can cause direct neurotoxicity and irreversible cauda equina injury. This is an established risk when tetracaine is administered intrathecally at excessive doses or with maldistribution — it is an adverse effect to monitor, not a therapeutic target. Any repurposing pathway must account for this neurotoxicity profile when selecting route of administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.93%) to the Tetracaine–ACA pair, but the Evidence Pack contains zero supporting clinical trials and zero relevant publications, placing this at Evidence Level L5. The mechanistic link between sodium channel blockade and *Borrelia*-driven chronic skin inflammation and fibrosis is not established, and the repurposing rationale provided suggests the high score reflects skin disease network proximity rather than direct pharmacological relevance.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank API to assess whether any secondary pharmacological activities (e.g., anti-inflammatory, immunomodulatory) are documented (DG002 remediation)
- Download and parse TFDA package insert PDF to obtain warnings and contraindications (DG001 remediation)
- Conduct a targeted literature review on local anesthetic anti-inflammatory effects in infectious dermatology and *Borrelia*-associated skin pathology
- If a plausible biological mechanism is identified, commission a preclinical feasibility study (e.g., *Borrelia burgdorferi* co-culture model with tetracaine exposure) before any clinical proposal
- Consider whether a topical administration route (the safest pharmacokinetic approach for this skin condition) would achieve sufficient tissue concentrations to exert any anti-inflammatory effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

