---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 483
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an Integrase Strand Transfer Inhibitor (INSTI) class antiretroviral agent, approved in multiple countries (e.g., US, EU) for HIV-1 treatment and pre-exposure prophylaxis (PrEP), but currently **not marketed in Taiwan**.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
with **0 clinical trials** and **0 publications** currently supporting this direction — this prediction remains at the pure computational hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (treatment & PrEP); no Taiwan TFDA license on record |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on publicly known information, Cabotegravir belongs to the Integrase Strand Transfer Inhibitor (INSTI) class of antiretroviral drugs. It works by blocking the HIV-1 integrase enzyme from inserting viral DNA into the host cell genome, thereby halting viral replication. Its long-acting injectable formulation (Cabenuva, combined with rilpivirine) has been approved in the US and EU.

The proposed mechanistic bridge to rheumatoid arthritis (RA) rests on the **endogenous retroviral element (ERV) hypothesis**: the human genome harbors a large number of endogenous retroviral sequences (ERV/LINE-1), some of which retain residual integrase activity. Certain ERV elements have been hypothesized to contribute to autoimmune conditions — including RA — by generating self-antigens and triggering interferon signaling. In theory, an INSTI such as Cabotegravir could suppress ERV transposition activity, thereby reducing autoantigen exposure and attenuating inflammatory cascades.

However, this mechanistic hypothesis remains entirely speculative. There is currently no in vitro, animal model, or clinical data specifically linking Cabotegravir to RA pathology. The TxGNN high score most likely reflects network topology within the knowledge graph (shared disease-node neighbors) rather than validated mechanistic similarity. The remaining four predicted indications (sclerosing cholangitis, bronchitis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, severe nonproliferative diabetic retinopathy) similarly lack any supporting evidence and are likely network artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cabotegravir in rheumatoid arthritis, sclerosing cholangitis, bronchitis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, or severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for any of the five predicted indications.

---

## Taiwan Market Information

Cabotegravir has no Taiwan TFDA marketing authorizations on record. The drug is therefore not currently available through official regulatory channels in Taiwan.

For reference, Cabotegravir is marketed internationally under the following brand names:
- **Vocabria** (oral tablet, GlaxoSmithKline/ViiV Healthcare) — US/EU approved for HIV-1 treatment
- **Cabenuva** (long-acting injectable, combined with rilpivirine) — US/EU approved for HIV-1 treatment
- **Apretude** (long-acting injectable) — US approved for HIV-1 PrEP

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan TFDA warnings, contraindications, or drug interaction data were retrievable for this drug at the time of this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications score at Evidence Level L5 — pure TxGNN model output with zero supporting clinical trials or literature. The most mechanistically plausible prediction (rheumatoid arthritis via the ERV/INSTI hypothesis) remains entirely theoretical and has not been tested in any experimental system. Proceeding to any development activity without foundational evidence would not be scientifically or commercially justifiable.

**To proceed, the following is needed:**

- **MOA data verification**: Retrieve full Cabotegravir pharmacology from DrugBank API or primary literature to confirm the ERV-INSTI hypothesis is even biochemically plausible
- **Preclinical mechanistic studies**: In vitro or animal model data demonstrating that Cabotegravir modulates ERV activity, interferon signaling, or RA-relevant inflammatory pathways (e.g., TNF-α, IL-6, anti-CCP)
- **Comparative ERV literature review**: Survey existing INSTI class studies (dolutegravir, bictegravir) for any incidental autoimmune or inflammatory findings that could inform hypothesis generation
- **Taiwan regulatory pathway assessment**: Since Cabotegravir is not marketed in Taiwan, any local repurposing study would need to address import, compassionate use, or IND filing frameworks
- **Safety data acquisition**: Obtain Taiwan TFDA package insert equivalent and DDI profile before any safety evaluation can begin
- **Evidence re-evaluation trigger**: If ≥1 peer-reviewed publication or registered clinical trial emerges linking any INSTI to RA or autoimmune outcomes, escalate to S1 safety pre-screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

