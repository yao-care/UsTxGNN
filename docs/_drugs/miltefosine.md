---
layout: default
title: Miltefosine
parent: Moderate Evidence (L3-L4)
nav_order: 931
evidence_level: L3
indication_count: 4
last_modified_at: 2026-10-14
description: "Miltefosine: predicted new indication Leishmaniasis, diffuse cutaneous (evidence level L3). Approved use: Leishmaniasis (including mucocutaneous and visceral leishmaniasis)"
monitor_inn: "MILTEFOSINE"
predicted_indications: ["leishmaniasis, diffuse cutaneous", "echinococcus granulosus infectious disease", "alveolar echinococcosis", "Smouldering systemic mastocytosis"]
---

# Miltefosine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

## Miltefosine: From Leishmaniasis to Diffuse Cutaneous Leishmaniasis
{: .text-alpha }

## One-Sentence Summary

Miltefosine is an oral alkylphosphocholine drug originally used to treat leishmaniasis (visceral, mucocutaneous and cutaneous forms).
The TxGNN model predicts it may be effective for **Diffuse Cutaneous Leishmaniasis**,
with **no registered clinical trials** but **20 publications** (mostly reviews and case reports) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leishmaniasis (including mucocutaneous and visceral leishmaniasis) |
| Predicted New Indication | Leishmaniasis, diffuse cutaneous |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| US Market Status | Cancelled only (the single NDA is cancelled) |
| Number of NDAs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on the published literature, miltefosine is an alkylphosphocholine with direct antileishmanial activity. It is thought to disrupt parasite lipid metabolism, membrane signaling and mitochondrial function.

Diffuse cutaneous leishmaniasis (DCL) is caused by the same family of *Leishmania* parasites as the approved indications. This prediction is therefore a close extension within the original indication class rather than a true repurposing. DCL is rare and severely disabling, and there is no established effective treatment.

Published reports describe a clinical response, but also relapse after treatment. They also include in vitro and in vivo susceptibility data for a *L. amazonensis* isolate from a patient with diffuse disease. Together these indicate real activity but limited durability.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32853410](https://pubmed.ncbi.nlm.nih.gov/32853410/) | 2020 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for American cutaneous and mucocutaneous leishmaniasis; pentavalent antimonials remain first choice, alternatives need effectiveness and safety review |
| [26938448](https://pubmed.ncbi.nlm.nih.gov/26938448/) | 2016 | Systematic review | PLoS Negl Trop Dis | Treatment of *L. aethiopica* cutaneous leishmaniasis, including diffuse and mucocutaneous forms; evidence-based guidelines are lacking |
| [34048461](https://pubmed.ncbi.nlm.nih.gov/34048461/) | 2021 | Pilot clinical study | PLoS Negl Trop Dis | Miltefosine for cutaneous leishmaniasis from *L. aethiopica* in Ethiopia; the only oral antileishmanial drug, with a more favourable side-effect profile than sodium stibogluconate |
| [17441955](https://pubmed.ncbi.nlm.nih.gov/17441955/) | 2007 | Case report | Br J Dermatol | Diffuse cutaneous leishmaniasis responded to miltefosine but then relapsed |
| [16796642](https://pubmed.ncbi.nlm.nih.gov/16796642/) | 2006 | Case report | Int J Dermatol | Miltefosine treatment of a 31-year-old man with lifelong diffuse cutaneous leishmaniasis |
| [17172368](https://pubmed.ncbi.nlm.nih.gov/17172368/) | 2006 | Case report | Am J Trop Med Hyg | Relapse of diffuse cutaneous leishmaniasis (*L. mexicana*) two months after miltefosine; lesions cleared after four months of treatment |
| [25033218](https://pubmed.ncbi.nlm.nih.gov/25033218/) | 2014 | In vitro / in vivo study | PLoS Negl Trop Dis | Miltefosine susceptibility of a *L. amazonensis* isolate from a patient with diffuse cutaneous leishmaniasis |
| [26568336](https://pubmed.ncbi.nlm.nih.gov/26568336/) | 2015 | Review | J Am Acad Dermatol | Differential diagnosis, diagnosis, histopathology and management of cutaneous and mucocutaneous leishmaniasis |
| [18721114](https://pubmed.ncbi.nlm.nih.gov/18721114/) | 2008 | Review | Expert Opin Drug Metab Toxicol | Status of miltefosine as the first oral leishmaniasis treatment, first registered in 2002 for Indian visceral leishmaniasis |
| [16597200](https://pubmed.ncbi.nlm.nih.gov/16597200/) | 2006 | Review | Expert Rev Anti Infect Ther | Oral miltefosine as an alternative to pentavalent antimony for leishmaniasis |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204684 (cancelled) | IMPAVIDO | Capsule | Not listed in the data compiled for this report |

## Safety Considerations

- **Contraindications (from knowledge-graph relationships, not label text)**: Sjögren-Larsson syndrome and congenital ichthyosiform erythroderma.
- **Drug Interactions**: 9 moderate-level interactions were identified, mainly with hormonal contraceptives and related agents: levonorgestrel, norethisterone, desogestrel, ethinylestradiol, drospirenone, norgestrel, dienogest and norgestimate. A moderate interaction with idelalisib was also identified. Miltefosine also acts on AKT serine/threonine kinase 1 (AKT1).

Please refer to the package insert for other safety information, including warnings.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
DCL is a *Leishmania* infection within the same class as miltefosine's original indications, and case reports and susceptibility data show activity. However, the evidence is limited to case reports, small studies and reviews, relapse after treatment is repeatedly documented, and there are no registered clinical trials.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently missing and blocking for safety screening)
- Detailed mechanism of action data
- Controlled studies or prospective trials evaluating durability of response and relapse prevention in DCL
- Current US availability review, since the only NDA is cancelled
- Safety management plan for drug interactions with hormonal contraceptives

**Other predicted indications (not recommended to advance now):** Echinococcus granulosus infection, alveolar echinococcosis and smouldering systemic mastocytosis (TxGNN scores 99.41%, 99.21% and 99.05%). All are L5, model prediction only, with no supporting trials or direct literature on miltefosine, so the decision for each is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

