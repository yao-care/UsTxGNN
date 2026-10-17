---
layout: default
title: Entecavir
parent: Moderate Evidence (L3-L4)
nav_order: 656
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Entecavir: predicted new indication Chronic hepatitis C virus infection (evidence level L4). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "ENTECAVIR"
predicted_indications: ["HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Entecavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is an oral nucleoside analogue originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may help in **chronic hepatitis C virus (HCV) infection**, but the supporting evidence is **indirect**: **2 clinical trials** and **20 publications** are linked, and none shows that entecavir treats HCV itself. The only real connection is that entecavir prevents HBV flare-ups in patients who carry both viruses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 10 authorizations (2 NDAs and 8 ANDAs), all cancelled |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, entecavir is a guanosine nucleoside analogue. Inside cells it is converted to its triphosphate form, which competes with dGTP and blocks HBV polymerase (reverse transcriptase). Its efficacy in chronic hepatitis B is well established.

HCV is a different kind of virus. It is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, and entecavir has no known direct activity against it. The high TxGNN score most likely reflects the two diseases sitting close together in the knowledge graph (both are viral hepatitis) rather than a real anti-HCV effect.

The one clinically meaningful link is co-infection. When patients with both HCV and HBV receive direct-acting antivirals (DAAs) for HCV, HBV can reactivate, and entecavir can help prevent that. In this setting entecavir protects against HBV reactivation but does not treat HCV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | DAA treatment in HCV/HBV co-infected patients, studying how often HBV reactivates. Any HCV effect comes from the DAAs, not entecavir. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Randomized, three-arm trial of nucleos(t)ide analogue prophylaxis (12 vs 24 weeks) against HBV reactivation during DAA therapy. Addresses HBV protection, not HCV treatment, and has no confirmed results. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Randomized trial | Clin Gastroenterol Hepatol | Tests entecavir to prevent HBV reactivation during DAA therapy in HCV/HBV dual infection (the available abstract excerpt does not report results). |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | 66 anti-HCV-positive chronic hepatitis B patients on nucleos(t)ide therapy, studied for HCV reactivation and viral load changes. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Observational | Dig Dis | Incidence and course of HBV reactivation in patients treated with DAAs for HCV. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Observational | J Gastroenterol Hepatol | Risk of HBV reactivation during DAA therapy in HCV patients with HBV infection. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Treatment advances for HBV/HCV co-infection, a group at high risk of cirrhosis and liver cancer. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | Therapy of chronic viral hepatitis B, C and D. Long-term nucleoside/nucleotide analogue therapy has greatly improved hepatitis B outcomes. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C (including entecavir) and their effects on kidney function. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and future prospects in chronic hepatitis B and C. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Management of hepatitis B and C in children. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Entecavir and tenofovir in hepatitis B and C patients around liver and kidney transplantation. Doses need adjusting for kidney function. |

None of these publications shows entecavir treating HCV infection. They cover HBV protection in co-infected patients and general hepatitis reviews.

---

## US Market Information

All ten US authorizations are cancelled, so no currently valid entecavir product is listed. The table shows five of them.

| Authorization Number | Product Name | Dosage Form | Status | Approved Indication |
|---------|------|------|------|-----------|
| NDA021797 | BARACLUDE | Tablet, film coated | Cancelled | Not specified in the compiled data |
| NDA021798 | BARACLUDE | Solution | Cancelled | Not specified in the compiled data |
| ANDA212126 | Entecavir | Tablet | Cancelled | Not specified in the compiled data |
| ANDA206872 | Entecavir | Tablet, film coated | Cancelled | Not specified in the compiled data |
| ANDA205740 | Entecavir | Tablet | Cancelled | Not specified in the compiled data |

---

## Safety Considerations

- **Contraindication-related conditions (from the TxGNN knowledge graph, not label text)**: impaired renal function, fatty liver disease, non-alcoholic steatohepatitis, and lactic acidosis.
- **Drug Interactions**: 44 interactions were found, and all 20 listed in detail are of moderate severity. The main ones are:
  - Acid-suppressing drugs: famotidine, ranitidine, cimetidine.
  - Metformin.
  - Amphotericin B (conventional, lipid complex, cholesteryl sulfate and liposomal forms).
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine.
  - Antibiotics: vancomycin, kanamycin, neomycin, polymyxin B, levofloxacin, amoxicillin.
  - Orlistat.

For label warnings and full safety details, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Entecavir has no known direct activity against HCV. The linked trials are small and address HBV reactivation during HCV DAA therapy, not HCV treatment, so the evidence stays at L4. The high model score likely reflects network proximity through hepatitis B. Entecavir's real value here is as an HBV safeguard in co-infection, which is already a recognized supportive use rather than a new indication.

**To proceed, the following is needed:**
- Mechanism-of-action data and any in vitro evidence of anti-HCV activity (none is currently available).
- Full results of the entecavir HBV-reactivation prophylaxis randomized trial in HCV/HBV co-infection (PMID 34864158).
- Label warnings and contraindications from the FDA package insert.
- Confirmation of product availability, since all US authorizations are cancelled.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

