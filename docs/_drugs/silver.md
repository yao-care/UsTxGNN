---
layout: default
title: Silver
parent: Model Prediction Only (L5)
nav_order: 1162
evidence_level: L5
indication_count: 1
---

# Silver
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

# Silver: From No Labeled Indication to Bone Paget Disease

## One-Sentence Summary

Silver is marketed in the US mainly as colloidal, wound-wash and homeopathic products, and the data record no approved indication for it.
The TxGNN model predicts it may be effective for **bone Paget disease**, but this is a model output only. The **2 clinical trials** and **5 publications** found have no therapeutic link between silver and Paget disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data |
| Predicted New Indication | bone Paget disease |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the drug record lists no original indications. Silver has no established treatment role in the data, so there is no proven efficacy in an original indication to extend to Paget disease.

The high score (0.997) most likely comes from the knowledge graph rather than from biology. The literature linking silver and Paget's disease of bone is about silver as a laboratory staining reagent. Examples are AgNOR staining of osteoclast nuclei and silver impregnation of bone sections. No mechanism such as osteoclast inhibition or bone-turnover modulation has been shown for silver. The prediction is therefore best read as a likely artifact of laboratory usage, not a real repurposing signal.

## Clinical Trial Evidence

Neither registered trial tests silver or a silver-containing product, and both were graded C (not relevant).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01793168](https://clinicaltrials.gov/study/NCT01793168) | N/A | Recruiting | 20000 | CoRDS rare-disease patient registry (Sanford Research). It does not test silver, so it gives no efficacy or safety evidence. |
| [NCT03573089](https://clinicaltrials.gov/study/NCT03573089) | N/A | Recruiting | 3600 | Trial of intensive vs. standard serum phosphate lowering in dialysis patients with end-stage kidney disease. It is unrelated to silver or Paget disease. |

## Literature Evidence

All five publications are laboratory or histology papers. None is a clinical study of silver as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9836854](https://pubmed.ncbi.nlm.nih.gov/9836854/) | 1998 | Laboratory/histopathology | Bone | Silver-stained nucleolar organizer regions (AgNORs) are increased in osteoclast nuclei of Paget's bone disease. Silver is used only as a stain. |
| [3163726](https://pubmed.ncbi.nlm.nih.gov/3163726/) | 1988 | Laboratory/imaging | J Nucl Med | Gallium-67 citrate localizes to osteoclast nuclei in Paget's disease. Silver is not the subject. |
| [4111887](https://pubmed.ncbi.nlm.nih.gov/4111887/) | 1972 | Histological methods | Stain Technology | Silver staining of bone before decalcification to measure osteoid in sections. |
| [2420233](https://pubmed.ncbi.nlm.nih.gov/2420233/) | 1985 | Histological methods | Anatomischer Anzeiger | Silver nitrate impregnation method for bone tissue. |
| [9227338](https://pubmed.ncbi.nlm.nih.gov/9227338/) | 1997 | Laboratory methods | J Pathol | Limitations of in situ RT-PCR for quantifying vitamin D receptor mRNA in kidney and bone sections. Silver is not the subject. |

## US Market Information

The listed authorization numbers are not available, and the approved indication text is empty for all five products below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Colloidal Silver (BioActive Nutritional, Inc.) | Liquid | Not stated |
| Not listed | Sovereign Silver Homeopathic Wound Wash (Natural Immunogenics Corp.) | Liquid | Not stated |
| Not listed | Argentum Nitricum (Hahnemann Laboratories, Inc.) | Pellet | Not stated |
| Not listed | Argentum Iodatum (Hahnemann Laboratories, Inc.) | Pellet | Not stated |
| Not listed | Argentum Muriaticum (OHM Pharma Inc.) | Pellet | Not stated |

## Safety Considerations

- **Drug Interactions**: No interactions were found in DrugBank for this entry.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a knowledge-graph score alone (Evidence Level L5). Neither registered trial tests silver, and the literature concerns silver only as a staining reagent. There is no supported therapeutic mechanism and no clear original indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed silver products
- Mechanism of action data (MOA) from DrugBank
- Any preclinical or clinical study that directly tests a silver compound in Paget disease or bone-turnover models
- Confirmation of whether the TxGNN link is an artifact of the laboratory literature, for example by checking the knowledge-graph edges behind the score
- A route and formulation assessment. The available forms (liquid, pellet, gel, spray, ointment) are not obviously suited to systemic bone disease.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

