---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 478
evidence_level: L5
indication_count: 6
---

# Buprenorphine
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

# Buprenorphine: From Opioid Use Disorder to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial μ-opioid receptor agonist and κ-opioid receptor antagonist, clinically established for the treatment of opioid use disorder and moderate-to-severe pain.
The TxGNN model predicts it may be relevant for **Acute Intermittent Porphyria (AIP)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid use disorder / Moderate-to-severe pain management |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| US Market Status | Not marketed (0 licenses found in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, buprenorphine is a partial μ-opioid receptor agonist and a κ-opioid receptor antagonist, with additional activity at the nociceptin/ORL-1 receptor. Its clinical efficacy in opioid use disorder and pain management is well-established; the unique "ceiling effect" at high doses gives it a more favorable respiratory safety profile compared to full opioid agonists.

The mechanistic connection to acute intermittent porphyria (AIP) is **indirect and safety-based rather than therapeutic**. AIP is a rare metabolic disorder caused by a deficiency of porphobilinogen deaminase, leading to accumulation of toxic heme precursors (ALA, PBG) in the liver. Many conventional drugs — including most opioids — can trigger AIP attacks by inducing hepatic δ-ALA synthase, the rate-limiting enzyme in heme biosynthesis. Buprenorphine is generally considered **porphyria-safe** because it does not significantly upregulate this enzyme, making it a preferred analgesic choice when AIP patients require pain management.

However, the critical distinction here is between *safe to administer in AIP patients* versus *therapeutic for AIP itself*. The available literature does not demonstrate any direct benefit of buprenorphine on the underlying porphyria pathophysiology. The TxGNN model's high prediction score most likely reflects its capture of this indirect pharmacological safety relationship, rather than a true disease-modifying repurposing signal. This prediction is more accurately categorized as a **research question** than a clinically actionable repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui — The Japanese Journal of Anesthesiology | Anesthetic management of a 40-year-old female with suspected AIP undergoing radical hysterectomy for ovarian malignancy; describes the challenge of selecting safe anesthetic agents in an unconfirmed AIP case, contextualizing buprenorphine as a safer opioid option |

---

## US Market Information

Buprenorphine has 0 licenses recorded in the current dataset (market status: not marketed). This may reflect a data gap — buprenorphine holds multiple FDA approvals in the US under brand names such as Suboxone, Subutex, Buprenex, Butrans, and Sublocade. Verification against the FDA Orange Book is recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All safety fields in this Evidence Pack (key warnings, contraindications, drug-drug interactions) are flagged as data gaps. For a drug with significant abuse potential and respiratory depression risk, obtaining full prescribing information before any clinical development planning is essential.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole available publication (a 1993 Japanese case report) describes safe anesthetic use *in* an AIP patient — not a therapeutic intervention *for* AIP. The TxGNN signal appears to reflect porphyria-safety pharmacology rather than a repurposable therapeutic mechanism; there is no biological rationale or clinical data supporting buprenorphine as a treatment that modifies AIP disease course.

**To proceed, the following is needed:**

- **Clarify the research question**: Is the hypothesis "buprenorphine as the preferred analgesic for managing acute pain episodes in AIP patients" (a safety/management question) or "buprenorphine as a disease-modifying treatment for AIP" (a repurposing question)? These require entirely different development pathways.
- **Obtain full MOA data** from DrugBank API to confirm hepatic enzyme induction profile and cytochrome P450 interactions relevant to AIP.
- **Retrieve package insert warnings and contraindications** (TFDA / FDA) — flagged as a Blocking data gap — before any safety evaluation can proceed.
- **Conduct a focused literature search** specifically on buprenorphine's effect on δ-ALA synthase induction and heme pathway enzymes to assess direct mechanistic plausibility.
- **Assess hepatic safety**: AIP patients often have compromised hepatic function during acute attacks; buprenorphine's hepatic metabolism (CYP3A4) and potential hepatotoxicity risk require specific evaluation in this population.
- **Evaluate orphan drug designation potential**: AIP is a rare disease; if a credible mechanism is identified, FDA Orphan Drug Designation could significantly reduce development barriers.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

