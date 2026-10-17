---
layout: default
title: Emapalumab
parent: Model Prediction Only (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Emapalumab: predicted new indication Autosomal recessive familial Mediterranean fever (evidence level L5). Approved use: Hemophagocytic lymphohistiocytosis / hemophagocytic syndrome"
monitor_inn: "EMAPALUMAB"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "hepatic infarction", "hepatic veno-occlusive disease", "X-linked lymphoproliferative disease due to SH2D1A deficiency", "familial Mediterranean fever", "A20 haploinsufficiency", "immune dysregulation with inflammatory bowel disease", "peliosis hepatis"]
---

# Emapalumab
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

# Emapalumab: From Hemophagocytic Lymphohistiocytosis to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Emapalumab is an interferon-gamma (IFN-γ)-neutralizing antibody, originally used for hemophagocytic lymphohistiocytosis (HLH).
The TxGNN model predicts it may be effective for **autosomal recessive familial Mediterranean fever (FMF)**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophagocytic lymphohistiocytosis / hemophagocytic syndrome |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (per the data compiled for this report) |
| Number of NDAs | 1 (a BLA, BLA761107) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Emapalumab is a monoclonal antibody that neutralizes IFN-γ. Detailed mechanism-of-action data were not available in the compiled drug record, but this role is the basis of its use in HLH, a hyperinflammatory syndrome driven by excess IFN-γ.

The link to FMF is weak. FMF is driven mainly by pyrin inflammasome activation and overproduction of IL-1β. Its established treatments (colchicine and IL-1 inhibitors) act on that pathway rather than on IFN-γ. One possible niche is macrophage activation syndrome complicating FMF, which does involve IFN-γ, but nothing in the data supports it. The high TxGNN score is therefore a computational signal, not a mechanistically or clinically validated one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761107 | GAMIFANT (Swedish Orphan Biovitrum AB) | Injection | — (no indication text in the data; the drug's original indication is HLH) |

The only authorization is listed with a **cancelled** status. This should be verified against the current FDA record before any decision relies on it.

## Safety Considerations

- **Drug Interactions**: 76 interactions were identified. The 20 reviewed are all rated Moderate. Notable groups include:
  - Anticoagulants: warfarin, dicoumarol, apixaban, rivaroxaban
  - Statins: simvastatin, atorvastatin
  - Opioids: fentanyl, hydrocodone, benzhydrocodone
  - Xanthines: theophylline, aminophylline, oxtriphylline
  - Cardiovascular drugs: amiodarone, amlodipine, nifedipine
  - Others: lidocaine, alprazolam, fosphenytoin, ethinylestradiol, norethisterone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and IFN-γ blockade has only a loose connection to the IL-1-driven biology of FMF. Evidence is limited to a model score (L5), and the label safety data are not available for review.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking IFN-γ to FMF, for example in macrophage activation syndrome complicating FMF
- Detailed mechanism-of-action data and the FDA package insert warnings and contraindications
- Confirmation of the current US regulatory and marketing status of GAMIFANT

**Note on other predictions:** Among the other TxGNN predictions for this drug, **hemophagocytic syndrome associated with an infection** has the most supporting material (score 99.99%, L4, "Research Question"). It has about 20 publications, including case series on EBV-associated HLH, reviews, and the pivotal primary HLH study (PMID 32374962), but no registered trials. **Malignancy-associated HLH** is also supported indirectly by a 2026 real-world study (PMID 41337692, REAL-HLH). Both are biologically closer to the original HLH indication, and either would be a stronger candidate than FMF for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

