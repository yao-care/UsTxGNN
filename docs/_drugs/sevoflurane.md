---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 1158
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevoflurane: From General Anesthesia to Prinzmetal Angina (and 9 Other Low-Confidence Candidates)

## One-Sentence Summary

> Sevoflurane is an inhalational general anesthetic, originally used for the induction and maintenance of general anesthesia during surgery.
> The TxGNN model's top-ranked prediction suggests possible relevance to **Prinzmetal Angina**,
> but **no clinical trials and no literature** currently support this specific therapeutic use — the score appears to reflect knowledge-graph co-occurrence (anesthetic ↔ cardiovascular disease) rather than a genuine treatment signal.
> Across all 10 predicted indications reviewed in this evidence pack, none reach an evidence level above L4, and every candidate is scored **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (induction/maintenance) — no formal indication text available; drug is not currently marketed in this jurisdiction |
| Predicted New Indication | Prinzmetal Angina (rank 1 of 10 candidates reviewed) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (no clinical trials, no literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, sevoflurane is an inhalational general anesthetic acting primarily via GABA-A receptor modulation, and is used exclusively for surgical anesthesia. It also has documented coronary vasodilatory and cardioprotective ("ischemic preconditioning") effects observed during anesthetic administration, which is the theoretical basis the TxGNN model appears to be drawing on for the Prinzmetal angina association.

However, there is no direct clinical or mechanistic study demonstrating that sevoflurane treats coronary vasospasm. The relationship between the original use (surgical anesthesia) and the predicted indication is not a natural disease-progression link — unlike typical repurposing cases (e.g., a drug moving from one cancer type to a related one), sevoflurane's connection to nearly all 10 predicted indications in this pack (Prinzmetal angina, Tourette syndrome, fibromyalgia, tendinitis, various myositis subtypes, migraine, etc.) is almost entirely mediated by *perioperative co-occurrence*: patients with these underlying conditions who happen to receive sevoflurane for unrelated surgery, generating case reports about **anesthetic management of the disease**, not **treatment of the disease with sevoflurane**.

This pattern is visible across the literature retrieved: papers on tendinitis/rotator cuff repair, fibromyalgia, inclusion body myositis, and migraine all describe sevoflurane as the anesthetic used *during surgery in patients who already have the condition*, or compare its perioperative side-effect profile (e.g., postoperative headache) to other anesthetics. None describe a therapeutic mechanism directed at the disease itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina (rank 1 candidate).

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina (rank 1 candidate).

---

## Other Predicted Indications (Supplementary Overview)

Because this evidence pack scored 10 candidate indications and **all were assessed as "Hold"**, a summary is included for transparency:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Evidence Available | Note |
|------|----------------------|-------------|-----------------|---------------------|------|
| 1 | Prinzmetal angina | 99.78% | L5 | None | Co-occurrence-based; no direct support |
| 2 | Tourette syndrome | 99.50% | L5 | None | No mechanistic basis |
| 3 | Fibromyalgia | 99.42% | L4 | 1 case report | Anesthetic management, not treatment |
| 4 | Tendinitis | 99.41% | L4 | 11 papers | All perioperative/anesthesia-comparison studies |
| 5 | Myositis fibrosa | 99.41% | L5 | None | No mechanistic basis |
| 6 | Idiopathic granulomatous myositis | 99.41% | L5 | None | No mechanistic basis |
| 7 | Nephrogenic SIAD | 99.40% | L5 | None | Sevoflurane's known renal/ADH effects run counter to, not supportive of, this indication |
| 8 | Trichotillomania | 99.33% | L5 | None | No mechanistic basis |
| 9 | Migraine disorder | 99.23% | L4 | 1 trial + 1 paper | Trial evaluates postoperative headache **risk**, not migraine treatment |
| 10 | Inclusion body myositis | 99.09% | L4 | 1 case report | Anesthetic risk management, not treatment |

**None of these candidates currently warrant progression beyond Hold.**

---

## US Market Information

Sevoflurane is currently **not marketed** in this jurisdiction (0 licenses on record), so no authorization/product table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying evidence pack flags this as a **Blocking data gap** — TFDA/FDA package insert warnings and contraindications have not yet been retrieved, which prevents any S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for sevoflurane are supported only by incidental perioperative literature (case reports of anesthetic management in patients who already have the condition) or by trials measuring anesthesia-related side effects — none demonstrate a therapeutic effect on the predicted disease itself. Evidence level does not exceed L4 for any candidate, and mechanistic rationale is speculative or, in one case (nephrogenic SIAD), potentially contradictory to the predicted benefit.

**To proceed, the following is needed:**
- TFDA/FDA package insert (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Verified mechanism of action data via DrugBank — currently a **High** priority gap (DG002)
- Any preclinical or mechanistic studies specifically testing sevoflurane's therapeutic (not anesthetic-incidental) effect on a candidate disease before advancing past S0
- If pursuing Prinzmetal angina specifically: dedicated pharmacological studies on sevoflurane's effect on coronary vasospasm, distinct from its general cardioprotective anesthesia literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

