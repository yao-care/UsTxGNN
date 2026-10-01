---
layout: default
title: Elosulfase Alfa
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Elosulfase Alfa: From Morquio A Syndrome to Scheie Syndrome

## One-Sentence Summary

Elosulfase alfa (VIMIZIM) is an enzyme replacement therapy, recombinant GALNS, used for Morquio A syndrome (MPS IVA).
The TxGNN model predicts it may be effective for **Scheie syndrome** (attenuated MPS I), but there are **0 clinical trials** and only **2 general MPS cohort publications**, and none of the evidence tests the drug in this disease.
The high score most likely reflects the two diseases' shared MPS class in the knowledge graph rather than a real drug-disease link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Morquio A syndrome (MPS IVA); the US license text is blank in the source data, so this is taken from the literature and mechanism notes |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% (model rank 3363) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125460) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Elosulfase alfa is a recombinant N-acetylgalactosamine-6-sulfatase (GALNS). It degrades **keratan sulfate** and **chondroitin-6-sulfate**, which build up in Morquio A syndrome.

Scheie syndrome is a different disease. It is the attenuated form of MPS I, caused by IDUA (alpha-L-iduronidase) deficiency, and it accumulates **dermatan sulfate and heparan sulfate**. Elosulfase alfa does not act on these substrates, so **there is no substrate overlap** and no direct mechanistic rationale.

The prediction therefore looks like a graph-proximity artifact: both diseases are mucopolysaccharidoses, and the model likely links them through that shared class. No clinical data support the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Cohort | Human Mutation | Molecular characterization of 302 Iranian MPS patients (289 families) using NGS panel and Sanger sequencing. A diagnostic and genetic study with no treatment data. |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Cohort | Pathologie-Biologie | Clinical features and consanguinity in MPS I and MPS IVA patients in Tunisia. Descriptive only, with no evaluation of elosulfase alfa. |

Both papers are general MPS epidemiology or genetics studies. Neither tests elosulfase alfa in Scheie syndrome.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125460 | VIMIZIM | Injection, solution, concentrate (injectable) | BioMarin Pharmaceutical Inc. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Elosulfase alfa cleaves different substrates (keratan sulfate and chondroitin-6-sulfate) from those that accumulate in Scheie syndrome (dermatan and heparan sulfate). There are no trials and no supporting literature, so this is an L5 model-only prediction with a likely graph artifact behind the score.

**To proceed, the following is needed:**
- Preclinical evidence, such as in vitro or animal data, that GALNS can affect dermatan or heparan sulfate turnover. Absent that, the mechanism argues against pursuing this indication.
- Package insert safety data (warnings and contraindications), which are currently missing.
- Detailed mechanism of action data from DrugBank.

**Note on other predictions:** The rank 2 prediction, "lysosomal storage disease with skeletal involvement," includes Morquio A syndrome. That is elosulfase alfa's own approved use, so it is on-label rather than repurposing. Evidence there supports Morquio A only and should not be extended to other skeletal lysosomal storage diseases without disease-specific data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

