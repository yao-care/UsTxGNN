---
layout: default
title: Pralatrexate
parent: Model Prediction Only (L5)
nav_order: 1073
evidence_level: L5
indication_count: 10
monitor_inn: "PRALATREXATE"
predicted_indications: ["pleural adenomatoid tumor", "relapsing-remitting multiple sclerosis", "pleural biphasic mesothelioma", "pleural epithelioid mesothelioma", "lymphohistiocytoid mesothelioma", "pericardium cancer", "pleural sarcomatoid mesothelioma", "malignant peritoneal mesothelioma", "well differentiated papillary mesothelioma", "pleural mesothelioma"]
---

# Pralatrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pralatrexate: From T-Cell Lymphoma to Pleural Mesothelioma

## One-Sentence Summary

Pralatrexate is an antifolate chemotherapy originally used for peripheral T-cell lymphoma and related non-Hodgkin lymphomas.
The TxGNN model's top-ranked prediction is *pleural adenomatoid tumor*, which has no supporting evidence. The best-supported prediction is **pleural mesothelioma** (including the epithelioid subtype), backed by **0 registered clinical trials** and **2 publications** (one Phase II trial and one review).

> Note: Because the top-ranked prediction has no supporting evidence, this report focuses on the best-supported prediction, pleural mesothelioma (rank 10, score 99.85%). The epithelioid subtype (rank 4) rests on the same Phase II study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mature T-cell and NK-cell non-Hodgkin lymphoma, including peripheral T-cell lymphoma (not otherwise specified) and primary cutaneous T-cell lymphoma subtypes |
| Predicted New Indication | Pleural mesothelioma (rank 10, best evidence). The rank 1 prediction, pleural adenomatoid tumor, has no evidence. |
| TxGNN Prediction Score | 99.85% (pleural mesothelioma); 99.91% (rank 1, pleural adenomatoid tumor) |
| Evidence Level | L3 (one single-arm Phase II study and one review; details not verified) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pralatrexate is an antifolate that inhibits dihydrofolate reductase (DHFR). It enters cells efficiently through the reduced folate carrier (RFC-1) and is retained through polyglutamylation. Its efficacy in T-cell lymphoma is established.

Malignant pleural mesothelioma is known to respond to antifolates, and pemetrexed is a standard therapy. Pralatrexate shares the antifolate mechanism, so it is plausible that it could act similarly. The epithelioid subtype is the most common and the most antifolate-responsive, which makes it the most reasonable subtype target.

The remaining predictions are much weaker:
- Other mesothelioma subtypes (biphasic, sarcomatoid, lymphohistiocytoid, peritoneal, pericardial, well-differentiated papillary) have no subtype-specific evidence. Sarcomatoid disease is generally more chemoresistant, and well-differentiated papillary disease is indolent and usually managed without cytotoxic therapy.
- Pleural adenomatoid tumor is a benign lesion usually treated by surgical excision, so there is no clear rationale for a cytotoxic drug.
- Relapsing-remitting multiple sclerosis has only a loose conceptual link through methotrexate's immunosuppressive use. Pralatrexate's mucositis and myelosuppression risk, together with established disease-modifying therapies, makes the benefit-risk profile unfavorable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Phase II trial (single-arm; details unverified) | J Thorac Oncol | Pralatrexate in unresectable malignant pleural mesothelioma. The background notes that mesothelioma responds to antifolates, that pralatrexate's toxicity is mainly stomatitis, and that it showed antitumor activity in mesothelioma cell lines and xenografts. Outcomes were not available in the compiled data. |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Review | Cancer Manag Res | Review of antifolates targeting folic acid synthesis, giving mechanistic context for DHFR inhibitors in cancer chemotherapy. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206183 (Dr. Reddy's Laboratories; cancelled) | Pralatrexate | Injection | Not available |
| NDA022468 (Fresenius Kabi USA; cancelled) | Pralatrexate | Injection | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate class) |
| Myelosuppression Risk | Medium to high. The knowledge graph links the drug to thrombocytopenia, neutropenia, agranulocytosis and anemia. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, renal function, and oral mucosa assessment (stomatitis is the main toxicity noted in the literature) |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (from knowledge graph, not label text)**: thrombocytopenia, neutropenia, agranulocytosis, anemia, macrocytic anemia, impaired renal function, and stomatitis.
- **Drug Interactions**: 100 interactions were identified; the 20 shown in the compiled data include:
  - **Major**: deferiprone, samarium (153Sm) lexidronam
  - **Moderate**: NSAIDs (acetylsalicylic acid, ibuprofen, flurbiprofen, diclofenac, ketorolac), chloramphenicol, zidovudine, pyrimethamine, palifermin, glucarpidase, naltrexone, sapropterin, roflumilast, strontium-89 chloride, and a tetanus toxoid vaccine

Label warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a 2007 single-arm Phase II study in pleural mesothelioma, which was assessed from limited information only, and there are no registered trials. The top-ranked prediction (pleural adenomatoid tumor) and most other predictions have no evidence. Pralatrexate has a significant toxicity profile, and all of its US licenses are cancelled, which limits practical development. Pleural mesothelioma, particularly the epithelioid subtype, is the only prediction worth a follow-up research question.

**To proceed, the following is needed:**
- Full text of the Phase II study (PMID 17409804): response rate, survival, histology breakdown, and toxicity
- Current mesothelioma standard-of-care comparison (e.g., pemetrexed-based regimens) to define a possible niche
- Mechanism of action data and FDA package insert warnings and contraindications
- Clarification of the regulatory and commercial status of the cancelled US licenses
- Any later trials or preclinical data for pralatrexate in mesothelioma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

