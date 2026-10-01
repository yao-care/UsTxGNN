---
layout: default
title: Cidofovir
parent: Model Prediction Only (L5)
nav_order: 529
evidence_level: L5
indication_count: 4
---

# Cidofovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cidofovir: From Antiviral Therapy to Sclerosing Cholangitis

## One-Sentence Summary

Cidofovir is an injectable antiviral nucleotide analog that inhibits viral DNA polymerase, and it is currently marketed in the US as generic injection products.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but **0 clinical trials** and **0 publications** support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this record. Based on known information, cidofovir is a nucleotide analog that inhibits viral DNA polymerase, so its established role is antiviral. Mechanistically, it could only be applicable to sclerosing cholangitis through a speculative hypothesis of a viral or CMV-associated cholangiopathy.

No published or registered evidence supports this hypothesis. Sclerosing cholangitis is generally considered a chronic, immune-mediated or fibro-inflammatory bile duct disease, and nothing supplied here links viral DNA polymerase inhibition to its pathophysiology. The very high TxGNN score (0.999) should therefore be read as a knowledge-graph association, not as clinical or mechanistic validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Two generic injection products are authorized. Approved indication text was not provided for either.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA202501 | Cidofovir Dihydrate | Injection, solution | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. |
| ANDA201276 | Cidofovir | Injection, solution | Mylan Institutional LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model score. There are no clinical trials, no supporting literature, and no identifiable mechanistic link between an antiviral DNA polymerase inhibitor and sclerosing cholangitis. The other top predictions (rheumatoid arthritis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome) are also L5 and unsupported. The literature retrieved for rheumatoid arthritis concerned leflunomide for CMV, not cidofovir for RA.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening), obtained from the FDA label
- Mechanism of action data from DrugBank
- A defined biological hypothesis, such as a viral etiology in a specific sclerosing cholangitis subtype, supported by preclinical or mechanistic evidence
- A route and dosing feasibility assessment. Cidofovir is available only as an injection, and its suitability for a chronic biliary indication is unassessed.
- A literature search targeted at cidofovir and cholangiopathy to test whether any evidence exists

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

