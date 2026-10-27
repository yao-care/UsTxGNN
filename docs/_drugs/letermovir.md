---
layout: default
title: Letermovir
parent: Model Prediction Only (L5)
nav_order: 847
evidence_level: L5
indication_count: 1
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
last_modified_at: 2026-10-14
description: "Letermovir: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Cytomegalovirus infection"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Letermovir: From Cytomegalovirus Infection to Vulvovaginal Candidiasis
{: .text-alpha }

## One-Sentence Summary

Letermovir is an antiviral originally used to treat **cytomegalovirus (CMV) infection**.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**,
but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cytomegalovirus infection |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, letermovir is a CMV-specific antiviral that inhibits the viral terminase complex (pUL56/pUL51/pUL89). This target has no known human or fungal counterpart.

Cytomegalovirus infection is a viral disease, while vulvovaginal candidiasis is a fungal infection. There is no clear mechanistic path from a viral terminase inhibitor to antifungal activity against *Candida* species. Any link would have to be indirect, for example through changes in host immunity or the vaginal microbiome, and nothing in the compiled data supports this.

The very high score (0.9988) is therefore best treated with caution. It may reflect a graph-based artifact, such as shared drug-interaction neighbours, or the co-occurrence of candidiasis with immunosuppressed transplant populations, which is the setting where letermovir is used.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA209939 | PREVYMIS | Tablet, film coated | Indication text not available (status: cancelled) |
| NDA219104 | PREVYMIS | Pellet | Indication text not available (status: cancelled) |
| NDA209940 | PREVYMIS | Injection, solution | Indication text not available (status: cancelled) |

All three authorizations (manufacturer: Merck Sharp & Dohme LLC) are listed as cancelled in the compiled data. This status should be verified against current FDA records before any planning.

## Safety Considerations

- **Drug Interactions**: An interaction query returned 100 records. The sample reviewed included mostly Moderate-level interactions, with several **Major** ones:
  - Eliglustat (Major)
  - Naloxegol (Major)
  - Cisapride (Major)
  - Moderate examples: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), omeprazole, lansoprazole, aprepitant, clarithromycin, and several antidiabetic drugs (pioglitazone, glimepiride, chlorpropamide, saxagliptin, acetohexamide).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it. There are no clinical trials or publications, and the known mechanism (inhibition of a CMV-specific viral terminase) gives no plausible route to antifungal activity. The evidence level is L5.

**To proceed, the following is needed:**
- Confirmation of the mechanism of action and any plausible link to *Candida* biology
- In vitro antifungal activity data against *Candida* species
- Package insert warnings and contraindications (not yet available), plus clarification of the cancelled US authorization status
- Assessment of route compatibility for a vaginal or other local formulation, since current dosage forms are oral, injectable, and pellet
- Review of the major drug interactions for the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

