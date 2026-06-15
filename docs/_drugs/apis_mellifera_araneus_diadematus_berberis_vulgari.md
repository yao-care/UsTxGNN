---
layout: default
title: Apis Mellifera Araneus Diadematus Berberis Vulgari
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 0
---

# Apis Mellifera Araneus Diadematus Berberis Vulgari
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

The background skill-check has completed (result: skip) — confirming the `txgnn-pipeline` skill was not needed for this report-generation task. The evaluation report above is the final output.

---

**Summary of key findings:**

| Issue | Detail |
|-------|--------|
| Entity resolution failure | 11-ingredient homeopathic string → `drugbank_id: null` → no KG node |
| TxGNN output | `predicted_indications: []` — zero predictions generated |
| Regulatory status | 0 Taiwan licenses; not marketed in any jurisdiction on record |
| Safety data | All fields return `[Data Gap]`; three components carry high-risk profiles at non-homeopathic doses |
| Decision | **Hold** — re-submit as decomposed individual ingredients after DrugBank mapping |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

