---
layout: default
title: Hyaluronidase
parent: Model Prediction Only (L5)
nav_order: 775
evidence_level: L5
indication_count: 10
---

# Hyaluronidase
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

# Hyaluronidase: From Drug-Dispersion Adjuvant to Esotropia

## One-Sentence Summary

Hyaluronidase is an enzyme marketed in the US in several injectable products, and its approved indication text was not supplied in the data.
The TxGNN model predicts it may be effective for **esotropia**, but there are **0 clinical trials** and only **1 publication** behind this prediction.
That publication is a case series on strabismus as a complication after cataract surgery, so it suggests an adverse-event association rather than a treatment effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (no therapeutic evidence; the only paper is a case series on a procedural complication) |
| US Market Status | ✓ Marketed |
| Number of Licenses | 16 (all listed as BLAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Hyaluronidase is generally known as an enzyme that breaks down hyaluronan. It is used to help other injected drugs spread and be absorbed, for example in anesthetic blocks and in subcutaneous products such as Darzalex Faspro and Hylenex. No approved indication text was supplied to compare against esotropia.

On the evidence supplied, the prediction is **not well supported**. The only linked paper (PMID 16934027) reports persistent diplopia and strabismus after cataract surgery under local anesthesia. Hyaluronidase is commonly added to such anesthetic blocks. This points to a possible procedural or adverse-event association, not a therapeutic benefit. No plausible mechanism was identified by which hyaluronidase would treat esotropia. The high TxGNN score is most likely an artifact of the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/) | 2006 | Case report/series | Binocular Vision & Strabismus Quarterly | Describes persistent diplopia and strabismus as a rare complication of local (retrobulbar) anesthesia for cataract surgery, and the treatments used. It does not test hyaluronidase as a treatment. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA021665 | AMPHADASE (Amphastar Pharmaceuticals) | Injection |
| BLA021640 | VITRASE (Bausch & Lomb) | Injection, solution |
| BLA021859 | HYALURONIDASE (HF Acquisition Co, DBA HealthFirst) | Injection, solution |
| BLA021859 | HYLENEX Recombinant (Antares Pharma) | Injection, solution |
| BLA761145 | Darzalex Faspro (Janssen Biotech) | Injection |

---

## Safety Considerations

- **Drug Interactions**: No interactions were found in the queried database.
- **Allergy**: A 2024 review (PMID 37145319) describes allergic complications of hyaluronidase injection, which is frequently misdiagnosed. It covers risk factors and management recommendations.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score and one case series describing a complication, with no trials and no therapeutic mechanism. The evidence does not support moving this indication forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications
- Mechanism of action data
- Any prospective clinical evidence of hyaluronidase treating esotropia (none is currently identified)

**Note on other candidates:** In the same prediction list, **diabetic retinopathy** (rank 6) has much stronger support. It has two completed Phase 3 trials of intravitreal Vitrase (NCT00198510, n=750; NCT00198497, n=510), but their results were not supplied. The target condition is likely vitreous hemorrhage rather than retinopathy progression. This candidate should be evaluated separately once the outcomes and regulatory status are verified.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

