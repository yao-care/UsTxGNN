---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

Using the TxGNN pipeline context and the v5 report format, I'll now generate the evaluation report. Note that among the 10 predicted indications, I'm featuring **gonococcal urethritis** (rank 5) as the focal indication — it is the only prediction with a positive recommendation (Proceed with Guardrails) and meaningful clinical evidence (L2), making it the pharmacologically actionable finding. The higher-ranked TxGNN predictions (ranks 1–4) all carry mechanistic contradictions or zero evidence and remain on Hold.

---

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Aztreonam is a synthetic monobactam antibiotic developed for serious gram-negative bacterial infections, working by inhibiting cell wall synthesis in gram-negative pathogens.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis** — a mechanistically plausible repurposing given rising antimicrobial resistance in *Neisseria gonorrhoeae* —
with **1 completed Phase 2/3 clinical trial** and **8 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (not recorded in current regulatory database) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed (0 approved licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction selection:** TxGNN ranks 1–4 (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, Ureaplasma urethritis) all carry mechanistic contradictions or model false-positive flags with zero supporting evidence, and are classified Hold/S0. Gonococcal urethritis (rank 5) is the first prediction with a coherent mechanistic link, completed Phase 2/3 trial data, and a positive recommendation.

---

## Why is This Prediction Reasonable?

Aztreonam is a monocyclic β-lactam (monobactam) antibiotic with a unique structural feature: it is selectively active against aerobic gram-negative bacteria and has no meaningful activity against gram-positive organisms or anaerobes. Its mechanism centers on binding to **Penicillin-Binding Protein 3 (PBP3)** — and specifically **PBP2** in *Neisseria gonorrhoeae* — thereby disrupting peptidoglycan cross-linking and triggering bacterial lysis. Crucially, aztreonam is stable against many β-lactamases, making it a candidate for strains resistant to conventional penicillins.

*Neisseria gonorrhoeae*, the causative pathogen of gonococcal urethritis, is a gram-negative diplococcus that falls squarely within aztreonam's spectrum of activity. The CDC has classified antimicrobial-resistant (AMR) *N. gonorrhoeae* as one of the nation's top three **urgent** AMR threats. Since parenteral third-generation cephalosporins (ceftriaxone) represent the last remaining first-line class with consistent efficacy, identifying repurposed agents is a public health priority. Aztreonam achieves MIC values against gonococci that are within clinically attainable serum concentrations following intramuscular dosing.

The evidence chain spans four decades. Early clinical studies from 1983–1986 confirmed aztreonam's efficacy against both penicillin-sensitive and penicillinase-producing *N. gonorrhoeae* (PPNG) strains at various anatomical sites. A 2020 single-arm open-label clinical trial and its companion Phase 2/3 demonstration study (NCT03867734, completed 2019) specifically evaluated 2 g intramuscular aztreonam for pharyngeal gonorrhea in the modern AMR context. This mechanistic-to-clinical evidence arc makes the TxGNN prediction biologically and clinically sound.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Demonstration study evaluating aztreonam 2 g IM for pharyngeal *N. gonorrhoeae* infection in men; designed to address the urgent need for alternative regimens against AMR gonorrhea; conducted April–September 2019 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm Clinical Trial | *Antimicrobial Agents and Chemotherapy* | Open-label single-dose aztreonam 2 g IM for *N. gonorrhoeae*; companion publication to NCT03867734; directly evaluates pharyngeal eradication in the AMR era |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical Study | *Antimicrobial Agents and Chemotherapy* | Aztreonam 1 g IM vs. spectinomycin 2 g IM for uncomplicated gonorrhea; no treatment failures with either drug; efficacy confirmed at urethral, rectal, and endocervical sites |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical Study | *Genitourinary Medicine* | Aztreonam 1 g IM single-dose cleared infection in 61 men and 26 women at all anatomical sites; effective against both penicillin-sensitive and penicillin-resistant strains; well tolerated with no adverse effects |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Clinical Study | *Journal of Infectious Diseases* | Aztreonam efficacy against penicillinase-producing *N. gonorrhoeae* (PPNG); provides an alternative when both penicillin and spectinomycin fail; early proof-of-concept against resistant strains |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Clinical Evaluation | *Japanese Journal of Antibiotics* | Bacteriological and clinical evaluation in 30 male patients with gonococcal urethritis; MIC data reported for 61 strains including 9 PPNG strains (15%); clinical outcomes assessed |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Clinical Cohort | *Acta Urologica Japonica* | Epidemiological and therapeutic study of single-shot aztreonam for gonorrheal infections; demographic data across age groups including identification of beta-lactamase-producing strains |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Clinical Study | *Giornale Italiano di Dermatologia e Venereologia* | Early Italian clinical study of aztreonam in acute gonococcal urethritis; one of the earliest European confirmatory reports |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Microbiological Surveillance | *Journal of Infection and Chemotherapy* | Emergence of cephem- and aztreonam-high-resistant *N. gonorrhoeae* strains not producing β-lactamase in Japan; critical resistance monitoring data relevant to ongoing utility assessment |

---

## US Market Information

No approved product authorizations for aztreonam are recorded in the current regulatory database (total licenses: 0; market status: not marketed).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| — | — | — | No licensed products on record |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data gap noted:** Key warnings, contraindications, and drug-drug interaction data are not available in this Evidence Pack. Obtaining the full prescribing information (package insert / SmPC) is required before any clinical planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aztreonam's mechanism of action directly targets gram-negative cell wall synthesis via PBP2 in *N. gonorrhoeae*, providing a mechanistically coherent basis for treating gonococcal urethritis. The evidence base — spanning one completed Phase 2/3 demonstration trial (NCT03867734, n=32) plus eight clinical publications from 1983–2020 — meets L2 criteria, and the severe AMR resistance context elevates the public health urgency for alternative regimens.

**To proceed, the following is needed:**

- **Full prescribing information / package insert** — Required to complete S1 safety screening; key warnings, contraindications, and drug interactions are currently unresolved data gaps
- **Mechanistic confirmation (MOA documentation from DrugBank)** — Formal documentation of PBP2 binding in *N. gonorrhoeae* to support regulatory submissions
- **Primary outcome data from NCT03867734** — The trial is completed but bacterial eradication rates (the primary efficacy endpoint) are not available in this Evidence Pack; confirm results via ClinicalTrials.gov or published report
- **AMR surveillance data** — Current local MIC distributions for *N. gonorrhoeae* against aztreonam to assess whether historical efficacy translates to contemporary strains
- **Route-of-administration confirmation** — Intramuscular formulation availability in the target jurisdiction must be verified before clinical planning

---

> ⚠️ *This report is for research reference only and does not constitute medical advice. Any repurposing candidate requires clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

