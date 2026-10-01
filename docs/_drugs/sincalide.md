---
layout: default
title: Sincalide
parent: Model Prediction Only (L5)
nav_order: 1164
evidence_level: L5
indication_count: 10
---

# Sincalide
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

# Sincalide: From Diagnostic Gallbladder and Pancreatic Testing to Malignant Catarrh

## One-Sentence Summary

Sincalide is a synthetic cholecystokinin (CCK-8) analog used as a diagnostic agent to stimulate gallbladder contraction and pancreatic secretion.
The TxGNN model predicts it may be effective for **malignant catarrh**, a veterinary viral disease of cattle, with **0 clinical trials** and **0 publications** supporting this direction.
This looks like a knowledge-graph artifact rather than a real repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US licence data (diagnostic use for gallbladder contraction and pancreatic secretion, per the mechanistic assessment) |
| Predicted New Indication | Malignant catarrh |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 licence entries (2 distinct NDA numbers: NDA017697, NDA210850) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, sincalide is a CCK-8 analog. It acts on CCK receptors to stimulate gallbladder smooth-muscle contraction and pancreatic secretion, and it is used diagnostically rather than therapeutically.

**The prediction is not reasonable on current evidence.**
- Malignant catarrh is a veterinary viral disease with no known connection to CCK receptor pharmacology.
- No trials or publications support the link.
- The high score most likely reflects the graph structure, not biology.

The same pattern appears across the other nine top predictions:

| Predicted indication | Score | Evidence | Assessment |
|------|------|------|------|
| Infectious bovine rhinotracheitis | 99.96% | L5 | Bovine herpesvirus disease, no mechanistic link |
| Cytomegalovirus infection | 99.96% | L5 | The only retrieved paper (PMID 11484914) is a rat pancreatic acinar study, a keyword mismatch |
| Thrombotic disease | 99.94% | L5 | No known antithrombotic mechanism |
| Hyperthyroidism | 99.93% | L4 | Indirect rodent studies only; no therapeutic effect shown |
| Resistance to thyroid hormone (THR-beta mutation) | 99.92% | L5 | No known connection |
| Hyperthyroxinemia | 99.88% | L5 | Speculative |
| Homozygous familial hypercholesterolemia | 99.85% | L5 | No effect on LDL receptor function |
| Prinzmetal angina | 99.84% | L5 | No established mechanism |
| Amenorrhea | 99.83% | L5 | No link to the reproductive axis |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017697 | KINEVAC (Bracco Diagnostics) | Lyophilized powder for injection | Not provided in source data |
| NDA017697 | SINCALIDE (Fresenius Kabi USA) | Lyophilized powder for injection | Not provided in source data |
| NDA210850 | Sincalide (Fosun Pharma USA) | Lyophilized powder for injection | Not provided in source data |
| NDA210850 | Sincalide (MAIA Pharmaceuticals) | Lyophilized powder for injection | Not provided in source data |

All products are injectable only.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting literature, and no plausible mechanism links a CCK-8 analog to a bovine viral disease. It should not be pursued as a human repurposing candidate.

**To proceed, the following is needed:**
- Confirm whether the target disease mapping is valid for humans, since malignant catarrh is a veterinary condition.
- Retrieve the FDA package insert (warnings and contraindications), which currently blocks safety screening.
- Obtain mechanism of action data from DrugBank.
- Consider re-screening the other top predictions (for example hyperthyroidism, the only one with any indirect literature) only if new human data emerge.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

