---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 999
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a third-generation platinum-based chemotherapy agent, internationally established as part of the FOLFOX regimen for metastatic colorectal cancer. The TxGNN model predicts it may also be effective for **Malignant Pleural Mesothelioma**, with **6 clinical trials** and **20 publications** currently supporting this direction, including a completed Phase II trial directly testing oxaliplatin in this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack (no license record); internationally recognized for metastatic colorectal cancer (FOLFOX regimen) |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data from DrugBank is currently a flagged data gap (DG002). Based on known pharmacology, oxaliplatin is a third-generation platinum compound that forms DNA-platinum adducts and interstrand cross-links, blocking DNA replication and transcription and inducing apoptosis in rapidly dividing cells — the same mechanistic class as cisplatin, which along with pemetrexed forms the current standard-of-care backbone for malignant pleural mesothelioma (MPM).

Oxaliplatin's original clinical use in colorectal cancer relies on this same DNA cross-linking cytotoxicity. Because MPM is also treated with platinum-based combination chemotherapy as its backbone, there is strong mechanistic overlap between the two indications: both are solid tumors relying on DNA-damage-induced apoptosis for treatment response.

This mechanistic rationale is further reinforced by real-world clinical development history — multiple completed Phase II trials have already tested oxaliplatin in combination with gemcitabine or raltitrexed specifically in MPM patients, providing direct (not merely theoretical) support for the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Oxaliplatin + gemcitabine as first- or second-line therapy for pleural/peritoneal mesothelioma; directly evaluates response rate to this combination |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib (Velcade) + oxaliplatin (Eloxatin) in previously treated pleural/peritoneal mesothelioma |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A (registry) | Unknown | 1000 | Multicenter international PIPAC/PITAC registry documenting outcomes for peritoneal/pleural malignancies; not oxaliplatin-specific |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Not yet recruiting | 30 | Neoadjuvant chemoimmunotherapy for gastroesophageal junction/gastric cancer; relevance to MPM appears to be a keyword mismatch |
| [NCT05107674](https://clinicaltrials.gov/study/NCT05107674) | Phase 1 | Recruiting | 345 | Dose-escalation study of CBL-B inhibitor NX-1607 in advanced malignancies; not an oxaliplatin trial |
| [NCT07532902](https://clinicaltrials.gov/study/NCT07532902) | Phase 1 | Recruiting | 60 | Basket trial of BMS-986504 in MTAP-deleted solid tumors; not an oxaliplatin trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase 2 trial | J Clin Oncol | Raltitrexed + oxaliplatin combination shown active in diffuse malignant pleural mesothelioma (70 patients) |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase 2 trial | Tumori | Oxaliplatin + raltitrexed pilot study in inoperable MPM |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase 2 trial | Clin Lung Cancer | Multicenter Phase II of gemcitabine + oxaliplatin in MPM (n=25) |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Observational | J Occup Med Toxicol | Gemcitabine + oxaliplatin in pemetrexed-pretreated MPM patients |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase 2 trial | Lung Cancer | Vinorelbine + oxaliplatin as first-line therapy in MPM |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase 2 trial | Lung Cancer | Raltitrexed-oxaliplatin found inactive as second-line MPM therapy (negative result) |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Institutional review | Eur J Cancer | Institut Gustave Roussy 9-year experience with chemo/chemo-immunotherapy including raltitrexed-oxaliplatin in mesothelioma |
| [15261443](https://pubmed.ncbi.nlm.nih.gov/15261443/) | 2004 | Review | Lung Cancer | Review of chemotherapy results and developments in MPM |
| [11836672](https://pubmed.ncbi.nlm.nih.gov/11836672/) | 2002 | Review | Semin Oncol | Emerging role of antifolates, including the raltitrexed/oxaliplatin combination, in MPM |
| [26526504](https://pubmed.ncbi.nlm.nih.gov/26526504/) | 2015 | Review | Cancer Treat Rev | Platinum + pemetrexed noted as standard of care in MPM; context for vinca alkaloid alternatives |

---

## US Market Information

This drug currently has no marketing license on file in this evidence pack (Market Status: Not Marketed; Total Licenses: 0).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic chemotherapy (platinum-based DNA cross-linking agent) |
| Myelosuppression Risk | Not specified in evidence pack — please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not specified in evidence pack — please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, renal function, and peripheral neuropathy assessment (standard for platinum-based agents) |
| Handling Protection | Requires cytotoxic drug handling precautions per standard chemotherapy handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase II trials (notably NCT00859469, and the published raltitrexed/gemcitabine-oxaliplatin combination studies) directly support the biological plausibility and clinical signal of oxaliplatin in malignant pleural mesothelioma, justifying an L2 evidence level. However, a **Blocking-severity data gap** exists at the drug level: TFDA-equivalent label warnings and contraindications (DG001) are unavailable, which prevents formal entry into the safety pre-assessment stage.

**To proceed, the following is needed:**
- TFDA/regulatory label PDF with warnings and contraindications (DG001, Blocking)
- Formal DrugBank mechanism-of-action data (DG002)
- Confirmation of original approved indication and license status
- Safety monitoring plan addressing known platinum-class risks (myelosuppression, peripheral neuropathy, renal function)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

