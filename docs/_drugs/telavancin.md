---
layout: default
title: Telavancin
parent: 僅模型預測 (L5)
nav_order: 624
evidence_level: L5
indication_count: 9
---

# Telavancin
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

# Telavancin: From Gram-positive Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Telavancin (Vibativ) is a lipoglycopeptide antibiotic approved internationally for serious gram-positive bacterial infections, including MRSA pneumonia and complicated skin and skin structure infections, though it is not currently approved or marketed in Taiwan.
The TxGNN model predicts it may be effective for **Hyperamylasemia** as its top-ranked new indication,
with **0 clinical trials** and **0 publications** supporting this direction — representing a purely model-driven signal with no empirical evidence base.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (not marketed in Taiwan; internationally approved for gram-positive bacterial infections including MRSA) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed in Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Telavancin is a lipoglycopeptide antibiotic that works by dual mechanisms: inhibiting bacterial cell wall synthesis (by binding to D-Ala-D-Ala terminus of peptidoglycan precursors) and disrupting bacterial membrane integrity. It is active exclusively against gram-positive organisms, with particular utility against methicillin-resistant *Staphylococcus aureus* (MRSA).

The predicted top indication — hyperamylasemia — refers to an elevated serum amylase level, which is a laboratory finding (not an independent disease entity) typically reflecting pancreatic or salivary gland pathology. There is no known mechanistic link between cell wall synthesis inhibition or membrane disruption and the regulation of amylase secretion or clearance. This prediction lacks biological plausibility.

Reviewing all 9 TxGNN-predicted indications in this evidence pack, a consistent pattern emerges: **none of the predictions fall within the antimicrobial spectrum** that Telavancin operates in. The predicted indications span haematological disorders (congenital and acquired), immunoglobulin dysproteinaemias, laboratory value abnormalities, and immunologically mediated syndromes — none of which involve gram-positive bacterial pathogenesis. This suggests the TxGNN model may be operating on structural or network embedding similarities unrelated to Telavancin's actual pharmacological class, making the entire predicted indication set unsuitable for drug repurposing development at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 9 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 9 predicted indications.

---

## US Market Information

Telavancin is not approved or marketed in Taiwan. No NDA records are available in this evidence pack.

For reference, Telavancin (Vibativ®) holds international approvals from the US FDA for:
- Complicated skin and skin structure infections (cSSSI) caused by susceptible gram-positive organisms
- Hospital-acquired bacterial pneumonia (HABP) and ventilator-associated bacterial pneumonia (VABP) caused by susceptible gram-positive organisms including MRSA

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, drug interactions) for Taiwan is not available from this evidence pack.

The following safety signals are derived from the mechanistic rationale analysis within this evidence pack and warrant specific attention:

- **Peripheral Neuropathy Risk**: Telavancin has known peripheral neuropathy as an adverse effect. The predicted indication "hematological disease associated with an acquired peripheral neuropathy" (Rank 7) poses an active harm risk — administering Telavancin to patients with pre-existing peripheral neuropathy may exacerbate neurological damage.
- **Protein Binding Pharmacokinetic Concern**: Telavancin is approximately 93% protein-bound. The predicted indication "congenital analbuminemia" (Rank 3) poses a serious pharmacokinetic safety concern, as the near-complete absence of albumin would dramatically alter drug distribution and could result in toxicity from unbound drug.

Please refer to the complete package insert (Vibativ® prescribing information) for comprehensive warnings, contraindications, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 9 TxGNN-predicted indications for Telavancin lack biological plausibility — none correspond to gram-positive bacterial infections (Telavancin's established pharmacological domain), zero clinical trial or literature evidence exists for any predicted indication, and two predictions (peripheral neuropathy-associated haematological disease and congenital analbuminemia) carry active safety risks that contraindicate use in the predicted patient populations.

**To proceed, the following would be needed:**

- **Re-evaluation of TxGNN input features**: Investigate why the model generated exclusively non-infectious disease predictions for a narrow-spectrum antibiotic; potential issues include node embedding conflation or missing drug-class categorical features.
- **Mechanism of action data**: Obtain full MOA characterisation from DrugBank API (currently a blocking data gap) to determine whether any secondary pharmacological activities (beyond antibacterial) exist that could theoretically support non-infectious indications.
- **Taiwan regulatory feasibility assessment**: Before any repurposing program, a regulatory pathway analysis is needed given that Telavancin has zero existing approvals in Taiwan.
- **Alternative indication search**: Consider running a targeted search for gram-positive bacterial infection indications not currently captured in the TFDA approved list (e.g., prosthetic joint infection, endocarditis, nosocomial MRSA pneumonia) rather than pursuing the model-predicted indications in this pack.
- **Safety dossier completion**: Retrieve TFDA package insert data and complete the drug interaction profile before any clinical evaluation is considered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

