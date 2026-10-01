---
layout: default
title: Levofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 855
evidence_level: L4
indication_count: 10
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levofloxacin: From Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibacterial that is widely marketed in the United States. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but the evidence is weak: **0 clinical trials** and **1 publication**, an outbreak report that does not show levofloxacin efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the five listed are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Levofloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy against bacterial infections is established, so a benefit in an eye surface disease would depend on a bacterial component.

The prediction is weakly supported. The only linked paper describes an outbreak of **microsporidial** keratoconjunctivitis traced to swimming pool water in Taiwan. Microsporidia are fungi-related intracellular parasites, and fluoroquinolones are not established as active against them. If levofloxacin was used in that setting, it was probably to cover bacterial co-infection or as a non-specific anti-infective. No efficacy signal can be inferred. The very high score (0.999) most likely reflects proximity in the knowledge graph rather than a demonstrated therapeutic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | Am J Ophthalmol | Outbreak of microsporidial keratoconjunctivitis linked to contaminated swimming pool water in Taiwan. It does not show levofloxacin efficacy. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077652 | levofloxacin | Tablet, film coated | Coupler LLC |
| ANDA202801 | Levofloxacin | Tablet, film coated | A-S Medication Solutions |
| ANDA076710 | Levofloxacin | Tablet, film coated | Northwind Health Company, LLC |
| ANDA076710 | Levofloxacin | Tablet, film coated | REMEDYREPACK INC. |
| ANDA076710 | Levofloxacin | Tablet, film coated | Dr. Reddy's Laboratories Limited |

Available forms across all licenses: oral tablets, injection solution, and solution.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials. The single paper is an outbreak report of a microsporidial infection, which is not a setting where fluoroquinolones are known to work. This supports a model-only prediction at the L4 level.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap)
- Mechanism of action data from DrugBank
- Studies showing levofloxacin activity or benefit in punctate epithelial keratoconjunctivitis, including the causative pathogens and any ophthalmic formulation or route
- Confirmation of the original approved indication, since all listed licenses have empty indication text

**Other candidates in the same Evidence Pack with stronger support:**
- **Monoclonal gammopathy (rank 7, L1, Proceed with Guardrails):** the double-blind, placebo-controlled Phase 3 TEAMM trial ([PMID 31668592](https://pubmed.ncbi.nlm.nih.gov/31668592/)) tested levofloxacin prophylaxis in newly diagnosed symptomatic myeloma. The benefit is infection prevention, not treatment of the plasma-cell disease, and it does not extend directly to MGUS.
- **Septicemic plague (rank 9, L4, Proceed with Guardrails):** African green monkey studies ([PMID 21347450](https://pubmed.ncbi.nlm.nih.gov/21347450/)) support activity against *Yersinia pestis*. This is probably already an on-label indication, so the label status should be verified.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

