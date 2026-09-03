---
layout: default
title: Ziconotide
parent: 僅模型預測 (L5)
nav_order: 1303
evidence_level: L5
indication_count: 10
---

# Ziconotide
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

# Ziconotide: From Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

> Ziconotide's original indication and mechanism of action are not documented in the current evidence pack (data gap), and the drug is not marketed in Taiwan.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> with **0 clinical trials** and **1 publication** (a single case report) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for the drug record itself is not available (`original_moa` is flagged as a data gap). However, the evidence pack's repurposing rationale for this candidate provides mechanistic detail: Ziconotide is a selective N-type (Cav2.2) voltage-gated calcium channel blocker acting at primary afferent nerve terminals in the spinal dorsal horn, where it inhibits release of pain-related neurotransmitters including substance P, glutamate, and CGRP.

This mechanism has a theoretical overlap with migraine pathophysiology, which involves trigeminovascular system sensitization and CGRP release. That said, this connection is currently supported only by a single intrathecal case report, without any systematic clinical trials. Ziconotide's intrathecal administration also carries well-known serious neuropsychiatric adverse effects (cognitive impairment, hallucinations), so any exploration of this indication would require careful risk-benefit assessment.

Because original indication data is not available in this evidence pack, a direct comparison between the original and predicted indications cannot be made at this time; this assessment relies solely on the mechanistic rationale documented above.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Case Report | Journal of Pain Research | Resolution of chronic migraine headaches following intrathecal ziconotide administration; ziconotide described as an N-type calcium channel blocker used for chronic severe pain without tolerance/dependency issues seen with opioids |

---

## Taiwan Market Information

No marketing authorizations are currently on record for ziconotide in Taiwan (`total_licenses: 0`, `market_status: 未上市`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all flagged as blocking data gaps in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting the migraine indication is currently limited to a single case report (L4, no clinical trials), the drug is not marketed in Taiwan, and safety data (warnings, contraindications, drug interactions) are entirely unavailable — including a **Blocking**-severity gap (TFDA label warnings/contraindications) that prevents this candidate from advancing past the initial safety screening stage.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (Blocking gap — required before any S1 safety assessment)
- Confirmed mechanism of action data via DrugBank (High-priority gap)
- Systematic clinical evidence (case series, observational study, or trial) beyond the single existing case report
- Explicit evaluation of intrathecal-route feasibility and risk-benefit profile given known neuropsychiatric adverse effects, before considering migraine as a research direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

