---
layout: default
title: Desloratadine
parent: Model Prediction Only (L5)
nav_order: 585
evidence_level: L5
indication_count: 6
---

# Desloratadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Desloratadine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation antihistamine (H1-receptor blocker), marketed in the US as Clarinex and as generics.
The TxGNN model predicts it may be effective for **cold urticaria**,
with **3 completed clinical trials** and **7 publications** (3 of them randomized trials) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data. The label indications (allergic rhinitis, chronic urticaria) are from general knowledge and were not verified against this record. |
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (as assigned by the Evidence Pack). Note that the completed trials are Phase 4, not Phase 3. |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 authorizations in total (1 NDA, Clarinex, plus generic ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on class pharmacology, desloratadine is a selective peripheral H1-receptor inverse agonist. Cold urticaria is a mast-cell-driven physical urticaria: cold exposure triggers histamine release, which produces wheals and itching. Blocking H1 receptors therefore targets the effector pathway directly.

The original indication is also missing from the source record. The drug is generally used for histamine-mediated allergic conditions, so cold urticaria sits in the same disease family. Guidelines cited in the literature recommend increasing doses of non-sedating antihistamines for patients with acquired cold urticaria who do not respond to the standard dose. Trials of desloratadine at up to 20 mg (four times the usual 5 mg dose) have been run specifically for this reason.

This link rests on class pharmacology and the trial evidence, not on the source drug record.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover. Compares 5 mg vs 20 mg desloratadine vs placebo on experimentally induced cold urticaria lesions (thermography, volumetry, photography). Results not in the record. |
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multicenter, double-blind dose-escalation (5, 10, 20 mg) in acquired cold urticaria. Aims to find the dose sufficient to inhibit symptoms. Results not in the record. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Compares the inhibitory effect of 5 antihistamines in urticaria. The population is urticaria broadly, so cold-urticaria-specific efficacy is not confirmed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomized, placebo-controlled crossover study. High-dose desloratadine decreased wheal volume and improved cold provocation thresholds compared with standard dose in acquired cold urticaria. |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized trial of H1-antihistamine dose escalation, measuring the critical temperature threshold. Notes that patient response is variable and hard to predict. |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | 5 mg desloratadine for 4 days, tested by ice-cube challenge before and after treatment in 12 patients with cold urticaria. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of chronic urticaria causes, management and treatment options. General background. |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of ebastine (a different antihistamine) in allergic rhinitis and chronic idiopathic urticaria. Indirect relevance only. |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria following black ant bite anaphylaxis. Background on triggers, no desloratadine data. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case report | J Allergy Clin Immunol Pract | Describes food-dependent cold urticaria as a new variant of physical urticaria. No abstract available. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021165 | Clarinex (Organon LLC) | Tablet, film coated | Not listed in source record |
| ANDA078352 | Desloratadine (A-S Medication Solutions) | Tablet, film coated | Not listed in source record |
| ANDA078367 | Desloratadine (Dr. Reddy's Laboratories) | Tablet, orally disintegrating | Not listed in source record |
| ANDA078355 | Desloratadine (Virtus Pharmaceuticals) | Tablet | Not listed in source record |

A oral solution form is also recorded. ANDA078367 appears twice in the source data with identical details, so it is shown once here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 4 trials, including two dedicated to acquired cold urticaria, and several randomized studies in the literature support high-dose desloratadine for this condition. The mechanism (H1 blockade of histamine-driven wheals) is plausible. However, the evidence comes from small studies (30 to 33 patients in the cold-urticaria trials), and the safety and mechanism data in the source record are missing.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication text, which is empty in every US license record
- Trial results for NCT00600847 and NCT01444196, which are not in the record
- A safety review of doses above the labeled 5 mg (the trials tested up to 20 mg)
- Route and formulation compatibility assessment (currently pending)

The other five predicted indications (nasal cavity disease, acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness, rosacea conjunctivitis) have little or no supporting evidence and are not recommended for further work at this stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

