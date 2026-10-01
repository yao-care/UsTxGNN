---
layout: default
title: Raxibacumab
parent: Model Prediction Only (L5)
nav_order: 1113
evidence_level: L5
indication_count: 8
---

# Raxibacumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Raxibacumab: From Anthrax to Postinfectious Vasculitis

## One-Sentence Summary

Raxibacumab is a monoclonal antibody that neutralizes the anthrax toxin, and it is marketed in the US as an injection.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but this is a graph-based prediction only.
There are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anthrax (the license record has no indication text; this is inferred from the drug's mechanism) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA125349) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. From the drug's known biology, raxibacumab binds the protective antigen (PA) of *Bacillus anthracis* and blocks anthrax toxin from entering cells. Its efficacy therefore depends on the presence of this specific toxin.

The predicted indication does not fit this mechanism. Postinfectious vasculitis is generally driven by immune complexes or autoimmune mechanisms after an infection. Anthrax PA toxin is not involved, so the antibody has no known target in this disease. The high TxGNN score (99.75%) reflects patterns in the knowledge graph, not biological or clinical support.

The same weakness applies to the other seven predictions in the candidate list, including post-infectious syndrome, otitis externa, Chagas cardiomyopathy and drug-induced osteoporosis. Only infection-related hemolytic uremic syndrome offers a conceptual parallel, since it also involves a bacterial toxin. Even there, raxibacumab does not neutralize Shiga toxin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

The only trials found in the pack sit under a different, vaguer prediction ("post-bacterial disorder"). They study anthrax itself (vaccine interaction and observational use), so they do not support postinfectious vasculitis.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125349 | Raxibacumab (Emergent Manufacturing Operations Baltimore LLC) | Injection | Not listed in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There is no trial or literature support, and there is no plausible mechanistic link between an anti-anthrax-PA antibody and postinfectious vasculitis.

**To proceed, the following is needed:**
- A defensible mechanistic hypothesis, or preclinical data, showing a role for PA toxin or its pathway in postinfectious vasculitis
- The FDA package insert, including approved indication, warnings and contraindications, to allow safety screening
- A literature search targeting raxibacumab (or anti-PA antibodies) in vasculitis
- A specific disease definition and clinical rationale before any further assessment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

