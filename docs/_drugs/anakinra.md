---
layout: default
title: Anakinra
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Rheumatoid Arthritis to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra is a recombinant interleukin-1 (IL-1) receptor antagonist, originally used for rheumatoid arthritis and cryopyrin-associated periodic syndromes (including CINCA syndrome).
The TxGNN model's top-ranked prediction is **Extracutaneous Mastocytoma**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
Among the other predicted indications, **autosomal recessive familial Mediterranean fever** and **pyogenic autoinflammatory syndrome** have the most supporting literature (19 and 14 publications respectively, mainly reviews, case reports and case series).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, cryopyrin-associated periodic syndrome, CINCA syndrome (the license record has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (the single BLA is recorded as cancelled) |
| Number of NDAs | 1 (BLA) |
| Recommended Decision | Hold |

**Other candidate indications from the same analysis:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 3 | Autosomal recessive familial Mediterranean fever | 99.89% | L3 | Research question |
| 9 | Pyogenic autoinflammatory syndrome | 99.83% | L3 | Research question |
| 10 | Unclassified autoinflammatory syndrome | 99.81% | L3 | Research question |
| 7–8 | Oligoarticular juvenile idiopathic arthritis (ANA-negative / ANA-positive) | 99.85% | L4 | Hold |
| 2, 4, 5, 6 | Hepatic infarction, aggressive systemic mastocytosis, hepatic veno-occlusive disease, peliosis hepatis | 99.88–99.89% (aggressive systemic mastocytosis 99.88%, hepatic veno-occlusive disease 99.88%, peliosis hepatis 99.85%) | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Based on known information, anakinra blocks IL-1 receptor signaling. Its efficacy in rheumatoid arthritis and cryopyrin-associated periodic syndromes is established, and both conditions involve IL-1-driven inflammation.

For the top-ranked prediction, extracutaneous mastocytoma, the data compiled for this report shows only a TxGNN score of 0.999. IL-1 signaling has a theoretical role in mast cell-driven inflammation, but no direct link to anakinra was shown, and no trials or literature were found. The prediction should therefore be treated as a hypothesis only.

The mechanistic rationale is considerably stronger for the autoinflammatory predictions:

- **Familial Mediterranean fever (FMF):** MEFV (pyrin) mutations lead to inflammasome activation and excess IL-1β, which anakinra directly targets.
- **PAPA/PASH/PAPASH spectrum (pyogenic autoinflammatory syndrome):** PSTPIP1 mutations cause pyrin-inflammasome dysregulation and IL-1 overproduction.
- **Unclassified autoinflammatory syndromes:** These often show IL-1-driven inflammation, and anakinra is used empirically.

For the remaining low-evidence predictions (hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis), no plausible mechanistic rationale can be established from the available data, and the high graph scores may be network artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

**Top-ranked prediction (extracutaneous mastocytoma):** Currently no related literature available.

**Most evidence-supported prediction: autosomal recessive familial Mediterranean fever** (selected examples; none are RCTs)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Case series + review | Semin Arthritis Rheum | IL-1-targeting drugs in FMF, with rationale that pyrin is implicated in IL-1 maturation and secretion |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Cohort (canakinumab, class-effect evidence) | Rheumatol Int | Canakinumab effective in FMF resistant or intolerant to colchicine and/or anakinra |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review | Clin Rev Allergy Immunol | IL-1β biological treatment of FMF |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Case report | Nephrol Dial Transplant | Successful anakinra treatment of FMF and outcome after renal transplantation |
| [20386914](https://pubmed.ncbi.nlm.nih.gov/20386914/) | 2012 | Case report | Rheumatol Int | Anakinra efficacy in a patient with colchicine-resistant FMF and secondary amyloidosis |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Case series | Nephrol Dial Transplant | IL-1 inhibitor treatment in FMF complicated by amyloidosis and renal failure |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Case series | J Pak Med Assoc | Anakinra and canakinumab used successfully in four colchicine-resistant patients |
| [32655029](https://pubmed.ncbi.nlm.nih.gov/32655029/) | 2020 | Case report | Iran J Kidney Dis | Late acute cellular rejection after anakinra in a kidney transplant patient; the authors question whether this was coincidental |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Case report | Joint Bone Spine | Myositis in FMF with spondyloarthritis successfully treated with anakinra |

**Pyogenic autoinflammatory syndrome (PAPA/PASH/PAPASH)** (selected examples)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Systematic/scoping review | Front Immunol | Efficacy and safety of anakinra and canakinumab in PSTPIP1-associated inflammatory diseases |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Case report + literature review | Cureus | Anakinra in PAPASH spectrum disorder |
| [38006373](https://pubmed.ncbi.nlm.nih.gov/38006373/) | 2023 | Case report/review | Acta Dermatovenerol Croat | Challenges in achieving long-term remission in PAPA syndrome, suggesting variable response |
| [24275598](https://pubmed.ncbi.nlm.nih.gov/24275598/) | 2013 | Review | Semin Immunol | Overview of IL-1 blockade in human inflammatory disease |

**Unclassified autoinflammatory syndrome** (selected examples)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36589607](https://pubmed.ncbi.nlm.nih.gov/36589607/) | 2022 | Retrospective cohort (single center) | Arch Rheumatol | Efficacy of anakinra in pediatric rheumatic diseases |
| [41904303](https://pubmed.ncbi.nlm.nih.gov/41904303/) | 2026 | Case report | Eur Arch Otorhinolaryngol | TRAPS-like unclassified syndrome controlled with canakinumab (not anakinra) |
| [37747561](https://pubmed.ncbi.nlm.nih.gov/37747561/) | 2024 | Cohort | Rheumatol Int | German GARROD registry: clinical and genetic characteristics of patients on anti-IL-1 therapy |

**Aggressive systemic mastocytosis:** The two retrieved papers ([40718535](https://pubmed.ncbi.nlm.nih.gov/40718535/), [25840575](https://pubmed.ncbi.nlm.nih.gov/25840575/)) describe Schnitzler syndrome case reports and appear mismatched to this indication, so they do not support it.

**Oligoarticular juvenile idiopathic arthritis:** Only one general review is available ([28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/), 2017, Balkan Med J), with no oligoarticular-specific anakinra data.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103950 (cancelled) | Kineret (Swedish Orphan Biovitrum AB) | Injection, solution | Not provided in the license record |

---

## Safety Considerations

- **Drug Interactions:** 100 interactions were identified in total, and the entries reviewed fall mainly in the Moderate category.
  - **Major:** Deferiprone.
  - **Moderate:** Corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone), simvastatin, radiopharmaceuticals and related agents (ibritumomab tiuxetan, iobenguane I-131, tositumomab), and anticoagulants (apixaban, dicoumarol, rivaroxaban).
  - **Minor:** Zinc salts (acetate, gluconate, sulfate).
- A case report in a kidney transplant patient described late acute cellular rejection after anakinra; a causal link is uncertain.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, extracutaneous mastocytoma)

**Rationale:**
The top-ranked prediction rests on a model score alone (L5), with no trials, no literature, and no demonstrated mechanistic link to anakinra. Its high score should not be read as evidence of efficacy. Among the other predictions, familial Mediterranean fever, pyogenic autoinflammatory syndrome, and unclassified autoinflammatory syndrome have a more credible IL-1-based rationale and L3 evidence (case series, reviews, class-level data). They are better candidates for further research questions than the top-ranked prediction, but none has randomized trial support.

**To proceed, the following is needed:**
- Confirm whether the cancelled BLA reflects a true loss of US marketing status or a data-source artifact, since the market status entry shows "Cancelled only".
- Obtain the current package insert so that warnings and contraindications can be reviewed.
- Obtain detailed mechanism-of-action data.
- For extracutaneous mastocytoma: a targeted literature search and a preclinical evaluation of IL-1 involvement in mast cell disease.
- For the autoinflammatory candidates: a systematic evaluation of the case-level evidence, and registry or prospective study design where feasible.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

