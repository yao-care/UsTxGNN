---
layout: default
title: Oxacillin
parent: Model Prediction Only (L5)
nav_order: 998
evidence_level: L5
indication_count: 4
monitor_inn: "OXACILLIN"
predicted_indications: ["epiglottitis", "laryngitis", "bacterial arthritis", "urinary tract infection (disease)"]
last_modified_at: 2026-10-30
description: "Oxacillin: predicted new indication Epiglottitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Oxacillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Oxacillin: Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Oxacillin is a penicillinase-resistant beta-lactam antibiotic, originally used to treat staphylococcal infections, including *Staphylococcus aureus* infection, pharyngitis, staphylococcal pneumonia and sinusitis.
The TxGNN model predicts it may be effective for **Epiglottitis**, but this prediction rests on the model alone, with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 8 of 8) |
| Number of FDA Applications | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, oxacillin is a penicillinase-resistant beta-lactam. It inhibits bacterial cell wall synthesis and is active against methicillin-susceptible *Staphylococcus aureus* (MSSA).

Epiglottitis is mainly caused by *Haemophilus influenzae* and *Streptococcus* species, and less often by *S. aureus*. A mechanistic rationale therefore exists only for staphylococcal cases. Oxacillin is also not a first-line choice, because empirical regimens target *H. influenzae* with third-generation cephalosporins.

The high score (0.999) is a model prediction only. It may partly reflect network proximity to the existing upper respiratory indications (pharyngitis, sinusitis) rather than a distinct new therapeutic use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

All 8 US authorizations are valid, and the drug is marketed. No approved indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206198 | Oxacillin (Fresenius Kabi USA) | Injection, powder, for solution | Not recorded |
| ANDA201539 | Oxacillin (Eugia US) | Injection, powder, for solution | Not recorded |
| ANDA091486 | Oxacillin (Onesource Specialty Pharma) | Injection, powder, for solution | Not recorded |
| ANDA201538 | Oxacillin (Eugia US) | Powder, for solution | Not recorded |
| ANDA207148 | Oxacillin (Wockhardt USA) | Injection, powder, for solution | Not recorded |

Three more authorizations (ANDA207147, ANDA206199 and NDA050640, the Baxter injectable solution) are also cancelled.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.
- **Drug Interactions**: 41 interactions were identified. The moderate-level ones include:
  - Doxycycline
  - Tetracycline
  - Minocycline
  - Picosulfuric acid
  - Iodide I-131
  
  Clarithromycin is minor. Many others have an unrated level, including vancomycin, metronidazole, omeprazole and prednisone.
- **Literature safety signals** (from reports retrieved for other predicted indications): oxacillin-induced DRESS syndrome and leukopenia/granulocytopenia with high-dose therapy.

The package insert's warnings and contraindications could not be retrieved, so please refer to it for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no trials or literature for epiglottitis. Staphylococcal involvement is uncommon, and standard empirical therapy targets other organisms. All 8 US licenses are valid.

**To proceed, the following is needed:**
- Clinical or observational evidence of oxacillin use in staphylococcal epiglottitis
- Package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data
- Confirmation of current US availability

### Other Predicted Indications (for reference)

| Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Laryngitis | 0.9973 | L5 | Hold. Most cases are viral or non-infectious, and there are no trials or literature. |
| Bacterial arthritis | 0.9950 | L5 | Research question. Oxacillin is already standard care for MSSA bone and joint infection, supported by reviews (e.g., PMID 24119927). It is more a matter of labeling than true repurposing. |
| Urinary tract infection | 0.9903 | L4 | Hold. Oxacillin has no activity against the Gram-negative organisms that cause most UTIs, and the literature is mostly surveillance data. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

