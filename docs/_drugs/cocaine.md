---
layout: default
title: Cocaine
parent: Model Prediction Only (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine: From Topical Local Anesthesia to Cauda Equina Syndrome

## One-Sentence Summary

Cocaine hydrochloride is marketed in the US as a nasal topical solution (Numbrino, Goprelto), which is a local anesthetic use.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but this is a graph-based prediction only, with **0 clinical trials** and **1 publication** (a case report unrelated to cocaine).

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 product listings under 2 unique NDAs (NDA209575, NDA209963) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Cocaine is known as a local anesthetic that blocks sodium channels, and it also inhibits monoamine reuptake. The US labeled indication text was not provided in the data. The marketed products are topical nasal solutions.

The predicted disease is different in kind. Cauda equina syndrome is a compressive neurological emergency, typically caused by lumbosacral disc pathology. It presents with urinary retention, fecal incontinence, saddle anesthesia and leg weakness. Treatment is urgent surgical decompression. Cocaine's local anesthetic and sodium-channel blocking activity does not address this compression.

**We found no plausible mechanistic link.** The high score (0.9998) reflects graph proximity in the knowledge graph, not pharmacological rationale. The prediction should not be treated as a therapeutic hypothesis without independent support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report | Surgical Neurology International | Distal cauda equina syndrome from lumbosacral disc pathology, with a literature review. It describes the disease and its diagnostic difficulty, and does not evaluate cocaine as a treatment. |

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA209575 | Cocaine hydrochloride nasal | Solution |
| NDA209575 | Numbrino | Solution |
| NDA209963 | Cocaine hydrochloride | Solution |
| NDA209963 | Goprelto | Solution |

All listed products are solutions. Manufacturers are Omnivium Pharmaceuticals LLC (NDA209575) and LXO US Inc. (NDA209963).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5). No trials exist, and the single retrieved article is an unrelated case report. There is no plausible mechanism for treating compressive cauda equina pathology. The other nine predicted indications are also rated Hold. For rhinitis and pharyngitis, the retrieved literature mostly documents cocaine-related tissue injury, which is a safety signal rather than therapeutic evidence.

**To proceed, the following is needed:**
- Mechanistic evidence for any effect of cocaine on cauda equina syndrome or its symptoms (for example, preclinical or nerve-block studies)
- FDA package insert warnings and contraindications (a blocking gap for safety screening), plus the approved indication text
- Mechanism of action data from DrugBank
- A clinical rationale showing that any proposed use adds value over standard surgical management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

