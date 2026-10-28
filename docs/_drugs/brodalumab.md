---
layout: default
title: Brodalumab
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
monitor_inn: "BRODALUMAB"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "isolated optic neuritis", "optic perineuritis", "chronic relapsing inflammatory optic neuropathy", "recurrent idiopathic neuroretinitis", "episcleritis periodica fugax", "nodular episcleritis"]
last_modified_at: 2026-10-28
description: "Brodalumab: predicted new indication Strongyloidiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Brodalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Brodalumab: Strongyloidiasis
{: .text-alpha }

## One-Sentence Summary

Brodalumab is an injectable biologic that blocks the IL-17 receptor A (IL-17RA). The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **strongyloidiasis**, but **0 clinical trials** and **0 publications** support this prediction, and the biological rationale points the other way.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the drug's known class, brodalumab is an IL-17 receptor A inhibitor, and this is the basis for the analysis below.

The prediction is weakly supported at best. IL-17 signaling contributes to mucosal and anti-helminth immunity, so blocking it would be expected to impair host defence rather than help. Immunosuppressive biologics also raise concern about *Strongyloides* hyperinfection. The high TxGNN score (0.9984) therefore looks like a network-based artifact rather than a sign of true therapeutic potential. No clinical trials or literature back this indication.

For context, the other top predictions are also unsupported:

- **Eye disease (rank 2, 0.9982)**: the only prediction with any literature (3 papers, L4). It is too broad to act on, and the papers suggest possible safety signals rather than benefit.
- **Vitamin deficiency disorder, von Hippel anomaly**: no identifiable mechanistic link.
- **Optic neuritis-related conditions and episcleritis**: only a hypothetical link through Th17/IL-17 inflammation, with no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for strongyloidiasis.

For reference, the following papers were retrieved for the second-ranked prediction, eye disease. They are indirect and not evidence of efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | Preclinical/Animal study | Journal of Translational Medicine | IL-17 receptor blockade with brodalumab limited experimental periodontitis |
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | Case report | Rheumatology International | Behçet's disease developed as a paradoxical reaction after brodalumab initiation in a patient with chronic non-bacterial osteitis |
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | Pharmacovigilance analysis | Canadian Journal of Ophthalmology | Real-world analysis of FDA-approved systemic drugs disproportionately associated with reported uveitis |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761032 | Siliq (Bausch Health US LLC) | Injection | Not available (status: valid) |

## Safety Considerations

- **Disease contraindication signals (knowledge graph)**: Crohn disease, inflammatory bowel disease, and Crohn's colitis. These come from drug-disease contraindication links in the TxGNN knowledge graph, not from package insert text.
- **Drug Interactions**: 68 interactions were identified. Major interactions include:
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Bacillus Calmette-Guérin (live, Tice substrain)

  Moderate interactions include roflumilast, alefacept, alemtuzumab, anakinra, canakinumab, and several vaccines (tetanus toxoid, anthrax, adenovirus, cholera, *Candida albicans*). Zinc salts have Minor interactions. These mainly reflect additive immunosuppression and concerns about live vaccines.
- **Paradoxical inflammation**: A case report describes Behçet's disease arising after brodalumab initiation. A pharmacovigilance study has also examined uveitis from systemic drugs.
- **Infection risk**: Immunosuppression raises concern about *Strongyloides* hyperinfection, which is directly relevant to this predicted indication.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or literature, and the mechanism argues against benefit: IL-17 blockade could weaken anti-helminth defence and increase the risk of hyperinfection. The US license is cancelled, and the original indication and mechanism data are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication text
- A clear immunological rationale for IL-17RA blockade in strongyloidiasis, supported by preclinical data
- A review of the paradoxical inflammatory and ocular safety signals
- Consideration of other candidates from the prediction list that have a more plausible mechanism, such as immune-mediated ocular inflammation, once narrowed to a specific disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

