---
layout: default
title: Dupilumab
parent: Moderate Evidence (L3-L4)
nav_order: 634
evidence_level: L4
indication_count: 10
---

# Dupilumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Dupilumab: From an Unspecified Approved Indication to Bronchitis

## One-Sentence Summary

Dupilumab is an IL-4 receptor alpha blocker marketed in the US as Dupixent. The supplied record does not list its approved indications.
The TxGNN model predicts it may be effective for **bronchitis**, but the direct evidence is thin. There is **1 indirect clinical trial** (chronic rhinosinusitis, not bronchitis) and **6 publications** drawn mostly from asthma, COPD and a review of eosinophilic plastic bronchitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied record |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 license records (all under one BLA, BLA761055) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The DrugBank mechanism-of-action field is empty in the supplied data. From the prediction rationale, dupilumab blocks IL-4Rα, which shuts down both IL-4 and IL-13 signaling and dampens type 2 inflammation. Type 2 inflammation drives eosinophilic airway disease such as asthma.

Bronchitis is an airway inflammatory condition, so the link is plausible for **eosinophilic or type 2-driven bronchial disease**. Examples are asthma-overlap phenotypes and eosinophilic plastic bronchitis. The evidence comes from asthma and COPD data and a review of eosinophilic plastic bronchitis, so it is indirect. No study tests dupilumab in bronchitis itself.

The rationale does not hold for **acute or infectious bronchitis**, which has no clear type 2 mechanism. The prediction should therefore not be read as applying to bronchitis in general.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in chronic rhinosinusitis without nasal polyps. It is an upper-airway type 2 disease, not a bronchitis population, so it gives only indirect support. No results were included in the supplied data. |

No registered trial in the supplied data enrolls patients with bronchitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic review / meta-analysis of RCTs | J Asthma | Pooled efficacy and safety of dupilumab versus placebo in uncontrolled asthma. Asthma evidence, not bronchitis. |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Open-label extension (TRAVERSE) | Lancet Respir Med | Long-term safety and efficacy of dupilumab in moderate-to-severe asthma beyond 1 year. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Cohort / imaging study | Chest | Anti-T2 biologics, including dupilumab, and lung ventilation on MRI in prednisone-dependent asthma. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review | Tuberc Respir Dis | Pharmacologic options for preventing COPD exacerbations, including newer biologic agents. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Managing asthma with smoking-induced airway disease (chronic bronchitis, emphysema, asthma-COPD overlap). These patients are excluded from most trials. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review | Pediatr Pulmonol | Novel therapies for eosinophilic pediatric plastic bronchitis. No abstract was supplied, so the findings are unconfirmed. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761055 | Dupixent (sanofi-aventis U.S. LLC) | Injection, solution | Not specified in the supplied record |

The supplied record contains five identical license entries under BLA761055. They are shown here once.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication studies dupilumab in bronchitis. The support is indirect and comes from asthma, COPD and a review of eosinophilic plastic bronchitis. The model score is very high, but it is not backed by bronchitis-specific evidence.

**To proceed, the following is needed:**
- Define the target bronchitis subtype, such as an eosinophilic or type 2 phenotype, and exclude acute or infectious bronchitis
- Bronchitis-specific clinical data, or a trial in that phenotype
- The current US approved indications and the package insert warnings and contraindications
- Detailed mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

