---
layout: default
title: Tryptophan
parent: 僅模型預測 (L5)
nav_order: 1271
evidence_level: L5
indication_count: 8
---

# Tryptophan
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

# Tryptophan: From Nutritional Supplement to Restless Legs Syndrome

## One-Sentence Summary

Tryptophan is an essential amino acid and serotonin precursor with no current formal drug indication or active market authorization — historically it was marketed as an over-the-counter sleep and mood aid before a 1989 contamination-related withdrawal.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**,
with **8 relevant publications** (including two small 1980s clinical studies) but **no registered clinical trials**, and the underlying mechanism is not without controversy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No formal approved drug indication on record (historically used OTC as a sleep/mood nutritional supplement) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tryptophan (DrugBank MOA field is a data gap). Based on known pharmacology, tryptophan is the metabolic precursor of 5-hydroxytryptophan (5-HTP), which is converted to serotonin and subsequently to melatonin. This serotonin/melatonin axis is the reason tryptophan was historically marketed as an OTC aid for sleep and mood — it has no other formally recognized indication, which is why no "original indication" can be cited here.

RLS pathophysiology is thought to involve dysregulation of both the dopaminergic and serotonergic systems, which is the biological basis for TxGNN's high prediction score: two small clinical studies from the 1980s (PMID 3953904, 3659737) directly tested L-tryptophan or its metabolites in RLS/periodic limb movement patients and reported some symptomatic benefit.

However, the mechanistic story is not clean. A 2020 pharmacovigilance study (PMID 32546134) found that antidepressants which *increase* synaptic serotonin (SSRIs) are associated with *inducing or worsening* RLS symptoms — the opposite direction from what tryptophan supplementation would be expected to produce if the "more serotonin improves RLS" hypothesis were correct. This internal contradiction means the mechanistic rationale should be treated as a hypothesis requiring further clarification, not an established pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3953904](https://pubmed.ncbi.nlm.nih.gov/3953904/) | 1986 | Open-label clinical study | The American Journal of Psychiatry | Early open-label study reporting symptomatic improvement in RLS patients treated with L-tryptophan |
| [3659737](https://pubmed.ncbi.nlm.nih.gov/3659737/) | 1987 | Clinical study | Sleep | Compared periodic leg movements under L-dopa, 5-HTP, and L-tryptophan, providing early comparative mechanistic data |
| [32546134](https://pubmed.ncbi.nlm.nih.gov/32546134/) | 2020 | Pharmacovigilance cohort | BMC Psychiatry | Global pharmacovigilance analysis found serotonin-increasing antidepressants (SSRIs) associated with drug-induced movement disorders including RLS — a finding that runs counter to the tryptophan-improves-RLS hypothesis |
| [33836477](https://pubmed.ncbi.nlm.nih.gov/33836477/) | 2021 | Systematic review/meta-analysis | Sleep Medicine Reviews | Found elevated tryptophan levels and altered dopamine turnover associated with RLS in chronic liver disease patients — an associative, not interventional, link |
| [1305630](https://pubmed.ncbi.nlm.nih.gov/1305630/) | 1992 | Review | The International Journal of Neuroscience | General review of L-tryptophan's role in serotonin-related neuropsychiatric and motor conditions |
| [2881477](https://pubmed.ncbi.nlm.nih.gov/2881477/) | 1987 | Review | American Family Physician | General review of insomnia diagnosis and treatment, mentioning tryptophan among historical options; not RLS-specific |
| [36897462](https://pubmed.ncbi.nlm.nih.gov/36897462/) | 2023 | Case report | Neurological Sciences | Case report of RLS in a patient with DNAJC12-related dopaminergic/serotonergic deficiency, an inherited metabolic disorder unrelated to tryptophan supplementation |
| [1777530](https://pubmed.ncbi.nlm.nih.gov/1777530/) | 1991 | Case report | Biological Psychiatry | Case report of lithium-induced RLS; no direct tryptophan therapeutic data |

---

## Safety Considerations

Please refer to the package insert for safety information. Note that key warnings, contraindications, and drug-interaction data for tryptophan are currently unavailable in this evidence pack — this is flagged as a **blocking data gap** that prevents a formal safety pre-assessment (see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While TxGNN assigns a high prediction score and two small historical clinical studies suggest possible symptomatic benefit, there are no registered clinical trials, no confirmed mechanism of action, and the serotonergic rationale is directly contradicted by pharmacovigilance evidence showing SSRIs can induce/worsen RLS. Combined with a blocking gap in TFDA/FDA warning and contraindication data, the evidence base is insufficient to proceed.

**To proceed, the following is needed:**
- TFDA/FDA package insert warnings and contraindications (blocking gap — required before any safety pre-assessment can begin)
- Confirmed mechanism of action data (DrugBank API query)
- A modern, adequately powered RCT of tryptophan or 5-HTP specifically in RLS patients
- Mechanistic clarification of the apparent contradiction between serotonergic RLS induction (SSRIs) and the proposed serotonergic benefit of tryptophan
- Review of the 1989 eosinophilia-myalgia syndrome contamination history and current manufacturing/purity controls before considering any therapeutic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

