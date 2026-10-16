---
layout: default
title: Nevirapine
parent: Moderate Evidence (L3-L4)
nav_order: 962
evidence_level: L4
indication_count: 3
monitor_inn: "NEVIRAPINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Nevirapine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Nevirapine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**,
but there are currently **0 clinical trials** and only **indirect literature** (13 publications, mostly in vitro or animal-model work, none showing direct activity of nevirapine against wild-type SIV).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection / AIDS |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 9 (all cancelled; listed as ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nevirapine is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI). Its efficacy in HIV infection is established, and SIV is a closely related lentivirus, so a model that relies on viral similarity would naturally link the two.

However, the mechanistic link is weak. SIV reverse transcriptase is naturally resistant to most NNRTIs, as is HIV-2's. The literature is consistent with this: SIV/HIV chimeric viruses (RT-SHIV), in which the SIV RT is replaced by HIV-1 RT, are used specifically to model NNRTI susceptibility in macaques. The high TxGNN score is therefore likely driven by lentiviral similarity rather than direct evidence of nevirapine activity against wild-type SIV.

SIV infection is also an animal disease with no direct human clinical relevance as a repurposing target. The literature assessment here was based mainly on titles and partial abstracts.

Two other predictions were also reviewed and are not supported either:
- **Feline acquired immunodeficiency syndrome** (score 99.85%): one 2023 biochemical and structural study compared NNRTIs against feline immunodeficiency virus RT. This is indirect evidence only, the binding pocket differs from HIV-1 RT, and NNRTIs are generally weak against FIV. It is a veterinary indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.82%): no trials, no literature, and no evident mechanistic connection.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Animal model | AIDS Res Hum Retroviruses | Monkey model (RT-SHIV) for studying emergence and reversal of reverse transcriptase drug resistance |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model | Virology | RT-SHIV transmitted efficiently by the vaginal route in rhesus macaques |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro | J Virol | SIV-HIV chimera expressing HIV-1 RT; NNRTIs do not effectively inhibit SIV RT |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro | Biochem Biophys Res Commun | Sensitivity/resistance profile of RT-SHIV toward NNRTIs; SIV itself was inhibited only by nucleoside inhibitors |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Susceptibility of HIV-2, SIV and SHIV to approved anti-HIV-1 drugs; relevant to treatment and post-exposure prophylaxis |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | In vitro | Virology | NRTIs and NNRTIs used to inhibit endogenous reverse transcription of HIV-1 and SIV virions |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Ann Emerg Med | HIV post-exposure prophylaxis; animal studies show antiretrovirals can reduce SIV infection (not specific to nevirapine) |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro | Antimicrob Agents Chemother | Integrase inhibitor L-708,906 combined with nevirapine was subsynergistic; nevirapine was not the subject |

These are the most relevant of the 13 publications retrieved. The remainder concern other compounds (for example integrase or protease inhibitors) and do not bear on nevirapine against SIV.

## US Market Information

All nine authorizations are generic applications (ANDA) with cancelled status. No approved indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206879 | Nevirapine (Macleods) | Extended-release tablet | Not available |
| ANDA205651 | Nevirapine (Mylan) | Extended-release tablet | Not available |
| ANDA077521 | Nevirapine (Aurobindo) | Tablet | Not available |
| ANDA078584 | Nevirapine (Camber) | Tablet | Not available |
| ANDA077702 | Nevirapine (Aurobindo) | Suspension | Not available |

## Safety Considerations

- **Related disease associations (from the knowledge graph, not label text)**: liver failure, liver disease, drug-induced liver injury, chronic hepatitis B and C virus infection, gallbladder disease, rash (exanthem), Stevens-Johnson syndrome, toxic epidermal necrolysis (Lyell syndrome), rhabdomyolysis, and nodular fasciitis.
- **Drug Interactions**: 100 interactions were identified, which is a heavy burden (consistent with CYP3A4/2B6 induction). The listed examples are all moderate-level: rabeprazole, bupropion, aprepitant, triamcinolone, dexamethasone, betamethasone, budesonide, clarithromycin, saxagliptin, eliglustat, linagliptin, naltrexone, cisapride, ondansetron, and prednisolone.

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and indirect in vitro and animal-model literature. The literature points toward SIV being naturally resistant to nevirapine, SIV infection has no human clinical relevance, and nevirapine currently has no valid US authorizations. The safety profile (hepatotoxicity, severe skin reactions, large interaction burden) adds further concern.

**To proceed, the following is needed:**
- Direct evidence of nevirapine activity against wild-type SIV (currently contradicted by available literature)
- Confirmation that SIV or any related animal indication is a meaningful repurposing target
- Mechanism of action data (MOA)
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Full-text review of the literature, since the assessment so far relied mainly on titles and partial abstracts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

