---
layout: default
title: Olodaterol
parent: Model Prediction Only (L5)
nav_order: 988
evidence_level: L5
indication_count: 2
---

# Olodaterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Olodaterol: From COPD to Bronchitis

## One-Sentence Summary

Olodaterol is an inhaled long-acting beta2-agonist (LABA) marketed in the US as Striverdi Respimat, and the trial and literature record shows it is used for COPD maintenance treatment.
The TxGNN model predicts it may be effective for **bronchitis**, but the **3 registered trials** and **2 publications** linked to this prediction are all COPD-level, so none tests bronchitis as a separate endpoint.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (license text is empty); COPD maintenance bronchodilator per the trial and literature record |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (indirect, COPD-level evidence only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Olodaterol is a long-acting beta2-adrenergic agonist. It relaxes airway smooth muscle through the beta2 receptor and cAMP pathway. This is the standard rationale for maintenance bronchodilation in COPD.

Chronic bronchitis is one COPD phenotype, so airflow limitation is plausibly relevant to it. The link is indirect, however. None of the listed trials or papers evaluates bronchitis as a distinct endpoint. The very high TxGNN score probably reflects the drug's established COPD use rather than a new bronchitis-specific signal.

The second-ranked prediction, **obstructive lung disease**, has much stronger support: several completed Phase 3 RCTs and systematic reviews (evidence level L1). It is effectively on-label COPD use rather than true repurposing, so it is not a real repurposing candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completed | 11,316 | Observational study of healthcare resource use, cost and outcomes in COPD patients starting tiotropium/olodaterol vs. fluticasone furoate/umeclidinium/vilanterol. No efficacy evidence for bronchitis. |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completed | 1,335 | Japanese post-marketing surveillance of long-term tiotropium+olodaterol use in COPD (chronic bronchitis, emphysema). Real-world safety and effectiveness data, not bronchitis-specific. |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22,155 | Drug utilisation and safety study of aclidinium bromide, a different drug. It does not evaluate olodaterol for bronchitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | Am J Health Syst Pharm | Reviews the pharmacology, pharmacokinetics, efficacy and safety of once-daily olodaterol in COPD. |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | Finnish national guideline on diagnosis and pharmacotherapy of stable COPD, intended mainly for primary care. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203108 | Striverdi Respimat (Boehringer Ingelheim Pharmaceuticals, Inc.) | Metered spray | Indication text not supplied |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests only on indirect COPD-level evidence, with no bronchitis-specific trial or publication, so it remains a research question. The evidence-rich signal in this pack is the on-label COPD use (obstructive lung disease), which is not a repurposing case.

**To proceed, the following is needed:**
- Bronchitis-specific evidence, for example a trial or subgroup analysis with a chronic bronchitis endpoint
- The FDA package insert, including warnings and contraindications
- Mechanism of action data from DrugBank
- A cardiovascular and pneumonia monitoring plan, if any COPD-based extension is pursued, since these signals appear in the cohort literature
- Confirmation that the truncated trial titles in the input match the olodaterol arms before citing them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

