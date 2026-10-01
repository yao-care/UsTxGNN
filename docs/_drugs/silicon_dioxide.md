---
layout: default
title: Silicon Dioxide
parent: Model Prediction Only (L5)
nav_order: 1159
evidence_level: L5
indication_count: 4
---

# Silicon Dioxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Silicon Dioxide: From an Unspecified Original Indication to Active Peptic Ulcer Disease

## One-Sentence Summary

Silicon dioxide (DrugBank DB11132) is marketed in the US in 20 listed products, but the records give no approved indication for it.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with a score of 99.93%.
**No clinical trials** are registered for this pairing, and none of the retrieved publications test silicon dioxide itself against peptic ulcer disease. The prediction is therefore hypothesis-level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available records |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (mechanism and preclinical literature only; no completed trials) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (total licenses listed) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for silicon dioxide, so no direct mechanistic link can be documented. The plausible routes are indirect. Silicates and orthosilicic acid derivatives may coat or adsorb at the gastric mucosa, as in smectite clay products. Silica-based materials also appear in the antacid literature, for example magnesium trisilicate, and as carriers in gastroretentive drug-delivery systems.

The retrieved literature is mostly about reflux esophagitis, antacid combinations, and rat paw-edema anti-inflammatory models. In the silica-related papers, silica is a delivery vehicle or mineral component, not a validated active agent. The high TxGNN score reflects knowledge-graph proximity, not clinical proof.

The related predictions for gastric ulcer and gastrojejunal ulcer have the same weakness. They rest on a small muscovite (silicate mineral) study and on preclinical mesoporous silica work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers tests silicon dioxide as a treatment for active peptic ulcer disease. They provide background on adjacent therapies and on silicon chemistry.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2986275](https://pubmed.ncbi.nlm.nih.gov/2986275/) | 1985 | RCT | Scand J Gastroenterol | Sucralfate vs alginate/antacid in reflux esophagitis. Both improved symptoms in about 70% of patients. Silica was not tested. |
| [2877526](https://pubmed.ncbi.nlm.nih.gov/2877526/) | 1986 | Review | Z Gastroenterol | Stepwise medical therapy for reflux disease, covering antacids, alginate, acid suppressants and mucosal protectants. |
| [6095236](https://pubmed.ncbi.nlm.nih.gov/6095236/) | 1983 | Review | Polimery w medycynie | Summary of the biological and pharmacological properties of orthosilicic acid and its derivatives. Early evaluation only. |
| [7604597](https://pubmed.ncbi.nlm.nih.gov/7604597/) | 1994 | Clinical report | Likars'ka sprava | Smecta (a clay product) reduced gastric proteolytic activity and had an acid-neutralizing effect in peptic ulcer patients. |
| [1550303](https://pubmed.ncbi.nlm.nih.gov/1550303/) | 1992 | Clinical series | Am Surg | Endoscopic intervention as an alternative to surgery for upper GI bleeding. No link to silica. |
| [5458923](https://pubmed.ncbi.nlm.nih.gov/5458923/) | 1970 | Animal study | Therapie | Anti-inflammatory and anti-ulcer activity of a steroid alkaloid. Not related to silica. |
| [157060](https://pubmed.ncbi.nlm.nih.gov/157060/) | 1979 | Animal study | Agents Actions | Comparison of drugs across four rat paw-edema models. Not related to silica. |
| [7401102](https://pubmed.ncbi.nlm.nih.gov/7401102/) | 1980 | Animal study | J Med Chem | Anti-inflammatory activity of copper complexes in rodents. Not related to silica. |

---

## US Market Information

There are 20 listings in total. Five are shown below. The records give no license numbers or approved indication text for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | BM Silicea Icing Sugar (BM Private Limited) | Tablet | Not specified |
| Not listed | QELBY Hesperidin Patch (JD Life Sciences) | Patch | Not specified |
| Not listed | Silicea (Hahnemann Laboratories) | Pellet | Not specified |
| Not listed | SILICEA (Hyland's) | Tablet | Not specified |
| Not listed | Silicea (Boiron) | Pellet | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no registered clinical trials and no publication testing silicon dioxide itself in peptic ulcer disease. Silica appears only as a carrier or mineral component in indirect literature. Safety data (warnings, contraindications) and mechanism data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block the safety screening step
- Mechanism of action data, for example from DrugBank
- The approved indications of the marketed products, to establish the original indication
- Preclinical evidence of silicon dioxide itself, not silica used as a carrier, in an ulcer model
- Confirmation of route and formulation compatibility for the intended use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

