---
layout: default
title: Valine
parent: Model Prediction Only (L5)
nav_order: 1279
evidence_level: L5
indication_count: 10
---

# Valine
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

# Valine: From Nutritional Amino Acid Supplement to Sclerosing Cholangitis

## One-Sentence Summary

Valine is an essential branched-chain amino acid, and in the US it is marketed as liquid supplement products with no approved indication on record.
The TxGNN model predicts it may be relevant to **sclerosing cholangitis**, but there are **0 clinical trials** and only **2 publications**, both indirect (a metabolite cohort study and a Mendelian randomization study).
This is a model-generated research question, not clinically supported evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None listed (the US product records contain no approved indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 (indirect and mechanistic studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (license numbers not available in the records) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for valine is not currently available. Valine is a branched-chain amino acid (BCAA) involved in protein synthesis and energy metabolism, and the records list no approved indication for it.

The link to sclerosing cholangitis is indirect. Chronic cholestatic liver disease alters amino acid metabolism, including BCAAs and aromatic amino acids. A Mendelian randomization study connects circulating blood metabolites to the risk of cholestatic liver diseases, including primary sclerosing cholangitis (PSC). These findings show that metabolism changes in these diseases. They do not show that giving valine changes the disease course, and no study has tested valine supplementation in PSC.

The high TxGNN score (99.42%) reflects a knowledge-graph prediction, not clinical support. Other top-ranked predictions are weaker. The glaucoma and thyroid-related predictions rely mostly on literature hits where "valine" is only an amino acid residue in a mutated protein, and the other predictions have no literature at all.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined amino acid abnormalities and their relation to fatigue in primary biliary cirrhosis and PSC. The study focused on plasma tyrosine, not valine treatment. |
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian randomization | Frontiers in Medicine | Tested causal links between blood metabolites and the risk of primary biliary cholangitis and PSC. It supports a metabolic association only, not a therapeutic effect. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | L-Valine High | Liquid | Not available |
| Not available | L-Valine | Liquid | Not available |

Both products are made by Professional Complementary Health Formulas.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and two indirect papers, with no trials and no evidence that valine changes the course of sclerosing cholangitis. The rank-1 candidate is best treated as a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking data gap)
- Mechanism of action data from DrugBank
- Review of the full literature set to confirm that no direct evidence has been missed
- Preclinical or observational data on valine or BCAA supplementation in PSC
- Evaluation of the route and formulation, since the marketed products are liquid supplements with no recorded approved indication
- Safety review for patients with hepatic impairment, since PSC is a liver disease and the safety data are empty

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

