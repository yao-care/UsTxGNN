---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Apixaban: From Anticoagulation Therapy to Migraine Disorder

## One-Sentence Summary

Apixaban is a direct oral anticoagulant (Factor Xa inhibitor) established for thromboembolic prevention, including stroke prevention in atrial fibrillation and DVT/PE treatment.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **1 clinical trial** and **4 publications** currently providing indirect support.
Critically, the available case literature presents contradictory signals — two reports specifically document migraine *worsening* with apixaban — raising significant concerns about this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thromboembolic prevention (stroke, DVT/PE) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (0 approvals on record) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Apixaban is a selective, direct Factor Xa inhibitor belonging to the DOAC (direct oral anticoagulant) class. Although detailed MOA data was not returned in this evidence pack, it is well established that apixaban blocks Factor Xa in both the intrinsic and extrinsic coagulation pathways, preventing thrombin generation and fibrin clot formation without requiring antithrombin as a cofactor.

The hypothesized mechanistic bridge to migraine is indirect: by suppressing microthrombus formation — particularly in patients with patent foramen ovale (PFO) — apixaban might theoretically reduce paradoxical microemboli that could trigger cortical spreading depression (CSD), the neurophysiological substrate of migraine aura. This parallels the clinical observation that PFO transcatheter closure reduces migraine frequency in selected patients, and aligns with case reports showing that vitamin K antagonists (warfarin) can suppress migraine in anticoagulated patients.

However, the evidence directly involving apixaban undermines this hypothesis. Two published case reports specifically document that migraine *worsened* upon initiating apixaban or *recurred* when switching from warfarin to apixaban — with symptoms resolving again upon warfarin resumption. This divergence implies that Factor Xa inhibition and vitamin K antagonism engage meaningfully different pathways relevant to migraine pathophysiology, and that the class-level anticoagulant hypothesis does not generalize to apixaban specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compared PFO closure, oral anticoagulants, and antiplatelet therapy for secondary stroke prevention in PFO patients. Migraine was not a primary endpoint; apixaban was not individually specified in the anticoagulant arm. Relevance to migraine is indirect (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Observational Study | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies; antithrombotic therapy showed symptomatic improvement, suggesting a hypercoagulable subtype of migraine may respond to anticoagulation — provides mechanistic context but does not isolate apixaban. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | Migraine with aura worsened after initiating apixaban; accompanying literature review concludes that DOAC evidence in migraine is scarce and contradictory — **negative signal** for apixaban. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | 55-year-old female with 12 years of migraine remission on warfarin; symptoms returned within 3 weeks of switching to apixaban and resolved again upon warfarin resumption — direct head-to-head contrast, **negative signal** for apixaban vs. warfarin in migraine. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolution on warfarin plus topiramate; no apixaban data, provides contextual support for the anticoagulant-migraine hypothesis at the class level only. |

---

## US Market Information

Apixaban currently has no approved licenses on record in this regulatory dataset (0 authorizations). No marketed products are available for this drug in the queried jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for apixaban in migraine disorder sits at Level L4 (mechanistic hypothesis / indirect case data), and the directly relevant case literature raises a red flag: apixaban appears to worsen rather than improve migraine, in direct contrast to warfarin — suggesting the Factor Xa inhibition pathway is not equivalent to vitamin K antagonism for this indication, and possibly counterproductive.

**To proceed, the following is needed:**

- Prospective clinical studies specifically evaluating apixaban in migraine patients, particularly those with confirmed PFO or antiphospholipid antibodies
- Head-to-head pharmacological comparison of apixaban versus warfarin effects on cortical spreading depression (CSD) in preclinical models — to clarify whether the mechanism divergence is real
- Subgroup analysis from existing PFO-stroke trials to extract any migraine frequency data from anticoagulant-treated arms (and identify which specific agents were used)
- Regulatory pathway assessment, as apixaban is currently not approved in the queried jurisdiction and would require a full NDA submission before any repurposing clinical program could advance
- MOA data retrieval from DrugBank (flagged as a data gap) to complete the mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

