---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 1065
evidence_level: L5
indication_count: 1
---

# Posaconazole
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

# Posaconazole: From Invasive Fungal Infection Prophylaxis to Pneumocystosis

## One-Sentence Summary

> Posaconazole is a triazole antifungal currently used as broad-spectrum prophylaxis against invasive fungal infections (Aspergillus, Candida, Mucorales) in immunocompromised and transplant patients.
> The TxGNN model predicts it may also be effective for **Pneumocystosis (Pneumocystis jirovecii pneumonia)**,
> but this direction is currently supported only by **2 indirectly relevant clinical trials** and **5 background literature references** — none of which directly test posaconazole against Pneumocystis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of invasive fungal infections (Aspergillus, Candida, Mucorales) in immunocompromised/transplant patients *(derived from repurposing rationale; official label text not available)* |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the source label/DrugBank record for this evidence pack. Based on known pharmacology, posaconazole is a triazole antifungal that inhibits lanosterol 14α-demethylase (CYP51), blocking ergosterol synthesis in fungal cell membranes. It is currently used as broad-spectrum antifungal prophylaxis in hematology/transplant patients, covering Aspergillus, Candida, and Mucorales species.

However, the mechanistic link to Pneumocystosis is weak. *Pneumocystis jirovecii* is an atypical fungus with very low membrane ergosterol content and a synthesis pathway that differs substantially from typical filamentous/yeast fungi, so triazole antifungals have limited direct evidence of fungicidal activity against it. Posaconazole's clinical role today is prophylactic coverage of other mold/yeast pathogens in transplant and hematologic malignancy patients — it is **not** first-line therapy for PJP (which remains TMP-SMX).

The predicted association therefore appears to arise from indication co-occurrence in high-risk immunocompromised/transplant populations (where posaconazole prophylaxis and PJP risk overlap clinically) rather than from a direct pharmacological mechanism against *Pneumocystis*. This is an indirect, inferential link rather than established antifungal activity evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin (an echinocandin, **not posaconazole**) vs. standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic HSCT recipients. Relevance grade C — different drug class, disease-domain background only. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens after mismatched unrelated donor PBSCT; may include antifungal prophylaxis (potentially posaconazole) as supportive care, but not designed to evaluate posaconazole for pneumocystosis specifically. Relevance grade C — indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet. Infectious Diseases | UK best-practice update on diagnosis of serious fungal diseases (diagnostic methods, not posaconazole-specific treatment evidence). |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | Chinese 2025 clinical practice guideline for diagnosis/management of invasive pulmonary fungal disease. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and PJP; notes posaconazole's established role as mould-active prophylaxis reducing invasive candidiasis in high-risk hemato-oncology patients (not direct PJP treatment data). |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK/PD) | Clinical Pharmacokinetics | Pulmonary epithelial lining fluid penetration of antifungal/antitubercular agents — pharmacokinetic background only. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort/Case series | Transplant Infectious Disease | Infectious complications (including fungal) in acute GVHD after liver transplant; general infection epidemiology, not posaconazole-PJP specific. |

---

## US Market Information

Currently no marketing authorizations recorded for this drug in the reference jurisdiction dataset (market status: Not Marketed, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Warning labels, contraindications, and drug-drug interaction data are flagged as outstanding data gaps (including a **blocking** gap for TFDA label warnings/contraindications) and could not be sourced for this evidence pack.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence directly evaluates posaconazole for pneumocystosis — all available trials/publications are indirect background references (different drug class, general infection epidemiology, or diagnostic guidelines). The mechanistic rationale itself is characterized as inferential rather than established, and posaconazole is not currently marketed in the reference jurisdiction, further limiting near-term actionability.

**To proceed, the following is needed:**
- Resolve blocking safety data gap: TFDA (or equivalent) label warnings/contraindications for posaconazole
- Obtain detailed mechanism of action (MOA) documentation from DrugBank/label to support or refute the mechanistic hypothesis
- Identify or commission a clinical study directly testing posaconazole efficacy against *Pneumocystis jirovecii* (current evidence base has no direct trials)
- Clarify market/regulatory pathway status, since the drug currently has no license record in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

