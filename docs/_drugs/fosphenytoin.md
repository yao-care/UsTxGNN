---
layout: default
title: Fosphenytoin
parent: Model Prediction Only (L5)
nav_order: 739
evidence_level: L5
indication_count: 7
monitor_inn: "FOSPHENYTOIN"
predicted_indications: ["conjunctivitis", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "manic bipolar affective disorder", "idiopathic granulomatous myositis", "myositis fibrosa", "fibromyalgia"]
last_modified_at: 2026-10-14
description: "Fosphenytoin: predicted new indication Conjunctivitis (evidence level L5). Approved use: Epilepsy, status epilepticus"
---

# Fosphenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Fosphenytoin: From Epilepsy to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fosphenytoin is a water-soluble prodrug of phenytoin, originally used to treat epilepsy and status epilepticus.
The TxGNN model predicts it may be effective for **conjunctivitis**,
but **no clinical trials** and **no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, status epilepticus |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 6 (1 NDA and 5 ANDAs, all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, fosphenytoin is converted in the body to phenytoin, which blocks voltage-gated sodium channels and stabilizes neuronal membranes. This is the basis of its efficacy in epilepsy and status epilepticus.

For conjunctivitis, however, there is no clear mechanistic link. Conjunctivitis is typically infectious or allergic, and no plausible sodium-channel-mediated pathway is evident. The high TxGNN score reflects a pattern in the knowledge graph rather than a demonstrated biological rationale, and it should be read as a hypothesis-generating signal only.

### Other Predicted Indications Reviewed

Other predictions were also reviewed. All have lower evidence than would be needed to advance:

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Nephrogenic syndrome of inappropriate antidiuresis | 99.28% | L5 | The condition is caused by gain-of-function mutations in the vasopressin V2 receptor; sodium-channel blockade does not address this. No evidence. |
| Tourette syndrome | 99.22% | L5 | Involves dopaminergic and cortico-striatal circuit dysregulation; no direct evidence for fosphenytoin. |
| Manic bipolar affective disorder | 99.18% | L4 | Other anticonvulsants are effective in mania, and one 2003 publication on intravenous fosphenytoin in acute mania exists. Design and sample size are unverified. This is the most plausible of the predictions as a research question. |
| Idiopathic granulomatous myositis | 99.02% | L5 | An immune-mediated myopathy; fosphenytoin has no relevant immunomodulatory action, and phenytoin can itself cause myopathy or hypersensitivity. |
| Myositis fibrosa | 99.02% | L5 | No known mechanism; the score is likely driven by shared graph neighbors with granulomatous myositis. |
| Fibromyalgia | 99.02% | L5 | Pregabalin and gabapentin act through a different mechanism (α2δ calcium-channel subunit); phenytoin-class agents have no established benefit. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for conjunctivitis.

For the manic bipolar affective disorder prediction, one publication was identified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/) | 2003 | Preliminary clinical study / case-level report (design unverified) | The Journal of Clinical Psychiatry | Tested the hypothesis that high-dose intravenous phenytoin delivered as fosphenytoin, which has fewer cardiac and local vein side effects, might act rapidly against acute mania. Results are not available in the abstract provided. |

---

## US Market Information

All six US authorizations are cancelled, so there is currently no actively marketed fosphenytoin product in the data compiled for this report. Approved indication text is not available for these entries.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020450 | CEREBYX (Pfizer) | Injection, solution | Not available (cancelled) |
| ANDA214926 | Fosphenytoin sodium (Glenmark) | Injection, solution | Not available (cancelled) |
| ANDA078765 | Fosphenytoin sodium (West-Ward) | Injection, solution | Not available (cancelled) |
| ANDA077989 | Fosphenytoin sodium (Hikma) | Injection | Not available (cancelled) |
| ANDA078476 | Fosphenytoin sodium (Amneal) | Injection | Not available (cancelled) |

---

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for safety information.

**Contraindication signals from the knowledge graph** (not label text, so they should be verified against the label):
- **Cardiac:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, Adams-Stokes syndrome
- **Hematologic:** thrombocytopenia, leukopenia, pancytopenia, agranulocytosis, neutropenia (including congenital forms)
- **Organ disease:** kidney disease, liver disease, gallbladder disease
- **Other:** systemic lupus erythematosus, hypotensive disorder, substance abuse/dependence, hyperphosphatemia, lymphatic system disease

**Drug Interactions:** 100 interactions were recorded. Examples from the listed entries:
- **Major:** cimetidine, eliglustat
- **Moderate:** acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, betamethasone, clarithromycin, aprepitant, canagliflozin, and others
- **Minor:** acetylsalicylic acid

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The conjunctivitis prediction has a high model score but no clinical trials, no literature, and no plausible mechanistic link (Level L5). All US authorizations are cancelled, which further limits practical development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- A mechanistic or preclinical rationale for fosphenytoin in conjunctivitis, plus a route assessment (the drug is available only as an injection, and a conjunctival indication would likely need a different formulation)
- If a lead is desired, consider the manic bipolar disorder signal as a research question: obtain the full text of PMID 12716241 to verify its design and results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

