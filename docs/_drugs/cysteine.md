---
layout: default
title: Cysteine
parent: Model Prediction Only (L5)
nav_order: 561
evidence_level: L5
indication_count: 7
monitor_inn: "CYSTEINE"
predicted_indications: ["dry eye syndrome", "closed-angle glaucoma", "nasal cavity disease", "acute laryngopharyngitis", "pharyngitis", "exercise-induced malignant hyperthermia", "angle-closure glaucoma"]
last_modified_at: 2026-10-14
description: "Cysteine: predicted new indication Dry eye syndrome (evidence level L5). Approved use: Bronchitis, paracetamol poisoning, cystic fibrosis, bronchiectasis…"
---

# Cysteine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cysteine: From Bronchitis and Mucus-Related Conditions to Dry Eye Syndrome

## One-Sentence Summary

Cysteine is an amino acid used in injectable and liquid products. Its original indications in the knowledge graph include bronchitis, paracetamol poisoning, cystic fibrosis, bronchiectasis and amyloidosis.
The TxGNN model predicts it may be effective for **dry eye syndrome**, but there are **0 clinical trials** and only **preclinical literature** in which cysteine serves mainly as a component of a delivery system or prodrug.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, paracetamol poisoning, cystic fibrosis, bronchiectasis, amyloidosis (from the knowledge graph; no approved indication text is available for the US licenses) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cysteine is a thiol-containing amino acid. Its mucolytic and antioxidant properties are consistent with its original respiratory indications and may be applicable to dry eye.

The literature compiled for this report suggests two possible links:

- **Thiol chemistry for mucoadhesion.** Cysteine provides thiol groups used in thiolated polymers (thiomers), such as thiolated chitosan. These bind mucus and improve retention on the ocular surface.
- **Antioxidant and persulfide activity.** Excess reactive oxygen species (ROS) and NLRP3 inflammasome activation drive inflammation in dry eye. Cysteine-derived persulfide/H2S donors may counter this.

In the retrieved studies, cysteine is a building block of a delivery system or prodrug, not a stand-alone therapy. No study tested cysteine itself as a dry eye treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The most relevant publications are listed below. All are preclinical or review-level, and no RCTs were found. Many of the 20 retrieved papers concern Sjögren's syndrome biology or are only loosely related, so they are not listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Advanced Materials | Eye-drop nanoformulation of catalase self-assembled with cysteine-modified chitosan, designed to remove excess ROS in dry eye disease |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical | Int J Biol Macromol | Chondroitin sulfate–L-cysteine conjugate on lipid carriers improved corneal retention and permeation of dexamethasone |
| [41485487](https://pubmed.ncbi.nlm.nih.gov/41485487/) | 2026 | Preclinical | J Control Release | Superoxide-responsive persulfide prodrug designed to eliminate ROS in dry eye |
| [26606856](https://pubmed.ncbi.nlm.nih.gov/26606856/) | 2015 | Preclinical | Ther Deliv | Hyaluronic acid modified with cysteine ethyl ester evaluated as a mucoadhesive lubricant |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Review | J Control Release | Review of thiolated polymers (thiomers) and their improved mucoadhesion |
| [31028759](https://pubmed.ncbi.nlm.nih.gov/31028759/) | 2019 | Review | Adv Drug Deliv Rev | Review of thiolated polymers and their disulfide bonding with mucus and membrane proteins |
| [36626177](https://pubmed.ncbi.nlm.nih.gov/36626177/) | 2023 | Preclinical | Invest Ophthalmol Vis Sci | Aquaporin 5 deficiency worsens ROS/NLRP3-mediated pyroptosis in lacrimal glands |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Preclinical/observational | Exp Eye Res | ROS-activated NLRP3 inflammasomes drive inflammation in hyperosmolarity-stressed corneal cells and dry eye patients |
| [24836981](https://pubmed.ncbi.nlm.nih.gov/24836981/) | 2014 | Preclinical | Exp Eye Res | ROS-activated NLRP3 inflammasomes prime inflammation in a murine dry eye model |

## US Market Information

All three US licenses are cancelled, and the data compiled for this report contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| NDA212535 | Cysteine Hydrochloride (Baxter Healthcare) | Injection | Cancelled |
| NDA210660 | ELCYS (Exela Pharma Sciences) | Injection, solution | Cancelled |
| Not available | L-Cysteine (Professional Complementary Health Formulas) | Liquid | Cancelled |

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

The knowledge graph links cysteine to the following conditions as potential contraindications. These come from graph data, not label text, and should be verified:

- Peptic ulcer disease (including active peptic ulcer disease)
- Hypotensive disorder
- Respiratory failure
- Asthma and bronchial disease
- Esophageal varices
- Phenylketonuria and other disorders of phenylalanine metabolism

No drug interaction data were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for dry eye is very high, but supporting evidence is limited to preclinical formulation and mechanism studies, with no clinical trials. In these studies cysteine acts as a component of a delivery system or prodrug, not as a stand-alone treatment. All US licenses are cancelled, and no label safety data are available.

Other predicted indications are weaker:

- **Closed-angle glaucoma and angle-closure glaucoma** (duplicate entries): the literature concerns SPARC, a cysteine-rich protein, so the link is incidental. Evidence level L5.
- **Nasal cavity disease and pharyngitis**: only indirect support from N-acetylcysteine, a derivative. These include a 1996 small nasal resistance study in healthy volunteers and an in vitro tonsil biofilm study. Evidence level L4.
- **Acute laryngopharyngitis and exercise-induced malignant hyperthermia**: prediction only, with no relevant evidence. Evidence level L5.

**To proceed, the following is needed:**
- Mechanism of action data for cysteine
- FDA package insert warnings and contraindications, to complete the safety screen
- Direct evidence for cysteine itself in dry eye, such as animal efficacy studies of cysteine or N-acetylcysteine eye drops
- A decision on whether a topical ocular formulation is feasible, since the former US products were injectable or liquid and route compatibility has not been assessed
- Confirmation of the contraindications flagged in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

