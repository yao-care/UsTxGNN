---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

Now let me generate the evaluation report. I note several key issues with this evidence pack that require careful framing:

- **Rank 1 prediction** (polyclonal hyperviscosity syndrome) is mechanistically implausible — a β-lactam antibiotic has zero relevance to immunoglobulin-mediated conditions.
- **Rank 4 prediction** (UTI) carries the highest evidence (L2, 17 trials, 20 papers) and is actually Ceftazidime's **globally established** indication — the data gap is in the Taiwan registry, not in clinical evidence.
- All safety fields are [Data Gap].
- Ceftazidime is **not** antineoplastic — the Cytotoxicity section will be omitted.

---

# Ceftazidime: From Third-Generation Cephalosporin to Urinary Tract Infection

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin β-lactam antibiotic with strong bactericidal activity against Gram-negative pathogens — including *Pseudomonas aeruginosa* — that is globally established for serious bacterial infections but currently absent from the Taiwan regulatory database.
Although TxGNN's highest-ranked prediction is polyclonal hyperviscosity syndrome, this has been assessed as mechanistically implausible (Evidence Level L5, **Hold**); the most evidence-supported and actionable prediction is **Urinary Tract Infection**, backed by **17 clinical trials** and **20 publications** at Evidence Level **L2**.

> ⚠️ **Editorial Note**: Ceftazidime is FDA-approved and EMA-approved for UTI in most major jurisdictions. The Taiwan system's prediction of UTI as a "new" indication reflects a **regulatory data gap**, not a genuine repurposing scenario. This report is therefore better characterized as a **market introduction evaluation** rather than a classic drug repurposing case.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan regulatory records; globally established for serious bacterial infections (UTI, pneumonia, septicemia, meningitis, febrile neutropenia) |
| Predicted New Indication | Urinary Tract Infection *(rank 4; highest evidence — see note below)* |
| TxGNN Prediction Score | 99.41% (UTI, rank 4) |
| Evidence Level | L2 |
| US Market Status | Not marketed *(Taiwan database shows 未上市; Ceftazidime IS approved in the US as Fortaz®/Tazicef®)* |
| Number of NDAs | 0 *(Taiwan records only)* |
| Recommended Decision | Proceed with Guardrails |

> † TxGNN rank 1 (polyclonal hyperviscosity syndrome, 99.51%) and ranks 2–3 (hyperamylasemia, congenital analbuminemia) have been evaluated and rejected as model artifacts with no mechanistic basis. Rank 6 (Ureaplasma urethritis) is directly contraindicated — *Ureaplasma* lacks a cell wall and is inherently resistant to all β-lactams. UTI (rank 4) is the most clinically actionable prediction in this set.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from the queried data sources for this evidence pack. Based on established pharmacological knowledge, however, Ceftazidime is a β-lactam antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), ultimately causing bacteriolysis. Its antimicrobial spectrum is strongly oriented toward Gram-negative aerobic bacteria — *Escherichia coli*, *Klebsiella pneumoniae*, *Proteus* spp., *Enterobacter* spp., and critically *Pseudomonas aeruginosa* — which together account for the large majority of urinary tract infection (UTI) pathogens, particularly in complicated and healthcare-associated settings.

The pharmacokinetic profile of Ceftazidime is ideally suited for UTI: it is predominantly excreted unchanged by the kidneys, achieving urinary drug concentrations that are 10–100× higher than serum levels and far exceed the MIC of most susceptible uropathogens. This makes Ceftazidime especially valuable for complicated UTIs (cUTI), pyelonephritis, and catheter-associated UTIs driven by multidrug-resistant (MDR) Gram-negative organisms, for which first-line oral options are often unavailable. Its anti-*Pseudomonas* activity is a key differentiating feature compared to other cephalosporins.

It is important to flag an interpretive caveat: Ceftazidime's use in UTI is not a novel repurposing — it is an **established, FDA-approved indication** (cUTI is a listed indication for Fortaz®). The TxGNN model predicted it for UTI because the current evidence pack has no Taiwan regulatory records for this drug, causing the system to treat a licensed indication as a new prediction. Ranks 1–3 in this set (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia) represent spurious knowledge-graph connections with no biological plausibility and should be disregarded. The UTI evidence reviewed below therefore validates both the clinical evidence base and the drug's suitability, rather than discovering a genuinely new therapeutic use.

---

## Clinical Trial Evidence

*(Extracted from predicted_indications[3] — Urinary Tract Infection, rank 4; 17 trials retrieved, 10 most relevant listed below)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | Completed | 129 | Head-to-head double-blind RCT: IV CXA-101 vs **Ceftazidime** in complicated UTI including pyelonephritis — highest-relevance trial, directly evaluates Ceftazidime as active comparator in cUTI |
| [NCT00690378](https://clinicaltrials.gov/study/NCT00690378) | Phase 2 | Completed | 137 | Prospective multicenter RCT: NXL104 (Avibactam) + **Ceftazidime** vs comparator in hospitalized adults with complicated UTI; followed by appropriate oral therapy |
| [NCT02497781](https://clinicaltrials.gov/study/NCT02497781) | Phase 2 | Completed | 97 | Single-blind RCT: **Ceftazidime-Avibactam** vs Cefepime in children (3 months–18 years) with complicated UTI — safety, tolerability, PK, and efficacy in pediatric cUTI |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | Completed | 60 | Open-label RCT: CAZ-AVI vs best available therapy for carbapenem-resistant Gram-negative infections in Chinese adults — infection types include cUTI, HAP, cIAI, and BSI |
| [NCT05258851](https://clinicaltrials.gov/study/NCT05258851) | Phase 3 | Terminated | 29 | Non-inferiority RCT: CAZ-AVI vs Colistin for carbapenem-resistant Enterobacterales in critically ill patients; terminated early (29 of planned enrollment) — includes UTI as infection type |
| [NCT01601093](https://clinicaltrials.gov/study/NCT01601093) | Phase 2 | Suspended | 288 | **Ceftazidime-Sulbactam** (2:1) for respiratory and urinary tract acute bacterial infection — directly tests Ceftazidime combination for UTI; currently suspended (reason unconfirmed) |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | Completed | 43 | Two-part PK and drug-drug interaction study of **Ceftazidime-Avibactam** combination — provides PK basis for Ceftazidime dosing in serious infections |
| [NCT03147807](https://clinicaltrials.gov/study/NCT03147807) | N/A | Completed | 75 | BetaLACTA®-guided de-escalation from empirical carbapenems in ICU pulmonary, urinary, and bloodstream infections — Ceftazidime is a primary de-escalation target |
| [NCT04628572](https://clinicaltrials.gov/study/NCT04628572) | N/A | Completed | 189 | Retrospective real-world analysis: treatment patterns, effectiveness, and safety of CAZ-AVI in India — includes UTI among covered infection types |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Large PK/PD study for understudied drugs administered to pediatric patients per standard of care — may generate Ceftazidime-specific PK data in children with UTI |

---

## Literature Evidence

*(Extracted from predicted_indications[3] — Urinary Tract Infection, rank 4; 20 publications retrieved, 10 most relevant listed below)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic Review / Meta-analysis | J Comparative Effectiveness Res | Network meta-analysis of treatment options for complicated UTI and acute pyelonephritis; evaluates β-lactam/β-lactamase inhibitor combinations including Ceftazidime-based regimens against carbapenems as last line |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Expert Consensus Review | Int J Antimicrobial Agents | Italian-French infectious disease society joint guidance on treating MDR Gram-negative bacilli; positions Ceftazidime-Avibactam as a key agent for CRE and ESBL-producing uropathogens |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Retrospective Cohort | Clin Infect Dis | Multicenter observational study of CAZ-AVI for KPC-producing *Klebsiella pneumoniae* infections; establishes real-world clinical value of Ceftazidime combinations for resistant uropathogens |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Comparative Cohort | Antimicrob Agents Chemother | Multicenter retrospective comparison of CAZ-AVI vs meropenem-vaborbactam for CRE infections — UTI patients excluded from primary endpoint but provides comparative efficacy context |
| [40530972](https://pubmed.ncbi.nlm.nih.gov/40530972/) | 2025 | PK/PD Modeling | Antimicrob Agents Chemother | Population PK/PD modeling for aztreonam-avibactam (EU-approved for cUTI/cIAI/HAP caused by MDR Gram-negatives); methodology and dosing optimization directly applicable to Ceftazidime-based BLI combinations |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrobial Agents | Clinical evidence review for novel antibiotics against MDR Gram-negative bacteria; Ceftazidime-Avibactam featured prominently for UTI and intra-abdominal indications |
| [39934901](https://pubmed.ncbi.nlm.nih.gov/39934901/) | 2025 | Systematic Review / Meta-analysis | Antimicrob Resistance & Infection Control | Global trends of CAZ-AVI resistance in Gram-negative bacteria — critical for informing appropriate patient selection and monitoring requirements |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | Antibiotic renal dose adjustment review; discusses reduced clinical response warnings for Ceftazidime-Avibactam in patients with creatinine clearance 30–50 mL/min — directly relevant for UTI patients with concurrent renal impairment |
| [37873539](https://pubmed.ncbi.nlm.nih.gov/37873539/) | 2023 | Cross-sectional Observational | Open Medicine | Bacteriology and antibiogram of UTI in chronic kidney disease patients; confirms susceptibility profiles for Gram-negative uropathogens relevant to Ceftazidime selection |
| [30270406](https://pubmed.ncbi.nlm.nih.gov/30270406/) | 2018 | Phase 3 RCT | Infectious Dis & Therapy | TANGO II: meropenem-vaborbactam vs best available therapy (including CAZ-AVI) for CRE infections — provides Phase 3 comparative efficacy context for Ceftazidime-based regimens |

---

## US Market Information

No records were found in the current database for Ceftazidime. This reflects a **data gap in the Taiwan regulatory registry**, not an absence of global approvals.

For reference, Ceftazidime is approved in the US under:

| Brand Name | Dosage Form | Key Approved Indications (US FDA) |
|---------|------|-----------|
| Fortaz® | IV / IM Injection | Complicated and uncomplicated UTI, lower respiratory tract infections, skin/soft tissue infections, bacterial septicemia, bone/joint infections, CNS infections (meningitis), intra-abdominal infections |
| Tazicef® | IV / IM Injection | Same indications as Fortaz® (generic/alternative brand) |
| Avycaz® *(as CAZ-AVI)* | IV Infusion | Complicated intra-abdominal infections (with metronidazole), complicated UTI including pyelonephritis, hospital-acquired/ventilator-associated bacterial pneumonia — for MDR Gram-negative organisms |

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety data fields — key warnings, contraindications, and drug-drug interaction database — returned no retrievable data in this evidence pack. This is a **data gap** (flagged as DG001, severity: Blocking), not an absence of known safety concerns. Based on established pharmacological knowledge, clinicians should be aware that Ceftazidime carries well-characterized risks including: requirement for **renal dose adjustment** (creatinine clearance monitoring), risk of *Clostridioides difficile*-associated diarrhea, potential for seizures at supratherapeutic doses, and cross-reactivity considerations in patients with penicillin allergy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ceftazidime has a well-established pharmacological mechanism, strong renal pharmacokinetics, and multiple completed Phase 2 RCTs directly supporting efficacy in complicated UTI — including two trials where Ceftazidime served as the active comparator arm, reflecting its status as a clinical standard. The primary barrier is not clinical evidence but rather the **absence of Taiwan regulatory records and safety data in the current system**, both of which must be resolved before any formal indication review can proceed.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve TFDA package insert warnings and contraindications: download PDF from TFDA website and extract safety text before S1 safety screening can be completed
- **[DG002 — High]** Obtain Mechanism of Action data via DrugBank API (DB00438) to populate the mechanistic link analysis
- Clarify the **regulatory pathway**: this appears to be a market introduction case (Ceftazidime is already FDA/EMA approved for UTI), not a classic repurposing — confirm whether a Taiwan NDA, abbreviated NDA, or import approval is the appropriate route
- Obtain complete **drug-drug interaction profile** from DrugBank or clinical references (e.g., interactions with nephrotoxic agents, anticoagulants)
- Define a **patient selection strategy**: Ceftazidime's UTI value is primarily in complicated UTI / MDR uropathogens; clear criteria should distinguish from simpler UTIs where oral agents suffice
- Establish a **renal function monitoring protocol**: dose adjustment is mandatory for patients with CrCl < 50 mL/min, which is common in UTI populations with underlying comorbidities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

