---
layout: default
title: Pregabalin
parent: Moderate Evidence (L3-L4)
nav_order: 1079
evidence_level: L4
indication_count: 6
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Pregabalin: From Neuropathic Pain and Epilepsy to Tendinitis

## One-Sentence Summary

Pregabalin is marketed in the US, and the literature in the pack describes it as approved for partial epilepsy and neuropathic pain. The TxGNN model predicts it may be useful for **tendinitis**, but **no clinical trials** and **no publications that directly test pregabalin in tendinitis** were found. The prediction currently rests on model output and indirect pain-related literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the US license records (the literature describes partial epilepsy and neuropathic pain) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal mechanism-of-action field for pregabalin is not available in this dataset. The pack's rationale notes that pregabalin binds the alpha2-delta subunit of voltage-gated calcium channels. This reduces excitatory neurotransmitter release and central sensitization, which dampens neuropathic and nociceptive pain signaling.

That mechanism could plausibly ease the pain of tendon disorders. However, pregabalin has no known effect on tendon pathology itself (inflammation, degeneration or repair). At most it would treat pain symptoms, not the underlying disease.

The very high score (0.997) should be read with caution. The supporting literature is about pain after rotator cuff surgery and about adverse-event context, not about treating tendinitis. The two high-scoring myositis predictions (idiopathic granulomatous myositis and myositis fibrosa) have identical scores. This suggests they share a graph neighborhood rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these studies tests pregabalin as a treatment for tendinitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Compared oral pregabalin with interscalene nerve block for pain after arthroscopic rotator cuff repair. This is perioperative analgesia, not tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort | J Orthop Sci | Evaluated pregabalin's pain relief and opioid-sparing effect after rotator cuff repair. Earlier studies on opioid-sparing were conflicting. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report/Review | Praxis | Fluoroquinolone-associated disability after ciprofloxacin, which includes tendinopathy as a side effect. Adverse-event context only. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial commentary | Arthroscopy | Piriformis syndrome and its treatment by sciatic neurolysis and piriformis tendon release. Not about pregabalin. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Pract | Posterior femoral cutaneous nerve impingement after a marathon, linked to hamstring tendonitis. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | A plant extract in vincristine-induced neuropathy in rats. Not relevant to pregabalin in tendinitis. |

---

## US Market Information

The license records contain no approved-indication text. Showing 5 of 20 licenses.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021446 | Lyrica | Capsule | Viatris Specialty LLC |
| ANDA212988 | Pregabalin | Capsule | Eskayef Pharmaceuticals Limited |
| ANDA216197 | Pregabalin | Capsule | Marksans Pharma Limited |
| ANDA206912 | Pregabalin | Capsule | NorthStar Rx LLC |
| ANDA205924 | Pregablin | Capsule | Macleods Pharmaceuticals Limited |

Available oral forms also include extended-release film-coated tablets.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The tendinitis prediction has a high model score but no registered trials and no studies of pregabalin in tendinitis. The mechanism would at most relieve pain, not treat tendon disease.

Among the other predictions, **migraine disorder** is the best supported (L2, small RCTs and preclinical work on cortical spreading depression, but the only Phase 3 trial was withdrawn). It would be a stronger candidate to pursue as a research question. The myositis predictions (L5) and migraine with brainstem aura (L4) also remain on Hold.

**To proceed, the following is needed:**
- A tendinitis-specific clinical study, or a pilot study of pain outcomes in tendinopathy patients
- Detailed mechanism-of-action data
- Package insert warnings and contraindications, which are currently missing
- A clear plan that separates symptomatic pain relief from any disease-modifying claim
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

