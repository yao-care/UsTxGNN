---
layout: default
title: Cyclobenzaprine
parent: Model Prediction Only (L5)
nav_order: 554
evidence_level: L5
indication_count: 3
---

# Cyclobenzaprine
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

# Cyclobenzaprine: From Muscle Spasm to Myofascial Pain Syndrome

## One-Sentence Summary

Cyclobenzaprine is an oral skeletal muscle relaxant, used for muscle spasm associated with acute, painful musculoskeletal conditions.
The TxGNN model predicts it may be effective for **myofascial pain syndrome**.
Of the **16 clinical trials** listed, most test a sublingual cyclobenzaprine product in fibromyalgia, a related but different condition. Only 1 small trial directly studies myofascial pain, and **no publications** were retrieved for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasm associated with acute, painful musculoskeletal conditions (taken from a trial description, because the license records list no indication text) |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L2 per the Evidence Pack. This is generous: the Phase 2/3 and Phase 3 RCTs are in fibromyalgia, not myofascial pain, so direct evidence is closer to L4. |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all shown listings are generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank in this pack. Based on the pack's mechanistic notes, cyclobenzaprine is a centrally acting muscle relaxant structurally related to tricyclic antidepressants. It acts on brainstem descending pathways with 5-HT2 antagonism, plus H1 and anticholinergic activity.

Myofascial pain syndrome is a regional muscle pain condition, so a drug already used for painful muscle spasm is a plausible fit. The sedative and serotonergic effects may also help with the sleep disturbance that often accompanies chronic muscle pain.

Note that a graph score is not clinical evidence. Most of the supporting trials come from a low-dose sublingual product (TNX-102 SL) developed for fibromyalgia. Fibromyalgia is related to myofascial pain but is not the same condition. That product has reportedly been approved by the US FDA for fibromyalgia under the brand name TONMYA, according to a trial record.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05273749](https://clinicaltrials.gov/study/NCT05273749) | Phase 3 | Completed | 457 | 14-week placebo-controlled RCT of TNX-102 SL 5.6 mg at bedtime in fibromyalgia |
| [NCT04172831](https://clinicaltrials.gov/study/NCT04172831) | Phase 3 | Completed | 503 | Same design and program, fibromyalgia |
| [NCT04508621](https://clinicaltrials.gov/study/NCT04508621) | Phase 3 | Completed | 514 | Same design and program, fibromyalgia |
| [NCT02436096](https://clinicaltrials.gov/study/NCT02436096) | Phase 3 | Completed | 519 | 12-week placebo-controlled RCT of TNX-102 SL 2.8 mg in fibromyalgia |
| [NCT01903265](https://clinicaltrials.gov/study/NCT01903265) | Phase 2/3 | Completed | 205 | Phase 2b placebo-controlled RCT, 12 weeks, TNX-102 SL 2.8 mg in fibromyalgia |
| [NCT02589275](https://clinicaltrials.gov/study/NCT02589275) | Phase 3 | Completed | 375 | 3-month open-label extension for long-term safety and efficacy in fibromyalgia (uncontrolled) |
| [NCT00635037](https://clinicaltrials.gov/study/NCT00635037) | N/A | Completed | 30 | Acupuncture vs trigger point injection combined with dipyrone and cyclobenzaprine in myofascial pain. Small, and cyclobenzaprine is part of a combination. |
| [NCT01041495](https://clinicaltrials.gov/study/NCT01041495) | Phase 4 | Terminated | 37 | Cyclobenzaprine ER augmentation for fibromyalgia fatigue and muscle pain. Underpowered. |
| [NCT04704297](https://clinicaltrials.gov/study/NCT04704297) | Phase 4 | Recruiting | 180 | Trigger point injection for low-back myofascial pain. Cyclobenzaprine is not the studied drug. |
| [NCT01921296](https://clinicaltrials.gov/study/NCT01921296) | Phase 2 | Terminated | 2 | Cyclobenzaprine for sleep disturbance, fatigue and musculoskeletal symptoms in breast cancer patients on aromatase inhibitors. Too small to inform efficacy. |

The registered conditions of the TNX-102 SL trials should be verified. The pack flags that they appear to target fibromyalgia rather than myofascial pain.

---

## Literature Evidence

Currently no related literature available for myofascial pain syndrome.

---

## US Market Information

The license records contain no approved-indication text. Five of the 20 listings are shown.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA091281 | Cyclobenzaprine Hydrochloride (Asclemed USA, Inc.) | Capsule, extended release |
| ANDA078643 | Cyclobenzaprine Hydrochloride (Rising Pharma Holdings, Inc.) | Tablet, film coated |
| ANDA077797 | Cyclobenzaprine Hydrochloride (Bryant Ranch Prepack) | Tablet, film coated |
| ANDA213324 | Cyclobenzaprine Hydrochloride (Asclemed USA, Inc.) | Tablet, film coated |
| ANDA077563 | Cyclobenzaprine Hydrochloride (Doc Rx) | Tablet, film coated |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest trials (four completed Phase 3 RCTs and one Phase 2/3 RCT) are in fibromyalgia, not myofascial pain. The only trial that directly involves myofascial pain is small (n=30) and tests cyclobenzaprine only as part of a combination. No literature supports this indication, and the package insert safety data is missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label
- Formal mechanism-of-action data from DrugBank
- Verification of the registered conditions for the TNX-102 SL trials
- A myofascial-pain-specific RCT, or a literature review of cyclobenzaprine in myofascial pain
- A route and formulation compatibility assessment (oral vs sublingual)

**Other predictions:** Neuralgia (score 99.08%) has only indirect evidence from multi-ingredient topical products and reviews, so it stays on Hold at evidence level L4. Papillary conjunctivitis (score 99.08%) has no trials or literature at all (L5). Its anticholinergic effects may even worsen ocular symptoms, so it is also on Hold.

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

