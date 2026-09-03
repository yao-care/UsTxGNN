---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 946
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Organ Transplant Rejection Prevention to HIV Infectious Disease

## One-Sentence Summary

Mycophenolate mofetil (MMF) is a purine-synthesis-inhibiting immunosuppressant established for preventing organ transplant rejection. The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **10 clinical trials** and **20 publications** currently identified as supporting evidence, though several trials were withdrawn or have unreported outcomes.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of organ transplant rejection (kidney/heart/liver) — based on established pharmacological knowledge; not present in this evidence pack's TFDA license data (0 licenses on file) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, DrugBank-sourced mechanism-of-action data for this drug is marked as a data gap. Based on the mechanistic rationale available in the predictions, MMF is an inosine monophosphate dehydrogenase (IMPDH) inhibitor that blocks de novo purine synthesis, suppressing proliferation of activated T and B lymphocytes. This is the same mechanism that underlies its proven efficacy in preventing transplant rejection.

In HIV infection, activated CD4+ T cells are both the primary viral target and the main driver of the latent reservoir. The "virostatic" hypothesis proposes that limiting proliferation of these activated cells with MMF could reduce viral target-cell availability and reservoir expansion. Several early studies also report a pharmacodynamic synergy between MMF and abacavir, with MMF depleting intracellular dGTP pools that potentiate abacavir's antiviral activity.

However, this mechanism is inherently double-edged in HIV: immunosuppression that reduces T-cell proliferation could also impair immune reconstitution and increase susceptibility to opportunistic infection in an already immunocompromised population. This tension is reflected in the trial evidence below, where several MMF-HIV studies were withdrawn or terminated, and no completed trial demonstrates a definitive clinical benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | Withdrawn | 0 | Designed to assess MMF safety/tolerability and antiretroviral activity added to abacavir in treatment-experienced HIV patients; withdrawn, no results |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy evaluating MMF's effect on cardiovascular surrogate markers in HIV-1 patients; outcome status unconfirmed |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study: MMF in ART-naive chronically HIV-1-infected patients, assessing immune hyperactivation, CD4+ decline, and plasma HIV-1 RNA; outcome status unconfirmed |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT with fludarabine/TBI plus cyclosporine and MMF for HIV-positive patients (with/without cancer) |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Randomized, double-blind pilot comparing DAPD vs. DAPD+MMF in treatment-experienced HIV subjects |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal transplantation safety/efficacy in HIV-infected patients with end-stage renal disease; MMF used as standard post-transplant immunosuppression |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor BMT with post-transplant cyclophosphamide; MMF used for GVHD prophylaxis in hematologic malignancy, not HIV-specific |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Clinical/immunological follow-up after renal transplantation in HIV-1-infected patients on antiretroviral regimens including raltegravir |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine+MMF vs. cyclophosphamide+prednisolone for anti-r-HuEpo-associated PRCA; not an HIV indication trial |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | TBF conditioning for haploidentical HSCT in elderly high-risk AML; not an HIV indication trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Clinical study | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing ART depleted intracellular dGTP and was associated with decreased plasma HIV-1 RNA in 5 heavily treated patients |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | MMF during HAART interruption in chronic HIV-1 infection; assessed immune response and viral load in lymphatic tissue |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical trial | AIDS | HAART with or without MMF in treatment-naive HIV-1 patients; studied effect on plasma HIV-1 RNA decay and latent reservoir |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | No detrimental immunological effects observed with MMF plus HAART in treatment-naive acute/chronic HIV-1 patients |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort/PK-PD study | Clin Pharmacokinet | Pharmacokinetics/pharmacodynamics of low-dose MMF combined with abacavir, efavirenz, and nelfinavir in HIV patients |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK study | Clin Pharmacokinet | MMF's effect on antiretroviral drug pharmacokinetics and intracellular nucleoside triphosphate pools |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical trial | AIDS | Safety, tolerability, and antiretroviral activity of DAPD with or without MMF in drug-resistant HIV-1 infection |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | Open-label pilot of MMF added to salvage ART (abacavir, ddI, amprenavir, ritonavir ± efavirenz) in multidrug-resistant HIV-1 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Reviews immunosuppressive drugs, including MMF, as adjunctive strategies targeting immune hyperactivation in HIV disease |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Mechanistic/translational study | J Clin Invest | Explores selective targeting of clonally expanded HIV-infected CD4+ T cells via antiproliferative drug susceptibility |

## US Market Information

This drug is currently recorded as **not marketed** in the reviewed regulatory jurisdiction, with 0 license records on file — no NDA/product-level detail is available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are marked as data gaps in this evidence pack; note that DG001 — missing TFDA label warnings/contraindications — is flagged as a **Blocking** severity gap that prevents completion of the initial safety screen (S1).)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic rationale (IMPDH inhibition limiting activated CD4+ T-cell proliferation) is biologically plausible and supported by multiple early-phase and cohort studies, no completed trial demonstrates definitive clinical benefit — several key trials (NCT00021489, NCT00247494, NCT00120419) are withdrawn, terminated, or of unconfirmed outcome status. Critically, the Blocking data gap on TFDA label warnings/contraindications (DG001) prevents completion of even the initial safety screen for an immunosuppressant in an immunocompromised HIV population, where opportunistic infection risk is a major concern.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert warnings and contraindications to complete the S1 safety screen
- Formal DrugBank mechanism-of-action confirmation
- Outcome data retrieval for the unknown-status MAN2 studies (NCT00247494, NCT00120419)
- Drug interaction data, particularly with antiretroviral regimens
- Updated literature/trial search to capture any post-2025 developments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

