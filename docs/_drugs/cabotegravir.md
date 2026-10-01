---
layout: default
title: Cabotegravir
parent: Model Prediction Only (L5)
nav_order: 483
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor. It is marketed in the US as an oral film-coated tablet (Vocabria), and the provided data do not list its approved indication text.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction is a model output only, so it should be treated as a hypothesis, not a lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (from general pharmacology: HIV-1 infection) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. From general pharmacology, cabotegravir is an HIV-1 integrase strand transfer inhibitor, an antiviral that blocks viral DNA integration into the host genome. It has no known immunomodulatory activity relevant to rheumatoid arthritis.

No established link exists between the original use and the predicted one. Rheumatoid arthritis is a chronic autoimmune joint disease, and nothing in the data connects integrase inhibition to its inflammatory pathways. The high score (0.995) reflects a knowledge-graph pattern, not biological or clinical evidence, and should not be read as a sign of efficacy.

The other top-ranked predictions have the same weakness. They are sclerosing cholangitis (99.22%), bronchitis (99.19%), colobomatous microphthalmia-rhizomelic dysplasia syndrome (99.16%) and severe nonproliferative diabetic retinopathy (99.03%). All are L5 with no trials or literature and no plausible mechanistic link. The rare developmental disorder in particular is likely a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 212887 | Vocabria (ViiV Healthcare Company) | Tablet, film coated (oral) | Not listed in the provided data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials or publications, no plausible mechanistic link, and route compatibility has not been assessed. Blocking safety information is also missing.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication), which is required before any safety screening
- Mechanism of action data from DrugBank
- A mechanistic rationale connecting integrase inhibition to rheumatoid arthritis, or preclinical evidence supporting it
- A literature and trial search for cabotegravir in rheumatoid arthritis, to confirm that no evidence exists
- An assessment of route compatibility (oral and long-acting formulations against the needs of the predicted indication)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

