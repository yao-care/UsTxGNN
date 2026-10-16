---
layout: default
title: Fedratinib
parent: Model Prediction Only (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
monitor_inn: "FEDRATINIB"
predicted_indications: ["benign PEComa", "lymphangiomyoma", "uterine corpus perivascular epithelioid cell tumor", "dermatofibrosarcoma protuberans", "rhabdoid tumor", "familial rhabdoid tumor", "autosomal recessive familial Mediterranean fever", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "lymphangioleiomyomatosis"]
---

# Fedratinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Fedratinib: From Myelofibrosis to Benign PEComa

## One-Sentence Summary

Fedratinib is an oral kinase inhibitor originally used to treat primary myelofibrosis and myelofibrosis.
The TxGNN model predicts it may be effective for **benign PEComa**,
but **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary myelofibrosis, myelofibrosis (from the knowledge graph; no approved-indication text is available in the US license record) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single NDA is marked cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fedratinib is a JAK2 inhibitor (with additional FLT3 and BRD4 activity). Its efficacy in myelofibrosis, a disease driven by dysregulated JAK/STAT signaling, is the basis of its original use.

PEComas are typically driven by mTOR pathway activation through TSC1/TSC2 loss. No direct link between JAK2 inhibition and mTOR-driven biology is established in the data compiled for this report, so the mechanistic connection is weak and speculative. The high TxGNN score reflects a knowledge-graph pattern, not demonstrated biology.

The other top predictions share this limitation. Several are mTOR-related (lymphangiomyoma, uterine PEComa, lymphangioleiomyomatosis), where sirolimus is the established therapy. Two others are rhabdoid tumor entities, where a BRD4/epigenetic rationale is conceivable but untested. The two hemophagocytic lymphohistiocytosis (HLH) predictions have the most plausible class rationale (JAK/STAT cytokine signaling, with ruxolitinib as precedent), but no fedratinib-specific data exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA212327 (cancelled) | Inrebic (Celgene Corporation) | Capsule | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC, liver function, and renal function for kinase inhibitors) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database; the first 20 reviewed are mostly Moderate. The **Major** interactions among them are:
  - Dexamethasone
  - Clarithromycin
  - Eliglustat
  - Naloxegol
  
  Moderate interactions include proton pump inhibitors (omeprazole, rabeprazole, lansoprazole), cimetidine, aprepitant, naltrexone, saxagliptin, and several corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide).

- **Boxed warning (from general knowledge, not the compiled data)**: Fedratinib is known to carry a boxed warning for encephalopathy, including Wernicke's. This is a particular concern for the critically ill patients seen in HLH. It should be verified against the current package insert.

The package insert warnings and contraindications were not available and must be obtained before any safety screening.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5), with no clinical trials or publications, a weak mechanistic link to mTOR-driven PEComa biology, and a cancelled US NDA.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence of fedratinib activity in PEComa or TSC/mTOR-driven models
- A literature and trial search, and a comparison against established therapies (e.g., sirolimus for mTOR-driven diseases)
- Consideration of the HLH predictions as a more mechanistically plausible alternative, after assessing the safety profile in that setting
- Clarification of the current US regulatory status of fedratinib, since the compiled record shows only a cancelled NDA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

