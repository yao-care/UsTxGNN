---
layout: default
title: Tolcapone
parent: 僅模型預測 (L5)
nav_order: 1239
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: From Parkinson's Disease to Lewy Body Dementia

## One-Sentence Summary

> Tolcapone is a COMT (catechol-O-methyltransferase) inhibitor used as adjunct therapy with levodopa/carbidopa for Parkinson's disease.
> Among 10 TxGNN-ranked candidate indications, **Lewy Body Dementia** is the strongest repurposing lead,
> supported by **2 preclinical/mechanistic publications** on dopamine-metabolite–driven α-synuclein aggregation — but **no clinical trials exist yet**.
> The remaining 8 candidates (including the top-ranked TxGNN hit) lack any mechanistic or clinical support and are held at screening stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, adjunct to levodopa/carbidopa (inferred from candidate rationale text; not present as a structured field in this evidence pack) |
| Predicted New Indication | Lewy Body Dementia |
| TxGNN Prediction Score | 99.64% (rank 9225 of full candidate list) |
| Evidence Level | L4 (mechanistic/preclinical only) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available in this evidence pack (drug-level MOA is flagged as a data gap). Based on the rationale accompanying the candidate predictions, tolcapone is known to act as a COMT inhibitor, approved for use alongside levodopa/carbidopa to prolong levodopa's effect and reduce peripheral dopamine metabolism in Parkinson's disease.

The mechanistic link to Lewy Body Dementia proposed here is that COMT inhibition reduces production of 3,4-dihydroxyphenylacetaldehyde (DOPAL), a reactive dopamine metabolite. Literature evidence indicates DOPAL promotes oligomerization and quinone-modification of α-synuclein — the core pathological protein in Lewy body disease. By theoretically limiting DOPAL formation, tolcapone could plausibly reduce a driver of α-synuclein aggregation, the central pathology of Lewy body dementia. This is a biologically coherent hypothesis, but it currently rests entirely on in vitro/organoid and biochemical studies, not on any tolcapone-specific animal or clinical data.

It is also worth noting that of the 10 TxGNN top candidates reviewed, one other (juvenile parkinsonism / "paralysis agitans, juvenile, of Hunt") falls within the same disease category as tolcapone's known approved use, which lends it face-validity — but it has zero supporting trials or literature in this evidence pack and involves a pediatric population where tolcapone's hepatotoxicity profile has not been characterized. The remaining 8 candidates (e.g., Rasmussen encephalitis, myelitis, several inherited metabolic/neurodevelopmental disorders) show no plausible mechanistic connection to COMT inhibition and are explicitly flagged in their own rationale as likely reflecting non-specific graph clustering rather than true biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclinical (iPSC organoid model) | Science Advances | Modeled Lewy body disease using SNCA-triplication iPSC-derived cortical organoids to characterize α-synuclein pathology and screen therapeutic drug candidates |
| [31744850](https://pubmed.ncbi.nlm.nih.gov/31744850/) | 2020 | Preclinical (in vitro biochemical study) | J Pharmacol Exp Ther | Showed DOPAL (a dopamine oxidation product formed via monoamine oxidase) is more potent than dopamine itself at oligomerizing and quinone-modifying α-synuclein, supporting DOPAL as a pathogenic driver in Lewy body diseases |

---

## Taiwan Market Information

No marketing authorization records were found. Tolcapone is currently **not marketed** in Taiwan (0 licenses on file).

---

## Safety Considerations

Package insert warnings, contraindications, and drug-interaction data for tolcapone have not yet been collected in this evidence pack — this is flagged as a **blocking gap (DG001)** that prevents a formal S1 safety screen. Candidate-level rationale text separately references tolcapone's known hepatotoxicity boxed warning, but this has not been independently verified against a primary source (e.g., TFDA label) in this pack.

Please refer to the official package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Lewy body dementia hypothesis has a coherent biological rationale (DOPAL–α-synuclein pathway) but is supported only by preclinical/in vitro studies (L4), with no clinical trials, no Taiwan market presence, and no verified safety/label data — safety review cannot proceed until the blocking data gap is resolved.

**To proceed, the following is needed:**
- Collect TFDA package insert data (warnings, contraindications, DDI) — currently blocking S1 review (DG001)
- Confirm tolcapone's formal MOA and approved-indication records via DrugBank API (DG002)
- Generate in vivo (animal model) evidence testing the DOPAL/α-synuclein hypothesis specifically with tolcapone, not just dopamine metabolites generally
- Given tolcapone's known hepatotoxicity signal, any future clinical development requires a liver-function monitoring protocol
- Monitor for emerging clinical trial registrations in Lewy body dementia/synucleinopathies before advancing beyond "Research Question" stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

