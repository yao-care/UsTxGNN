---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 895
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Chemotherapy Backbone to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan (DrugBank DB01042) is a classic cytotoxic alkylating chemotherapy agent; this evidence pack does not include a Taiwan-approved original indication text since the drug is not currently marketed in Taiwan. The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor**, with **8 clinical trials** and **4 publications** currently supporting this direction, largely reflecting melphalan's established role in high-dose chemotherapy/autologous stem cell transplant (ASCT) salvage regimens for relapsed germ cell tumors.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (drug currently unmarketed in Taiwan; internationally melphalan is classically indicated for multiple myeloma and ovarian carcinoma — general background, not sourced from this pack) |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Drug-level mechanism-of-action data is flagged as a data gap (DG002) in this pack. However, disease-specific rationale notes within the evidence do describe melphalan as a **bifunctional alkylating agent (a phenylalanine-derived nitrogen mustard)** that induces DNA cross-linking and apoptosis in rapidly dividing cells — consistent with its well-documented use as a conventional cytotoxic chemotherapy agent.

Testicular/gonadal germ cell tumors are known to be highly sensitive to alkylating agents. High-dose melphalan combined with autologous stem cell transplant rescue is already an established oncology salvage strategy for relapsed or refractory germ cell tumors, rather than a wholly novel hypothesis — this is reflected directly in the trial evidence below (e.g., NCT00936936, a disease-specific Phase 2 study). The TxGNN prediction therefore aligns with existing, though not disease-label-approved, clinical practice patterns.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | High-dose chemotherapy (gemcitabine/docetaxel/melphalan/carboplatin, then ifosfamide/carboplatin/etoposide) for poor-prognosis relapsed germ-cell tumors — disease-specific (Grade A relevance) |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients (not disease-specific) |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan + melphalan + topotecan followed by ASCT in advanced/recurrent solid tumors |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Autologous blood/marrow transplantation across hematologic malignancies and selected solid tumors (broad population) |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine chemoprotection with ASCT for high-risk/relapsed pediatric solid and brain tumors |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | High-dose regimens ± total-body irradiation before ASCT for hematologic cancers and selected solid tumors |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | N/A | Completed | 36 | Nonmyeloablative allogeneic HSCT (ATG + melphalan/cladribine or TLI) across various hematologic illnesses |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis (different indication/route; low relevance) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Review | Oncology | Chemotherapy of testicular germinal tumors (abstract not available in pack; title-level relevance) |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | Urologic Clinics of North America | Seminoma treatment review (abstract not available in pack) |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Cohort | Voprosy onkologii | Historical experience treating testicular seminoma and its metastases with sarcolysin (an early name for melphalan) |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Other (endocrine mechanism) | Acta Unio Internationalis Contra Cancrum | Influence of hormonal and alkylating drugs on pituitary FSH-stimulating function — mechanistic, not a direct treatment study |

*Note: abstracts were not populated in this evidence pack for these older publications; summaries above are based on titles only.*

## Cytotoxicity

Melphalan is a conventional cytotoxic alkylating chemotherapy agent, and all current predicted indications are oncologic — this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard/phenylalanine derivative) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no drug-specific toxicity data in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack flags TFDA label warnings/contraindications as a **Blocking** data gap (DG001) — safety data was not available and formal S1 safety pre-assessment could not be completed.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One disease-specific completed Phase 2 trial (NCT00936936) plus established oncologic practice (melphalan-containing high-dose ASCT salvage regimens for relapsed germ cell tumors) support L2-level evidence. However, the drug is not currently marketed in Taiwan and TFDA label/safety data is a blocking gap, so this cannot yet advance without guardrails.

**To proceed, the following is needed:**
- TFDA-equivalent label warnings/contraindications (DG001, blocking) before any S1 safety pre-assessment
- Confirmed mechanism-of-action documentation (DG002)
- Taiwan market/registration pathway assessment, since total_licenses = 0
- Route-of-administration compatibility confirmation (currently pending in the pack)

*Note: Lower-ranked candidates (ovarian primitive germ cell tumor, L3; choriocarcinoma of ovary and the five mucinous adenocarcinoma indications, all L5/Hold) lack clinical or literature support and are flagged in the pack as likely reflecting TxGNN embedding-cluster similarity rather than independent signal — not recommended for near-term investment.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

