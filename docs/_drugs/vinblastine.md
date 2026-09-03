---
layout: default
title: Vinblastine
parent: 僅模型預測 (L5)
nav_order: 1292
evidence_level: L5
indication_count: 10
---

# Vinblastine
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

# Vinblastine: From Cytotoxic Chemotherapy to Rhabdomyosarcoma

## One-Sentence Summary

> Vinblastine is a vinca alkaloid antineoplastic agent whose specific original indication is not documented in this evidence pack (the drug is not currently marketed in the reviewed jurisdiction).
> The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**,
> supported by **0 registered clinical trials** and **16 relevant publications**, including case reports, pilot cohorts, and one Phase 2 RCT of a related vinca alkaloid (vinorelbine).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack; vinblastine is a historically established cytotoxic antineoplastic agent (vinca alkaloid class) |
| Predicted New Indication | Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (`original_moa`: Data Gap). Based on the known pharmacology captured in the repurposing rationale, vinblastine is a **vinca alkaloid** that inhibits tubulin/microtubule polymerization, thereby blocking mitosis. This is the same mechanistic class as vincristine and vinorelbine, both of which are established components of standard rhabdomyosarcoma chemotherapy regimens.

Rhabdomyosarcoma is a highly proliferative pediatric/adult soft-tissue sarcoma, and microtubule-targeting agents are a core pillar of its treatment. The literature evidence directly supports this mechanistic link: a preclinical xenograft study (PMID 3329524) found vinblastine and vincristine to be the only vinca alkaloids with demonstrated clinical utility against human rhabdomyosarcoma, and multiple case reports describe vinblastine used within combination regimens (e.g., cisplatin-vinblastine-bleomycin, PVP therapy) for prostate and perianal rhabdomyosarcoma. While vinblastine itself has not been tested in a dedicated large-scale trial for this indication, its structural analogue vinorelbine has Phase 2 RCT-level evidence of activity in relapsed/refractory rhabdomyosarcoma (PMID 22633624), reinforcing the plausibility of the class effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | RCT (Phase 2) | European Journal of Cancer | Vinorelbine + low-dose cyclophosphamide showed good tolerance and efficacy in relapsed/refractory pediatric solid tumours, with activity specifically noted in rhabdomyosarcoma |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Cohort (Pilot) | Oncotarget | Pilot study of a 4-drug pediatric metronomic regimen for resistant cancers |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | Cohort (Pilot) | Cancer | Vinorelbine + low-dose cyclophosphamide pilot study to define optimal dosing ahead of European Rhabdomyosarcoma Protocol |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Cohort | Cancer | Vinorelbine showed evidence of activity in previously treated advanced childhood rhabdomyosarcoma |
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Case Report/Review | Medicine | Adult perianal rhabdomyosarcoma with nodal metastases achieved partial response after nivolumab, dacarbazine, cisplatin, and **vinblastine** combination therapy |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Mechanistic (Preclinical) | Anti-Cancer Drug Design | Xenograft model of human rhabdomyosarcoma identified vincristine and **vinblastine** as the only vinca alkaloids with demonstrated clinical utility against this tumour type |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case Report | Hinyokika Kiyo | Refractory prostatic rhabdomyosarcoma in a child responded to combination cisplatin, **vinblastine**, and peplomycin (PVP) therapy after relapse |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | Preclinical | Cell Death and Differentiation | Identified synthetic lethality between PLK1 inhibitors and microtubule-destabilizing drugs (vinblastine's mechanistic class) in preclinical rhabdomyosarcoma models |
| [2412542](https://pubmed.ncbi.nlm.nih.gov/2412542/) | 1985 | Case Report | ANZ Journal of Surgery | Rhabdomyosarcoma developed in a patient previously treated with chemotherapy for metastatic germ cell testicular tumour |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | Prospective Trial (pending classification) | Pediatric Blood & Cancer | CWS-96/CWS-2002P prospective European trials evaluating risk stratification and chemotherapy regimens across soft tissue sarcoma entities, reclassified against a recent registry |

---

## US Market Information

Vinblastine is currently **not marketed** in the reviewed jurisdiction (market status: Not Marketed), and no license/NDA records are available in the evidence pack (`total_licenses: 0`).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid, microtubule polymerization inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a conventional cytotoxic agent (vinca alkaloid class), standard cytotoxic drug handling precautions should apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Mechanistic plausibility is strong (vinca alkaloid class effect shared with vincristine/vinorelbine, both standard-of-care in rhabdomyosarcoma), and it is corroborated by one Phase 2 RCT of a related agent plus multiple case reports directly using vinblastine in rhabdomyosarcoma regimens. However, there are no registered clinical trials of vinblastine itself for this indication, and a **Blocking**-severity data gap exists for prescribing/safety information (TFDA-equivalent warnings and contraindications), which prevents a safety pre-assessment (S1) from being completed.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and DDI data (currently Blocking data gap, DG001)
- Confirmed mechanism of action documentation (DG002)
- A dedicated clinical trial or larger case series evaluating vinblastine specifically (not only related vinca alkaloids) in rhabdomyosarcoma
- Myelosuppression/emetogenicity and monitoring protocol specific to the intended dosing regimen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

