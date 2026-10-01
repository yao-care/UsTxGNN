---
layout: default
title: Abacavir
parent: Moderate Evidence (L3-L4)
nav_order: 36
evidence_level: L4
indication_count: 3
---

# Abacavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Abacavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) used in human HIV-1 therapy. The TxGNN model predicts it may be effective against **simian immunodeficiency virus (SIV) infection**, but the only supporting evidence is **1 in vitro publication** and **0 clinical trials**. SIV is a non-human primate infection, so this prediction is mainly relevant to HIV research models rather than human treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from the abacavir/lamivudine HIV-1 trials in the evidence pack; the US license records carry no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 (the sampled listings are ANDA generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, abacavir is an NRTI, and its efficacy in HIV-1 is well established. SIV is a lentivirus whose reverse transcriptase is closely related to that of HIV, so NRTI activity against it is mechanistically plausible.

The prediction most likely reflects the close biological similarity between HIV and SIV rather than a genuinely new therapeutic signal. The only supporting study is an in vitro comparison of antiviral susceptibility, and it does not show clinical benefit. Because SIV infects non-human primates, it is mainly useful as an animal model for HIV research, not as a human repurposing target.

The same model run also returned two other predictions. Feline acquired immunodeficiency syndrome (score 99.79%) is likewise an animal-model indication. The evidence for it consists of human HIV-1 trials and one preclinical FIV study, so it is indirect evidence at best. A rare neurodevelopmental disorder (score 99.78%) has no trials or literature and no evident mechanistic link to an NRTI, so it may be a knowledge-graph artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Tested 16 approved anti-HIV drugs and the experimental compound AMD3100 against HIV-2, SIV (mac251, B670) and SHIV strains. The goal was to inform treatment and post-exposure prophylaxis. The available abstract is truncated, so the abacavir-specific result is not confirmed. |

---

## US Market Information

The source records contain no approved-indication text, so that column is omitted. Only 5 of the 15 licenses were supplied. Several generic ANDA applications are held by multiple labelers.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091560 | Abacavir | Tablet | Coupler LLC |
| ANDA091294 | Abacavir Sulfate | Tablet, film coated | Mylan Pharmaceuticals Inc. |
| ANDA077844 | Abacavir | Tablet, film coated | Aurobindo Pharma Limited |
| ANDA091560 | Abacavir | Tablet | XLCare Pharmaceuticals Inc. |
| ANDA091560 | Abacavir | Tablet | AvPAK |

Available dosage forms include oral tablets, film-coated tablets and a solution.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence is one 2004 in vitro susceptibility study (L4), and no clinical trials exist for this indication. SIV is a non-human primate infection with little relevance as a human repurposing target. The high TxGNN score most likely reflects the HIV/SIV similarity, not a new therapeutic opportunity.

**To proceed, the following is needed:**
- The full text of PMID 15040537, to confirm the abacavir-specific susceptibility data
- A decision on whether an animal-model use (SIV/SHIV research) counts as in scope, since no human indication is being pursued
- Package insert warnings and contraindications, because safety data is missing and blocks safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- A check of the underlying knowledge-graph path for the neurodevelopmental disorder prediction, to rule out an artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

