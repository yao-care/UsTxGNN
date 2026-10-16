---
layout: default
title: Posaconazole
parent: Model Prediction Only (L5)
nav_order: 1065
evidence_level: L5
indication_count: 1
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Posaconazole: From Invasive Fungal Infections to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal originally used for fungal infections such as aspergillosis, candidiasis (including oral candidiasis), and histoplasmosis.
The TxGNN model predicts it may be effective for **Pneumocystosis**, but only **1 loosely related clinical trial** (which tests a different drug) and **5 general publications** (none directly testing posaconazole for this condition) are available, so the supporting evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chromomycosis, coccidioidomycosis, aspergillosis, candidiasis, histoplasmosis, sporotrichosis, fusariosis, mycetoma and other fungal infections |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 14 (2 NDAs and 12 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, posaconazole is a triazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis. Its efficacy against several fungal infections is established.

The prediction is weak mechanistically. *Pneumocystis jirovecii* has cholesterol rather than ergosterol in its membranes, so azoles are generally considered ineffective against it. First-line therapy is trimethoprim-sulfamethoxazole. The very high TxGNN score likely reflects the drug's broad antifungal class association in the knowledge graph rather than a true mechanistic link.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin (an echinocandin, not posaconazole) vs standard antimicrobial regimen for preventing invasive fungal disease in adults undergoing allogeneic blood and marrow transplantation. It provides no direct evidence for posaconazole. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and Pneumocystis pneumonia. Notes that mould-active posaconazole prophylaxis reduced invasive fungal infections in high-risk haemato-oncological patients. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | The Lancet Infectious Diseases | British Society for Medical Mycology 2025 update on diagnosing serious fungal diseases. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 Chinese guidelines for diagnosing and managing invasive pulmonary fungal diseases. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective study of infectious complications in acute graft-versus-host disease after liver transplantation. |

None of these publications tests posaconazole for pneumocystosis.

## US Market Information

All 14 US authorizations are listed as cancelled. The data compiled for this report contains no approved indication text. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205596 | NOXAFIL (Merck Sharp & Dohme LLC) | Solution | Not available (cancelled) |
| NDA205053 | Posaconazole (Bryant Ranch Prepack) | Tablet, coated | Not available (cancelled) |
| ANDA214842 | Posaconazole (Eugia US LLC) | Injection | Not available (cancelled) |
| ANDA212226 | Posaconazole (Golden State Medical Supply) | Tablet, delayed release | Not available (cancelled) |
| ANDA219057 | Posaconazole (Camber Pharmaceuticals) | Solution | Not available (cancelled) |

Available dosage forms include injectable, oral (delayed-release and coated tablets) and solution.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. The examples below are from the 20 that were itemized.
  - **Major**: loperamide, triamcinolone, budesonide
  - **Moderate** (examples): famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, aprepitant, clarithromycin, saxagliptin, bisacodyl

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by a plausible mechanism, because *Pneumocystis* lacks ergosterol and azoles are generally ineffective against it. No trial or publication directly tests posaconazole for pneumocystosis, and the only trial found studies a different drug. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Mechanism of action data, plus evidence that posaconazole has activity against *Pneumocystis*
- Preclinical or clinical studies of posaconazole in pneumocystosis, or a review of any posaconazole-containing prophylaxis trials that report *Pneumocystis* outcomes
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Clarification of the regulatory status, since all US licenses are listed as cancelled
- Comparison against trimethoprim-sulfamethoxazole, the standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

