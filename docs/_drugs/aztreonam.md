---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Gram-Negative Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Aztreonam is a monobactam antibiotic that inhibits bacterial cell-wall synthesis (PBP3) and is used against gram-negative infections. The TxGNN model ranks **polyclonal hyperviscosity syndrome** as its top prediction, but **no clinical trials and no publications** support it, and the mechanism is implausible, so it is most likely a knowledge-graph artifact. Among the 10 predicted indications, **gonococcal urethritis** (rank 5) is the only one with meaningful clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-negative bacterial infections (the approved indication text is not included in the record; this is based on the drug's antibacterial class) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, aztreonam is a monobactam beta-lactam that inhibits penicillin-binding protein 3 (PBP3) in gram-negative bacteria. Its efficacy in bacterial infections is established.

For polyclonal hyperviscosity syndrome, **the prediction is not mechanistically reasonable**. The condition involves elevated serum immunoglobulins and blood viscosity. Aztreonam has no known effect on immunoglobulin levels or viscosity, and the high score is likely a knowledge-graph artifact. Several other top-ranked predictions (hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease) show the same problem: they are laboratory findings, genetic disorders or non-infectious conditions with no plausible antibacterial mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

## Other Predicted Indications Worth Noting

| Rank | Predicted Indication | Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|------|
| 1 | Polyclonal hyperviscosity syndrome | 99.73% | L5 | Hold | No plausible link |
| 2 | Hyperamylasemia | 99.73% | L5 | Hold | Laboratory finding, not an infection |
| 3 | Congenital analbuminemia | 99.69% | L5 | Hold | Genetic disorder |
| 4 | Ureaplasma urethritis | 99.59% | L5 | Hold | Ureaplasma has no cell wall, so beta-lactams are expected to be inactive |
| 5 | **Gonococcal urethritis** | 99.59% | **L2** | Research Question | Direct mechanism and clinical data |
| 6 | Blood group incompatibility | 99.59% | L5 | Hold | The only retrieved paper is unrelated (plasmid genomics) |
| 7 | Premalignant hematological system disease | 99.54% | L5 | Hold | No antineoplastic activity |
| 8 | Epiglottitis | 99.53% | L4 | Hold | Plausible (*H. influenzae* coverage), but cephalosporins are standard |
| 9 | Monoclonal gammopathy | 99.50% | L4 | Hold | Supports treating infections in this population, not the disease itself |
| 10 | Xanthogranulomatous pyelonephritis | 99.49% | L5 | Hold | Plausible organisms, but management is surgical and no evidence was found |

### Gonococcal urethritis (rank 5): the strongest candidate

Aztreonam inhibits PBP3 and has documented activity against *Neisseria gonorrhoeae*, including penicillin-resistant strains.

- **Trial:** [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) is a completed Phase 2/3 demonstration study (n=32, 2019) of aztreonam for **pharyngeal** gonorrhea. It appears non-randomized and does not directly show urethral efficacy.
- **Recent literature:** [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) (Antimicrob Agents Chemother, 2020) is a single-arm open-label trial of single-dose intramuscular aztreonam 2 g for *N. gonorrhoeae*.
- **Historical clinical studies (1983–1986):** Single-dose aztreonam cleared uncomplicated gonorrhea in several small studies ([3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) vs spectinomycin, no failures; [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/), 87 patients cleared; [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/), 30 men with urethritis).
- **Resistance concern:** [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) (2001) reported non-beta-lactamase-producing gonococci with high-level cephem and aztreonam resistance.
- **Limitations:** There is no randomized comparison against ceftriaxone, sample sizes are small, and aztreonam is parenteral only. The realistic niche is a reserve option for cephalosporin-resistant or beta-lactam-allergic patients.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA050580 | AZACTAM | Injection, powder, for solution | A-S Medication Solutions |
| NDA050580 | AZACTAM | Injection, powder, for solution | E.R. Squibb & Sons, L.L.C. |
| ANDA206517 | Aztreonam | Injection, powder, lyophilized, for solution | Hospira, Inc. |
| NDA050580 | AZACTAM | Injection, powder, for solution | E.R. Squibb & Sons, L.L.C. |
| ANDA065439 | Aztreonam | Injection, powder, lyophilized, for solution | Fresenius Kabi USA, LLC |

All listed products are injectables. The record contains 7 authorizations in total; the 5 shown are the main entries.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, polyclonal hyperviscosity syndrome, has no clinical or literature support and no plausible mechanism, so the score reflects a knowledge-graph artifact. The only clinically supported direction is gonococcal urethritis, which is better handled as a separate research question than as this prediction.

**To proceed, the following is needed:**
- Drop polyclonal hyperviscosity syndrome and the other non-infectious predictions from active consideration, unless new mechanistic evidence emerges.
- For gonococcal urethritis: a randomized trial against ceftriaxone with urogenital endpoints, plus current aztreonam susceptibility data for *N. gonorrhoeae*.
- Package insert warnings and contraindications (blocking gap for safety screening).
- Mechanism of action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

