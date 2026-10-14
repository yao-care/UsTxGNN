---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 1075
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome to Migraine Disorder

## One-Sentence Summary

Prasugrel is a P2Y12 platelet inhibitor, originally used for acute coronary syndrome.
The data compiled for this report show that TxGNN's top-ranked prediction is pulmonary hypertension, which has no direct supporting evidence. The best-supported candidate is **Migraine Disorder** (rank 2), with **2 related clinical trials** (neither tests prasugrel) and **2 class-level publications** currently supporting this direction.

> **Note on selection:** The highest-scoring prediction (pulmonary hypertension, 99.88%) has no clinical trials and no relevant literature. This report therefore focuses on migraine disorder, which has the strongest evidence among the ten predictions (evidence level L3 versus L5 for pulmonary hypertension).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 (retrospective review and open-label pilot, class-level; no prasugrel RCT) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 7 authorizations in total (1 NDA, 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, prasugrel is a thienopyridine P2Y12 antagonist that inhibits platelet aggregation. Its efficacy in acute coronary syndrome is established, and mechanistically it may be applicable to migraine in a specific subgroup.

Some people with migraine also have a patent foramen ovale (PFO), a small opening in the heart wall. In these patients, small emboli or platelet-derived vasoactive mediators (such as serotonin) may bypass the lungs' filtering and trigger migraine. Blocking platelet activation with a P2Y12 inhibitor may reduce migraine frequency in this subgroup.

The supporting evidence is indirect. It consists of a retrospective review of thienopyridines (clopidogrel and prasugrel) and an open-label pilot of ticagrelor, a different P2Y12 inhibitor. No randomized trial of prasugrel in migraine has been identified.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | Recruiting | 32 | COMFORT-PFO: PFO-directed therapy for migraine cessation. The protocol mentions prasugrel as a platelet-inhibiting option, but the study is not a prasugrel efficacy trial. Indirect context only. |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | NA | Terminated | 7 | GORE CARDIOFORM Septal Occluder study of transcatheter PFO closure for migraine. It is a device study with no prasugrel evidence, and was terminated early with very small enrollment. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | Ticagrelor (a non-thienopyridine P2Y12 inhibitor) in refractory migraine with PFO. It was undertaken after clopidogrel and prasugrel were seen to reduce migraine symptoms in some PFO patients. Class-level evidence only. |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Clinical experience with off-label thienopyridines in patients with migraine and PFO. |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preclinical (mouse) | European Journal of Pharmacology | Prasugrel showed neuroprotective effects in a pentylenetetrazol-induced kindling epilepsy model. This is an epilepsy model, not migraine, so it is only indirectly relevant. |

## US Market Information

All seven authorizations are cancelled. No active US marketing authorization remains in the data compiled for this report. Approved indication text was not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022307 | Effient (Cosette Pharmaceuticals) | Coated tablet | Not available |
| ANDA213315 | Prasugrel (Unichem) | Film-coated tablet | Not available |
| ANDA205913 | Prasugrel (Amneal) | Film-coated tablet | Not available |
| ANDA205897 | Prasugrel (Apotex) | Film-coated tablet | Not available |
| ANDA205927 | Prasugrel (Mylan) | Film-coated tablet | Not available |

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text):** liver failure, hypotensive disorder, blood coagulation disease, stroke disorder, cerebrovascular disorder, cerebral infarction, injury, thrombocytopenic purpura, intracranial hemorrhage, transient ischemic attack, and vertebrobasilar insufficiency. These are consistent with the bleeding risk of a potent antiplatelet agent. Of particular concern for migraine, stroke and intracranial hemorrhage are listed.
- **Drug Interactions** (100 interactions in total; selected examples):
  - **Major:** deferasirox, ibritumomab tiuxetan.
  - **Moderate:** acetylsalicylic acid, morphine, opium, fenfluramine, dexfenfluramine, sibutramine.
  - **Minor:** proton pump inhibitors (omeprazole, esomeprazole, pantoprazole and others), H2 blockers (famotidine, ranitidine, cimetidine, nizatidine), bupropion.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine hypothesis rests on a retrospective review and an open-label pilot of related P2Y12 inhibitors in the PFO subgroup, not on prasugrel trials. The two listed trials are PFO-closure studies, and one was terminated after enrolling 7 patients. Prasugrel's bleeding risk, including intracranial hemorrhage, and its large interaction burden make an off-label benefit-risk case hard to justify without stronger data. Because all US authorizations are cancelled, there is also no active US product route.

**To proceed, the following is needed:**
- Mechanism of action data and the package insert warnings and contraindications (both are currently missing and block safety screening)
- Prasugrel-specific controlled data in migraine with PFO, such as a randomized trial in a well-defined PFO subgroup
- Benefit-risk assessment of bleeding, especially intracranial hemorrhage, in a non-cardiac population
- Clarification of the regulatory and supply situation, given that all US authorizations are cancelled
- Review of the other nine predictions: none has direct prasugrel evidence, and pulmonary hypertension, the top-scoring one, has none at all.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

