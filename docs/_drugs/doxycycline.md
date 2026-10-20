---
layout: default
title: Doxycycline
parent: Model Prediction Only (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Doxycycline: predicted new indication Top-ranked: punctate epithelial keratoconjunctivitis . Best-supported… (evidence level L5). Approved use: Bronchitis, acne, bacterial pneumonia, anthrax, gonorrh…"
monitor_inn: "DOXYCYCLINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
---

# Doxycycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Doxycycline: From Bacterial Infections to Post-Bacterial Disorder (Doxycycline Post-Exposure Prophylaxis)

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic, originally used for bronchitis, acne, bacterial pneumonia, anthrax, gonorrhea and other infections.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but the best-supported direction in the data is **post-bacterial disorder**, which in practice maps to post-exposure prophylaxis against bacterial infections (doxy-PEP).
That direction is backed by **11 clinical trials** (several completed Phase 4 and Phase 2/3 studies); the top-ranked prediction has only **1 case report** and no trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, acne, bacterial pneumonia, anthrax, gonorrhea, and others (from the knowledge graph; no approved-indication text in the US license records) |
| Predicted New Indication | Top-ranked: punctate epithelial keratoconjunctivitis (rank 1). Best-supported: post-bacterial disorder (rank 4) |
| TxGNN Prediction Score | 99.94% (punctate epithelial keratoconjunctivitis); 99.89% (post-bacterial disorder) |
| Evidence Level | L4 (punctate epithelial keratoconjunctivitis); L1 (post-bacterial disorder) |
| US Market Status | Cancelled only (all 15 licenses cancelled) |
| Number of NDAs | 15 (1 NDA, 14 ANDAs) |
| Recommended Decision | Hold (top-ranked prediction); Proceed with Guardrails (post-bacterial disorder / doxy-PEP) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, doxycycline is a tetracycline-class antibiotic that inhibits bacterial protein synthesis at the 30S ribosomal subunit. It also has anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects.

**Top-ranked prediction (punctate epithelial keratoconjunctivitis).** Doxycycline is active against *Chlamydia trachomatis*, and the single supporting publication (a 1992 case report) describes punctate keratitis persisting after chlamydial conjunctivitis had been treated with tetracycline or doxycycline. This is indirect and does not show a treatment effect. The anti-inflammatory properties offer a plausible but unproven link.

**Best-supported prediction (post-bacterial disorder).** The trials map this label to prevention of bacterial infection after exposure rather than treatment of a post-infectious condition. Doxycycline's antibacterial spectrum covers chlamydia, syphilis and, partially, gonorrhea, as well as *Borrelia* (relapsing fever). Its established use against sexually transmitted and tick-borne infections is the mechanistic basis for post-exposure prophylaxis. Gonorrhea efficacy is limited by tetracycline resistance.

**Other predictions** (otitis externa, post-infectious vasculitis, infective urethral stricture, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome, exposure keratitis) rest on indirect literature, case reports, veterinary data or no evidence at all. Chronic gingivitis has some support through subantimicrobial-dose and locally delivered doxycycline, but the studies are in periodontitis, not gingivitis.

---

## Clinical Trial Evidence

Trials for post-bacterial disorder (rank 4). The other predictions have no registered trials, except post-infectious syndrome (rank 5), which overlaps with this list (NCT04050540, NCT07500415) and adds NCT07658976 (Phase 3, not yet recruiting).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04050540](https://clinicaltrials.gov/study/NCT04050540) | Phase 4 | Completed | 449 | Randomized doxy-PEP for bacterial STI prevention in Kenyan women on HIV PrEP |
| [NCT03980223](https://clinicaltrials.gov/study/NCT03980223) | Phase 4 | Completed | 641 | Doxy-PEP to reduce gonorrhea, chlamydia and syphilis in PrEP users and men with HIV who have sex with men |
| [NCT00237016](https://clinicaltrials.gov/study/NCT00237016) | Phase 2/3 | Completed | 140 | Double-blind, placebo-controlled post-exposure doxycycline for relapsing fever prevention |
| [NCT01207739](https://clinicaltrials.gov/study/NCT01207739) | Phase 4 | Completed | 280 | Prolonged oral antibiotic strategies after ceftriaxone in persistent Lyme disease |
| [NCT00351273](https://clinicaltrials.gov/study/NCT00351273) | Phase 3 | Completed | 42 | Six-month combination antibiotics for chlamydia-induced reactive arthritis (small; indirect fit) |
| [NCT04067011](https://clinicaltrials.gov/study/NCT04067011) | Phase 2 | Completed | 210 | Drug-vaccine interaction study (AV7909 anthrax vaccine with doxycycline or ciprofloxacin); not a disease-outcome study |
| [NCT06468462](https://clinicaltrials.gov/study/NCT06468462) | Phase 4 | Recruiting | 2900 | Periodic presumptive treatment vs doxy-PEP among men who have sex with men in Kenya |
| [NCT06188442](https://clinicaltrials.gov/study/NCT06188442) | Phase 4 | Active, not recruiting | 300 | On-demand doxycycline PrEP vs PEP for STI prevention |
| [NCT07397403](https://clinicaltrials.gov/study/NCT07397403) | Phase 4 | Recruiting | 400 | Efficacy and safety of doxy-PEP in men who have sex with men in Bangkok |
| [NCT04762134](https://clinicaltrials.gov/study/NCT04762134) | Not specified | Recruiting | 560 | Randomized doxycycline chemoprophylaxis for STIs in gay, bisexual and other men who have sex with men (Canada) |

One further registered trial (not listed above because the table is capped at 10) is a recruiting pilot implementation study of doxy-PEP in Brazil (NCT07500415, n=200) and a trial of early syphilis treatment with or without doxycycline (NCT06069141, n=688).

---

## Literature Evidence

Literature for the top-ranked prediction (punctate epithelial keratoconjunctivitis) and the most relevant items from other predictions. No literature was compiled for post-bacterial disorder.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients developed recurrent punctate epithelial keratitis after chlamydial follicular conjunctivitis was treated with tetracycline or doxycycline |
| [20461319](https://pubmed.ncbi.nlm.nih.gov/20461319/) | 2010 | RCT | J Contemp Dent Pract | Subantimicrobial-dose doxycycline plus scaling and root planing in chronic periodontitis with diabetes (relevant to the gingivitis/periodontal prediction, not gingivitis itself) |
| [39926939](https://pubmed.ncbi.nlm.nih.gov/39926939/) | 2024 | RCT | J Pharm Bioallied Sci | 1% alendronate gel vs 10% doxycycline gel as adjunct to scaling and root planing in chronic periodontitis |
| [35890542](https://pubmed.ncbi.nlm.nih.gov/35890542/) | 2022 | RCT | Polymers | 2% lemongrass gel vs 10% doxycycline hyclate gel as adjunct in chronic periodontitis |
| [18166090](https://pubmed.ncbi.nlm.nih.gov/18166090/) | 2008 | RCT | J Periodontol | Combined host modulation and topical antimicrobial therapy in moderate to severe periodontitis |
| [14971246](https://pubmed.ncbi.nlm.nih.gov/14971246/) | 2003 | Systematic review | Ann Periodontol | Host modulation with antiproteinase, anti-inflammatory and bone-sparing agents in chronic periodontitis |
| [31353153](https://pubmed.ncbi.nlm.nih.gov/31353153/) | 2020 | Preclinical (mouse) | Int J Cardiol | Doxycycline added to benznidazole showed no additive effect in Chagas model (negative result) |
| [37026784](https://pubmed.ncbi.nlm.nih.gov/37026784/) | 2023 | In vitro | Otol Neurotol | Tetracyclines are less cytotoxic than quinolones to human tympanic membrane fibroblasts |
| [9120367](https://pubmed.ncbi.nlm.nih.gov/9120367/) | 1997 | Case series | J Mal Vasc | Three cases of post-infectious systemic vasculitis, two recovering without corticosteroids |
| [32552113](https://pubmed.ncbi.nlm.nih.gov/32552113/) | 2020 | Retrospective case series | J Int Med Res | 22 cases of brucellar reproductive system injury (indirect to urethral stricture) |

---

## US Market Information

All 15 US licenses are cancelled; none are currently valid. The license records contain no approved-indication text. The main entries are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050641 | Doxycycline Monohydrate (Chartwell RX) | Capsule | Not available (cancelled) |
| ANDA062505 | Doxycycline Hyclate (Proficient Rx) | Tablet, film coated | Not available (cancelled) |
| ANDA207289 | Doxycycline Hyclate (Bryant Ranch Prepack) | Capsule | Not available (cancelled) |
| ANDA065055 | Doxycycline (Strides Pharma) | Capsule | Not available (cancelled) |
| ANDA210537 | Doxycycline Hyclate (Alembic) | Tablet, film coated | Not available (cancelled) |

All products are oral (tablets and capsules).

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, dyskinesia of esophagus.
- **Drug Interactions**: 100 interactions were identified; the 20 reviewed include these:
  - **Major**: isotretinoin, acitretin, aminolevulinic acid
  - **Moderate**: aluminum hydroxide, aminophylline, amobarbital, amoxicillin, ampicillin, anisindione, asparaginase (both forms), atracurium, attapulgite, bacampicillin, balsalazide, bedaquiline
  - **Minor**: acetazolamide, amiloride, bendroflumethiazide
- **Prediction-specific concerns**:
  - Antibiotic use in STEC-associated hemolytic uremic syndrome is generally avoided because it may increase toxin release.
  - Tetracycline cytotoxicity in tympanic membrane fibroblasts is a concern for topical otic use.
  - Widespread doxy-PEP raises antimicrobial resistance concerns (tetracycline resistance already limits gonorrhea efficacy).

Please refer to the package insert for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (punctate epithelial keratoconjunctivitis); Proceed with Guardrails for post-bacterial disorder (doxy-PEP)**

**Rationale:**
- The highest-scoring prediction rests on a single 1992 case report, with no trials and no evidence of a treatment effect, so it cannot advance. Most other predictions (otitis externa, vasculitis, urethral stricture, Chagas cardiomyopathy, HUS, exposure keratitis) are likewise weak or carry safety concerns.
- Post-bacterial disorder has multiple completed Phase 2/3 and Phase 4 trials, but the label actually corresponds to STI and relapsing-fever prophylaxis, which is an established antibiotic use rather than a new disease mechanism. All US licenses are cancelled, which complicates any development path.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Results and efficacy outcomes from the completed doxy-PEP trials, since this report summarises only registry descriptions
- An antimicrobial resistance monitoring plan for any prophylaxis strategy
- A decision on whether the disease label "post-bacterial disorder" meaningfully represents the prophylaxis use case
- For chronic gingivitis, verification of trial designs and gingivitis-specific (not periodontitis) outcome data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

