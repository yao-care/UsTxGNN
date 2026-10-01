---
layout: default
title: Interferon Gamma-1B
parent: Model Prediction Only (L5)
nav_order: 803
evidence_level: L5
indication_count: 10
---

# Interferon Gamma-1B
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

# Interferon Gamma-1b: From Chronic Granulomatous Disease to Heart Disease

## One-Sentence Summary

Interferon gamma-1b (marketed in the US as Actimmune) is an immune-activating protein used mainly for chronic granulomatous disease (CGD) and refractory infections.
The TxGNN model predicts it may be effective for **heart disease**, with a very high model score (99.99%).
However, **no clinical trial has tested it in heart disease**, and the literature offers only **infection-related case reports**, so real-world support is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic granulomatous disease (from the drug's known use; the license records in the pack contain no indication text) |
| Predicted New Indication | Heart disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (case reports and mechanism only; no interventional study in heart disease) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records (only one, BLA103836, carries a license number) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known biology, IFN-gamma activates macrophages and strengthens phagocyte killing. This explains its use in CGD and in refractory mycobacterial or fungal infections.

The link to heart disease is weak. The only cardiac signals are case reports of infection-related cardiac disease in immunocompromised patients: *M. chimaera* prosthetic endocarditis and *Aspergillus* pericarditis in CGD. In these cases the drug treats the underlying infection or immune defect, not the heart itself.

IFN-gamma is also pro-inflammatory, which raises a plausible safety concern in non-infectious heart disease. The high TxGNN score is therefore not supported by clinical evidence.

## Clinical Trial Evidence

The search returned about 40 trials, but almost none involve IFN-gamma 1b, and **none test it in heart disease**. The most relevant entries are below. Most others are unrelated exercise, vaccine or other-drug studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021567](https://clinicaltrials.gov/study/NCT00021567) | Phase 2 | Completed | 20 | Inhaled IFN-gamma 1b plus antimycobacterial drugs in pulmonary MAC infection (infection, not cardiac) |
| [NCT03888664](https://clinicaltrials.gov/study/NCT03888664) | Phase 2 | Completed | 12 | Open-label safety and efficacy pilot of gamma interferon in Friedreich ataxia (neurological) |
| [NCT07538336](https://clinicaltrials.gov/study/NCT07538336) | Phase 2 | Not yet recruiting | 40 | Emapalumab (an anti-IFN-gamma antibody) in lung transplant recipients with acute allograft dysfunction; this blocks IFN-gamma rather than giving it |
| [NCT06996119](https://clinicaltrials.gov/study/NCT06996119) | Phase 1 | Not yet recruiting | 15 | Emapalumab plus post-transplant cyclophosphamide for GVHD prophylaxis |
| [NCT05837143](https://clinicaltrials.gov/study/NCT05837143) | Early Phase 1 | Active, not recruiting | 12 | Gene therapy (modified telomerase) in dilated cardiomyopathy heart failure; different drug |
| [NCT06634108](https://clinicaltrials.gov/study/NCT06634108) | Phase 1/2 | Recruiting | 20 | Genistein for inflammation in transthyretin amyloid heart failure; different drug |
| [NCT02475694](https://clinicaltrials.gov/study/NCT02475694) | N/A | Completed | 50 | Inflammatory response and lung injury after cardiac surgery; observational, no IFN-gamma intervention |
| [NCT03672812](https://clinicaltrials.gov/study/NCT03672812) | Phase 3 | Completed | 50 | Liraglutide in brain-dead organ donors; different drug and indication |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Systematic review | Ther Adv Rare Dis | Reviews interventions in Friedreich ataxia; not cardiac and not specific to IFN-gamma |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Case report | Eur Heart J Case Rep | Successful treatment of healthcare-associated *M. chimaera* prosthetic endocarditis after cardiac surgery |
| [29456196](https://pubmed.ncbi.nlm.nih.gov/29456196/) | 2018 | Case report | J Cyst Fibros | IFN-gamma therapy improved *Exophiala dermatitidis* airway persistence and respiratory decline in a cystic fibrosis patient |
| [28990950](https://pubmed.ncbi.nlm.nih.gov/28990950/) | 2017 | Case report | Turk Kardiyol Dern Ars | Constrictive *Aspergillus* pericarditis as a rare complication of CGD in a child |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Validation study | Am J Respir Crit Care Med | Six-minute-walk test validation in idiopathic pulmonary fibrosis (indirect; not about IFN-gamma in heart disease) |

None of these studies shows that IFN-gamma 1b treats heart disease itself.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA103836 | ACTIMMUNE (Horizon Therapeutics USA, Inc.) | Injection, solution | Not stated in the license record |
| No number on record | GUNA-INF GAMMA (Guna spa) | Solution/drops | Not stated in the license record |
| No number on record | GAMMA-12 (Guna spa) | Solution/drops | Not stated in the license record |
| No number on record | GUNA-REACT (Guna spa) | Pellet | Not stated in the license record |

## Safety Considerations

- **Mechanism-based concern**: IFN-gamma is pro-inflammatory, which may be a problem in non-infectious heart disease.

Please refer to the package insert for other safety information (warnings, contraindications and drug interactions were not available in the record).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.99% TxGNN score is not backed by any trial, and the literature reflects treatment of infections in patients who happen to have cardiac disease. The mechanism gives no reason to expect a benefit in heart disease and raises a possible safety concern. The other nine predicted indications (ranks 2–10, mostly congenital or chromosomal syndromes) have no clinical evidence either.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- A specific cardiac disease subtype and a testable mechanistic hypothesis, since "heart disease" is too broad
- Preclinical or observational evidence that IFN-gamma 1b benefits, or at least does not harm, non-infectious cardiac conditions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

