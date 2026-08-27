---
layout: default
title: Fenbendazole
parent: 僅模型預測 (L5)
nav_order: 697
evidence_level: L5
indication_count: 10
---

# Fenbendazole
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

# Fenbendazole: From Veterinary Antiparasitic Use to Urinary Bladder Carcinoma

## One-Sentence Summary

Fenbendazole is a benzimidazole-class antiparasitic drug used in veterinary medicine and has no approved human indication. The TxGNN model predicts it may be effective for **Urinary Bladder Carcinoma**, but this specific prediction currently has **no clinical trials and no supporting publications** — it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Veterinary antiparasitic (benzimidazole anthelmintic) — not an approved human indication |
| Predicted New Indication | Urinary Bladder Carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fenbendazole is a benzimidazole anthelmintic that, like related drugs in its class (mebendazole, albendazole), binds β-tubulin and disrupts microtubule polymerization — a mechanism mechanistically analogous to established microtubule-targeting anticancer agents such as vincristine and taxanes. Additional reports describe possible p53 activation, GLUT-mediated glucose uptake inhibition, and ferroptosis induction, though these come largely from preclinical and anecdotal sources rather than controlled studies.

For the specific predicted indication "urinary bladder carcinoma," the evidence pack notes this ranking may partly reflect clustering of similar bladder-cancer-subtype nodes within the knowledge graph rather than an independently validated signal — nine of the ten top predicted indications in this evidence pack are bladder cancer subtypes, several of them rare histologic variants, and only one (urinary bladder neoplasm, rank 2) has any literature support at all: two papers on intravesical fenbendazole combination therapy and an unrelated carcinogenesis mechanism study. No clinical trial, in any bladder cancer subtype, currently tests fenbendazole. The prediction should be treated as hypothesis-generating rather than clinically supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but it is unsupported by any clinical trial or publication specific to urinary bladder carcinoma, and fenbendazole has no marketed human formulation or regulatory approval in Taiwan or the US (0 licenses). Combined with a Blocking-severity data gap on TFDA safety labeling, there is no basis to advance beyond model prediction at this time.

**To proceed, the following is needed:**
- TFDA/regulatory-grade safety labeling (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Prospective preclinical or early-phase clinical evidence testing fenbendazole specifically in bladder carcinoma (the only related literature concerns intravesical combination therapy for bladder neoplasm generally, not this specific subtype)
- Human pharmacokinetic and dosing data, since fenbendazole currently has no approved human formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

