---
layout: default
title: Alitretinoin
parent: Model Prediction Only (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
monitor_inn: "ALITRETINOIN"
predicted_indications: ["amenorrhea (disease)", "acne (disease)", "atypical coarctation of aorta", "pregnancy associated osteoporosis", "aortic malformation", "postmenopausal osteoporosis", "autosomal dominant neovascular inflammatory vitreoretinopathy", "breast fibrocystic disease", "benign mammary dysplasia", "Worth syndrome"]
last_modified_at: 2026-10-14
description: "Alitretinoin: predicted new indication Amenorrhea (evidence level L5). Approved use: Not stated in the US license record. Drug-level pharmacology data lis…"
---

# Alitretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Alitretinoin: From Kaposi Sarcoma Skin Lesions to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a retinoid that was marketed in the US as a topical gel (Panretin). The TxGNN model's top prediction is **Amenorrhea**, with a score of 99.99%. However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license record. Drug-level pharmacology data lists Kaposi sarcoma and severe chronic hand eczema as clinical uses |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active marketing authorisation) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology records show that alitretinoin binds retinoic acid receptors (RAR-α, -β, -γ) and retinoid X receptors (RXR-α, -β, -γ). These nuclear receptors regulate cell differentiation and proliferation. Their signalling also touches reproductive and endocrine tissues.

That link is general, and it does not amount to a therapeutic rationale for amenorrhea. No clinical or literature evidence supports it. Retinoids are also strongly teratogenic, which is a major safety concern for use in women of reproductive age. The score should be treated as a computational hypothesis only.

For context, the other nine predictions are also unsupported or weak:
- **Acne** (score 99.92%) is the only prediction with any literature. It has two review articles on retinoids as a class, and none specific to alitretinoin. Evidence level is L4 and the stage is "Research Question". The mechanism is plausible, since retinoids normalise keratinocyte differentiation and reduce sebaceous activity.
- **Aortic conditions** (atypical coarctation of aorta, aortic malformation) are structural anomalies unlikely to respond to drug therapy. Retinoid signalling's role in cardiovascular development is a teratogenic concern rather than a benefit.
- **Osteoporosis** (pregnancy-associated and postmenopausal): excess retinoid or vitamin A exposure is associated with reduced bone density, which argues against benefit.
- **Other predictions** (neovascular inflammatory vitreoretinopathy, fibrocystic breast disease, benign mammary dysplasia, Worth syndrome) have no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered for amenorrhea.

## Literature Evidence

Currently no related literature available for amenorrhea.

For reference, the only literature in the data relates to the second-ranked prediction, acne:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clinics in Dermatology | Overview of vitamin A and retinoids in dermatology, covering topical and oral retinoids and their use in skin conditions |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacology and Applied Skin Physiology | Retinoids act through nuclear retinoid receptors, with relatively selective effects on skin structures, and review of dermatological indications likely to benefit |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020886 (cancelled) | PANRETIN | Gel (topical) | Not stated in the license record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (retinoid receptor agonist); it is not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** The TxGNN knowledge graph lists contraindication links to mycosis fungoides and variants, primary cutaneous T-cell lymphoma, folliculotropic mycosis fungoides, localized pagetoid reticulosis, and granulomatous slack skin disease. These come from graph edges and should be verified against the official label.
- **Drug Interactions:** Pharmacology records show 7 interaction entries. Six are receptor targets (RARA, RARB, RARG, RXRA, RXRB, RXRG) and one is VKORC1 (vitamin K epoxide reductase). The VKORC1 link may be relevant for patients on warfarin-type anticoagulants. No graded interaction severity is available.
- **Teratogenicity:** Retinoids as a class carry a serious risk of birth defects. This is especially important for any use in women of reproductive age, as in amenorrhea.

The package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea prediction rests on a model score alone (L5). There are no trials or publications, the mechanistic link is weak, and teratogenicity is a major safety obstacle. The US marketing authorisation is also cancelled.

**To proceed, the following is needed:**
- Any primary clinical or preclinical evidence linking alitretinoin to amenorrhea
- Detailed mechanism of action data
- FDA package insert warnings and contraindications, to allow a proper safety screen
- A teratogenicity risk assessment and pregnancy-prevention plan for women of reproductive age
- Consideration of whether acne, the only prediction with any literature, is a better research question, although its evidence is class-level only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

