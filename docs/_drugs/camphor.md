---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From Topical OTC Products to Migraine Disorder

## One-Sentence Summary

Camphor is an active ingredient in over-the-counter topical and inhalant products in the US, such as salves, balms, creams and vapor liquids. The TxGNN model predicts it may be effective for **migraine disorder**, but **0 clinical trials** and only **5 loosely related publications** exist, and none shows camphor benefiting migraine. The two case reports that mention camphor-containing essential oils point toward possible headache triggering, not treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license records |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (as assigned in the Evidence Pack; the supporting evidence is indirect) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Camphor is a common essential-oil constituent and topical counterirritant, and it is marketed in many OTC forms. No established mechanism links it to migraine.

The only drug-relevant signal is a case report (PMID 34373243) and a related case series (PMID 35856604). They describe cluster headache temporally associated with toothpastes containing essential oils, including camphor and eucalyptus. Camphor was not shown to be the active agent. Cluster headache is also a different disorder from migraine, and the direction of the signal is possible harm, not benefit.

The high TxGNN score (99.85%) is a computational prediction only. It should be treated as a research question, not as evidence of efficacy.

Other predicted indications had no supporting evidence either:
- **Pulmonary hypertension** and **Raynaud disease**: the retrieved literature is a name collision with the Cambridge Pulmonary Hypertension Outcome Review (CAMPHOR) questionnaire, not the drug.
- **Migraine with brainstem aura**, **kyphoscoliotic heart disease**, **ulerythema ophryogenesis**, **atrophoderma vermiculata** and **Tourette syndrome**: no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | RCT | J Headache Pain | Phase 3 erenumab study in chronic migraine prevention (DRAGON). Not related to camphor; retrieved by disease term only |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Reports | Two cluster headache cases temporally related to toothpastes containing camphor and eucalyptus essential oils; suggests a possible trigger, not a treatment |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cluster headache cases linked to toothpastes containing pro-convulsant essential oils. Indirect, and the direction is possible harm |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical analysis of child and adolescent neuropsychopharmacotherapy in the 1940s and 50s. No direct camphor–migraine evidence |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Other | Minerva Med | Italian paper on therapy for essential hemicrania. No abstract available |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Owell Naturals Draw Salve with Camphor 2.0 oz. | Salve | Not listed |
| M012 | Quality Choice Vapor Steam | Liquid | Not listed |
| M017 | 365 Medicated Lip Balm | Stick | Not listed |
| M017 | Jointflex | Cream | Not listed |
| M017 | Quality Choice Camphor Spirit | Liquid | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

Literature signal: the case reports above describe essential oils with pro-convulsant properties, including camphor-containing products, as possible triggers of cluster headache and as capable of worsening migraine or causing seizures. This is an indirect signal and needs formal safety review. A preclinical oral acute toxicity study in rats (PMID 27955803) also exists for edible camphor.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, no camphor-specific efficacy data, and no established mechanism. The only drug-relevant literature is two case reports suggesting essential oils may trigger headache.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank), to test whether any plausible link to migraine exists
- FDA package insert warnings and contraindications, plus a review of camphor neurotoxicity and seizure risk
- Route compatibility assessment: the marketed products are topical or inhalant OTC forms, and the route required for migraine is not defined
- A targeted literature search that separates the drug from the CAMPHOR questionnaire, and clarifies whether camphor was the active agent in the essential-oil cases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

