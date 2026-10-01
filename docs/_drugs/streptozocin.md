---
layout: default
title: Streptozocin
parent: Model Prediction Only (L5)
nav_order: 1183
evidence_level: L5
indication_count: 10
---

# Streptozocin
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

# Streptozocin: From Pancreatic Neuroendocrine Tumors to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Streptozocin is a nitrosourea alkylating agent used as chemotherapy for pancreatic neuroendocrine tumors.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but there are **0 clinical trials** and **1 publication** (a preclinical animal study that does not test streptozocin as a treatment).
The prediction rests on model output alone and has no credible mechanistic support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic neuroendocrine tumors (the US license record has no indication text; this comes from the evidence rationale) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, streptozocin is a nitrosourea alkylating agent that is selectively toxic to pancreatic beta cells, and its efficacy in pancreatic neuroendocrine tumors is the basis of its approval.

The evidence does not support a mechanistic link to multiple sclerosis. Streptozocin's beta-cell toxicity is why it is used to induce diabetes in animal models, and it is also nephrotoxic. Nothing in its known pharmacology points to a role in an autoimmune demyelinating disease.

The high TxGNN score is most likely a knowledge-graph artifact. The only retrieved paper mentions streptozotocin because it was used to induce diabetes in rats, and it discusses fingolimod, an approved MS drug, as the treatment being tested. The apparent link between streptozocin and MS comes from that co-mention, not from a therapeutic relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28162947](https://pubmed.ncbi.nlm.nih.gov/28162947/) | 2017 | Preclinical (animal model) | J Sex Med | Fingolimod (FTY720) partially improved erectile dysfunction in rats with streptozotocin-induced type 1 diabetes. Streptozotocin served only as a diabetes-induction tool, not as a treatment, so the paper gives no support for streptozocin in MS. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA (number not specified in the data) | Zanosar (ESTEVE PHARMACEUTICALS, S.A.) | Powder, for solution | Not listed in the available data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Renal function is essential given known nephrotoxicity. For other parameters, refer to the package insert. |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Streptozocin is known to be nephrotoxic. For all other safety information, including warnings, contraindications, and drug interactions, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no credible mechanistic link, and the only retrieved paper uses streptozotocin as a research tool rather than a therapy. Streptozocin's cytotoxic and nephrotoxic profile makes it an unlikely fit for a chronic autoimmune disease with many approved treatments. Of the other predictions in this pack, only small cell lung carcinoma has meaningful literature, and it shows streptozocin to be ineffective.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for a safety screen
- Detailed mechanism of action data (MOA)
- Any evidence linking streptozocin to MS pathophysiology, since none currently exists
- A review of other predicted indications with stronger biological plausibility for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

