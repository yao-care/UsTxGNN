---
layout: default
title: Chloroprocaine
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 1
---

# Chloroprocaine
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

以下是根據 Evidence Pack 產生的藥師評估報告：

---

# Chloroprocaine: From Regional Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Chloroprocaine is an ester-type local anesthetic widely used for regional and spinal anesthesia procedures.
The TxGNN model assigns it a **99.01% score** for **cauda equina syndrome (CES)**, with **1 observational study** and **4 publications** co-mentioning both terms.
Critically, however, all available evidence identifies chloroprocaine as a documented **iatrogenic cause** of CES — not a potential treatment — indicating this is a false positive prediction driven by adverse-event co-occurrence in the literature rather than any therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in this database (known pharmacological class: ester-type local anesthetic for regional/spinal anesthesia) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.01% (rank: 21,288) |
| Evidence Level | L5 |
| US Market Status | Not marketed (no registered products in database) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided dataset. Based on information in the clinical literature, chloroprocaine is an ester-type local anesthetic whose primary mechanism involves **blocking voltage-gated sodium channels (Nav)**, thereby inhibiting nerve impulse conduction and producing reversible regional anesthesia. It is used clinically for short-duration spinal, epidural, and infiltration anesthesia.

The relationship between chloroprocaine and cauda equina syndrome in the medical literature is **not therapeutic — it is iatrogenic and in the opposite causal direction.** Intrathecal injection of chloroprocaine, particularly older formulations containing preservatives (e.g., sodium bisulfite), has been reported as a direct cause of CES. The proposed injury mechanism involves sustained Nav blockade producing localised nerve root hypoxia and cytotoxicity, leading to the characteristic bladder, bowel, and lower-limb deficits of CES.

The TxGNN model's high probability score (99.01%) reflects the **high co-occurrence frequency** of "chloroprocaine" and "cauda equina syndrome" in the indexed literature. However, this co-occurrence captures an adverse drug reaction relationship — **drug → disease (harm)** — rather than a treatment indication — **disease → drug (therapy)**. This represents a known blind spot of graph-based repurposing models when the drug and disease appear together predominantly in a safety or complication context. No mechanistic pathway has been identified by which chloroprocaine could reverse or treat CES.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02067806](https://clinicaltrials.gov/study/NCT02067806) | N/A | Completed | 394 | Prospective observational safety study monitoring neurological adverse events — including TNS and **CES as an adverse outcome** — following intrathecal 1% 2-chloroprocaine. This trial monitors CES as a risk to be detected, not as a condition being treated. |

> ⚠️ **Note:** The sole identified trial does not evaluate chloroprocaine as a treatment for CES. It is a pharmacovigilance study designed to measure the incidence of CES and other neurological harms caused by the drug.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiologica Scandinavica | Randomised comparison of 2-chloroprocaine versus lidocaine (with fentanyl) for selective spinal anesthesia in outpatient TURP — evaluates efficacy and safety as an anesthetic agent, not as a CES treatment. |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiologica Scandinavica | Comprehensive review of 2-chloroprocaine for spinal anaesthesia; discusses its candidacy to replace lidocaine while noting that high-dose preservative-containing formulations have been associated with neurological sequelae including CES. |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Safety | Broad review of regional anaesthesia complications; identifies CES as a rare but serious complication of central neuraxial blockade, with chloroprocaine among implicated agents. |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case Report | Regional Anesthesia | Two case reports of CES following combined spinal-epidural anesthesia; review of prior literature implicating lidocaine, chloroprocaine, and procaine in CES aetiology — confirms causation, not treatment. |

> ⚠️ **Note:** All four publications document chloroprocaine as a **contributing cause** of CES. None describe or support its use as a therapeutic agent for CES.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this dataset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of chloroprocaine for cauda equina syndrome is a **confirmed false positive**. The drug is a documented iatrogenic cause of CES, not a treatment for it; the causal direction in all retrieved evidence runs from drug to disease (harm), not disease to drug (therapy). Pursuing this indication would not only lack therapeutic rationale but would also raise direct patient safety concerns.

**To proceed meaningfully, the following would be required:**

- **False-positive triage:** Flag this candidate in the TxGNN output pipeline as an adverse-reaction co-occurrence pattern, not a repurposing signal — to prevent downstream clinical misinterpretation.
- **Model feedback:** Consider enriching TxGNN training data or post-processing filters to distinguish therapeutic associations from harm/complication associations in the knowledge graph.
- **MOA data retrieval:** Obtain complete DrugBank mechanism data (DG002) to improve future mechanistic plausibility screening for chloroprocaine predictions.
- **Package insert review:** Retrieve TFDA/FDA label (DG001) to complete the safety profile before any further evaluation of this compound in other indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

