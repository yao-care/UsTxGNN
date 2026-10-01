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

# Alglucosidase Alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is a recombinant human acid alpha-glucosidase (GAA) enzyme replacement therapy, marketed in the US as Lumizyme and Nexviazyme and used for Pompe disease.
The TxGNN model predicts it may be effective for **adult polyglucosan body disease (APBD)**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pompe disease (acid alpha-glucosidase deficiency). The approved-indication text in the Evidence Pack is blank, so this comes from general knowledge of the products. |
| Predicted New Indication | Adult polyglucosan body disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both are BLAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Alglucosidase alfa is recombinant human GAA. It hydrolyzes glycogen inside lysosomes, and this is the basis of its use in Pompe disease.

APBD is caused by deficiency of the glycogen branching enzyme (GBE1). This produces poorly branched polyglucosan that accumulates mainly in the cytosol of neurons and glia. Both diseases involve abnormal glycogen handling, and this shared axis explains the high graph score.

The mechanistic fit is weak to moderate for three reasons:
- GAA works in the lysosome and does not restore branching enzyme activity.
- A large recombinant enzyme has limited CNS penetration, and APBD is predominantly neurological.
- No clinical data support the prediction.

The next two predictions (ranks 2–3) are the congenital and fatal perinatal neuromuscular forms of GBE1-deficiency glycogen storage disease (GSD IV). They have the same indirect link and no supporting evidence.

Ranks 4–10 are eyelid and ocular-motor conditions: congenital entropion, congenital ectropion, congenital Horner syndrome, ptosis-vocal cord paralysis syndrome, camptodactyly-myopia-medial rectus fibrosis, epiblepharon, and ptosis-strabismus-ectopic pupils syndrome. They probably reflect phenotype overlap (such as ptosis in Pompe disease) in the knowledge graph rather than a real therapeutic mechanism. All of these carry a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125291 | Lumizyme (Genzyme Corporation) | Injection, powder, for solution | Not listed in the source data |
| BLA761194 | Nexviazyme (Genzyme Corporation) | Injection, powder, lyophilized, for solution | Not listed in the source data |

Both products are injectable only. Route compatibility with the predicted indications has not been assessed.

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). The mechanism is only indirectly plausible, because lysosomal GAA does not correct the cytosolic branching-enzyme defect in APBD, and CNS delivery is a further barrier. The eyelid and ocular-motor predictions look like knowledge-graph artifacts.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence that GAA can reduce polyglucosan burden in neural tissue or in GBE1-deficient models
- An assessment of CNS penetration and route feasibility for a neurological indication
- A targeted literature search on GAA or enzyme replacement in GBE1-deficiency disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

