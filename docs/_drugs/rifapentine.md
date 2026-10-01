---
layout: default
title: Rifapentine
parent: Model Prediction Only (L5)
nav_order: 1121
evidence_level: L5
indication_count: 10
---

# Rifapentine
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

# Rifapentine: From Tuberculosis to Leprosy

## One-Sentence Summary

Rifapentine (brand name Priftin) is a rifamycin antibiotic that is marketed in the US and used against tuberculosis. The supplied license record carries no indication text, so this original indication comes from the drug's known use and from the tuberculosis focus of the retrieved trials. The TxGNN model predicts it may be useful for **leprosy**, with **0 registered clinical trials** and **20 retrieved publications** (about half are leprosy-relevant), including a 2023 NEJM study of single-dose rifapentine in household contacts. The evidence concerns **prevention after exposure** rather than treatment, and its design has not been verified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (not stated in the supplied license record) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 (provisional; upgrade to L1 only if the NEJM study is verified as a Phase 3 RCT) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Based on class knowledge, rifapentine is a rifamycin that inhibits bacterial DNA-dependent RNA polymerase (rpoB). Its efficacy in mycobacterial disease (tuberculosis) is established.

*Mycobacterium leprae* is susceptible to rifampicin, a close relative. In mouse footpad models, rifapentine showed stronger bactericidal activity than rifampicin. Rifapentine also has a longer half-life and lower minimum inhibitory concentrations. Together these make the leprosy prediction mechanistically coherent.

The strongest clinical signal is a randomized study of single-dose rifapentine as post-exposure prophylaxis in household contacts of leprosy patients (PMID 37195940). Only the title and background were supplied, so its design and results have not been checked. The other evidence is preclinical: post-exposure prophylaxis in mice, activity against rifampicin-resistant strains, and combination regimens.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for leprosy.

---

## Literature Evidence

Study types marked "title-based" were inferred from titles only. Abstracts supplied were mostly background sections, so no efficacy results are claimed here.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37195940](https://pubmed.ncbi.nlm.nih.gov/37195940/) | 2023 | RCT (title-based, design unverified) | N Engl J Med | Single-dose rifapentine in household contacts of leprosy patients. Background: rifapentine is more bactericidal than rifampin in mice, but data on preventing leprosy were lacking. |
| [37585641](https://pubmed.ncbi.nlm.nih.gov/37585641/) | 2023 | Correspondence | N Engl J Med | Commentary on the household-contact study. No abstract supplied. |
| [40278757](https://pubmed.ncbi.nlm.nih.gov/40278757/) | 2025 | Review | Trop Med Infect Dis | Reviews efficacy, safety and feasibility of rifamycin-based post-exposure chemoprophylaxis. Notes WHO's 2021 recommendation, based on the COLEP study's 57% reduction in leprosy incidence among contacts. |
| [38440733](https://pubmed.ncbi.nlm.nih.gov/38440733/) | 2024 | Review | Front Immunol | Leprosy treatment, prevention and immunity. Notes that rifampicin-resistant strains threaten multidrug therapy. |
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasit Vectors | Pipeline review of oral anti-infectives for off-label use against neglected tropical diseases. |
| [32936818](https://pubmed.ncbi.nlm.nih.gov/32936818/) | 2020 | Preclinical (mouse footpad) | PLoS Negl Trop Dis | Compared post-exposure prophylaxis efficacy of rifampin, rifapentine, moxifloxacin, minocycline and clarithromycin, to guide clinical trial choices. |
| [30207440](https://pubmed.ncbi.nlm.nih.gov/30207440/) | 2016 | Preclinical (mouse) | Indian J Lepr | Antibacterial activity of rifapentine and combinations in a rifampicin-resistant leprosy model. |
| [30207441](https://pubmed.ncbi.nlm.nih.gov/30207441/) | 2016 | Preclinical (mouse) | Indian J Lepr | Tested rifapentine and combinations as short-duration alternatives to WHO multidrug therapy. |
| [10991891](https://pubmed.ncbi.nlm.nih.gov/10991891/) | 2000 | Preclinical (mouse) | Antimicrob Agents Chemother | Compared bactericidal activity of rifapentine, moxifloxacin and HMR 3647 against *M. leprae* with rifampin, ofloxacin and clarithromycin. |
| [11201894](https://pubmed.ncbi.nlm.nih.gov/11201894/) | 2000 | Preclinical (mouse) | Lepr Rev | Rifapentine-moxifloxacin-minocycline combination, evaluated as a monthly, fully supervisable regimen. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA 021024 | Priftin (sanofi-aventis U.S. LLC) | Tablet, film coated (oral) | Not stated in the supplied record |

---

## Safety Considerations

- **Drug Interactions**: The structured interaction query returned no records. This is a data gap, not evidence of no interactions. Rifapentine induces CYP3A4/UGT, so antiretroviral interactions are the main concern. Pharmacokinetic studies exist with dolutegravir, efavirenz, nevirapine and other agents.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is coherent and the NEJM prophylaxis study is a promising signal, but its design is unverified. It concerns prevention, not treatment, and no leprosy trial is registered. The package insert safety data is missing, which the evidence pack flags as blocking.

**To proceed, the following is needed:**
- Verify the design, phase and results of PMID 37195940, and locate its trial registration number. Upgrade to L1 only if it is confirmed as a Phase 3 RCT.
- Clarify whether the target is post-exposure prophylaxis or treatment, since the evidence covers prophylaxis only.
- Obtain the package insert warnings and contraindications (DG001).
- Obtain mechanism of action data from DrugBank (DG002).
- Build a dedicated interaction review for CYP3A4/UGT substrates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

