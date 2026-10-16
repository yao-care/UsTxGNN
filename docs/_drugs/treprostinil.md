---
layout: default
title: Treprostinil
parent: Model Prediction Only (L5)
nav_order: 1256
evidence_level: L5
indication_count: 10
monitor_inn: "TREPROSTINIL"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "pulmonary arterial hypertension associated with chronic hemolytic anemia", "pulmonary arterial hypertension associated with schistosomiasis", "pulmonary arterial hypertension associated with connective tissue disease", "pulmonary arterial hypertension associated with HIV infection", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita"]
last_modified_at: 2026-10-14
description: "Treprostinil: predicted new indication Pulmonary arteriovenous malformation (evidence level L5). Approved use: Pulmonary arterial hypertension"
---

# Treprostinil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Treprostinil: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Treprostinil is a prostacyclin analogue originally used to treat pulmonary arterial hypertension (PAH).
The TxGNN model's top-ranked prediction is **pulmonary arteriovenous malformation**, but it has **0 clinical trials** and **0 publications** behind it. The strongest evidence in the data compiled for this report is for the PAH subgroup **PAH associated with connective tissue disease** (1 placebo-controlled RCT in general PAH, plus a meta-analysis and reviews), which is largely an extension within the approved PAH indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension |
| Predicted New Indication | Pulmonary arteriovenous malformation (top-ranked prediction) |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (top prediction); best among the top 10 predictions is L3 (PAH associated with connective tissue disease) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 9 (all cancelled; includes both NDAs and ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known pharmacology, treprostinil is a prostacyclin (PGI2) analogue. It acts on IP receptors to cause vasodilation, inhibit platelet aggregation, and reduce vascular cell proliferation. Its efficacy in PAH is established.

Most of the top-10 predictions are PAH subgroups (congenital heart disease, chronic hemolytic anemia, schistosomiasis, connective tissue disease, HIV infection). These share the same WHO Group 1 pathophysiology, so the mechanism plausibly carries over. These are better viewed as extensions within the approved indication than as true repurposing.

The top-ranked prediction, pulmonary arteriovenous malformation, is different. Vasodilating a malformation could worsen shunting and hypoxemia, so the mechanistic rationale is weak and potentially harmful. The hair-disorder and developmental-syndrome predictions (ranks 7-10: hypotrichosis simplex of the scalp, congenital hypotrichosis milia, malformation syndrome with odontal/periodontal component, Ambras-type hypertrichosis) have no identified mechanistic link and likely reflect graph proximity only.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or any of the other top-10 predictions.

## Literature Evidence

The top-ranked prediction (pulmonary arteriovenous malformation) has no related literature. The table below covers the best-supported prediction, PAH associated with connective tissue disease (rank 5).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | RCT | Am J Respir Crit Care Med | 12-week double-blind, placebo-controlled trial of continuous subcutaneous treprostinil in PAH (not CTD-specific) |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review | Intern Emerg Med | Meta-analysis of RCT subgroup data on PAH treatment in connective tissue disease |
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | Clinical study | Chest | Efficacy and safety of continuous subcutaneous treprostinil in PAH with connective tissue disease |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review | Biomolecules | Current therapeutic strategies and future prospects in CTD-PAH |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals | Recent advances in treating PAH associated with connective tissue disease |
| [22291467](https://pubmed.ncbi.nlm.nih.gov/22291467/) | 2012 | Review | Drug Des Devel Ther | Therapeutic review of inhaled treprostinil |
| [34462153](https://pubmed.ncbi.nlm.nih.gov/34462153/) | 2021 | Retrospective study | Rev Med Interne | Characteristics and outcomes of CTD-PAH patients treated with prostanoids |

For PAH associated with congenital heart disease (rank 2), supporting data are limited to observational work, for example subcutaneous treprostinil in adult CHD-PAH ([29436381](https://pubmed.ncbi.nlm.nih.gov/29436381/), 2018, Heart, cohort) and long-term continuous prostacyclin therapy ([23890862](https://pubmed.ncbi.nlm.nih.gov/23890862/), 2013, Int J Cardiol, cohort of 8 adults). For PAH associated with HIV infection (rank 6), only general prostanoid reviews are available, with no HIV-specific data.

## US Market Information

All nine US authorizations are cancelled; none is currently valid. Approved indication text was not available in the data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021272 | Remodulin | Injection, solution | Not available |
| NDA022387 | Tyvaso | Inhalant | Not available |
| NDA214324 | Tyvaso DPI | Inhalant | Not available |
| NDA203496 | Orenitram | Tablet, extended release | Not available |
| NDA213005 | Yutrepia | Capsule | Not available |

Four generic injection ANDAs (Dr. Reddy's, Alembic, Sandoz, Teva) are also listed as cancelled.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, blood coagulation disease, lung disease, obsolete rare pulmonary disease.
- **Drug Interactions:** 100 interactions were recorded. Those rated Moderate include epinephrine, acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), mannitol, glycerin, papaverine, ephedrine, fenfluramine, dexfenfluramine, and sibutramine. Several others (e.g., pantoprazole, omeprazole, lansoprazole, prednisone, simvastatin, potassium chloride) have an unknown severity level.
- Given its antiplatelet effect and the blood coagulation disease flag, bleeding risk with concomitant antithrombotics warrants attention. Vasodilation of a pulmonary vascular malformation may also worsen shunting.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, pulmonary arteriovenous malformation, has only a model score, no trials or literature, and a mechanistic concern (possible worsening of shunting). The better-supported predictions are PAH subgroups, which are largely covered by the existing PAH indication. All nine US authorizations are also cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- For PAH subgroups (CTD-PAH, CHD-PAH): dedicated trials or registry analyses, and confirmation of current US marketing status
- For pulmonary arteriovenous malformation: preclinical or hemodynamic safety data on shunting and oxygenation before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

