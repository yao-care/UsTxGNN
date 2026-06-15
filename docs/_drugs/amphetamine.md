---
layout: default
title: Amphetamine
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 5
---

# Amphetamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Amphetamine: From ADHD / Narcolepsy to Faciodigitogenital Syndrome

## One-Sentence Summary

Amphetamine is a central nervous system stimulant with established global use in attention deficit hyperactivity disorder (ADHD) and narcolepsy, though it carries no approved licenses in Taiwan as of this report's data cutoff.
The TxGNN model's highest-ranked prediction is **Faciodigitogenital Syndrome** (Aarskog-Scott Syndrome), a rare X-linked developmental disorder caused by FGD1 gene mutations.
Currently **0 clinical trials** and **0 publications** directly support this repurposing direction, placing it at Evidence Level L5 with a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ADHD, Narcolepsy (US FDA-approved; no Taiwan license) |
| Predicted New Indication | Faciodigitogenital Syndrome (Aarskog-Scott Syndrome) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on established pharmacological knowledge, amphetamine is a catecholamine-releasing agent: it promotes presynaptic release of dopamine (DA) and norepinephrine (NE) at central synapses while simultaneously blocking their reuptake transporters (DAT and NET). This dual action enhances prefrontal cortex executive function, working memory, and attentional control — the neurobiological foundation for its approved use in ADHD and narcolepsy.

Faciodigitogenital syndrome (Aarskog-Scott syndrome) is caused by loss-of-function mutations in **FGD1**, a gene encoding a Rho guanine nucleotide exchange factor (GEF) that activates the GTPase CDC42. This pathway governs cytoskeletal dynamics and directional cell migration during fetal morphogenesis. Its disruption produces the syndrome's hallmark triad: facial dysmorphia (hypertelorism, broad nasal bridge), brachydactyly with short stature, and genital hypoplasia (shawl scrotum). The FGD1-CDC42 axis operates entirely in the domain of embryonic structural development — a process biologically distinct from catecholaminergic neurotransmission.

No known biological mechanism links amphetamine's DA/NE-releasing action to the FGD1-Rho GEF signaling pathway. The TxGNN score of 99.97% most likely reflects a non-specific generalization through the knowledge graph's "developmental disorder" super-node, rather than a true mechanistic hypothesis. This prediction is assessed as model noise rather than a clinically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important:** Taiwan TFDA package insert data is unavailable for this Evidence Pack (Data Gap DG001, severity: **Blocking**). Full safety review — including controlled substance scheduling, cardiovascular warnings, CNS stimulant effects, dependence potential, and pediatric growth effects — must be conducted from official regulatory sources (TFDA official website, package insert PDF) before any clinical consideration proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No preclinical or clinical evidence connects amphetamine to faciodigitogenital syndrome. The high TxGNN score reflects knowledge graph topology rather than biological plausibility — amphetamine's DA/NE neurotransmitter mechanism has no established link to the FGD1-CDC42 developmental signaling pathway responsible for this syndrome, and the prediction is most likely a generalization artifact.

**To proceed, the following is needed:**
- Preclinical evidence (in vitro or animal model) demonstrating interaction between catecholaminergic neurotransmission and FGD1/CDC42 signaling
- At least one published hypothesis or case observation suggesting therapeutic potential in Aarskog-Scott syndrome
- Retrieval of Taiwan TFDA package insert to resolve the **Blocking** safety data gap (DG001)
- DrugBank MOA data retrieval to enable full mechanistic analysis (DG002)

---

> **Reviewer Note — Priority Redirect:** Among the five predicted indications in this Evidence Pack, **Specific Developmental Disorder** (rank 3, TxGNN score 99.91%, Evidence Level **L3**, decision stage **S2**) presents the strongest actionable repurposing signal. It is supported by 23 clinical trials and 19 literature references, and amphetamine already holds US FDA approval for ADHD — a direct subset of the ICD-10 F80–F89 specific developmental disorder category. A dedicated evaluation report for this indication is recommended as the priority next step before allocating further resources to any other prediction in this pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

