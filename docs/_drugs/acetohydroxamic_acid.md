---
layout: default
title: Acetohydroxamic Acid
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 4
---

# Acetohydroxamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Acetohydroxamic Acid: From Chronic Urea-Splitting Urinary Infection (Adjunct Therapy) to Ureaplasma Urethritis

## One-Sentence Summary

Acetohydroxamic acid is an oral urease inhibitor marketed in the US as Lithostat tablets. The Evidence Pack describes its use as adjunct therapy in chronic urea-splitting urinary infections, although the FDA license record contains no indication text.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but **0 clinical trials** and **0 publications** are currently linked, so this is a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license record (the Evidence Pack's rationale describes adjunct use in chronic urea-splitting urinary infections) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record. Based on the mechanistic rationale in the Evidence Pack, acetohydroxamic acid is a urease inhibitor. Blocking urease reduces the breakdown of urea into ammonia, which in turn limits local alkalinization of the urinary tract.

*Ureaplasma urealyticum* expresses urease, so there is a plausible biological rationale: inhibiting the enzyme could reduce ammonia production and local alkalinization at the infection site. This is the same logic behind the drug's use in urea-splitting urinary infections.

The reasoning stops there. The 99.63% TxGNN score is a graph-based prediction only. No trial or publication shows that urease inhibition improves outcomes in Ureaplasma urethritis. Standard antibiotic therapy is not replaced by this mechanism. Systemic exposure also carries known safety concerns, including teratogenicity and hemolytic anemia.

For the other predictions, the Evidence Pack sees the following:

- **Gonococcal urethritis (99.63%):** No clear mechanistic link, because *Neisseria gonorrhoeae* is not a recognized urease-producing pathogen. Recommendation: Hold.
- **Uterine inflammatory disease (99.54%):** No established link, because the disease is polymicrobial. The drug's teratogenicity is also a problem for women of reproductive age. Recommendation: Hold.
- **Xanthogranulomatous pyelonephritis (99.46%):** A plausible indirect link through urease-producing organisms (e.g., Proteus) and struvite stones. The link is inferred from shared pathophysiology only. The disease is usually managed surgically and antimicrobially. Recommendation: Research Question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018749 | Lithostat (Mission Pharmacal Company) | Tablet (oral) | Not provided in the license record |

## Safety Considerations

Structured warning, contraindication and drug-interaction data are not available in the Evidence Pack. Please refer to the package insert for safety information.

The mechanistic rationale for this candidate flags these concerns for systemic exposure:

- **Teratogenicity:** This is a particular problem for uterine inflammatory disease, where the target population is women of reproductive age.
- **Hemolytic anemia**
- **Thromboembolic events**

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score and a plausible urease-based rationale alone. There are no linked trials or publications (Evidence Level L5, stage S0), and standard antibiotic therapy already exists. The drug's systemic toxicity profile adds further risk.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A literature review of urease inhibition in *Ureaplasma* infection, covering preclinical and case-based evidence
- Route compatibility and similarity-to-original assessments, currently pending
- For the xanthogranulomatous pyelonephritis hypothesis, a retrospective or case-based evidence review weighed against the drug's toxicity

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

