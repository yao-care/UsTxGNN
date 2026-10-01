---
layout: default
title: Ixekizumab
parent: Model Prediction Only (L5)
nav_order: 823
evidence_level: L5
indication_count: 10
---

# Ixekizumab
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

# Ixekizumab: From Psoriasis and Spondyloarthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab is an IL-17A-blocking monoclonal antibody, marketed as TALTZ and used for psoriasis, psoriatic arthritis and axial spondyloarthritis.
The TxGNN model predicts it may be effective for **rheumatoid vasculitis**, but **no ixekizumab-specific trial or publication** supports this yet.
The one linked trial studies perioperative immunosuppressant management, not ixekizumab efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis, psoriatic arthritis, ankylosing spondylitis / axial spondyloarthritis (taken from the literature and trial data; the approved-indication text was not supplied in the license records) |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 (all listings under BLA125521) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available. Ixekizumab is a selective IL-17A antagonist. IL-17A drives inflammation in psoriasis, psoriatic arthritis and axial spondyloarthritis, and Phase 3 trials have confirmed efficacy in those diseases.

IL-17A has also been implicated in autoimmune vasculitis, so a link to rheumatoid vasculitis is plausible in principle. However, no ixekizumab-specific efficacy data exist for this condition. The high score (0.975) is a graph-based prediction and should not be read as clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Compares shorter vs longer preoperative immunosuppressant holds in rheumatology patients having shoulder arthroplasty. It does not test ixekizumab for rheumatoid vasculitis, so it provides no efficacy evidence (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125521 (4 listings) | TALTZ (Eli Lilly and Company) | Injection, solution | Indication text not included in the supplied records |

## Safety Considerations

The pack contains no package-insert warnings or contraindications, and the drug-interaction query returned no results. Please refer to the package insert for safety information.

Class-level cautions from the literature attached to other predicted indications:
- **Inflammatory bowel disease**: IL-17 blockers can trigger new-onset or worsening IBD (PMID 32719044).
- **Infections and vaccination**: check infection and vaccination status before and during therapy (PMID 38331098).
- **Immunosuppression**: a theoretical concern in any additional immune-mediated or malignant setting.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trial or publication tests ixekizumab in rheumatoid vasculitis, and the single linked trial is unrelated to efficacy.

**Other predicted indications:**
- **Inflammatory spondylopathy and vertebral disease** (ranks 6 and 9) have L1 evidence and are rated "Proceed with Guardrails". This comes from multiple completed Phase 3 RCTs in psoriatic arthritis and axial spondyloarthritis (for example COAST-V, COAST-X, SPIRIT-P1 and SPIRIT-P2). These correspond to already-labeled uses, so they are on-label confirmation, not novel repurposing.
- **Haematologic malignancies** (ALL and CLL/SLL), **coccyx hypermobility**, **Kummell disease** and **gingival fibromatosis** have no supporting evidence and no plausible IL-17A mechanism.
- **Polyarticular juvenile rheumatoid arthritis** is plausible in principle but has no linked trial or publication.

**To proceed, the following is needed:**
- Any preclinical, case-series or trial evidence of IL-17A blockade in rheumatoid vasculitis
- Approved-indication text and package-insert warnings and contraindications (label data are missing from the pack)
- DrugBank mechanism-of-action data
- Correction of the empty original-indication field so on-label uses are not mistaken for new repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

