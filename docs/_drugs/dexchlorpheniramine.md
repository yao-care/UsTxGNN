---
layout: default
title: Dexchlorpheniramine
parent: 僅模型預測 (L5)
nav_order: 592
evidence_level: L5
indication_count: 2
---

# Dexchlorpheniramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Dexchlorpheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Dexchlorpheniramine is the active dextrorotatory enantiomer of chlorpheniramine and is pharmacologically classified as a first-generation H1 receptor antagonist, globally established for treating allergic conditions such as allergic rhinitis and urticaria.
The TxGNN model predicts it may be effective for **Allergic Urticaria** (top-ranked indication) and secondarily for **Cold Urticaria**, with **0 clinical trials** and **0 publications** captured in the current evidence pipeline — reflecting a data retrieval gap rather than a clinical evidence void.
The mechanistic rationale is direct and well-supported pharmacologically; however, the absence of pipeline-captured evidence places this at **Evidence Level L5**, warranting targeted literature supplementation before advancing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally used for allergic rhinitis and allergic conditions (first-generation H1 antihistamine) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only; no trials or literature captured in pipeline) |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Approved Licenses | 0 |
| Recommended Decision | Hold — pending targeted evidence supplementation |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (MOA field shows a data gap). Based on established pharmacological knowledge documented in the repurposing rationale, dexchlorpheniramine is the active dextrorotatory enantiomer of chlorpheniramine, classified as a first-generation, competitive H1 receptor antagonist. It binds reversibly to peripheral and central H1 receptors, blocking the downstream effects of histamine release.

The core pathophysiology of allergic urticaria involves IgE-mediated mast cell degranulation, resulting in massive histamine release that activates H1 receptors on dermal blood vessels and sensory nerves — producing vasodilation, increased vascular permeability, wheal-and-flare reactions, and pruritus. H1 receptor antagonists represent the first-line treatment explicitly recommended by the EAACI/GA²LEN urticaria guidelines, making the mechanistic alignment between dexchlorpheniramine and allergic urticaria essentially direct and pharmacologically self-evident.

For cold urticaria (the second-ranked prediction, score 99.61%), the mechanism remains H1-mediated symptom control: cold stimuli trigger abnormal mast cell and basophil degranulation releasing histamine, PAF, and other mediators at the contact site. While cold urticaria may additionally involve non-IgE pathways (e.g., cold-reactive IgM), EAACI cold urticaria guidelines still designate H1 antagonists as the primary symptomatic management option — with second-generation agents preferred but first-generation agents serving as adjuncts in severe episodes. The slightly lower TxGNN score for cold urticaria (99.61% vs. 99.89%) is consistent with this more complex, multi-pathway trigger mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dexchlorpheniramine + allergic urticaria or cold urticaria in ClinicalTrials.gov or ICTRP.

> **Note:** This reflects the scope of the current pipeline query (dexchlorpheniramine-specific searches). Broader searches using the racemic parent compound chlorpheniramine or the therapeutic class (first-generation H1 antihistamines) in urticaria may yield substantial evidence. This is a data pipeline gap, not an absence of clinical evidence in the field.

---

## Literature Evidence

Currently no related literature available for dexchlorpheniramine + allergic urticaria or cold urticaria in PubMed.

> **Note:** Same pipeline scope limitation as above. The PubMed query was limited to "DEXCHLORPHENIRAMINE" as the drug term. Supplemental searches with chlorpheniramine, dexchlorphenamine, or drug-class-level queries (antihistamine + urticaria) are expected to return substantial published literature including RCTs and systematic reviews.

---

## Taiwan Market Information

Dexchlorpheniramine is not registered in Taiwan (市場狀態：未上市). No NDA, license records, or approved indications are on file with the TFDA.

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA package insert warnings, contraindications, or drug interaction data were captured in the current pipeline.

> **Class-level context:** As a first-generation antihistamine, dexchlorpheniramine is generally expected to carry class-typical concerns including sedation (CNS depression), anticholinergic effects (dry mouth, urinary retention, constipation), and additive CNS depression with alcohol or sedatives. Use in elderly patients, those with glaucoma or BPH, and concurrent CNS depressant users warrants caution based on drug-class knowledge. Formal safety data should be sourced from the originator package insert or DrugBank API.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model score is exceptionally high (99.89%) and the mechanistic alignment between dexchlorpheniramine (H1 antagonist) and allergic urticaria (histamine-driven pathology) is pharmacologically direct — this is not a speculative repurposing signal. However, the Evidence Pack currently contains zero clinical trials and zero literature from pipeline-automated searches, placing the evidence level at L5. This reflects a data retrieval limitation (queries were dexchlorpheniramine-specific), not a genuine absence of clinical knowledge. Advancing to formal evaluation requires closing the evidence gap first.

**To proceed, the following is needed:**

- **Targeted literature supplementation:** Re-run PubMed and ClinicalTrials.gov with broadened query terms: chlorpheniramine (racemic parent), dexchlorphenamine, first-generation antihistamines + urticaria, chlorphenamine + urticaria
- **MOA data retrieval:** Query DrugBank API for DB13679 to populate mechanism of action, categories, and toxicity data (currently flagged as Data Gap DG002)
- **Safety data retrieval:** Download and parse the originator package insert (or international equivalent such as EMA/PMDA label) to populate key warnings, contraindications, and DDI data (Data Gap DG001)
- **Class-level evidence mapping:** Identify whether existing H1 antihistamine urticaria RCTs can be used as class-bridging evidence to upgrade the effective evidence level
- **Taiwan registration feasibility assessment:** Determine whether a Taiwan NDA pathway is applicable, given the drug is currently 未上市
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

