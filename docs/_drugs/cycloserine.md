---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 557
evidence_level: L5
indication_count: 7
---

# Cycloserine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cycloserine: From Tuberculosis (MDR-TB) to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a broad-spectrum antibiotic classically used as a second-line agent for multidrug-resistant tuberculosis (MDR-TB).
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**,
though currently **no clinical trials or publications** directly support this direction — the prediction rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant tuberculosis (MDR-TB) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (0 licenses) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on what is known, Cycloserine is a broad-spectrum antibiotic that inhibits bacterial cell wall biosynthesis by blocking D-alanine racemase and D-alanyl-D-alanine synthetase — enzymes essential for peptidoglycan cross-linking. In its D-isomer form (D-cycloserine), it additionally functions as a partial agonist at the glycine co-agonist site of NMDA receptors, a property that has driven considerable research into its psychoneurological applications.

The predicted mechanistic link to IBS follows three speculative pathways: (1) gut microbiome remodeling through its antibacterial activity, which could alter the dysbiotic patterns implicated in IBS; (2) modulation of gut motility via enteric nervous system NMDA receptors (notably the NR2B subtype), which regulate intestinal peristalsis; and (3) effects on D-serine and glycine metabolism in intestinal epithelial cells. None of these pathways has been evaluated in preclinical IBS models.

The distance between MDR-TB (its established use) and IBS is substantial. The high TxGNN score most likely reflects structural or network-level associations within the knowledge graph — possibly the NMDA partial agonist property linking cycloserine to neuroenteric signaling nodes — rather than a direct pharmacological rationale supported by data. This prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cycloserine in Irritable Bowel Syndrome.

---

## Literature Evidence

Currently no related literature available for Cycloserine in Irritable Bowel Syndrome.

---

## Market Information

Cycloserine currently has **no registered licenses** with the Taiwan FDA and is **not marketed in Taiwan**.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No licenses on record |

> **Note:** In the United States, Cycloserine is FDA-approved (under brand names such as Seromycin) for pulmonary and extrapulmonary tuberculosis — including MDR-TB — as a second-line agent when primary drugs have failed or are contraindicated. It is also listed for treatment of urinary tract infections caused by susceptible bacteria when conventional therapy has failed.

---

## Safety Considerations

Please refer to the package insert for safety information. No Taiwan FDA package insert data, drug interaction records, or formal warning/contraindication data were available in this evidence pack.

> **Known class-level cautions** (from general pharmacological literature): Cycloserine carries a well-recognized risk of CNS toxicity including seizures, psychosis, anxiety, and peripheral neuropathy, particularly at higher doses or in patients with renal impairment. These toxicity considerations would be highly relevant to any new indication assessment and must be retrieved from the full prescribing information before any development decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (Evidence Level L5) with zero supporting preclinical or clinical evidence. The proposed mechanistic link between Cycloserine and IBS is entirely speculative, and the drug's CNS safety profile introduces significant risk considerations that must be characterized before any repurposing pathway can be evaluated.

**To proceed, the following is needed:**

- **MOA data retrieval**: Query DrugBank API to confirm full mechanism of action, pharmacokinetic properties, and known target profile
- **Safety package**: Download and parse the Taiwan FDA (or US FDA) package insert to extract formal warnings, contraindications, and boxed warnings — currently blocking S1 safety evaluation
- **Preclinical signal search**: Conduct a broader PubMed search covering cycloserine + gut microbiome, enteric nervous system, or NMDA receptor + GI motility to determine if any foundational science exists
- **Indication reranking consideration**: Evidence Pack ranks 4 (Conjunctivitis, L4, 3 publications on Chlamydia trachomatis activity) and 5 (Insomnia, L3, 3 clinical trials including a completed Phase 2/3 for NRX-101) carry substantially stronger evidence bases and may be more viable near-term repurposing candidates than IBS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

