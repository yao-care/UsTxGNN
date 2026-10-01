---
layout: default
title: Chlorzoxazone
parent: Model Prediction Only (L5)
nav_order: 525
evidence_level: L5
indication_count: 9
---

# Chlorzoxazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Chlorzoxazone: From Skeletal Muscle Relaxant Use to Migraine Disorder

## One-Sentence Summary

Chlorzoxazone is an oral, centrally acting skeletal muscle relaxant that is marketed in the US as generic tablets.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 registered clinical trials** and only **3 indirect publications**, none of which studies chlorzoxazone in migraine.
The prediction is best treated as a research question, not clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skeletal muscle relaxant use (label indication text is not included in the provided US license records) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (preclinical/mechanistic signal only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (all listed examples are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record provided. Based on the available information, chlorzoxazone is a centrally acting muscle relaxant that is known to activate Ca²⁺-activated K⁺ channels (SK/IK). That is the only mechanistic link to migraine.

One preclinical study (PMID 23115190) found that activators of Ca²⁺-dependent K⁺ channels reduced ataxia caused by enhanced CaV2.1 calcium currents in mutant mice. CaV2.1 dysfunction (the *CACNA1A* gene) is also implicated in familial hemiplegic migraine. This suggests a plausible channelopathy-based hypothesis: modulating K⁺ channels might counterbalance CaV2.1 hyperactivity.

This is only a hypothesis. The study is in mice and does not involve chlorzoxazone or migraine patients. The two vertigo and ataxia reviews are background only. The 99.73% TxGNN score is a computational prediction from the knowledge graph, not proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | Preclinical/Animal | J Neurosci | In *Cacna1a* S218L mutant mice, Ca²⁺-dependent K⁺-channel activators alleviated ataxia caused by enhanced CaV2.1 currents. CACNA1A mutations are linked to ataxia, hemiplegic migraine and epilepsy. |
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Review | J Neurol | Overview of drug treatment for cerebellar and central vestibular disorders (e.g., 4-aminopyridine for downbeat nystagmus). Background only. |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Dtsch Arztebl Int | Treatment and natural course of peripheral and central vertigo. Vestibular migraine accounts for about 11.4% of cases. Background only. |

None of these papers evaluates chlorzoxazone in migraine.

## US Market Information

Five of the 20 authorizations are shown. All are oral tablets named Chlorzoxazone. The provided records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA089859 | Chlorzoxazone | Tablet | Bryant Ranch Prepack |
| ANDA089859 | Chlorzoxazone | Tablet | Actavis Pharma, Inc. |
| ANDA212743 | Chlorzoxazone | Tablet | Endo USA, Inc. |
| ANDA214702 | Chlorzoxazone | Tablet | Lifsa Drugs LLC |
| ANDA089853 | Chlorzoxazone | Tablet | REMEDYREPACK INC. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no studies of chlorzoxazone in migraine. The only support is a preclinical K⁺-channel/CaV2.1 hypothesis plus the TxGNN score. This is a research question, not a candidate ready for clinical development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism-of-action data from DrugBank, including SK/IK channel activity and its relevance to CaV2.1-related migraine
- Preclinical or mechanistic studies testing chlorzoxazone directly in migraine models, especially familial hemiplegic migraine
- Confirmed US label indication text

Among the other predicted indications, rheumatoid arthritis has the most literature. It is limited to old, uncontrolled reports and a 2012 Cochrane review of muscle relaxants for RA pain, whose conclusions need manual review. Any role there would be symptomatic pain and spasm relief, not disease modification.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

