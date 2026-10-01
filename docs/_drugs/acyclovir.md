---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpesvirus Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is an antiviral nucleoside analogue. The Evidence Pack does not list its original indications, but it is generally used against herpesvirus infections.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**.
Currently **0 clinical trials** and **2 publications** are retrieved for this indication. Neither publication is about acyclovir, so the prediction is model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (approved indication text is empty) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% (rank 8,551) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (total US licences; the five listed below include one NDA and four ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Acyclovir is a herpesvirus antiviral. The Evidence Pack does not state its approved indications, but its antiviral role is well known, and any mechanistic argument has to start from that.

Acyclovir must be activated by a viral thymidine kinase, so it works only against viruses that encode one. Punctate epithelial keratitis has several causes:
- **Herpes simplex or varicella-zoster virus (HSV/VZV):** these viruses do encode the enzyme, so acyclovir is plausible.
- **Adenoviral or microsporidial infection:** acyclovir would not be expected to work.

The data do not say which cause the TxGNN score reflects. The high score is therefore a graph-proximity signal that needs an aetiology-specific check. It is not evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Review/Observational | Am J Ophthalmol | Two AIDS patients treated for opportunistic infections developed bilateral ocular surface changes suggestive of drug-induced corneal lipidosis. Acyclovir is not the subject. |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Characteristics of microsporidial keratoconjunctivitis in an eastern Indian cohort. Not an acyclovir study. |

## US Market Information

The Evidence Pack lists no approved indication text for any of these authorizations. Two of the five are valacyclovir (an acyclovir prodrug) generics, and one is the valacyclovir brand VALTREX.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA079012 | Valacyclovir Hydrochloride | Tablet |
| ANDA075382 | Acyclovir | Tablet |
| NDA020487 | VALTREX | Tablet, film coated |
| ANDA090682 | Valacyclovir Hydrochloride | Tablet, film coated |
| ANDA077135 | Valacyclovir hydrochloride | Tablet |

Other US dosage forms on record: injection solution, capsule, ointment, and cream.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, and neither retrieved paper concerns acyclovir. The score reflects model prediction only (L5). The indication also spans causes where acyclovir is plausible (HSV/VZV) and causes where it is not (adenovirus, microsporidia).

**To proceed, the following is needed:**
- Aetiology-specific evidence, such as acyclovir in HSV/VZV epithelial keratitis, separated from adenoviral or microsporidial cases
- Approved indications and package-insert safety data (currently data gaps)
- Mechanism of action data from DrugBank
- Ocular route compatibility (not yet assessed)

**Note:** Among the other predictions in this pack, "disease of orbital region" (rank 9) has the strongest support (L1, Proceed with Guardrails). It rests on herpetic eye disease trials and appears to reflect existing herpetic ophthalmic use rather than true repurposing. "Common wart" (rank 2) has L2 evidence from small intralesional trials. Both are better candidates to evaluate first.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

