---
layout: default
title: Guaifenesin
parent: Moderate Evidence (L3-L4)
nav_order: 763
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Guaifenesin: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "GUAIFENESIN"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
---

# Guaifenesin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

## Guaifenesin: From Upper Respiratory Conditions (Rhinitis, Common Cold) to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Guaifenesin is an expectorant originally associated with upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be useful for **nasal cavity disease**,
but there are currently **no registered clinical trials** and only **1 publication** (a narrative review), so the prediction rests mainly on the model score and biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; no approved indication text is available in the US licence records) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (all licences cancelled) |
| Number of NDAs | 8 licences in total (1 NDA, 7 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, guaifenesin is an expectorant that thins and loosens airway mucus. This could plausibly relieve mucus retention in the nose and upper airway.

The original indications (allergic rhinitis, vasomotor rhinitis, rhinitis, nasopharyngitis, common cold) are closely related upper respiratory conditions that involve the nasal cavity. This anatomical and clinical proximity makes the predicted indication biologically plausible.

This link is inferred from the drug class and has not been confirmed. The very high TxGNN score is a computational prediction only and does not establish efficacy.

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Acute laryngopharyngitis | 99.98% | L5 | Adjacent to pharyngitis and the common cold; no trials or literature |
| 3 | Faucial diphtheria | 99.54% | L5 | Toxin-mediated bacterial infection; guaifenesin has no antibacterial or antitoxin activity, so the signal likely reflects graph association only |
| 4 | Cervical disc degenerative disorder | 99.50% | L5 | No plausible mechanistic link identified; any signal is speculative |
| 5 | Papillary conjunctivitis | 99.27% | L5 | No clear ocular mechanism; may reflect association with allergic rhinitis |

All four have a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Discusses treatment of hidden respiratory allergies in voice users. Notes that antihistamines are generally avoided, that decongestants containing guaifenesin may be useful, and that steroids (nasal, inhaled or systemic) are helpful, especially for perennial allergic symptoms. |

This is a narrative review with indirect relevance, not controlled evidence of efficacy in nasal cavity disease.

## US Market Information

All 8 licences are cancelled; no currently valid licences were found. Approved indication text is not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Status |
|---------|------|------|-----------|
| ANDA213420 | Mucus Relief (NUVICARE LLC) | Tablet, extended release | Cancelled |
| M012 | Guaifenesin (PAI Pharma) | Solution | Cancelled |
| ANDA207342 | Mucus Relief (Best Choice) | Tablet | Cancelled |
| ANDA217780 | Guaifenesin 1200 mg (Marksans Pharma) | Tablet | Cancelled |
| ANDA078912 | Mucus and Chest Congestion (CVS) | Tablet, multilayer, extended release | Cancelled |

Three further cancelled licences are not listed here, including NDA021282 (Mucinex, Bryant Ranch Prepack).

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the compiled data. Please refer to the package insert for safety information.

The knowledge graph lists the following conditions as contraindication-related associations for guaifenesin. These come from graph edges, not label text, and should be verified against the official label before any use:
- **Cardiovascular:** hypertension
- **Hepatic and renal:** liver failure, liver disease, cirrhosis of liver, kidney disease
- **Respiratory:** chronic obstructive pulmonary disease
- **Gastrointestinal and biliary:** gastric ulcer, peptic ulcer disease, inflammatory bowel disease, pancreatitis, gallbladder disease
- **Neuropsychiatric:** epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder
- **Metabolic and endocrine:** inherited porphyria / porphyria, hypothyroidism, myxedema, congenital hypothyroidism, adrenocortical insufficiency, Addison disease
- **Haematological:** thrombocytopenia
- **Other:** pyoureter

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible because guaifenesin is a mucus-thinning agent and nasal cavity disease is closely related to its original indications. However, there are no clinical trials, only one indirect narrative review, and no mechanism of action or label safety data. All US licences are cancelled. The evidence does not yet support moving forward.

**To proceed, the following is needed:**
- Obtain the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank
- Clarify which specific nasal cavity conditions are targeted, and search for controlled studies in them
- Clarify the reasons for licence cancellation and the current regulatory pathway (e.g., OTC availability)
- Verify the knowledge-graph contraindication associations against the official label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

