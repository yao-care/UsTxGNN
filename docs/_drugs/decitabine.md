---
layout: default
title: Decitabine
parent: 僅模型預測 (L5)
nav_order: 576
evidence_level: L5
indication_count: 1
---

# Decitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Decitabine: From Myelodysplastic Syndromes to Refractory Cytopenia of Childhood

## One-Sentence Summary

Decitabine is a DNA hypomethylating agent (DNMT inhibitor) with established efficacy in adult myelodysplastic syndromes (MDS), where FDA approval has been granted for that indication.
The TxGNN model predicts it may be effective for **Refractory Cytopenia of Childhood (RCC)**, a rare pediatric subtype of MDS sharing overlapping epigenetic pathology.
Currently, **no registered clinical trials** and **1 retrospective cohort publication** support this specific direction, placing this candidate at an early-evidence stage that warrants further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myelodysplastic syndromes (MDS) — adult population, FDA-approved |
| Predicted New Indication | Refractory Cytopenia of Childhood (RCC) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| US Market Status | No license records in current dataset |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Decitabine is a nucleoside analog that functions as a **DNA methyltransferase (DNMT) inhibitor**. By incorporating into DNA during replication, it covalently traps DNMT enzymes, leading to progressive DNA hypomethylation. This mechanism reactivates silenced tumor suppressor genes and promotes differentiation of dysplastic hematopoietic progenitors — the core therapeutic rationale in myeloid disorders.

Refractory Cytopenia of Childhood is a distinct pediatric MDS subtype characterized by hypocellular bone marrow, peripheral cytopenias, and aberrant epigenetic regulation. RCC shares key molecular features with adult MDS, including dysregulation of DNMT3A/TET2 methylation pathways, making it biologically plausible that a DNMT inhibitor proven in adult MDS would carry activity in RCC. The clinical context further supports this: decitabine is used in pediatric MDS as bridging therapy before allogeneic hematopoietic stem cell transplantation (allo-HSCT), specifically because low-dose hypomethylation achieves disease control without excessive myelosuppression.

The TxGNN model's high confidence score (99.03%) reflects this strong mechanistic continuity. The prediction essentially extends an established adult indication into a pediatric subtype with shared pathobiology, which is one of the most defensible repurposing hypotheses in hematological oncology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Decitabine in Refractory Cytopenia of Childhood.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Retrospective Cohort | BMC Pediatrics | Single-center 10-year experience with decitabine-combined minimally myelosuppressive regimen (DAC + MMR) bridging to allo-HSCT in children with MDS; demonstrates feasibility of this approach in controlling disease prior to transplantation without excessive marrow toxicity |

---

## US Market Information

No NDA/licensing records are available in the current dataset for Decitabine. Note: Decitabine (brand name Dacogen) holds FDA approval for adult MDS in the United States — this should be retrieved and integrated into a follow-up data pull to complete regulatory context.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Hypomethylating Agent (Nucleoside analog / DNMT inhibitor) |
| Myelosuppression Risk | **High** — Neutropenia, thrombocytopenia, and anemia are the most common dose-limiting toxicities; CBC nadir typically occurs within 2–4 weeks of treatment initiation |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential and platelet count (before each cycle and as clinically indicated), liver function tests, renal function (serum creatinine), serum electrolytes |
| Handling Protection | Must be handled following cytotoxic drug safety regulations — gown, gloves, and appropriate containment during preparation and administration |

---

## Safety Considerations

No key warnings, contraindications, or drug interaction data are available in the current Evidence Pack. Detailed safety information should be obtained directly from the Decitabine (Dacogen) FDA-approved prescribing information before any clinical or regulatory decision-making.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Decitabine's DNMT-inhibition mechanism and the epigenetic pathology of RCC is scientifically sound and directly extends an established adult MDS indication into a pediatric subtype; however, the current evidence base consists of a single retrospective cohort study with no prospective trials, which is insufficient to support unguarded clinical advancement.

**To proceed, the following is needed:**

- **Regulatory data retrieval**: Pull the complete US FDA Dacogen label (prescribing information) to populate warnings, contraindications, boxed warnings, and dosing for pediatric populations
- **Mechanism of action documentation**: Formally document decitabine's DNMT1/3A inhibition mechanism from DrugBank to support the mechanistic rationale section
- **Clinical trial landscape review**: Search ClinicalTrials.gov and ICTRP for pediatric MDS or RCC trials that included decitabine even as a secondary arm, as targeted RCC-specific trials may be registered under broader pediatric MDS identifiers
- **Additional literature search**: Expand PubMed query to include "decitabine pediatric MDS" and "5-azacytidine RCC" to capture hypomethylating class evidence beyond this single paper
- **Pediatric dosing assessment**: Identify if any published pediatric pharmacokinetic/pharmacodynamic data exist for weight-based or BSA-based decitabine dosing in the RCC/pediatric MDS population
- **Escalation path**: If supporting evidence is identified, consider prospective case series or a Phase 1/2 open-label pediatric trial as the appropriate next clinical step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

