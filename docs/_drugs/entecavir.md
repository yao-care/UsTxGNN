---
layout: default
title: Entecavir
parent: Model Prediction Only (L5)
nav_order: 656
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analog antiviral used to treat chronic hepatitis B (HBV). The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection** with a very high score (99.98%). However, the retrieved trials and publications are almost entirely about HBV or HBV/HCV co-infection, so **no study shows entecavir working against HCV**, and the score most likely reflects graph proximity to HBV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B (inferred from the evidence pack's rationale; the US label text is empty in the input) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (the pack lists L4, but it contains no HCV-specific preclinical or mechanistic study, so L5 is the fit) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Entecavir is a guanosine nucleoside analog. Its active triphosphate form competes with dGTP and inhibits HBV polymerase, blocking priming, reverse transcription and DNA synthesis. Detailed mechanism-of-action data is not available in the DrugBank field, so this is taken from the evidence pack's rationale.

HBV and HCV are both hepatotropic viruses that cause chronic liver disease, which is probably why the knowledge graph places them close together. Mechanistically, though, they differ. HCV is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, and nothing in the provided data supports entecavir activity against it. HCV is now treated with direct-acting antivirals.

The trials and papers found are mainly HBV studies or HBV/HCV co-infection reports, where entecavir treats the HBV component. The prediction is therefore weak from a mechanistic standpoint.

---

## Clinical Trial Evidence

No listed trial tests entecavir as a treatment for HCV. The trials below are the most relevant, and all are HBV or co-infection studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Tests whether prophylactic nucleos(t)ide analogue during DAA therapy (12 vs 24 weeks) prevents HBV reactivation in HCV/HBV co-infected patients |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studies HBV reactivation during direct-acting antiviral treatment of HCV/HBV co-infection |
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | QL-007 plus entecavir or tenofovir in chronic hepatitis B; entecavir covers HBV only |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys plus entecavir vs entecavir alone in HBeAg-positive chronic hepatitis B |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Phase 3 | Unknown | 120 | Tenofovir vs lamivudine in severe HBV acute exacerbation; does not involve entecavir for HCV |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Entecavir vs adefovir viral kinetics in nucleoside-naive HBV |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Japanese dose-response study of entecavir vs lamivudine in HBV |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Entecavir for HBV in HCC patients after radiofrequency ablation; HCV is mentioned only as background |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Arabinoxylan rice bran in HCC and hepatitis B/C; not an entecavir study |
| [NCT01179594](https://clinicaltrials.gov/study/NCT01179594) | Phase 4 | Withdrawn | 0 | Pegasys with or without entecavir in HBeAg-negative CHB; withdrawn |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | 66 anti-HCV-positive CHB patients on nucleos(t)ide therapy, studied for HCV reactivation and viral load evolution |
| [36873880](https://pubmed.ncbi.nlm.nih.gov/36873880/) | 2023 | Case report | Front Med | Unusual viral evolution after antiviral therapy in a patient with concurrent HBV and HCV |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Treatment advances in HBV/HCV coinfection |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clin Res Hepatol Gastroenterol | HBV/HCV co-infection as a therapeutic challenge, with a case report |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and prospects for chronic hepatitis B and C |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Not classified | J Gastroenterol Hepatol | Risk of HBV reactivation when treating chronic hepatitis C with direct-acting antivirals |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Not classified | Minerva Gastroenterol Dietol | Antivirals for hepatitis B and C and their effects on kidney function |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Not classified | Chin Clin Oncol | Timing and management of hepatitis B and C in HCC patients |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Not classified | Clin Res Hepatol Gastroenterol | Management of viral hepatitis B and C in children |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Not classified | World J Gastroenterol | HBV infection and alcohol consumption in relation to HCC |

None of these reports entecavir efficacy against HCV.

---

## US Market Information

The evidence pack lists 20 US authorizations in total (5 shown below). Approved-indication text is empty in the input and is omitted here.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA212126 | Entecavir | Tablet | Epic Pharma, LLC |
| ANDA206872 | Entecavir | Tablet, film coated | NorthStar Rx LLC |
| ANDA205740 | Entecavir | Tablet | Camber Pharmaceuticals, Inc. |
| ANDA206652 | Entecavir | Tablet, film coated | AvKARE |
| ANDA206652 | Entecavir | Tablet, film coated | Amneal Pharmaceuticals LLC |

---

## Safety Considerations

Please refer to the package insert for safety information. The pack has no warnings or contraindications, and its drug-interaction query found no results.

The pack's rationale notes these points for entecavir use in HBV. They matter if HCV/HBV co-infected patients are ever considered:
- Renal dose adjustment is needed.
- Lactic acidosis and hepatomegaly are warnings.
- Severe hepatitis exacerbation can occur on discontinuation.
- Resistance is a concern in lamivudine-experienced patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any HCV-specific evidence. All retrieved trials and literature concern HBV or co-infection, where entecavir treats HBV only. There is also no plausible mechanism against the HCV NS5B polymerase, and HCV already has effective direct-acting antivirals.

**To proceed, the following is needed:**
- A package insert review (the pack flags this as a blocking gap, so the candidate cannot pass safety screening without it)
- In vitro evidence of entecavir activity against HCV replication, such as replicon assays
- Confirmation that the signal is not just HBV/HCV co-infection (in which case the value is HBV coverage, e.g. reactivation prophylaxis during DAA therapy, rather than HCV treatment)
- Attention to the pack's other predictions: hepatitis B virus infection (rank 2) is the drug's existing indication rather than repurposing, and the HIV prediction carries an M184V resistance concern

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

