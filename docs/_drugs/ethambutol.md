---
layout: default
title: Ethambutol
parent: Model Prediction Only (L5)
nav_order: 681
evidence_level: L5
indication_count: 5
monitor_inn: "ETHAMBUTOL"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
last_modified_at: 2026-10-14
description: "Ethambutol: predicted new indication Epiglottitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ethambutol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ethambutol: Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Ethambutol is an anti-tuberculosis drug, originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **Epiglottitis**, but there are currently **0 clinical trials** and only **1 publication** (a case series on laryngeal tuberculosis) supporting this direction.
The evidence indicates that this is a tuberculosis-related manifestation, not a true new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ethambutol inhibits arabinosyl transferase, an enzyme that mycobacteria need to build their cell wall. This is how it acts against *Mycobacterium tuberculosis* as part of multidrug anti-TB regimens. Detailed mechanism data was not available in the data compiled for this report, so this description reflects the drug's generally known pharmacology.

The link between tuberculosis and epiglottitis most likely comes from laryngeal tuberculosis, in which the epiglottis can be one of the affected sites. In the one case series retrieved (41 patients), patients were treated with multidrug anti-TB regimens that included ethambutol. This supports ethambutol as part of anti-TB therapy when TB involves the larynx. It does not support use against typical epiglottitis, which is mainly caused by bacteria such as *Haemophilus influenzae* type b and streptococci, and against which ethambutol has no known activity. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Case series / Retrospective | The European Respiratory Journal | 41 cases of laryngeal tuberculosis (1975–1985); the epiglottis was the second most common site after the true vocal cords; all patients had current or earlier pulmonary TB; treated with isoniazid, rifampicin, ethambutol and other agents |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA075095 | Ethambutol Hydrochloride (Epic Pharma) | Tablet, film coated | Not specified (status: valid) |
| NDA016320 | Ethambutol Hydrochloride (Marlex Pharmaceuticals) | Tablet, film coated | Not specified (status: valid) |
| ANDA078939 | Ethambutol Hydrochloride (Lupin Pharmaceuticals) | Tablet | Not specified (status: valid) |

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The knowledge graph links ethambutol with caution or contraindication in kidney disease, pyoureter, gout, diabetic retinopathy, diabetic cataract and optic neuritis. These should be verified against the official label.
- **Drug Interactions**: 100 interactions were identified. The moderate-level ones include metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin, tinidazole and aluminum hydroxide. Others, such as clotrimazole, pantoprazole, morphine, omeprazole, lansoprazole, vancomycin, prednisone, nystatin, hydrocortisone, potassium chloride, sulfasalazine, prednisolone and ranitidine, have an unknown severity level.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a single case series on laryngeal tuberculosis, where ethambutol is one component of a multidrug regimen. This extends the existing anti-TB role to a specific anatomical site rather than creating a new indication for epiglottitis. There are no clinical trials, and a plausible mechanism against typical epiglottitis pathogens is lacking.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A clear case definition separating tuberculous epiglottitis from bacterial epiglottitis
- Clinical data isolating ethambutol's contribution, beyond combination regimens
- Clarification of the regulatory and market status, given that the drug is marketed with 3 valid US licenses out of 3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

