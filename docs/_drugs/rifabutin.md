---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 1120
evidence_level: L5
indication_count: 10
---

# Rifabutin
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

# Rifabutin: From MAC Infection Prophylaxis / HIV-TB Co-treatment to HIV Infectious Disease

## One-Sentence Summary

> Rifabutin is a rifamycin-class antibiotic already established for preventing and treating disseminated *Mycobacterium avium* complex (MAC) infection in AIDS patients and for treating HIV-tuberculosis co-infection.
> The TxGNN model's top-ranked prediction is **HIV infectious disease** — but as the evidence pack itself flags, this largely reflects an **already-approved use** rather than a novel repurposing signal.
> Support is very strong (**44 clinical trials, 22 publications**), but this is confirmatory evidence, not discovery evidence. A more genuinely novel candidate — **leprosy** (rank 6, L3, Research Question) — is discussed separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in Taiwan license data (drug not marketed in Taiwan). Per the evidence pack's clinical rationale, Rifabutin's established global indication is prevention/treatment of disseminated MAC infection in AIDS patients and treatment of HIV-related tuberculosis. |
| Predicted New Indication | HIV infectious disease *(see caveat: substantially overlaps with an already-approved use, not a novel signal)* |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although the drug-level mechanism-of-action field is marked as a data gap, the clinical evidence embedded in this pack indicates that Rifabutin, a semisynthetic rifamycin, inhibits mycobacterial DNA-dependent RNA polymerase — the same core mechanism as rifampicin, giving it broad activity against *Mycobacterium avium* complex, *M. tuberculosis*, and *M. leprae*.

The TxGNN model's top prediction, "HIV infectious disease," is best understood through this mechanistic lens: Rifabutin has **no direct antiretroviral activity**. Its clinical role in HIV care is as an anti-mycobacterial agent used to prevent/treat opportunistic MAC infection and to treat tuberculosis in HIV-co-infected patients — a role it already holds by regulatory approval elsewhere. The evidence pack's own rationale explicitly flags this: *"此為FDA已核准之標準適應症（非新穎老藥新用）"*. In other words, TxGNN has correctly recovered a known knowledge-graph relationship rather than surfaced a new repurposing opportunity — a useful validation of the model, but not a new drug-development lead.

A more genuinely novel signal in this evidence pack is **leprosy** (rank 6, L3 evidence, "Research Question"): Rifabutin shares rifampicin's RNA-polymerase-inhibiting mechanism and has documented *in vivo* activity against *M. leprae* in armadillo and mouse models, with literature explicitly discussing it as a candidate substitute for rifampicin-resistant or rifampicin-intolerant leprosy patients — but no human RCT confirms efficacy. Other ranked predictions (multiple endocrine neoplasia, sclerosing cholangitis, a rare neurodevelopmental disorder, feline AIDS, SIV infection) have zero supporting evidence and no plausible mechanistic link, and should be held. Conjunctivitis is notable for having evidence pointing in the *opposite* direction — a single review lists Rifabutin as a cause of drug-induced ocular inflammation, not a treatment.

---

## Clinical Trial Evidence
*(for predicted indication: HIV infectious disease)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002032](https://clinicaltrials.gov/study/NCT00002032) | NA | Completed | 750 | Double-blind, placebo-controlled trial of oral rifabutin for prevention of MAC bacteremia in AIDS patients with CD4 ≤200; key foundational evidence for the approved indication |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1,100 | Large RCT comparing clarithromycin vs. rifabutin vs. combination for prevention of MAC bacteremia/disseminated disease in HIV patients with CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Randomized study of daily/intermittent azithromycin and rifabutin regimens for prevention of disseminated MAC and fungal infections |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Three-arm trial of clarithromycin/ethambutol ± rifabutin (two doses) vs. placebo for treatment of MAC bacteremia in AIDS |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Comparison of four clarithromycin/ethambutol/rifabutin or clofazimine regimens for disseminated MAC disease in AIDS |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2/3 | Completed | 246 | Multicenter RCT comparing clarithromycin-containing combination regimens (including rifabutin) for disseminated MAC disease |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | NA | Completed | 215 | TBTC Study 23: treatment of HIV-related tuberculosis using an intermittent rifabutin-based regimen |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | NA | Completed | 200 | Double-blind RCT of a rifabutin regimen for MAC bacteremia treatment in AIDS patients |
| [NCT00002343](https://clinicaltrials.gov/study/NCT00002343) | Phase 4 | Completed | 200 | PK/PD study of rifabutin ± ethambutol for MAC prophylaxis in AIDS patients with CD4 ≤100 |
| [NCT00004736](https://clinicaltrials.gov/study/NCT00004736) | Phase 1 | Completed | 44 | Viral/immune dynamics of HAART in HIV patients with tuberculosis, supporting the HIV-TB co-treatment context |

*Note: the majority of the remaining ~34 registered trials in this evidence pack are pharmacokinetic drug-drug interaction studies between rifabutin and antiretrovirals (efavirenz, nevirapine, protease inhibitors, dolutegravir, cabotegravir, etc.), reflecting rifabutin's role as a CYP3A inducer requiring dose adjustment in ART regimens rather than direct efficacy evidence.*

---

## Literature Evidence
*(for predicted indication: HIV infectious disease)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Cochrane Review | Cochrane Database Syst Rev | Rifamycins (including rifabutin) vs. isoniazid for TB prevention; supports rifamycin-based regimens as shorter, higher-completion alternatives |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiology Spectrum | Comprehensive review of the bidirectional TB-HIV disease relationship, framing rifabutin's role in co-treatment |
| [21726477](https://pubmed.ncbi.nlm.nih.gov/21726477/) | 2009 | Clinical Evidence Review | BMJ Clinical Evidence | Reviews treatment approaches for HIV-TB co-infection including rifamycin-based regimens |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort/PK | J Antimicrob Chemother | Rifabutin PK and safety in TB/HIV-coinfected children on LPV/r-based second-line ART; notes prior neutropenia signal |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety and efficacy of rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir-based ART |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | Cohort/PK | J Antimicrob Chemother | PK and short-term safety of rifabutin combined with lopinavir/ritonavir in young HIV-infected children |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | Pooled PK Analysis | J Antimicrob Chemother | Population PK pooled analysis of rifabutin-HIV protease inhibitor interactions, informing dosing recommendations |
| [16206114](https://pubmed.ncbi.nlm.nih.gov/16206114/) | 2005 | PK Study | Clin Infect Dis | Evaluates the rifabutin-efavirenz interaction and dose-adjustment recommendations in HIV-TB patients |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Population PK Model | Br J Clin Pharmacol | Rifabutin-dolutegravir drug-drug interaction, positioning rifabutin as an alternative to rifampicin in integrase-inhibitor regimens |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | PK Review | Clinical Pharmacokinetics | Foundational clinical pharmacokinetics review supporting rifabutin's use for MAC prophylaxis in HIV-positive patients |

---

## Market Information (Taiwan)

Rifabutin currently holds **no marketing authorization in Taiwan** (0 licenses; market status: 未上市/Not Marketed). No product name, dosage form, or Taiwan-approved indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The evidence pack flags a **Blocking**-severity data gap (DG001 – TFDA package insert warnings/contraindications) that must be resolved before this candidate can undergo formal safety review (S1). Drug interaction data is also marked "not found" in this pack; however, the clinical trial and literature evidence above independently documents extensive, clinically significant interactions between rifabutin and antiretrovirals (protease inhibitors, NNRTIs, integrase inhibitors) via CYP3A induction/inhibition, requiring dose adjustment in any HIV-TB co-treatment context.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clinical evidence for rifabutin in the HIV/MAC/TB context is very strong (L1: multiple completed Phase 3 RCTs, 44 trials, 22 publications) — but this largely confirms an existing approved use rather than identifying a novel repurposing opportunity, so it should be scoped as a label-extension/confirmation review rather than a new indication. Meanwhile, a Blocking data gap (missing TFDA warnings/contraindications) currently prevents any formal safety sign-off.

**To proceed, the following is needed:**
- Obtain TFDA package insert warnings/contraindications (DG001, Blocking) — required before S1 safety review can begin
- Obtain detailed MOA/pharmacology profile from DrugBank (DG002)
- Clarify Taiwan regulatory pathway, since Rifabutin currently has zero Taiwan market authorizations (未上市) — determine whether named-patient/import use is the intended pathway
- Reclassify the "HIV infectious disease" prediction internally as a known-use confirmation rather than a novel repurposing candidate, to avoid overstating novelty in downstream reporting
- If pursuing genuinely novel signals, open a separate research track for **leprosy** (rank 6, L3, mechanistically plausible via shared RNA-polymerase inhibition with rifampicin, but no human RCT yet) — this is the strongest true repurposing candidate in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

