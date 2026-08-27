---
layout: default
title: Dinutuximab
parent: 僅模型預測 (L5)
nav_order: 611
evidence_level: L5
indication_count: 4
---

# Dinutuximab
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

# Dinutuximab: From Neuroblastoma to Ganglioneuroblastoma

## One-Sentence Summary

Dinutuximab is a chimeric anti-GD2 monoclonal antibody with an established role in high-risk neuroblastoma immunotherapy. The TxGNN model predicts it may also be effective for **Ganglioneuroblastoma**, a closely related neuroblastic tumor, with **7 clinical trials** and **2 publications** currently supporting this direction.

*(Note: The evidence pack returned four candidate indications for dinutuximab. Three of them — a congenital vertebral/endocrine/T-cell dysfunction syndrome, retroperitoneal neoplasm, and BCR-ABL1-positive chronic myelogenous leukemia — have no supporting clinical trials or literature and are assessed by the model itself as low-confidence graph noise (Evidence Level L5/L4, recommendation "Hold"). This report focuses on the one candidate with substantive evidence: Ganglioneuroblastoma.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | High-risk, GD2-positive Neuroblastoma (established use; not formally captured in the local regulatory record — see Market Status below) |
| Predicted New Indication | Ganglioneuroblastoma (disease) |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for dinutuximab is not available in the current record (flagged as a High-severity data gap, DG002). Based on information available within the evidence pack, dinutuximab is a chimeric monoclonal antibody directed against GD2 (disialoganglioside), a surface antigen densely expressed on tumors of neuroectodermal origin. Its mechanism relies on GD2 binding to trigger antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (CDC) against antigen-positive tumor cells, and it already holds an established treatment role — together with GM-CSF and isotretinoin — in high-risk neuroblastoma (reflected in the COG standard-of-care regimens referenced by the supporting trials below).

Ganglioneuroblastoma belongs to the same neuroblastic tumor spectrum as neuroblastoma, arising from the same sympathetic neural crest precursor cells and commonly co-expressing GD2. This shared cell-of-origin and antigen expression profile is the mechanistic basis for the TxGNN prediction: a drug validated against GD2-positive neuroblastoma is plausible against GD2-positive ganglioneuroblastoma as well.

One caveat is worth flagging: most registered trials and publications label patient populations as "neuroblastoma" broadly, and ganglioneuroblastoma (particularly its nodular subtype) is typically enrolled as a pathological subtype within that broader category rather than as an independently defined study population. The evidence below should therefore be read as strongly supportive by mechanistic analogy and shared trial enrollment, rather than as ganglioneuroblastoma-specific pivotal data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Tests addition of dinutuximab to induction chemotherapy alongside surgery, radiation, stem cell transplant, and immunotherapy in newly diagnosed high-risk neuroblastoma; largest and most direct Phase 3 evidence source, results pending. |
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Pilot induction regimen combining ch14.18 (dinutuximab) with sargramostim (GM-CSF) plus chemotherapy in newly diagnosed high-risk neuroblastoma. |
| [NCT01767194](https://clinicaltrials.gov/study/NCT01767194) | Phase 2 | Completed | 73 | Randomized trial comparing irinotecan/temozolomide plus temsirolimus vs. dinutuximab in relapsed/refractory neuroblastoma; only completed, results-bearing RCT identified (see PMID 28549783). |
| [NCT04385277](https://clinicaltrials.gov/study/NCT04385277) | Phase 2 | Active, not recruiting | 41 | Pilot study of dinutuximab, GM-CSF, and isotretinoin combined with irinotecan/temozolomide in the post-consolidation setting for high-risk neuroblastoma. |
| [NCT07437963](https://clinicaltrials.gov/study/NCT07437963) | Phase 1/2 | Not yet recruiting | 76 | Dinutuximab/cyclophosphamide/topotecan/GM-CSF with or without iberdomide in relapsed, refractory, or progressive neuroblastoma after prior chemoimmunotherapy. |
| [NCT07375563](https://clinicaltrials.gov/study/NCT07375563) | Phase 3 | Recruiting | 5 | Chemoimmunotherapy combined with autologous NK cell therapy in pediatric refractory/relapsed high-risk neuroblastoma and ganglioneuroblastoma; dinutuximab's role as core agent is not explicit, small cohort. |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | Large trial of 131I-MIBG or ALK inhibitor added to intensive therapy for newly diagnosed high-risk neuroblastoma/ganglioneuroblastoma; dinutuximab likely present only as background standard therapy, not the tested variable. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28549783](https://pubmed.ncbi.nlm.nih.gov/28549783/) | 2017 | RCT | The Lancet Oncology | COG ANBL1221 open-label randomized Phase 2 trial: irinotecan-temozolomide combined with temsirolimus or dinutuximab in children with relapsed/refractory neuroblastoma; establishes dinutuximab's activity and tolerability in this setting. |
| [37929737](https://pubmed.ncbi.nlm.nih.gov/37929737/) | 2025 | Review/Case Report | Current Pediatric Reviews | Case report and literature review of late relapse in neuroblastoma, the most common extracranial solid tumor in children, with poor survival on recurrence. |

---

## US Market Information

Dinutuximab is not currently marketed locally (market status: Not Marketed) and no license/NDA records are available (0 authorizations on file).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — anti-GD2 chimeric monoclonal antibody acting via ADCC/CDC against GD2-expressing tumor cells; not a conventional cytotoxic chemotherapeutic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no DrugBank toxicity data on file; dinutuximab is typically co-administered with a chemotherapy/GM-CSF backbone that carries its own independent myelosuppression risk) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Local regulatory warnings, contraindications, and drug-interaction data are all currently unavailable — this is flagged as a Blocking-severity data gap, see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Ganglioneuroblastoma prediction is backed by a completed randomized Phase 2 trial (NCT01767194 / PMID 28549783), an actively enrolling large Phase 3 trial (NCT06172296), and a strong mechanistic rationale rooted in shared GD2 expression across the neuroblastic tumor spectrum — sufficient to move past pure model prediction (L2 evidence level). However, this drug is not currently marketed locally and local safety labeling (warnings/contraindications) is entirely absent, which is flagged as a **Blocking-severity data gap (DG001)** that prevents entry into the standard safety pre-assessment (S1) stage.

**To proceed, the following is needed:**
- Local package insert / prescribing information (warnings, contraindications, DDI) — currently a Blocking data gap
- Formal mechanism-of-action documentation from DrugBank or manufacturer labeling — currently a High-severity data gap
- Pathology-level confirmation of GD2 expression in ganglioneuroblastoma (vs. inference from the neuroblastoma spectrum)
- Monitoring of NCT06172296 and NCT07437963 results as they mature, since current direct evidence relies primarily on one completed Phase 2 RCT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

