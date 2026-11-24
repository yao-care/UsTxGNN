---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 1192
evidence_level: L5
indication_count: 8
monitor_inn: "Tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-11-24
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). In the US: 52 FDA applications (44 active), plus 1 OTC monograph/unapproved NDC listing"
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Tadalafil: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia, and pulmonary hypertension.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **0 clinical trials** and **0 publications** currently support this direction. The prediction is a model output only, and it may reflect an adverse-effect association rather than a therapeutic one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 44 of 52; OTC monograph / unapproved listings: 1) |
| Number of FDA Applications | 52 (active: 44) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for tadalafil: "Penile erection during sexual stimulation is caused by increased penile blood flow resulting from the relaxation of penile arteries and corpus cavernosal smooth muscle. This response is mediated by the release of nitric oxide (NO) from nerve terminals and endothelial cells, which stimulates the synthesis of cGMP in smooth muscle cells. […] Tadalafil inhibits PDE5." ([DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895), label version 2026-06-03; accessed 2026-11-19.) Tadalafil is generally known as a PDE5 inhibitor that raises cGMP and causes vasodilation. Its efficacy in erectile dysfunction and pulmonary hypertension is established.

The predicted disease is a congenital condition driven by genetic (chromosomal or regulatory) abnormalities, and a biological link to PDE5 inhibition is not evident. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Hypertrichosis is a known adverse effect of vasodilators such as minoxidil, so the association may point in the wrong direction (inducing rather than treating). The therapeutic rationale is unsupported.

The other top-ranked predictions show the same pattern, and the compiled data provides no evidence for any of them:
- Hypertrichosis (0.9998): likely a shared vasodilatory or cGMP-pathway signal, with an unclear direction of effect.
- Malformation syndrome with odontal and/or periodontal component (0.9997): no plausible mechanism.
- Syndrome with a Dandy-Walker malformation as major feature (0.9997): a structural brain anomaly that a PDE5 inhibitor would not be expected to reverse.
- Isolated genetic hair shaft abnormality (0.9996): no established rationale.
- Familial isolated trichomegaly (0.9965): a genetic trait with no plausible therapeutic mechanism.
- Kyphoscoliotic heart disease (0.9943): the most biologically plausible, because kyphoscoliosis can cause chronic hypoxia and secondary pulmonary hypertension. This is a hypothesis only and has not been tested.
- Migraine with brainstem aura (0.9908): the only evidence is a case report suggesting tadalafil may trigger aura (an adverse-event signal).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the only publication found among the top predictions relates to migraine with brainstem aura (rank 8):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache, an adverse-event signal rather than evidence of benefit |

## US Market Information

Five of them are shown below.

<!-- review:begin us-lic-20261105-tadalafil-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 11 US licenses are valid, and none has approved-indication text on record. Five of them are shown below." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-05). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261105-tadalafil-1 -->

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| ANDA090141 | TADALAFIL | TEVA PHARMS USA | Tablet; oral | Valid |
| ANDA204809 | TADALAFIL | ALEMBIC | Tablet; oral | Valid |
| ANDA205885 | TADALAFIL | WATSON LABS INC | Tablet; oral | Valid |
| ANDA206285 | TADALAFIL | AUROBINDO PHARMA LTD | Tablet; oral | Valid |
| ANDA206286 | TADALAFIL | AUROBINDO PHARMA LTD | Tablet; oral | Valid |

Showing 5 of 53 entries (FDA applications first, active before discontinued; NDC listings without an FDA application last).

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** liver failure, epilepsy, aortic stenosis and other aortic valve disease, hypotensive disorder, blood coagulation disease, acute coronary syndrome, myocardial infarction, stroke and other cerebrovascular disorders, sickle cell anemia and other hemoglobinopathies, plasma cell myeloma, leukemia, priapism, Peyronie disease, hearing loss disorders, and hypertrophic cardiomyopathy.
- **Drug Interactions:** 100 interactions were found in total. The main moderate-level ones include aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole, clotrimazole, lorcaserin, sapropterin, troglitazone, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Papaverine is a minor interaction.
- **Additional signal:** A case report linked tadalafil to migraine aura, which should be noted in any neurological indication work.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or publications (Evidence Level L5). The biological rationale is weak, and the signal may reflect an adverse-effect association (hypertrichosis from vasodilation) rather than a therapeutic one. The drug is marketed in the US, but the official safety label data is missing.

<!-- review:begin us-lic-20261106-tadalafil-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the US with 11 valid licenses, but the official safety label data is missing." Removed: the number or status of FDA applications stated here did not match the FDA data after applications were matched by ingredient (Drugs@FDA and the NDC Directory as of 2026-11-06). The current number of FDA applications and NDC listings for this drug is shown in the Quick Overview and in the table under US Market Information. Source: [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/).

<!-- review:end us-lic-20261106-tadalafil-2 -->

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- FDA package insert warnings and contraindications, needed for safety screening
- A literature review to clarify the direction of effect for hypertrichosis (therapeutic vs. adverse)
- Consider a targeted review of PDE5 inhibitors in secondary pulmonary hypertension, which could assess kyphoscoliotic heart disease, the most plausible of the predictions
- Confirmation of current US market and licensing status

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official FDA data (Drugs@FDA, the NDC Directory, or DailyMed labeling). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 11 US licenses are valid, and none has approved-indication text on record" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-06 | Removed: "with 11 valid licenses" | Corrected (revised 2026-11-24; earlier version kept in the record) | [openFDA Drugs@FDA](https://open.fda.gov/data/drugsfda/); [openFDA NDC Directory](https://open.fda.gov/data/ndc/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

