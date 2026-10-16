---
layout: default
title: Allopurinol
parent: Moderate Evidence (L3-L4)
nav_order: 225
evidence_level: L4
indication_count: 10
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-14
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L4). Approved use: Gout"
---

# Allopurinol
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

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol was originally used to treat gout, hyperuricemia and acute urate nephropathy.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are currently **0 clinical trials** and only **2 indirect publications** (a hypothesis paper and a rat study), and neither shows that allopurinol treats the condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout (also hyperuricemia and acute urate nephropathy, per the knowledge graph) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 14 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Allopurinol is generally known as a xanthine oxidase inhibitor that lowers uric acid, and its efficacy in gout is well established. That mechanism has no obvious link to porphyria.

The only mechanistic connection comes from older preclinical work suggesting allopurinol can affect hepatic heme metabolism (degradation of cytochrome P450 heme and perturbation of ALA synthase regulation). This effect is generally associated with **precipitating or exacerbating** porphyria rather than treating it. The retrieved literature is a hypothesis paper on targeting 5-aminolevulinate synthase and a rat study of carbamazepine, so support is indirect. The high TxGNN score reflects a knowledge-graph association and is not clinical evidence. The direction of effect may even be harmful, which needs to be clarified before any further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes metabolic targeting of liver 5-ALAS (via tryptophan or inhibition of heme utilisation by tryptophan 2,3-dioxygenase) as a therapy for acute hepatic porphyrias; does not study allopurinol directly |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (animal) | Biochemical Pharmacology | Acute carbamazepine administration altered haem metabolism in rat liver, relevant to how drugs exacerbate hepatic porphyrias; not about allopurinol |

## US Market Information

All 14 US authorizations are listed as cancelled; none are currently valid. Approved indication text is not available. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016084 | Allopurinol (Rising Pharma Holdings) | Tablet | Not available |
| NDA018877 | Allopurinol (Bryant Ranch Prepack) | Tablet | Not available |
| NDA020298 | Aloprim (Mylan Institutional) | Lyophilized powder for injection | Not available |
| ANDA212363 | Allopurinol (Gland Pharma) | Lyophilized powder for injection | Not available |
| ANDA210117 | Allopurinol (Zydus Lifesciences) | Tablet | Not available |

## Safety Considerations

- **Knowledge-graph contraindication associations** (from drug-disease edges, not label text): liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis, and anti-glomerular basement membrane disease. The liver disease association is particularly relevant to a hepatic indication.
- **Drug Interactions**: 100 interactions were found in total. Moderate-level interactions include aluminum hydroxide, attapulgite, kaolin, magaldrate and sucralfate. Minor-level interactions include amoxicillin and chlorpropamide. Many others (e.g., metformin, omeprazole, pantoprazole, glimepiride, morphine) have an unclassified severity level.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and indirect preclinical or hypothesis literature, with no clinical trials. Existing mechanistic evidence suggests allopurinol may worsen rather than treat porphyria, and the knowledge graph flags liver disease as a contraindication. The other nine predicted indications (e.g., hepatoportal sclerosis, hepatopulmonary syndrome, immune-mediated necrotizing myopathy) have no trials or literature, and the phenylalanine metabolism disorder literature is off-target.

**To proceed, the following is needed:**
- Direct evidence on whether allopurinol exacerbates or improves hepatic porphyria (preclinical and case reports)
- Mechanism of action data
- FDA package insert warnings and contraindications, to complete safety screening
- Confirmation of current US marketing status, since all listed licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

