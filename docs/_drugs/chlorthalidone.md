---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

Using the `txgnn-pipeline` skill for this report generation task. That skill isn't available as a deferred tool, so I'll proceed directly with the report generation per the Drug Repurposing Evaluation Report Prompt (v5) instructions.

---

# Chlorthalidone: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic with a long-established role in hypertension management, acting by reducing sodium reabsorption in the distal nephron to lower circulating blood volume and blood pressure.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, with **no clinical trials** and **no publications** directly supporting this specific indication.
The high prediction score (99.92%) most likely reflects indirect topological associations in the knowledge graph — particularly between diuretic drug nodes and ocular pressure-related disease nodes — rather than pharmacological evidence of efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (established use; no regulatory data on file for this jurisdiction) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Chlorthalidone is a sulfonamide-derived thiazide-like diuretic. Its primary mechanism of action is inhibition of the sodium-chloride cotransporter (NCC) in the distal convoluted tubule of the kidney, which promotes urinary excretion of sodium and water, reduces plasma volume and preload, and consequently lowers systemic blood pressure. In addition to this dominant renal mechanism, chlorthalidone possesses weak carbonic anhydrase (CA) inhibitory activity — a property shared by the sulfonamide chemical scaffold.

The theoretical bridge to glaucoma runs through this weak CA inhibitory property. Dedicated carbonic anhydrase inhibitors such as acetazolamide (systemic) and dorzolamide (topical) are established glaucoma treatments: by suppressing CA activity in the ciliary epithelium, they reduce aqueous humor production and thereby lower intraocular pressure (IOP). Primary hereditary glaucoma — typically associated with mutations in genes such as *MYOC*, *CYP1B1*, or *LTBP2* — causes impaired trabecular outflow, and elevated IOP is its principal modifiable driver.

However, the mechanistic link is very thin. Chlorthalidone's CA inhibitory potency is substantially weaker than that of acetazolamide, and no systemic diuretic has demonstrated clinically meaningful IOP reduction at therapeutic doses. Furthermore, primary hereditary glaucoma is a monogenic disease in which the underlying structural defect may not be reversible through IOP reduction alone; gene-specific or surgical approaches are often required. The TxGNN model's high score should therefore be interpreted as a knowledge-graph signal requiring experimental validation, not as pharmacological evidence. No clinical trials or literature support this repurposing hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Chlorthalidone holds no regulatory licenses in the queried jurisdiction. No approved product data is on file.

> **Note:** Chlorthalidone (e.g., Hygroton®, Thalitone®) is pharmacologically well-established and has regulatory approvals in multiple major markets for hypertension. The absence of records here reflects the scope of the current regulatory database query, not the global approval status of the compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for chlorthalidone in primary hereditary glaucoma is currently at L5 — model prediction only, with zero supporting clinical trials or publications. The mechanistic rationale (weak carbonic anhydrase inhibition) is biologically plausible but pharmacologically insufficient, and the genetic nature of primary hereditary glaucoma further limits the expected therapeutic impact of a systemic diuretic.

**To proceed, the following would be needed:**

- **Mechanism of action confirmation:** Obtain quantitative CA inhibition data for chlorthalidone (IC₅₀ vs. CA-II) and compare to clinically effective CAIs, to determine if the effect size is pharmacologically meaningful.
- **IOP measurement studies:** Preclinical or observational data demonstrating that therapeutic doses of chlorthalidone produce measurable IOP reduction in patients with or at risk for glaucoma.
- **Genetic subtype mapping:** Evaluate whether any *MYOC*, *CYP1B1*, or *LTBP2* mutation subtypes might specifically benefit from systemic fluid-pressure reduction strategies.
- **Safety data retrieval:** Download and parse the full prescribing information (package insert) to identify key warnings, contraindications, and drug interactions — this is currently a blocking data gap (DG001).
- **Comparative analysis against existing CAIs:** If IOP reduction is confirmed, benchmark chlorthalidone against dorzolamide/brinzolamide (topical) and acetazolamide (systemic) on both efficacy and systemic side effect profile.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

