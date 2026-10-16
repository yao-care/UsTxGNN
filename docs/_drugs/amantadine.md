---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 4
monitor_inn: "AMANTADINE"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
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

# Amantadine: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine was originally used to treat Parkinson's disease and related movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (and related parkinsonian and basal ganglia disorders, per the knowledge graph) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, amantadine acts as an NMDA receptor antagonist and modulates dopaminergic transmission. Its efficacy in Parkinson's disease and related movement disorders is established.

Rasmussen encephalitis is a rare, immune-mediated brain disorder with neuronal injury, glutamate-related excitotoxicity, and intractable seizures. NMDA antagonism offers a plausible but purely theoretical link to this process. The high TxGNN score is a computational prediction only, and no trials or literature were found to confirm it.

For context, other predictions for this drug have somewhat more support. Myelitis (score 99.24%) has literature on post-polio fatigue, including a small placebo-controlled trial. PLA2G6-associated neurodegeneration (99.23%) has only a case report in a different disease subtype. Neither changes the assessment for the top-ranked indication here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA214178 | Amantadine Hydrochloride (Patrin Pharma) | Solution | Not available (cancelled) |
| ANDA210129 | Amantadine Hydrochloride (Marlex) | Capsule, gelatin coated | Not available (cancelled) |
| ANDA209035 | Amantadine HCL (Direct_Rx) | Tablet | Not available (cancelled) |
| ANDA074509 | Amantadine Hydrochloride (American Health Packaging) | Solution | Not available (cancelled) |
| ANDA209171 | Amantadine Hydrochloride (Chartwell RX) | Capsule | Not available (cancelled) |

All 10 US authorizations on record are cancelled. Only the first 5 are shown.

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, epilepsy, kidney disease, congestive heart failure, psychotic and related disorders (including schizophreniform and schizoaffective disorder), melanoma, angle-closure glaucoma, substance-related disorders, and atopic eczema/dermatitis. Epilepsy is especially relevant to a seizure-driven condition like Rasmussen encephalitis.
- **Drug Interactions**: 93 interactions were identified in total. The main ones are:
  - **Major**: Bupropion
  - **Moderate**: anticholinergics (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium), metoclopramide, polyethylene glycol (3350 with electrolytes), picosulfuric acid, and sodium sulfate
  - **Unknown severity**: calcitriol, pantoprazole, glimepiride, doxycycline, metformin

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and a theoretical NMDA/excitotoxicity link. There are no clinical trials or publications, and no valid US marketing authorization currently exists.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search specific to Rasmussen encephalitis
- An evaluation of seizure-related risk, given that epilepsy appears among the knowledge-graph contraindications
- Confirmation of current US regulatory and product availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

