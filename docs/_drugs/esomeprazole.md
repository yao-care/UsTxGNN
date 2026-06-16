---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 572
evidence_level: L5
indication_count: 3
---

# Esomeprazole
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

The skill confirms this is a TxGNN pipeline report task. Now generating the evaluation report based on `predicted_indications[0]` (duodenogastric reflux, rank #1) as the primary focus, with supporting context from the rank #3 indication where relevant.

---

# Esomeprazole: From Gastroesophageal Reflux Disease to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) — the S-isomer of omeprazole — widely established in clinical practice for treating gastroesophageal reflux disease (GERD), peptic ulcer disease, and *Helicobacter pylori* eradication.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux** (score: 99.53%), with **0 clinical trials** and **1 review publication** currently supporting this specific direction.
Evidence for this particular repurposing direction remains at an early mechanistic stage (L4), warranting further dedicated investigation before clinical progression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | GERD and acid-related diseases (derived from published literature; no US license record in current dataset) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| US Market Status | Not marketed (no license on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on published literature (PMID 18679668; PMID 10983736), Esomeprazole irreversibly binds to and inhibits the gastric H⁺/K⁺-ATPase proton pump — the terminal step of gastric acid secretion — producing sustained, dose-dependent suppression of intragastric acidity. As the S-isomer of omeprazole, it benefits from reduced first-pass CYP2C19 metabolism, resulting in higher and more consistent plasma concentrations than the racemic parent compound, and thus superior acid control.

Duodenogastric reflux (DGR) is a condition in which duodenal contents — including bile acids, lysolecithin, and pancreatic secretions — reflux back into the stomach. The mucosal injury in DGR is driven not solely by acid, but by the synergistic cytotoxicity of bile acids acting in an acidic environment. By raising intragastric pH, PPI therapy can neutralize the acidic milieu that amplifies bile-acid-mediated damage and reduces mucosal permeability, indirectly attenuating the injury cascade. However, PPI therapy does not address the primary cause of DGR (impaired pyloric function or altered gastric motility) and has no direct effect on the bile or alkaline reflux components themselves.

The TxGNN model's high score for this indication (rank #11,278 globally) most likely reflects structural proximity between the duodenogastric reflux node and closely related acid-disease nodes in the knowledge graph — such as GERD, peptic ulcer, and reflux esophagitis — where Esomeprazole already has well-established edges. The biological rationale is plausible but indirect; PPIs are sometimes used empirically in DGR patients with concurrent acid exposure, yet no dedicated randomized trial evidence exists for DGR as a standalone indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Narrative Review | European Journal of Clinical Pharmacology | Comprehensive PPI clinical use update; esomeprazole identified as first-line for GERD, peptic ulcer, *H. pylori* infection, NSAID-induced GI lesions, and Zollinger-Ellison syndrome. No DGR-specific efficacy data presented. |

---

## US Market Information

No US drug authorizations are on record for Esomeprazole in the current dataset. This likely reflects a data pipeline gap — Esomeprazole (Nexium®) is widely approved in major markets. US FDA label data should be retrieved directly from the FDA Drugs@FDA database to complete this section.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a high raw score for duodenogastric reflux, but this prediction is driven by knowledge-graph structural proximity rather than direct mechanistic or clinical evidence. With zero clinical trials and only a single non-DGR-specific narrative review, the evidence base is insufficient (L4, decision stage S1) to justify advancement without first establishing a dedicated research programme.

**To proceed, the following is needed:**

- **Dedicated clinical evidence**: Prospective observational studies or pilot RCTs evaluating esomeprazole specifically in patients with confirmed duodenogastric reflux (e.g., bile reflux monitoring endpoints, validated symptom scores)
- **Mechanistic clarification**: Pre-clinical or translational data demonstrating that acid suppression alone attenuates DGR-specific mucosal injury in bile/acid mixed reflux models
- **US regulatory label data**: Retrieve the full Nexium® (or equivalent) US FDA-approved label to establish the safety baseline (warnings, contraindications, Box Warnings) — currently absent from this dataset
- **Drug-drug interaction data**: DDI query returned no results; cross-reference DrugBank and clinical DDI databases for CYP2C19-mediated interactions (especially with clopidogrel, methotrexate, and antiretrovirals) before any clinical advancement
- **Differentiating from established indications**: Note that Esomeprazole already holds robust L1 evidence for **duodenal ulcer** (predicted indication rank #3; 50+ clinical trials), which may be a more actionable near-term repurposing priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

