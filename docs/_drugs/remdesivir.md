---
layout: default
title: Remdesivir
parent: Model Prediction Only (L5)
nav_order: 1116
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir (marketed as Veklury) is an intravenous antiviral, and the Evidence Pack's trials and literature center on COVID-19. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it. This is a model artifact rather than a credible repurposing lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licensing data provided; COVID-19 is inferred from the trials and literature in the pack |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Remdesivir is a nucleotide analog prodrug that inhibits viral RNA-dependent RNA polymerase (RdRp). Its known use is against RNA viruses such as SARS-CoV-2. It was also studied for Ebola virus persistence in the PREVAIL IV trial.

Multiple endocrine neoplasia is a hereditary tumor syndrome (MEN1/RET). It has no viral driver and no RdRp target, so no plausible mechanistic link exists between the two. The high TxGNN score (0.995) most likely reflects knowledge-graph proximity rather than biology, and no trial or publication supports it. The prediction is therefore not considered mechanistically credible.

Other predictions for this drug are also weak:
- **HIV infection (rank 2):** 23 trials and 20 publications were matched, but they are COVID-19 or Ebola studies linked through HIV-related keywords or co-administered antiretrovirals. None test remdesivir as an HIV treatment, and HIV depends on reverse transcriptase rather than RdRp. This is indirect evidence only (L4).
- **SIV infection, feline AIDS, a rare neurodevelopmental disorder and homozygous familial hypercholesterolemia (ranks 3–6):** No supporting evidence and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for multiple endocrine neoplasia.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA214787 | Veklury (Gilead Sciences, Inc.) | Injection, powder, lyophilized, for solution | Not listed in the data provided |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no plausible mechanism, since remdesivir targets viral RdRp and multiple endocrine neoplasia is a hereditary tumor syndrome. The high TxGNN score is likely a graph artifact and does not justify further investment.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence for remdesivir in multiple endocrine neoplasia; none currently exists
- The FDA package insert warnings and contraindications, which are missing from the pack and block safety screening
- Detailed mechanism of action data (for example, from DrugBank), to confirm the mechanistic assessment
- Approved indication text for NDA214787, which is missing from the licensing data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

