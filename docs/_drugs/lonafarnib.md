---
layout: default
title: Lonafarnib
parent: Model Prediction Only (L5)
nav_order: 868
evidence_level: L5
indication_count: 1
monitor_inn: "LONAFARNIB"
predicted_indications: ["leprosy"]
last_modified_at: 2026-10-30
description: "Lonafarnib: predicted new indication Leprosy (evidence level L5). Approved use: Not stated in the data compiled for this report"
---

# Lonafarnib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lonafarnib: From Progeria (Original Approval) to Leprosy
{: .text-alpha }

## One-Sentence Summary

Lonafarnib is an oral farnesyltransferase inhibitor, marketed in the US as Zokinvy (NDA213969).
The TxGNN model predicts it may be effective for **leprosy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the license record has no indication text) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lonafarnib is a farnesyltransferase inhibitor (FTI). It blocks farnesylation, a protein modification that anchors certain proteins to cell membranes. Detailed mechanism of action data is not available in the compiled record. This description is general pharmacological knowledge, not drawn from the supplied data.

The data compiled for this report does not establish a direct mechanistic link between lonafarnib and *Mycobacterium leprae* infection. One speculative hypothesis is that host prenylated small GTPases (Ras/Rho family), which are involved in macrophage function, phagocytosis and inflammatory signaling, could be modulated. No evidence in the record supports this. The high TxGNN score (0.9914) is a model-based prediction only and should not be read as clinical evidence. The model's rank for this prediction is 18,762, which further suggests treating it with caution.

The original indication is not recorded in the data, so the relationship between the original and predicted indications cannot be assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213969 (Cancelled) | Zokinvy (Sentynl Therapeutics, Inc.) | Capsule (oral) | Not listed in the compiled record |

## Cytotoxicity

Lonafarnib has been studied in oncology, but it is not classified here as a conventional cytotoxic drug, and the compiled record contains no antineoplastic classification or toxicity data. Please refer to the package insert warnings and precautions.

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 interacting drugs. The 20 entries shown include many Major-level interactions:
  - Major: loperamide, aprepitant, triamcinolone, dexamethasone, budesonide, cimetidine, clarithromycin, eliglustat, naloxegol.
  - Moderate: hydrocortisone, omeprazole, betamethasone, chlorpropamide, saxagliptin, empagliflozin, oxandrolone, naldemedine, and the ophthalmic forms of hydrocortisone, dexamethasone and prednisolone.
  - Many of the Major interactions involve corticosteroids or drugs metabolized through common pathways, so concomitant medications need careful review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no supporting clinical trials or literature (evidence level L5), and no mechanistic link to *M. leprae* is established. The US license is also cancelled, and the package insert safety data is missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (download from the FDA website)
- Mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic studies testing whether farnesyltransferase inhibition affects *M. leprae* infection or host macrophage response
- A literature and trial search specific to leprosy
- Route compatibility assessment against the oral capsule form
- A review of the high number of major drug interactions for the likely leprosy treatment setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

