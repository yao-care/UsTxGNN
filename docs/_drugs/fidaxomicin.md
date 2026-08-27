---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 706
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Fidaxomicin: From Clostridioides difficile Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrolide antibiotic whose established use is treating *Clostridioides difficile* infection (CDI), acting locally in the gut with minimal systemic absorption. The TxGNN model predicts it may be effective for **Staphylococcal Scalded Skin Syndrome (SSSS)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying rationale explicitly flags a mechanistic contradiction rather than support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridioides difficile* infection (CDI) — not present in local license records, but referenced consistently across the evidence pack's mechanistic analysis |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for fidaxomicin is currently a data gap. Based on information available elsewhere in the evidence pack, fidaxomicin is a narrow-spectrum macrolide that inhibits bacterial RNA polymerase and is used for CDI specifically because it acts locally within the gut lumen — it is **almost not systemically absorbed** after oral dosing.

SSSS, by contrast, is not primarily a bacterial-burden problem: it is caused by exfoliative toxins produced by *Staphylococcus aureus* and requires drug exposure at the skin/systemic level to have any therapeutic effect. Because fidaxomicin's defining pharmacokinetic property is the *absence* of meaningful systemic or dermal concentration, the evidence pack's own mechanistic rationale for this candidate concludes it is "only a TxGNN score association, without substantive mechanism or clinical support."

In short, the antimicrobial spectrum may theoretically overlap with *S. aureus*, but the route/exposure requirements of SSSS are incompatible with how fidaxomicin actually behaves in the body. This is a case where the prediction score is high but the underlying pharmacology argues against, rather than for, repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Fidaxomicin currently holds no active license records in this dataset (0 NDAs; market status: Not Marketed). No authorization details are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are zero clinical trials and zero publications supporting this specific indication (Evidence Level L5), and the evidence pack's own mechanistic analysis argues that fidaxomicin's negligible systemic absorption makes it pharmacologically unsuited to a toxin-mediated, exposure-dependent skin condition like SSSS. This is a low-confidence, model-only signal.

**To proceed, the following is needed:**
- Verified mechanism-of-action and pharmacokinetic data (systemic/dermal exposure levels) from DrugBank or primary literature
- TFDA/FDA labeling data (warnings, contraindications) — currently a blocking data gap
- Any preclinical or in-vitro data specifically testing fidaxomicin activity in toxin-mediated staphylococcal skin disease, given the mechanistic contradiction identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

