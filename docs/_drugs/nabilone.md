---
layout: default
title: Nabilone
parent: Model Prediction Only (L5)
nav_order: 948
evidence_level: L5
indication_count: 10
---

# Nabilone
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

# Nabilone: From Chemotherapy-Induced Vomiting to Migraine Disorder

## One-Sentence Summary

Nabilone is a synthetic cannabinoid (a THC analog), originally used to treat chemotherapy-induced nausea and vomiting.
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials and no publications** currently support this specific prediction.
The closest signal is one small preliminary RCT in medication overuse headache, a related headache condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced vomiting refractory to standard antiemetics (taken from the literature, because the license record has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on general pharmacology, nabilone is a synthetic agonist of the CB1 and CB2 cannabinoid receptors. Its efficacy in chemotherapy-induced vomiting is established, and mechanistically it may be applicable to migraine. This link comes from general pharmacology, not from the supplied data.

The endocannabinoid system is thought to modulate trigeminovascular pain signalling and central pain processing, which are central to migraine. The other top predictions are also headache-related (migraine with brainstem aura, headache disorder, trigeminal autonomic cephalalgia), which suggests the model is picking up a consistent headache signal.

The score alone is not strong evidence. The prediction ranks 3,706th overall, and no supporting study was retrieved for migraine itself.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

For the neighbouring prediction "headache disorder", the only trial retrieved is [NCT03422861](https://clinicaltrials.gov/study/NCT03422861). It studies nabilone for acute post-surgical pain in IBD patients on chronic opioids, not headache, so it is not headache evidence.

## Literature Evidence

Currently no related literature available for migraine disorder.

The most relevant nearby signal is [PMID 23070400](https://pubmed.ncbi.nlm.nih.gov/23070400/) (2012, *J Headache Pain*). It is a preliminary double-blind, active-controlled RCT of nabilone in 30 patients with medication overuse headache. This is a different condition from migraine, and the study is small and unreplicated.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018677 | Cesamet (Bausch Health US LLC) | Capsule (oral) | Not listed in the license record |

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack has no warning, contraindication or drug-interaction data. The DDI query returned no results.

Cannabinoids can worsen mania or psychosis. This matters for any neuropsychiatric repurposing and should be reviewed when the label is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or literature for migraine. Safety data are also missing, which blocks the safety screening stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (obtain from the FDA label)
- DrugBank mechanism of action data
- Replication of the medication overuse headache RCT (PMID 23070400) in an adequately powered trial. This is the most credible route toward a migraine-related hypothesis, since "headache disorder" (rank 3) is currently the only prediction with direct evidence (L2, capped because unreplicated).
- A nabilone-specific study in migraine before any further advancement

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

