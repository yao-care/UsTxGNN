---
layout: default
title: Paromomycin
parent: 僅模型預測 (L5)
nav_order: 1016
evidence_level: L5
indication_count: 8
---

# Paromomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Paromomycin (DB01421): Original Indication Unclear → Idiopathic Copper-Associated Cirrhosis (Low-Confidence Candidate)

## One-Sentence Summary

> Paromomycin's approved indication could not be determined from this evidence pack (no Taiwan license records, no original indication text on file), though the underlying rationale text describes it as a non-absorbable aminoglycoside antibiotic used against amoebiasis/leishmaniasis.
> The TxGNN model's top prediction is **Idiopathic Copper-Associated Cirrhosis**, but this shares an identical score with four other unrelated hepatic/vascular disorders (ranks 2–5), and the model's own rationale text flags this cluster as a likely **false positive driven by liver-disease node embedding similarity**, not a genuine mechanistic signal.
> No clinical trials or literature support any of the top-ranked predictions; the only indication with any literature backing (peritonitis, rank 8) has weak, indirect evidence only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license records or approved indication text on file for this drug |
| Predicted New Indication | Idiopathic Copper-Associated Cirrhosis (rank 1; tied in score with 4 other hepatic/vascular diseases at ranks 2–5) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status (Taiwan) | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field is marked as a data gap. However, the evidence pack's own rationale text describes paromomycin as a **non-absorbable aminoglycoside antibiotic** that acts by inhibiting 30S ribosomal protein synthesis in susceptible organisms, giving it antiamoebic and antileishmanial activity.

There is **no identifiable mechanistic pathway** connecting this antimicrobial action to the pathophysiology of the top five predicted indications (copper-associated cirrhosis, hepatoportal sclerosis, hepatopulmonary syndrome, familial noncirrhotic portal hypertension, primary portal vein thrombosis). All five diseases sit in the same "liver disease" node neighborhood and share an **identical TxGNN score**, which strongly suggests the ranking reflects **knowledge-graph embedding clustering** rather than a true drug–disease mechanistic relationship.

Two additional findings work against pursuing this candidate further:
- **Rank 7 (acute urate nephropathy)** shows a *negative* mechanistic signal — aminoglycosides, including paromomycin, carry known nephrotoxicity risk (PMID 4293095), making this indication counter-indicated rather than promising.
- **Rank 8 (peritonitis)** has the only literature support in the pack, but it is indirect (amoebic colitis can rarely progress to amoebic peritonitis) and the bulk of the cited literature is unrelated in-vitro/leishmaniasis resistance research retrieved as keyword noise, not peritonitis-specific evidence.

Given this, none of the eight predicted indications currently has a defensible mechanistic or clinical rationale for repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (Idiopathic Copper-Associated Cirrhosis).

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication (Idiopathic Copper-Associated Cirrhosis).

*(Note: among all 8 candidates evaluated, only rank 8 — peritonitis — has any literature evidence, and it is indirect/weak; see rationale above.)*

---

## Market Information

No marketing authorization records are available — this drug is currently **not marketed** in the evaluated jurisdiction (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** A **Blocking** data gap (DG001) has been identified — the local regulatory label/warnings and contraindications could not be retrieved, which by itself prevents this candidate from advancing to Stage 1 safety review regardless of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All eight TxGNN-predicted indications lack mechanistic plausibility or clinical/trial evidence; the top five appear to be a knowledge-graph embedding artifact rather than a genuine signal, and one (acute urate nephropathy) is actively counter-indicated by paromomycin's known nephrotoxicity. Separately, a **Blocking** safety data gap (missing label/warnings) prevents any candidate from this drug from entering safety review at this time.

**To proceed, the following is needed:**
- Retrieve official label warnings/contraindications (DG001, Blocking) — required before any Stage 1 safety review
- Obtain confirmed mechanism of action data from DrugBank (DG002, High)
- If pursuing further, prioritize independent verification of the peritonitis (rank 8) signal with peritonitis-specific literature/trial searches, since it is the only candidate with any topical evidence — current searches returned largely off-target leishmaniasis/in-vitro studies
- Given the near-zero mechanistic basis, this drug is a low-priority candidate for repurposing pending materially stronger new evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

