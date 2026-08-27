---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis to Bronchitis

## One-Sentence Summary

Dupilumab is an IL-4Rα-targeting monoclonal antibody whose established indications (documented in the accompanying literature) include moderate-to-severe atopic dermatitis and asthma. The TxGNN model predicts it may also be effective for **Bronchitis**, but this direction is currently supported by only **1 clinical trial** (not conducted in bronchitis patients) and **6 publications** (mostly on asthma/COPD, not bronchitis specifically) — the evidence is indirect, mechanism-based extrapolation rather than direct proof.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (also approved for asthma, CRSwNP — per literature in evidence pack; no Taiwan license record exists to confirm locally) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Market Status (Taiwan) | ✗ Not Marketed |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was flagged as a data gap in this evidence pack (DG002). However, the literature evidence collected for this candidate consistently describes dupilumab as a fully human monoclonal antibody that blocks the shared IL-4/IL-13 receptor subunit (IL-4Rα), thereby inhibiting Th2 ("type 2")-driven inflammation. This mechanism is well documented in the literature underlying its dermatitis and asthma evidence (e.g., PMID 25006719, PMID 28478972).

The rationale for extending to bronchitis rests on the fact that Th2/eosinophilic inflammation is a shared pathway across several airway diseases — asthma, COPD, and eosinophilic bronchitis all involve overlapping IL-4/IL-13-driven mechanisms. Since dupilumab has proven efficacy in asthma (TRAVERSE extension study, PMID 34597534; meta-analysis, PMID 30273510), it is mechanistically plausible that it could benefit bronchitis as well.

That said, the model's own repurposing rationale flags an important caveat: the single registered clinical trial for this pairing (NCT04362501) was actually conducted in chronic rhinosinusitis without nasal polyps (CRSsNP), not bronchitis, and the literature largely addresses asthma/COPD rather than bronchitis itself. This is pharmacological extrapolation, not direct clinical evidence for bronchitis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in **chronic rhinosinusitis without nasal polyps (CRSsNP)** — not a bronchitis-specific trial. Relevance graded "C" (indirect): shares Th2 inflammatory mechanism but different disease population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT Extension (TRAVERSE) | Lancet Respir Med | Long-term safety/efficacy of dupilumab in moderate-to-severe asthma beyond 1 year of treatment |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Meta-analysis | J Asthma | Systematic review/meta-analysis of RCTs on dupilumab efficacy and safety in uncontrolled asthma |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review | Tuberc Respir Dis | Comprehensive review of pharmacologic therapies (including biologics) for preventing COPD exacerbations |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review/Case | Pediatr Pulmonol | Novel therapies for eosinophilic pediatric plastic bronchitis |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | N/A | Expert Opin Pharmacother | Discusses treatment challenges in smoking-induced airway diseases (chronic bronchitis, emphysema, ACO) in asthma patients |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | N/A | Chest | MRI-based evaluation of anti-T2 biologic (dupilumab) effects on lung ventilation in prednisone-dependent severe asthma |

---

## Taiwan Market Information

No TFDA license record exists for dupilumab in this evidence pack (`market_status: 未上市`, `total_licenses: 0`). Regulatory/product data cannot be summarized until a license is registered or obtained.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack — DG001 flags TFDA label/warning data as a blocking gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, and the Th2/IL-4-IL-13 mechanism is biologically plausible for airway inflammatory disease, but the actual evidence base for **bronchitis specifically** is essentially absent — the one trial found is in a different disease (CRSsNP), and the literature centers on asthma/COPD rather than bronchitis. This is model-driven mechanistic extrapolation, not disease-specific clinical evidence, so it does not yet meet the bar to proceed even with guardrails.

**To proceed, the following is needed:**
- A clinical trial or observational study conducted specifically in bronchitis (not asthma/COPD/CRSsNP) patients
- TFDA-approved label data (warnings, contraindications, DDI) to close the S1 blocking gap (DG001)
- Confirmed original indication/MOA sourced from an authoritative regulatory filing, since Taiwan license data is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

