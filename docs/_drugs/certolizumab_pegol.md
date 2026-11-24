---
layout: default
title: Certolizumab Pegol
parent: Model Prediction Only (L5)
nav_order: 514
evidence_level: L5
indication_count: 3
monitor_inn: "CERTOLIZUMAB PEGOL"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-11-24
description: "Certolizumab Pegol: predicted new indication Hypermobility of coccyx (evidence level L5). In the US: 1 FDA application (1 active)"
---

# Certolizumab Pegol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Certolizumab Pegol: PEGylated anti-TNF-alpha antibody fragment → Hypermobility of coccyx
{: .text-alpha }

## One-Sentence Summary

Certolizumab pegol is a PEGylated antigen-binding fragment of a recombinant human antibody that neutralizes tumour necrosis factor alpha (TNF-α), and it is marketed in the US as an injectable biologic.
The TxGNN model predicts it may be useful for **hypermobility of coccyx**, with a score of 0.9975.
**No clinical trials and no publications** directly support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypermobility of coccyx |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 1) |
| Number of FDA Applications | 1 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for certolizumab pegol: "Certolizumab pegol binds to human TNFα with a KD of 90pM. TNFα is a key pro-inflammatory cytokine with a central role in inflammatory processes. Certolizumab pegol selectively neutralizes TNFα (IC 90 of 4 ng/mL for inhibition of human TNFα in the in vitro L929 murine fibrosarcoma cytotoxicity assay) but does not neutralize lymphotoxin α (TNFβ)." ([DailyMed: Cimzia (certolizumab pegol) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4c2c9dc-a0bb-4d64-a667-a67ebe88392d), label version 2026-10-29; accessed 2026-11-19.) Certolizumab pegol is known to bind and neutralize TNF-α, a driver of inflammation in several immune-mediated joint and spinal diseases.

Hypermobility of coccyx is a mechanical or structural condition of the tailbone, not a TNF-driven inflammatory disease. No plausible TNF-mediated mechanism links the drug to it. The high model score (0.9975) is probably a statistical artifact of the model associating the drug with spine-related terms rather than a sign of a real therapeutic link. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| BLA125160 | CIMZIA | UCB INC | Injectable; injection | Valid |

<!-- licenses:end -->

The product is an injectable (subcutaneous-type) formulation only. The local licence record does not include approved indication text.

## Safety Considerations

- **Drug Interactions**: The interaction search completed and returned 100 interacting drugs in total. The main ones listed in the data are:
  - **Major**:
    - Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone (including the ophthalmic form).
    - Deferiprone.
    - Radiopharmaceuticals: ibritumomab tiuxetan, iobenguane (I-131), tositumomab (I-131).
  - **Moderate**: metronidazole, tinidazole, rosuvastatin, simvastatin, pegvaliase.
  - **Minor**: zinc acetate, zinc gluconate, zinc sulfate.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it. There are no trials or publications on this condition, and no plausible TNF-mediated mechanism. Evidence level is L5.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence that TNF-α inhibition affects coccyx hypermobility or related pathology
- Mechanism of action data to support a biological rationale
- Package insert warnings and contraindications for a safety review
- Expert clinical review to judge whether the prediction is meaningful or a model artifact

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cimzia (certolizumab pegol) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4c2c9dc-a0bb-4d64-a667-a67ebe88392d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

