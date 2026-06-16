---
layout: default
title: Cyclopentolate
parent: 僅模型預測 (L5)
nav_order: 555
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
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

# Cyclopentolate: From Ophthalmic Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a non-selective muscarinic receptor antagonist (M1–M5) used clinically as an ophthalmic cycloplegic and mydriatic agent to dilate pupils during eye examinations.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome** (as well as neurogenic bladder and irritable bowel syndrome),
with **no clinical trials and no publications** currently supporting any of these new directions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory license on record (0 authorizations found) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| US Market Status | Not marketed (no licenses found) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published pharmacological knowledge, Cyclopentolate is a non-selective anticholinergic agent that competitively blocks muscarinic receptors across all five subtypes (M1–M5). Its primary clinical use is ophthalmic: blocking the ciliary muscle and iris sphincter to produce cycloplegia (paralysis of accommodation) and mydriasis (pupil dilation). It is formulated exclusively as an eye drop and carries notable CNS penetration due to its lipophilicity.

Cauda equina syndrome (CES) is a surgical emergency arising from compression of lumbar nerve roots in the spinal canal, with standard treatment being urgent decompression surgery. The TxGNN model's predicted link is mechanistically indirect: CES commonly produces secondary neurogenic bladder dysfunction (urinary retention or overflow incontinence), and since muscarinic antagonists are a recognised class for managing overactive neurogenic bladder, the model may have identified this downstream symptom pathway. However, this is a weak connection — cyclopentolate's pharmacological target is smooth muscle, not the core pathology of mechanical nerve compression, and it cannot reverse or repair structural nerve damage.

Among the three predicted indications, **neurogenic bladder** (rank 2) represents the strongest mechanistic rationale within this candidate cluster. Established muscarinic antagonists such as oxybutynin, solifenacin, and tolterodine are first-line treatments for overactive neurogenic bladder via M2/M3 receptor blockade at the detrusor — the same receptor class Cyclopentolate blocks. A plausible class-effect argument exists. However, three substantial barriers prevent translation: (1) no systemic formulation of cyclopentolate exists; (2) its high CNS penetrance elevates the risk of central anticholinergic adverse effects; and (3) no molecular-level or clinical evidence for cyclopentolate in bladder indications has been published. For **irritable bowel syndrome** (rank 3), antispasmodic anticholinergics (hyoscine, dicyclomine) are used symptomatically for gut cramping via M3 blockade, providing a similar indirect mechanistic thread — but modern IBS management has shifted toward gut-selective agents precisely to avoid the systemic anticholinergic profile cyclopentolate would carry.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cyclopentolate in any of the three predicted indications.

---

## Literature Evidence

Currently no related literature available for Cyclopentolate in cauda equina syndrome, neurogenic bladder, or irritable bowel syndrome.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications are rated L5 (model prediction only, no supporting studies), and the mechanistic link between an ophthalmic-only anticholinergic agent and a surgical nerve-compression emergency (cauda equina syndrome) is weak and indirect. The absence of a systemic formulation, combined with high CNS penetrance and zero clinical data, means there is no immediate basis for repurposing investment.

**To proceed, the following is needed:**
- Retrieve the full package insert (FDA labeling) to document approved indications, warnings, and contraindications
- Confirm mechanism of action via DrugBank API (M-subtype selectivity profile, receptor binding data)
- Assess whether a systemic formulation of cyclopentolate is pharmacologically and toxicologically feasible before pursuing bladder or bowel indications
- For neurogenic bladder specifically: conduct a preclinical comparison study between cyclopentolate and established bladder-selective muscarinic antagonists (oxybutynin, solifenacin) to establish whether any differentiation exists
- For cauda equina syndrome: reconsider this prediction as a model artifact — the link is too indirect to justify a repurposing program; neurogenic bladder is the more scientifically coherent primary target within this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

