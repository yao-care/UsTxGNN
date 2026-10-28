---
layout: default
title: Desloratadine
parent: Model Prediction Only (L5)
nav_order: 585
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
monitor_inn: "DESLORATADINE"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
description: "Desloratadine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Desloratadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Desloratadine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Desloratadine is a second-generation antihistamine originally used for allergic and vasomotor rhinitis, conjunctivitis and urticaria.
with **2 clinical trials** and **6 publications** currently supporting this direction (3 of the publications are directly on point: 3 randomized controlled trials).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 (see note below) |
| US Market Status | Marketed (valid licenses: 6 of 6) |
| Number of NDAs | 6 (valid: 6) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* the strict L1 definition asks for at least two completed Phase 3 RCTs. The two completed trials here are Phase 4, randomized and double-blind, and are supported by three published RCTs. They were treated as equivalent to L1 for this report, but this is a judgment call.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, desloratadine is a selective peripheral H1-receptor inverse agonist. It blocks the histamine-driven wheal and flare response.

Cold urticaria is a histamine-mediated physical urticaria. Desloratadine is already used for idiopathic and allergic urticaria, so the new indication sits close to existing use. Increasing the dose of second-generation H1 antihistamines is also endorsed by guidelines for patients with cold urticaria who do not respond to the standard dose. The repurposing rationale is therefore mechanistically coherent.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-center, double-blind dose escalation of desloratadine 5, 10 and 20 mg in acquired cold urticaria, to find the dose sufficient to inhibit symptoms |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg vs 20 mg desloratadine on experimentally induced cold urticaria lesions |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomized, placebo-controlled crossover study. High-dose desloratadine decreased wheal volume and improved cold provocation thresholds compared with standard dose in acquired cold urticaria |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized trial of H1-antihistamine dose escalation, using critical temperature threshold measurement in cold urticaria |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | Desloratadine 5 mg for 4 days, tested with ice cubes before and after treatment in 12 patients with cold urticaria |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of the causes, management and treatment options for chronic urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of ebastine (a different antihistamine) in allergic rhinitis and chronic idiopathic urticaria; indirect relevance |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria following black ant bite anaphylaxis; does not involve desloratadine |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021165 | Clarinex (Organon LLC) | Film-coated tablet | Not available |
| ANDA078352 | Desloratadine (A-S Medication Solutions) | Film-coated tablet | Not available |
| ANDA078367 | Desloratadine (Dr. Reddy's Laboratories) | Orally disintegrating tablet | Not available |
| ANDA078355 | Desloratadine (Virtus Pharmaceuticals) | Tablet | Not available |
| ANDA078357 | Desloratadine (Bionpharma) | Film-coated tablet | Not available |

A sixth license, ANDA202936 (Desloratadine Oral Solution, INA Pharmaceutics), is also listed.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** the TxGNN knowledge graph links desloratadine with contraindication signals for hypertension, kidney disease, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and atherosclerosis, angle-closure glaucoma, and hyperthyroidism (Graves disease, thyrotoxicosis). These need to be checked against the official label.
- **Drug Interactions:** 100 potential interactions were identified, but severity levels are unclassified. Examples include calcitriol, phentermine, pantoprazole, doxycycline, morphine, metformin, omeprazole, cimetidine, simvastatin, epinephrine, prednisone and potassium chloride.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed randomized, double-blind Phase 4 trials and three published RCTs directly study desloratadine in cold urticaria, and the dose-escalation approach is guideline-endorsed. The trials are small (30 to 33 patients), and the product's US licenses are all cancelled, so the evidence is promising but not definitive.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Safety review of the higher-than-labeled doses (10 to 20 mg) used in the studies

## Other Predicted Indications (Lower Priority)

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Nasal cavity disease | 0.9987 | L5 | Hold | Largely overlaps with approved rhinitis use; only preclinical literature, none on desloratadine directly |
| Recalcitrant atopic dermatitis | 0.9975 | L5 | Hold | Itch is only partly histamine-dependent; no evidence |
| IgE responsiveness, atopic | 0.9964 | L5 | Hold | A trait rather than a treatable disease |
| Rosacea conjunctivitis | 0.9940 | L5 | Hold | Not primarily histamine-driven; no evidence |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

