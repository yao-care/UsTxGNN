---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 1083
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is an antiseizure drug marketed in the US as oral tablets. The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but **no clinical trials and no publications** support this prediction. It is a model output only and most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data (primidone is a known antiseizure drug) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Primidone is an established antiseizure drug, and its efficacy in seizure disorders is well known. However, it has no known antineoplastic mechanism, so nothing links it mechanistically to a tumour of the trigeminal nerve.

The very high TxGNN score is probably a propagation artifact. The graph likely connects primidone to this disease through shared neurological or cranial-nerve nodes, not through a real therapeutic relationship. No independent mechanistic evidence was found to support the prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA040862 | Primidone | Tablet | Dr. Reddy's Laboratories Limited |
| ANDA040866 | Primidone | Tablet | Bryant Ranch Prepack |
| ANDA214896 | Primidone | Tablet | Advagen Pharma Limited |
| ANDA040866 | Primidone | Tablet | NCS HealthCare of KY, LLC dba Vangard Labs |
| ANDA040866 | Primidone | Tablet | AvPAK |

The approved indication text was not provided in the license data. Only oral tablets are marketed.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were returned. Primidone is partly metabolized to phenobarbital and is an enzyme inducer, so interaction screening is needed before any further development.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature, and no plausible antineoplastic mechanism. It is Evidence Level L5, model prediction only, and the high score is most likely a graph artifact.

**Other predicted indications in this pack:**
- **Trigeminal neuralgia** (rank 9, L4, Research Question): A preclinical link exists through TRPM3, but no primidone trial was found.
- **Micturition-induced seizures** and **audiogenic seizures** (ranks 4 and 7, L4, Research Question): Only indirect evidence exists, including general antiseizure reviews and animal screening studies.
- **Startle epilepsy, orgasm-induced seizures, thinking seizures, eating seizures, reading seizures** (L4 to L5, Hold): The evidence is a single case report, tangential studies, or none.
- **Beta-ketothiolase deficiency** (rank 10, L5, Hold): There is no evidence and no mechanistic basis.

**To proceed, the following is needed:**
- Original indications and the mechanism of action (MOA) from the US package insert and DrugBank
- Package insert warnings and contraindications, since the safety data are incomplete
- Confirmation that the drug interaction count of 0 is a data gap, since primidone induces enzymes
- For a more credible candidate such as trigeminal neuralgia, a targeted literature and trial search for primidone and TRPM3 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

