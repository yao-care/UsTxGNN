---
layout: default
title: Flunisolide
parent: Moderate Evidence (L3-L4)
nav_order: 717
evidence_level: L4
indication_count: 10
---

# Flunisolide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Flunisolide: From Inhaled Corticosteroid to Atopic Eczema

## One-Sentence Summary

Flunisolide is a synthetic glucocorticoid marketed in the US as an inhaled or intranasal solution, and the supplied data do not include its approved indication text.
The TxGNN model predicts it may be effective for **atopic eczema**, but there are **0 registered clinical trials** and only **1 publication**, a biomarker cohort study that does not test flunisolide as a treatment for the skin disease.
The prediction is therefore best treated as a research question, not an evidence-backed candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Atopic eczema (also listed as "dermatitis, atopic", a duplicate entry) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 (all ANDA generic approvals) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Flunisolide is a synthetic glucocorticoid, and corticosteroids as a class suppress type 2 and other inflammatory cytokine signaling. Corticosteroids are an established drug class for atopic dermatitis, so the link is plausible at the class level.

There is an important caveat. Flunisolide is marketed as an inhaled or intranasal formulation, whereas atopic eczema is normally treated with topical corticosteroids applied to the skin. The very high TxGNN score (99.98%) most likely reflects class-level proximity in the knowledge graph rather than flunisolide-specific data. Route compatibility has not yet been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18926054](https://pubmed.ncbi.nlm.nih.gov/18926054/) | 2008 | Cohort | Allergy and Asthma Proceedings | Measured exhaled breath condensate pH and Th1/Th2/T-regulatory cytokines in asthmatic children with atopic dermatitis, and looked at the effect of a short course of inhaled corticosteroid. This is a biomarker study and does not test flunisolide as a treatment for atopic dermatitis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA074805 | Flunisolide | Solution | Oceanside Pharmaceuticals |
| ANDA074805 | Flunisolide | Solution | Bausch & Lomb Incorporated |
| ANDA207802 | Flunisolide | Solution | Ingenus Pharmaceuticals, LLC |

Approved indication text was not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on class-level plausibility only, with no registered trials and no flunisolide-specific evidence in atopic eczema. The route of administration (inhaled or intranasal) also differs from the standard topical approach for skin disease.

**To proceed, the following is needed:**
- The package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A route compatibility assessment, since no topical flunisolide formulation is listed among the US authorizations
- Flunisolide-specific clinical evidence in atopic dermatitis
- Merging the duplicate "atopic eczema" and "dermatitis, atopic" entries in downstream reporting

Among the other predictions for this drug, bronchitis and polyp of frontal sinus fit the marketed inhaled or intranasal route better, though their evidence is also thin. A targeted search on nasal polyposis or chronic rhinosinusitis with nasal polyps could strengthen the latter.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

