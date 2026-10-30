---
layout: default
title: Triprolidine
parent: Model Prediction Only (L5)
nav_order: 1266
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "TRIPROLIDINE"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
description: "Triprolidine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Triprolidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Triprolidine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Triprolidine is a first-generation H1-receptor antihistamine, originally used for allergic and vasomotor rhinitis, the common cold, allergic conjunctivitis, urticaria and angioedema.
but **no clinical trials** and only **2 indirect publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, triprolidine is a first-generation H1-receptor antagonist. Its efficacy in histamine-mediated conditions such as allergic rhinitis is established, and urticaria and angioedema are already among its listed original indications.

Allergic urticaria is driven by histamine release, so H1 blockade is mechanistically coherent. This is essentially an extension within an existing indication class rather than a true repurposing. The prediction mainly confirms a known drug-class effect and does not point to a new therapeutic area.

The other predicted indications are weaker:
- **Pharyngitis** (0.9982): any benefit would be symptomatic only (reduced rhinorrhea and congestion), not treatment of the underlying infection.
- **Nasal cavity disease**, **acute laryngopharyngitis**, **recalcitrant atopic dermatitis** and **IgE responsiveness, atopic**: no supporting trials or literature. Some are overly broad or non-disease terms, and H1 blockade does not address the drivers of atopic dermatitis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2568212](https://pubmed.ncbi.nlm.nih.gov/2568212/) | 1989 | Review | Clinical Pharmacy | Review of non-sedating H1 antagonists (terfenadine, astemizole, loratadine, acrivastine). Acrivastine is a metabolite of triprolidine. Indirect, class-level information only. |
| [14283425](https://pubmed.ncbi.nlm.nih.gov/14283425/) | 1965 | Experimental study | British Journal of Dermatology | Study of triprolidine and skin response to UV radiation. Not a trial in urticaria. |

Evidence for other predicted indications (all indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | RCT (comparators only) | Dermatologica | Double-blind crossover trial in 18 patients with idiopathic cold urticaria. Acrivastine (a triprolidine derivative) and cyproheptadine reduced weal areas versus placebo, and acrivastine was more effective. Triprolidine itself was not studied. |
| [6377256](https://pubmed.ncbi.nlm.nih.gov/6377256/) | 1984 | RCT | Pediatric Infectious Disease | Double-blind, placebo-controlled trial in 142 children with purulent nasopharyngitis, comparing cephalexin alone or with pseudoephedrine/triprolidine. The role of triprolidine is unconfirmed. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 (cancelled) | HISTEX | Syrup | Not listed |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** hypertension, coronary artery disease and myocardial infarction, heart conduction disease, epilepsy, kidney and liver disease, pancreatitis, gallbladder disease, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, diabetes and diabetic ketoacidosis, benign prostatic hyperplasia, ocular hypertension, and others.
- **Drug Interactions:** the interaction query found 100 interacting drugs in total.
  - **Major:** potassium citrate and potassium chloride.
  - **Moderate** (anticholinergic, opioid or cannabinoid additive effects): hyoscyamine, atropine, scopolamine, glycopyrronium, dicyclomine, trospium, loperamide, morphine, metoclopramide, dronabinol, nabilone and eluxadoline, among others.

The official package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is indirect. There are no triprolidine-specific trials, and the only literature concerns related drugs or is a historical study. Allergic urticaria also largely overlaps with the drug's existing indications, so there is little true repurposing value. The only US license is cancelled, and the label safety data needed for screening are missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Triprolidine-specific clinical evidence in urticaria, or a clear regulatory rationale for why the existing indication does not already cover it
- Confirmation of current US marketing status and available formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

