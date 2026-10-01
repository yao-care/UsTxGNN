---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 1217
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Tetrabenazine: From Huntington's Disease Chorea to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

Tetrabenazine is a marketed oral drug, best known for reducing chorea in Huntington's disease (this comes from a retrieved trial, not from the license records).
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**, but this is a model prediction only, with **0 clinical trials** and **20 publications** that are disease background and do not mention tetrabenazine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Huntington's disease chorea (inferred from a retrieved trial; the license records list no indication text) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (total licenses, including generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Tetrabenazine is generally described as a reversible VMAT2 inhibitor that depletes presynaptic monoamines, which explains its use in hyperkinetic movement disorders such as chorea.

The predicted disease is a genetic cystic disorder of the kidney and liver, linked to genes such as GANAB and PRKCSH. It has no known connection to VMAT2 or monoamine pathways, so the very high TxGNN score has no supporting mechanism. None of the 20 retrieved papers mention tetrabenazine.

The other nine top predictions (renal-hepatic-pancreatic dysplasia, Joubert syndrome with renal defect, karyomegalic interstitial nephritis and others) are also model-only predictions at L5 with no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these papers studies tetrabenazine. They describe the disease background, and no RCTs were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL guidance on diagnosing and managing cystic liver diseases, including polycystic liver disease |
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | Am J Gastroenterol | ACG guideline on focal liver lesions, including hepatic cystic lesions and polycystic liver disease |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | ADPKD is a systemic disorder with liver cysts and other extrarenal complications |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic liver disease in ADPKD; tolvaptan can slow renal decline |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic and phenotypic overlap between ADPKD and polycystic liver disease (PKD1, PKD2, GANAB, PRKCSH and others) |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of polycystic kidney and liver diseases; cilia defects are central to pathogenesis |
| [29175241](https://pubmed.ncbi.nlm.nih.gov/29175241/) | 2018 | Clinical management | J Hepatol | Case-based approach to managing polycystic liver disease |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annu Rev Pathol | Mechanisms and treatment advances in polycystic liver disease |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | Hepat Med | Pathophysiology, diagnosis and treatment of polycystic liver disease |
| [40296340](https://pubmed.ncbi.nlm.nih.gov/40296340/) | 2025 | Cohort | Ann Transplant | Retrospective outcomes of organ transplantation in 9 patients with polycystic liver disease |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021894 | Xenazine (Lundbeck Pharmaceuticals LLC) | Tablet | Not listed in the source data |
| ANDA206129 | Tetrabenazine (Sun Pharmaceutical Industries, Inc.) | Tablet | Not listed in the source data |
| ANDA213316 | Tetrabenazine (Heritage / Avet Pharmaceuticals) | Tablet | Not listed in the source data |
| ANDA207682 | Tetrabenazine (Precision Dose Inc.) | Tablet | Not listed in the source data |

The route is oral. Tablet and coated tablet forms are registered.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the source data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials, none of the retrieved papers evaluate tetrabenazine, and no mechanism links VMAT2 inhibition to a genetic cystic kidney and liver disorder.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required for any safety screening
- Detailed mechanism of action data from DrugBank
- A credible biological hypothesis connecting monoamine depletion to cyst formation, backed by preclinical evidence
- A review of the other top-ranked predictions, or a decision to deprioritize this drug for repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

