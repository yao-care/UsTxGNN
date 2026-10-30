---
layout: default
title: Besifloxacin
parent: Model Prediction Only (L5)
nav_order: 453
evidence_level: L5
indication_count: 8
monitor_inn: "BESIFLOXACIN"
predicted_indications: ["bronchitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa"]
last_modified_at: 2026-10-30
description: "Besifloxacin: predicted new indication Bronchitis (evidence level L5). Approved use: Conjunctivitis"
---

# Besifloxacin
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

## Besifloxacin: From Conjunctivitis to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Besifloxacin is a fluoroquinolone antibiotic, originally used as an ophthalmic suspension for bacterial conjunctivitis.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting this specific direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Conjunctivitis; acute contagious conjunctivitis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, besifloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Activity against respiratory bacterial pathogens is therefore biologically plausible.

There are important limits on this rationale. Besifloxacin exists only as an ophthalmic suspension with minimal systemic exposure, and no systemic or inhaled formulation is available. Most bronchitis cases are viral, which further weakens the case for an antibacterial. The very high TxGNN score reflects model output, not clinical evidence.

Other predictions were also reviewed. Most are mechanistically weak, because they are immune-mediated or toxin-mediated conditions (postinfectious vasculitis, post-infectious syndrome, infection-related hemolytic uremic syndrome), anatomical or fibrotic (infective urethral stricture), or parasitic (Chagas cardiomyopathy). **Otitis externa** (score 0.9903) is the most mechanistically plausible, because topical fluoroquinolones are established treatments for it. However, no otic formulation or trial exists for besifloxacin.

## Clinical Trial Evidence

Currently no clinical trials are registered for bronchitis, the top predicted indication.

For reference, one trial is linked to a lower-ranked prediction ("post-bacterial disorder"). It is a safety and exposure study in the original conjunctivitis context, not an efficacy test of the predicted indication:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00407589](https://clinicaltrials.gov/study/NCT00407589) | Phase 1 | Completed | 24 | Systemic pharmacokinetics after single and multiple ocular instillations in suspected bacterial conjunctivitis; shows low systemic exposure, which argues against systemic repurposing |

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022308 | Besivance (Bausch & Lomb Americas Inc.) | Suspension | Not specified in the compiled data (license status: valid) |

## Cytotoxicity

Not applicable. Besifloxacin is an antibacterial, not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph lists "superimposed infection" (an obsolete term) as a contraindication. This comes from graph edges, not label text.
- **Predicted-indication concern**: For infection-related hemolytic uremic syndrome, antibiotics including fluoroquinolones may increase toxin release and risk. This is a safety concern, not a therapeutic rationale.

No drug interaction records were found. For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests only on a model score, with no trials or literature. The drug is available only as an ophthalmic suspension with minimal systemic exposure, and its only US license is cancelled. Most bronchitis is viral. All eight predicted indications remain at evidence level L5.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- In vitro susceptibility data against bronchitis-relevant bacterial pathogens
- A feasible systemic or inhaled formulation, with a route compatibility assessment
- If a lead indication is pursued, consider otitis externa instead, which would require otic formulation feasibility work and susceptibility data against *Pseudomonas aeruginosa* and *Staphylococcus aureus*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

