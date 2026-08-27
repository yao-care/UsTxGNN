---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 769
evidence_level: L5
indication_count: 2
---

# Heparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Heparin: From Anticoagulation to Thrombophilia due to Protein C Deficiency

## One-Sentence Summary

Heparin (DrugBank DB01109) is a standard anticoagulant, classically used to prevent and treat thromboembolic events by activating antithrombin III. The TxGNN model predicts it may also be effective for **Thrombophilia due to Protein C Deficiency, Autosomal Recessive**, but this pairing currently has **0 clinical trials** and **0 publications** supporting it — the score reflects a model prediction only. A second, lower-priority candidate indication (primary platelet release disorder) was also evaluated and is addressed separately below, as the evidence suggests it is likely a false-positive pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation / thromboprophylaxis (no formal indication license on file in this evidence pack) |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| US Market Status | ✗ Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack. Based on known information, heparin activates antithrombin III, which in turn strongly inhibits thrombin (Factor IIa) and Factor Xa — this is the pharmacological basis for its established role as a first-line anticoagulant.

Protein C deficiency is an inherited thrombophilia: affected patients have a genetically reduced ability to inactivate Factors Va and VIIIa, leading to a hypercoagulable state and elevated venous thromboembolism risk. Heparin is already used clinically in this population during acute thrombotic events and as bridging therapy before initiating warfarin (avoiding the transient hypercoagulable state warfarin can cause via protein C suppression).

Because of this, the mechanistic link is plausible but represents an extension of heparin's existing anticoagulant use rather than a genuinely novel repurposing discovery. No clinical trials or literature specific to this drug–disease pairing were found in this evidence pack, so despite the high TxGNN score (99.29%), the finding should be treated as an unvalidated model prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No approved license records are available — heparin is recorded as not marketed (0 licenses) in this evidence pack, so no authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Predicted Indication Evaluated (Not Recommended)

This evidence pack ("multi") also scored a second candidate indication for heparin: **Primary Release Disorder of Platelets** (TxGNN score 99.06%, rank 20326, Evidence Level L4). Unlike the primary candidate above, this pairing returned substantial trial and literature volume — but review of that evidence indicates a mechanistic mismatch, not supporting evidence.

**Why this pairing is not recommended:** Primary release disorder of platelets is a bleeding disorder caused by defective platelet granule release, requiring pro-hemostatic management. Heparin is an anticoagulant with the opposite pharmacological direction, and can itself trigger heparin-induced thrombocytopenia (HIT), a platelet-activating adverse reaction. All 10 clinical trials reviewed were graded "C" (low relevance) — they concern heparin's existing uses in VTE prophylaxis, ACS, cardiac surgery, sepsis, and COVID-19, or study HIT as a heparin side effect, not treatment of this platelet disorder.

**Selected Clinical Trials (graded low relevance):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05293132](https://clinicaltrials.gov/study/NCT05293132) | Phase 2/3 | Completed | 90 | Montelukast vs. CoQ10 in sepsis — unrelated to heparin/platelet release |
| [NCT07127718](https://clinicaltrials.gov/study/NCT07127718) | Phase 2 | Recruiting | 678 | Leptospirosis complication prevention — unrelated |
| [NCT00250471](https://clinicaltrials.gov/study/NCT00250471) | Phase 3 | Completed | 900 | Bivalirudin vs. eptifibatide ± heparin for post-PCI microvascular dysfunction |
| [NCT01729559](https://clinicaltrials.gov/study/NCT01729559) | Phase 4 | Completed | 495 | Unfractionated heparin vs. enoxaparin for VTE prophylaxis after trauma |
| [NCT04528888](https://clinicaltrials.gov/study/NCT04528888) | Phase 3 | Unknown | 210 | Steroids + heparin in COVID-19 pneumonia |
| [NCT00329433](https://clinicaltrials.gov/study/NCT00329433) | Phase 2/3 | Completed | 120 | Desirudin vs. heparin for thrombosis prophylaxis in cardiothoracic surgery |
| [NCT01863134](https://clinicaltrials.gov/study/NCT01863134) | Phase 4 | Completed | 140 | Eptifibatide in high-risk NSTE-ACS requiring CABG |
| [NCT00457002](https://clinicaltrials.gov/study/NCT00457002) | Phase 3 | Completed | 6758 | Apixaban vs. enoxaparin for VTE prophylaxis in acutely ill medical patients |
| [NCT06565364](https://clinicaltrials.gov/study/NCT06565364) | N/A | Completed | 160 | Protamine-heparin antibody immunogenicity and thrombotic potential (HIT-related side effect study) |
| [NCT00222352](https://clinicaltrials.gov/study/NCT00222352) | N/A | Completed | 2000 | Bedside troponin testing in ED ACS diagnosis — unrelated |

**Selected Literature (Review/Cohort/Case Report, all Tier 3):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Review | Gastroenterology | AGA update on coagulation management in cirrhosis |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | 2024 | Review | Allergologie select | Genomic identification of primary atopic disorders (unrelated to platelet release) |
| [27885969](https://pubmed.ncbi.nlm.nih.gov/27885969/) | 2016 | Review | Critical Care | ICU/emergency medicine symposium abstracts, sepsis-related |
| [11079020](https://pubmed.ncbi.nlm.nih.gov/11079020/) | 2000 | Review | Arch Pathol Lab Med | Pathophysiology of heparin-induced thrombocytopenia (adverse effect, not this indication) |
| [32829961](https://pubmed.ncbi.nlm.nih.gov/32829961/) | 2021 | Review | Blood Reviews | Cytokine release, coagulopathy and antithrombin III in COVID-19 |
| [27882374](https://pubmed.ncbi.nlm.nih.gov/27882374/) | 2017 | Review | Thromb Haemost | Cancer-associated venous thromboembolism management |
| [28646118](https://pubmed.ncbi.nlm.nih.gov/28646118/) | 2017 | Review | Blood | DOACs for treatment of HIT |
| [23839295](https://pubmed.ncbi.nlm.nih.gov/23839295/) | 2013 | Cohort | Curr Opin Hematol | Tissue factor pathway inhibitor isoforms — coagulation biology, not platelet release |
| [32898858](https://pubmed.ncbi.nlm.nih.gov/32898858/) | 2021 | Cohort | Blood | PF4-dependent assay for HIT diagnosis |
| [35763168](https://pubmed.ncbi.nlm.nih.gov/35763168/) | 2022 | Case Report | J Thromb Thrombolysis | Limb ischemia from spontaneous HIT in COVID-19 |

**Assessment:** This appears to be a spurious knowledge-graph association (likely driven by "heparin–platelet" co-occurrence from HIT literature) rather than a genuine repurposing signal. **Decision: Hold — do not advance.**

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary candidate (thrombophilia due to protein C deficiency) has a plausible mechanistic rationale but zero supporting trials or literature (L5, model prediction only). The secondary candidate (primary platelet release disorder) has evidence volume but it argues against the pairing on mechanistic grounds. Neither candidate currently meets the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) documentation — currently a High-severity data gap (DG002)
- Targeted literature/trial search specifically for heparin use in protein C deficiency thrombophilia (bridging anticoagulation, acute VTE management in this population)
- If pursuing the platelet-disorder candidate further, independent confirmation that the TxGNN association is not an artifact of HIT-related co-occurrence in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

