---
layout: default
title: Abiraterone Acetate Niraparib Tosylate Monohydrate
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate Niraparib Tosylate Monohydrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Abiraterone Acetate / Niraparib Tosylate Monohydrate: Drug Repurposing Assessment

## One-Sentence Summary

Abiraterone Acetate / Niraparib Tosylate Monohydrate is a fixed-dose oral combination of two anticancer agents — a CYP17A1 androgen biosynthesis inhibitor and a PARP-1/2 inhibitor — approved in the United States as Akeega® for metastatic castration-resistant prostate cancer (mCRPC) with *BRCA* mutations.
**No TxGNN repurposing predictions were generated** for this drug combination, as it carries no Taiwan TFDA license records (0 licenses found), preventing the model from mapping a baseline indication entry.
Without a scored prediction candidate, this report documents the data gaps and outlines the remediation steps required before a formal repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no TFDA license data |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction is currently available for this combination. The following describes the known pharmacological basis of each component to support future analysis once the data gaps are resolved.

**Abiraterone Acetate** is an irreversible inhibitor of CYP17A1 (17α-hydroxylase/C17,20-lyase), the enzyme responsible for androgen biosynthesis in the testes, adrenal glands, and intratumoural tissue. By suppressing testosterone and dihydrotestosterone production, it starves androgen receptor–positive prostate tumour cells of their primary proliferative signal. It is used in combination with prednisone to suppress residual adrenal androgen output after castration.

**Niraparib Tosylate** is a potent PARP-1/2 inhibitor. It traps PARP complexes at DNA single-strand break sites, causing replication fork collapse and synthetic lethality in tumour cells with homologous recombination repair deficiency (HRD) — particularly those harbouring *BRCA1/2* mutations. The rationale for combining niraparib with abiraterone rests on evidence that androgen receptor signalling cross-talks with DNA repair pathways: androgen deprivation may upregulate HRD, thereby sensitising mCRPC cells to PARP inhibition. This mechanistic synergy formed the basis for the FDA approval of Akeega® in August 2023.

Because neither component is individually registered with the Taiwan TFDA under this combination's name, TxGNN cannot locate a seed indication node to propagate predictions. Repurposing directions for related HRD-positive solid tumours (e.g., BRCA-mutant breast cancer, ovarian cancer, pancreatic cancer) remain biologically plausible but must be evaluated by running TxGNN separately on each component's DrugBank entry.

---

## Clinical Trial Evidence

Currently no related clinical trials are available from the TxGNN evidence pipeline for this drug combination.

> **Reference for context:** The pivotal Phase 3 MAGNITUDE trial (NCT03748641) evaluated niraparib + abiraterone acetate/prednisone vs. placebo + abiraterone acetate/prednisone in mCRPC with HRD/BRCA alterations (n = 423 HRD-positive cohort). This trial supported the FDA approval but falls outside the TxGNN prediction scope and is not included in the scored evidence.

---

## Literature Evidence

Currently no related literature is available from the TxGNN evidence pipeline for this combination.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Abiraterone: CYP17A1 inhibitor (hormonal); Niraparib: PARP inhibitor (DNA damage response) |
| Myelosuppression Risk | **High** (driven by niraparib) — thrombocytopenia, anaemia, and neutropenia are common dose-limiting toxicities; incidence of Grade ≥3 thrombocytopenia ~14% in MAGNITUDE |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly for the first month, then monthly); liver function (ALT/AST/bilirubin); blood pressure; serum potassium; renal function (SCr/eGFR) |
| Handling Protection | Both components are oral solid dosage forms; follow cytotoxic drug handling regulations, including appropriate PPE during dose preparation or dispensing |

---

## Safety Considerations

Drug interaction data was not found (DDI query status: `not_found`; 0 interactions retrieved).

All key warnings and contraindications are currently unavailable pending resolution of Data Gap DG001. Please refer to the Akeega® US package insert and individual component prescribing information for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This drug combination is not registered in Taiwan, carries no MOA data in the current Evidence Pack, and TxGNN generated no repurposing predictions — the evidence base is insufficient to support a formal repurposing recommendation at this stage.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Download and parse TFDA package insert PDFs for any individually licensed components (Abiraterone Acetate and/or Niraparib) to retrieve warnings and contraindications
- **Resolve DG002 (High):** Query DrugBank API using known IDs — Abiraterone Acetate (DB05812) and Niraparib (DB11901) — to populate MOA fields
- **Re-run TxGNN per component:** Generate separate Evidence Packs for Abiraterone Acetate and Niraparib Tosylate individually; combine findings post-prediction
- **Assess Taiwan registration pathway:** Determine whether a new drug application (NDA) for the Akeega® combination or its individual components would be feasible given local regulatory requirements
- **Establish an HRD biomarker strategy:** Any clinical repurposing effort should include *BRCA1/2* and HRD testing protocols as companion diagnostics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

