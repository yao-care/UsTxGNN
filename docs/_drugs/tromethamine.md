---
layout: default
title: Tromethamine
parent: Model Prediction Only (L5)
nav_order: 1268
evidence_level: L5
indication_count: 10
---

# Tromethamine
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

# Tromethamine: From Buffer/Alkalinizing Agent to Allergic Urticaria

## One-Sentence Summary

Tromethamine is a buffer/alkalinizing agent. It is also widely used as the salt counterion in other drugs, such as fosfomycin tromethamine and ketorolac tromethamine.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **0 clinical trials** and **1 publication** are linked to this prediction. That publication is an adverse-event case report, not evidence of benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US label data provided |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only; the evidence pack labels it L4, but the only literature is an adverse-event case report) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tromethamine is a buffer/alkalinizing agent and a common excipient or counterion. It is marketed alone (THAM injection) and as the salt form of fosfomycin.

No therapeutic mechanism links tromethamine to allergic urticaria. The only literature is a case report of a biphasic anaphylactic reaction to **ketorolac tromethamine**, where tromethamine is only the counterion of an NSAID. That is an adverse-event signal, not a benefit signal.

The very high TxGNN score (0.999) is most likely a graph-proximity artifact. The model may be picking up the many drugs that share the tromethamine name or salt form. The prediction should be treated as a hypothesis with no supporting rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

Trials linked to other predicted indications, such as "post-bacterial disorder", are mostly fosfomycin trometamol studies in urinary tract infection. Their antibacterial effect comes from fosfomycin, not from tromethamine. Several others are vaccine or unrelated studies matched by name. None supports the allergic urticaria prediction.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16831313](https://pubmed.ncbi.nlm.nih.gov/16831313/) | 2006 | Case report | Int J Immunopathol Pharmacol | Biphasic anaphylactic reaction to injectable ketorolac tromethamine (an NSAID). This is a harm signal and does not show therapeutic benefit. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217608 | Fosfomycin tromethamine (Aurobindo Pharma) | Granule, for solution | Not stated in the data |
| ANDA214554 | Fosfomycin Tromethamine (A-S Medication Solutions) | Granule, for solution | Not stated in the data |
| NDA013025 | THAM (Hospira) | Injection, solution | Not stated in the data |
| ANDA211881 | Fosfomycin Tromethamine (Cipla USA) | Granule, for solution | Not stated in the data |
| ANDA212548 | Fosfomycin Tromethamine (Xiromed) | Powder | Not stated in the data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score alone, with no trials and no mechanism. The single linked publication describes an allergic-type adverse reaction, which points the opposite way from a therapeutic effect.

**To proceed, the following is needed:**
- US package insert data: approved indications, warnings and contraindications
- Mechanism of action data, and a plausible biological link between tromethamine and allergic urticaria
- Evidence that any effect comes from tromethamine itself rather than from a partner active ingredient (for example fosfomycin)
- Any preclinical or clinical signal for allergic urticaria. Without one, the candidate should not advance beyond the screening stage (S0).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

