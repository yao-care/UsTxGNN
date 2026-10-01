---
layout: default
title: Canakinumab
parent: Model Prediction Only (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Cryopyrin-Associated Periodic Syndromes to Familial Mediterranean Fever

> **Note on indication choice:** The top TxGNN hit (rank 1, hepatic infarction) has no supporting evidence. This report therefore leads with the best-supported prediction, familial Mediterranean fever (rank 6). The other candidates are summarized in the conclusion.

## One-Sentence Summary

Canakinumab is an IL-1β-neutralizing antibody, originally approved for cryopyrin-associated periodic syndromes (CAPS).
The TxGNN model predicts it may be effective for **familial Mediterranean fever (FMF)**, with **7 registered canakinumab trials** and **more than 20 publications** currently pointing in this direction.
The trials are mostly in CAPS and related periodic fevers, so the FMF-specific evidence rests mainly on the literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CAPS (familial cold autoinflammatory syndrome and Muckle-Wells syndrome, per the literature; the US license records contain no indication text) |
| Predicted New Indication | Familial Mediterranean fever, autosomal dominant |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 as assigned in the Evidence Pack, but provisional (see the caveat below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 3 listed licenses (1 BLA, 2 entries without a license number) |
| Recommended Decision | Proceed with Guardrails |

**Caveat on L1:** The Phase 3 trials listed below appear to be CAPS studies, not FMF studies. Their link to FMF is unverified. The FMF-specific support comes from a systematic review and meta-analysis, cohort studies and reviews. A strict reading would put the FMF evidence closer to L3 until an FMF-specific RCT is confirmed.

## Why is This Prediction Reasonable?

Canakinumab is a fully human monoclonal antibody that neutralizes IL-1β signaling and suppresses inflammation. Detailed mechanism-of-action data are not available in DrugBank for this pack, but the literature describes this mechanism consistently. CAPS is driven by NLRP3 mutations that cause IL-1β overproduction, and canakinumab treats it by blocking that cytokine.

FMF is also an IL-1β-driven autoinflammatory disease. It is caused by gain-of-function MEFV mutations affecting pyrin, a regulator of IL-1β activation. Colchicine is first-line therapy. Roughly 40% of patients respond only partially and 5–10% do not respond, so IL-1 blockade is a logical option for colchicine-resistant or colchicine-intolerant patients. Published reports cover canakinumab in this setting, including pediatric cohorts, withdrawal strategies, and use with or without colchicine.

## Clinical Trial Evidence

None of the trial records below is confirmed as an FMF trial. They support the class effect and long-term safety of canakinumab in autoinflammatory disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Completed | 166 | Long-term safety and efficacy of canakinumab in CAPS (FCAS, MWS, NOMID) |
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | Completed | 35 | Three-part study with a randomized, double-blind, placebo-controlled withdrawal phase in Muckle-Wells syndrome |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Completed | 19 | Open-label 24-week efficacy and safety study in Japanese CAPS patients, with an extension phase |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | Completed | 17 | One-year open-label study in CAPS patients aged 4 years or younger, including childhood vaccination response |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Completed | 17 | Open-label extension for long-term safety and efficacy in young CAPS patients |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | Completed | 20 | Four-month open-label canakinumab treatment in TRAPS, with 6-month follow-up |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | Recruiting | 25 | Real-world observational study (REASSURE) of Ilaris in hereditary periodic fevers (including colchicine-resistant FMF) and sJIA; no results yet |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Systematic review and meta-analysis | Rheumatology (Oxford) | Qualitative and quantitative evidence on anti-IL-1 treatment in colchicine-unresponsive or colchicine-intolerant FMF |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic review | Front Immunol | Safety and efficacy of IL-1 blockers (anakinra, canakinumab, rilonacept) across immune-mediated disorders |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Classified as Review in the pack | N Engl J Med | Canakinumab in FMF, mevalonate kinase deficiency and TRAPS; it may be the pivotal trial report, so verify before citing |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Review / trial report | Expert Rev Clin Immunol | Canakinumab for FMF patients with inadequate response to, or intolerance of, colchicine |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohort | Int J Rheum Dis | Compares attack features, acute-phase reactants and renal outcomes with canakinumab with or without colchicine |
| [34568239](https://pubmed.ncbi.nlm.nih.gov/34568239/) | 2021 | Retrospective study | Front Pediatr | 65 colchicine-resistant or colchicine-intolerant FMF patients on canakinumab for at least 6 months; dosing every 4 weeks |
| [31463794](https://pubmed.ncbi.nlm.nih.gov/31463794/) | 2019 | Retrospective, single center | Paediatr Drugs | Experience with canakinumab in pediatric FMF unresponsive to colchicine |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Retrospective study | Rheumatology (Oxford) | Feasibility of canakinumab tapering and withdrawal in pediatric colchicine-resistant FMF |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Review | Clin Exp Rheumatol | Clinical outcomes and expectations of IL-1 inhibition in FMF |
| [27603969](https://pubmed.ncbi.nlm.nih.gov/27603969/) | 2016 | Review | Expert Opin Biol Ther | Rationale for anti-IL-1 agents in colchicine-resistant FMF, based on pyrin regulation of IL-1β activation |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA 125319 | Ilaris | Injection, solution | Novartis Pharmaceuticals Corporation |
| No number listed | GUNA-ANTI IL 1 | Solution / drops | Guna spa |
| No number listed | GUNA-HEMORRHOIDS | Solution / drops | Guna spa |

Ilaris is the only entry with a real license number, and it is a BLA, not an NDA. The two Guna drop products have no license number and appear to be a different product category from the injectable antibody. None of the entries includes approved indication text.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the database query.

Please refer to the package insert for warnings and contraindications. That information is missing from this Evidence Pack and blocks a formal safety screen.

Guardrail from the pack's assessment: monitor for infection risk during IL-1 blockade.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
FMF is a plausible IL-1-driven target for a marketed IL-1β blocker. The supporting literature includes a meta-analysis of anti-IL-1 therapy in FMF and several canakinumab cohorts in colchicine-resistant patients. However, the listed Phase 3 trials are CAPS studies, and the L1 grade is provisional.

**Guardrails:**
- Colchicine stays first-line, and IL-1 blockade is considered only for colchicine-resistant or colchicine-intolerant patients.
- Monitor for infections.

**To proceed, the following is needed:**
- Confirmation of whether PMID 29768139 is the FMF-relevant pivotal RCT, and of any FMF-specific NCT records.
- The package insert (warnings, contraindications, interactions) to complete the safety screen.
- Approved indication text for the US licenses.
- Route compatibility assessment, which is still pending.

**Other candidates:**
- Blau syndrome (rank 8, L3): only case-level and pooled retrospective evidence, so it stays a research question.
- Periodic fever-infantile enterocolitis-autoinflammatory syndrome (rank 5, L4): only indirect class-level evidence, so it stays a research question.
- Hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis, syndrome with combined immunodeficiency, extracutaneous mastocytoma, monosomy X and liver angiosarcoma: no supporting evidence, so each stays on Hold. Hepatic infarction, monosomy X and liver angiosarcoma have no plausible mechanistic link.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

