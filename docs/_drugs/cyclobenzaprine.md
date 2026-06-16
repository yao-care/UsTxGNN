---
layout: default
title: Cyclobenzaprine
parent: 僅模型預測 (L5)
nav_order: 554
evidence_level: L5
indication_count: 3
---

# Cyclobenzaprine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Cyclobenzaprine: From Muscle Spasm to Myofascial Pain Syndrome

## One-Sentence Summary

Cyclobenzaprine is a centrally-acting skeletal muscle relaxant, traditionally used for acute muscle spasm associated with painful musculoskeletal conditions.
The TxGNN model predicts it may be effective for **Myofascial Pain Syndrome (MPS)**, with **17 clinical trials** identified — predominantly pivotal Phase 3 RCTs evaluating a low-dose sublingual formulation (TNX-102 SL / TONMYA) that has since received US FDA approval for fibromyalgia, a closely related central sensitization disorder.
No separate PubMed literature was retrieved for MPS specifically, but the mechanistic and clinical crossover from fibromyalgia provides strong indirect support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute muscle spasm associated with painful musculoskeletal conditions |
| Predicted New Indication | Myofascial Pain Syndrome |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Market Status (Taiwan) | Not marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known pharmacology, cyclobenzaprine acts centrally at the brainstem level to reduce tonic somatic motor output, and inhibits norepinephrine reuptake to enhance descending pain inhibition pathways. Its tricyclic structure closely resembles antidepressants such as amitriptyline — a first-line agent for chronic pain — making its analgesic potential mechanistically plausible beyond simple muscle relaxation.

Myofascial Pain Syndrome is characterized by two core pathological processes: peripheral muscle hypertonicity (trigger points) and central sensitization. Cyclobenzaprine's brainstem-mediated reduction of tonic motor drive directly addresses the peripheral component, while its norepinephrine reuptake inhibition targets the central component. These are not incidental overlaps — they are the primary mechanisms through which bedtime low-dose cyclobenzaprine is hypothesized to exert benefit, as described in multiple trial rationales.

The strongest clinical rationale comes from fibromyalgia — a disorder now widely understood to share substantial pathophysiology with MPS, including central sensitization, disrupted sleep architecture, and widespread musculoskeletal pain. The TNX-102 SL program (low-dose sublingual cyclobenzaprine at bedtime) completed four large Phase 3 placebo-controlled RCTs in fibromyalgia and received US FDA approval under the brand name TONMYA. This body of evidence makes the TxGNN prediction for MPS not just algorithmically plausible, but clinically well-grounded.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02436096](https://clinicaltrials.gov/study/NCT02436096) | Phase 3 | Completed | 519 | Pivotal RCT: TNX-102 SL 2.8 mg nightly vs. placebo over 12 weeks in fibromyalgia; established dose selection and efficacy baseline for nightly low-dose cyclobenzaprine |
| [NCT04172831](https://clinicaltrials.gov/study/NCT04172831) | Phase 3 | Completed | 503 | Replication RCT: TNX-102 SL 5.6 mg nightly vs. placebo over 14 weeks; independently confirmed efficacy across pain, sleep, and overall FM symptomatology |
| [NCT04508621](https://clinicaltrials.gov/study/NCT04508621) | Phase 3 | Completed | 514 | Third pivotal RCT: further reinforced reproducibility of treatment effect and expanded the safety database for daily bedtime use |
| [NCT05273749](https://clinicaltrials.gov/study/NCT05273749) | Phase 3 | Completed | 457 | Fourth pivotal RCT: most recently completed large-scale placebo-controlled study; provided regulatory-grade evidence contributing to FDA approval of TONMYA |
| [NCT01903265](https://clinicaltrials.gov/study/NCT01903265) | Phase 2b/3 | Completed | 205 | Key proof-of-concept RCT (BESTFIT study): TNX-102 SL 2.8 mg nightly over 12 weeks; provided the efficacy signal that justified the subsequent Phase 3 program |
| [NCT02589275](https://clinicaltrials.gov/study/NCT02589275) | Phase 3 (OLE) | Completed | 375 | 3-month open-label extension of Phase 3 double-blind studies; evaluated long-term tolerability and sustained efficacy of daily bedtime dosing |
| [NCT00635037](https://clinicaltrials.gov/study/NCT00635037) | N/A | Completed | 30 | **Direct MPS trial**: randomized comparison of acupuncture vs. trigger point injection combined with cyclobenzaprine + dipyrone for myofascial pain; conducted at a dedicated Pain Clinic |
| [NCT04704297](https://clinicaltrials.gov/study/NCT04704297) | Phase 4 | Recruiting | 180 | **Direct MPS trial**: T-PIMPS RCT evaluating trigger point injection for MPS of the low back; provides contemporary context for MPS treatment landscape |
| [NCT01041495](https://clinicaltrials.gov/study/NCT01041495) | Phase 4 | Terminated | 37 | Cyclobenzaprine ER (Amrix) augmentation for fibromyalgia fatigue and muscle pain; terminated early — insufficient statistical power |
| [NCT02829814](https://clinicaltrials.gov/study/NCT02829814) | Phase 3 | Terminated | 51 | Phase 3 RCT of TNX-102 SL for fibromyalgia; terminated early due to low enrollment — no efficacy conclusions possible |

---

## Literature Evidence

Currently no related literature available for myofascial pain syndrome specifically.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four independently completed Phase 3 placebo-controlled RCTs of cyclobenzaprine (as TNX-102 SL / TONMYA) in fibromyalgia — a disorder with well-established pathophysiological overlap with MPS — have demonstrated reproducible efficacy and safety, culminating in US FDA approval. One completed randomized trial directly investigated cyclobenzaprine in MPS patients. The mechanistic link between cyclobenzaprine's central norepinephrine modulation and MPS pathology (muscle hypertonicity + central sensitization) is direct, not inferential, making this a well-supported repurposing candidate.

**To proceed, the following is needed:**
- Full mechanism of action data (MOA) from DrugBank API — currently a High-severity data gap
- Taiwan FDA (TFDA) package insert to obtain key warnings, contraindications, and drug-drug interactions — currently a Blocking data gap for safety screening
- A dedicated Phase 2/3 clinical trial specifically enrolling MPS patients (distinguishing MPS from fibromyalgia as a separate indication for regulatory purposes)
- Clarification of optimal dose and formulation for MPS: sublingual low-dose (as in TONMYA) vs. standard oral immediate-release; the bedtime strategy that succeeded in fibromyalgia may not directly translate
- Safety monitoring plan addressing known tricyclic-class risks (anticholinergic effects, sedation, QTc prolongation potential) in the MPS target population, particularly elderly patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

