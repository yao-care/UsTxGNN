---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 612
evidence_level: L5
indication_count: 1
---

# Diphenhydramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diphenhydramine: From Allergic Conditions to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1-antihistamine traditionally associated with allergic symptom relief (itching, tearing, mild allergic conjunctivitis).
The TxGNN model predicts it may be effective for **Rosacea Conjunctivitis**,
but this direction is currently supported by **0 clinical trials** and **0 publications**, making it a pure model-driven hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no approved license on file); mechanistic notes describe diphenhydramine as a first-generation H1-antihistamine typically used for allergic symptom relief |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for diphenhydramine is not available in this evidence pack. Based on the mechanistic notes accompanying this prediction, diphenhydramine is a first-generation H1 histamine receptor antagonist with anticholinergic, antipruritic, and mild anti-inflammatory activity, and it is clinically used for symptomatic relief of allergic conjunctivitis (itching, tearing).

Rosacea conjunctivitis (ocular rosacea), however, is driven by a different set of pathological mechanisms: meibomian gland dysfunction leading to tear film instability, neurovascular dysregulation causing chronic inflammation and vasodilation, and Demodex mite proliferation with overactivation of innate immune pathways (TLR2, cathelicidin/LL-37). These processes are not primarily histamine-mediated Type I hypersensitivity reactions.

As a result, the overlap between diphenhydramine's H1-antagonist mechanism and rosacea's core pathophysiology is limited to symptom-level features (photophobia, itching/discomfort), rather than the disease-specific pathways (cathelicidin signaling, TLR2 activation, vascular reactivity) that drive rosacea. The very high TxGNN score (99.2%) should be interpreted cautiously: knowledge-graph—based scores of this kind can arise from frequent co-occurrence of related node types (e.g., "antihistamine" and "conjunctivitis") rather than disease-specific mechanistic evidence, raising the possibility of a false positive. This uncertainty is compounded by the absence of confirmed original indication data and MOA data for this drug, as well as its "not marketed" status in the reference market.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Diphenhydramine currently has no approved license or authorization on file in the reference market (market status: **Not Marketed**, 0 licenses). No product/dosage-form/indication records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN knowledge-graph score (L5 evidence) with no supporting clinical trials or literature, and the proposed mechanistic link only partially overlaps with rosacea's actual pathophysiology. Combined with the drug's unmarketed status and missing MOA/label data, there is insufficient evidence to advance beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA/label-equivalent data confirming diphenhydramine's approved indications, warnings, and contraindications (currently a blocking data gap)
- Verified mechanism of action (MOA) data from DrugBank or another authoritative source
- Preclinical or mechanistic studies directly linking H1-antihistamine activity to rosacea-specific pathways (cathelicidin/LL-37, TLR2, Demodex-related inflammation)
- Any case reports, observational studies, or exploratory trials evaluating antihistamines in ocular rosacea
- Reassessment of the TxGNN score against a specificity/false-positive check for this drug–disease pair before any further development steps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

