---
layout: default
title: Valrubicin
parent: 僅模型預測 (L5)
nav_order: 1281
evidence_level: L5
indication_count: 10
---

# Valrubicin
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

# Valrubicin: From Bladder Carcinoma In Situ to Colonic Neoplasm

## One-Sentence Summary

> Valrubicin is an anthracycline-class cytotoxic agent historically used as an intravesical instillation for BCG-unresponsive carcinoma in situ of the urinary bladder.
> The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph association with no direct experimental or clinical validation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bladder carcinoma in situ (BCG-unresponsive NMIBC), intravesical instillation — noted in mechanistic rationale; no formal TFDA license record available |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for valrubicin is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, valrubicin is described as an **anthracycline-class cytotoxic agent** acting via DNA intercalation and topoisomerase II inhibition. Its established efficacy is in **local, intravesical treatment of bladder carcinoma in situ** — a setting defined by direct bladder-wall contact, not systemic exposure.

The mechanistic rationale for extending this to colonic neoplasm is weak: as a broad-spectrum cytotoxic agent, valrubicin could theoretically exert non-specific antiproliferative activity against any rapidly dividing malignant tissue, including colorectal cancer. However, there is no pharmacokinetic data on systemic or enteral exposure, no preclinical evidence of activity in colonic tissue, and no clinical experience outside the bladder. Systemic toxicity risks relevant to anthracyclines (myelosuppression, cardiotoxicity) are explicitly noted as **unknown** in this new context.

It is also important to note that 9 of the top 10 TxGNN-ranked predictions for this drug are colon/cecum-related nodes, and several of them (lymphangioma, lipoma, villous adenoma, leiomyoma, cavernous hemangioma, benign neoplasm of cecum) are **benign, non-proliferative, or low-grade lesions for which cytotoxic chemotherapy has no established rationale or clinical role**. This pattern suggests the model may be picking up a graph-clustering artifact around "colon"-adjacent disease nodes rather than a genuine, differentiated mechanistic signal for colonic neoplasm specifically. This should temper confidence in the rank-1 prediction as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Valrubicin is **not currently marketed in Taiwan** (0 licenses on record). No TFDA license, product, or approved-indication data is available in this evidence pack.

---

## Cytotoxicity

Valrubicin is an anthracycline-class chemotherapeutic agent originally indicated for a malignant condition (bladder carcinoma in situ), meeting the criteria for inclusion of this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Anthracycline class) |
| Myelosuppression Risk | Unassessed in this context — original use is local/intravesical; systemic myelosuppression and cardiotoxicity risk under a colonic-neoplasm (presumably systemic) treatment paradigm is explicitly unknown |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | If systemic use were ever pursued: CBC with differential, cardiac function/LVEF (anthracycline class effect), liver and renal function |
| Handling Protection | Yes — cytotoxic/hazardous drug handling precautions required per standard chemotherapy handling protocols |

---

## Safety Considerations

- **Drug Interactions**: DDI database query returned no interactions on record (0 results found).
- Formal TFDA label warnings and contraindications have not yet been retrieved (blocking data gap — see remediation below); until obtained, safety evaluation cannot proceed to the next stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, knowledge-graph-only prediction with zero supporting clinical trials or literature, for a drug not currently marketed in Taiwan and with a blocking gap in TFDA label safety data. The mechanistic case is speculative (local-only original indication vs. a presumed systemic new indication), and the clustering of mostly benign/low-grade lesions among the top 10 predictions raises concern about prediction specificity.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — Blocking gap, required before any S1 safety screening
- Confirmed mechanism of action via DrugBank API — High-priority gap, needed for mechanistic-link analysis
- Preclinical evidence of activity in colonic/colorectal tissue (in vitro/in vivo) before any clinical hypothesis is pursued
- Pharmacokinetic data on systemic or enteral exposure, given the original formulation is intravesical only
- Re-evaluation of the prediction cluster (colon/cecum benign lesions) to rule out graph-artifact bias before treating the rank-1 colonic neoplasm signal as differentiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

