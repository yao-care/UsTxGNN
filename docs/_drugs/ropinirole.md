---
layout: default
title: Ropinirole
parent: Moderate Evidence (L3-L4)
nav_order: 1134
evidence_level: L4
indication_count: 10
---

# Ropinirole
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

# Ropinirole: From Restless Legs Syndrome to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Ropinirole is a dopamine agonist marketed in the US as oral tablets, and the candidate's rationale names restless legs syndrome (RLS) as an approved use.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but the support is thin: **0 registered clinical trials**, **1 pediatric case report** and a few reviews on the ADHD-RLS overlap.
This is a research question, not a treatment recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Restless legs syndrome (per the candidate's rationale; the license records contain no indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the listed ones are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Ropinirole is a D2/D3 dopamine receptor agonist, and ADHD is linked to dopaminergic dysfunction, so a mechanistic connection is plausible.

The literature signal comes mainly from the overlap between RLS and ADHD. The two conditions frequently occur together, and a 2005 review discusses using common treatments when both are present. A single pediatric case report describes a 6-year-old boy with ADHD and probable RLS/periodic limb movement syndrome. Methylphenidate had limited effect, and ropinirole improved both his ADHD symptoms and his sleep.

This is indirect evidence. The benefit may have come from treating RLS-related sleep disruption rather than ADHD core symptoms. The very high TxGNN score is a model prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | Case report | Pediatr Neurol | Child with ADHD and RLS; ropinirole improved both ADHD symptoms and sleep problems |
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Review | Sleep | Reviews the RLS-ADHD association, possible mechanisms, and shared pharmacologic treatment |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Rev Neurol | General review of RLS (about 2-3% prevalence in Western countries) |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical | Pharmacol Res | Dopamine D4 receptor variants and α2A adrenoceptor interact; relevant to ADHD genetics |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | Preclinical | J Neuropathol Exp Neurol | Mouse model of RLS combining dopaminergic lesion and iron deprivation |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Clinical study | Clin Neuropharmacol | 11-week comparison of piribedil vs pramipexole/ropinirole on vigilance in Parkinson's disease; not ADHD |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | Case report | Cornea | Corneal edema in 3 patients on systemic dopaminergic agents (safety signal) |
| [30460371](https://pubmed.ncbi.nlm.nih.gov/30460371/) | 2019 | Case report | Acta Derm Venereol | Delusions of infestation linked to increased brain dopamine during treatment (safety signal) |

## US Market Information

The record lists 20 licenses; five entries are shown here, and the repeated ANDA078110 entries are merged. The indication text is blank in all of them. Oral film-coated tablets and extended-release film-coated tablets are both marketed.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA090135 | ropinirole | Tablet, film coated | Glenmark Pharmaceuticals Inc., USA |
| ANDA078110 | ropinirole hydrochloride | Tablet, film coated | SOLCO HEALTHCARE US, LLC |
| ANDA078110 | ropinirole hydrochloride | Tablet, film coated | Bryant Ranch Prepack |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

The retrieved literature contains dopaminergic-agent case reports of corneal edema and drug-induced delusions of infestation. These are not label-level data and should be treated only as signals to check.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is one pediatric case report plus reviews of the ADHD-RLS overlap, with no registered trials. Any benefit could be secondary to treating RLS rather than ADHD itself. The 99.99% TxGNN score is a prediction only.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Controlled studies of ropinirole in ADHD, ideally in patients with and without RLS, to separate an ADHD effect from an RLS effect
- Pediatric safety review, including dopamine-agonist neuropsychiatric effects such as delusions

The lower-ranked predictions (for example schizophrenia, myopia and rare congenital disorders) have no trials, and most have no plausible mechanism. For schizophrenia, the retrieved reports describe dopamine-agonist-associated psychosis, so the safety signal outweighs the evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

