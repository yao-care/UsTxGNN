---
layout: default
title: Aconitum Napellus Whole Arsenic Trioxide Datura St
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 0
---

# Aconitum Napellus Whole Arsenic Trioxide Datura St
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

# 12-Ingredient Homeopathic Compound: No TxGNN Repurposing Prediction Available

## One-Sentence Summary

This submission describes a 12-ingredient complex preparation—including Aconitum Napellus, Arsenic Trioxide, Datura Stramonium, Lachesis Muta Venom, and others—consistent with a classical homeopathic or compound naturopathic formula.
The TxGNN model generated **no repurposing predictions** for this entry, as the preparation lacks a unified DrugBank ID and cannot be anchored to a pharmacological node in the knowledge graph.
With zero regulatory approvals, no identified original indications, and no model output, a standard repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | None — TxGNN produced no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 (no model prediction, no clinical studies, no literature) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this compound, so the standard repurposing reasoning does not apply. The 12 listed ingredients are characteristic of a classical homeopathic or complex naturopathic formula — including archetypes such as Arsenicum Album (Arsenic Trioxide), Aconitum, Belladonna-family plants (Datura Stramonium), and animal venoms (Lachesis Muta). In homeopathic preparations, each ingredient is present at extreme dilutions (e.g., 6C, 30C), making the pharmacological behavior fundamentally different from pharmaceutical-grade dosing.

Currently, detailed mechanism of action data is not available. Because the preparation has no unified DrugBank ID and no recognized active pharmaceutical ingredient (API) designation, the TxGNN knowledge graph cannot map it to any drug–target–disease pathway. The model therefore returned an empty prediction set, which is the expected result for unregistered multi-ingredient homeopathic preparations.

Without resolving the data gaps (DG001: package insert warnings; DG002: MOA data), any mechanistic claim about this preparation's repurposing potential would be speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This preparation has **0 recorded regulatory approvals**. It is not currently marketed in any identified jurisdiction within the database.

---

## Cytotoxicity

**Arsenic Trioxide (As₂O₃)** appears explicitly in the ingredient list. At pharmaceutical concentrations, Arsenic Trioxide is an FDA-approved antineoplastic agent (indicated for Acute Promyelocytic Leukemia). This section is included for completeness, with the critical caveat that the homeopathic context fundamentally alters the risk profile.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Arsenic Trioxide = conventional cytotoxic at pharmaceutical doses; homeopathic dilution is not classified as cytotoxic |
| Myelosuppression Risk | High at pharmaceutical concentrations (leukopenia, thrombocytopenia); not applicable at homeopathic dilutions |
| Emetogenicity Classification | Low to moderate at pharmaceutical concentrations; not applicable at homeopathic dilutions |
| Monitoring Items | If pharmaceutical-grade Arsenic Trioxide is used: ECG (QTc interval), CBC with differential, liver function, renal function, serum electrolytes |
| Handling Protection | Pharmaceutical-grade Arsenic Trioxide requires cytotoxic handling protocols; homeopathic preparations do not typically require this |

---

## Safety Considerations

Please refer to the package insert for safety information.

Several ingredients in this preparation carry significant intrinsic toxicity at non-homeopathic concentrations. These are flagged for awareness:

- **Aconitum Napellus**: Contains aconitine, a highly toxic alkaloid; cardiovascular (arrhythmia) and neurotoxic effects even at small doses
- **Datura Stramonium**: Contains tropane alkaloids (atropine, scopolamine, hyoscyamine); severe anticholinergic toxicity
- **Strychnos Ignatii Seed (Ignatia Amara)**: Contains strychnine; CNS stimulant and convulsant at toxic concentrations
- **Lachesis Muta Venom**: Hemorrhagic and neurotoxic components derived from Bushmaster snake
- **Arsenic Trioxide**: Cardiotoxic (QTc prolongation), hepatotoxic, and neurotoxic at systemic concentrations

At classical homeopathic dilutions, these risks are considered theoretical by homeopathic practice conventions. However, regulatory acceptance of multi-ingredient preparations containing these substances varies significantly by jurisdiction and requires explicit legal review before any market-entry activity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no repurposing predictions for this entry because the 12-ingredient homeopathic preparation cannot be mapped to a pharmacological node in the knowledge graph without a unified DrugBank ID or API designation. There is no regulatory foundation, no original indication, and no model output to evaluate.

**To proceed, the following is needed:**

- **Clarify product identity**: Confirm whether this is a registered homeopathic product and identify its intended therapeutic use and dilution levels
- **Resolve Data Gap DG002 (MOA)**: Obtain DrugBank entries for individual active components, particularly Arsenic Trioxide, Aconitum, and Datura, if each is to be evaluated as a standalone repurposing candidate
- **Resolve Data Gap DG001 (Package Insert)**: Retrieve the package insert (if any) from the relevant regulatory agency to extract approved warnings and contraindications
- **Determine evaluation strategy**: Decide whether to (a) evaluate this multi-ingredient product as a whole, or (b) split into individual ingredient-level repurposing analyses — the latter is more compatible with the TxGNN framework
- **Re-run TxGNN pipeline**: After resolving DG001 and DG002, re-submit with individual DrugBank IDs for each pharmacologically active component
- **Legal/regulatory review**: Confirm jurisdiction-specific rules for registering preparations containing Aconitum, Arsenic, Datura, and snake venom
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

