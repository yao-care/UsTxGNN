---
layout: default
title: Adenine
parent: Model Prediction Only (L5)
nav_order: 215
evidence_level: L5
indication_count: 1
---

# Adenine
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

# Adenine: From No Documented Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

Adenine is a purine base that is currently listed in the US as liquid products, but the records give no approved indication.
The TxGNN model predicts it may be relevant to **drug-induced osteoporosis**, but **0 clinical trials** and **0 publications** actually support this. The one registered trial found is an unrelated kidney disease registry, and the four papers found describe purine-analog drugs that *cause* bone damage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the records |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (license numbers not recorded) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. No original indication is recorded either, so there is no established use to build a mechanistic bridge from.

The score is high (0.99), but the supplied evidence does not link adenine to treating or preventing drug-induced osteoporosis. The retrieved literature is about adenine-nucleotide-analog antivirals such as adefovir and tenofovir. These drugs are associated with bone toxicity, which is the opposite of a therapeutic effect. The graph signal most likely reflects network proximity to these purine-analog drugs, not a true therapeutic relationship.

One further point comes from general background knowledge, not from the supplied data, and has not been verified here. Adenine at high doses is a known experimental nephropathy inducer in rodents. That raises a safety question for any bone-related use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06065852](https://clinicaltrials.gov/study/NCT06065852) | N/A | Recruiting | 35,000 | National registry of rare kidney diseases (RaDaR), collecting data for guidelines and audits. It does not test adenine or any intervention and does not address drug-induced osteoporosis (relevance grade C, no usable evidence). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22943210](https://pubmed.ncbi.nlm.nih.gov/22943210/) | 2012 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics/pharmacodynamics of emtricitabine/tenofovir in HIV infection. Not about osteoporosis treatment. |
| [41924521](https://pubmed.ncbi.nlm.nih.gov/41924521/) | 2026 | Case report | Front Endocrinol | Long-term adefovir dipivoxil caused Fanconi syndrome and hypophosphatemic osteomalacia and osteoporosis in a 67-year-old woman. The drug caused the bone damage. |
| [31026554](https://pubmed.ncbi.nlm.nih.gov/31026554/) | 2019 | Preclinical (rat) | J Ethnopharmacol | Xian-Ling-Gu-Bao, an herbal formula used for osteoporosis, induced liver injury in rats through inflammatory and oxidative stress. Unrelated to adenine. |
| [20026012](https://pubmed.ncbi.nlm.nih.gov/20026012/) | 2010 | In vitro | Biochem Biophys Res Commun | Tenofovir exposure altered gene expression (Gnas, Got2, Snord32a) in primary osteoclasts, a possible mechanism for drug-induced bone loss. |

None of these studies tests adenine.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Adenine (Professional Complementary Health Formulas) | Liquid | Not stated |
| Not listed | Adenine 3X (Energique, Inc.) | Liquid | Not stated |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (evidence level L5). No trial or paper supports adenine for drug-induced osteoporosis, and the retrieved literature points to bone toxicity from related purine analogs. There is also no recorded original indication, mechanism, or safety information.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to test whether any real link to bone metabolism exists
- Direct evidence on adenine and bone health, such as preclinical or clinical studies
- An assessment of the rodent nephropathy signal and its relevance to human dosing
- Confirmation of what the two listed liquid products are and their regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

