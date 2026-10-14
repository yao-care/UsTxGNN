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

# Cidofovir: From an Antiviral Indication to Sclerosing Cholangitis

## One-Sentence Summary

Cidofovir is an injectable antiviral nucleotide analog. The US licence records compiled for this report do not state its approved indication text.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The prediction is a model output only, and the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available US licence records |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 2 (both ANDA, both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cidofovir is known as a nucleotide analog with activity against DNA viruses, but this report cannot verify the mechanism from the compiled data.

No direct link between cidofovir and sclerosing cholangitis is evident. Sclerosing cholangitis is an immune-mediated or cholestatic disease. A possible indirect link is secondary sclerosing cholangitis associated with infection, such as CMV or other viral cholangiopathy in immunocompromised patients, but this is speculative.

The very high TxGNN score (99.94%) is a model prediction only. It likely reflects knowledge-graph relationships rather than demonstrated biology or clinical benefit. Cidofovir's known nephrotoxicity is also a concern in this population.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

Other predictions for this drug were also reviewed:
- **Rheumatoid arthritis** (score 99.82%): the five retrieved publications do not show cidofovir efficacy. They concern leflunomide for CMV infection after transplant (cidofovir appears only as a comparator or background therapy), retinal drug toxicity, and warts. The match comes from leflunomide being an RA drug, not from evidence for cidofovir.
- **Colobomatous microphthalmia-rhizomelic dysplasia syndrome** (99.62%) and **brachydactyly-syndactyly syndrome** (99.49%): both are rare congenital genetic conditions with no trials, no literature, and no plausible mechanistic rationale.

All four predictions are at evidence level L5 with a Hold recommendation.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202501 | Cidofovir Dihydrate (Heritage Pharmaceuticals / Avet Pharmaceuticals) | Injection, solution | Not stated (licence cancelled) |
| ANDA201276 | Cidofovir (Mylan Institutional) | Injection, solution | Not stated (licence cancelled) |

## Safety Considerations

- **Predicted disease contraindications (knowledge graph, not label text)**: kidney disease, pyoureter, acidosis disorder, acquired lactic acidosis.
- **Drug Interactions**: 55 interactions were identified. Most of those listed are Major, and many involve other nephrotoxic or renally cleared agents:
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Polymyxin B and vancomycin
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Deferasirox and deferoxamine
  - Iodinated contrast and radiopharmaceuticals: diatrizoate, iodipamide, iobenguane (I-131)
  - Moderate interactions: exenatide and trospium

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no supporting literature, and no clear mechanistic link. Cidofovir's nephrotoxicity and the many major interactions with nephrotoxic drugs add further concern, and no US licences are currently valid.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Mechanism of action data
- Any preclinical or clinical evidence linking cidofovir to sclerosing cholangitis, for example viral cholangiopathy in immunocompromised patients
- A renal safety assessment for the target population
- Confirmation of the original approved indication and the current availability of the product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

