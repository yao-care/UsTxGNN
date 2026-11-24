---
layout: default
title: Scopolamine
parent: Model Prediction Only (L5)
nav_order: 1145
evidence_level: L5
indication_count: 6
monitor_inn: "SCOPOLAMINE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
last_modified_at: 2026-11-24
description: "Scopolamine: predicted new indication Cauda equina syndrome (evidence level L5). In the US: 8 FDA applications (8 active), plus 12 OTC monograph/unapproved NDC listings"
---

# Scopolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Scopolamine: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Scopolamine is an antimuscarinic drug originally used for conditions such as motion sickness, peptic ulcer disease, irritable bowel syndrome, and cycloplegia.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
but **no clinical trials and no publications** currently support this prediction; it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 8 of 8; OTC monograph / unapproved listings: 12) |
| Number of FDA Applications | 8 (active: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for scopolamine: "Scopolamine, a belladonna alkaloid, is an anticholinergic. Scopolamine acts: i) as a competitive inhibitor at postganglionic muscarinic receptor sites of the parasympathetic nervous system, and ii) on smooth muscles that respond to acetylcholine but lack cholinergic innervation." ([DailyMed: Transderm Scop (scopolamine) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b877a694-a1d0-4280-937a-a06820b12a88), label version 2025-06-10; accessed 2026-11-19.) Based on known pharmacology, scopolamine is a non-selective muscarinic antagonist. Blocking muscarinic receptors can reduce detrusor (bladder muscle) overactivity, and that is the link to the bladder dysfunction seen in cauda equina syndrome.

The relationship to the original indications is loose. Scopolamine's known uses are mostly related to reducing smooth muscle spasm and secretions, and to blocking cholinergic signalling in the gut, eye, and vestibular system. Cauda equina syndrome, however, is caused by compression of the nerve roots at the base of the spine and needs surgical decompression. Any effect of scopolamine would at most relieve bladder symptoms, not treat the underlying injury.

The prediction should be read as a model-based hypothesis only.

Other predicted indications were also reviewed. All are at evidence level L5 with no trials or literature:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Obsolete neurogenic bladder (disease) | 0.9998 | Mechanism is plausible (antimuscarinics are an established approach for neurogenic detrusor overactivity), but scopolamine has central nervous system effects and better-studied alternatives exist, such as oxybutynin and solifenacin. The disease term is obsolete in the ontology and needs mapping to a current concept. |
| Papillary conjunctivitis | 0.9998 | Driven by allergic or mechanical inflammation; no established antimuscarinic role. |
| Atopic conjunctivitis | 0.9980 | Mainly IgE/mast cell mediated; antimuscarinic action does not address the core pathology and may cause dry eye. |
| Rosacea conjunctivitis | 0.9940 | Antimuscarinics may reduce tear production and worsen dryness; poor mechanistic fit. |
| Vernal conjunctivitis | 0.9908 | Th2/mast cell driven; at most symptomatic relief of ciliary spasm. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The US license records for scopolamine are all valid. No approved indication text is available in these records.

<!-- review:begin us-lic-20261124b-scopolamine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The nine US license records for scopolamine are all valid." Corrected: the number or type of FDA applications stated here did not match the FDA data (Drugs@FDA and the NDC Directory). The current figures are shown in the Quick Overview and in the program-generated table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261124b-scopolamine-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA078830 | SCOPOLAMINE | DIFGEN PHARMS | System; transdermal | Valid |
| ANDA203753 | SCOPOLAMINE | MYLAN TECHNOLOGIES | System; transdermal | Valid |
| ANDA208769 | SCOPOLAMINE | ACTAVIS LABS UT INC | System; transdermal | Valid |
| ANDA212342 | SCOPOLAMINE | RICONPHARMA LLC | System; transdermal | Valid |
| ANDA215329 | SCOPOLAMINE | RHODES PHARMS | System; transdermal | Valid |

Showing 5 of 20 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from drug-disease relationship data, not from package insert text):
hypertension, liver failure and liver disease, hepatic coma, epilepsy, chronic obstructive pulmonary disease, gastric ulcer, anxiety and neurotic disorders, psychotic and other mental disorders, porphyria, kidney disease, pancreatitis, gallbladder disease, thrombocytopenia, neutropenia and agranulocytosis, open-angle glaucoma, diabetes mellitus and diabetic ketoacidosis, and benign prostatic hyperplasia.

Two of these are relevant to the predicted uses. Benign prostatic hyperplasia and urinary retention risk are a concern for any bladder-related use of an antimuscarinic. Glaucoma is a concern for ocular use.

**Drug Interactions:** 100 interactions were found; most of those listed are Moderate. Main ones include:
- Other anticholinergic agents: hyoscyamine, aclidinium, amantadine, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine (additive anticholinergic effects)
- Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol (additive sedation)
- Others: botulinum toxin type A, phenylephrine, acebutolol, acetylcholine, loperamide
- Minor: acetaminophen, hydrochlorothiazide

Please refer to the package insert for label warnings, as they were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or literature (evidence level L5). Cauda equina syndrome is a surgical emergency, so any drug effect would be symptomatic only. The data compiled for this report lack label safety information and mechanism data.

<!-- review:begin us-lic-20261106-scopolamine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "All nine US licenses are valid, and the data compiled for this report lack label safety information and mechanism data." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-scopolamine-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- A literature and trial search for scopolamine or antimuscarinics in neurogenic bladder dysfunction related to cauda equina syndrome
- Mapping of the obsolete neurogenic bladder term to a current disease concept
- A comparison with established peripherally acting antimuscarinics, and an assessment of route of administration compatibility (currently pending)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "All nine US licenses are valid, and t" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Transderm Scop (scopolamine) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b877a694-a1d0-4280-937a-a06820b12a88) |
| 2026-11-24 | Corrected: "The nine US license records for scopolamine are all valid." | Corrected | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

