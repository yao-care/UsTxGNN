---
layout: default
title: Apixaban
parent: Model Prediction Only (L5)
nav_order: 392
evidence_level: L5
indication_count: 1
monitor_inn: "APIXABAN"
predicted_indications: ["migraine disorder"]
last_modified_at: 2026-11-04
description: "Apixaban: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Apixaban
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

## Apixaban: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Apixaban is a direct factor Xa inhibitor (an oral anticoagulant) marketed in the United States.
The TxGNN model predicts it may be relevant for **migraine disorder**, but the evidence level is **L5**: no study supports apixaban for migraine. The two case reports describe migraine with aura that worsened, or did not resolve, on apixaban.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9902 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 5) |
| Number of FDA Applications | 5 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Apixaban is known as a direct factor Xa inhibitor, which reduces thrombin generation and clot formation.

A plausible but unproven link is that migraine with aura has been associated with paradoxical embolism through a patent foramen ovale, microthrombi, and prothrombotic states such as antiphospholipid antibodies. Anticoagulation might therefore help selected patients. The TxGNN score is high (0.9902), but it comes from a model-based prediction and does not establish a mechanism.

The available case reports point the other way. One describes migraine with aura worsening after starting apixaban. Another describes no response to apixaban, while symptoms resolved on warfarin. This suggests no class-wide benefit, and any effect may be drug-specific or patient-specific. No established mechanism links factor Xa inhibition to migraine pathophysiology (CGRP, cortical spreading depression, trigeminovascular activation).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compared PFO closure or anticoagulants with antiplatelet therapy to prevent stroke recurrence in patients with PFO and prior cryptogenic stroke. Migraine was not the primary condition or endpoint; apixaban is not clearly the agent tested. Indirect context only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Response to antithrombotic therapy in refractory migraine with antiphospholipid antibodies; whether apixaban was tested is not confirmed from the available abstract. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | A 55-year-old woman with migraine with aura in remission on warfarin for 12 years; symptoms returned within 3 weeks of switching to apixaban and resolved again on resuming warfarin. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report with literature review | The Neurologist | Migraine with aura worsened after starting apixaban; the literature on direct oral anticoagulants and migraine is scarce and controversial. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA202155 | ELIQUIS (Cardinal Health 107) | Film-coated tablet | Not available |
| ANDA210067 | Apixaban (Macleods) | Film-coated tablet | Not available |
| ANDA209810 | Apixaban (Amneal) | Film-coated tablet | Not available |
| NDA220073 | ELIQUIS SPRINKLE (E.R. Squibb & Sons) | Capsule | Not available |
| ANDA209898 | Apixaban (Indoco Remedies) | Film-coated tablet | Not available |

Of the 5 licences listed, 3 are valid and 2 are cancelled.

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Examples of Major-level interactions: acetylsalicylic acid, cobicistat, deferasirox, ibritumomab tiuxetan, tositumomab. Examples of Moderate-level interactions: aprepitant, clarithromycin, dexamethasone, miconazole, rolapitant, sugammadex.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. No study supports apixaban for migraine, and the available case reports describe worsening or no response on apixaban. The high TxGNN score alone does not justify moving forward.

**To proceed, the following is needed:**
- Controlled studies that directly test apixaban in migraine, ideally in defined subgroups (e.g., migraine with aura and PFO, or antiphospholipid antibodies)
- Mechanism of action data linking factor Xa inhibition to migraine pathophysiology
- Review of the package insert for warnings and contraindications

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

