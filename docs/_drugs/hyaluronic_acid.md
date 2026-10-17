---
layout: default
title: Hyaluronic Acid
parent: High Evidence (L1-L2)
nav_order: 774
evidence_level: L2
indication_count: 10
monitor_inn: "HYALURONIC ACID"
predicted_indications: ["dry eye syndrome", "Sjogren syndrome", "xerophthalmia", "psoriasis", "dermatitis, atopic", "prolapse of lacrimal gland", "parapsoriasis", "pityriasis lichenoides", "severe nonproliferative diabetic retinopathy", "exanthem (disease)"]
last_modified_at: 2026-10-14
description: "Hyaluronic Acid: predicted new indication Dry eye syndrome (evidence level L2). Approved use: Not specified in the license records (all approved-indication fields…"
---

# Hyaluronic Acid
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Hyaluronic Acid: From No Labeled Indication to Dry Eye Syndrome

## One-Sentence Summary

Hyaluronic acid is a hygroscopic, viscoelastic polymer used mainly in cosmetic, topical and ophthalmic products. No approved indication text appears in its US license records.
The TxGNN model predicts it may be effective for **dry eye syndrome**,
with **10 clinical trials** and **20 publications** currently supporting this direction. This includes a completed Phase 3 randomized trial and several meta-analyses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the license records (all approved-indication fields are blank) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (per the evidence scoring; note that only one Phase 3 RCT is listed, see below) |
| US Market Status | Cancelled only |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the known properties of the molecule, hyaluronic acid is a hygroscopic, viscoelastic polymer. It retains water on the ocular surface, stabilizes the tear film, lubricates, and supports corneal epithelial wound healing (CD44-mediated).

Dry eye is fundamentally a tear-film deficiency and ocular surface discomfort problem, so this mechanism maps directly onto the disease. Meta-analyses and systematic reviews (PMIDs 33804439, 38895674, 35514082) support its efficacy.

Hyaluronic acid is already widely marketed as artificial tears, largely as a medical device. This is therefore closer to an established use than true repurposing.

Other predicted indications are much weaker:

| Predicted Indication | Evidence Level | Decision | Comment |
|------|------|------|------|
| Sjogren syndrome | L2 | Proceed with Guardrails | Palliative relief of the ocular component only; does not modify the autoimmune disease |
| Xerophthalmia | L3 | Research Question | Evidence is from general dry eye; vitamin A repletion is the real treatment |
| Atopic dermatitis | L3 | Research Question | Adjunctive emollient/barrier support; HA is mostly a component or carrier |
| Psoriasis | L4 | Hold | Preclinical only; HA acts mainly as a CD44-targeting carrier |
| Exanthem | L4 | Hold | Loose ontology match; retrieved trials are not about exanthems |
| Lacrimal gland prolapse, parapsoriasis, pityriasis lichenoides, severe NPDR | L5 | Hold | Model prediction only, no supporting studies |

---

## Clinical Trial Evidence

Trials for the top prediction (dry eye syndrome):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00599716](https://clinicaltrials.gov/study/NCT00599716) | Phase 3 | Completed | 300 | Multicenter, double-masked RCT of Vismed (sodium hyaluronate) vs. vehicle in dry eye; direct Phase 3 evidence |
| [NCT06478134](https://clinicaltrials.gov/study/NCT06478134) | Phase 2/3 | Completed | 124 | TriMix multiple-action tear substitute vs. HA-based control; combination product |
| [NCT07722650](https://clinicaltrials.gov/study/NCT07722650) | N/A | Completed | 120 | Twice-daily Systane Complete vs. four-times-daily Thealoz Duo (trehalose plus HA); HA effect not isolated |
| [NCT05823961](https://clinicaltrials.gov/study/NCT05823961) | N/A | Completed | 80 | Single-arm post-market follow-up of cross-linked HA eye drops; supports performance and safety |
| [NCT03074344](https://clinicaltrials.gov/study/NCT03074344) | N/A | Completed | 40 | Cross-linked HA plus coenzyme Q10 eye drops in mild to moderate dry eye; small, combination product |
| [NCT06122428](https://clinicaltrials.gov/study/NCT06122428) | N/A | Completed | 16 | Riboflavin-conjugated HA 0.1% (HAr) lubricant drops; small retrospective study |

Trials with HA only as a comparator or with a different focus (limited relevance): NCT04673643 and NCT06544447 (auricular vagus nerve stimulation, status unknown), NCT07089511 (cord blood plasma eye drops), and NCT01838252 (HA gels for lid retraction, withdrawn with no enrolment).

Other indications: one completed Phase 3 trial under Sjogren syndrome tests platelet-rich plasma, not HA ([NCT02257957](https://clinicaltrials.gov/study/NCT02257957)). One completed study under atopic dermatitis tests an HA-containing repair cream ([NCT07742241](https://clinicaltrials.gov/study/NCT07742241), n=116, multi-component product).

**Evidence-level caveat:** the data show only one completed Phase 3 RCT directly testing an HA product against vehicle (NCT00599716), plus one Phase 2/3 trial. The L1 label rests mainly on the meta-analyses below, and a stricter reading of the rules (≥2 completed Phase 3 RCTs) would place the evidence at L2.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | Non-inferiority trial comparing laughter exercise with 0.1% sodium hyaluronate in dry eye disease |
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | Meta-analysis | Int J Environ Res Public Health | Compares HA with non-HA eye drops (saline, conventional artificial tears) in dry eye |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | Systematic review/Meta-analysis | Int J Ophthalmol | Compares high vs. low concentration HA eye drops for dry eye |
| [37162564](https://pubmed.ncbi.nlm.nih.gov/37162564/) | 2023 | Meta-analysis of RCTs | Graefes Arch Clin Exp Ophthalmol | Topical diquafosol vs. HA for dry eye disease |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmol | Critical evaluation of safety and efficacy of HA artificial tears in dry eye |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Review | Acta Ophthalmol | HA compared with other single-ingredient eye drops; HA described as a long-standing safe and effective treatment |
| [37682142](https://pubmed.ncbi.nlm.nih.gov/37682142/) | 2023 | RCT | Medicine | 0.15% HA vs. 0.05% cyclosporine A vs. 3% diquafosol in college students with dry eye |
| [31373862](https://pubmed.ncbi.nlm.nih.gov/31373862/) | 2019 | Review | J Ocul Pharmacol Ther | Cross-linked HA as tear substitute; HA superior to PVA, HPMC, CMC and PEG for viscosity and tear-film stability |
| [37117131](https://pubmed.ncbi.nlm.nih.gov/37117131/) | 2023 | Clinical study | Contact Lens & Anterior Eye | Trehalose plus HA artificial tears in women aged 42-54 vs. ≥55 years |
| [3101502](https://pubmed.ncbi.nlm.nih.gov/3101502/) | 1987 | Controlled study | Am J Ophthalmol | HA and chondroitin sulfate in 20 keratoconjunctivitis sicca patients; 18 reported marked improvement |

Supporting studies in Sjogren syndrome include a comparative study of HA vs. cross-linked HA eye drops ([28557655](https://pubmed.ncbi.nlm.nih.gov/28557655/), 2017) and a clinical study of cortisol phosphate in an HA vehicle ([28375792](https://pubmed.ncbi.nlm.nih.gov/28375792/), 2017).

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M016 | Roushun kojic Skin Lightening Natural Skin Care treatment serum 30ml | Liquid | Not specified (cancelled) |
| nan | JASBELLO VAGINAL | Suppository | Not specified (cancelled) |
| 505G(a)(3) | Instant Anti Aging Wrinkle Eye Treatment Syringe | Cream | Not specified (cancelled) |

All three authorizations are cancelled, and there is no active US-approved drug product for this ingredient in the data compiled. The listed products are cosmetic or skincare items, not ophthalmic drugs.

---

## Safety Considerations

- **Knowledge-graph contraindication signal:** glaucoma appears as a drug-disease contraindication edge in the TxGNN knowledge graph. This comes from the graph, not from label text, and should be verified for ophthalmic use.
- **Drug Interactions:** two moderate-level interactions were identified, both with topical quaternary ammonium antiseptics: cetylpyridinium (topical) and benzalkonium (topical).
- **Literature signals:** case reports describe chronic eyelid oedema and dry eye symptoms after periorbital HA filler injection (PMID 31441981). Autoimmune/inflammatory syndrome induced by adjuvants (ASIA) has been reported with injected biomaterials, including HA fillers (PMIDs 29199390, 22952322). These relate to injectable filler use, not eye drops.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Dry eye syndrome has a direct mechanistic fit, a completed Phase 3 vehicle-controlled RCT, and several meta-analyses supporting HA eye drops. HA is already widely used as artificial tears, so this is mostly an established use rather than new repurposing. The US license records, however, are cancelled cosmetic or skincare products with no stated indication.

**To proceed, the following is needed:**
- Regulatory pathway clarification: HA eye drops are largely marketed as devices, and no active US drug license exists in the data.
- Label warnings and contraindications, which are not available in the data compiled; verify the glaucoma signal.
- Detailed mechanism of action data from DrugBank.
- A second adequately powered, HA-specific randomized trial, since many listed trials are combination products or use HA only as a comparator.
- Other predicted indications (Sjogren syndrome: palliative only; xerophthalmia and atopic dermatitis: research questions) should not advance without HA-specific clinical evidence. Psoriasis, exanthem and the remaining predictions are on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

