---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 990
evidence_level: L5
indication_count: 10
---

# Olsalazine
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

# Olsalazine: From Ulcerative Colitis to Myelodysplastic Syndrome

## One-Sentence Summary

Olsalazine is a prodrug of 5-aminosalicylic acid (5-ASA) that acts locally in the colon, and it is generally used for ulcerative colitis.
The TxGNN model predicts it may be effective for **myelodysplastic syndrome**, but this is a graph-based prediction only.
There are currently **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (olsalazine is generally used for ulcerative colitis) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Olsalazine is a dimer of 5-ASA that is poorly absorbed and acts mainly on the gut mucosa. Its anti-inflammatory effects are thought to involve NF-kB and COX/LOX modulation.

No established link connects this activity to myelodysplastic syndrome (MDS), a disorder of clonal hematopoiesis. The high score most likely reflects shared neighbors in the knowledge graph rather than biology. The same applies to the other top predictions, which fall into three groups:

- **MDS cluster:** unclassified MDS, refractory cytopenia of childhood, partial deletion of 5q, aregenerative anemia, and congenital sideroblastic anemia.
- **Hair disorders:** hypotrichosis simplex of the scalp, congenital hypotrichosis milia, alopecia, and diffuse alopecia areata.

Two of these have a speculative anti-inflammatory rationale, and none has supporting evidence:

- **Alopecia areata:** it is immune-mediated, but olsalazine is not known to act on the relevant pathways (JAK-STAT, IFN-gamma). Systemic exposure at the scalp is also unlikely.
- **Aregenerative anemia:** aminosalicylates are occasionally linked to cytopenias as adverse effects, so the safety direction may be opposite to the predicted benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA019715 | Dipentum | Capsule, gelatin coated (oral) | Viatris Specialty LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature, and no plausible mechanistic link. Olsalazine's local colonic action does not fit MDS, and aminosalicylate-associated cytopenias raise a possible safety concern in this population.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank) to test any link to MDS or immune-mediated hair loss
- Any preclinical or clinical signal for MDS or alopecia areata before re-evaluation
- Route and exposure assessment, since olsalazine is oral and colon-targeted, so systemic or scalp exposure is limited

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

