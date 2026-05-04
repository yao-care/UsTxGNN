---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

The txgnn-pipeline skill is about deployment and pipeline management, not report generation — the detailed reporting instructions are in the system prompt. Proceeding to produce the evaluation report based on the Evidence Pack.

---

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab (Benlysta®) is a human monoclonal antibody targeting BLyS/BAFF that is globally approved for the treatment of systemic lupus erythematosus (SLE) and lupus nephritis, reducing B cell survival and pathogenic autoantibody production.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, currently ranked #1 with a prediction score of **99.96%**.
However, only **1 tangentially related clinical trial** and **no published literature** exist for this specific pairing, and the mechanistic rationale is weak — making this a hypothesis-generating signal rather than an actionable drug repurposing candidate at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic Lupus Erythematosus (SLE) / Lupus Nephritis (from public approval record; not present in dataset) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| US Market Status | Not marketed (per dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, Belimumab is a fully human IgG1λ monoclonal antibody that specifically binds to soluble B-Lymphocyte Stimulator (BLyS, also known as BAFF). By blocking BLyS from engaging its receptors on B cells, it curtails B cell survival, maturation, and differentiation — ultimately reducing the production of pathogenic autoantibodies. This mechanism is highly effective in autoantibody-driven diseases such as SLE.

Primary release disorder of platelets, however, is fundamentally different in origin. It refers to hereditary defects in platelet granule secretion — specifically failures of dense granules (δ-granules) or α-granules to release their contents upon platelet activation (e.g., Hermansky-Pudlak syndrome, Chediak-Higashi syndrome). These conditions arise from genetic mutations affecting intracellular trafficking and secretory pathways, not from B cell activity or circulating autoantibodies. Belimumab's BLyS-inhibition pathway has no direct mechanistic relevance to this pathology.

The TxGNN model's very high prediction score (99.96%) is most likely a consequence of graph proximity effects in the knowledge graph — broad connectivity between "platelet disorder" and general "immune disease" nodes — rather than a true biological signal. Without supporting clinical trials or literature, and with a misaligned mechanism, this prediction is best regarded as a false positive for this specific indication, warranting a Hold decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label mechanistic study of belimumab (10 mg/kg IV) in PLA2R autoantibody-positive idiopathic membranous glomerulonephropathy. Evaluated efficacy, safety, and biomarker-autoantibody relationships over 24 weeks. **Relevance to primary platelet release disorder is nil** — the trial was retrieved because belimumab was the study drug, not because of any connection to platelet pathology. It provides background evidence of belimumab's Phase 2 experience in immune-mediated disease only. |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US market authorizations are recorded in this dataset for Belimumab.

> **Data Note:** Belimumab (Benlysta®) holds FDA approval for active, autoantibody-positive SLE in adults and pediatric patients ≥5 years, and for active lupus nephritis. If the dataset reflects Taiwan (TFDA) regulatory status, "not marketed" is consistent with TFDA records as of the data cutoff. US NDA details should be verified via FDA Drugs@FDA separately.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Primary release disorder of platelets is a hereditary platelet granule secretion defect; its pathophysiology does not involve B cell activation or autoantibody-driven mechanisms, and therefore Belimumab's core BLyS-inhibiting mechanism is biologically misaligned. The single clinical trial retrieved (NCT01610492) evaluated a different immune-mediated condition entirely and provides no efficacy signal for platelet release disorders.

**To proceed, the following is needed:**

- Obtain full MOA and pharmacology data from DrugBank (DG002) to formally document the BLyS-inhibition mechanism and verify whether any downstream platelet-biology interaction exists
- Retrieve and parse the FDA/TFDA package insert (DG001) to complete the safety and contraindication profile before any further evaluation
- Commission a targeted literature search for BLyS/BAFF expression in megakaryocytes or platelet biology to determine if any mechanistic bridge exists
- **Consider re-prioritizing evaluation to Rank 4 (Fetal and Neonatal Alloimmune Thrombocytopenia / FNAIT)**, which is the only indication in this dataset with a plausible immune-mediated mechanism (maternal anti-HPA IgG alloantibodies); however, FNAIT evaluation must begin with a dedicated pregnancy safety gating step given belimumab's transplacental passage as an IgG1 antibody
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

