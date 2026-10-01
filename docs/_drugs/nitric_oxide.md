---
layout: default
title: Nitric Oxide
parent: Model Prediction Only (L5)
nav_order: 970
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide: From an Approved Inhaled Gas to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Nitric oxide is a marketed inhaled gas product in the US, but the records provided contain no approved-indication text for it.
The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**.
This prediction has **0 clinical trials** and **20 retrieved publications**, none of which studied nitric oxide as an intervention, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitric oxide is a marketed inhaled gas product, but the record provides neither an approved indication nor a mechanism.

The high TxGNN score (0.996) comes from knowledge-graph patterns alone. The retrieved literature covers periodontitis in general (diabetes links, surgical technique, microbiome, guidelines), and none of it involves nitric oxide as a treatment. No biological link between inhaled nitric oxide and this developmental malformation syndrome is supported by the available evidence.

This prediction should therefore be treated as a hypothesis with no supporting rationale, not as a repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 10 publications below were retrieved for the predicted indication. All are about periodontal disease in general, and none tests nitric oxide.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Cochrane systematic review | Cochrane Database Syst Rev | Treating periodontitis for glycaemic control in people with diabetes |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Cochrane systematic review | Cochrane Database Syst Rev | Supportive periodontal therapy for maintaining the dentition after periodontitis treatment |
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guideline | J Clin Periodontol | EFP S3-level clinical practice guideline for stage IV periodontitis |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Two-way relationship between periodontitis and diabetes |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy in periodontitis |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontol 2000 | Sleep disorders, especially obstructive sleep apnea, as a risk factor for periodontal health |
| [37355088](https://pubmed.ncbi.nlm.nih.gov/37355088/) | 2023 | Meta-epidemiological study | J Dent | Age differences in the effects of periodontal treatment in people with diabetes |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Clinical study | J Dent Res | Effect of periodontitis and its treatment on oral and gut microbiota |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Not classified | Periodontol 2000 | Complications and treatment errors in regenerative periodontal surgery |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Not classified | J Dent Res | Role of gingival fibroblasts in the pathogenesis of periodontitis |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA 202860 | GENOSYL (Vero Biotech) | Gas |
| NDA 020845 | INOMAX (INO Therapeutics) | Gas |
| ANDA 207141 | Noxivent 102 (Linde Gas & Equipment) | Gas |

The record lists 8 authorizations in total, and 5 entries were returned. NDA 202860 appears three times. The approved indication text is empty in every entry provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, no nitric oxide-specific literature, and no plausible mechanism for inhaled nitric oxide in a developmental periodontal malformation syndrome.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block the safety screen
- Mechanism of action data (for example from DrugBank)
- Any direct biological evidence linking nitric oxide signalling to this syndrome
- Consideration of the lower-ranked predictions in the same pack. Pulmonary arterial hypertension associated with congenital heart disease (rank 8) has one small completed Phase 3 trial (NCT01959828, n=18) and is scored "Proceed with Guardrails" at evidence level L2. Pulmonary arterial hypertension (rank 7) is L2 but only "Research Question". Pulmonary arteriovenous malformation (rank 6) is L4 and also "Research Question". These are more credible starting points for repurposing work than this rank 1 prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

