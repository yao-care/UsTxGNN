---
layout: default
title: Meropenem
parent: Moderate Evidence (L3-L4)
nav_order: 903
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Meropenem: predicted new indication Bacterial arthritis (evidence level L5). Approved use: Bacterial meningitis, peritonitis…"
monitor_inn: "MEROPENEM"
predicted_indications: ["bacterial arthritis", "epiglottitis", "staphylococcus aureus infection", "laryngitis", "paratyphoid fever", "Lyme disease", "Peptostreptococcus infectious disease", "Ureaplasma urethritis", "gonococcal urethritis"]
---

# Meropenem
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Meropenem: From Bacterial Infections (Meningitis, Peritonitis, Pseudomonas) to Bacterial Arthritis
{: .text-alpha }

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic, originally used for serious bacterial infections such as bacterial meningitis, peritonitis, and Pseudomonas aeruginosa infection.
The TxGNN model's top-ranked prediction is **bacterial arthritis**, but there are **no registered clinical trials** and only **20 publications** (mostly case reports, surveys, and pharmacokinetic studies) for this indication.
The best-supported candidate among the ten predictions is **urinary tract infection**, with **9 clinical trials** and **20 publications**, including Phase 3 RCTs.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial meningitis, peritonitis, Pseudomonas aeruginosa infection and other serious bacterial infections (the US license records contain no indication text) |
| Predicted New Indication | Bacterial arthritis (rank 1); urinary tract infection (rank 6) has the strongest evidence |
| TxGNN Prediction Score | 0.9992 (bacterial arthritis) |
| Evidence Level | L4 (bacterial arthritis); L1 (urinary tract infection) |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | 9 (1 NDA and 8 ANDAs, all cancelled) |
| Recommended Decision | Hold (bacterial arthritis); Proceed with Guardrails (urinary tract infection) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, meropenem is a carbapenem that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It covers many Gram-negative and Gram-positive organisms, including ESBL-producing Enterobacterales, and many anaerobes.

Bone and joint infections are caused by susceptible Gram-negative and Gram-positive bacteria, so the mechanism is plausible for bacterial arthritis. The literature, however, is limited to case reports (for example, ESBL-producing *Klebsiella* septic arthritis treated with meropenem plus amikacin), a retrospective melioidosis cohort, pharmacokinetic work, and pathogen and resistance surveys. No study tests meropenem directly in bacterial arthritis.

For urinary tract infection, the rationale is stronger. Meropenem is active against the Enterobacterales that cause complicated UTI, including ESBL producers. This is largely an extension of established antibacterial use, so the repurposing novelty is low.

Other predictions are weaker. Ureaplasma has no cell wall, so beta-lactams are expected to be ineffective, and this prediction is likely a false positive. Laryngitis is mostly viral. Lyme disease and gonococcal urethritis have well-established standard treatments. Peptostreptococcus is plausible given meropenem's anaerobic coverage, but no data support it.

## Clinical Trial Evidence

There are no registered clinical trials for bacterial arthritis, the top-ranked prediction. The table below shows trials for **urinary tract infection** (rank 6), the best-supported prediction. In several of them meropenem is the comparator rather than the tested drug.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840148](https://clinicaltrials.gov/study/NCT03840148) | Phase 3 | Completed | 661 | Cefepime/VNRX-5133 vs meropenem in complicated UTI (meropenem is the comparator) |
| [NCT03477422](https://clinicaltrials.gov/study/NCT03477422) | Phase 3 | Completed | 230 | CSE-1034 vs meropenem in complicated UTI caused by β-lactamase-producing bacteria |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Phase 4 | Suspended | 198 | Piperacillin/tazobactam vs carbapenems in ESBL UTI |
| [NCT02142751](https://clinicaltrials.gov/study/NCT02142751) | Phase 3 | Completed | 161 | Fosfomycin vs meropenem or ceftriaxone in bacteraemic UTI due to multidrug-resistant *E. coli* |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Phase 2 | Completed | 134 | Ceftolozane/tazobactam vs meropenem in paediatric complicated UTI |
| [NCT01970371](https://clinicaltrials.gov/study/NCT01970371) | Phase 3 | Completed | 69 | Plazomicin vs colistin, each combined with meropenem or tigecycline, in carbapenem-resistant Enterobacteriaceae infection |
| [NCT03543436](https://clinicaltrials.gov/study/NCT03543436) | Phase 3 | Completed | 29 | Temocillin vs a carbapenem in ESBL-related UTI |
| [NCT03174795](https://clinicaltrials.gov/study/NCT03174795) | Phase 1 | Completed | 20 | Pharmacokinetics of RO7079901 co-administered with meropenem in complicated UTI |
| [NCT00771316](https://clinicaltrials.gov/study/NCT00771316) | Phase 3 | Terminated | 6 | MK0826 vs meropenem in complicated UTI; terminated with too few participants for usable efficacy data |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Pharmacokinetics and safety of understudied drugs in children; not a UTI efficacy study |

## Literature Evidence

Publications for **urinary tract infection** (rank 6), prioritising RCTs and reviews:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | RCT | JAMA | TANGO I: meropenem-vaborbactam vs piperacillin-tazobactam in complicated UTI |
| [30270406](https://pubmed.ncbi.nlm.nih.gov/30270406/) | 2018 | RCT | Infect Dis Ther | TANGO II: meropenem-vaborbactam vs best available therapy in carbapenem-resistant Enterobacteriaceae infections |
| [33058798](https://pubmed.ncbi.nlm.nih.gov/33058798/) | 2021 | RCT | Lancet Infect Dis | APEKS-NP: cefiderocol vs high-dose extended-infusion meropenem in Gram-negative nosocomial pneumonia (not UTI) |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Meta-analysis | J Comp Eff Res | Systematic review and network meta-analysis of treatments for complicated UTI, including acute pyelonephritis |
| [18416587](https://pubmed.ncbi.nlm.nih.gov/18416587/) | 2008 | Review | Drugs | Review of meropenem in serious bacterial infections |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | Clinical data from novel antibiotics for multidrug-resistant Gram-negative infections |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review | Int J Antimicrob Agents | Italian and French practical approach to multidrug-resistant Gram-negative infections |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Cohort | Antimicrob Agents Chemother | Meropenem-vaborbactam vs ceftazidime-avibactam in carbapenem-resistant Enterobacteriaceae infections |

For **bacterial arthritis** (rank 1), the strongest items are weaker in design: a retrospective osteoarticular melioidosis cohort ([35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/), 2021), and a case report of ESBL *Klebsiella* septic arthritis treated with meropenem and amikacin ([17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/), 2007).

## US Market Information

Nine US authorizations are valid. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA091404 | Meropenem (Fresenius Kabi USA) | Injection, powder, for solution | Not recorded |
| ANDA216424 | Meropenem (Sagent Pharmaceuticals) | Injection, powder, for solution | Not recorded |
| ANDA206086 | Meropenem (Civica) | Injection | Not recorded |
| ANDA219084 | Meropenem (Brooks Steriscience) | Injection | Not recorded |
| ANDA206141 | Meropenem (Gland Pharma) | Injection | Not recorded |

Also cancelled: NDA202106 (Meropenem and Sodium Chloride, B. Braun, injection solution), ANDA216154, ANDA205883 and ANDA210773.

## Safety Considerations

- **Contraindication-related disease associations** (from the knowledge graph, not package insert text): epilepsy, kidney disease, pyoureter, thrombocytopenia, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis.
- **Drug Interactions** (14 recorded): the **Major** interactions are with bupropion, iohexol, and iopamidol. Moderate interactions include picosulfuric acid, polyethylene glycol (3350 with electrolytes), nitisinone, sodium sulfate, lindane, ethinylestradiol, alpelisib, encorafenib, mycophenolic acid, pemetrexed, and teriflunomide.

Please refer to the package insert for key warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold (bacterial arthritis, the top-ranked prediction); Proceed with Guardrails (urinary tract infection)**

**Rationale:**
- For bacterial arthritis, the model score is very high (0.9992), but evidence is limited to case reports, surveys, and pharmacokinetic work (L4), with no trials. Use today rests on susceptibility-guided clinical judgement rather than efficacy data.
- Complicated urinary tract infection has Phase 3 RCT support (L1), but the trials largely use meropenem as a comparator or combination partner, and the novelty is low because it is an established class use. Reserve it for ESBL or multidrug-resistant pathogens, with stewardship, susceptibility testing, and renal dose adjustment.
- Other predictions (epiglottitis, laryngitis, paratyphoid fever, Lyme disease, Peptostreptococcus, gonococcal urethritis) should stay on Hold. Ureaplasma urethritis is likely a false positive because the organism has no cell wall. Staphylococcus aureus infection is a research question limited to combination therapy for persistent MSSA bacteraemia, since meropenem is not active against MRSA.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block formal safety screening.
- Detailed mechanism of action data from DrugBank.
- Clarification of US regulatory status, since the drug is marketed with nine valid licenses.
- For bacterial arthritis, prospective or comparative data on meropenem in bone and joint infection.
- For urinary tract infection, review of the trials where meropenem is the tested agent rather than the comparator.
- Dosing guidance for renal impairment, and a seizure-risk review given the epilepsy association.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

