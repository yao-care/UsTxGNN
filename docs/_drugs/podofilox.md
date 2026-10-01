---
layout: default
title: Podofilox
parent: Model Prediction Only (L5)
nav_order: 1057
evidence_level: L5
indication_count: 10
---

# Podofilox
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

# Podofilox: From Genital Warts to Vulvovaginal Candidiasis

## One-Sentence Summary

Podofilox is a topical antimitotic agent, marketed in the US as a solution and a gel; its established use is external genital warts. The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but there are **0 clinical trials** and only **1 publication**, a general review of sexually transmitted diseases. The prediction is not supported by any clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | External genital warts (inferred from known topical use; the license records supplied contain no indication text) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both ANDA generic approvals) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Podofilox is known to be an antimitotic agent that binds tubulin. Its efficacy in external genital warts is established, but this mechanism has no known antifungal activity.

The link to vulvovaginal candidiasis is weak. The only supporting paper is a 1999 review of sexually transmitted disease treatment (vaginal infections, pelvic inflammatory disease and genital warts). The drug and the disease most likely co-occur in that article by chance. The very high TxGNN score (0.995) therefore looks like a co-mention artifact, not a real pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Review | American Family Physician | Overview of the 1998 CDC treatment recommendations for vaginal infections, pelvic inflammatory disease and genital warts. It gives no podofilox-specific evidence for candidiasis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075600 | Podofilox | Solution | Padagis US LLC |
| ANDA211871 | Podofilox | Gel (topical) | Padagis US LLC |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no plausible mechanism and only one non-specific review, so it is model output only (L5). Podofilox is an antimitotic agent, not an antifungal, and established antifungal therapies already exist for this condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any primary evidence of antifungal activity, which is currently absent
- Separate evaluation of the rank 3 prediction, **human papilloma virus infection** (L3, Proceed with Guardrails). It is most likely the established genital wart use rather than true repurposing. It is supported only by guidelines and reviews, so the underlying primary RCTs should be confirmed before the evidence grade is raised.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

