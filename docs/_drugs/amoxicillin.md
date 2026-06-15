---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a broad-spectrum penicillin-class β-lactam antibiotic with established efficacy against a wide range of bacterial infections, including respiratory tract, urinary tract, and skin infections.
The TxGNN model's top-ranked prediction suggests it may be effective for **Polyclonal Hyperviscosity Syndrome**, though this direction is currently supported by **no clinical trials** and **no publications**, resting entirely on the computational model.
Among the 8 evaluated predictions, **Monoclonal Gammopathy** (rank 6, L4) carries the most compelling mechanistic rationale—amoxicillin's role in *H. pylori* eradication regimens tied to IPSID/Mediterranean lymphoma regression—backed by **1 clinical trial** and **11 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (β-lactam antibiotic; no US regulatory license records retrieved — data gap) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | Data not retrieved (pipeline gap; amoxicillin is a widely available US generic) |
| Number of NDAs | 0 (data gap — see note below) |
| Recommended Decision | Hold |

> **Note on regulatory data**: The data pipeline returned 0 license records for amoxicillin. Amoxicillin is a long-established generic antibiotic with multiple manufacturers and broad FDA approval in the United States. The absence of records reflects a retrieval gap in this pipeline run, not an absence of approval.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on well-established pharmacological knowledge, amoxicillin is a penicillin-class β-lactam antibiotic that works by irreversibly binding to penicillin-binding proteins (PBPs) in bacterial cell walls, inhibiting cross-linking of peptidoglycan and causing cell lysis. This mechanism is effective against a broad spectrum of Gram-positive and some Gram-negative bacteria, making amoxicillin one of the most widely prescribed antibiotics globally.

Polyclonal hyperviscosity syndrome arises from massive overproduction of polyclonal immunoglobulins, typically driven by chronic infection, autoimmune disease, or reactive plasmacytosis—not a primary B-cell malignancy. The TxGNN knowledge graph appears to have established this association through an indirect pathway: bacterial infection triggers immune activation → elevated polyclonal immunoglobulin production → increased blood viscosity. By clearing the bacterial trigger, amoxicillin could theoretically reduce the immunological driver. However, amoxicillin has no known direct effect on blood viscosity, immunoglobulin levels, or B-cell regulation. This is most plausibly a knowledge graph false positive arising from distal node associations.

Among all 8 evaluated predictions, **Monoclonal Gammopathy** (rank 6) presents the most biologically sound repurposing hypothesis. Immunoproliferative small intestinal disease (IPSID, also known as Alpha chain disease or Mediterranean lymphoma) is a subtype involving monoclonal IgA overproduction causally linked to *Campylobacter jejuni* or *H. pylori* chronic infection. Multiple published case series document spontaneous regression of IPSID following antibiotic eradication of the infection. Amoxicillin is a core component of standard *H. pylori* triple therapy (Amoxicillin + Clarithromycin + PPI), and its structural precursor ampicillin carries historical use in IPSID treatment—making this the mechanistically strongest repurposing hypothesis in this data set, and a more actionable research direction than the rank-1 prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Polyclonal Hyperviscosity Syndrome.

---

## Literature Evidence

Currently no related literature available for Polyclonal Hyperviscosity Syndrome.

---

## US Market Information

No US FDA authorization records were retrieved for amoxicillin in this data pipeline run. Amoxicillin is a long-established generic antibiotic approved across multiple indications in the United States, manufactured by numerous companies under various brand names (e.g., Amoxil, Trimox). The absence of records in this report reflects a data retrieval limitation and should be resolved by querying the FDA Orange Book directly.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high computational score (99.63%) to the amoxicillin–polyclonal hyperviscosity syndrome association, the biological plausibility is low—the proposed mechanism is entirely indirect—and no clinical trial or publication currently supports this repurposing direction.

**To proceed, the following is needed:**
- Mechanistic studies establishing whether antibiotic-mediated infection clearance measurably reduces polyclonal immunoglobulin levels and blood viscosity in humans
- Retrospective patient data linking amoxicillin treatment outcomes to viscosity normalization in polyclonal hyperviscosity cases
- Resolution of the regulatory data gap: retrieve US FDA Orange Book entries and package insert (warnings, contraindications, approved indications) for complete safety profiling

---

**Higher-Priority Research Direction — Monoclonal Gammopathy (Rank 6, Evidence Level L4):**

This prediction warrants active investigation and should be prioritized over the rank-1 prediction, based on the following:

| Basis | Details |
|-------|---------|
| Mechanistic link | *H. pylori* / *Campylobacter* infection drives monoclonal IgA overproduction in IPSID; antibiotic eradication induces B-cell clone regression |
| Historical precedent | Case series show IPSID regression after antibiotic therapy including ampicillin (amoxicillin's structural precursor): PMID [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/), [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/), [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/), [16253033](https://pubmed.ncbi.nlm.nih.gov/16253033/) |
| Clinical trial | [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) enrolled febrile neutropenic cancer patients (population may include monoclonal disease); trial terminated, not directly confirmatory |
| Recommended next step | Commission a systematic review of antibiotic regimens in IPSID/Alpha chain disease to quantify remission rates and define amoxicillin's specific contribution within combination *H. pylori* eradication protocols |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

