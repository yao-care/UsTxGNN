---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 1079
evidence_level: L5
indication_count: 6
---

# Pregabalin
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

# Pregabalin: From Neuropathic Pain/Epilepsy to Tendinitis

## One-Sentence Summary

> Pregabalin (DrugBank ID: DB00230) is an α2δ calcium-channel ligand best known globally for neuropathic pain, epilepsy adjunct therapy, and fibromyalgia (registry-level original indication data is not available in this evidence pack).
> The TxGNN model's top-ranked prediction is **Tendinitis**, but this is currently supported only by **0 directly relevant clinical trials** and **6 loosely related publications**, none of which test pregabalin for tendon inflammation itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (`original_indications` is empty; pregabalin is globally marketed for neuropathic pain, epilepsy adjunct, and fibromyalgia) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not on file (`original_moa: [Data Gap]`). Based on established pharmacology, pregabalin binds the α2δ subunit of voltage-gated calcium channels, reducing release of excitatory neurotransmitters (glutamate, substance P) — the basis for its analgesic and anticonvulsant effects.

The link to tendinitis, however, is indirect. The available literature places pregabalin in **perioperative pain control** after rotator cuff (shoulder tendon) surgery and in **peripheral nerve compression syndromes near tendons** — not in the inflammatory or structural pathology of tendinitis itself. In other words, the evidence supports pregabalin as an adjunct analgesic in patients who happen to have tendon-related surgery or injury, not as a treatment that modifies tendon inflammation or healing.

Because of this gap between "pain control around a tendon problem" and "treating the tendon problem," the mechanistic rationale is rated weak, consistent with the L4/Hold classification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT (retrospective cohort) | J Orthop Sci | Evaluated pregabalin's analgesic and opioid-sparing effect after arthroscopic rotator cuff repair; evidence for use in this multimodal regimen remains limited. |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin produced pain scores comparable to interscalene brachial plexus block after rotator cuff repair — pain-control comparison, not a tendinitis treatment trial. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case Report | Praxis | Describes fluoroquinolone (ciprofloxacin)-associated tendinopathy — unrelated to pregabalin; only tangentially about tendon injury. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case Report | Pain Practice | Case of posterior femoral cutaneous nerve impingement from hamstring tendonitis; does not involve pregabalin treatment. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial/Commentary | Arthroscopy | Commentary on piriformis syndrome diagnosis and surgical release; not related to pregabalin or tendinitis pharmacotherapy. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical/Animal | Adv Pharmacol Pharm Sci | Plant extract (Cissus quadrangularis) tested in vincristine-induced neuropathy model; no pregabalin or tendinitis relevance. |

---

## Market Information

No marketing authorization is currently on file for this product (0 licenses registered; market status: **Not Marketed**).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are not currently available in this evidence pack — DG001 flags TFDA label warnings/contraindications as a **Blocking** gap that prevents a formal S1 safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between pregabalin and tendinitis is indirect (perioperative analgesia around tendon surgery, not tendon inflammation itself), no clinical trials directly test this indication, and evidence level is L4. Additionally, a **Blocking** data gap (DG001 — TFDA warnings/contraindications) prevents any safety evaluation from proceeding.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety review
- Formal mechanism-of-action documentation (DG002, High) — needed to properly assess mechanistic relevance to tendinitis
- A trial or study directly testing pregabalin's effect on tendon inflammation/healing, rather than only perioperative pain control
- Re-evaluation against alternative predicted indications in this pack (e.g., migraine, rank 5) which currently show substantially stronger evidence (L2, multiple RCTs and a Cochrane review) and may warrant prioritization over tendinitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

