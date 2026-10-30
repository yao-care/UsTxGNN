---
layout: default
title: Miltefosine
parent: Model Prediction Only (L5)
nav_order: 931
evidence_level: L5
indication_count: 3
monitor_inn: "MILTEFOSINE"
predicted_indications: ["echinococcus granulosus infectious disease", "alveolar echinococcosis", "Smouldering systemic mastocytosis"]
last_modified_at: 2026-10-30
description: "Miltefosine: predicted new indication Echinococcus granulosus infectious disease (evidence level L5). Approved use: Leishmaniasis (including mucocutaneous and visceral leishmaniasis)"
---

# Miltefosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Miltefosine: From Leishmaniasis to Echinococcus granulosus Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Miltefosine is an oral drug originally used to treat leishmaniasis (including visceral and mucocutaneous forms).
The TxGNN model predicts it may be effective for **echinococcus granulosus infectious disease**,
but there are currently **0 clinical trials** and **0 publications** directly studying this disease, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leishmaniasis (including mucocutaneous and visceral leishmaniasis); recorded in the knowledge graph, as the US licence has no indication text in the data compiled for this report |
| Predicted New Indication | Echinococcus granulosus infectious disease |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Number of approvals | 1 NDA |
| Recommended Decision | Hold |

Two other predictions were also generated: alveolar echinococcosis (score 0.9921) and smouldering systemic mastocytosis (score 0.9905). Both are also L5 and Hold, and are discussed briefly below.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, miltefosine is an alkylphosphocholine with established antiparasitic activity against Leishmania and other protozoa. It is thought to disrupt lipid metabolism, membrane signaling and calcium homeostasis in parasites.

*Echinococcus granulosus* is a parasitic tapeworm (cestode) that causes cystic echinococcosis. A similar membrane-targeting effect on its larval stages (metacestodes or protoscoleces) is plausible, but this is unverified. The very high TxGNN score is a computational prediction only, and the supplied data contain no study that confirms the link.

**Other predicted indications**
- **Alveolar echinococcosis:** The same reasoning applies to the related tapeworm *Echinococcus multilocularis*. The only supplied publication (PMID 16940089) tested other drugs and, based on its title, does not evaluate miltefosine, so it gives no direct support.
- **Smouldering systemic mastocytosis:** No clear mechanistic link is evident. Miltefosine affects PI3K/Akt signaling and phospholipid metabolism, which could in theory influence mast cell survival, but this is speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For echinococcus granulosus infectious disease, currently no related literature is available.

For the related prediction alveolar echinococcosis, one publication was supplied, but it does not study miltefosine:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16940089](https://pubmed.ncbi.nlm.nih.gov/16940089/) | 2006 | In vitro study | Antimicrobial Agents and Chemotherapy | Tested itraconazole, methiazole and nitazoxanide against *E. multilocularis* larvae. Albendazole and mebendazole are the only licensed drugs for human alveolar echinococcosis. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204684 | IMPAVIDO (Profounda, Inc.) | Capsule (oral) | Not available in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication relations (not label text):** Sjogren-Larsson syndrome and congenital ichthyosiform erythroderma.
- **Drug Interactions:** Nine interactions are rated Moderate, mostly with hormonal contraceptives and related agents: levonorgestrel, norethisterone, desogestrel, ethinylestradiol, drospirenone, norgestrel, dienogest and norgestimate. Idelalisib is also rated Moderate.
- **Pharmacology:** Miltefosine is recorded as acting on the human AKT1 kinase target.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for echinococcus granulosus infectious disease is supported only by a high model score. No clinical trials or publications directly study this disease, so the evidence level is L5. The mechanism of action data are also missing.

**To proceed, the following is needed:**
- Preclinical validation (in vitro and animal studies) of miltefosine against *Echinococcus* larval stages
- Mechanism of action data for miltefosine
- FDA package insert warnings and contraindications for safety screening
- Comparison with the current standard of care (benzimidazoles and surgery) to define the clinical need
- Assessment of route and dosing suitability, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

