---
layout: default
title: Parathyroid Hormone
parent: Model Prediction Only (L5)
nav_order: 1015
evidence_level: L5
indication_count: 10
---

# Parathyroid Hormone
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

# Parathyroid Hormone: From Its Approved Use to Migraine Disorder

## One-Sentence Summary

Parathyroid hormone (marketed in the US as NATPARA, BLA125511) is an approved injectable hormone product, but the Evidence Pack does not include its approved indication text.
The TxGNN model predicts it may be relevant to **migraine disorder**, but the support is thin: **1 registered trial** (unrelated to PTH) and **1 genetic association study** suggesting a possible link through PTH-related peptide receptors.
No study has tested PTH as a migraine treatment.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (mechanistic and genetic signal only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 records (all the same BLA125511) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. PTH is a peptide hormone that acts through the PTH receptor and regulates calcium and bone metabolism. The Evidence Pack does not confirm the original indication, so the link between it and migraine cannot be assessed directly.

The only mechanistic hint is a 2025 genetic association study (Brain Communications) linking variants in **PTH-related peptide (PTHrP) receptors** to migraine susceptibility. This is a hypothesis-level signal. It is not evidence that giving PTH would help. It is unclear whether receptor agonism would relieve or worsen migraine.

The other retrieved papers are indirect. They concern vitamin D, magnesium and calcium homeostasis in migraine, not PTH treatment. The high TxGNN score is a knowledge-graph prediction only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07028684](https://clinicaltrials.gov/study/NCT07028684) | N/A | Completed | 22 | Foot reflexology massage for pain, sleep and quality of life in women with migraine. Non-drug study that does not involve PTH (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40297711](https://pubmed.ncbi.nlm.nih.gov/40297711/) | 2025 | Genetic association study | Brain Communications | PTHrP receptor variants are proposed as genetic drivers of migraine susceptibility. This is the only direct mechanistic signal. |
| [31261815](https://pubmed.ncbi.nlm.nih.gov/31261815/) | 2019 | Cohort | Medicina (Kaunas) | Vitamin D levels and response to vitamin D therapy in childhood migraine. Indirect, not PTH. |
| [24714817](https://pubmed.ncbi.nlm.nih.gov/24714817/) | 2014 | Clinical study | Braz J Med Biol Res | Vitamin D added to amitriptyline in 53 children with migraine. Not PTH. |
| [29429076](https://pubmed.ncbi.nlm.nih.gov/29429076/) | 2018 | Review | Neuromolecular Medicine | Autonomic dysfunction, bone homeostasis and neurodegeneration in multiple sclerosis. Only peripherally relevant. |
| [11425281](https://pubmed.ncbi.nlm.nih.gov/11425281/) | 2001 | Review | Medical Hypotheses | Magnesium deficiency and its wide-ranging effects. Indirect. |
| [3739765](https://pubmed.ncbi.nlm.nih.gov/3739765/) | 1986 | Preclinical/Review | Acta Neurologica | Central effects of calcitonin and parathormone. Old, no abstract, no migraine treatment data. |

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA125511 | NATPARA (parathyroid hormone), Takeda Pharmaceuticals America, Inc. | Lyophilized powder for injection |

The pack lists four identical BLA125511 records, shown here once. None includes approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

One literature signal is worth noting: a 2016 case report (PMID 26992073) described worsening of calcinosis cutis in two osteoporotic patients with systemic autoimmune disease after teriparatide, a PTH analogue. It is a potential safety signal, not evidence of benefit.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single genetic association paper and a knowledge-graph score. No trial or study tests PTH in migraine, and the direction of effect is unknown. The other nine predicted indications are also L4 or L5, and all are Hold.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication text and mechanism of action data (DrugBank)
- Functional or preclinical evidence on whether PTH1R/PTHrP agonism helps or worsens migraine
- Clinical review of whether an injectable hormone with calcium-related risks is plausible for a chronic, non-life-threatening condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

