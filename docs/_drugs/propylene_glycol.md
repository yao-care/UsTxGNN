---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 1093
evidence_level: L5
indication_count: 10
monitor_inn: "PROPYLENE GLYCOL"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "immature cataract"]
last_modified_at: 2026-10-14
description: "Propylene Glycol: predicted new indication Bronchitis (evidence level L5). Approved use: Dry eye syndrome"
---

# Propylene Glycol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Propylene Glycol: From Dry Eye Syndrome to Bronchitis

## One-Sentence Summary

Propylene glycol was originally used for **dry eye syndrome (xerophthalmia)**, mainly as an ocular lubricant.
The TxGNN model predicts it may be effective for **bronchitis**, but the data compiled for this report contain **no clinical trials** and only **3 publications** for this indication.
Those publications point toward possible airway harm from inhaled propylene glycol, not benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry eye syndrome; xerophthalmia (from the knowledge graph, not from product labels) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propylene glycol is a common solvent, humectant and ocular lubricant. Its use in dry eye relates to moisture retention at the ocular surface, and it is also widely used as a formulation excipient.

No credible mechanistic link to bronchitis was found. The retrieved literature discusses e-cigarette aerosol, in which propylene glycol is a vehicle or constituent, as a possible cause or aggravator of airway disease. That is the opposite of a therapeutic signal. The third paper (quercetin in a mouse COPD model) does not involve propylene glycol.

The high TxGNN score (99.90%) is therefore not supported by clinical evidence. It is likely a graph-based inference and should be treated cautiously.

Other predicted indications are also unsupported. These include severe nonproliferative diabetic retinopathy, several cataract types (nuclear senile, cortical, senile, diabetic, type 2 diabetes-associated, tetanic, immature), and diabetic retinopathy. All have scores above 99.5%. Most have no trials or literature. For diabetic retinopathy, the only evidence is indirect, as detailed below.

---

## Clinical Trial Evidence

For bronchitis (the top prediction), currently no related clinical trials are registered.

For reference, the only trial found across the top predictions concerns diabetic retinopathy (rank 3):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07090044](https://clinicaltrials.gov/study/NCT07090044) | Phase 4 | Completed | 77 | Compared loteprednol, bromfenac and preservative-free artificial tears for pain after intravitreal injection. Artificial tears were a symptom-relief comparator, so the trial does not test propylene glycol against retinopathy. Indirect evidence only. |

---

## Literature Evidence

For bronchitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Discusses whether chronic e-cigarette use could cause lung disease, including chronic bronchitis. This is a potential harm signal. |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette liquids and aerosols contain airway irritants linked to asthma and worsening lung disease. This is a potential harm signal. |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal) | Respir Res | Quercetin reduced lung inflammation in a mouse COPD model. It does not involve propylene glycol. |

Evidence from the diabetic retinopathy prediction (rank 3) is also not direct:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39006273](https://pubmed.ncbi.nlm.nih.gov/39006273/) | 2024 | Clinical study | Am J Transl Res | Studies propylene glycol **mannate sulfate**, a different chemical entity, in non-proliferative diabetic retinopathy. It cannot be attributed to propylene glycol. |
| [34303817](https://pubmed.ncbi.nlm.nih.gov/34303817/) | 2021 | Formulation / ex vivo | Int J Pharm | Ocular progesterone insert that uses 2% propylene glycol as an excipient, not as an active agent. |
| [40132765](https://pubmed.ncbi.nlm.nih.gov/40132765/) | 2025 | Formulation / in vitro | Int J Pharm | Dasatinib nanoemulsions for ocular delivery that use propylene glycol as an excipient. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M018 | Equate Complete Relief Lubricant Eye Drops (Cancelled) | Solution/drops | Not specified |
| M003 | Instant Hand Sanitizeing Wipe (Cancelled) | Cloth | Not specified |
| M031 | EGHMTW hair oil (Cancelled) | Liquid | Not specified |

All three authorizations are cancelled, and no currently valid single-ingredient or combination authorization exists.

---

## Safety Considerations

Please refer to the package insert for safety information.

The data compiled for this report did not retrieve label warnings or contraindications. No drug-drug interaction records were found. The literature for the lead prediction raises a possible concern about airway irritation when propylene glycol is inhaled, which would be especially relevant in bronchitis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a model score alone (L5), with no clinical trials. The retrieved literature suggests inhaled propylene glycol may aggravate airway disease rather than treat it. No other predicted indication has direct supporting evidence either.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to assess whether any link to the predicted indications exists
- Direct evidence for propylene glycol itself, as opposed to propylene glycol mannate sulfate or its use as an excipient
- A safety assessment of the airway effects of inhaled propylene glycol before any respiratory indication is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

