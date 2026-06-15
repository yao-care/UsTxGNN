---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 6
---

# Amiloride
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

# Amiloride: From Potassium-Sparing Diuretic to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic that directly blocks the epithelial sodium channel (ENaC) in the renal collecting duct, used as an adjunct for managing edema in congestive heart failure and hypertension — particularly in combination with loop or thiazide diuretics to prevent hypokalemia.
TxGNN predicts it may be effective for **malignant hypertensive renal disease** with a prediction score of **99.82%**, though this top-ranked indication currently has **no supporting clinical trials or literature**.
Across the six predicted indications in this multi-indication report, **chronic pulmonary heart disease** (rank 6) carries the strongest actionable evidence — **2 RCTs** and **3 additional studies** (Evidence Level L3) — making it the most viable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally used as potassium-sparing diuretic for edema and hypertension (CHF combination therapy) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (no clinical trials or literature for rank 1 indication) |
| Market Status (Taiwan) | ✗ Not marketed |
| Number of Approved Products | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Amiloride is a direct blocker of the epithelial sodium channel (ENaC) in the distal renal tubule and collecting duct. By occluding ENaC, it reduces sodium reabsorption, lowers intravascular volume, and decreases blood pressure without causing potassium wasting — a key mechanistic distinction from loop or thiazide diuretics. This mechanism is directly relevant to conditions where aldosterone-driven sodium retention perpetuates hypertension and volume overload, including secondary hyperaldosteronism commonly seen in severe hypertensive disease.

Malignant hypertensive renal disease represents the end-organ manifestation of severely uncontrolled hypertension: renal microangiopathy, rapid decline in glomerular filtration, and dysregulated sodium-potassium handling through aldosterone-ENaC signaling. The mechanistic bridge between amiloride's ENaC-blocking action and renal tubular sodium retention in malignant hypertension is biologically coherent. However, the identical TxGNN score shared with "malignant renovascular hypertension" (both 99.82%) strongly suggests these two closely related disease ontology nodes are receiving the same score through knowledge-graph diffusion — not through independent mechanistic pathways — and should be interpreted with caution.

Currently, detailed mechanism of action data for amiloride was not available from this evidence pack (data gap DG002). Based on established pharmacology, amiloride's ENaC blockade is most effective in conditions involving aldosterone excess — including primary aldosteronism, secondary hyperaldosteronism, and fluid-overloaded states. This mechanism theoretically applies to malignant hypertensive renal disease, but without direct clinical evidence, the prediction remains at hypothesis level.

---

## Multi-Indication Overview

This evidence pack covers six TxGNN-predicted indications. The table below summarizes the evidence landscape across all candidates:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Literature | Recommendation |
|------|----------------------|-------------|----------------|--------|------------|----------------|
| 1 | Malignant hypertensive renal disease | 99.82% | L5 | 0 | 0 | Hold |
| 2 | Malignant renovascular hypertension | 99.82% | L4 | 0 | 1 (indirect) | Research Question |
| 3 | Pulmonary hypertension, multifactorial | 99.81% | L5 | 0 | 0 | Hold |
| 4 | Pulmonary hypertension, lung disease/hypoxia | 99.81% | L5 | 0 | 20 (none relevant to amiloride) | Hold |
| 5 | Braddock syndrome | 99.75% | L5 | 0 | 0 | Hold |
| **6** | **Chronic pulmonary heart disease** | **99.68%** | **L3** | **0** | **5** | **Proceed with Guardrails** |

> **Note on Rank 4**: Despite 20 retrieved publications, every paper addresses general hypoxia biology (brain aging, cancer metabolism, neurodegeneration). None studies amiloride in this indication. Literature relevance to the drug is zero; evidence level remains L5.

> **Note on Rank 5**: Braddock syndrome (OMIM 619980) is caused by *POLR3A* gene mutation, presenting as a rare congenital disorder with intellectual disability and sensorineural hearing loss. No plausible mechanism connects amiloride's ENaC/sodium-channel pharmacology to this genetic pathway. The prediction likely reflects upstream shared disease nodes in the knowledge graph (cardiac or neurological development).

---

## Clinical Trial Evidence

No clinical trials are currently registered for amiloride in **malignant hypertensive renal disease**.

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly addresses amiloride in **malignant hypertensive renal disease**.

The following table presents the most relevant literature from **chronic pulmonary heart disease** (rank 6) — the indication with the strongest evidence in this pack:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/) | 1987 | RCT | *Lancet* | Double-blind crossover trial (n=14): captopril alone vs frusemide + amiloride in mild heart failure; combination maintained hemodynamic control in 10/14 patients; 4 patients with prior pulmonary oedema deteriorated on captopril alone |
| [2831702](https://pubmed.ncbi.nlm.nih.gov/2831702/) | 1988 | RCT | *Am J Cardiology* | Isosorbide-5-mononitrate added to a regimen including amiloride 5–10 mg/day plus ACE inhibitor in CHF (NYHA II–III); hemodynamic dose-response assessment |
| [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/) | 1991 | Clinical Observational | *Cardiovascular Drugs and Therapy* | Double-blind, crossover, placebo-controlled (n=11): amiloride improved pulmonary capillary wedge pressure and cardiac output in chronic CHF patients on digoxin, without blunting digoxin's inotropic effect |
| [16815890](https://pubmed.ncbi.nlm.nih.gov/16815890/) | 2006 | Animal Study | *Am J Physiol Lung Cell Mol Physiol* | Alveolar fluid reabsorption (driven by apical ENaC and basolateral Na-K-ATPase) is increased in compensated CHF rats; mechanistically supports ENaC activity as a physiologic target in heart failure-associated pulmonary fluid dynamics |
| [8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/) | 1996 | Case Report | *Am J Med Sciences* | Severe hyperkalemia (K⁺ = 9.3 mEq/L) with EKG changes in a geriatric CHF patient co-prescribed trimethoprim-sulfamethoxazole; highlights the additive potassium-retention risk when combining ENaC-blocking agents |

For **malignant renovascular hypertension** (rank 2), one supporting literature item exists:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | *J Hypertension Supplement* | Diagnostic workup for mineralocorticoid hypertension (primary aldosteronism, Conn's syndrome, bilateral adrenal hyperplasia); amiloride suppression test described as a clinical tool to differentiate primary from secondary aldosteronism in renovascular hypertension — indirect mechanistic support only |

---

## Market Information

Amiloride is not registered or marketed in Taiwan. No approved products, NDA numbers, or licensed indications exist in the Taiwan market based on current regulatory data.

For reference, amiloride is available in several international markets (including the United States) as a generic oral tablet, typically in 5 mg strength, often co-formulated with hydrochlorothiazide (e.g., Moduretic). Any Taiwan clinical development program would require a new market authorization strategy.

---

## Safety Considerations

Safety data (key warnings, contraindications, full drug interaction profiles) were not captured in this evidence pack. Please refer to the package insert for complete safety information.

The following clinically relevant signal was identified from retrieved literature:

- **Hyperkalemia**: Amiloride's potassium-sparing mechanism poses a risk of life-threatening hyperkalemia when combined with ACE inhibitors, ARBs, other potassium-sparing diuretics, or drugs that reduce renal potassium excretion (e.g., trimethoprim, NSAIDs). A case report (PMID 8615380) documented K⁺ = 9.3 mEq/L with EKG changes in a CHF patient, underscoring the need for electrolyte monitoring in any combination therapy protocol.

---

## Conclusion and Next Steps

**Decision: Hold** *(for malignant hypertensive renal disease, rank 1)*

**Rationale:**
The top-ranked TxGNN prediction has zero supporting evidence, and the identical prediction score shared with malignant renovascular hypertension strongly suggests a knowledge-graph diffusion artifact between adjacent disease ontology nodes rather than drug-specific mechanistic evidence. Proceeding further would rest entirely on model output with no experimental validation.

---

**Alternative Decision: Proceed with Guardrails** *(for chronic pulmonary heart disease, rank 6)*

**Rationale:**
Amiloride has been directly evaluated in chronic congestive heart failure — a mechanistically overlapping condition with cor pulmonale — via two RCTs and a dedicated clinical observational study, all demonstrating measurable hemodynamic benefit. Chronic pulmonary heart disease involves right-heart failure with volume overload driven by pulmonary hypertension, representing a physiologically coherent ENaC-mediated sodium reduction target. The ENaC-alveolar fluid link further demonstrated in animal models (PMID 16815890) adds mechanistic depth.

**To proceed, the following is needed:**

- Resolve blocking data gap DG001: Obtain Taiwan TFDA (or originator) package insert warnings and contraindications before any clinical protocol development
- Resolve data gap DG002: Retrieve complete MOA data from DrugBank to strengthen mechanistic rationale documentation
- Conduct a dedicated pilot trial or observational study specifically in cor pulmonale — existing RCT evidence covers general CHF, not right-heart-predominant disease
- Design a pre-specified electrolyte and renal function monitoring protocol to manage hyperkalemia risk, especially in patients concurrently on ACE inhibitors, ARBs, or trimethoprim-based antibiotics
- Develop a Taiwan regulatory access strategy for a drug not currently marketed in Taiwan (new market authorization required before any sponsored clinical trial)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

