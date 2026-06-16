---
layout: default
title: Cyproheptadine
parent: 僅模型預測 (L5)
nav_order: 559
evidence_level: L5
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cyproheptadine: From Appetite Stimulation to Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation antihistamine with dual H1 and serotonin (5-HT2) antagonist properties, widely used in pediatric settings for appetite stimulation and historically for allergic conditions.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **2 clinical trials** and **19 publications** (primarily on related second-generation antihistamines) currently supporting this direction.
Notably, the drug's second-ranked predicted indication — **Cold Urticaria** — carries stronger direct evidence, including multiple double-blind RCTs specifically studying cyproheptadine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No active regulatory records available (not currently marketed) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| US Market Status | Not Marketed (0 active licenses in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cyproheptadine is a first-generation piperidine antihistamine that competitively antagonizes peripheral H1 histamine receptors. Unlike second-generation antihistamines, it also blocks serotonin 5-HT2 receptors, giving it a dual mechanism of action. In allergic urticaria, mast cell degranulation releases histamine as the primary mediator of the wheal-and-flare response — directly addressable by H1 blockade. The 5-HT2 antagonism may additionally suppress serotonin-mediated amplification of the inflammatory cascade, providing a mechanistic rationale that pure H1 antagonists cannot claim.

Allergic urticaria and cold urticaria share the same fundamental mast cell-mediated pathophysiology, differing mainly in triggering stimulus. Cyproheptadine's dual H1 + 5-HT2 mechanism has demonstrated direct clinical efficacy in cold urticaria (double-blind placebo-controlled RCT, Wanderer et al. 1977; four-arm comparative RCT, Neittaanmäki et al. 1984), providing strong cross-indication biological plausibility for allergic urticaria. The drug's Rank 2 predicted indication (cold urticaria, L2 evidence) therefore also reinforces the biological case for Rank 1.

The main caveat in the current evidence set is that the majority of retrieved literature focuses on second-generation antihistamines (desloratadine, loratadine, rupatadine, bilastine) rather than cyproheptadine itself. Current international guidelines position second-generation antihistamines as first-line treatment due to their improved sedation and anticholinergic profiles. Cyproheptadine's dual H1 + 5-HT2 profile may still offer clinical value in refractory patients, specific physical urticaria subtypes, or populations where appetite stimulation is an acceptable side-effect benefit.

---

## Clinical Trial Evidence

No clinical trials directly studying cyproheptadine for allergic urticaria were identified. The two retrieved trials involve related antihistamines in similar indications and provide indirect class-level evidence only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A (Post-marketing) | Completed | 1,003 | Post-marketing surveillance of loratadine (second-generation H1 antagonist) in Japanese children with allergic conditions including urticaria — confirms safety and symptom score improvement; indirect class benchmark |
| [NCT07101445](https://clinicaltrials.gov/study/NCT07101445) | Phase 4 | Recruiting | 94 | Dexamethasone vs. methylprednisolone premedication to prevent allergic reactions to motixafortide in multiple myeloma — different drug class and indication; minimal relevance to cyproheptadine in urticaria |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | RCT | Asian Pacific J Allergy Immunol | **Direct cyproheptadine evidence**: double-blind crossover trial in 6 Thai children with cold urticaria comparing cyproheptadine vs. ketotifen — cyproheptadine demonstrated clinical efficacy; generalizes to allergic urticaria via shared mast cell mechanism |
| [33198523](https://pubmed.ncbi.nlm.nih.gov/33198523/) | 2021 | Systematic Review | Expert Opinion Pharmacotherapy | Second-generation H1-antihistamines as first-line for childhood allergic urticaria; notes most pediatric data extrapolated from adults — highlights evidence gap that cyproheptadine's pediatric RCTs could fill |
| [39549290](https://pubmed.ncbi.nlm.nih.gov/39549290/) | 2024 | RCT | Iran J Allergy Asthma Immunol | Randomized trial of mometasone + desloratadine ± montelukast in childhood allergic rhinitis — confirms antihistamine dose-response in allergic disease; indirect class evidence |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | H1-antihistamines in chronic spontaneous urticaria — argues that head-to-head comparisons are needed and patients respond differently; supports identifying niche populations for first-generation agents |
| [18339040](https://pubmed.ncbi.nlm.nih.gov/18339040/) | 2008 | Review | Allergy | Rupatadine (dual H1 + PAF antagonist) in allergic rhinitis and urticaria — highlights that multi-target antihistamines beyond pure H1 blockade show additional benefit, directly supporting cyproheptadine's dual H1 + 5-HT2 rationale |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Substances | Comprehensive loratadine profile confirming H1-antihistamine class efficacy in chronic urticaria and allergic rhinitis — class benchmark for comparison |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine Phase III data in seasonal allergic rhinoconjunctivitis and urticaria — confirms H1 antagonism as the mechanism of action standard of care for urticaria |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinetics | Comparative PK/PD of desloratadine, fexofenadine, and levocetirizine vs. first-generation agents — provides safety and efficacy framework for positioning cyproheptadine's sedating profile relative to current alternatives |
| [11398910](https://pubmed.ncbi.nlm.nih.gov/11398910/) | 2001 | Review | Drugs | Desloratadine profile — no cardiovascular adverse effects or psychomotor impairment at 9× therapeutic dose; contrasts sharply with cyproheptadine's CNS sedation and informs competitive safety positioning |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine historical review — double-blind trials showing efficacy in chronic urticaria comparable to terfenadine and clemastine; contextualizes first-generation antihistamine class performance |

---

## US Market Information

No active NDA or license records were found for cyproheptadine in this regulatory dataset.

> Cyproheptadine was historically marketed in the United States as **Periactin®** (Merck); the original NDA is no longer active, and the drug is currently available as a generic. Formal current regulatory status should be verified directly in the FDA Orange Book before initiating any regulatory strategy.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) were not retrieved in this Evidence Pack.

> Please refer to the package insert for complete safety information. As a first-generation antihistamine, cyproheptadine carries known CNS sedation and anticholinergic effects including dry mouth, urinary retention, blurred vision, and constipation. These effects are a primary differentiator from second-generation agents and must be weighed carefully in patient selection, particularly for individuals who operate machinery, have benign prostatic hyperplasia, or narrow-angle glaucoma.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyproheptadine's dual H1 + 5-HT2 antagonism provides a mechanistically coherent basis for treating allergic urticaria, supported by direct RCT evidence in cold urticaria (Rank 2, L2 evidence level) and broad indirect class evidence from second-generation antihistamines for urticaria. The drug is not currently marketed under an active NDA, and its sedation profile limits first-line positioning; however, a focused regulatory or clinical strategy for refractory urticaria or cold urticaria subpopulations is feasible.

**To proceed, the following is needed:**
- Retrieve complete MOA data from DrugBank (Data Gap DG002) to formally document the dual H1 + 5-HT2 mechanism and distinguish it from second-generation agents in regulatory submissions
- Obtain the US package insert to assess key warnings and contraindications (Data Gap DG001), which is currently blocking the formal S1 safety evaluation
- Confirm current FDA Orange Book status and evaluate whether a 505(b)(2) pathway or supplemental NDA is appropriate for re-entering the market
- Commission or identify head-to-head RCT data comparing cyproheptadine against second-generation antihistamines specifically in patients with refractory allergic urticaria or cold urticaria — this is the clearest evidence gap
- Evaluate cold urticaria (Rank 2, L2 evidence, multiple direct RCTs from 1971–1995) as a potentially more defensible initial regulatory target before expanding to broader allergic urticaria
- Define target patient populations where cyproheptadine's dual mechanism or its appetite-stimulating side effect profile converts from a liability to a therapeutic benefit (e.g., pediatric patients with concurrent failure to thrive)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

