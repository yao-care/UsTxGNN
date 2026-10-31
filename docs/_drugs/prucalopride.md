---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 1097
evidence_level: L5
indication_count: 10
monitor_inn: "PRUCALOPRIDE"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
last_modified_at: 2026-10-31
description: "Prucalopride: predicted new indication Hypoalphalipoproteinemia (evidence level L5). Approved use: Constipation disorder"
---

# Prucalopride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Prucalopride: From Constipation Disorder to Hypoalphalipoproteinemia
{: .text-alpha }

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist that was originally used to treat chronic constipation.
The TxGNN model predicts it may be effective for **Hypoalphalipoproteinemia** (low HDL cholesterol), but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 13) |
| Number of FDA Applications | at least 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, prucalopride is a selective 5-HT4 receptor agonist that enhances gut motility, and its efficacy in constipation is established.

For the top prediction, hypoalphalipoproteinemia, no mechanistic link can be identified. 5-HT4 agonism acts on gut motility and has no known role in HDL metabolism or ApoA-I regulation. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are similarly weak. Homozygous familial hypercholesterolemia, obsolete familial combined hyperlipidemia, oral candidiasis, strongyloidiasis, HIV infection and acquired amyloid peripheral neuropathy have no plausible mechanism and no supporting evidence. Duodenal ulcer is speculative, because prucalopride is neither acid-suppressive nor mucosal-protective.

The only predictions with some indirect rationale are **amyloidosis** and **primary amyloidosis**. Amyloid infiltration of the gut can cause dysmotility and chronic intestinal pseudo-obstruction, where a prokinetic could relieve symptoms. This would be symptomatic benefit only, not disease modification. Amyloid-related autonomic dysfunction may also limit response.

## Clinical Trial Evidence

Currently no related clinical trials registered for hypoalphalipoproteinemia, nor for any of the other nine top-ranked predicted indications.

## Literature Evidence

Currently no related literature available for hypoalphalipoproteinemia.

For the amyloidosis-related predictions, the following papers were retrieved. Neither tests prucalopride, so they provide context only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case report | Cureus | A 61-year-old man with amyloidosis presenting as chronic intestinal pseudo-obstruction after repeated hospitalizations and laparotomies without a diagnosis |
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohort/Review | Turk J Gastroenterol | Specific GI motility disorders (gastroparesis, pseudo-obstruction, colonic inertia) are often misdiagnosed as functional GI disorders in the early stage |

## US Market Information

The drug is marketed, with 13 valid licenses. The data compiled for this report contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210166 | MOTEGRITY (Takeda) | Film-coated tablet | Not available |
| ANDA218812 | Prucalopride (SKG Pharma) | Film-coated tablet | Not available |
| ANDA218847 | Prucalopride (Lupin) | Film-coated tablet | Not available |
| ANDA218177 | Prucalopride (Novadoz) | Film-coated tablet | Not available |
| ANDA219078 | Prucalopride succinate (Somerset) | Tablet | Not available |

Eight further ANDAs from Zydus, Apotex, Ajanta, Hikma, Sandoz, Cipla, ANI and SpecGx are also recorded as cancelled.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): ulcerative colitis, inflammatory bowel disease and intestinal perforation.
- **Drug Interactions**: 98 interactions are recorded. Examples include:
  - Moderate: aclidinium, atropine, benzatropine, biperiden, clidinium, glycopyrronium and hyoscyamine (anticholinergics, which oppose the prokinetic effect); levonorgestrel, norethisterone and ethinylestradiol (hormonal agents).
  - Minor: nifedipine, afatinib, alpelisib, amiodarone, cobicistat, captopril, diltiazem, spironolactone, carvedilol and conivaptan.
- The large interaction count would need attention in polypharmacy settings such as HIV treatment.

Package insert warnings and contraindications were not available, so please refer to the package insert for the complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hypoalphalipoproteinemia, has no identifiable mechanistic link, no clinical trials and no literature (L5, model prediction only). The drug is marketed, with 13 valid US licenses. The amyloidosis-related predictions have only indirect, symptomatic rationale and could be treated as research questions rather than development candidates.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence of a biological link between 5-HT4 agonism and HDL metabolism, or a re-ranking toward more plausible indications
- For the amyloidosis-related GI dysmotility, a focused literature search and a feasibility assessment of symptomatic prokinetic use
- Clarification of the US market status, since 13 licenses are shown as valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

