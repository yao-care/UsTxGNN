---
layout: default
title: Procarbazine
parent: 僅模型預測 (L5)
nav_order: 1087
evidence_level: L5
indication_count: 5
---

# Procarbazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Procarbazine: From Hodgkin's Lymphoma to Follicular Lymphoma

## One-Sentence Summary

> Procarbazine is a methylhydrazine-derivative alkylating agent historically used as a core component of combination chemotherapy for Hodgkin's lymphoma (e.g., the MOPP regimen).
> The TxGNN model predicts it may be effective for **Follicular Lymphoma**,
> with **3 clinical trials** and **20 publications** currently identified, though only a subset directly evaluates procarbazine itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin's Lymphoma (per literature evidence; no formal license/indication text available — see note below) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L2 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: `taiwan_regulatory.licenses` is empty and `drug.original_indications` is empty in the source data. The original indication above is inferred from literature evidence (PMID 16690522), not from an official regulatory license record.*

---

## Why is This Prediction Reasonable?

Procarbazine is a methylhydrazine-derivative alkylating agent that induces DNA/RNA methylation and oxidative DNA damage. It was historically a core component of classic combination regimens for Hodgkin's lymphoma, most notably MOPP (mechlorethamine, vincristine, procarbazine, prednisone) and its variant C-MOPP.

Follicular lymphoma is, like Hodgkin's lymphoma, a lymphoid malignancy, and procarbazine already carries an established (if now largely historical) indication in non-Hodgkin's lymphoma — a 2006 review (PMID 16690522) specifically describes durable complete remissions in relapsed/refractory follicular lymphoma patients treated with prolonged daily procarbazine. This supports the plausibility of the TxGNN prediction.

Mechanistically, procarbazine's cytotoxic alkylation of actively dividing lymphocytes is not specific to Hodgkin's disease and can theoretically extend to other indolent B-cell lymphomas such as follicular lymphoma. However, most modern trials in follicular lymphoma (e.g., FND + rituximab, fludarabine/mitoxantrone-based regimens) no longer include procarbazine, having shifted toward purine analogs, anthracyclines, and anti-CD20 monoclonal antibodies. The evidence for procarbazine's direct contribution in this indication is therefore older and more indirect than for contemporary standard-of-care agents.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01130194](https://clinicaltrials.gov/study/NCT01130194) | Phase 2 | Completed | 29 | Sequential chemotherapy, radioimmunotherapy, and autologous stem cell transplantation in follicular lymphoma, aiming for durable first complete remission; regimen composition (incl. procarbazine) not confirmed from title alone. |
| [NCT00577993](https://clinicaltrials.gov/study/NCT00577993) | Phase 3 | Completed | 210 | FND (fludarabine/mitoxantrone/dexamethasone) ± rituximab in stage IV indolent lymphoma; does not include procarbazine — same indication, different regimen. |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Terminated | 6 | Oral combination chemotherapy + G-CSF in elderly patients with intermediate/high-grade NHL; very small terminated trial, weak evidence but supports feasibility of oral alkylator-based regimens. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16690522](https://pubmed.ncbi.nlm.nih.gov/16690522/) | 2006 | Review | Leukemia & Lymphoma | Procarbazine is an oral alkylating agent with lymphoma activity; two relapsed/refractory follicular lymphoma patients achieved complete, durable remission on prolonged daily procarbazine. |
| [16111588](https://pubmed.ncbi.nlm.nih.gov/16111588/) | 2005 | RCT | Int J Radiat Oncol Biol Phys | Prospective randomized study comparing central lymphatic irradiation vs. alternating triple chemotherapy for molecular response in stage I-III follicular lymphoma. |
| [16230674](https://pubmed.ncbi.nlm.nih.gov/16230674/) | 2005 | Review | J Clin Oncol | Reviews how new treatment options have changed the historically incurable natural history and survival of follicular lymphoma. |
| [9248325](https://pubmed.ncbi.nlm.nih.gov/9248325/) | 1997 | Cohort | Rinsho Ketsueki | 72 follicular lymphoma patients treated with combination chemotherapy; 83.3% achieved complete remission, 5-year survival 63.7%. |
| [9001350](https://pubmed.ncbi.nlm.nih.gov/9001350/) | 1996 | Cohort | Jpn J Clin Oncol | 25-year single-institution review of prognostic factors in 118 Japanese follicular lymphoma patients. |
| [8426197](https://pubmed.ncbi.nlm.nih.gov/8426197/) | 1993 | Cohort | J Clin Oncol | Nebraska Lymphoma Study Group report on clinical features and prognosis of follicular large-cell lymphoma. |
| [22507790](https://pubmed.ncbi.nlm.nih.gov/22507790/) | 2012 | Case series | Hematology (Amsterdam) | PEP-C low-dose oral metronomic chemotherapy regimen for refractory/relapsed lymphoma (regimen includes an oral alkylating agent component). |
| [9156664](https://pubmed.ncbi.nlm.nih.gov/9156664/) | 1997 | Cohort | Leukemia & Lymphoma | Salvage treatment outcomes after failure/relapse of initial chemotherapy in follicular NHL. |
| [9336721](https://pubmed.ncbi.nlm.nih.gov/9336721/) | 1997 | Review | Hematol Oncol Clin North Am | Overview of treatment for localized low-grade (follicular) lymphoma, focused on radiotherapy outcomes. |
| [11672513](https://pubmed.ncbi.nlm.nih.gov/11672513/) | 2001 | Cohort | J Hematother Stem Cell Res | Chemotherapy + interferon-alpha2b vs. chemotherapy alone in follicular lymphoma; increased event-free but not overall survival. |

---

## US Market Information

Procarbazine currently has no recorded license/authorization entries in the available regulatory dataset (`total_licenses = 0`, market status: Not marketed). No NDA table can be generated at this time.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (methylhydrazine-derivative alkylating agent) |
| Myelosuppression Risk | High — classic component of the MOPP regimen, associated with significant leukopenia and thrombocytopenia |
| Emetogenicity Classification | High (as part of MOPP-type combination regimens) |
| Monitoring Items | CBC with differential and platelet count, liver and renal function; long-term monitoring for secondary malignancy risk given alkylating agent class |
| Handling Protection | Yes — must be handled per hazardous/cytotoxic drug handling protocols; note MAOI-like activity requiring dietary and drug-interaction caution |

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently available in the evidence pack — DDI query status: not found.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The follicular lymphoma prediction is supported by one completed Phase 2/3-level trial context and a historical review directly describing durable remissions with procarbazine (L2 evidence), giving reasonable mechanistic and clinical plausibility. However, modern standard regimens for follicular lymphoma have largely moved away from procarbazine, and no Taiwan/US regulatory, safety, or MOA data are currently available.

**To proceed, the following is needed:**
- Formal MOA and original indication confirmation via DrugBank/regulatory source (currently flagged as Blocking/High data gaps)
- TFDA/US package insert warnings, contraindications, and DDI data for safety review (S1 gate)
- Full-text review of NCT01130194 to confirm whether procarbazine is an actual regimen component
- Assessment of concordance between historical procarbazine-based regimens and current follicular lymphoma standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

