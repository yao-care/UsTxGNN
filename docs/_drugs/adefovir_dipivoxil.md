---
layout: default
title: Adefovir Dipivoxil
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Adefovir dipivoxil is an oral nucleotide analog antiviral, established for chronic hepatitis B.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but **0 of the 10 retrieved clinical trials and 0 of the retrieved publications test adefovir in HCV**. All are HBV studies or general viral hepatitis reviews, so the prediction is best viewed as a graph-embedding artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license record. Other records in the pack describe chronic hepatitis B as the established marketed use |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (no HCV-specific study; only HBV-related and mechanism-adjacent material) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (ANDA202051) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Adefovir is known as an acyclic nucleotide analog. Its active diphosphate metabolite inhibits DNA polymerase and reverse transcriptase and terminates the viral DNA chain. This underlies its activity against HBV, including lamivudine-resistant strains.

HBV and HCV are both hepatotropic viruses that cause chronic viral hepatitis, and they sit close together in the knowledge graph. That proximity most likely explains the very high score. Mechanistically, however, HCV is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, so there is no plausible direct target for adefovir.

The retrieved evidence agrees with this. The trials are HBV, HIV/HBV or interferon-based studies, and the literature covers HBV or general viral hepatitis. Nothing shows adefovir efficacy against HCV.

---

## Clinical Trial Evidence

None of these trials evaluates adefovir for HCV. They were retrieved through HBV or "chronic hepatitis" keyword matching.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00973219](https://clinicaltrials.gov/study/NCT00973219) | Not applicable | Completed | 151 | Peg-interferon plus adefovir or tenofovir vs no treatment in HBeAg-negative chronic hepatitis B with low viral load; no HCV endpoint |
| [NCT02560649](https://clinicaltrials.gov/study/NCT02560649) | Phase 4 | Unknown | 324 | Response-guided add-on of PEG-IFN in nucleoside-analog-treated HBeAg-positive hepatitis B patients |
| [NCT00013702](https://clinicaltrials.gov/study/NCT00013702) | Phase 2 | Completed | 30 | Adefovir added to lamivudine for HBV in HIV-infected patients with decompensated liver disease; not an HCV study |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Interferon alpha-2b plus ribavirin pilot in chronic hepatitis B; adefovir not tested |
| [NCT00371761](https://clinicaltrials.gov/study/NCT00371761) | Phase 3 | Completed | 25 | PegIntron vs adefovir 10 mg in HBeAg-positive hepatitis B in Taiwan |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys plus entecavir vs entecavir vs Pegasys in HBeAg-negative hepatitis B |
| [NCT00645294](https://clinicaltrials.gov/study/NCT00645294) | Phase 1/2 | Completed | 47 | Single-dose pharmacokinetics and safety of adefovir in children and adolescents with hepatitis B |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | Completed | 104 | Antiviral effect of adefovir over 12 and 52 weeks in Korean hepatitis B patients |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | Unknown | 600 | Early vs conventional antiviral treatment and 10-year prognosis in chronic HBV |
| [NCT00051077](https://clinicaltrials.gov/study/NCT00051077) | Phase 2 | Withdrawn | 0 | Adefovir, peginterferon and ribavirin in HBV/HCV/HIV triple infection; withdrawn with no participants and no data |

---

## Literature Evidence

None of these publications reports adefovir efficacy against HCV.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their kidney effects; adefovir is listed as an HBV nucleotide analog |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment of chronic hepatitis B and C; peginterferon is preferred for HBV |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Med Chem | Bicyclol as a novel drug for chronic hepatitis B and C; does not involve adefovir |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Review | Dig Dis | Established and emerging therapies for viral hepatitis; adefovir is licensed for HBV, while HCV is treated with interferon plus ribavirin |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | Treatment strategies for chronic viral hepatitis; adefovir listed among HBV nucleoside analogs |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orv Hetil | Hungarian consensus guideline on hepatitis B, C and D diagnosis and treatment |
| [16880074](https://pubmed.ncbi.nlm.nih.gov/16880074/) | 2006 | Review | Gastroenterol Clin North Am | Treatment pathway in hepatitis B |
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Pat Anti-Infect Drug Discov | Pegylated interferons for chronic hepatitis B; adefovir is one of five approved HBV drugs |
| [16107195](https://pubmed.ncbi.nlm.nih.gov/16107195/) | 2005 | Review | Expert Rev Anti Infect Ther | Peginterferon alpha-2a for hepatitis B; adefovir monotherapy described as unsatisfactory |
| [31572002](https://pubmed.ncbi.nlm.nih.gov/31572002/) | 2019 | Retrospective study | Cancer Manag Res | Nucleos(t)ide analog therapy and survival in HBV-related small hepatocellular carcinoma |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202051 | ADEFOVIR DIPIVOXIL (Sigmapharm Laboratories, LLC) | Tablet (oral) | Not stated in the license record |

---

## Safety Considerations

Package-insert warnings, contraindications and drug-interaction data are not available in the record. Please refer to the package insert for safety information.

Other material in the pack points to these risks:
- **Nephrotoxicity**: renal function monitoring is needed. Adefovir-induced Fanconi syndrome with hypophosphatemic osteomalacia has been reported (PMID 32289307).
- **Resistance mutations**: rtN236T and rtA181V/T are associated with adefovir resistance in HBV.
- **Withdrawal risk**: lactic acidosis or hepatitis flare after stopping treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by any HCV-specific clinical or mechanistic evidence, and there is no plausible adefovir target in HCV. Approved direct-acting antivirals already treat HCV well, so a repurposing case for adefovir is unlikely.

**To proceed, the following is needed:**
- HCV-specific in vitro or clinical data showing adefovir activity, which does not currently exist in the pack
- Package-insert warnings, contraindications and approved-indication text
- Mechanism-of-action data from DrugBank
- A renal safety monitoring plan, since nephrotoxicity is a known risk

**Related predictions in the pack:** HIV infection is the best-supported alternative (L2), with randomized placebo-controlled trials showing antiviral activity. However, the HIV-dose regimen caused dose-limiting nephrotoxicity and was not approved. The hepatitis B prediction (L1) is a confirmation of the established use rather than new repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

