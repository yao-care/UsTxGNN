---
layout: default
title: Vitamin A
parent: 僅模型預測 (L5)
nav_order: 1295
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: From Nutritional Deficiency to Perinatal & Neonatal Disease Prevention

## One-Sentence Summary

Vitamin A (DrugBank DB00162) is an essential fat-soluble vitamin whose established clinical role is treating and preventing vitamin A deficiency. TxGNN's single highest-scoring prediction ("congenital prothrombin deficiency") is almost certainly a knowledge-graph artifact confusing Vitamin A with Vitamin K and is **not clinically credible**. Among the ten model-ranked candidates, the strongest evidence-backed signal is **Perinatal Disease** — reflecting Vitamin A's well-documented role in preventing bronchopulmonary dysplasia (BPD) and reducing neonatal/maternal mortality — supported by **five Cochrane systematic reviews** and a **Phase 3 RCT enrolling 100,000 participants**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin A deficiency (no structured indication text on file; drug is a nutritional/essential vitamin, not a single-indication pharmaceutical) |
| Predicted New Indication (evidence-led) | Perinatal disease (Vitamin A supplementation in very low birth weight / preterm infants) |
| TxGNN Prediction Score (this candidate) | 99.63% (rank 9411/~17,000 in disease vocabulary) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs / Cochrane systematic reviews) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

⚠️ **Note:** The disease with the *highest* raw TxGNN score in this evidence pack (congenital prothrombin deficiency, 99.97%) was **not selected** as the headline indication — see "Full Candidate Summary" and "Why is This Prediction Reasonable" below for the rationale.

---

## Full Candidate Summary (All 10 Model-Ranked Indications)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Reviewer Note |
|------|---------|-------------|-----------------|-----------------|----------------|
| 1 | Congenital prothrombin deficiency | 99.97% | L5 | Hold | Likely false positive — Vitamin A/K confusion; no mechanistic link (Factor II synthesis depends on Vitamin K, not A) |
| 2 | Biotin metabolic disease | 99.85% | L5 | Hold | Likely false positive — unrelated coenzyme pathway |
| 3 | Non-syndromic esophageal malformation | 99.72% | L5 | Hold | Plausible embryology (RA signaling in foregut development) but zero human evidence |
| 4 | Injury (wound healing) | 99.69% | L3 | Research Question | Real RAR-mediated mechanism; evidence is observational/mixed (fracture risk both ways) |
| 5 | Cell proliferation disorder | 99.64% | L4 | Research Question | Mechanism valid via RAR/RXR, but strongest clinical evidence belongs to ATRA (a distinct drug entity), not Vitamin A itself |
| **6** | **Perinatal disease** | **99.63%** | **L1** | **Proceed with Guardrails** | **Strongest evidence tier — established use, Cochrane-level support** |
| 6 | Florid cemento-osseous dysplasia | 99.63% | L5 | Hold | No trials, no literature — no clinical basis |
| 8 | Segmental odontomaxillary dysplasia | 99.63% | L5 | Hold | No trials, no literature — no clinical basis |
| 9 | Disease by subcellular system affected | 99.63% | L5 | Hold | Ontology node, not a real disease entity — should be excluded from candidate list |
| 10 | Radiation/chemically induced disorder | 99.63% | L3 | Research Question | Valid for the photoaging subset (topical retinoids) but the label is too broad; most trials unrelated to Vitamin A |

*(Perinatal disease is technically rank 7 by raw score ordering but is elevated here because it is the only candidate reaching L1 evidence and an actionable S3 decision stage.)*

---

## Why is This Prediction Reasonable?

**On model reliability:** Six of the ten candidates (ranks 1, 2, 3, 6, 8, 9) have **no supporting clinical trials or literature at all**, or evidence pack notes explicitly flag them as probable knowledge-graph embedding artifacts (e.g., Vitamin A conflated with Vitamin K for the top-scoring candidate). One node ("disease by subcellular system affected") is an ontology category, not a real disease. This report does not treat raw TxGNN score as a proxy for clinical credibility, and features the candidate with the strongest actual evidence instead.

**Mechanism:** Vitamin A (retinol) and its active metabolite retinoic acid signal through nuclear retinoic acid receptors (RAR/RXR), which are essential for normal lung growth, alveolar epithelial differentiation, and immune maturation. Preterm and very-low-birth-weight (VLBW) infants are born with low hepatic vitamin A stores and low serum retinol-binding protein, placing them at elevated risk of chronic lung disease (bronchopulmonary dysplasia) and infection-related mortality.

**Relationship to original use:** This is not a novel repurposing hypothesis so much as a well-established, evidence-dense clinical practice (vitamin A supplementation in VLBW infants) that the TxGNN model independently rediscovered from the knowledge graph — a positive validation signal for the model, even though the underlying use is not "new." A genuinely novel finding within this evidence set (wound healing / cell proliferation, ranks 4–5) has real mechanistic plausibility but only observational or preclinical support today.

---

## Clinical Trial Evidence
*(Perinatal disease — Vitamin A–specific trials only; many other trials in the evidence pool concern unrelated vitamins (D, C, B) or micronutrient combinations and are excluded here as not directly relevant.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00211341](https://clinicaltrials.gov/study/NCT00211341) | Phase 3 | Completed | 100,000 | Randomised, double-blind, placebo-controlled trial of weekly vitamin A supplementation in reproductive-age women (Ghana); hypothesized 33% reduction in maternal mortality — largest RCT in this evidence pack directly testing Vitamin A |
| [NCT03971604](https://clinicaltrials.gov/study/NCT03971604) | N/A | Unknown | 300 | Correlation between maternal Vitamin A/E levels and preeclampsia risk |
| [NCT00860470](https://clinicaltrials.gov/study/NCT00860470) | Phase 3 | Completed | 44,567 | Antenatal multiple micronutrient supplementation (including vitamin A) to improve infant survival and health, Bangladesh |
| [NCT02300155](https://clinicaltrials.gov/study/NCT02300155) | Phase 4 | Completed | 1,370 | Tolerability of a multivitamin (containing vitamin A) vs. a standard prenatal vitamin in pregnant women with morning sickness |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27552058](https://pubmed.ncbi.nlm.nih.gov/27552058/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Vitamin A supplementation reduces mortality and short/long-term morbidity (including BPD) in very low birth weight infants — most recent update of a repeatedly-confirmed Cochrane series |
| [22742601](https://pubmed.ncbi.nlm.nih.gov/22742601/) | 2012 | Systematic Review/Meta-analysis | Paediatr Perinat Epidemiol | Vitamin A/carotenoid supplementation during pregnancy improves maternal, fetal, neonatal and infant health outcomes |
| [23445845](https://pubmed.ncbi.nlm.nih.gov/23445845/) | 2013 | Review | J Pediatr | Vitamin A and D deficiencies in preterm/LBW infants; supplementation needed to prevent detrimental consequences |
| [25222155](https://pubmed.ncbi.nlm.nih.gov/25222155/) | 2014 | Review/Editorial | JAMA Pediatrics | Vitamin A shortage directly linked to risk of bronchopulmonary dysplasia in preterm infants |
| [21975731](https://pubmed.ncbi.nlm.nih.gov/21975731/) | 2011 | Cochrane Systematic Review | Cochrane Database Syst Rev | Earlier update of the same Cochrane review confirming consistent effect across multiple update cycles (2000, 2002, 2007, 2011, 2016) |
| [2672772](https://pubmed.ncbi.nlm.nih.gov/2672772/) | 1989 | Review | Am J Clin Nutr | Premature infants have lower retinol reserves than term infants; parenteral supplementation strategy discussed |
| [29895848](https://pubmed.ncbi.nlm.nih.gov/29895848/) | 2018 | Case report | Eur J Clin Nutr | Vitamin A/micronutrient deficiency post-bariatric surgery causing maternal and fetal complications across multiple pregnancies |
| [17952233](https://pubmed.ncbi.nlm.nih.gov/17952233/) | 2007 | Burden-of-disease study | S Afr Med J | Estimated disease burden attributable to vitamin A deficiency in children and pregnant women, South Africa |

---

## US Market Information

Vitamin A is currently recorded as **not marketed** (0 licenses on file) in the source regulatory dataset for this evidence pack. No license records are available to summarize.

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, DDI) in this evidence pack are all marked as data gaps.

**Relevant point from the literature evidence base:** Vitamin A has a narrow therapeutic window in pregnancy and infancy — both deficiency *and* excess (hypervitaminosis A) are associated with adverse outcomes. Case-level literature in this pack (PMID 29895848) documents maternal/fetal complications from vitamin A excess following bariatric-surgery-related deficiency correction, and separate systematic reviews (not part of the perinatal evidence set) associate high-dose vitamin A intake with increased fracture risk. Dosing in neonatal/perinatal use should follow established NICU protocols rather than general supplement dosing.

Beyond this, please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Perinatal Disease / VLBW infant supplementation specifically)

**Rationale:**
This is the only candidate in the full set reaching L1 evidence (multiple Cochrane systematic reviews plus a 100,000-participant Phase 3 RCT), and it reflects an already-established area of neonatal clinical practice rather than a speculative new mechanism. The remaining nine model-ranked candidates should be held: six have no clinical trial or literature support at all (several explicitly flagged as likely knowledge-graph artifacts), and the two with mechanistic plausibility (wound healing, cell proliferation) currently rest only on observational or preclinical data.

**To proceed, the following is needed:**
- Structured MOA and formal package-insert safety data (currently data gaps) to complete a S1 safety pre-screen
- Confirmation of dosing protocols and route of administration specific to preterm/VLBW neonatal populations
- Independent verification that "congenital prothrombin deficiency" and "biotin metabolic disease" predictions are graph-embedding artifacts (recommend flagging to the TxGNN pipeline team for model QA)
- Exclusion of ontology-category nodes (e.g., "disease by subcellular system affected") from future candidate lists at the data-processing stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

