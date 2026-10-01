---
layout: default
title: Iloprost
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Iloprost: From an Unspecified Original Indication to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Iloprost is a prostacyclin (IP receptor) agonist marketed in the US as an injection (AURLUMYN), but the record lists no approved indication text.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a monogenic hair disorder.
This prediction has **no clinical trials and no publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the record |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Iloprost is a prostacyclin analog that acts as an IP receptor agonist. Prostacyclin analogs cause vasodilation and inhibit platelet aggregation. Other prostaglandin analogs are known to affect hair growth, which is the only plausible link to a hair indication.

Hypotrichosis simplex of the scalp is a monogenic hair disorder. A vasodilator mechanism is unlikely to correct a genetic defect, and no data support a hair-growth benefit from iloprost. The high score (99.45%) probably reflects shared hair-phenotype neighbors in the knowledge graph rather than a real pharmacological relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA217933 | AURLUMYN (BTG International Inc) | Injection, solution | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is model output only (L5), with no trials or literature. The mechanism is implausible for a monogenic hair disorder, and the FDA label warnings and contraindications are missing from the record.

Lower-ranked predictions in the same pack have more support, so they may be better candidates to pursue:
- **PAH associated with congenital heart disease** (L3, Proceed with Guardrails): one N/A-phase trial (NCT01383083, n=42) plus adult and pediatric cohort studies.
- **PAH associated with connective tissue disease** (L3, Proceed with Guardrails): observational data, including long-term domiciliary IV iloprost outcomes (PMID 27651181).
- **PAH associated with HIV infection** (L3, Research Question): NCT00709956 is a completed Phase 3 randomized placebo-controlled trial, but its drug and population are not verifiable from the truncated title.

Because the record lists no original indications, PAH may already be a labeled use. If so, these would not be true repurposing.

**To proceed, the following is needed:**
- The FDA package insert (approved indication, warnings, contraindications), which currently blocks safety screening
- Mechanism of action data from DrugBank
- Verification of the intervention and population in NCT00709956
- Any genetic or preclinical rationale for iloprost in hypotrichosis, before further work on this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

