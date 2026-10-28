---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
monitor_inn: "LIDOCAINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-10-23
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Relations recorded in the knowledge graph (not label-confirmed): derm…"
---

# Lidocaine
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

## Lidocaine: From Dermatitis and Neuralgia to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a local anesthetic and sodium channel blocker. The TxGNN model's top prediction is **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** support it, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph (not label-confirmed): dermatitis, neuralgia, postherpetic neuralgia, hemorrhoid, scabies and others. No approved indication text was available in the licence records. |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | at least 9 |
| Number of approvals | At least 9 (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lidocaine is generally known as a local anesthetic that blocks voltage-gated sodium channels and reduces sensory nerve signaling. In theory, this could relieve pain or discomfort on the ocular surface.

The relations recorded in the knowledge graph (dermatitis, neuralgia, postherpetic neuralgia and others) are mostly about pain, itch and local sensory symptoms. This overlaps with the symptoms of ocular surface disease. Any benefit would be symptomatic only. It would not treat the underlying epithelial damage.

There is also a safety concern. Repeated use of topical anesthetics on the cornea can cause corneal toxicity, which argues against chronic use on an already damaged epithelium. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by direct studies.

### Other Predictions in the Same Run

| Rank | Predicted Disease | Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Papillary conjunctivitis | 0.9998 | L5 | No studies |
| 3 | Rosacea conjunctivitis | 0.9992 | L5 | No studies; symptomatic link only |
| 4 | Exposure keratitis | 0.9987 | L5 | One unrelated case series (methamphetamine abusers) |
| 5 | Atopic conjunctivitis | 0.9986 | L5 | Mechanistic and physiological papers only |
| 6 | Conjunctival disorder | 0.9984 | L5 | Procedural anesthesia studies (pterygium surgery); see below |
| 7 | Nephrotic syndrome | 0.9983 | L5 | Pharmacokinetic and safety papers only |
| 8 | Non-human animal disease | 0.9982 | L5 | Not a human indication; animal safety report |
| 9 | Tinea corporis | 0.9982 | L5 | No antifungal activity |
| 10 | Steroid-resistant nephrotic syndrome | 0.9979 | L5 | No studies |

The top prediction has no studies for its own disease. Under the evidence rules, the level is L5. Ranks 6 and 7 are also set to L5 here. Their studies address procedural anesthesia or pharmacokinetics, not treatment of the predicted disease itself.

## Clinical Trial Evidence

Currently no related clinical trials are registered for punctate epithelial keratoconjunctivitis.

For reference, two completed trials were found for the lower-ranked prediction "conjunctival disorder". They concern anesthesia during surgery, not disease treatment:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine ophthalmic gel vs subconjunctival lidocaine injection in pterygium excision |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | Not applicable | Completed | 34 | Postoperative pain with two types of local anesthesia in drooping eyelid surgery |

## Literature Evidence

Currently no related literature is available for punctate epithelial keratoconjunctivitis.

For reference, the following papers relate to lower-ranked ocular predictions. None tests lidocaine as a treatment for the top-ranked disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye | Lidocaine 2% gel vs tetracaine 1% drops as the sole topical anesthetic in primary pterygium surgery |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Pilot study | Cornea | Subconjunctival injection vs 2% vs 5% lidocaine gel in pterygium surgery |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical study | Acta Ophthalmol Scand | Efficacy of lidocaine 2% gel in pterygium surgery |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Clinical study | Ophthalmologica | Pain relief after pterygium surgery with viscous lidocaine |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Preclinical | JCI Insight | Nerve-goblet cell association promotes allergen passage in allergic conjunctivitis |
| [8039024](https://pubmed.ncbi.nlm.nih.gov/8039024/) | 1994 | Physiological study | Clin Exp Allergy | Nasal anesthesia and lacrimal function after nasal allergen challenge |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Safety review | Cephalalgia | Neuropsychiatric side effects of lidocaine in headache treatment |
| [8862924](https://pubmed.ncbi.nlm.nih.gov/8862924/) | 1996 | Case series | Cornea | Keratitis in methamphetamine abusers (no lidocaine benefit shown) |

## US Market Information

Nine US licences are listed; the list may be partial. All are single-ingredient products. No approved indication text was available in the licence records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA088327 | Lidocaine Hydrochloride | Injection, solution | Not available |
| NDA006488 | Xylocain (Lidocaine HCl) | Injection, solution | Not available |
| ANDA088325 | Lidocaine Hydrochloride | Injection, solution | Not available |
| ANDA209190 | Tridacaine XL | Patch | Not available |
| ANDA206463 | Lidocaine | Patch | Not available |

Other listed products include topical gels and creams (for example pain relief rollers and numbing creams).

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** hypertension, liver failure and liver disease, cirrhosis, epilepsy, kidney disease, adrenocortical insufficiency, hypothyroidism, open-angle glaucoma, herpes simplex keratitis, varicella zoster infection, measles, atopic dermatitis, osteoporosis, psychotic and other mental disorders, fungal infections, potassium deficiency and gastritis. These should be checked against the package insert.
- **Drug interactions:** 100 interactions were found. Major: bupropion. Moderate: aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol (3350 with electrolytes), picosulfuric acid and sodium sulfate. Minor: dexamethasone, kanamycin, neomycin, streptomycin, omeprazole and troglitazone.
- **Literature signals:** neuropsychiatric and cardiac side effects with intravenous lidocaine (PMID 19250287), and methemoglobinemia in a child using several methemoglobin-inducing drugs (PMID 41995267). Repeated topical anesthetic use on the cornea carries a risk of corneal toxicity.

Package insert warnings and contraindications were not available and must be reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by a model score. There are no trials or publications for punctate epithelial keratoconjunctivitis (L5). Repeated topical anesthetic use on damaged corneal epithelium also carries a safety concern. The ocular studies found concern procedural anesthesia, which is not repurposing evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label
- Detailed mechanism of action data
- Preclinical or clinical evidence for lidocaine in punctate epithelial keratoconjunctivitis, with attention to corneal toxicity
- Confirmation of whether any ophthalmic route or formulation is suitable (route compatibility is still pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

