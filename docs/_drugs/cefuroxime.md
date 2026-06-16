---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

The skill confirms this is a US TxGNN report. Now generating the report — using the UTI prediction (rank 6) as the featured indication, as it is the highest-quality actionable finding (L2, S3, Proceed with Guardrails); ranks 1–3 and 5, 7, 10 are topology-driven false signals (L5/Hold) and rank 4 is an outdated in-vitro study.

---

# Cefuroxime: From Bacterial Infection Treatment to Urinary Tract Infection

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic whose original indications are not captured in the current dataset, though it is clinically established for a range of bacterial infections.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (UTI)**, supported by **17 clinical trials** and **20 publications** — and this prediction is better understood as a **confirmation of established clinical use** rather than a novel repurposing, as cefuroxime axetil (the oral prodrug) is already a standard outpatient UTI agent in multiple countries.
The evidence qualifies as **Level L2**, and the overall recommendation is **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset (data gap) |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L2 |
| US Market Status | Not marketed (per current dataset — likely a data capture gap; manual FDA Orange Book verification recommended) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction ranking:** The TxGNN top-ranked predictions (ranks 1–3, 5, 7, 10) are assessed as topological false signals driven by dense hematological disease clustering in the knowledge graph, with no credible mechanistic link and no supporting evidence. Urinary tract infection (rank 6) is selected as the primary subject of this report as it represents the highest-evidence, clinically actionable finding.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, Cefuroxime is a β-lactam antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and causing bacterial cell lysis. Its second-generation cephalosporin profile provides broader gram-negative coverage than first-generation agents while retaining gram-positive activity — making it well-suited for mixed-flora infections and outpatient-manageable pathogens.

The most prevalent uropathogens — *Escherichia coli*, *Klebsiella pneumoniae*, *Proteus mirabilis*, and *Staphylococcus saprophyticus* — fall within Cefuroxime's antimicrobial spectrum. The oral prodrug cefuroxime axetil achieves urinary drug concentrations sufficient for treating uncomplicated lower UTI in ambulatory patients, while intravenous cefuroxime sodium is used for more severe presentations such as complicated UTI and pyelonephritis. This mechanistic fit explains both the high TxGNN score and the substantial real-world evidence base.

One critical guardrail: regional ESBL prevalence among *E. coli* and *Klebsiella* isolates should be monitored continuously. Where community ESBL rates exceed 10%, empiric Cefuroxime may be inadequate and carbapenem reassessment is warranted. Multiple included studies (PMIDs 39005695, 29373965, 35096675) directly address this surveillance need across different geographies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07236944](https://clinicaltrials.gov/study/NCT07236944) | Phase 4 | Recruiting | 560 | Phase 4 non-inferiority RCT of oral pivmecillinam vs standard of care (Cefuroxime as active comparator) for step-down therapy in febrile *E. coli* UTI after 2–4 days of IV antibiotics |
| [NCT03020940](https://clinicaltrials.gov/study/NCT03020940) | N/A | Unknown | 100,000 | National, multi-centre, prospective real-world registration study of cefuroxime axetil dispersible tablets; safety and efficacy revaluation across 100,000 cases |
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Completed study examining the effect of inappropriate empirical Cefuroxime therapy on mortality and morbidity in hospitalized patients with pyelonephritis — directly evaluates Cefuroxime resistance implications in UTI |
| [NCT05609240](https://clinicaltrials.gov/study/NCT05609240) | Phase 2 | Recruiting | 180 | Feasibility RCT comparing standard bolus Cefuroxime prophylaxis vs bolus-continuous infusion Cefuroxime to maintain drug levels throughout colorectal surgery (framework applicable to UTI PK/PD optimization) |
| [NCT02072798](https://clinicaltrials.gov/study/NCT02072798) | Phase 4 | Completed | 42 | Phase 4 completed trial of antibiotic prophylaxis for postpartum infections (endometritis, UTI, wound infection) after Caesarean section; single-dose pre-surgical Cefuroxime arm included |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Completed study of preventive antibiotic treatment during the puerperium for pregnant women with recurrent UTI; addresses prophylactic role of antibiotics in a high-risk population |
| [NCT03221504](https://clinicaltrials.gov/study/NCT03221504) | N/A | Unknown | 221 | RCT comparing 7-day vs 10-day antibiotic treatment for febrile UTI in children; assesses treatment duration optimization with cephalosporin-class agents |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1,000 | Study of whether antibiotic prophylaxis at urinary catheter removal reduces post-catheterization UTI; large sample, high ecological relevance |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | Preventive role of antimicrobial solutions before minimally invasive upper tract lithotomy; addresses UTI/urosepsis prevention in urological procedures |
| [NCT04146142](https://clinicaltrials.gov/study/NCT04146142) | N/A | Completed | 550 | Completed RCT of antibiotic prophylaxis vs no prophylaxis before transperineal MRI-TRUS fusion guided prostate biopsy; assesses post-procedure UTI and infection risk |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7037184](https://pubmed.ncbi.nlm.nih.gov/7037184/) | 1981 | RCT | Clinical Therapeutics | Prospective randomized trial of IM cefuroxime vs cefazolin in 58 men with complicated UTI; both drugs showed comparable bacteriological cure with organisms sensitive to both |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | The Lancet Infectious Diseases | Multicentre RCT showing de-escalation from antipseudomonal β-lactams to narrow-spectrum agents (including Cefuroxime) was non-inferior in Enterobacterales bacteraemia, supporting step-down use |
| [30234077](https://pubmed.ncbi.nlm.nih.gov/30234077/) | 2018 | Prospective Cohort | Frontiers in Pediatrics | Two-year prospective cohort of oral cefuroxime-axetil in 82 children with first febrile UTI; found high fever resolution rate, acceptable tolerance, and low bacterial resistance at follow-up |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Drug Review | International Journal of Antimicrobial Agents | Landmark review of cefuroxime axetil covering spectrum, PK/PD, and clinical use in UTI and respiratory infections; foundational reference for oral cefuroxime dosing |
| [35069075](https://pubmed.ncbi.nlm.nih.gov/35069075/) | 2021 | Review | Menopause Review | Review of antibiotic resistance in UTI; discusses Cefuroxime's role in recurrent UTI management, resistance prevention strategies, and appropriate agent selection by pathogen |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Observational | Infectious Diseases & Clinical Microbiology | Community-acquired UTI causative organisms and antibiotic susceptibility; identifies ESBL risk factors and Cefuroxime susceptibility patterns relevant to empiric prescribing |
| [35096675](https://pubmed.ncbi.nlm.nih.gov/35096675/) | 2021 | Retrospective Cohort | Germs | Pediatric UTI clinical and antimicrobial resistance data from Bucharest; cephalosporin susceptibility (including Cefuroxime) profiled across common uropathogens |
| [26607682](https://pubmed.ncbi.nlm.nih.gov/26607682/) | 2016 | Cohort | Brazilian Journal of Infectious Diseases | Follow-up of UTI recurrence in infants under 2 months; describes microbiological patterns and treatment, including cephalosporin-class use in neonatal UTI |
| [29373965](https://pubmed.ncbi.nlm.nih.gov/29373965/) | 2018 | Observational | BMC Infectious Diseases | Clinical risk factors for antimicrobial resistance and multi-drug resistance in UTI in a German emergency department; Cefuroxime resistance profiled for risk-stratified prescribing |
| [30197697](https://pubmed.ncbi.nlm.nih.gov/30197697/) | 2018 | Case Report | The Open Microbiology Journal | UTI and septicaemia due to non-typable *Haemophilus influenzae* associated with renal stone disease; Cefuroxime identified as a susceptible treatment option for this unusual uropathogen |

---

## US Market Information

The current dataset records **0 US FDA licenses** for Cefuroxime, with market status listed as "not marketed." This is assessed to be a **data capture gap** rather than an accurate regulatory status, as cefuroxime axetil (Ceftin®) and cefuroxime sodium for injection (Zinacef®) are known to have FDA approval history in the United States.

**Recommended action:** Cross-reference the [FDA Orange Book](https://www.accessdata.fda.gov/scripts/cder/ob/) for NDA records under the active ingredient "cefuroxime" before proceeding with any regulatory strategy.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields in the current dataset (key warnings, contraindications, drug interactions) are listed as data gaps. The DDI query returned no results. These must be populated from the Cefuroxime prescribing information (available from the FDA label database) before any clinical assessment proceeds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cefuroxime has a strong mechanistic fit with UTI treatment through β-lactam activity against the major uropathogens, and the evidence base — anchored by a 100,000-patient real-world study, a completed pyelonephritis outcome study, and an active Phase 4 RCT using Cefuroxime as an active comparator — confirms well-established clinical efficacy. This prediction is a validation of known use, not a speculative repurposing, making the evidence threshold effectively already met.

**To proceed, the following is needed:**
- **Verify US FDA market status** from the FDA Orange Book (current 0-license record is likely a data capture gap)
- **Obtain the full prescribing information** to populate MOA, key warnings, and contraindications — all currently missing
- **Establish DDI profile** — no drug interaction data was retrieved in the current dataset
- **Monitor local ESBL prevalence** among uropathogens: if community ESBL rates for *E. coli* exceed 10%, empiric Cefuroxime use should be reassessed
- **Clarify route and population scope**: oral cefuroxime axetil (uncomplicated/outpatient UTI) vs IV cefuroxime sodium (complicated UTI, pyelonephritis) have distinct clinical contexts and should be assessed separately
- **Resolve the higher-ranked false-positive predictions** (ranks 1–3, 5, 7, 10): these are likely knowledge graph topology artifacts and do not represent actionable repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

