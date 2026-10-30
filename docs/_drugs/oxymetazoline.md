---
layout: default
title: Oxymetazoline
parent: Model Prediction Only (L5)
nav_order: 1005
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "OXYMETAZOLINE"
predicted_indications: ["nasal cavity disease", "headache disorder"]
description: "Oxymetazoline: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Oxymetazoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Oxymetazoline: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Oxymetazoline is a topical alpha-adrenergic decongestant, originally used for the common cold and pharyngitis.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
but there are currently **0 registered clinical trials** and only **5 indirect publications** (mostly case reports, an animal study, and non-efficacy papers) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 1) |
| Number of FDA Applications | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, oxymetazoline is a topical sympathomimetic that acts as an agonist at alpha-1 and alpha-2 adrenergic receptors (and also binds several serotonin receptors, including 5-HT1B, 5-HT1D and 5-HT2C). Alpha-adrenergic activation constricts blood vessels in the nasal mucosa, which reduces congestion, swelling and mucosal blood flow.

The predicted indication, nasal cavity disease, is a broad category that overlaps heavily with the existing uses (common cold and rhinitis symptoms). It is therefore better viewed as a broad extension of the current use than as a truly novel repurposing. The mechanism is plausible for nasal conditions involving congestion, edema or bleeding, but "nasal cavity disease" is heterogeneous, so no single clinical claim can be supported.

The TxGNN score is very high, but it is a model prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Clinical study | Ann N Y Acad Sci | Effects of acute rhinitis (common cold) on olfactory function in 36 subjects; oxymetazoline is not clearly the studied intervention |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal study (rabbit) | Ann Otol Rhinol Laryngol | Oxymetazoline nose drops tested on local tissue defense in experimental acute sinusitis; preclinical |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Observational | J Plast Surg Hand Surg | Nasal patency measured by acoustic rhinometry after cleft lip and palate repair; indirect relevance |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Procedural report | Am J Rhinol Allergy | Coblation treatment of nasal telangiectasias in hereditary hemorrhagic telangiectasia; oxymetazoline likely an adjunct |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Glob Pediatr Health | Rhinoscleroma in a 9-year-old boy; oxymetazoline likely incidental |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 (cancelled) | Afrin | Spray | Not available |

Other dosage forms recorded for oxymetazoline include aerosol spray, metered spray, jelly and liquid.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): hypertension and other hypertensive disorders, heart disease, cardiovascular disease, coronary artery disease, arteriosclerosis and atherosclerosis, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), eye infections, conjunctivitis, vision disorders and blindness.
- **Drug Interactions**: The interaction query returned 9 records. All are receptor-binding entries rather than drug-drug interactions: 5-HT1B, 5-HT1D, 5-HT2C, alpha-1A/1B/1D and alpha-2A/2B/2C receptors. A literature signal also suggests that sympathomimetics may interact with MAO inhibitors and raise the risk of hypertensive crisis.
- **Other considerations** noted in the evidence review: blood pressure effects and rebound congestion with prolonged use.

Please refer to the package insert for complete safety information, as label-based warnings and contraindications were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but largely overlaps with oxymetazoline's existing use. Supporting evidence is indirect (an animal study, case reports and non-efficacy papers), and no clinical trials are registered. The US product record is cancelled, and label safety data are missing, so a decision to advance is not yet justified.

**To proceed, the following is needed:**
- A specific, well-defined nasal condition to target instead of the broad "nasal cavity disease" category
- FDA package insert warnings and contraindications
- Detailed mechanism of action data
- Controlled clinical evidence for the chosen condition
- A review of cardiovascular risk, MAOI interactions and rebound congestion with prolonged use

---

### Other Predicted Indications (for reference)

- **Headache disorder** (score 0.9904, L4, Research Question): The most relevant paper is [PMID 31919839](https://pubmed.ncbi.nlm.nih.gov/31919839/) (2020, *Headache*), a study of intranasal 3% tetracaine plus 0.05% oxymetazoline in status migrainosus. It is a combination product and its design is unverified, so effects cannot be attributed to oxymetazoline alone. The other papers are a case report and non-efficacy reviews.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

