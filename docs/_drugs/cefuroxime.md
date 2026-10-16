---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 509
evidence_level: L5
indication_count: 10
monitor_inn: "CEFUROXIME"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "urinary tract infection (disease)", "premalignant hematological system disease", "monoclonal gammopathy", "suppurative otitis media", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic, originally used for bacterial infections such as otitis media, pneumonia, meningitis, gonorrhea and Lyme disease.
The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but it has **no supporting trials or literature**. The best-supported candidate in the list is **urinary tract infection (UTI)**, with **5 clinical trials** and **20 publications**, although this is largely an extension of existing antibacterial use rather than true repurposing.

> Note: The rank-1 prediction (polyclonal hyperviscosity syndrome) has no evidence and no plausible mechanism. This report therefore presents it in the overview and focuses the evidence sections on the best-supported candidate, UTI (rank 6).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (otitis media, pneumonia, meningitis, gonorrhea, Lyme disease, etc.). The data compiled for this report contain no label indication text. |
| Predicted New Indication (rank 1) | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score (rank 1) | 99.76% |
| Evidence Level (rank 1) | L5 |
| Best-Supported Candidate | Urinary tract infection (score 99.62%, Evidence Level L3) |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs/ANDAs | 5 (all cancelled) |
| Recommended Decision | Hold (rank 1); UTI is a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, cefuroxime is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis.

**Rank 1 (polyclonal hyperviscosity syndrome):** There is no identifiable mechanistic link. This is a plasma protein and immunoglobulin disorder, and an antibacterial has no known effect on it. The high score is a graph-based artifact with no trial or literature support. The same applies to the other top-scoring predictions with no evidence, such as hyperamylasemia, congenital analbuminemia, premalignant hematological system disease and blood group incompatibility.

**Best-supported candidate (UTI):** Cefuroxime is active against common uropathogens such as *E. coli*, *Klebsiella* and *Proteus*, so the mechanism is biologically coherent. UTI is also close to cefuroxime's already-labeled bacterial infection indications, so this is an extension of existing use rather than novel repurposing. Rising resistance and the cancelled-only US market status limit its practical value.

**Other candidates:** Suppurative otitis media overlaps with an already-labeled indication, and the evidence is indirect (reviews and susceptibility studies). Peptostreptococcus infection is plausible for a beta-lactam, but the only evidence is a 1981 in-vitro paper centered on ceftazidime.

---

## Clinical Trial Evidence

Trials linked to UTI (rank 6). No other candidate has linked clinical trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Effect of inappropriate cefuroxime therapy in adults hospitalized with pyelonephritis. Directly relevant, but observational rather than an interventional efficacy trial. |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotics in pregnant women with recurrent UTI. Relevant to prophylaxis; the specific agent is uncertain. |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | One-week antimicrobial solutions to prevent UTI before minimally invasive upper tract lithotomy. Cefuroxime's role is unclear. |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Antibiotic prophylaxis at urinary catheter removal. Prevention rather than treatment; agent not clearly cefuroxime. |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Withdrawn | 0 | Antibiotic prophylaxis for postpartum infections after caesarean section. No participants enrolled, so no data. |

---

## Literature Evidence

Selected publications linked to UTI (rank 6), prioritizing comparative and review literature.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | Randomized comparison | Infection | Aztreonam vs cefuroxime in hospitalized patients with gram-negative upper UTI |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | Lancet Infect Dis | De-escalation from antipseudomonal β-lactams in Enterobacterales bloodstream infection (indirect) |
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Systematic review | Pharmacotherapy | Oral β-lactams versus TMP/SMX and fluoroquinolones for complicated UTI |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil: antibacterial activity, pharmacokinetics and therapeutic efficacy |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Review | Int J Antimicrob Agents | Cefuroxime axetil overview; sensitive against major respiratory pathogens |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Review | Ther Drug Monit | Cefuroxime antimicrobial activity, pharmacology and clinical efficacy |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Cefuroxime mechanism, spectrum, pharmacokinetics and indications |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Cohort/epidemiology | Infect Dis Clin Microbiol | Causative organisms and ESBL risk factors in community-acquired UTI |

---

## US Market Information

All five US authorizations are cancelled; no currently valid license exists. Approved-indication text is not available in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065048 | Cefuroxime (Hikma) | Injection, powder, for solution | Not available (cancelled) |
| ANDA065308 | Cefuroxime Axetil (NorthStar Rx) | Tablet | Not available (cancelled) |
| ANDA065496 | Cefuroxime axetil (A-S Medication Solutions) | Tablet, film coated | Not available (cancelled) |
| ANDA064125 | Cefuroxime sodium (Sagent) | Injection, powder, for solution | Not available (cancelled) |
| NDA050780 | Cefuroxime and Dextrose (B. Braun) | Injection, solution | Not available (cancelled) |

---

## Safety Considerations

- **Disease contraindication signals (knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions:** 100 interactions were identified, all of the 20 listed being Moderate severity. Main groups:
  - Acid-reducing agents: famotidine, ranitidine, cimetidine, nizatidine, and proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole)
  - Antacids: aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate/hydroxide/oxide
  - Aminoglycosides: kanamycin, neomycin
  - Balsalazide

Please refer to the package insert for warnings and contraindications from the label.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, polyclonal hyperviscosity syndrome). UTI and suppurative otitis media are best treated as research questions.

**Rationale:**
- The highest-scoring predictions have no mechanistic rationale and no clinical or literature support, so the scores should not be relied upon.
- The best-supported candidates (UTI, otitis media) overlap with existing antibacterial uses. Their evidence is mostly observational, prophylaxis-focused or indirect, with no Phase 3 RCT. Rising resistance and the cancelled-only US market status further limit value.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Cefuroxime-specific comparative trials for UTI, if pursued
- Confirmation of whether a currently marketed cefuroxime product exists in the US, since all listed licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

