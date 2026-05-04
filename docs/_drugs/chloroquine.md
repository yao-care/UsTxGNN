---
layout: default
title: Chloroquine
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 4
---

# Chloroquine
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

以下是根據 Evidence Pack 生成的完整報告：

---

# Chloroquine: From Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is a classic antimalarial and antirheumatic agent with decades of historical use in autoimmune conditions, including as an early disease-modifying antirheumatic drug (DMARD).
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (RF+ PJIA)**,
with **no registered clinical trials** and **2 publications** currently supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal authorization on record; historically used for malaria and autoimmune diseases |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, chloroquine is a 4-aminoquinoline compound that accumulates in acidic intracellular compartments and raises intralysosomal pH. This impairs MHC class II antigen processing and presentation, thereby reducing the activation of autoreactive T cells. Chloroquine also blocks endosomal TLR7/9 signaling by preventing endosomal acidification, suppressing the downstream production of pro-inflammatory cytokines and autoantibodies — a cascade central to seropositive autoimmune arthritis.

RF+ polyarticular JIA is the subtype most closely resembling adult seropositive rheumatoid arthritis, characterized by high autoantibody burden (rheumatoid factor positivity), systemic immune activation, and progressive joint destruction. This immunological profile aligns well with chloroquine's multi-target anti-inflammatory mechanism. Its close structural analogue hydroxychloroquine (HCQ) is a current standard DMARD for adult seropositive RA, lending strong mechanistic plausibility to the prediction.

Historically, chloroquine itself was part of the JIA treatment armamentarium. A 1991 Czech controlled trial (PMID 1688268) directly compared Delagil (chloroquine diphosphate) with sulfasalazine in juvenile chronic arthritis patients, and pharmacokinetic data from JIA patients receiving MTX + chloroquine combination therapy has been published (PMID 18021335). The TxGNN model's prediction therefore reflects a historically tested and mechanistically coherent hypothesis — though evidence specific to the RF+ polyarticular subtype remains limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Prospective Cohort | The Journal of Rheumatology | Long-term real-world experience with leflunomide in JIA; provides DMARD treatment context for this patient population |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Case Series | The Journal of Pediatrics | Two RF+ polyarticular JRA patients developed MTX-induced accelerated nodulosis; addition of hydroxychloroquine arrested nodule progression in one case, suggesting HCQ/CQ class activity in this subtype |

---

## Market Information

No market authorization data is available for chloroquine in Taiwan. The drug is not currently marketed under this jurisdiction based on available regulatory records.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings and contraindications data are currently unavailable in this Evidence Pack and require remediation. Chloroquine is known to carry significant cardiac (QT prolongation, atrioventricular block) and ophthalmologic (irreversible retinal toxicity) risks — these must be reviewed against the prescribing information before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials targeting RF+ polyarticular JIA with chloroquine are registered, and the 2 available literature items address this specific subtype only tangentially; evidence currently stands at L4 (historical use and mechanism only), which is insufficient to advance repurposing without additional targeted data.

**To proceed, the following is needed:**

- **Retrieve full safety profile** — Download and parse prescribing information to obtain contraindications and black-box warnings (Data Gap DG001); chloroquine's cardiac and retinal toxicity profile is significantly broader than that of hydroxychloroquine and must be formally characterized before any pediatric use assessment
- **Retrieve MOA data** — Query DrugBank API for complete mechanism of action information (Data Gap DG002)
- **CQ vs. HCQ comparative justification** — Since hydroxychloroquine is already the preferred agent in this drug class for autoimmune arthritis, a formal comparison of benefit-risk profiles is needed to determine whether chloroquine adds incremental value
- **Targeted literature search** — Conduct a systematic search specifically for chloroquine (not hydroxychloroquine) in RF+ polyarticular JIA or seropositive pediatric arthritis
- **Ophthalmologic monitoring protocol** — Define retinal toxicity surveillance requirements given chloroquine's known higher risk vs. HCQ, especially relevant for long-term pediatric use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

