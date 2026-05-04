---
layout: default
title: Acetohydroxamic Acid
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 4
---

# Acetohydroxamic Acid
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

Using the `txgnn-pipeline` skill — this is a TxGNN drug repurposing report generation task. Now producing the report from the Evidence Pack.

---

# Acetohydroxamic Acid: From Struvite Urinary Tract Infection to Ureaplasma Urethritis

## One-Sentence Summary

Acetohydroxamic acid (AHA) is a urease inhibitor, traditionally used as adjunctive therapy for recurrent struvite (infection) kidney stones caused by urease-producing bacteria, though no local market authorization data is available in this dataset.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis** with a prediction score of **99.63%**, but **no clinical trials** and **no publications** currently support this direction within the current dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from local registry (US Lithostat: adjunctive therapy for struvite kidney stones due to urease-producing bacteria) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Acetohydroxamic acid is a synthetic hydroxamic acid compound that acts as a competitive and irreversible inhibitor of bacterial urease — the enzyme responsible for hydrolyzing urea into ammonia and carbon dioxide. This ammonia production creates an alkaline urinary environment that damages urothelial membranes, promotes inflammation, and in the kidney, drives struvite crystal formation. By blocking urease at the enzymatic level, AHA cuts off this entire downstream cascade.

*Ureaplasma urealyticum* and *Ureaplasma parvum* are exceptional among urogenital pathogens: their pathogenicity is almost entirely dependent on urease activity. They are among the most potent urease-producing organisms colonizing the urogenital tract, and urease-derived ammonia is the primary driver of mucosal damage, persistent inflammation, and colonization success. This creates a direct, mechanism-first connection between AHA's pharmacological action and Ureaplasma urethritis — the pathogen's Achilles heel is precisely what AHA targets.

Among the four predicted indications in this Evidence Pack, Ureaplasma urethritis has the clearest and strongest mechanistic rationale. While no clinical trial or publication records appear within the current dataset, in vitro studies and animal model evidence supporting AHA's activity against Ureaplasma are known to exist in the broader scientific literature. This is most likely a dataset coverage gap rather than a genuine absence of scientific basis, making this an active hypothesis worth pursuing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No licensed products are registered in the local market (0 authorizations on record). Acetohydroxamic acid is marketed in the United States as **Lithostat** (Mission Pharmacal) for adjunctive treatment of chronic urea-splitting urinary tract infections causing struvite nephrolithiasis, but does not appear in the local (Taiwan) regulatory registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Prescribing information (TFDA label and DDI data) was not available in this dataset. The US Lithostat prescribing information documents known risks including hemolytic anemia, teratogenicity, and neurological side effects. These should be reviewed before any clinical development planning.

---

## Additional Predicted Indications

The TxGNN model identified three further candidates. Mechanistic assessments from the Evidence Pack are summarized for completeness:

| Rank | Disease | Score | Decision | Mechanistic Assessment |
|------|---------|-------|----------|----------------------|
| 2 | Gonococcal urethritis | 99.63% | Hold | *Neisseria gonorrhoeae* is urease-negative; TxGNN score likely driven by disease-class similarity (urethritis), not mechanism. No direct pharmacological basis. |
| 3 | Uterine inflammatory disease | 99.54% | Hold | May involve Ureaplasma in a subset of cases, but the condition is broadly defined and predominantly polymicrobial (non-urease organisms). Applicability is indirect and limited. |
| 4 | Xanthogranulomatous pyelonephritis | 99.46% | Hold | Mechanistic link exists via *Proteus mirabilis* (a strong urease producer), but XGP treatment is primarily surgical (nephrectomy). AHA's long-term toxicity profile makes the benefit/risk ratio unfavorable in this chronic inflammatory context. |

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic connection between AHA's urease inhibition and Ureaplasma's urease-dependent pathogenesis is direct and pharmacologically coherent — this is among the cleaner mechanism-to-target alignments seen in urological repurposing candidates. However, with zero supporting clinical trial or literature evidence in the current dataset (L5), this is a hypothesis that requires translational validation before any development commitment.

**To proceed, the following is needed:**
- Targeted literature review outside the current dataset to surface existing in vitro MIC data for AHA against *Ureaplasma urealyticum* / *U. parvum*
- MOA data retrieval from DrugBank (data gap DG002) to complete formal mechanistic documentation
- Full prescribing information review (US Lithostat label or TFDA equivalent) to characterize safety boundaries — particularly hemolytic anemia risk and teratogenicity for the target population
- Pharmacokinetic assessment: urogenital tissue penetration and urethral concentration achievable at tolerated doses
- Route-of-administration feasibility: evaluation of oral vs. topical/local delivery for urethral indications
- If in vitro data is supportive, design a small Phase 2 proof-of-concept study in *Ureaplasma*-positive urethritis patients with confirmed antibiotic resistance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

