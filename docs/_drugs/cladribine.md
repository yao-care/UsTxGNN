---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 533
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog conventionally used to treat hairy cell leukemia, working by selectively depleting lymphocytes and monocytes through DNA synthesis disruption.
The TxGNN model predicts it may be effective for **Parameningeal Embryonal Rhabdomyosarcoma**, a rare pediatric soft-tissue sarcoma;
however, **no supporting clinical trials or publications** currently exist for this specific combination, placing this prediction at evidence Level **L5** — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hairy cell leukemia (based on known pharmacology; no Taiwan market registration found) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Cladribine (2-chlorodeoxyadenosine, 2-CdA) is a purine nucleoside analog that is phosphorylated intracellularly and incorporated into DNA, disrupting DNA synthesis and repair and triggering apoptosis. It selectively accumulates in lymphocytes and monocytes due to their uniquely high deoxycytidine kinase-to-5'-nucleotidase ratio, making it highly effective against lymphoid malignancies such as hairy cell leukemia.

Parameningeal embryonal rhabdomyosarcoma is a mesenchymal tumor of skeletal muscle origin arising near the skull base or spinal meninges. Its cellular biology — driven by RAS/MAPK pathway dysregulation and PAX-FOXO1 fusions — differs fundamentally from the lymphocyte proliferation biology that Cladribine targets. The TxGNN model's high prediction score is most likely driven by shared knowledge graph nodes around DNA repair pathways and nucleoside metabolism, which are broadly present across tumor biology rather than being specific to rhabdomyosarcoma.

Importantly, the prediction rationale in this pack explicitly flags this as a weak, indirect mechanistic link. Current drug repurposing efforts for rhabdomyosarcoma focus on mTOR inhibitors, MDM2 antagonists, and immune checkpoint therapy — purine nucleoside analogs are not among the established or investigational candidates. The near-identical TxGNN scores across all seven rhabdomyosarcoma subtypes (ranks 6,268–6,938) further suggest a **knowledge graph cluster inflation effect** rather than a genuine biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Cladribine meets the criteria for an antineoplastic agent: it is a purine nucleoside analog indicated for hairy cell leukemia (a hematologic malignancy) and exerts direct cytotoxic activity through DNA incorporation and apoptosis induction.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine nucleoside analog) |
| Myelosuppression Risk | High — profound, prolonged lymphopenia and neutropenia are class hallmarks; CD4+ lymphocyte nadir may persist for months |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (serial lymphocyte and neutrophil counts), renal function, liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations (gloves, closed-system transfer where applicable) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, translational, or preclinical evidence supporting Cladribine's use in rhabdomyosarcoma or any related soft-tissue sarcoma. The high TxGNN score appears to reflect a knowledge graph cluster inflation artifact — all seven rhabdomyosarcoma subtypes in the top predictions share nearly identical scores — rather than a true drug-disease biological signal. The mechanistic gap between Cladribine's lymphocyte-directed cytotoxicity and mesenchymal tumor biology is substantial and not bridged by current evidence.

**To proceed, the following is needed:**
- **Preclinical wet-lab data**: In vitro cytotoxicity assays in established RMS cell lines (e.g., RD, A204, SMS-CTR) to determine whether Cladribine has any direct anti-RMS activity before investing further resources
- **MOA data gap resolution (DG002)**: Query DrugBank API to confirm full mechanism — specifically whether any off-target effects might be relevant to mesenchymal tumors
- **KG cluster audit**: Evaluate whether the rhabdomyosarcoma family is systematically over-predicted across all candidates due to cluster inflation; if confirmed, the entire RMS prediction cluster for Cladribine may warrant systematic deprioritization
- **Safety data gap resolution (DG001)**: Download and parse the package insert to populate key warnings and contraindications for any future safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

