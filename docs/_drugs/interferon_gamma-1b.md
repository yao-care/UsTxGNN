---
layout: default
title: Interferon Gamma-1B
parent: 僅模型預測 (L5)
nav_order: 803
evidence_level: L5
indication_count: 10
---

# Interferon Gamma-1B
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

# Interferon Gamma-1b: From Chronic Granulomatous Disease to Heart Disease

## One-Sentence Summary

Interferon gamma-1b is an immunomodulatory cytokine originally indicated for chronic granulomatous disease (CGD) and severe malignant osteopetrosis. The TxGNN model predicts it may be effective for **Heart Disease**, but this direction is currently supported by **0 directly relevant clinical trials** and **0 directly relevant publications** out of 50 trials and 5 papers retrieved — the evidence collected is dominated by keyword-matching noise rather than true drug-disease evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Granulomatous Disease (CGD); severe, malignant osteopetrosis (per repurposing rationale; not present in structured license data) |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action (MOA) data for this candidate is flagged as a data gap in the evidence pack. Based on the information available, interferon gamma-1b is known to activate macrophages, enhance phagocytic killing, and promote a pro-inflammatory immune response — the basis for its approved use in chronic granulomatous disease and malignant osteopetrosis. This is a fundamentally pro-inflammatory mechanism.

Heart disease, as a broad category, generally responds better to anti-inflammatory or cardioprotective mechanisms rather than immune activation. None of the 50 clinical trials retrieved for this pairing actually test interferon gamma-1b in a cardiac indication — the search results are populated by unrelated exercise-rehabilitation trials, trials of other drugs (liraglutide, ritlecitinib, cyclosporine, ALKS 4230, etc.), and general inflammation-biomarker studies. This is consistent with the pipeline's own assessment that this match is likely a keyword/pipeline mismatch rather than genuine mechanistic evidence.

The single literature item with plausible relevance is a case report of aspergillus constrictive pericarditis in a CGD patient — this describes a disease complication in a patient population that happens to use this drug, not a treatment effect on heart disease. Overall, the mechanistic rationale for this specific pairing is weak, and the directionality (pro-inflammatory vs. the anti-inflammatory/cardioprotective mechanisms typically sought in heart disease) raises concern rather than support.

---

## Clinical Trial Evidence

None of the retrieved trials directly test interferon gamma-1b for heart disease. The table below lists the top trials returned by the search, with their assessed relevance noted — all were graded "C" (not relevant / keyword mismatch):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03652519](https://clinicaltrials.gov/study/NCT03652519) | NA | Completed | 72 | Aerobic exercise rehabilitation in multiple sclerosis; does not involve interferon gamma-1b |
| [NCT04356248](https://clinicaltrials.gov/study/NCT04356248) | NA | Completed | 106 | High-intensity training vs. standard training in MS; unrelated to the drug |
| [NCT03672812](https://clinicaltrials.gov/study/NCT03672812) | Phase 3 | Completed | 50 | Tests liraglutide in brain-death organ donors, not interferon gamma-1b |
| [NCT07099911](https://clinicaltrials.gov/study/NCT07099911) | NA | Recruiting | 20 | Neuromuscular electrical stimulation for glucose control; unrelated |
| [NCT05650333](https://clinicaltrials.gov/study/NCT05650333) | Phase 1 | Completed | 15 | PK/PD of ritlecitinib (JAK inhibitor) in alopecia areata; not this drug |
| [NCT05027958](https://clinicaltrials.gov/study/NCT05027958) | Early Phase 1 | Completed | 17 | Bronchoscopic mycobacterial antigen instillation study; not a drug intervention trial for heart disease |
| [NCT02489383](https://clinicaltrials.gov/study/NCT02489383) | NA | Unknown | 60 | Continuous vs. interval aerobic exercise in asthma; unrelated |
| [NCT00974142](https://clinicaltrials.gov/study/NCT00974142) | Phase 1/2 | Completed | 43 | Oral cyclosporine in advanced COPD; not this drug |
| [NCT03904277](https://clinicaltrials.gov/study/NCT03904277) | N/A | Completed | 28 | Observational study of patent foramen ovale size; no drug intervention |
| [NCT02799095](https://clinicaltrials.gov/study/NCT02799095) | Phase 1/2 | Completed | 243 | ALKS 4230 ± pembrolizumab in solid tumors; not this drug |

**Note:** 40 additional trials were retrieved but not yet graded for relevance ("pending"); a manual scan of titles found none that test interferon gamma-1b specifically for a cardiac indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28990950](https://pubmed.ncbi.nlm.nih.gov/28990950/) | 2017 | Case Report | Turk Kardiyoloji Dernegi Arsivi | Pediatric CGD patient with constrictive aspergillus pericarditis and congestive heart failure — a disease complication in a CGD patient, not a treatment study of the drug for heart disease |
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Review | Therapeutic Advances in Rare Disease | Systematic review of interventions in Friedreich ataxia; unrelated to heart disease indication |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Case Report | European Heart Journal – Case Reports | Mycobacterium chimaera prosthetic valve endocarditis after cardiac surgery; does not involve this drug |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Validation Study | American Journal of Respiratory and Critical Care Medicine | Validation of the 6-minute-walk test in idiopathic pulmonary fibrosis; unrelated to this drug or heart disease |

None of the retrieved literature demonstrates a treatment effect of interferon gamma-1b on heart disease.

---

## US Market Information

Interferon gamma-1b is currently **not marketed** in this jurisdiction, and no license/NDA records were found (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warning, contraindication, and drug-interaction data were not available at this data cutoff (2026-08-13); TFDA labeling has not yet been retrieved (see Conclusion, below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted pairing (interferon gamma-1b → heart disease) is supported only by a raw TxGNN model score, with no clinical trial or literature evidence that directly tests the drug in a cardiac indication — the retrieved evidence is best explained as pipeline/keyword noise. The drug's known pro-inflammatory mechanism (macrophage activation) also runs counter to the anti-inflammatory/cardioprotective mechanisms typically sought in heart disease, making the biological rationale weak.

**To proceed, the following is needed:**
- Official TFDA label/package insert (warnings, contraindications) — currently a blocking data gap
- Verified DrugBank mechanism-of-action data
- A disease-specific literature/trial search (e.g., restricting "heart disease" to a defined subtype) rather than the broad category used here, to rule out further keyword mismatch
- If genuine mechanistic or preclinical rationale for a specific cardiac subtype emerges, re-evaluate at L3/L4 with targeted evidence collection

**Additional note on lower-ranked candidates:** Ranks 2–10 (Jeune syndrome, orofacial clefting, Pierre Robin syndrome variants, chromosomal deletions, Laubry-Pezzi syndrome, interventricular septum aneurysm) returned **zero** clinical trials and **zero or off-target** literature, corresponding to Evidence Level L5 (model prediction only). These are not viable candidates for further evaluation at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

