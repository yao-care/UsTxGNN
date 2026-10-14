---
layout: default
title: Alglucosidase Alfa
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase Alfa: From Glycogen Storage Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is a recombinant enzyme originally used for glycogen storage disease (Pompe disease, acid alpha-glucosidase deficiency).
The TxGNN model predicts it may be effective for **adult polyglucosan body disease**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glycogen storage disease (Pompe disease) |
| Predicted New Indication | Adult polyglucosan body disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 (BLA licenses, both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alglucosidase alfa is a recombinant acid alpha-glucosidase that breaks down glycogen inside lysosomes. Its efficacy is established in Pompe disease, a lysosomal glycogen storage disorder.

Adult polyglucosan body disease is caused by deficiency of the glycogen branching enzyme (GBE1). This leads to accumulation of poorly branched polyglucosan in neurons and other tissues. The only link is shared glycogen metabolism, which likely explains the high model score.

The rationale is weak for three reasons:
- The pathology is cytosolic polyglucosan accumulation, not lysosomal glycogen storage.
- The enzyme does not correct GBE1 deficiency.
- Enzyme replacement therapy penetrates the central nervous system poorly, which limits relevance for a neurological disease.

Other top-ranked predictions have similarly weak support:
- **Glycogen branching enzyme deficiency forms (congenital neuromuscular and fatal perinatal; score 99.32% each):** the link is only the shared glycogen storage disease class, and the drug does not replace branching enzyme.
- **Eyelid and ocular congenital conditions (congenital entropion, congenital ectropion, epiblepharon, congenital Horner syndrome, ptosis-strabismus-ectopic pupils syndrome) and related rare syndromes (ptosis-vocal cord paralysis syndrome, camptodactyly-myopia-medial rectus fibrosis syndrome):** no plausible mechanistic connection was identified, and these predictions appear to be graph-based artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125291 | Lumizyme (Genzyme Corporation) | Injection, powder, for solution | Not available (status: cancelled) |
| BLA761194 | Nexviazyme (Genzyme Corporation) | Injection, powder, lyophilized, for solution | Not available (status: cancelled) |

Both licenses are listed as cancelled in the data compiled for this report, and the dosage forms are injectable only.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found, and no knowledge-graph contraindications were listed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and the mechanism is weak: the enzyme targets lysosomal acid alpha-glucosidase, not GBE1 deficiency, and it has limited CNS penetration. The US market status (both licenses cancelled) and the lack of safety label data add further uncertainty.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence (for example, cell or animal models) showing a benefit on polyglucosan accumulation
- Evidence on CNS delivery of the enzyme
- Verification of current US regulatory status
- Assessment of route compatibility (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

