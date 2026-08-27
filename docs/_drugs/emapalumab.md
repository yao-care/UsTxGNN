---
layout: default
title: Emapalumab
parent: 僅模型預測 (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Emapalumab
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

# Emapalumab: From Primary Hemophagocytic Lymphohistiocytosis to Infection-Associated Hemophagocytic Lymphohistiocytosis

> **Note on indication selection**: This evidence pack contains 10 TxGNN-predicted indications for emapalumab, ranked by model score. The #1-ranked node (*autosomal recessive familial Mediterranean fever*) has zero supporting trials or literature (Evidence Level L5, Hold). This report instead focuses on **"hemophagocytic syndrome associated with an infection"** (rank 3, score 99.99%), the only candidate in this pack backed by an actual clinical trial and a substantial literature base, and the highest decision stage reached (S2, Proceed with Guardrails). The other HLH-spectrum candidates (malignancy-associated HLH, XLP1/SH2D1A deficiency) are mechanistically related but lack direct evidence and are noted only in passing.

## One-Sentence Summary

Emapalumab is an anti-interferon-gamma (IFN-γ) monoclonal antibody originally established for **Primary Hemophagocytic Lymphohistiocytosis (pHLH)**. Within this evidence pack, TxGNN predicts it may also be effective for **infection-associated (secondary) hemophagocytic lymphohistiocytosis** — most notably EBV-triggered HLH — with **1 clinical trial** and **20 publications** currently identified, though the trial was terminated with only 7 patients enrolled.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary Hemophagocytic Lymphohistiocytosis (pHLH) — inferred from literature in this pack (e.g., PMID 32374962); not recorded in the regulatory dataset (see US Market Status) |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection (secondary/infection-associated HLH) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| US Market Status | Not marketed (per this dataset — see note below) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on market status**: The regulatory dataset in this evidence pack records 0 licenses and "not marketed." A Blocking data gap (DG001) flags that the official label (warnings/contraindications) could not be retrieved, so this status should be treated as a data-collection gap rather than a confirmed absence of approval, and should be re-verified from primary regulatory sources before use in decision-making.

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not available in the structured `original_moa` field (marked as a data gap, DG002). However, the literature captured in this evidence pack is consistent: emapalumab is described repeatedly as "a fully human monoclonal antibody that neutralizes interferon-gamma (IFN-γ)... a key cytokine driving the inflammation and tissue damage seen in HLH" (NCT03985423 summary; PMID 32374962, 39117840, 38014905).

Primary HLH and infection-associated (secondary) HLH share the same core pathophysiology: uncontrolled IFN-γ-driven macrophage activation and cytokine storm. The literature in this pack explicitly frames secondary HLH — including infection-, malignancy-, and rheumatologic-disease-associated forms — as sharing the hyperinflammatory pathobiology of primary HLH, with EBV infection being the dominant infectious trigger described across multiple case series (PMID 38691058, 39719162, 39331881, 41066671). This makes the extension of an IFN-γ-neutralizing mechanism from primary to infection-triggered HLH a direct, biologically grounded extrapolation rather than a speculative new mechanism — TxGNN's high score for this node reflects a real mechanistic neighbor to the drug's established indication, not an artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03985423](https://clinicaltrials.gov/study/NCT03985423) | Phase 2/3 | Terminated | 7 | Open-label, single-arm study of emapalumab in adult HLH patients (etiologies include autoimmune disease, infection, malignancy) evaluating efficacy, safety and pharmacokinetics; terminated early with only 7 of planned enrollment completed, limiting statistical power. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32374962](https://pubmed.ncbi.nlm.nih.gov/32374962/) | 2020 | Cohort (pivotal) | N Engl J Med | Foundational efficacy/safety study of emapalumab in primary HLH in children; establishes the IFN-γ-neutralization mechanism this prediction extrapolates from. |
| [41337692](https://pubmed.ncbi.nlm.nih.gov/41337692/) | 2026 | Cohort (real-world US) | Blood Advances | REAL-HLH study: retrospective chart review across 33 US hospitals on real-world emapalumab use and outcomes in secondary HLH populations, including malignancy- and infection-triggered cases. |
| [38014905](https://pubmed.ncbi.nlm.nih.gov/38014905/) | 2024 | PK/Exposure-safety analysis | Pediatric Blood & Cancer | Exposure-safety relationship analysis for emapalumab in HLH; examines risk of immune dysfunction/immunosuppression from IFN-γ blockade. |
| [34096649](https://pubmed.ncbi.nlm.nih.gov/34096649/) | 2021 | Review | Acta Paediatrica | Reviews virus-triggered secondary HLH, distinguishing it from primary HLH and describing shared hyperinflammatory/hypercytokinemic mechanisms. |
| [39117832](https://pubmed.ncbi.nlm.nih.gov/39117832/) | 2024 | Review | Adv Exp Med Biol | Discusses overlap between primary HLH, secondary HLH (including infection-associated), and sepsis-induced MODS, and implications for targeted therapy. |
| [39117840](https://pubmed.ncbi.nlm.nih.gov/39117840/) | 2024 | Review | Adv Exp Med Biol | Reviews the role of IFN-γ in cytokine storm syndromes and summarizes anti-IFN-γ therapeutic approaches, including emapalumab. |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Case series | J Pediatr Hematol Oncol | Emapalumab combined with ruxolitinib and dexamethasone effectively treated EBV-associated HLH complicated by multiorgan damage and severe infection. |
| [39719162](https://pubmed.ncbi.nlm.nih.gov/39719162/) | 2025 | Case series | Transplant Immunology | Low-dose emapalumab combined with chemotherapy controlled EBV-associated HLH in 3 adult patients. |
| [39331881](https://pubmed.ncbi.nlm.nih.gov/39331881/) | 2024 | Case series | Medicine | Case series describing emapalumab as an effective therapeutic option for EBV-associated HLH refractory to standard protocols. |
| [41066671](https://pubmed.ncbi.nlm.nih.gov/41066671/) | 2025 | Case series | Annals of Medicine | Emapalumab improved outcomes in 3 pediatric EBV-HLH patients with multiple organ dysfunction syndrome. |

---

## US Market Information

According to this evidence pack's regulatory dataset, no NDA/BLA licenses are on file for emapalumab and market status is recorded as "not marketed." This coincides with Blocking data gap DG001 (TFDA/label warnings and contraindications not retrieved), so the official approval and label status should be independently re-verified rather than relied on from this dataset alone.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were retrieved in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is strong — infection-associated (especially EBV-triggered) secondary HLH shares the same IFN-γ-driven pathophysiology as emapalumab's established primary-HLH mechanism, and this is the only predicted indication in the pack with any clinical trial or literature support (1 terminated Phase 2/3 trial, 10+ relevant publications, evidence level L3). However, the supporting trial was terminated with only 7 patients and no data reach RCT-level confirmation specifically for infection-triggered HLH; most direct clinical support is case-series level.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain official label warnings/contraindications from the regulatory source
- Resolve High-severity data gap DG002: confirm formal MOA documentation via DrugBank
- Investigate why NCT03985423 was terminated and whether follow-on/replacement trials exist
- Seek RCT-level or larger prospective data specifically in infection-/EBV-associated secondary HLH (current evidence is cohort/case-series level)
- Obtain formal drug-drug interaction data (current query: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

