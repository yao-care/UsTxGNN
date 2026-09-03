---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 992
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

> Omalizumab is a humanized anti-IgE monoclonal antibody whose established use, based on the literature in this evidence pack, is moderate-to-severe persistent allergic asthma (it is not currently marketed in this jurisdiction). The TxGNN model's top-ranked new indication is **Bronchitis** (specifically persistent eosinophilic bronchitis), but this is supported by only **2 clinical trials** and **8 publications**, most of which are indirect asthma studies rather than dedicated bronchitis research — evidence is currently insufficient to advance this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in this jurisdiction; literature in this pack identifies the globally approved use as moderate-to-severe persistent allergic asthma |
| Predicted New Indication | Bronchitis (persistent eosinophilic bronchitis) |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Omalizumab is an anti-IgE monoclonal antibody that blocks free IgE from binding to the FcεRI receptor, reducing mast cell and basophil degranulation. This mechanism is well established in IgE-mediated allergic asthma, where it reduces airway inflammation and improves clinical control.

Bronchitis, however, is a heterogeneous condition — most cases are infectious or irritant-driven (e.g., smoking-induced chronic bronchitis), which do not involve IgE-mediated pathways. Only a specific sub-phenotype, persistent eosinophilic bronchitis, shares the Th2/eosinophilic inflammatory features seen in asthma, giving a plausible but narrow mechanistic rationale for omalizumab's potential benefit.

Consistent with this, the supporting evidence in this pack is thin and largely indirect: the one trial that directly targets eosinophilic bronchitis enrolled only 11 patients and is explicitly graded "C" relevance (design centers on asthma with a steroid-sparing endpoint, not bronchitis as the primary condition); the second trial concerns chronic spontaneous urticaria, an unrelated allergic condition. The literature similarly consists mostly of asthma reviews that mention chronic bronchitis/COPD only in passing. Overall, this prediction should be treated as a weak, mechanistically-plausible-but-unproven signal rather than a validated repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Double-blind, placebo-controlled, 3-center trial testing whether adding omalizumab allows corticosteroid dose reduction in patients with asthma and persistent eosinophilic bronchitis. Small sample; design centers on steroid-sparing in an asthma population rather than bronchitis as the primary indication. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Completed | 382 | Dose-finding study of anti-IgE agent QGE031 as add-on therapy in chronic spontaneous urticaria (CSU). Not a bronchitis trial; included only via broad allergic-airway/IgE mechanism overlap. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical reviews in allergy & immunology | Overview of omalizumab's approval and post-approval experience in moderate-to-severe persistent asthma; no bronchitis-specific data. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Review | Current medical research and opinion | Pooled safety analysis of omalizumab in children with IgE-mediated allergic asthma; not bronchitis-specific. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postępy dermatologii i alergologii | Cohort study of omalizumab in older patients with severe allergic asthma-COPD overlap; indirectly touches on the chronic bronchitis phenotype within COPD overlap. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert opinion on pharmacotherapy | Discusses management challenges in asthma associated with smoking-induced airway disease (chronic bronchitis, emphysema, ACO); notes these patients are usually excluded from asthma trials, so omalizumab evidence here is uncertain. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergologia et immunopathologia | General review of monoclonal antibody use in pediatrics across multiple disease areas; only broadly mentions omalizumab, not bronchitis-specific. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Revue des maladies respiratoires | French expert review on adult asthma exacerbations; does not directly address bronchitis or omalizumab use in it. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui (Japanese Journal of Anesthesiology) | Review on perioperative management of bronchial asthma/chronic bronchitis patients; briefly notes omalizumab's availability for severe allergic asthma, not a bronchitis treatment study. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | Journal of investigational allergology & clinical immunology | Case report of plastic bronchitis following bronchial thermoplasty in a severe asthma patient — a rare adverse pulmonary event, not evidence of omalizumab efficacy for bronchitis. |

---

## US Market Information

This drug is not currently marketed in this jurisdiction (未上市, 0 licenses on file), so no license/authorization data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying evidence pack flags the absence of official label warnings/contraindications as a Blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between omalizumab's IgE-blocking action and bronchitis is plausible only for a narrow eosinophilic sub-phenotype, not bronchitis broadly. Direct supporting evidence is limited to one small (n=11), low-relevance trial, with the remaining trials and literature being largely indirect asthma-focused material. Combined with the missing safety/label data (Blocking gap), the evidence does not yet support advancement.

**To proceed, the following is needed:**
- TFDA/official label warnings and contraindications (currently a Blocking data gap, DG001)
- Formal DrugBank-sourced mechanism of action data (High-severity gap, DG002)
- A dedicated, adequately powered trial in confirmed eosinophilic (allergic) bronchitis patients, distinct from general asthma or smoking-related chronic bronchitis populations
- Clarification of whether "bronchitis" in this candidate should be narrowed to the eosinophilic phenotype only, to avoid conflating it with infectious/smoking-induced bronchitis where the mechanism does not apply
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

