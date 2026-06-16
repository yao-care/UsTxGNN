---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 546
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Codeine: From Opioid Analgesia to Nasal Cavity Disease

## One-Sentence Summary

Codeine (DB00318) is a well-established mu-opioid receptor agonist widely used as an analgesic and antitussive, though formal indication data was not captured in this Evidence Pack.
The TxGNN model predicts it may have activity in **Nasal Cavity Disease** (score: 99.93%), with **0 clinical trials** and **2 publications** retrieved — however, both publications describe codeine as a *cause* of nasal pathology, not a treatment.
This pattern repeats across all four predicted indications and represents a likely **directionality error** in the knowledge graph, warranting a **Hold** recommendation across the board.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal regulatory record in this dataset; codeine is widely established as an opioid analgesic and antitussive |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Not captured (0 regulatory licenses retrieved) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, codeine is a prodrug metabolized by CYP2D6 to morphine, acting primarily as a mu-opioid receptor (MOR) agonist. Its established clinical uses include analgesia, cough suppression, and management of diarrhea — all mediated via central and peripheral opioid receptors.

The TxGNN model likely established a link between codeine and nasal cavity disease because the knowledge graph contains a high density of co-occurrence between codeine and nasal pathology. However, reviewing the two retrieved publications reveals a classic **directionality error**: both describe codeine (or related opioids) as the *cause* of nasal injury. One case series documents intranasal abuse of hydrocodone-acetaminophen leading to mucosal necrosis; the other reports a rhinolith formed around an "opioma" — a foreign body composed of codeine and opium. Neither provides any evidence of a therapeutic effect on nasal cavity disease.

In short, the knowledge graph connection reflects "codeine → nasal disease" (harm pathway), whereas a valid drug repurposing hypothesis requires "codeine → treats nasal disease" (therapeutic pathway). These two relationships are fundamentally different, and the model cannot distinguish between them at the prediction stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Codeine in Nasal Cavity Disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case Report | The Laryngoscope | Intranasal abuse of hydrocodone-acetaminophen (crushing and snorting tablets) leads to mucosal necrosis of the nasal cavity and pharynx — codeine-class opioid as the *cause* of disease, not treatment |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case Report | Ear, Nose, & Throat Journal | Rhinolithiasis formed around an impacted "opioma" (hardened codeine + opium foreign body) causing nasal obstruction and purulent rhinorrhea — opioid substance as a *mechanical cause* of nasal pathology |

> ⚠️ **Critical Note:** Both publications document codeine/opioids as etiological agents of nasal pathology, not as therapeutic interventions. The high TxGNN score almost certainly reflects knowledge graph co-occurrence of codeine with nasal disease in an adverse/causal context — a directionality error rather than a therapeutic signal.

---

## US Market Information

No regulatory license records were retrieved for Codeine in this dataset (0 licenses; query returned no results). This is likely a data collection gap rather than reflecting the actual US market status. Codeine is known to be available in the United States in various combination products (e.g., codeine-acetaminophen, codeine-containing cough preparations) as well as Schedule II single-entity formulations.

Please refer to the FDA Orange Book or DailyMed for current authorization details.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Known Safety Concern (from general pharmacological knowledge, not this dataset):** Codeine carries an FDA Black Box Warning for respiratory depression, particularly in CYP2D6 ultra-metabolizers who convert codeine to morphine at an accelerated rate. This risk is especially severe in children and post-tonsillectomy/adenoidectomy patients. Any repurposing investigation must account for this population-specific safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications for Codeine share the same fundamental problem: the knowledge graph connection reflects codeine as a *cause or confounder* rather than a *therapeutic agent* for the predicted disease. This constitutes a systemic directionality error across the entire prediction set, making none of the four candidates suitable for progression.

| Predicted Indication | Why It Fails |
|---------------------|-------------|
| Nasal Cavity Disease | Both publications show opioid-induced nasal necrosis; reverse causality |
| Acute Laryngopharyngitis | Zero evidence; antitussive effect is an *existing* use, not repurposing |
| Trigeminal Autonomic Cephalalgia | 5 case reports all document opioid use as patient background, not as treatment; EHF/AHS guidelines explicitly recommend against opioids in TAC; MOH risk |
| Allergic Urticaria | 15 publications consistently identify codeine as a mast cell degranulator and urticaria *trigger*, not treatment; codeine is used as a positive control in urticaria skin testing |

**To proceed, the following is needed:**

- **Directionality audit of the knowledge graph:** Distinguish "codeine causes disease X" edges from "codeine treats disease X" edges before running future predictions for this drug class
- **MOA data (DG002):** Retrieve full mechanism-of-action profile from DrugBank API to enable proper mechanistic link analysis
- **US regulatory data:** Retrieve actual FDA license records (Orange Book / DailyMed) to complete the market status picture
- **Alternative indication search:** If repurposing potential is desired for codeine, consider redirecting the analysis toward indications where opioid receptors play a clearly *therapeutic* (not harmful) mechanistic role — and focus on indications beyond codeine's already-approved uses (analgesia, antitussive, antidiarrheal)
- **Safety framework:** Any future candidate should pre-specify a CYP2D6 genotyping strategy and respiratory monitoring plan given the Black Box Warning profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

