---
layout: default
title: Alirocumab
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to X-linked Ichthyosis (Without Steroid Sulfatase Deficiency)

## One-Sentence Summary

Alirocumab is a PCSK9-inhibiting antibody marketed in the US as Praluent, used to lower LDL cholesterol.
The TxGNN model predicts it may be effective for **X-linked ichthyosis without steroid sulfatase deficiency**, but this is a model output only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia (based on the drug class; the approved indication text was not provided in the source data) |
| Predicted New Indication | Ichthyosis, X-linked, without steroid sulfatase deficiency |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 (all records share BLA125559) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Alirocumab is a monoclonal antibody that inhibits PCSK9. By blocking PCSK9, it increases LDL receptor recycling and lowers circulating LDL-C.

**No plausible mechanistic link to the predicted indication was identified.** X-linked ichthyosis is a skin disorder of epidermal cholesterol sulfate metabolism. It is not driven by LDL receptor recycling or circulating LDL-C, so PCSK9 inhibition has no obvious point of action. The high TxGNN score (0.994) reflects a pattern in the knowledge graph rather than biological or clinical support. Scores in this range were also given to many unrelated conditions in the same list, so the score alone should not be read as a strong signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125559 | Praluent (Sanofi-Aventis U.S. LLC) | Injection, solution | Not provided in the source data |
| BLA125559 | Praluent (Regeneron Pharmaceuticals, Inc.) | Injection, solution | Not provided in the source data |

The source data lists four records under the same BLA number (two per manufacturer). They are consolidated here by manufacturer.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications, and no plausible biological link between PCSK9 inhibition and X-linked ichthyosis.

**To proceed, the following is needed:**
- A mechanistic hypothesis connecting PCSK9 or LDL-C lowering to epidermal cholesterol sulfate metabolism
- The current US package insert (approved indications, warnings, contraindications)
- Preclinical or case-level evidence in X-linked ichthyosis

**Other predictions in the same run (for context only):**
- **Xanthomatosis (rank 3, L4, Research Question):** Biologically plausible, since xanthomas follow severe hypercholesterolemia. However, the two retrieved case reports do not show alirocumab-related xanthoma outcomes.
- **Cholesterol catabolic process disease (rank 5, tagged L1):** There is one completed Phase 3 trial (NCT03207945, EPIC-HIV, 118 participants) and several reviews. The trial population is HIV-specific and the primary endpoint is cardiovascular risk. The condition also overlaps with alirocumab's existing lipid-lowering use, so it may not be a true new indication. The L1 tag looks generous, given that L1 requires at least two completed Phase 3 RCTs, and it should be rechecked.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

