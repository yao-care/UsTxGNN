---
layout: default
title: Rifabutin
parent: High Evidence (L1-L2)
nav_order: 1120
evidence_level: L1
indication_count: 10
monitor_inn: "RIFABUTIN"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-14
description: "Rifabutin: predicted new indication HIV infectious disease (evidence level L1). Approved use: Not recorded in the local data"
---

# Rifabutin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Rifabutin: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Rifabutin is a rifamycin antibiotic that inhibits bacterial RNA polymerase. The data compiled for this report do not include an approved-indication text for it.
The TxGNN model predicts it may be useful for **HIV infectious disease**, with **35 clinical trials** and **20 publications** retrieved for this direction.
The link is indirect: rifabutin does not act on HIV itself, but it treats opportunistic mycobacterial infections (MAC, tuberculosis) in people living with HIV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L1 |
| US Market Status | Marketed (valid licenses: 2 of 2) |
| Number of NDAs | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, rifabutin is a rifamycin that inhibits bacterial DNA-dependent RNA polymerase (rpoB). It has **no direct antiviral activity** against HIV.

Its value in HIV is in treating and preventing opportunistic mycobacterial infections in people living with HIV, namely *Mycobacterium avium* complex (MAC) and tuberculosis. Compared with rifampin it is a weaker CYP3A4 inducer, so it is easier to combine with protease inhibitors and other antiretrovirals. Dose adjustment and interaction management are still required.

The high TxGNN score is therefore best read as reflecting this HIV-associated opportunistic-infection setting, not an anti-HIV effect. The "new indication" is better understood as supportive care in HIV patients than as treatment of HIV itself.

---

## Clinical Trial Evidence

Of the 35 trials retrieved, the table lists the 10 most relevant. Most trials are pharmacokinetic or drug-interaction studies; the randomized efficacy trials address MAC disease, not HIV replication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Four-regimen comparison (clarithromycin at two doses with ethambutol plus rifabutin or clofazimine) for disseminated MAC in AIDS |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Clarithromycin/ethambutol with rifabutin 450 mg, rifabutin 300 mg, or placebo for MAC bacteremia in AIDS |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Clarithromycin vs rifabutin vs combination for MAC prevention in HIV patients with CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and rifabutin, alone or combined, for preventing disseminated MAC in HIV patients |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Not labeled | Completed | 200 | Double-blind randomized trial of a rifabutin regimen for MAC bacteremia in AIDS |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Not labeled | Completed | 750 | Double-blind, placebo-controlled rifabutin monotherapy for MAC prevention in AIDS (CD4 ≤200) |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | Completed | 246 | Clarithromycin combined with rifabutin, ethambutol, or both for disseminated MAC in AIDS |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV co-infection (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV co-infection (South Africa) |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Not labeled | Completed | 215 | Intermittent rifabutin-based regimen for HIV-related tuberculosis (treatment failure and relapse rates) |

Many other registered trials are drug-interaction studies of rifabutin with antiretrovirals such as indinavir, nelfinavir, efavirenz, nevirapine, maraviroc, dolutegravir and cabotegravir.

---

## Literature Evidence

Of the 20 publications retrieved, the table lists the 10 most relevant. None is a randomized trial of rifabutin for HIV itself. They are mostly reviews, cohort studies and pharmacokinetic analyses.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Rifabutin safety and efficacy in HIV/TB-coinfected children on lopinavir/ritonavir; earlier work reported treatment-limiting neutropenia |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Rifabutin pharmacokinetics and safety in TB/HIV-coinfected children; a prior study was stopped early for severe neutropenia |
| [39037240](https://pubmed.ncbi.nlm.nih.gov/39037240/) | 2024 | Pharmacokinetic study | Antimicrob Agents Chemother | Population pharmacokinetics and dose optimization of rifabutin in HIV/TB children on lopinavir/ritonavir |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Pharmacokinetic modeling | Br J Clin Pharmacol | Rifabutin–dolutegravir interaction model; rifabutin is a less potent inducer than rifampicin |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Modeling study | Clin Infect Dis | Management of interactions between long-acting cabotegravir/rilpivirine and inducers such as rifabutin |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | Review | Int J Tuberc Lung Dis | Whether rifabutin can replace rifampicin in protease-inhibitor-based ART for TB |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Review | Drugs | Practical therapeutic approach to TB/HIV co-infection |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Review | Arch Intern Med | Update on rifampin and rifabutin drug interactions |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | Review | Drug Saf | Risk-benefit assessment of MAC therapies, including rifabutin |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Review | Med Clin North Am | Nontuberculous mycobacterial infections; MAC as the most common systemic bacterial infection in AIDS |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050689 (cancelled) | Rifabutin (Mylan Pharmaceuticals Inc.) | Capsule | Not available |
| ANDA215041 (cancelled) | Rifabutin (ANI Pharmaceuticals, Inc.) | Capsule | Not available |


---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): thrombocytopenia, neutropenia, agranulocytosis, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis. The neutropenia signal matches the treatment-limiting neutropenia reported in children given rifabutin with lopinavir/ritonavir.
- **Ocular risk**: the retrieved literature includes a report of uveitis associated with rifabutin prophylaxis and itraconazole therapy.
- **Drug interactions**: 100 interactions were identified. Among those listed, the one rated **Major** is eliglustat. Most of the others are rated Moderate, including doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, clarithromycin, metronidazole, morphine, aprepitant, pioglitazone, saxagliptin, linagliptin, chlorpropamide, acetohexamide, calcitriol, calcifediol, cholecalciferol and picosulfuric acid. Dolasetron is rated Minor. Rifabutin also has clinically important interactions with antiretrovirals (protease inhibitors, integrase inhibitors, NNRTIs), as shown by the many pharmacokinetic trials above.

Label warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large randomized Phase 3 trials support rifabutin-containing regimens for preventing and treating MAC in HIV-infected patients, and extensive pharmacokinetic data support its use alongside antiretrovirals. However, the evidence supports management of **HIV-associated opportunistic infections**, not direct treatment of HIV. The decision should be scoped accordingly.

**To proceed, the following is needed:**
- Retrieve the FDA package insert warnings, contraindications and approved indications (currently a blocking data gap for safety screening)
- Obtain mechanism-of-action data from DrugBank
- Define the intended indication precisely (MAC prophylaxis/treatment or TB in HIV) rather than "HIV infection"
- Establish a protocol for interaction management with specific antiretroviral regimens and for monitoring neutropenia, thrombocytopenia and uveitis
- Clarify the regulatory pathway given that both US licenses are cancelled

**Other predicted indications:** Leprosy (L4, preclinical and in vitro evidence only) is a research question. Endocarditis and pneumocystosis (L4) are Hold, with only case reports, reviews and animal data. Multiple endocrine neoplasia, sclerosing cholangitis, a rare neurodevelopmental disorder, conjunctivitis, feline AIDS and simian immunodeficiency virus infection (L5) are Hold, with no supporting evidence and likely TxGNN model (deep learning) artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

