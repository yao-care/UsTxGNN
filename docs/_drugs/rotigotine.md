---
layout: default
title: Rotigotine
parent: Moderate Evidence (L3-L4)
nav_order: 1137
evidence_level: L4
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease and Restless Legs Syndrome to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Rotigotine is a dopamine agonist delivered as a skin patch, used for Parkinson's disease and restless legs syndrome.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are currently **0 clinical trials** and only **3 indirect publications** (two RLS reviews and one preclinical study), so this is a hypothesis rather than a supported finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease and restless legs syndrome (per the literature record, PMID 37221270; the license records list no indication text) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 license records (all listed under NDA021829) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Rotigotine is a non-ergot dopamine agonist. It acts on dopamine receptors D1 through D5, mainly D3, D2 and D1, and also has some serotonergic and alpha-2B activity. The structured mechanism field is empty, so this description comes from the repurposing analysis.

ADHD is linked to dopaminergic and noradrenergic dysfunction, so a dopamine-acting drug is a plausible but indirect fit. The retrieved literature covers restless legs syndrome, including in children. RLS is a related comorbidity but not ADHD. One preclinical paper on α2A-adrenoceptor/D4 dopamine receptor heteromerization supports biological plausibility only.

Several points weigh against the prediction:
- Rotigotine's approved profile contains no ADHD efficacy data.
- Standard ADHD therapy works by blocking dopamine and norepinephrine reuptake, not by direct D2/D3 agonism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | Review of pharmacological options for restless legs syndrome in children. It concerns RLS, not ADHD. |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General review of restless legs syndrome (clinical features, prevalence 2–3% in Western countries). Not ADHD-specific. |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical (in vitro) | Pharmacological Research | Heteromerization of α2A adrenoceptors with dopamine D4 receptor variants alters pharmacology. It notes the D4.7 variant and α2A gene are associated with ADHD. Biological plausibility only. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021829 (5 identical records listed; UCB, Inc.) | Neupro | Extended-release patch | Not stated in the record; see the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any clinical trial or direct rotigotine evidence for ADHD, and the mechanism differs from standard ADHD therapy. The other top predictions are weaker still: schizophrenia (also L4) carries a risk that dopamine agonists worsen psychosis, and the rest have no supporting literature or trials (L5).

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications, currently missing. This blocks safety screening.
- Detailed mechanism-of-action data from DrugBank.
- Preclinical or early clinical evidence that rotigotine has an effect in ADHD, such as animal models or a pilot study.
- An assessment of whether a dopamine agonist patch is appropriate for the ADHD population, including pediatric safety and abuse or impulse-control risks.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

