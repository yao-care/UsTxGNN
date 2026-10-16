---
layout: default
title: Ipilimumab
parent: Model Prediction Only (L5)
nav_order: 808
evidence_level: L5
indication_count: 2
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia", "non-cutaneous melanoma"]
---

# Ipilimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Ipilimumab: From Metastatic Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab was originally used to treat metastatic melanoma.
The TxGNN model predicts it may be effective for **choroideremia**, an inherited retinal degeneration, but **no clinical trials and no publications** currently support this direction.
The prediction rests on a computational score alone, and the biology does not support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 (BLA125377) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Ipilimumab is an anti-CTLA-4 antibody. It releases the T-cell checkpoint brake and strengthens anti-tumour immunity, which is the basis of its efficacy in melanoma.

Choroideremia is an X-linked inherited retinal disease caused by loss of function of the *CHM* (REP1) gene. The retinal pigment epithelium, choroid and photoreceptors degenerate progressively. The disease is not driven by tumour immune evasion or by an immune-mediated process, so there is no plausible way for checkpoint blockade to act on it.

The very high TxGNN score (0.99) is a model output. It most likely reflects knowledge-graph topology rather than real biology. Systemic immune activation also carries a risk of immune-related adverse events, including uveitis. That would be undesirable in an already degenerating retina.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125377 | YERVOY (E.R. Squibb & Sons, L.L.C.) | Injection | Not specified; status: cancelled |

## Cytotoxicity

Ipilimumab is an antineoplastic immunotherapy. The descriptions below are general class-level information, not taken from the compiled data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (immune checkpoint inhibitor, anti-CTLA-4); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low as a direct effect; haematological immune-related events are possible |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, liver function, thyroid and other endocrine function, signs of colitis, skin and eye symptoms |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. The first 20 reviewed include:
  - **Major**: anticoagulants, including apixaban, betrixaban, bivalirudin, dalteparin, desirudin, edoxaban, argatroban and danaparoid.
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), metronidazole, tinidazole, naltrexone, and statins (rosuvastatin, simvastatin).
- **Disease-specific concern**: Immune-related adverse events, particularly uveitis, would be especially undesirable in choroideremia.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or published support (L5) and no credible mechanistic link. Choroideremia is a genetic, non-immune retinal degeneration, and ipilimumab's immune activation could harm the eye. The US licence is cancelled only.

**To proceed, the following is needed:**
- Any preclinical or mechanistic evidence linking CTLA-4 blockade to choroideremia pathology
- Detailed mechanism of action data and the full package insert safety information
- Assessment of ocular immune-related adverse event risk
- Confirmation of current US availability

**Note on another predicted indication:** The same data include a lower-ranked prediction, **non-cutaneous melanoma** (TxGNN score 99.02%), which is an extension within the melanoma family. It is supported by a completed Phase 2 trial of nivolumab plus ipilimumab in uveal melanoma (NCT02626962) and a clinical series (PMID 24999899), and carries an L1 grade with a "Proceed with Guardrails" recommendation. It deserves a separate evaluation and is a much stronger candidate than choroideremia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

