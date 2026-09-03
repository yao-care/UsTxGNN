---
layout: default
title: Magnesium Salicylate
parent: 僅模型預測 (L5)
nav_order: 885
evidence_level: L5
indication_count: 10
---

# Magnesium Salicylate
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

# Magnesium Salicylate: From Pain/Inflammation to Spondyloarthropathy, Susceptibility To

## One-Sentence Summary

Magnesium salicylate (DrugBank DB01397) is a salicylate-class NSAID generally used for pain, fever, and inflammation; detailed original-indication and mechanism-of-action data are not present in this evidence pack. The TxGNN model's top prediction is **Spondyloarthropathy, susceptibility to**, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on the knowledge-graph model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug class is a non-acetylated salicylate NSAID for pain/fever/inflammation) |
| Predicted New Indication | Spondyloarthropathy, susceptibility to |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (no clinical trials or literature support) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (data gap DG002). Based on general pharmacological knowledge, magnesium salicylate belongs to the salicylate class of NSAIDs (COX-1/COX-2 inhibition), a class whose anti-inflammatory and analgesic effects are well established. Mechanistically, this class-level effect could plausibly extend to inflammatory joint conditions in the spondyloarthropathy spectrum, since NSAIDs are the recognized first-line symptomatic treatment for axial spondyloarthritis and ankylosing spondylitis (per ASAS/EULAR guidance).

However, the top-ranked prediction here, "spondyloarthropathy, susceptibility to," is a genetic-susceptibility classification rather than the disease itself. A drug cannot alter inherited disease risk, so the pharmacological rationale only applies loosely — to symptom control in patients who have already developed disease, not to the "susceptibility" phenotype as coded. By contrast, rank 5 in this same evidence pack, **ankylosing spondylitis**, is the actual treatable disease for which the NSAID class rationale is directly applicable, though it carries an identical lack of direct evidence for this specific molecule.

No clinical trial, ICTRP registry, or PubMed record for magnesium salicylate against any of the top 10 predicted indications was found (see query log, IDs 4–33, all zero results). This means the current signal is model-only and should be treated as a research hypothesis rather than a data-supported repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications data (DG001) is flagged as a Blocking gap — this must be resolved before any safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication is a genetic-susceptibility code rather than an actual disease, and there is zero clinical trial or literature evidence for magnesium salicylate against any of the top 10 TxGNN candidates. Combined with the absence of TFDA/US labeling data (Blocking gap) and zero market licenses, evidence is insufficient to advance beyond a research question.

**To proceed, the following is needed:**
- TFDA/FDA label — warnings, contraindications (DG001, Blocking)
- Confirmed mechanism of action via DrugBank API (DG002)
- Re-evaluate rank 5 candidate, **ankylosing spondylitis**, as the mechanistically clearer and clinically actionable target compared to the "susceptibility to" phenotype at rank 1
- Direct clinical/preclinical evidence search specific to magnesium salicylate (current searches all returned 0 results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

