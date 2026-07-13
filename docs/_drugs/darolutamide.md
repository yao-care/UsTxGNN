---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 3
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is a non-steroidal androgen receptor (AR) antagonist approved for prostate cancer treatment in multiple jurisdictions.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
however **no clinical trials or published literature** currently support this direction, and mechanistic analysis reveals a fundamental logical break in the proposed pathway.
All three top predictions carry a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Taiwan regulatory data (not marketed in Taiwan); darolutamide is approved for prostate cancer in other jurisdictions |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on the mechanistic context provided in the repurposing rationale, darolutamide is an androgen receptor (AR) antagonist — its class mechanism involves blocking AR signaling, which is central to prostate cancer progression.

The theoretical bridge to HoFH relies on a two-step pathway: androgens (particularly DHT) are known to upregulate PCSK9 expression, which in turn suppresses hepatic LDL receptor (LDL-R) density. Blocking AR with darolutamide could theoretically relieve this PCSK9-mediated suppression, increasing LDL-R expression and improving LDL clearance.

**However, this pathway contains a fundamental logical break for HoFH specifically.** HoFH is caused by biallelic loss-of-function mutations in the *LDLR* gene (or variants in *APOB*, *PCSK9*, or *LDLRAP1*). Even if darolutamide successfully upregulated LDL-R transcription via PCSK9 derepression, functional receptors would remain absent due to the underlying genetic defect — lipoprotein clearance cannot be restored. The TxGNN high score (0.991) most likely reflects non-specific knowledge graph node neighborhood similarity (shared metabolic pathway nodes) rather than a genuine therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for darolutamide in homozygous familial hypercholesterolemia.

---

## Literature Evidence

Currently no related literature available for darolutamide in homozygous familial hypercholesterolemia.

---

## Taiwan Market Information

Darolutamide has **no Taiwan FDA authorizations** at the time of this report. The drug is not marketed in Taiwan.

| Item | Status |
|------|--------|
| Market Status | Not marketed |
| Total Licenses | 0 |
| Available Dosage Forms | — |

---

## Cytotoxicity

Darolutamide is an androgen receptor antagonist used in oncology (prostate cancer). It is classified as a targeted anticancer therapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Non-steroidal androgen receptor antagonist (not conventional cytotoxic) |
| Myelosuppression Risk | Low (AR antagonists do not directly suppress bone marrow) |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard oral oncology drug handling; cytotoxic handling precautions not typically required for AR antagonists, but confirm per institutional policy |

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan FDA label data, no drug interaction records, and no key warnings or contraindications data are available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (HoFH) carries zero supporting clinical or literature evidence (L5), and the proposed mechanistic pathway has a clearly identified logical break — HoFH patients lack functional LDL receptors due to biallelic *LDLR* mutations, rendering the AR → PCSK9 → LDL-R derepression hypothesis therapeutically inert. The remaining two predictions (multiple endocrine neoplasia at L4, HIV infectious disease at L5) are similarly unsupported and, in the case of HIV, mechanistically counterindicated. The high TxGNN scores across all three indications likely reflect graph topology artifacts rather than pharmacological relevance.

**To proceed, the following is needed:**

- **Mechanism of action data (MOA)**: Retrieve full DrugBank entry (DB12941) to confirm receptor binding profile, pharmacokinetics, and any off-target activities
- **Taiwan/FDA label review**: Download and parse the originator package insert (Nubeqa®) for approved indications, warnings, contraindications, and DDI profile
- **Preclinical data search**: Conduct targeted literature search for any *in vitro* or *in vivo* studies examining darolutamide effects on LDL metabolism, PCSK9 expression, or lipid profiles before escalating to clinical feasibility assessment
- **Biomarker-stratified hypothesis**: If AR expression has been documented in HoFH-adjacent lipid disorders (e.g., heterozygous FH or polygenic hypercholesterolemia without LDLR null mutation), a narrower biomarker-selected subpopulation hypothesis could be re-evaluated — but this would require new mechanistic studies, not just evidence retrieval
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

