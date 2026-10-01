---
layout: default
title: Trazodone
parent: High Evidence (L1-L2)
nav_order: 1254
evidence_level: L2
indication_count: 10
---

# Trazodone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Trazodone: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Trazodone is an antidepressant approved by the FDA for depression, according to a published review (PMID 27744763). The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**. This direction is supported by **0 registered clinical trials** and **20 publications**, most of them small studies and case reports from the 1980s and 1990s.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (per PMID 27744763; the US license records contain no indication text) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Trazodone is a serotonin antagonist and reuptake inhibitor. Its most potent action is 5-HT2A/2C receptor antagonism, with weaker serotonin transporter (SERT) inhibition (PMID 1365657). Detailed mechanism of action data is not available in the DrugBank record, so this description comes from the literature and the pack's mechanistic rationale.

Serotonin modulation is the core pharmacology of OCD treatment. The only drugs with strong evidence in OCD are potent serotonin reuptake inhibitors such as clomipramine, fluoxetine, fluvoxamine and paroxetine (PMID 8993077). Trazodone is also an established antidepressant, and depression often accompanies OCD. This makes the prediction biologically plausible.

There is an important caveat. Trazodone's SERT inhibition is much weaker than that of SSRIs or clomipramine. Any benefit in OCD is therefore more likely to be adjunctive than as monotherapy. The literature reflects this: some patients with clomipramine-resistant OCD responded, but a trazodone and tryptophan combination gave only marginal benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled study of trazodone in OCD. The abstract excerpt does not show the outcome. |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Clinical study | Clin Neuropharmacol | Nine clomipramine-resistant OCD patients. The group improved mildly but significantly, and 3 responded very favorably. Symptoms returned on withdrawal and eased on re-administration. |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Clinical study | Psychopathology | Responders to trazodone, with or without an MAOI, showed shifts in caudate glucose metabolism on PET. |
| [3571943](https://pubmed.ncbi.nlm.nih.gov/3571943/) | 1986 | Open pilot | Int Clin Psychopharmacol | Trazodone plus tryptophan in 11 patients. Results were not encouraging, with marginal benefit and poor tolerability in several patients. |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case report | J Nerv Ment Dis | Two treatment-refractory OCD patients with depression improved rapidly on trazodone. |
| [6703152](https://pubmed.ncbi.nlm.nih.gov/6703152/) | 1984 | Case report | Am J Psychiatry | Case report on trazodone in OCD (no abstract available). |
| [8434675](https://pubmed.ncbi.nlm.nih.gov/8434675/) | 1993 | Not classified | Am J Psychiatry | Trazodone treatment of OCD and trichotillomania (no abstract available). |
| [2589561](https://pubmed.ncbi.nlm.nih.gov/2589561/) | 1989 | Not classified | Am J Psychiatry | Trazodone-fluoxetine combination for OCD (no abstract available). |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Curr Pharm Des | Off-label trazodone use, listing OCD among the conditions where it is used. |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | Review of trazodone in psychiatric and medical conditions. It notes the FDA-approved indication is depression. |

---

## US Market Information

The US license records list no approved indication text. Showing the first 5 of 20 licenses; all are oral tablets.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA205253 | Trazodone Hydrochloride | Tablet | Cardinal Health 107, LLC |
| ANDA205253 | Trazodone Hydrochloride | Tablet | Zydus Lifesciences Limited |
| ANDA071524 | Trazodone Hydrochloride | Tablet | NCS HealthCare of KY, LLC dba Vangard Labs |
| ANDA202180 | Trazodone Hydrochloride | Tablet | Torrent Pharmaceuticals Limited |
| ANDA071196 | Trazodone Hydrochloride | Tablet | REMEDYREPACK INC. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The OCD prediction is mechanistically plausible and has some published clinical data, including one placebo-controlled RCT. However, the evidence is small, dated and mixed, and there are no registered trials. Trazodone's weak SERT inhibition suggests at best an adjunctive role. The package insert safety data is also missing, which blocks safety screening. The other nine predicted indications are weaker still. Most are L4–L5, with no or only indirect literature, and treat them as lower priority.

**To proceed, the following is needed:**
- Obtain and parse the FDA package insert (warnings and contraindications) to clear the blocking safety gap.
- Retrieve mechanism of action data from DrugBank.
- Read the full text of the 1992 placebo-controlled RCT (PMID 1629380) to confirm its actual outcome.
- Review the literature items still marked "pending" for relevance, and classify the unclassified studies.
- Define the clinical question, such as adjunct use in SRI-resistant OCD, before any trial design.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

