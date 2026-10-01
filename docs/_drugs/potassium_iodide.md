---
layout: default
title: Potassium Iodide
parent: Moderate Evidence (L3-L4)
nav_order: 1070
evidence_level: L4
indication_count: 2
---

# Potassium Iodide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Potassium Iodide: From Its Marketed Uses to Nasal Cavity Disease

## One-Sentence Summary

Potassium iodide is a marketed iodide salt sold in the US as solutions, tablets, and pellets, but the supplied regulatory data does not list its approved indications.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **0 clinical trials** and only **4 case reports** (3 veterinary, 1 human).
This is a computational prediction with very weak supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied US regulatory data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Potassium iodide has a long history of empirical use, and the retrieved literature links it to treating fungal and fungus-like infections of the nose and face. These include pythiosis, aspergillosis, *Pseudallescheria boydii* infection, and nasofacial zygomycosis. Its mechanism in these conditions is not well defined. It may involve immunomodulatory or anti-inflammatory effects, but this cannot be verified from the supplied data.

The prediction has an important limit. "Nasal cavity disease" is a very broad label, and the literature covers only mycotic or pythiosis-type infections. It does not cover nasal disease in general, such as allergic or chronic rhinosinusitis. The high TxGNN score is a model output, not proof of efficacy.

TxGNN also predicts **acute laryngopharyngitis** (score 99.95%) as a second indication. There are no trials or literature for it. Iodides have a historical role as expectorants, but nothing in the supplied data supports this, so it stays at L5 (model prediction only).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case report (human) | Rev Inst Med Trop Sao Paulo | 64-year-old woman with nasofacial zygomycosis in Pará, Brazil; rapid response to potassium iodide therapy |
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case report (veterinary, sheep) | J Mycol Med | Rhinofacial pythiosis in sheep, with masses in the nasal cavity and hard palate; reported as successfully treated with potassium iodide |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case report (veterinary, horse) | Vet Res Commun | Mare with *Aspergillus fumigatus* fungal rhinitis treated with topical clotrimazole plus oral potassium iodide |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case report (veterinary, horse) | J Am Vet Med Assoc | Horse with *Pseudallescheria boydii* nasal infection treated with intranasal miconazole, IV sodium iodide, and other therapy |

---

## US Market Information

The five licenses shown are the main ones listed. The pack reports 20 in total. Authorization numbers and approved indication text are not provided in the supplied data. Several of these products (for example Kali Iodatum pellets and the "6X" tablet) appear to be homeopathic-type preparations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Kali Iodatum (Hahnemann Laboratories) | Pellet | Not specified |
| Not listed | Kali Iodatum (Hahnemann Laboratories) | Pellet | Not specified |
| Not listed | SSKI (Atlantic Biologicals) | Solution | Not specified |
| Not listed | Kali iodatum (Boiron) | Pellet | Not specified |
| Not listed | BM Potassium iodide (Kali Iod) 6X (BM Private Limited) | Tablet | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no clinical trials exist, and the literature consists of four case reports, three of them in animals. The evidence is limited to fungal or fungus-like nasal infections, not nasal cavity disease broadly. Safety data and mechanism data are also missing, so the candidate cannot proceed to safety screening.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from the DrugBank API)
- Approved indication text for the marketed products
- A narrower, clinically defined target indication (e.g., specific fungal rhinosinusitis or nasofacial mycosis) instead of "nasal cavity disease"
- Human clinical evidence, such as more human case series or a controlled study
- Confirmation of route compatibility for the intended nasal use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

