---
layout: default
title: Letermovir
parent: Model Prediction Only (L5)
nav_order: 847
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Letermovir: From Cytomegalovirus (CMV) Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is a CMV-specific antiviral marketed in the US as PREVYMIS. The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but **0 clinical trials** and **0 publications** support this, and no credible mechanistic link has been identified. This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CMV infection (inferred from the drug's mechanism; the license records contain no indication text) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 license records (3 unique NDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record. The mechanistic review notes that letermovir inhibits the CMV viral terminase complex (pUL56/UL89/UL51). This blocks cleavage and packaging of viral DNA.

Candida species are fungi and have no homologous terminase target, so direct antifungal activity is not expected. The very high TxGNN score reflects a graph-based model output only. It cannot be verified against the available data, because the original MOA and indications are missing from the record.

Any plausible link would have to be indirect, for example through altered host immune or mucosal status. No data provided here supports such a link. At this stage the prediction is best treated as a hypothesis with weak biological grounding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 209939 | PREVYMIS (Merck Sharp & Dohme LLC) | Film-coated tablet | Not provided in record |
| NDA 209940 | PREVYMIS (Merck Sharp & Dohme LLC) | Solution for injection | Not provided in record |
| NDA 219104 | PREVYMIS (Merck Sharp & Dohme LLC) | Pellet | Not provided in record |

Available routes are oral (tablet), injectable (solution) and other (pellet). Duplicate license entries have been merged.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no supporting trials or publications, and the drug's known mechanism (CMV-specific terminase inhibition) does not apply to fungal pathogens. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Mechanism-of-action data from DrugBank, and original indication text from the license records
- Any in vitro evidence of anti-Candida activity or an indirect host-mediated mechanism
- A route-compatibility assessment, since vulvovaginal candidiasis is typically treated topically or orally
- A literature and trial search to confirm that no supporting evidence exists

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

