---
layout: default
title: Acetaminophen
parent: Model Prediction Only (L5)
nav_order: 92
evidence_level: L5
indication_count: 1
---

# Acetaminophen
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

# Acetaminophen: From Pain Relief to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen is a widely marketed pain-relief medicine. The data lists no approved indication text, but its US product names, such as "Pain Relief Extra Strength", point to that use.
The TxGNN model predicts it may be useful for **migraine with brainstem aura**.
No clinical trials are registered for this specific subtype, and the 20 publications retrieved are about migraine in general, so support is **indirect**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain relief (inferred from product names; no approved indication text in the data) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 (indirect only: general migraine literature, nothing specific to brainstem aura) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetaminophen is a long-established analgesic, and it is used for acute migraine attacks in general. Mechanistically it may be applicable to migraine with brainstem aura, but this link has not been verified.

The high TxGNN score most likely reflects the general association between acetaminophen and migraine, not the brainstem aura subtype. Acetaminophen is generally described as a centrally acting analgesic, but that mechanism was not provided in the input and was not verified here. Nothing in the data connects it to the pathophysiology of brainstem aura.

The literature supports acetaminophen as part of acute migraine care. One review of headache in pregnancy describes it as first-line symptomatic treatment. Randomized trials of acetaminophen combined with aspirin and caffeine show benefit in migraine overall. None of these studies address the brainstem aura subtype, so the prediction is best read as a general migraine signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below study brainstem aura specifically. All were still marked "relevance: pending" in the Evidence Pack.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence assessment (guideline-type review of RCTs) | Headache | American Headache Society update on the evidence for pharmacological acute migraine treatments |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT (3 double-blind, placebo-controlled trials) | Archives of Neurology | Tested the acetaminophen + aspirin + caffeine combination for relieving migraine headache pain |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Retrospective analysis of 3 RCTs | Clinical Therapeutics | Acetaminophen + aspirin + caffeine for menstruation-associated migraine vs migraine not linked to menses |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative study | Headache | Isometheptene/dichloralphenazone/acetaminophen vs sumatriptan for mild-to-moderate migraine, with or without aura |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurologic Clinics | Migraine is the most common headache in pregnancy; acetaminophen is first-line symptomatic treatment |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Status migrainosus, a prolonged (>72 h) complication of migraine with or without aura |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | Abortive and preventive migraine therapies in pregnancy |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Migraine in pregnancy and breastfeeding, and treatment approach |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Ubrogepant review; notes acetaminophen among non-prescription options for mild-to-moderate migraine |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Review | Pediatric Annals | Acute and preventive treatment of pediatric migraine |

## US Market Information

The data lists no approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA211544 | 8 Hour Pain Relief | Tablet, extended release | Chain Drug Marketing Association, Inc. |
| M013 | CareOne Infants Acetaminophen | Suspension | American Sales Company |
| M013 | Acetaminophen | Tablet | CVS Pharmacy, Inc. |
| M013 | Pain Relief Extra Strength | Capsule, liquid filled | Humanwell PuraCap Pharmaceutical (Wuhan), Ltd. |
| M013 | Acetaminophen (Red) | Capsule, liquid filled | Humanwell PuraCap Pharmaceutical (Wuhan), Ltd. |

Other marketed forms include chewable, film-coated and coated tablets, liquid, and suppository.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no registered trials and no evidence specific to brainstem aura. The literature is general migraine evidence, and none of it has been screened for relevance. The safety data is also missing entirely, which blocks safety screening. The candidate currently stands as a research question, not an actionable repurposing lead.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap)
- Mechanism of action data, for example from DrugBank
- Relevance screening of the retrieved literature, plus a targeted search for studies in migraine with brainstem aura
- Assessment of route compatibility and the similarity between pain relief and the predicted indication (both still pending)

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

