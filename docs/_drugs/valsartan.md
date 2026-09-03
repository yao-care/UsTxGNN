---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 1282
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the drug-repurposing evaluation report format to synthesize this evidence pack. Note: this is a **multi-indication candidate** (7 TxGNN predictions for valsartan), so I lead with the indication carrying the strongest actual evidence — **chronic pulmonary heart disease** (rank 6, the only candidate with registered trials and tiered literature) — rather than the top TxGNN score (rank 1), which has essentially no supporting evidence. All seven candidates are summarized in a portfolio table so nothing is hidden.

---

# Valsartan: From Hypertension to Chronic Pulmonary Heart Disease (Cor Pulmonale)

## One-Sentence Summary

> Valsartan is a well-established angiotensin II receptor blocker (ARB), originally used for hypertension, heart failure, and post-myocardial infarction management (this specific indication text is not captured in the evidence pack).
> TxGNN generated **7 candidate new indications** for valsartan; among them, **chronic pulmonary heart disease (cor pulmonale)** has the strongest actual evidence base, supported by **7 registered clinical trials** and **20 publications** — mostly relating to sacubitril/valsartan in heart failure patients with comorbid COPD/pulmonary hypertension, rather than trials designed specifically for cor pulmonale.
> The remaining six predicted indications (malignant renovascular hypertension, pulmonary hypertension subtypes, Prinzmetal angina, Braddock syndrome) have TxGNN scores as high as 99.97% but are backed by **no drug-specific clinical evidence** — several literature hits are off-topic (general hypoxia biology, wrong drug class) and should be treated as knowledge-graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (well-established ARB use; not itemized in this evidence pack) |
| Predicted New Indication (lead candidate) | Chronic Pulmonary Heart Disease (Cor Pulmonale) |
| TxGNN Prediction Score | 99.58% (rank 10,543 of embedding space) |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Predicted Indication Portfolio (All 7 Candidates)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|------------------|
| 1 | Malignant renovascular hypertension | 99.97% | L4 | S0 | Hold |
| 2 | Malignant hypertensive renal disease | 99.97% | L5 | S0 | Hold |
| 3 | Pulmonary hypertension owing to lung disease/hypoxia | 99.97% | L5 | S0 | Hold |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 99.97% | L5 | S0 | Hold |
| 5 | Braddock syndrome | 99.96% | L5 | S0 | Hold |
| **6** | **Chronic pulmonary heart disease** | **99.58%** | **L3** | **S1** | **Research Question** |
| 7 | Prinzmetal angina | 99.45% | L5 | S0 | Hold |

**Note on evidence quality:** TxGNN score is a graph-embedding similarity metric and does **not** correlate here with clinical evidence strength — rank 6 has the lowest score of the seven but by far the strongest supporting literature. Ranks 1, 2, and 7 cite literature studying a *different drug* (avosentan) or unrelated biology (T-wave alternans), not valsartan. Rank 5 (Braddock syndrome, a rare genetic developmental disorder) has no plausible mechanistic link to RAAS biology and should be treated as a likely graph artifact.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for valsartan is not available in this evidence pack (Data Gap DG002). Based on established pharmacology, valsartan is an angiotensin II type 1 (AT1) receptor blocker that inhibits the renin-angiotensin-aldosterone system (RAAS), reducing systemic vascular resistance and cardiac afterload — the basis for its approved use in hypertension and heart failure.

Chronic pulmonary heart disease (cor pulmonale) results from sustained pulmonary hypertension secondary to chronic lung disease, causing right ventricular pressure/volume overload and eventual right heart failure. Since RAAS activation contributes to ventricular remodeling in both left- and right-sided heart failure, ARB-based afterload reduction is mechanistically plausible for this indication. This is directly supported by PMID 32552157, which found that sacubitril/valsartan (an ARB-neprilysin inhibitor combination containing valsartan) attenuated right ventricular remodeling in a pulmonary hypertension model — the most mechanistically relevant single data point in this evidence pack.

However, most of the supporting clinical literature (PARADIGM-HF, PARAGON-HF subgroup analyses; VALIANT) studied valsartan or sacubitril/valsartan in **heart failure patients with comorbid COPD**, not in cor pulmonale as a primary, independently defined indication. This is an important distinction: the evidence supports a related population and a plausible mechanism, but not a dedicated efficacy trial in cor pulmonale itself.

---

## Clinical Trial Evidence

*(For lead candidate: Chronic Pulmonary Heart Disease)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02768298](https://clinicaltrials.gov/study/NCT02768298) | Phase 4 | Completed | 201 | RCT: LCZ696 (sacubitril/valsartan) vs. enalapril for exercise capacity in HFrEF. Grade B relevance — high-quality RCT but indication is HFrEF, not cor pulmonale specifically. |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Real-world retrospective study of sacubitril/valsartan in Indian HFrEF patients; Grade B — indirectly captures pulmonary hypertension/COPD comorbid subgroup. |
| [NCT06704633](https://clinicaltrials.gov/study/NCT06704633) | Phase 4 | Not yet recruiting | 238 | ARNI (sacubitril/valsartan) switch study in HFrEF, rural Tanzania — safety/benefit in an understudied population. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Empagliflozin + sacubitril/valsartan in adult congenital heart disease with HFrEF; Grade C — combination therapy, small sample. |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function/rehabilitation study in hypertension; Grade C — mechanistic, not disease-specific. |
| [NCT05428631](https://clinicaltrials.gov/study/NCT05428631) | N/A | Recruiting | 10 | CardioMEMS pulmonary artery pressure monitoring in cardio-renal syndrome; background/device study, not a drug trial. |
| [NCT06697353](https://clinicaltrials.gov/study/NCT06697353) | N/A | Completed | 4,936 | Real-world cohort of vericiguat (not valsartan) in Japanese HFrEF patients; background relevance only. |

**None of these trials use "chronic pulmonary heart disease" or "cor pulmonale" as the enrollment indication.** All represent adjacent evidence in HFrEF ± COPD/pulmonary hypertension comorbidity.

---

## Literature Evidence

*(For lead candidate: Chronic Pulmonary Heart Disease; top 10 of 20 available, prioritizing RCT/cohort evidence and mechanistic relevance)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32552157](https://pubmed.ncbi.nlm.nih.gov/32552157/) | 2020 | Preclinical/mechanistic | J Am Heart Assoc | Sacubitril/valsartan attenuated right ventricular remodeling in a pulmonary hypertension model — the most direct mechanistic support found. |
| [39210725](https://pubmed.ncbi.nlm.nih.gov/39210725/) | 2024 | RCT post-hoc (Tier 1) | JAMA Cardiology | Post-hoc analysis of PARADIGM-HF/PARAGON-HF: sacubitril/valsartan reduced all-cause hospitalization in HF, including comorbid populations. |
| [19176539](https://pubmed.ncbi.nlm.nih.gov/19176539/) | 2009 | Trial subgroup analysis (VALIANT) | Eur J Heart Fail | In the valsartan-specific VALIANT trial, COPD independently predicted mortality post-MI but not atherosclerotic events — valsartan-specific safety/outcome data. |
| [33522249](https://pubmed.ncbi.nlm.nih.gov/33522249/) | 2021 | RCT subgroup (PARADIGM-HF) | J Am Heart Assoc | HFrEF + COPD patients had worse outcomes; sacubitril/valsartan benefit direction preserved across COPD status. |
| [34796742](https://pubmed.ncbi.nlm.nih.gov/34796742/) | 2021 | Cohort (Tier 2, PARAGON-HF) | J Am Heart Assoc | COPD impact on HFpEF outcomes under sacubitril/valsartan (ARNI vs. ARB comparator). |
| [33706551](https://pubmed.ncbi.nlm.nih.gov/33706551/) | 2021 | Registry/Cohort (Tier 2) | Circ Heart Fail | Combined PARAGON-HF/PARADIGM-HF analysis of comorbidity burden and sacubitril/valsartan treatment effect across LVEF spectrum. |
| [18068611](https://pubmed.ncbi.nlm.nih.gov/18068611/) | 2007 | Cohort (Tier 2, Val-HeFT) | J Cardiac Fail | In the valsartan-specific Val-HeFT trial, COPD was an independent prognostic marker in chronic HF patients. |
| [40689605](https://pubmed.ncbi.nlm.nih.gov/40689605/) | 2026 | Meta-analysis of RCTs | Future Cardiology | ARNI vs. ACEi/ARB post-acute decompensated HF meta-analysis — supportive of angiotensin-pathway blockade generally. |
| [35413307](https://pubmed.ncbi.nlm.nih.gov/35413307/) | 2022 | Review (Tier 3) | Pharmacol Ther | Overview of contemporary chronic HF pharmacotherapy including RAAS/ARNI-based regimens. |
| [39433052](https://pubmed.ncbi.nlm.nih.gov/39433052/) | 2025 | Epidemiological review | Lancet Respir Med | Global Burden of Disease analysis establishing the epidemiological scale of pulmonary arterial hypertension, supporting unmet need. |

---

## Market Information

No Taiwan marketing authorizations were found in this evidence pack (`total_licenses = 0`, market status "未上市" / not marketed). This is itself a gating consideration — repurposing evaluation for an indication not currently marketed locally requires confirming import/registration pathway before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are flagged as **Data Gap (DG001, Blocking)** in this evidence pack — TFDA label warnings/contraindications have not yet been retrieved, and this blocks progression to the S1 safety pre-screen stage per the evidence pack's own scoring framework.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Among seven TxGNN-predicted indications, only chronic pulmonary heart disease has trial and literature support, and even that support is indirect (HFrEF + COPD comorbid subgroups using sacubitril/valsartan, not dedicated cor pulmonale trials). The remaining six candidates (including the two highest TxGNN scores) have no drug-specific clinical evidence and in several cases cite literature on unrelated drugs or biology. Combined with a **Blocking** data gap on TFDA warnings/contraindications, this candidate cannot progress past S1.

**To proceed, the following is needed:**
- Retrieve TFDA label warnings and contraindications (DG001 — blocking; required before any safety pre-screen)
- Retrieve formal DrugBank MOA record (DG002)
- If pursuing chronic pulmonary heart disease specifically: identify or design a trial using cor pulmonale (not general HFrEF/COPD comorbidity) as the primary enrollment indication
- Re-evaluate ranks 1–5 and 7 only if drug-specific (not off-target) literature emerges; current evidence for these is insufficient to justify further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

