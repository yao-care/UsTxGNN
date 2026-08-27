---
layout: default
title: Isavuconazonium
parent: 僅模型預測 (L5)
nav_order: 812
evidence_level: L5
indication_count: 2
---

# Isavuconazonium
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

# Isavuconazonium: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Isavuconazonium is a triazole antifungal prodrug (active metabolite: isavuconazole) that inhibits fungal CYP51 to block ergosterol synthesis; its original approved indication is not specified in the available data. The TxGNN model predicts potential efficacy in **pneumocystosis (*Pneumocystis jirovecii* pneumonia)**, but this prediction currently has **no supporting clinical trials or literature**, and the proposed mechanism may actually work against efficacy. A second, more mechanistically plausible candidate — **mycetoma** — is also flagged, supported by one review-level publication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available data (no Taiwan license record on file) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| Taiwan Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original-indication and formal MOA fields are not available in this evidence pack (flagged as data gaps DG001/DG002). Based on the mechanistic description that is available, isavuconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol biosynthesis and disrupting fungal cell membrane integrity.

For pneumocystosis specifically, however, this mechanism is questionable rather than clearly supportive. *Pneumocystis jirovecii* relies primarily on **cholesterol**, not ergosterol, in its pathogenic trophic-form membrane — ergosterol is present only in the minor cyst stage. This is the established pharmacological reason why triazole antifungals (including fluconazole and itraconazole) have historically shown poor clinical activity against pneumocystosis and are not part of standard treatment (TMP-SMX remains first-line). The TxGNN score is high (99.56%), but this appears to reflect a knowledge-graph association rather than a pharmacologically grounded hypothesis — consistent with its L5 evidence level and zero corroborating trials or publications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Isavuconazonium is currently **not marketed** in Taiwan, with no license records on file (0 NDAs).

---

## Additional Predicted Indication: Mycetoma (Rank 2)

A second candidate indication, **mycetoma**, shows comparatively stronger — though still preliminary — support and is included here because its evidence profile materially changes the overall risk/benefit picture for this drug.

| Item | Content |
|------|------|
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Decision Stage | S1 |
| Recommendation | Research Question |

**Mechanistic rationale:** Eumycetoma is caused primarily by filamentous fungi such as *Madurella mycetomatis*, whose cell membranes depend on ergosterol — a biologically plausible target for triazoles. Itraconazole is already standard-of-care for eumycetoma, and a newer-generation triazole (fosravuconazole) has shown efficacy in trials, supporting class-level plausibility. Isavuconazole's broad-spectrum activity against filamentous fungi (including *Aspergillus*) further supports potential activity, though no isavuconazole-specific trial or preclinical data against *M. mycetomatis* currently exists.

**Literature Evidence**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasites & Vectors | Review of the WHO NTD drug pipeline, covering oral anti-infective drugs (including triazole-class agents) under development or off-label use for neglected tropical diseases such as mycetoma |

**Clinical Trials:** Currently no related clinical trials registered

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (pneumocystosis) has an L5 evidence level with zero supporting trials or literature, and the proposed mechanism (ergosterol-pathway inhibition) is arguably inconsistent with *P. jirovecii*'s cholesterol-dependent trophic-form biology — a known reason triazoles underperform against this pathogen. The drug is also unmarketed in Taiwan with no safety/label data on file, blocking any S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed original indication(s) and formal MOA documentation from DrugBank (DG002)
- If pursuing the pneumocystosis hypothesis: preclinical evidence addressing the cholesterol-vs-ergosterol mechanistic concern before further investment
- If pursuing mycetoma instead (better-supported secondary candidate): isavuconazole-specific in vitro/in vivo data against *M. mycetomatis*, given the current evidence is class-level (itraconazole, fosravuconazole) rather than drug-specific
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

