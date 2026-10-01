---
layout: default
title: Tivozanib
parent: Model Prediction Only (L5)
nav_order: 1235
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: From Advanced Renal Cell Carcinoma to Endocervical Carcinoma

## One-Sentence Summary

Tivozanib is an oral kinase inhibitor marketed in the US as FOTIVDA. The US license records in the Evidence Pack do not list an approved indication, so the original indication above comes from general pharmacology knowledge (VEGFR-targeted therapy for advanced renal cell carcinoma), not from the pack.
The TxGNN model predicts it may be effective for **endocervical carcinoma**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the US license data (general knowledge: advanced renal cell carcinoma) |
| Predicted New Indication | Endocervical carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license records (both under NDA212904) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, tivozanib is a VEGFR-1/2/3 tyrosine kinase inhibitor. It blocks VEGF signaling, which tumors use to build new blood vessels.

Anti-angiogenic therapy is already clinically relevant in cervical cancer. The VEGF-targeted antibody bevacizumab is an established option. That makes a VEGFR-inhibiting small molecule a plausible candidate, but the link is indirect. No supplied data show that tivozanib itself works in cervical carcinoma.

The TxGNN score is very high (99.81%). Its top 10 predictions are all rare cervical or uterine ligament carcinoma variants, such as adenoid cystic, mucinous, glassy cell and signet ring subtypes. This pattern suggests the model is propagating from parent "cervical cancer" nodes in the knowledge graph. It probably does not reflect histology-specific evidence. The score should be read as a hypothesis-generating signal, not as proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212904 | FOTIVDA (AVEO Pharmaceuticals, Inc.) | Capsule (oral) | Not listed in the license record |

The pack contains two identical license records for this NDA. They are shown here as one entry.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert and institutional handling policies for oral antineoplastic agents |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found for this drug in the pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a TxGNN score, with no clinical trials and no literature (Evidence Level L5). The package insert safety data is also missing. This blocks progression to safety screening. The anti-angiogenic rationale is plausible for cervical cancer, but it is indirect and unverified for these rare histologic subtypes.

**To proceed, the following is needed:**
- Download and parse the FDA package insert to obtain warnings, contraindications and the approved indication
- Obtain mechanism of action data from DrugBank (DB11800)
- Search ClinicalTrials.gov and ICTRP for tivozanib or VEGFR-TKI studies in cervical and gynecologic carcinoma
- Search PubMed for preclinical or clinical evidence in cervical cancer
- Consider re-scoring against broader "cervical carcinoma" terms, since the rare-subtype predictions probably inherit from parent nodes
- Assess route compatibility (oral capsule) against the requirements of the target indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

