---
layout: default
title: Diazoxide
parent: Model Prediction Only (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
monitor_inn: "DIAZOXIDE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "autosomal dominant hyperinsulinism due to Kir6.2 deficiency"]
last_modified_at: 2026-10-14
description: "Diazoxide: predicted new indication Alopecia . The top three predictions… (evidence level L5). Approved use: Hyperinsulinemic hypoglycemia…"
---

# Diazoxide
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

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Alopecia

## One-Sentence Summary

Diazoxide is a KATP channel opener, originally used to treat hyperinsulinemic hypoglycemia and insulin-producing pancreatic tumours (insulinoma).
The TxGNN model predicts it may be effective for **Alopecia** (the highest-ranked prediction that has any supporting literature), with **0 registered clinical trials** and **5 publications** currently supporting this direction. All of these are reviews, case reports or preclinical work, and none tests efficacy in human alopecia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperinsulinemic hypoglycemia, insulinoma and related pancreatic conditions |
| Predicted New Indication | Alopecia (rank 4 of the model's top 10). The top three predictions, hypotrichosis simplex of the scalp, congenital hypotrichosis milia and diffuse alopecia areata, have no supporting evidence. |
| TxGNN Prediction Score | 99.92% (alopecia). The top-ranked prediction, hypotrichosis simplex of the scalp, scores 99.96%. |
| Evidence Level | L4 (preclinical evidence only) |
| US Market Status | Cancelled only (no currently valid listings) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, diazoxide opens ATP-sensitive potassium (KATP) channels. In the pancreas this suppresses insulin release, which explains its use in hyperinsulinemic hypoglycemia.

The link to hair is an adverse-effect signal. Hypertrichosis is a well-documented side effect of diazoxide. Minoxidil, an established hair-growth drug, is also a KATP opener (through its sulfate metabolite). Researchers have therefore asked whether diazoxide's hair-growth effect could be used on purpose. In a stumptailed macaque model of baldness, topical diazoxide induced hair regrowth on the bald scalp (PMID 2085505, PMID 8326148).

The original and new indications are unrelated diseases. The connection rests only on a shared mechanism and a side effect, with no human efficacy data. Several other top predictions are weaker still:

- **Diffuse alopecia areata:** this is autoimmune, and stimulating follicle growth does not address the immune attack.
- **Hypertrichosis and Ambras syndrome:** diazoxide causes excess hair, so using it for these conditions makes no sense and could worsen them. These are adverse-effect signals, not therapeutic ones.
- **Autosomal dominant hyperinsulinism due to Kir6.2 deficiency:** this is close to an existing use rather than a new one, and dominant Kir6.2 mutations are often diazoxide-unresponsive.
- **Malformation syndromes (odontal/periodontal, Dandy-Walker):** there is no plausible mechanism, and these are likely knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications retrieved for the alopecia prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Preclinical (macaque) | Journal of Dermatological Science | Topical diazoxide (5% solution) was tested on the bald frontal scalp of stumptailed macaques, with systemic side effects monitored. |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Review | Journal of Investigative Dermatology | Topical minoxidil and diazoxide, both with a hypertrichotic side effect, induced significant hair regrowth in bald macaque scalps. |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Review | Drug Safety | Reviews drug-induced hair loss and growth. It does not test diazoxide as an alopecia treatment. |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Case report | Pediatric Dermatology | Generalized hypertrichosis in a child after secondary topical minoxidil exposure. Diazoxide is mentioned only as a known cause of hypertrichosis. |
| [20682429](https://pubmed.ncbi.nlm.nih.gov/20682429/) | 2010 | Review | Vet Clin North Am Exotic Anim Pract | Medical management of insulinoma and adrenal disease in ferrets, with diazoxide as one option. Indirect relevance. |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Observational | Archives of Disease in Childhood | Fetal exposure to diazoxide in four infants. Indirect relevance. |

The macaque study is the only direct efficacy evidence, and it is preclinical.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA211050 | Diazoxide (e5 Pharma, LLC) | Suspension | Not listed; status cancelled |
| ANDA210799 | Diazoxide (Par Health USA, LLC) | Suspension | Not listed; status cancelled |
| NDA017453 | Proglycem (Teva Pharmaceuticals USA, Inc.) | Suspension | Not listed; status cancelled |

All three listings are cancelled, so no currently valid US listing was found in the compiled data. Only an oral suspension is on record. No topical formulation is listed.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links diazoxide to the following contraindicated conditions:
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, potassium deficiency, gout and hyperuricemia.
  - Cardiovascular: congestive heart failure, coronary artery disease, cerebrovascular disorder, orthostatic hypotension, postural orthostatic tachycardia syndrome and multiple system atrophy.
  - Organ disease: kidney disease, kidney failure, uremia, liver disease, gallbladder disease and pyoureter.
- **Drug Interactions:** 100 interactions were recorded, and all those shown are rated Moderate. Examples include:
  - Antidiabetic drugs: acarbose, metformin, pioglitazone, alogliptin, albiglutide, dulaglutide, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, chlorpropamide and acetohexamide.
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide and triamcinolone.
  - Others: bupropion, morphine and dronabinol.
- **Adverse effects reported in the literature:**
  - Hypertrichosis, the most common adverse reaction in a Japanese post-marketing survey (8.6%).
  - Water retention (8.3%) and cardiac failure (3.4%) in the same survey of 384 children.
  - Necrotizing enterocolitis in neonates (PMID 33483452).

Package insert warnings were not available in the compiled data. Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN scores are model predictions only. For alopecia the sole direct evidence is a 1990 macaque study of topical diazoxide, and no human trials exist. The systemic form has a substantial safety burden (fluid retention, heart failure, hyperglycemia) that is hard to justify for a cosmetic or dermatologic indication. Several top predictions (hypertrichosis, Ambras syndrome) point in the adverse-effect direction and should not be pursued. The Kir6.2 hyperinsulinism prediction is an existing-use variant, not new repurposing.

**To proceed, the following is needed:**
- Mechanism of action data and FDA package insert warnings and contraindications (currently missing).
- A topical formulation and route strategy, since systemic dosing is unlikely to be acceptable for alopecia. No topical product currently exists in the US data.
- Preclinical and early human data on topical diazoxide in androgenetic alopecia, including systemic absorption and a comparison with minoxidil.
- For the Kir6.2 hyperinsulinism prediction, genotype-specific evidence of diazoxide responsiveness.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

