---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 1043
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is an anticonvulsant sodium channel blocker. The license records in the pack do not list an indication, so "epilepsy" here comes from general drug knowledge.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and **5 publications** for this prediction, and none of the publications is about a neoplasm.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure control (general knowledge; not stated in the license records) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Phenytoin is a use-dependent voltage-gated sodium channel blocker that suppresses seizure spread. Its efficacy in seizure disorders is established, but the pack gives no direct route from that mechanism to tumor treatment.

The high score most likely comes from the drug's closeness to **trigeminal neuralgia** in the knowledge graph, not from any antitumor effect. The retrieved literature covers trigeminal neuralgia, Sturge-Weber syndrome, and nerve fiber physiology, not neoplasm. Sodium channel blockade might relieve tumor-related neuropathic pain, but it offers no antitumor rationale.

**Note:** The same drug has a much better-supported neighboring prediction, **trigeminal neuralgia** (rank 9, score 99.97%, Evidence Level L3). It is backed by one small prospective study (NCT03712254, n=15, IV phenytoin for acute exacerbations) and retrospective series. A 2017 review notes the evidence is weak compared with carbamazepine. That indication is a more realistic direction than the neoplasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia. It concerns neuralgia, not neoplasm. |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Review | J Assoc Physicians India | Sturge-Weber syndrome (facial vascular malformation with seizures). It is not a neoplasm study. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 Sturge-Weber cases, with clinical course and treatment response. |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Cohort | Birth Defects Orig Artic Ser | Skin disorders in institutionalized people with intellectual disability, including drug-therapy effects. Not relevant to neoplasm. |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Preclinical | Trans Am Neurol Assoc | Trigeminal root fiber size and pain conduction. No abstract in the pack. |

## US Market Information

The license records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA213834 | Phenytoin Sodium | Capsule, extended release | Unichem Pharmaceuticals (USA), Inc. |
| ANDA040684 | Phenytoin Sodium | Capsule, extended release | Golden State Medical Supply, Inc. |
| ANDA084307 | Phenytoin Sodium | Injection | Henry Schein, Inc. |
| ANDA084349 | DILANTIN | Capsule, extended release | REMEDYREPACK INC. |
| ANDA084307 | Phenytoin Sodium | Injection | ProPharma Distribution |

Other marketed forms include chewable tablet, capsule, and suspension.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no neoplasm-specific literature (Evidence Level L5), and it has no antitumor mechanistic basis. The score most likely reflects proximity to trigeminal neuralgia in the knowledge graph.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence that phenytoin acts on trigeminal nerve tumors, as opposed to tumor-related pain
- Consider redirecting the evaluation to **trigeminal neuralgia**, which has L3 evidence and a "Proceed with Guardrails" recommendation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

