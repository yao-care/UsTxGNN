---
layout: default
title: Vestronidase Alfa
parent: Model Prediction Only (L5)
nav_order: 1289
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
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

# Vestronidase Alfa: From Mucopolysaccharidosis VII to Scheie Syndrome

## One-Sentence Summary

Vestronidase alfa (Mepsevii) is a recombinant human beta-glucuronidase enzyme replacement therapy, originally used for mucopolysaccharidosis VII (MPS VII, Sly syndrome).
The TxGNN model predicts it may be effective for **Scheie syndrome** (attenuated MPS I), but **0 clinical trials** and **0 publications** currently support this direction, and the mechanistic link is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis VII (Sly syndrome). The license record's indication text is blank, so this comes from the literature and the model's rationale notes. |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA761047) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Vestronidase alfa is a recombinant human beta-glucuronidase (GUS). It replaces the enzyme missing in MPS VII, so that glycosaminoglycans (GAGs) can be broken down.

Scheie syndrome is caused by a different enzyme deficiency, alpha-L-iduronidase (IDUA). The block sits at a different step of the GAG degradation pathway, and GUS cannot replace IDUA. The high score most likely reflects network proximity within the MPS/GAG pathway in the knowledge graph, not a shared enzymatic target. The prediction should therefore be treated as a hypothesis with limited biological support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761047 | MEPSEVII (Ultragenyx Pharmaceutical Inc.) | Injection | Not provided in the license record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. Scheie syndrome is an IDUA deficiency that GUS replacement cannot correct, and no trials or publications link vestronidase alfa to it. The other predicted indications (Hurler syndrome, Sanfilippo syndrome and several rare ocular or neuromuscular syndromes) are also unsupported. The only related trial is a multi-disorder prenatal ERT study, and the published papers all concern MPS VII.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A disease-specific enzyme-substrate rationale, or preclinical data, showing GUS could affect GAG accumulation in Scheie syndrome
- Confirmation of which enzyme each arm receives in the PEARL trial (NCT04532047) before treating it as relevant evidence for any MPS I-type disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

