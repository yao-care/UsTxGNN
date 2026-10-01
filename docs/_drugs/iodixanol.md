---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 804
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Iodixanol: From Iodinated Contrast Agent to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is an iodinated, non-ionic contrast agent used in diagnostic imaging, and it is marketed in the US as an injectable solution.
The TxGNN model predicts it may be relevant to **Osteoarthritis Susceptibility**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available US license records (Iodixanol is an iodinated contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (2 unique: NDA020351 and ANDA214271) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is an iodinated, non-ionic contrast agent. It has no known disease-modifying pharmacology, so no mechanistic link to osteoarthritis susceptibility can be identified.

"Susceptibility" describes a genetic-risk phenotype rather than a clinical condition that can be treated. The high score (99.16%) most likely reflects a co-occurrence signal in the knowledge graph, not a therapeutic relationship.

Iodixanol does appear in osteoarthritis research, but as a **diagnostic and experimental probe**. For example, it is used as a CT contrast agent to study solute diffusion through cartilage. That is a different use from treating the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for osteoarthritis susceptibility.

For the closely related prediction **osteoarthritis** (score 99.07%), 7 papers were retrieved, but they do not support a treatment effect:

- They use iodinated contrast agents as imaging or diffusion probes. Examples are cartilage solute transport (PMID [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/), [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/)) and photon-counting CT (PMID [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/)).
- One in vitro study found that iodine contrast agents did not affect platelet-rich plasma function (PMID [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/)).
- All are preclinical, computational or ex vivo studies, with no clinical efficacy data.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020351 | Visipaque | Injection, solution | GE Healthcare Inc. |
| ANDA214271 | Iodixanol | Injection, solution | Fresenius Kabi USA, LLC |

The source data lists each of these two licenses twice, which accounts for the 4 records. Approved indication text is not available in the records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the literature covers only diagnostic or experimental use, and there is no plausible therapeutic mechanism. "Osteoarthritis susceptibility" is also not a treatable clinical indication.

**To proceed, the following is needed:**
- Mechanism of action data for iodixanol (DrugBank)
- The US package insert, including warnings and contraindications, so that safety screening can begin
- Clarification of whether the intended use is therapeutic or diagnostic (for example, cartilage imaging in osteoarthritis). A diagnostic use would need a different evaluation path.
- Any preclinical or clinical evidence of a therapeutic effect in osteoarthritis. None currently exists.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

