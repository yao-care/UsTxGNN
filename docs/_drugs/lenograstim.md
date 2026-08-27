---
layout: default
title: Lenograstim
parent: 僅模型預測 (L5)
nav_order: 845
evidence_level: L5
indication_count: 4
---

# Lenograstim
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

# Lenograstim: From Neutrophil Support/Stem Cell Mobilization to Primary Release Disorder of Platelets

## One-Sentence Summary

Lenograstim is a recombinant human G-CSF (granulocyte colony-stimulating factor) used to stimulate neutrophil precursor proliferation and to mobilize peripheral hematopoietic stem cells. The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but currently **no clinical trials or literature directly support this specific indication** — only 13 tangentially related hematopoietic stem cell transplantation trials were identified, all graded as low relevance (Grade C).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this Evidence Pack; per the drug's known pharmacology (documented in the repurposing rationale below), lenograstim is used to stimulate neutrophil recovery and for peripheral hematopoietic stem cell (HSC) mobilization |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (mechanism/indirect trial evidence only, no direct trials or literature) |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action (MOA) data for lenograstim is not available in this Evidence Pack (flagged as a High-severity data gap). However, the repurposing rationale supplied alongside the TxGNN prediction describes lenograstim as a glycosylated recombinant human G-CSF that acts primarily on the G-CSF receptor (CSF3R), stimulating proliferation and differentiation of granulocyte-lineage precursor cells in bone marrow and promoting neutrophil release and peripheral stem cell mobilization.

Primary release disorder of platelets, by contrast, is a platelet **function** defect typically involving impaired granule storage or release (e.g., δ-granule or α-granule defects) in megakaryocyte/platelet biology — a pathway distinct from the granulocytic lineage that G-CSF/CSF3R signaling targets. The Evidence Pack's own analysis notes that there is **no known direct receptor or signaling overlap** between lenograstim's pharmacology and the platelet granule release pathway.

Given this, the very high TxGNN score (99.91%) most likely reflects an **indirect association** in the knowledge graph — for example, shared "hematologic/bone marrow disease" nodes or co-occurrence in hematopoietic transplant/supportive-care contexts — rather than a direct, biologically plausible mechanism. This is consistent with the supporting clinical trials found: all 13 are hematopoietic stem cell transplantation studies where G-CSF-class drugs, if used at all, serve as supportive stem-cell mobilization agents rather than as a treatment directed at platelet release disorder itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSC transplant for hematological malignancies; not focused on platelet release disorder (Grade C — low relevance) |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous HSC transplant vs. best available therapy for treatment-resistant MS; G-CSF-class agents used only as supportive mobilization therapy (Grade C) |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial on post-transplant cyclophosphamide GVHD prophylaxis; no direct link to platelet release disorder (Grade C) |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSC transplant for hematologic malignancies; indirect relevance only (Grade C) |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved mismatched-donor bone marrow transplant study; withdrawn with no enrollment data (Grade C) |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation prevention in respiratory failure; no direct relevance to lenograstim or platelet disorder (Grade C) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplant in pediatric sarcomas; not directly relevant (Grade C) |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile for moderate COVID-19/cytokine release syndrome; relevance to lenograstim unclear (Grade C) |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Lowest effective dose of post-transplant cyclophosphamide for GVHD prophylaxis; not directly targeting platelet release disorder (Grade C) |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion + autologous HSC transplant for severe SLE; not directly relevant (Grade C) |

*Note: All 13 trials identified for this indication are hematopoietic stem cell transplantation studies in which G-CSF-class drugs (if used) serve only as supportive stem-cell mobilization agents, not as a treatment directed at primary platelet release disorder. None constitutes direct clinical evidence for this indication.*

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Lenograstim is **not currently marketed or registered (0 NDAs/licenses)** under this Evidence Pack's regulatory data. No approved product license or indication text is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields in this Evidence Pack — key warnings, contraindications, and drug interactions — are currently marked as data gaps. Notably, TFDA label warnings/contraindications data is flagged as a **Blocking** severity gap, meaning this candidate cannot yet pass the S1 safety pre-screening stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between lenograstim (a G-CSF/CSF3R agonist acting on the granulocytic lineage) and primary release disorder of platelets (a platelet granule storage/release defect) is weak and not supported by any direct clinical trial or literature evidence — only tangentially related HSC transplant trials exist. In addition, this drug is not marketed in Taiwan, and a Blocking-severity data gap (missing TFDA label warnings/contraindications) prevents any safety pre-screening at this time.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank — currently a High-severity data gap (DG002)
- Targeted preclinical or mechanistic studies evaluating any plausible role of G-CSF signaling in platelet granule release biology
- Note: the three other TxGNN-predicted indications for lenograstim (Glanzmann thrombasthenia, pseudo-von Willebrand disease, severe nonproliferative diabetic retinopathy) are all Evidence Level L5 — model prediction only, with no supporting trials or literature — and are likewise recommended for Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

