---
layout: default
title: Benzyl Alcohol
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
---

# Benzyl Alcohol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Benzyl Alcohol: From Pharmaceutical Preservative to Bronchitis

## One-Sentence Summary

Benzyl alcohol is an aromatic alcohol widely used as a pharmaceutical preservative and excipient, with no established systemic therapeutic indication in the regulatory record.
The TxGNN model predicts it may be effective for **Bronchitis**, with a prediction score of 99.46%.
However, **0 clinical trials** and **4 publications** are available — and critically, all literature documents benzyl alcohol as a **cause** of bronchitis when nebulized, not a treatment. This prediction is very likely a model false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No established therapeutic indication (used primarily as pharmaceutical preservative/excipient) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Benzyl alcohol is an aromatic alcohol primarily known as a pharmaceutical excipient — it serves as a bacteriostatic preservative in injectable solutions and nebulizer saline, and also has local anesthetic properties when applied topically. There is no published mechanistic basis for benzyl alcohol as a therapeutic agent in bronchitis.

The relationship between benzyl alcohol and bronchitis in the literature is one of **causation, not treatment**. When bacteriostatic saline containing 0.9% benzyl alcohol (as preservative) is nebulized and inhaled, benzyl alcohol itself acts as a tracheobronchial irritant and has been documented to induce bronchitis in healthy adults. This is the exact opposite of a therapeutic relationship.

The TxGNN model's high prediction score (99.46%) in this case is almost certainly a **false positive arising from co-occurrence bias**. The model likely detected statistical co-occurrence of "benzyl alcohol" and "bronchitis" in the knowledge graph or literature corpus, but misinterpreted a causal-harm relationship as a therapeutic one. This is a known failure mode for graph-based repurposing models and warrants no further development without fundamental mechanistic reframing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7807035](https://pubmed.ncbi.nlm.nih.gov/7807035/) | 1995 | Clinical Observation / Case Series | The Journal of Family Practice | Investigated whether nebulized bacteriostatic saline containing benzyl alcohol as a preservative is an irritant to the tracheobronchial mucosa in healthy adults — **benzyl alcohol identified as the causative irritant** |
| [2355429](https://pubmed.ncbi.nlm.nih.gov/2355429/) | 1990 | Clinical Case Report | JAMA | Documented nebulizer bronchitis **induced by** bacteriostatic saline (containing benzyl alcohol) — causal direction is BA → bronchitis, not therapeutic |
| [7775900](https://pubmed.ncbi.nlm.nih.gov/7775900/) | 1995 | Clinical Commentary / Review | The Journal of Family Practice | Commentary on nebulized saline and bronchitis relationship; contextually related to the above benzyl alcohol preservative issue |
| [36747926](https://pubmed.ncbi.nlm.nih.gov/36747926/) | 2023 | Phytochemical Analysis | Heliyon | Evaluation of Senna tora plant bioactive molecules for antioxidant, anti-inflammatory, and antibacterial activity against conditions including bronchitis — benzyl alcohol not the subject of investigation |

> ⚠️ **Critical Interpretation Note**: All four publications either show benzyl alcohol **causing** bronchitis (PMIDs 7807035, 2355429, 7775900) or do not study benzyl alcohol as a treatment at all (PMID 36747926). None of the literature supports a therapeutic role for benzyl alcohol in bronchitis.

---

## US Market Information

Benzyl alcohol has no approved drug product licenses in the United States or Taiwan under this INN. It is not authorized as an active pharmaceutical ingredient for any marketed indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Available literature raises a specific inhalation safety concern — nebulized benzyl alcohol (as a bacteriostatic preservative in saline) has been documented to cause tracheobronchial irritation and bronchitis in healthy adults. This is directly relevant to any proposed respiratory route of administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.46%), but all available evidence reveals a **causation-direction reversal**: benzyl alcohol is a documented tracheobronchial irritant that induces bronchitis upon inhalation — it does not treat the condition. This is a classic false positive arising from co-occurrence misinterpretation in the knowledge graph, not a genuine therapeutic signal. There is no mechanistic basis, no clinical trial, and no supportive literature to justify advancement.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis for benzyl alcohol treating bronchitis (e.g., anti-inflammatory or antimicrobial mechanism acting on airway mucosa) — currently none exists in the published literature
- Preclinical in vitro or in vivo data demonstrating anti-bronchitis efficacy (not via inhalation route, given the known irritant profile)
- Clarification of the TxGNN graph edge that generated this prediction — the model likely requires a directed therapeutic vs. adverse-effect edge distinction to avoid this class of false positive
- Complete MOA data from DrugBank to rule out any off-target mechanism not yet characterized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

