---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab (trade name Bavencio®) is an anti-PD-L1 immune checkpoint inhibitor that has been approved by the US FDA for Merkel cell carcinoma and locally advanced or metastatic urothelial carcinoma (as maintenance therapy after platinum-based chemotherapy), but is currently not marketed in Taiwan.
The TxGNN model predicts that it may have therapeutic efficacy for **Human Herpesvirus 8-Related Tumor** (HHV-8-related tumors, including Kaposi sarcoma and primary effusion lymphoma), however there are currently **0 clinical trials** and **0 literature reports** supporting this direction, with an evidence level of the lowest **L5 (model prediction, without actual research support)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original approved indications | No approval record in Taiwan TFDA; International approvals: Merkel cell carcinoma, locally advanced/metastatic urothelial carcinoma (maintenance therapy) |
| Predicted new indication | Human Herpesvirus 8-Related Tumor |
| TxGNN prediction score | 99.97% |
| Evidence level | L5 |
| Taiwan market status | ✗ Not marketed (TFDA) |
| Number of approval permits | 0 |
| Recommended decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, this Evidence Pack lacks formal mechanism of action (MOA) data for avelumab. Based on available information, avelumab is a fully humanized anti-PD-L1 IgG1 monoclonal antibody that blocks the interaction between PD-L1 and its receptors (PD-1 and CD80), thereby releasing immune suppression of cytotoxic T lymphocytes by tumors. Notably, the IgG1 Fc domain of avelumab retains antibody-dependent cellular cytotoxicity (ADCC), which can recruit natural killer cells to directly lyse PD-L1-positive tumor cells, distinguishing it from PD-1 inhibitors (such as nivolumab and pembrolizumab).

HHV-8 (Kaposi sarcoma-associated herpesvirus/KSHV) promotes tumor development through persistent viral infection, with related tumors including Kaposi sarcoma (KS), primary effusion lymphoma (PEL), and multicentric Castleman disease (MCD). Literature shows that HHV-8 infection can upregulate PD-L1 expression on tumor cell surfaces, providing a theoretical basis for anti-PD-L1 therapy; the ADCC mechanism of avelumab may provide additional antitumor effects against virus-transformed tumors.

However, this prediction has significant biological limitations. The primary patient populations for HHV-8-related tumors are severely immunocompromised individuals (HIV-infected patients or organ transplant recipients), whose immune microenvironment differs markedly from that of patients with approved indications for avelumab (urothelial carcinoma, Merkel cell carcinoma); PEL is a B-cell-derived malignancy in which the T-cell exhaustion model does not fully apply; moreover, using immune checkpoint inhibitors in HIV-positive patients may trigger unpredictable immune reactivation responses. In the absence of any clinical or basic research data, this prediction currently represents merely a biological hypothesis and is insufficient to support advancement to clinical development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Avelumab (Bavencio®) currently has **no TFDA approval permits** and has not been marketed for sale in Taiwan.

**International approval records (for reference):**

| Regulatory Agency | Approved Indications |
|-------------------|----------------------|
| US FDA (2017) | Unresectable or metastatic Merkel cell carcinoma (adults and children 12 years and older) |
| US FDA (2020) | First-line maintenance therapy for locally advanced or metastatic urothelial carcinoma with no progression after platinum-based chemotherapy (JAVELIN Bladder 100, Phase 3, N=700) |
| EMA (Bavencio) | Same two indications as above |

---

## Cytotoxicity

Avelumab is an antitumor immunotherapy drug and the following cytotoxicity-related information must be listed.

| Item | Content |
|------|---------|
| Cytotoxicity classification | Immunotherapy — anti-PD-L1 immune checkpoint inhibitor; not a conventional cytotoxic drug |
| Bone marrow suppression risk | Low (non-conventional bone marrow toxicity mechanism; immune-related hematologic effects [irAE] as possible exception) |
| Emetogenicity grade | Minimal (Minimal emetogenic risk, intravenous infusion formulation) |
| Monitoring items | Liver function (ALT/AST/bilirubin), thyroid function (TSH/Free T4), fasting blood glucose, CBC with differential, renal function (creatinine), adrenal function (cortisol); monitor for infusion reactions before each infusion |
| Handling precautions | Operate according to standard biologic intravenous infusion protocols; **does not require** special protective equipment for cytotoxic drugs. According to the package insert, premedication with antihistamine + acetaminophen is recommended before the first 4 infusions to prevent infusion reactions. |

---

## Safety Considerations

This Evidence Pack lacks Taiwan TFDA package insert warnings, contraindications, and drug-drug interactions data (Blocking data gap). Please consult the original avelumab US FDA approval package insert (Bavencio® US Prescribing Information) or EMA SmPC for complete safety information.

> **Special note (for HHV-8-related tumor target population):** This population (HIV-positive or organ transplant recipients) typically uses antiretroviral therapy (ART) or immunosuppressive agents concurrently, and systematic evaluation of drug-drug interactions with avelumab is lacking. The risk of immune-related adverse events (irAE), immune reconstitution inflammatory syndrome (IRIS), and infectious adverse reactions with immune checkpoint inhibitors in this population requires careful assessment and should be addressed well before any efficacy exploration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model provides a prediction score as high as 99.97%, yet this result completely lacks clinical or basic research support (L5). Although the hypothesis of PD-L1 upregulation in HHV-8 tumors is mechanistically reasonable, the unique immunosuppressed background of the target population and the B-cell origin of PEL introduce fundamental biological uncertainties regarding avelumab efficacy, falling short of the threshold for advancing clinical development.

**To proceed, the following is needed:**

- **Biomarker validation:** Quantification of PD-L1 expression in HHV-8-related tumor subtypes (KS, PEL, MCD) and characterization of the immune microenvironment (TIL composition, TMB)
- **Preclinical data:** Establish HHV-8-infected tumor models to verify anti-PD-L1 ± ADCC antitumor activity
- **MOA data completion:** Query the DrugBank API (DB11945) to obtain complete mechanism of action data for mechanistic relevance analysis
- **Safety data unlock:** Download and parse Taiwan TFDA package insert PDF to fill DG001 (Blocking data gap), enabling entry into S1 safety assessment
- **Special population safety framework:** Develop a safety assessment scheme for immune checkpoint inhibitor use in HIV-positive patients and organ transplant recipients, including review of ART drug-drug interactions
- **Model quality feedback:** The predicted indications ranked 5–8 in this Evidence Pack (ADA deficiency, Reticular dysgenesis, Immunoerythromyeloid hypoplasia, non-severe CID) all belong to immunodeficiency diseases, which are biologically contraindicated for avelumab (biological counter-indication), suggesting feedback to TxGNN training data to correct model bias

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

