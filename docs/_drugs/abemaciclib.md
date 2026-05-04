---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib (Verzenio®) is a selective CDK4/6 inhibitor used as a cornerstone therapy for hormone receptor-positive (HR+), HER2-negative breast cancer.
The TxGNN model predicts it may have activity against **Rheumatoid Arthritis**, supported by **0 clinical trials** and **1 publication**.
Critically, the sole available evidence reflects a **negative signal** — the identified publication documents immune-mediated adverse events triggered by CDK4/6 inhibitors, rather than any therapeutic benefit for RA.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+/HER2- Breast Cancer (inferred from clinical trial context; no US regulatory license records captured in this dataset — likely a data gap) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (data gap — Verzenio® holds known FDA approval for breast cancer) |
| Number of NDAs | 0 (data gap) |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack. Based on known information, Abemaciclib is a selective CDK4/6 inhibitor that blocks cyclin-dependent kinases 4 and 6, arresting the cell cycle at the G1/S checkpoint. Its efficacy in HR+/HER2- breast cancer has been demonstrated in landmark Phase 3 trials including MONARCH 2 (NCT02107703) and monarchE.

CDK4/6 kinases function beyond tumor proliferation — they also regulate T-cell activation and immune homeostasis. Since rheumatoid arthritis (RA) is driven by dysregulated T-cell activation and autoimmune inflammation, there is a theoretical basis for CDK4/6 inhibition exerting immunomodulatory effects relevant to RA pathology.

However, the available clinical evidence points in the opposite direction. The only identified publication (PMID 40504547, 2025) is a retrospective pharmacovigilance study reporting that CDK4/6 inhibitors may **trigger** autoimmune reactions — including RA-like conditions — as adverse events in breast cancer patients. This constitutes a safety concern rather than therapeutic support, and the mechanistic hypothesis remains entirely speculative at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Abemaciclib in Rheumatoid Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Retrospective Pharmacovigilance | The Oncologist | Retrospective cohort in HR+/HER2- breast cancer patients receiving CDK4/6 inhibitors + endocrine therapy; examines prevalence of pre-existing and emerging autoimmune diseases including RA-like conditions. Findings represent a **negative signal** — CDK4/6i may provoke, not treat, autoimmune disease |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted Therapy (Selective CDK4/6 Inhibitor) |
| Myelosuppression Risk | Moderate — neutropenia and leukopenia are common; generally less severe than palbociclib or ribociclib; dose interruptions or reductions are frequently required |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Complete blood count with differential (neutrophil count); liver function tests (ALT, AST, bilirubin); renal function; QTc interval on ECG; pulmonary symptoms (interstitial lung disease/pneumonitis) |
| Handling Protection | Handle as a hazardous drug per institutional cytotoxic drug handling protocols; oral capsule/tablet formulation — gloves required during preparation and dispensing |

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Cardiovascular Safety Note**: Pharmacovigilance data from the broader evidence pack shows CDK4/6 inhibitors — including Abemaciclib — are associated with QTc prolongation (PMID 39254653, 41422771) and potential direct cardiac damage (PMID 36164682). At least one case report links Abemaciclib to coronary plaque erosion and acute MI onset (PMID 33260247). These signals are especially consequential when evaluating repurposing into non-oncology indications where the benefit–risk profile has not been characterized.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (97.32%), the only available evidence for Abemaciclib in Rheumatoid Arthritis is a pharmacovigilance study documenting autoimmune reactions as drug-induced adverse events — a signal running counter to the therapeutic hypothesis. No clinical trials have explored this indication, and the immunomodulatory mechanism remains speculative.

**To proceed with RA evaluation, the following is needed:**

- Preclinical validation in RA models (e.g., collagen-induced arthritis, synoviocyte cultures) to determine whether CDK4/6 inhibition suppresses or exacerbates synovial inflammation
- Mechanistic clarification distinguishing "CDK4/6 inhibition triggering autoimmunity" (documented risk) from "suppressing pathological T-cell activation" (hypothesized benefit)
- Complete MOA data from DrugBank (Data Gap DG002)
- US FDA package insert review for full contraindications and warnings (Data Gap DG001)

---

> **Higher-Priority Repurposing Candidates Identified in This Pack**
>
> Two other TxGNN predictions in this evidence pack carry stronger biological rationale than the Rank 1 RA prediction and are recommended for prioritized follow-up:
>
> - ⭐ **Amyotrophic Lateral Sclerosis (ALS)** — Rank 10 · L4 · *Research Question*
>   PMID 38596406 (2024) directly demonstrates Abemaciclib accelerates autophagic flux and reduces TDP-43 aggregate accumulation in ALS cell models. Mechanistic pathway: CDK4/6 inhibition → RB dephosphorylation → TFEB activation → enhanced autophagy → TDP-43 clearance. This is the most biologically coherent repurposing signal in the entire pack.
>
> - **Multiple Endocrine Neoplasia (MEN)** — Rank 3 · L3 · *Research Question*
>   Menin (MEN1 gene product) is a direct regulator of CDK4; CDK4/6 is overactivated in MEN1-related neuroendocrine tumors (NETs). Preclinical NET model activity for CDK4/6 inhibitors has been reported, and ongoing umbrella trials (e.g., NCT03280563) may yield relevant data. Warrants focused literature and trial monitoring.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

