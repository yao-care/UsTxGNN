---
layout: default
title: Tranylcypromine
parent: Model Prediction Only (L5)
nav_order: 1249
evidence_level: L5
indication_count: 10
---

# Tranylcypromine
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

# Tranylcypromine: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Tranylcypromine is an irreversible monoamine oxidase inhibitor (MAOI) antidepressant, and the US label data supplied here lists no indication text. The TxGNN model ranks **benign paroxysmal torticollis of infancy** as its top predicted new indication, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** behind it. No credible mechanistic link was found, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (inferred from the literature; the US license records contain no indication text) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (2 NDAs and 3 ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tranylcypromine is known from the literature as an irreversible, non-selective MAO-A/B inhibitor that raises monoamine levels, and its efficacy in depression is established.

This prediction is not well supported mechanistically. Benign paroxysmal torticollis of infancy is linked to CACNA1A channelopathy and is related to migraine variants. Nothing connects MAO inhibition to this pathway, so the high score reflects graph proximity rather than biology.

There is also a practical barrier. Tranylcypromine carries risks of hypertensive crisis and dietary tyramine reactions, which make it unsuitable for infants.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA012342 | PARNATE (Advanz Pharma) | Tablet, film coated | Not provided in source data |
| ANDA213503 | Tranylcypromine (Solco Healthcare) | Tablet | Not provided in source data |
| ANDA206856 | Tranylcypromine (Novitium Pharma) | Tablet | Not provided in source data |
| ANDA040640 | Tranylcypromine Sulfate (Strides Pharma) | Tablet, film coated | Not provided in source data |
| NDA012342 | Tranylcypromine Sulfate (Actavis Pharma) | Tablet, film coated | Not provided in source data |

All products are oral tablets.

---

## Safety Considerations

- **Key risks for this candidate**: Hypertensive crisis and dietary tyramine reactions make the drug unsuitable for infants.
- **Class-level concerns**: The literature on other candidates adds serotonin syndrome, drug interactions, and withdrawal or discontinuation effects.

Please refer to the package insert for full warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or publications and no plausible mechanism. The drug is also a poor fit for infants because of its safety profile.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking MAO inhibition to CACNA1A-related episodic disorders
- A pediatric safety assessment, including tyramine and hypertensive-crisis risk
- Package insert warnings and contraindications, and mechanism of action data

**Other candidates in the same prediction list (for context):**

| Rank | Predicted Indication | Evidence Level | Recommendation | Note |
|------|------|------|------|------|
| 3 | Dysthymic disorder | L4 | Research Question | Only class-level antidepressant meta-analysis |
| 4 | Agoraphobia | L4 | Research Question | One case report and older MAOI reviews; no controlled trials |
| 5 | Melancholia | L2 | Proceed with Guardrails | Essentially an on-label depression use |
| 6 | Neurotic depression | L1 | Proceed with Guardrails | Double-blind comparison with moclobemide plus a meta-analysis of controlled studies; no registered Phase 3 trial |
| 8 | Neurotic disorder | L4 | Research Question | Mostly historical (1960s–1990s) papers |
| 2, 7, 9, 10 | Ohdo syndrome and variants, Ohdo-type blepharophimosis syndrome, ligneous conjunctivitis, Keppen-Lubinsky syndrome | L5 | Hold | No credible link; Ohdo-type has only a speculative LSD1/epigenetic link |

Ranks 5 and 6 are depression subtypes, so they are closer to the original use than to true repurposing. If a candidate is to be taken forward, they are the strongest, provided guardrails are enforced:
- Reserve use for treatment-resistant cases.
- Screen for dietary and drug interactions.
- Monitor blood pressure.
- Watch for cardiovascular effects when combined with esketamine.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

