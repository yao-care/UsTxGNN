---
layout: default
title: Vorinostat
parent: Moderate Evidence (L3-L4)
nav_order: 1296
evidence_level: L4
indication_count: 2
---

# Vorinostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Vorinostat: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Vorinostat (ZOLINZA) is an oral HDAC inhibitor. From general knowledge, it is marketed in the US for cutaneous T-cell lymphoma (CTCL); the US license record in the data has no indication text.
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma**, but no trial or study tests vorinostat in this disease. Support is limited to **7 loosely related clinical trials** and **1 preclinical paper**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CTCL (from general knowledge; not stated in the US license data) |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on general pharmacology, vorinostat is a pan-HDAC inhibitor. It increases histone and non-histone protein acetylation, which can trigger apoptosis and cell-cycle arrest in malignant lymphocytes. Its efficacy in CTCL is established, so the drug has a known track record in skin-involving lymphomas.

The one supplied paper supports activity in B-cell disease in the lab. In mantle cell lymphoma cells, vorinostat induced apoptosis through acetylation of pro-apoptotic BH3-only gene promoters. This makes activity in B-cell lymphoma biologically plausible.

There are two caveats. Mantle cell lymphoma is a different disease from primary cutaneous B-cell lymphoma, and the finding is preclinical only. The very high TxGNN score is probably driven by vorinostat's strong CTCL and lymphoma links in the knowledge graph. It is a model prediction, not clinical proof.

---

## Clinical Trial Evidence

None of these trials studies primary cutaneous B-cell lymphoma. They are indirect: lymphoma in general, other HDAC inhibitors, or other settings.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02943642](https://clinicaltrials.gov/study/NCT02943642) | Phase 2 | Unknown | 162 | Resimmune vs oral vorinostat in mycosis fungoides (a T-cell lymphoma). Linked only through the lymphoma search term. |
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib + vorinostat in relapsed Hodgkin, B-cell non-Hodgkin and peripheral T-cell lymphoma. No cutaneous B-cell subgroup is evident. |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Vorinostat pharmacokinetics and safety in solid tumors and lymphomas with liver dysfunction. Relevant to dosing, not efficacy. |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Early phase 1 of oral SAHA (vorinostat) in advanced solid tumors and hematologic malignancies. General safety data only. |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat + tacrolimus + methotrexate for GVHD prevention after stem cell transplant. Transplant setting, not lymphoma treatment. |
| [NCT00007345](https://clinicaltrials.gov/study/NCT00007345) | Phase 2 | Completed | 131 | Depsipeptide (romidepsin) in CTCL and peripheral T-cell lymphoma. A different HDAC inhibitor; class-level support only. |
| [NCT01500538](https://clinicaltrials.gov/study/NCT01500538) | Phase 2 | Terminated | 1 | Vorinostat + eltrombopag in lymphoma. Terminated after 1 patient, so no usable data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical | Clin Cancer Res | Vorinostat induces apoptosis in mantle cell lymphoma (an aggressive B-cell neoplasm) by acetylating pro-apoptotic BH3-only gene promoters. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021991 | ZOLINZA (Merck Sharp & Dohme LLC) | Capsule (oral) | — |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HDAC inhibitor), based on general pharmacology |
| Myelosuppression Risk | Medium. One trial in the pack notes that low platelet counts can occur early in vorinostat treatment. Please refer to the package insert for details. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | At minimum, CBC with platelets and liver and renal function. Please refer to the package insert for the full list. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for primary cutaneous B-cell lymphoma is one preclinical paper in a different B-cell lymphoma, plus indirect lymphoma trials with no cutaneous B-cell data. This is a research question, not a candidate ready for development.

The second TxGNN prediction for vorinostat, **Sézary syndrome** (score 99.07%), has far stronger support. It has a completed Phase 2b trial in advanced CTCL (NCT00091559) and the Phase 3 MAVORIC trial (NCT01728805, 372 patients). However, vorinostat is the comparator arm in MAVORIC, and Sézary syndrome is a CTCL variant, so it is likely already on or near label. It is better treated as a label-verification question than as true repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking any safety screening)
- Mechanism of action data from DrugBank
- Preclinical or early clinical data in cutaneous B-cell lymphoma (e.g., cell-line studies or a small phase 2 trial)
- Review of the current US label to confirm the approved indication text

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

