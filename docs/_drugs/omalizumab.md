---
layout: default
title: Omalizumab
parent: Model Prediction Only (L5)
nav_order: 992
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-06
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

Omalizumab is an anti-IgE monoclonal antibody used in allergic disease. The TxGNN model predicts it may be effective for **支氣管炎 (bronchitis)**, but the data compiled for this report contain **2 registered clinical trials** and **7 publications** and none of them shows a benefit of omalizumab in bronchitis itself, so the evidence level is L5.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. From the drug's known pharmacology, omalizumab binds free IgE (target: immunoglobulin heavy constant epsilon, IGHE), lowering free IgE and the activation of mast cells and basophils, and so dampening allergic airway inflammation.

Any benefit in bronchitis would most likely be indirect, for example in people with allergic asthma or asthma-COPD overlap who also have a chronic bronchitis phenotype. No study directly tests bronchitis as the indication, so the mechanistic link is a hypothesis rather than a demonstrated effect. The high model score should be read as a computational signal only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Placebo-controlled test of whether omalizumab lets prednisone doses be reduced in patients with asthma and persistent eosinophilic bronchitis. Very small and conducted in an asthma population; it does not show benefit in bronchitis. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of QGE031 (an anti-IgE agent) in chronic spontaneous urticaria. Not a bronchitis study. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | Omalizumab in middle-aged or older patients with severe allergic asthma-COPD overlap; an asthma-related population, not bronchitis alone. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Safety study | Curr Med Res Opin | Pooled safety analysis of omalizumab in children with allergic asthma. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Approval and post-approval experience of omalizumab in moderate-to-severe persistent asthma. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Management challenges in asthma with smoking-induced airway disease, including chronic bronchitis. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Preoperative management of patients with bronchial asthma or chronic bronchitis; mentions omalizumab for severe allergic asthma. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | Overview of monoclonal antibodies in paediatrics. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Plastic bronchitis following bronchial thermoplasty. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103976 | Xolair PFS (Genentech, Inc.) | Injection, solution | Not listed; status valid |
| BLA761399 | Omalizumab-igec (CELLTRION, Inc.) | Injection | Not listed; status valid |

## Safety Considerations

- **Drug Interactions**: Eight interaction records were found. One is rated Moderate (omacetaxine mepesuccinate). Six are rated Minor (zinc sulfate, zinc acetate, zinc gluconate, zinc chloride, echinacea, vitamin E). One further record is a pharmacology target entry (IgE heavy chain) and carries no severity rating.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No published study supports omalizumab in bronchitis. The one related trial (NCT02049294) was a very small study in asthma patients with eosinophilic bronchitis, and the remaining papers concern asthma, asthma-COPD overlap, or are general reviews. The high TxGNN score is therefore not backed by direct evidence (L5).

**To proceed, the following is needed:**
- A clear definition of the target bronchitis population (for example eosinophilic bronchitis or a type 2-high chronic bronchitis phenotype)
- A properly powered, controlled trial with bronchitis-specific outcomes
- Mechanism-of-action data and the full package insert warnings and contraindications

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

