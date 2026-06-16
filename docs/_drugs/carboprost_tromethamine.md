---
layout: default
title: Carboprost Tromethamine
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Carboprost Tromethamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Carboprost Tromethamine: From Obstetric Use to Atypical Coarctation of Aorta

## One-Sentence Summary

Carboprost tromethamine is a synthetic prostaglandin F2α (PGF2α) analogue used in obstetrics as a uterotonic agent for refractory postpartum hemorrhage and second-trimester abortion induction.
The TxGNN model predicts it may be effective for **Atypical Coarctation of Aorta** (highest-ranked among 10 predicted indications, score 99.99%), yet **no supporting clinical trials or literature evidence exists for any of the 10 predictions**.
All predicted indications are at evidence Level L5 (model prediction only); 9 of 10 receive a **Hold** recommendation, with the most mechanistically credible candidate being Primary Hereditary Glaucoma (Rank 10, L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory data available (drug not marketed in Taiwan) |
| Predicted New Indication | Atypical Coarctation of Aorta |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on pharmacological knowledge and references within the repurposing rationale, carboprost tromethamine is a 15-methyl analogue of prostaglandin F2α that acts as an FP receptor agonist. Its primary effect is stimulation of smooth muscle contraction—most notably uterine smooth muscle—which underpins its clinical use as a uterotonic for postpartum hemorrhage and as an abortifacient. The drug is administered by intramuscular injection and has well-known systemic effects including vasoconstriction, bronchospasm, and gastrointestinal smooth muscle stimulation.

Atypical coarctation of the aorta is a congenital structural defect characterized by narrowing of the aorta. It requires surgical or catheter-based intervention to correct the anatomical obstruction; there is no pharmacological treatment that addresses the underlying structural pathology. PGF2α receptor agonism (promoting vasoconstriction and smooth muscle contraction) has no established mechanistic basis for treating this condition. The TxGNN model's high score most likely reflects indirect graph-level associations between prostaglandin-related nodes and cardiovascular disease nodes in the knowledge graph—not a true therapeutic signal.

Across this Evidence Pack's 10 predicted indications, one candidate stands out as mechanistically plausible: **Primary Hereditary Glaucoma (Rank 10)**. Established PGF2α analogues—latanoprost, bimatoprost, travoprost, tafluprost—are the **first-line standard of care** for open-angle glaucoma, acting through the same FP receptor to increase uveoscleral aqueous humor outflow and reduce intraocular pressure. As a 15-methyl-PGF2α derivative, carboprost shares this receptor target and theoretically exhibits a class effect. However, a critical formulation barrier exists: all approved ophthalmic prostaglandins are topical eye drops, whereas carboprost is only available as intramuscular injection, making direct ophthalmic repurposing impractical without reformulation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Atypical Coarctation of Aorta.

---

## Literature Evidence

Currently no related literature available for Atypical Coarctation of Aorta.

---

## Supplementary: All 10 Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Mechanistic Assessment |
|------|-----------|------------|---------------|---------------|----------------------|
| 1 | Atypical Coarctation of Aorta | 99.99% | L5 | Hold | No mechanistic link; structural defect requiring surgery |
| 2 | Aortic Malformation | 99.98% | L5 | Hold | Structural defect; 1 trial (C-grade, obstetric monitoring only) |
| 3 | Migraine with Brainstem Aura | 99.97% | L5 | Hold | Cerebral vasospasm risk; no clinical data |
| 4 | Migraine Disorder | 99.96% | L5 | Hold | COX inhibitors (not agonists) are standard; opposite direction |
| 5 | Pulmonary Hypertension | 99.93% | L5 | **Hold ⚠️** | **Safety concern: PGF2α causes vasoconstriction—opposite to treatment goal** |
| 6 | Non-syndromic Esophageal Malformation | 99.92% | L5 | Hold | Congenital structural defect; no mechanistic link |
| 7 | Kyphoscoliotic Heart Disease | 99.92% | L5 | Hold | Mechanical etiology; bronchospasm AE may worsen respiratory function |
| 8 | Amenorrhea | 99.89% | L5 | Research Question | Luteolytic/endometrial shedding mechanism has indirect relevance |
| 9 | Esophageal Disease | 99.83% | L5 | Hold | Broad category; no specific therapeutic rationale |
| **10** | **Primary Hereditary Glaucoma** | **99.69%** | **L4** | **Research Question** | **Best candidate: FP receptor class effect shared with latanoprost/bimatoprost** |

> **⚠️ Safety Alert — Pulmonary Hypertension (Rank 5):** Carboprost's known adverse effects include pulmonary vasoconstriction and bronchospasm mediated by FP receptors. This is pharmacologically **opposite** to the vasodilation goal of PAH therapy. Approved prostanoids for PAH are PGI₂ analogues (epoprostenol, treprostinil), not PGF2α. This prediction should be considered a **false positive with potential for harm** and must not be pursued.

---

## Safety Considerations

Please refer to the package insert for full safety information (Taiwan regulatory data not available; US FDA package insert for Hemabate® is the recommended reference source).

Based on the pharmacological class (systemic PGF2α agonist), the following safety signals are known from published literature:

- **Pulmonary and Respiratory Risk**: FP receptor-mediated bronchospasm and pulmonary vasoconstriction are documented adverse effects. Contraindicated in patients with asthma, pulmonary hypertension, or obstructive airway disease.
- **Cardiovascular Effects**: Systemic vasoconstriction; blood pressure fluctuation possible.
- **Gastrointestinal Effects**: Nausea, vomiting, diarrhea common with intramuscular administration due to GI smooth muscle stimulation.
- **Drug Interactions**: No interaction data found in the Evidence Pack query (query_status: not_found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the 10 TxGNN-predicted indications has supporting clinical trial or published literature evidence, and the top-ranked prediction (atypical coarctation of aorta) has no biologically plausible mechanistic basis. The only candidate approaching actionability—primary hereditary glaucoma (Rank 10)—faces a fundamental formulation barrier (IM injection vs. required ophthalmic topical route) that would require a full drug delivery reformulation program before any clinical exploration.

**To proceed, the following is needed:**

- **Immediate (Data Gaps)**
  - Retrieve full MOA and safety/toxicity profile from DrugBank API (resolves DG002)
  - Download and parse Taiwan FDA or US FDA package insert for warnings and contraindications (resolves DG001)

- **For Primary Hereditary Glaucoma (Rank 10 — highest-priority candidate)**
  - Conduct targeted PubMed literature search: "carboprost" OR "15-methyl-PGF2α" AND "intraocular pressure" OR "glaucoma" OR "aqueous humor"
  - Confirm whether any in vitro or animal ophthalmic studies exist for carboprost or its structural analogues
  - Assess technical feasibility of ophthalmic formulation (topical eye drop or intracameral route)

- **For Amenorrhea (Rank 8 — secondary candidate)**
  - Literature review: PGF2α luteolytic mechanism and amenorrhea subtypes (specifically intrauterine adhesion-related or corpus luteum dysfunction)
  - Define the specific amenorrhea subtype(s) where PGF2α-mediated endometrial shedding could be therapeutic vs. harmful

- **Cross-cutting**
  - All L5 "Hold" indications should remain deprioritized until at least one of the above candidate investigations yields positive preclinical evidence
  - Do not proceed with pulmonary hypertension under any circumstances without full safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

