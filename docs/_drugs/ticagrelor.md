---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 1227
evidence_level: L5
indication_count: 10
---

# Ticagrelor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is a P2Y12 receptor antagonist established for acute coronary syndrome (ACS) and secondary prevention of ischemic events after percutaneous coronary intervention (PCI).
The TxGNN model predicts it may be effective for **Intracranial Arteriosclerosis**,
with **11 clinical trials** and **3 publications** currently supporting this direction, including an ongoing Phase 3 trial designed specifically for this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) / post-PCI secondary prevention (established pharmacological use; no local approved-label text available since the drug is not locally marketed) |
| Predicted New Indication | Intracranial Arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data for this DrugBank record is not available (data gap, DG002). Based on the pharmacological annotations available in the evidence pack, ticagrelor is a P2Y12 receptor antagonist that reversibly inhibits ADP-mediated platelet aggregation. Its established clinical use spans acute coronary syndrome and secondary prevention of ischemic events following percutaneous coronary intervention.

Intracranial arteriosclerosis causes ischemic stroke through the same underlying pathology as coronary artery disease: platelet-mediated thrombus formation on ruptured or stenotic atherosclerotic plaque. Because ticagrelor's antiplatelet mechanism targets this shared pathway rather than a coronary-specific target, extending its use to intracranial atherosclerotic stenosis represents a mechanistically consistent extension rather than a novel, unrelated mechanism.

This is supported directly by the evidence: the CAPTIVA trial (NCT05047172, Phase 3, active) was purpose-built to compare ticagrelor, rivaroxaban, and clopidogrel for reducing stroke, hemorrhage, and vascular death in symptomatic intracranial arterial stenosis, and a companion design paper (PMID 39862061) confirms the rationale that current clopidogrel+aspirin regimens leave a high residual stroke risk that alternative antiplatelet strategies — including ticagrelor — are being tested to address. Additional large completed Phase 3 antiplatelet trials (EUCLID, GLOBAL LEADERS) provide broad safety and efficacy context for ticagrelor in atherothrombotic vascular disease more generally.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13,885 | EUCLID trial: compared ticagrelor vs. clopidogrel for cardiovascular death, MI, and ischemic stroke in patients with peripheral artery disease. |
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1,683 | CAPTIVA trial: directly compares rivaroxaban, ticagrelor, and clopidogrel for reducing 1-year ischemic stroke, intracerebral hemorrhage, or vascular death in intracranial vascular atherostenosis. |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2,009 | Assessed safety of 3-month dual antiplatelet therapy in high-bleeding-risk patients undergoing PCI. |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15,991 | GLOBAL LEADERS: compared 1-month DAPT + 23-month ticagrelor monotherapy vs. standard 12-month DAPT after stenting. |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recruiting | 792 | DREAM-PRIDE: evaluates drug-eluting stent + aggressive medical therapy vs. medical therapy alone for preventing stroke recurrence in symptomatic intracranial atherosclerotic disease. |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | Not yet recruiting | 1,700 | SOLOPCI: tests very short DAPT followed by P2Y12 monotherapy in elderly PCI patients. |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2,036 | Compares low-dose vs. standard-dose ticagrelor in unstable angina patients after drug-eluting stent implantation. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recruiting | 100 | Pilot RCT of genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic intracranial atherosclerotic disease. |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Unknown | 2,171 | Compares anticoagulation alone vs. anticoagulation + antiplatelet therapy in acute ischemic stroke with concomitant AF and intracranial/extracranial artery stenosis. |
| [NCT06857045](https://clinicaltrials.gov/study/NCT06857045) | N/A | Withdrawn | 0 | Planned 3- vs. 6-month DAPT comparison after intracranial sirolimus-eluting stent implantation (withdrawn before enrollment). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT (design paper) | Int J Stroke | Describes design of CAPTIVA, testing whether dual antithrombotic regimens beyond standard clopidogrel+aspirin better reduce recurrent stroke in symptomatic intracranial atherosclerotic stenosis. |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort/Retrospective | J Neurointerv Surg | Reports experience with ticagrelor 60mg BID + aspirin vs. standard clopidogrel+aspirin for neurointerventional/intracranial stenting DAPT. |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis covering current knowledge gaps and treatment approaches. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by two completed large-scale Phase 3 antiplatelet RCTs plus an ongoing Phase 3 trial (CAPTIVA) purpose-designed for intracranial arteriosclerosis, giving reasonable mechanistic and clinical plausibility. However, the drug is not currently marketed locally and formal safety/label data are absent, so guardrails are required before any clinical application.

**To proceed, the following is needed:**
- TFDA/local label warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation can proceed)
- Formal DrugBank-sourced mechanism-of-action documentation (DG002, High priority)
- CAPTIVA trial results upon completion (currently active, not yet reporting)
- Local regulatory pathway assessment, since the drug currently has no marketing authorization on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

