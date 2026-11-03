---
layout: default
title: Omalizumab
parent: Model Prediction Only (L5)
nav_order: 992
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
description: "Omalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Omalizumab: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Omalizumab is an anti-IgE monoclonal antibody that is currently marketed in the United States.
The TxGNN model predicts it may be useful for **bronchitis**, but support is thin: **1 small clinical trial** in a related eosinophilic condition and **3 loosely related publications**, none of which tests bronchitis as the target indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of FDA Applications | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omalizumab binds free IgE and lowers its levels, which also reduces expression of the high-affinity IgE receptor (FcεRI) on mast cells, basophils and other cells. This dampens IgE-driven allergic inflammation in the airways. Detailed mechanism-of-action text was not available in the data compiled for this report, so this description rests on general pharmacology of the anti-IgE class.

Bronchitis is a broad condition, and most forms are not IgE-driven. Any benefit would probably be indirect. It could occur in patients whose chronic airway symptoms have an allergic or eosinophilic component. It could also occur in overlapping airway conditions with a chronic bronchitis phenotype. No trial in the data tests bronchitis as the indication, so the high model score is best treated as a hypothesis, not as confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Double-blind, placebo-controlled, 3-centre trial of whether omalizumab allows a lower prednisone dose in persistent eosinophilic bronchitis. It is very small, and no results are summarised in the data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses chronic bronchitis and other smoking-induced airway diseases in adults with chronic respiratory symptoms. Drug treatment is uncertain because these patients are excluded from most trials. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Preoperative management of patients with chronic airway disease, including chronic bronchitis. Mentions omalizumab as an available option for selected allergic patients. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Report of plastic bronchitis after bronchial thermoplasty. No abstract is available and no efficacy conclusion can be drawn. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103976 | Xolair PFS (Genentech, Inc.) | Injection, solution | Not listed; status valid |
| BLA761399 | Omalizumab-igec (CELLTRION, Inc.) | Injection | Not listed; status valid |

Both licences are single-ingredient products and both are currently valid.

## Safety Considerations

- **Drug Interactions**: 8 records were compiled. One is of Moderate severity: omacetaxine mepesuccinate. Five are Minor: zinc sulfate, zinc acetate, zinc gluconate, zinc chloride and Echinacea. A further Minor record covers vitamin E, and one pharmacology record identifies the target as immunoglobulin heavy constant epsilon (IgE).

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but no study in the data tests omalizumab in bronchitis. The only registered trial is a tiny steroid-sparing study in a related eosinophilic condition, and the publications are general reviews or a case report. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Define which bronchitis phenotype could be IgE- or eosinophil-driven, for example persistent eosinophilic bronchitis.
- Review the results of NCT02049294, or run an adequately powered, placebo-controlled trial in that phenotype.
- Obtain the current package insert warnings and contraindications.
- Obtain mechanism-of-action data to support the mechanistic link.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

