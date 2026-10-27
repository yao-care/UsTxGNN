---
layout: default
title: Zileuton
parent: Model Prediction Only (L5)
nav_order: 1305
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Zileuton: predicted new indication Bronchitis (evidence level L5). Approved use: Intrinsic asthma, allergic asthma"
monitor_inn: "ZILEUTON"
predicted_indications: ["bronchitis", "obstructive lung disease", "atopic eczema", "bronchial neoplasm (disease)", "Laubry-Pezzi syndrome", "heart disease", "interventricular septum aneurysm", "genetic syndromic Pierre Robin syndrome"]
---

# Zileuton
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

## Zileuton: From Asthma to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Zileuton is a 5-lipoxygenase inhibitor originally used to treat intrinsic and allergic asthma.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it.
The strongest nearby signals are in other airway conditions, such as obstructive lung disease (7 trials, 20 publications) and asthma itself (6 trials, 16 publications).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intrinsic asthma, allergic asthma |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no active marketed product) |
| Number of NDAs | 3 (all cancelled; listed under ANDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, zileuton inhibits 5-lipoxygenase and thereby reduces the synthesis of leukotrienes. Leukotrienes drive bronchoconstriction, mucus secretion and airway inflammation.

Asthma and bronchitis are both inflammatory airway diseases, so dampening leukotriene production could in theory help bronchitis too. However, no clinical trials or publications for bronchitis were found. The very high TxGNN score reflects network proximity to the asthma and leukotriene pathway, not clinical proof.

**Other predictions worth noting** (ranked by evidence rather than score):

- **Obstructive lung disease (score 99.87%, L1 by the pack's scoring):** A Phase 3 trial in COPD exacerbations (NCT00493974) was terminated, so it gives no confirmed efficacy result. Most supporting trials are in asthma.
- **Bronchial neoplasm (score 99.48%, L2):** Two completed Phase 2 trials exist, one in bronchial dysplasia (chemoprevention) and one combining eicosanoid modulators with chemotherapy in advanced NSCLC. There is no Phase 3 support.
- **Atopic eczema (score 99.49%, L3):** A small pilot study and a related report exist, plus preclinical itch models.
- **Heart disease (score 99.07%, L4):** Evidence is animal-based only.
- **Asthma (score 99.72%):** This is the original indication, so it is not true repurposing.
- Several other high-scoring predictions (asthma-related traits, Laubry-Pezzi syndrome, interventricular septum aneurysm, Pierre Robin syndrome) have no trials, no literature and no plausible mechanism, and are likely network artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

For reference, the closest airway-related trials from the neighboring predictions (obstructive lung disease and asthma) are:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00493974](https://clinicaltrials.gov/study/NCT00493974) | Phase 3 | Terminated | 119 | Zileuton to shorten hospital stay in COPD exacerbations; no confirmed result |
| [NCT00486343](https://clinicaltrials.gov/study/NCT00486343) | Phase 4 | Terminated | 400 | Randomized, placebo-controlled zileuton CR in poorly controlled asthma on inhaled corticosteroids |
| [NCT00534625](https://clinicaltrials.gov/study/NCT00534625) | Phase 2 | Completed | 36 | IV zileuton: pulmonary function, safety and PK in chronic stable asthma |
| [NCT00299065](https://clinicaltrials.gov/study/NCT00299065) | Phase 1/2 | Completed | 60 | Safety, tolerability and PK of IV zileuton in asthma |
| [NCT01805687](https://clinicaltrials.gov/study/NCT01805687) | Phase 4 | Completed | 25 | Open-label single-dose bronchodilation with zileuton CR 1200 mg |
| [NCT00575861](https://clinicaltrials.gov/study/NCT00575861) | Phase 4 | Completed | 19 | Add-on to Advair; effect on exhaled nitric oxide |
| [NCT00723021](https://clinicaltrials.gov/study/NCT00723021) | Phase 2 | Completed | 15 | PF-04191834 compared with zileuton for bronchodilation in asthma |

## Literature Evidence

Currently no related literature available for bronchitis.

For reference, the main publications from the neighboring airway predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31841698](https://pubmed.ncbi.nlm.nih.gov/31841698/) | 2020 | Cohort | Pulm Pharmacol Ther | Zileuton use and phenotypic features in asthma; modest response rates |
| [10181070](https://pubmed.ncbi.nlm.nih.gov/10181070/) | 1998 | Open-label study | Am J Manag Care | 12-month safety and efficacy in 2,947 chronic asthma patients; about 2% had reversible liver enzyme elevations |
| [10421833](https://pubmed.ncbi.nlm.nih.gov/10421833/) | 1999 | Review | Clin Exp Allergy | Leukotriene pathway inhibitors in asthma and COPD |
| [17394438](https://pubmed.ncbi.nlm.nih.gov/17394438/) | 2007 | Review | Int J Clin Pract | Clinical implications of 5-LOX inhibition in severe airway disease |
| [39558440](https://pubmed.ncbi.nlm.nih.gov/39558440/) | 2024 | Review | Med Lett Drugs Ther | Drugs for asthma |
| [8757156](https://pubmed.ncbi.nlm.nih.gov/8757156/) | 1996 | Review | Lancet | Overview of zileuton |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA215742 | Zileuton (Camber Pharmaceuticals) | Tablet, film coated, extended release | Not specified; status cancelled |
| ANDA212670 | Zileuton (Strides Pharma Science) | Tablet, multilayer, extended release | Not specified; status cancelled |
| ANDA204929 | Zileuton (Rising Pharma Holdings) | Tablet, extended release | Not specified; status cancelled |

All three authorizations are cancelled, so no zileuton product is currently marketed in the US under these listings.

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, anxiety.
- **Hepatotoxicity:** About 2% of patients in controlled trials had reversible liver enzyme elevations, so liver function monitoring is advisable.
- **Drug Interactions:** 56 interactions are known. One is Major: terfenadine. The others shown are Moderate and include theophylline, aminophylline, oxtriphylline, warfarin, tacrolimus, roflumilast, pentoxifylline, cisapride, astemizole, naltrexone, deferasirox, alosetron, eliglustat, obeticholic acid, troglitazone, fostamatinib, ivacaftor, osilodrostat and somatrem.

Please refer to the package insert for formal warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a very high model score alone, with no clinical trials and no literature. In addition, all US authorizations are cancelled, and there is a liver safety concern.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence specific to bronchitis
- Mechanism-of-action data and package insert warnings and contraindications
- A review of whether the better-supported neighboring indications (obstructive lung disease, bronchial dysplasia) are more promising research questions
- A plan for liver function monitoring and drug-interaction management (especially CYP1A2 substrates such as theophylline and warfarin)
- Clarification of the regulatory and supply path, given that the US products are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

