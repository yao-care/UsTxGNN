---
layout: default
title: Telotristat Ethyl
parent: 僅模型預測 (L5)
nav_order: 626
evidence_level: L5
indication_count: 2
---

# Telotristat Ethyl
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

# Telotristat Ethyl: From Carcinoid Syndrome Diarrhea to Cauda Equina Syndrome

## One-Sentence Summary

Telotristat ethyl (Xermelo®) is a selective tryptophan hydroxylase 1 (TPH1) inhibitor approved by the US FDA for carcinoid syndrome diarrhea in adults whose symptoms are inadequately controlled by somatostatin analog therapy.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, however with **0 clinical trials** and **0 publications** currently supporting this direction, the evidentiary foundation is entirely absent.
Given the extremely weak mechanistic link and lack of any supporting data, this candidate is not recommended for further development at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Carcinoid syndrome diarrhea (US FDA-approved; not marketed in Taiwan) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of NDAs (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, telotristat ethyl is a selective inhibitor of tryptophan hydroxylase 1 (TPH1) — the rate-limiting enzyme in peripheral serotonin biosynthesis — acting primarily within gastrointestinal enterochromaffin cells. By reducing intestinal serotonin production, it alleviates carcinoid syndrome diarrhea in patients with serotonin-secreting neuroendocrine tumors. It does not cross the blood-brain barrier and does not meaningfully inhibit central TPH2.

Cauda equina syndrome is a structural neurological emergency caused by mechanical compression of the nerve roots below L1 (most commonly from disc herniation, epidural hematoma, abscess, or tumor). Its pathophysiology is fundamentally biomechanical and inflammatory at the spinal level — not driven by peripheral serotonin excess. While serotonin does play a minor modulatory role in spinal pain circuits, the relevant receptors (5-HT₂, 5-HT₃, 5-HT₄) in that context are centrally located and would not be meaningfully reached by telotristat's gut-restricted TPH1 inhibition.

The repurposing rationale provided in this evidence pack explicitly flags the mechanistic link as "extremely weak," attributing the high TxGNN score to a likely knowledge graph topological artifact: serotonin's broad membership in neurological network nodes generates spurious signal rather than a genuine biological bridge between peripheral gut serotonin reduction and cauda equina nerve root compression. No independent evidence supports this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Telotristat ethyl is not currently marketed in Taiwan. No NDA submissions were identified in the Taiwan FDA database as of the data cutoff (2026-06-22).

> **Reference note:** Telotristat ethyl is commercially available in the United States as **Xermelo®** (Lexicon Pharmaceuticals), approved by the US FDA for carcinoid syndrome diarrhea in combination with somatostatin analog therapy. Stakeholders should consult the US FDA prescribing information for reference safety, dosing, and indication data in the absence of Taiwan-specific labeling.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.38%, this score likely reflects a knowledge graph topological artifact rather than a true mechanistic signal; cauda equina syndrome is a structural neurological emergency with no plausible connection to peripheral gut serotonin inhibition, and there is zero supporting clinical or preclinical evidence.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full mechanism of action from DrugBank API or the Xermelo® US prescribing information to formally document TPH1-selective inhibition profile
- **Taiwan TFDA package insert**: Required to complete S1 safety screening (currently a blocking data gap — DG001)
- **Biological plausibility study**: At minimum, a published preclinical study demonstrating that peripheral serotonin pathway modulation affects cauda equina syndrome outcomes would be required before this hypothesis can advance
- **Knowledge graph audit**: Investigate whether this high-scoring prediction is reproducibly a false positive due to serotonin's broad neurological network membership in the TxGNN knowledge graph, to improve future prediction quality
- **Secondary indication reassessment**: The second-ranked prediction (neurogenic bladder, rank 2) carries a slightly stronger theoretical rationale via pelvic serotonergic bladder control pathways, but is also L5 evidence and uses an "obsolete" disease node — this should be remapped to current terminology before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

