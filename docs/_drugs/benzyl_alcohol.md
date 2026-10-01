---
layout: default
title: Benzyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
---

# Benzyl Alcohol
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

# Benzyl Alcohol: From Topical OTC Products to Bronchitis

## One-Sentence Summary

Benzyl alcohol is marketed in the US mainly in topical and OTC products such as gels, liquids and sprays, and no original approved indication is recorded in the data.
The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and only **4 publications** on the topic.
Three of those four publications suggest that benzyl alcohol, used as a preservative in nebulized saline, may **cause** bronchitis rather than treat it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only; the retrieved literature does not support efficacy) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 15 listed authorizations (the examples shown are OTC monograph "M" numbers and 505G, not NDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data and original indication data are not available for benzyl alcohol. No supportive mechanism has been established for bronchitis. Any local antiseptic or anesthetic action of benzyl alcohol has not been shown to help in bronchitis.

The high TxGNN score (0.995) comes from patterns in the knowledge graph, not from clinical support. The retrieved literature points the opposite way. Reports from 1990 to 1995 link nebulized bacteriostatic saline, which contains benzyl alcohol as a preservative, to airway irritation and bronchitis. The graph association may therefore reflect this adverse-effect link, or the drug simply appearing alongside bronchitis in the literature, rather than a therapeutic benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7807035](https://pubmed.ncbi.nlm.nih.gov/7807035/) | 1995 | Study/case report | J Fam Pract | Tested whether nebulized bacteriostatic saline, which contains benzyl alcohol as a preservative, irritates the tracheobronchial mucosa in healthy adults. Only the study purpose is available; no results are reported. |
| [2355429](https://pubmed.ncbi.nlm.nih.gov/2355429/) | 1990 | Case report/series | JAMA | Reports bronchitis induced by nebulized bacteriostatic saline, pointing to an adverse effect, not a benefit. |
| [7775900](https://pubmed.ncbi.nlm.nih.gov/7775900/) | 1995 | Letter/commentary | J Fam Pract | Commentary on nebulized saline and bronchitis. No abstract is available. |
| [36747926](https://pubmed.ncbi.nlm.nih.gov/36747926/) | 2023 | In vitro study | Heliyon | Antioxidant, anti-inflammatory and antibacterial activity of *Senna tora* leaf extract. Not relevant to benzyl alcohol treatment of bronchitis. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| M022 | Zilactin | Gel |
| M017 | Lidocaine Plus Pain Relieving (CVS Pharmacy) | Liquid |
| 505G(a)(3) | CVS Maximum Strength LIDOCAINE PLUS | Spray |
| M017 | ITCH X | Gel |
| M017 | Salonpas LIDOCAINE PLUS | Liquid |

Approved indication text is not recorded for these products. Recorded dosage forms are gel, liquid, spray and cream. No inhaled or nebulized product is listed.

---

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records.

Please refer to the package insert for warnings and contraindications.

The literature above also raises a potential airway-irritation signal when benzyl alcohol is inhaled as a preservative in nebulized saline. This matters for any inhaled use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no registered trials, and the available literature suggests benzyl alcohol may irritate the airway rather than treat bronchitis. Nothing in the data supports moving forward.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and original indication data
- Package insert warnings and contraindications, which are needed before safety screening
- Review of whether the TxGNN association reflects the adverse-effect literature rather than efficacy
- Route compatibility assessment, since no inhaled or nebulized product is listed and the current products are topical
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

