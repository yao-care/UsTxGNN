---
layout: default
title: Cocaine
parent: 僅模型預測 (L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine: From Local Anesthetic to Cauda Equina Syndrome

## One-Sentence Summary

Cocaine (DB00907) is a naturally occurring tropane alkaloid historically applied as a topical local anesthetic and vasoconstrictor in ENT and ophthalmic procedures; it carries no currently approved indications or marketed products in the United States.
The TxGNN model ranks **Cauda Equina Syndrome** as the top predicted new indication, with a confidence score of **99.98%**.
Evidence support is extremely limited: **0 clinical trials** and **1 case report** are available, placing this at **Level L5** — model prediction only, with no dedicated clinical or preclinical studies supporting the repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally approved indications; historically used as a topical local anesthetic/vasoconstrictor in ENT and ophthalmic surgery |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cocaine is a naturally occurring alkaloid derived from *Erythroxylum coca* leaves. It exerts two well-characterized pharmacological effects: local anesthesia through voltage-gated sodium channel blockade in nerve membranes, and central sympathomimetic stimulation by inhibiting presynaptic reuptake of norepinephrine, dopamine, and serotonin. These combined properties made cocaine the first local anesthetic used in modern medicine — particularly in ENT and ophthalmologic surgery in the late 19th century — before safer, less addictive alternatives such as lidocaine and bupivacaine replaced it. Currently, detailed mechanism of action data is not available in the Evidence Pack, and no original indications are recorded in the US regulatory database.

Cauda equina syndrome (CES) is a neurological emergency caused by compression of the lumbar and sacral nerve roots below the conus medullaris, most commonly from a large central disc herniation, tumor, or spinal stenosis. Its hallmark presentation includes urinary retention, fecal incontinence, saddle-area sensory loss, and progressive lower-extremity weakness. The standard of care is **emergency surgical decompression** — not pharmacological management. Cocaine's local anesthetic properties could theoretically provide transient pain relief, but this addresses only a symptom and has no effect on the underlying mechanical nerve compression that defines and drives the syndrome.

The TxGNN model assigns an exceptionally high score (99.98%) to this prediction, but mechanistic analysis identifies this as almost certainly a **spurious knowledge-graph association**: CES shares neurological node connectivity with drugs that act on the peripheral nervous system, creating false positive linkages. There is no plausible anti-inflammatory, neuroprotective, or decompressive mechanism through which cocaine could alter the course of cauda equina syndrome. This prediction is assessed as clinically non-actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cocaine and cauda equina syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case Report | Surgical Neurology International | Describes a case of distal CES caused by lumbosacral disc pathology with a literature review of CES presentations; cocaine is not evaluated as a therapeutic agent — the report focuses on surgical diagnosis and decompressive management |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Cocaine is a Schedule II controlled substance under the US Controlled Substances Act. Its known pharmacological profile — including cardiovascular stimulation (tachycardia, hypertension, arrhythmia), CNS excitability (seizures, stroke), and high addiction potential — creates substantial barriers to any therapeutic repurposing outside tightly controlled procedural settings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All evidence for this indication sits at L5 (model prediction only); there are zero registered clinical trials, and the single retrieved literature item is a surgical case report that does not investigate cocaine as a treatment. Critically, cauda equina syndrome is a mechanical emergency requiring surgical decompression — cocaine's local anesthetic effect is symptom-masking at best and could dangerously delay definitive intervention.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis beyond temporary analgesia — e.g., evidence of neuroprotective, anti-edema, or spinal microcirculation effects relevant to nerve root compression
- Preclinical animal studies demonstrating measurable benefit in an established CES model
- A regulatory strategy addressing cocaine's Schedule II controlled substance classification
- A robust safety and addiction-risk mitigation framework for any novel therapeutic application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

