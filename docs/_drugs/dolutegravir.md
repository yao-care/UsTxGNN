---
layout: default
title: Dolutegravir
parent: Moderate Evidence (L3-L4)
nav_order: 620
evidence_level: L4
indication_count: 3
monitor_inn: "DOLUTEGRAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Dolutegravir
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

# Dolutegravir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir is an HIV-1 integrase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**,
but the evidence is thin: **0 clinical trials** and **1 publication** (a veterinary study of combination antiretroviral therapy) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| US Market Status | Cancelled only |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, dolutegravir is an integrase strand transfer inhibitor (INSTI). It blocks the step in which viral DNA is inserted into the host genome, which is essential for lentiviral replication.

Feline immunodeficiency virus (FIV) is a lentivirus that causes progressive immune dysfunction in cats, much like HIV in humans. It has its own integrase enzyme, which is related to HIV-1 integrase, so INSTI activity is biologically plausible. The high TxGNN score likely reflects this shared lentiviral biology and the drug's original HIV/AIDS indications.

Two caveats apply. First, this is a veterinary indication, so its relevance to human drug repurposing is limited. Second, the mechanism is inferred from drug-class knowledge rather than confirmed by source data.

Two other predictions were also generated but are not the focus of this report:
- **Simian immunodeficiency virus infection** (score 99.85%, evidence level L4): supported by 14 preclinical or animal-model publications, including dolutegravir monotherapy in SIV-infected macaques. These support the mechanism and model use, not a human therapeutic indication.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.80%, evidence level L5): no mechanistic link, trials, or literature could be identified. It is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical/veterinary study | Viruses | Evaluated pharmacokinetics and clinical outcomes of combination antiretroviral therapy (dolutegravir 2.5 mg/kg, tenofovir 20 mg/kg, emtricitabine 40 mg/kg) in FIV-infected cats. The study design could not be confirmed, and the evidence is not specific to dolutegravir alone. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213983 | Tivicay PD | Tablet, for suspension | Not available (status: cancelled) |
| NDA204790 | Tivicay | Tablet, film coated | Not available (status: cancelled) |

Both authorizations are held by ViiV Healthcare Company and are listed as cancelled; no currently valid authorization appears in the data compiled for this report.

## Safety Considerations

- **Drug Interactions**: The interaction screening completed and found **62 interacting drugs**. Of these, 20 are shown in the data compiled for this report. The main ones are:
  - **Major**: polyvalent-cation products, including aluminum hydroxide, magaldrate, attapulgite, kaolin, iron, and several calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate, phosphate) and magnesium salts (carbonate, chloride, citrate). These generally reduce dolutegravir absorption through chelation, so dosing needs to be separated from them.
  - **Minor**: aprepitant, cimetidine, clarithromycin, clotrimazole, dexamethasone.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a single veterinary study of a multi-drug regimen, with no registered clinical trials, so this is effectively a model-level prediction (L4). The indication is also non-human, and both US authorizations are cancelled, which limits any practical repurposing path.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- Full-text review of PMID 37112803 to confirm study design and the specific contribution of dolutegravir
- Dolutegravir-specific in vitro activity data against FIV integrase
- A decision on whether a veterinary development path is within scope, since the indication is not a human disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

