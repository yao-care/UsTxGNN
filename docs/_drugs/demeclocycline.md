---
layout: default
title: Demeclocycline
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 3
---

# Demeclocycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Demeclocycline: From Tetracycline Antibiotic to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Demeclocycline is a tetracycline-class antibiotic that is marketed in the US as oral tablets. The TxGNN model predicts it may be effective for **chronic ethmoidal sinusitis**, but there are **0 clinical trials** and only **1 publication** (a disease-pathology study that does not test the drug), so the prediction rests almost entirely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied label data (tetracycline-class antibacterial) |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 10 (all listed licenses are ANDAs, i.e., generics) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for demeclocycline. Based on general knowledge, demeclocycline is a tetracycline-class antibiotic. A plausible but unverified link is that its antibacterial activity, together with class-level anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects, could matter in chronic sinus inflammation and bone remodeling. None of this has been tested for demeclocycline in the supplied evidence.

The only linked paper (PMID 9546260) describes changes in ethmoid bone in chronic rhinosinusitis. It suggests bone is involved in the disease, but it does not evaluate demeclocycline or any tetracycline. The high TxGNN score (0.991) is a model output, not clinical evidence.

Two other predictions were returned:
- **Chronic rhinosinusitis** (score 99.09%) largely overlaps with the lead indication and shares the same single reference, so the two are not independent evidence.
- **Paranasal sinus neoplasm** (score 99.05%) has no trials or literature. It is a higher-stakes indication, and a tetracycline antibiotic would need strong preclinical and clinical support first.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9546260](https://pubmed.ncbi.nlm.nih.gov/9546260/) | 1998 | Histology / histomorphometry study | The Laryngoscope | Compared ethmoid bone from chronic sinusitis patients with controls, assessing bone synthesis, resorption and inflammatory cells. It suggests bone is involved in the disease, but it does not study demeclocycline. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065425 | Demeclocycline Hydrochloride (American Health Packaging) | Tablet | Not provided in supplied data |
| ANDA065425 | Demeclocycline Hydrochloride (Amneal Pharmaceuticals) | Tablet | Not provided in supplied data |
| ANDA065447 | Demeclocycline Hydrochloride (Epic Pharma) | Tablet, film coated | Not provided in supplied data |

Only the oral route is available. Route compatibility with the predicted indication has not been assessed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, and the single publication does not test demeclocycline. The mechanism of action and the package insert safety data are also missing, so a safety screen cannot be started.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap): download and parse the FDA label
- Mechanism of action data from DrugBank
- Approved indication text for the existing US licenses, to define the original indication
- Evidence that demeclocycline or tetracyclines have activity in chronic rhinosinusitis, such as preclinical, observational or clinical studies
- A route and dose compatibility assessment for sinus disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

