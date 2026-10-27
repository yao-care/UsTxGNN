---
layout: default
title: Adefovir Dipivoxil
parent: Moderate Evidence (L3-L4)
nav_order: 214
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Adefovir Dipivoxil: predicted new indication Chronic hepatitis C virus infection (evidence level L4). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "ADEFOVIR DIPIVOXIL"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hepatitis C virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection"]
---

# Adefovir Dipivoxil
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

## Adefovir Dipivoxil: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection
{: .text-alpha }

## One-Sentence Summary

Adefovir dipivoxil is an oral antiviral originally used to treat chronic hepatitis B virus infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but there are currently **0 registered clinical trials** and **10 publications** for this indication. None of the publications tests adefovir against hepatitis C, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| US Market Status | ✗ Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, adefovir dipivoxil is a prodrug of adefovir, an acyclic nucleotide analogue. Its active form inhibits the DNA polymerase/reverse transcriptase of hepatitis B virus (HBV) and terminates the growing DNA chain.

Hepatitis B and hepatitis C are both chronic viral liver diseases, so their treatments are discussed together in many reviews. The high TxGNN score probably reflects this closeness in the knowledge graph rather than a shared drug target.

The mechanistic link is weak. Hepatitis C virus (HCV) is an RNA virus that replicates through its own RNA-dependent RNA polymerase (NS5B), which is a different target from the one adefovir acts on. The literature retrieved for this prediction concerns hepatitis B or general viral hepatitis and does not show adefovir working against HCV. The prediction should therefore be treated as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below evaluates adefovir for hepatitis C. They mainly cover hepatitis B treatment or general viral hepatitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Patents on Anti-infective Drug Discovery | Pegylated interferons for chronic hepatitis B; lists adefovir dipivoxil among five approved hepatitis B drugs |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Practice & Research Clinical Gastroenterology | Treatment strategies for chronic viral hepatitis; adefovir discussed as a hepatitis B nucleoside analogue |
| [16107195](https://pubmed.ncbi.nlm.nih.gov/16107195/) | 2005 | Review | Expert Review of Anti-infective Therapy | Peginterferon-alpha2a for hepatitis B; notes that adefovir monotherapy remains unsatisfactory |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Review | Digestive Diseases | Established and emerging viral hepatitis therapies; adefovir licensed for hepatitis B, with interferon plus ribavirin used for hepatitis C |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Effects of hepatitis B and C antivirals on kidney function; adefovir is a hepatitis B nucleotide analogue |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orvosi Hetilap | Hungarian consensus guideline for hepatitis B, C and D diagnosis and treatment |
| [24797262](https://pubmed.ncbi.nlm.nih.gov/24797262/) | 2014 | Cohort | Viral Immunology | Serum cytokine profiles linked to HBeAg seroconversion after stopping nucleos(t)ide analogue therapy in hepatitis B |
| [31572002](https://pubmed.ncbi.nlm.nih.gov/31572002/) | 2019 | Cohort | Cancer Management and Research | Nucleos(t)ide analogue therapy and survival in patients with HBV-related small hepatocellular carcinoma |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Medicinal Chemistry | Bicyclol, a different drug, for chronic hepatitis B and C; not about adefovir |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202051 (cancelled) | ADEFOVIR DIPIVOXIL (Sigmapharm Laboratories, LLC) | Tablet | Not specified in the data compiled |

The only US authorization found has been cancelled, and there are no currently valid single-agent or combination authorizations.

---

## Safety Considerations

- **Kidney effects**: A knowledge-graph link flags kidney disease. This fits the published concern about adefovir nephrotoxicity (see PMID 25027705, a review of antiviral effects on kidney function).
- **Other conditions flagged in the knowledge graph (not label text)**: Lactic acidosis, fatty liver disease, non-alcoholic steatohepatitis, obesity disorder, monogenic obesity and pyoureter.
- **Drug Interactions**: 25 potential interactions are recorded, and none has a severity grade. Examples include pantoprazole, omeprazole, lansoprazole, rabeprazole, ranitidine, famotidine, morphine, warfarin, heparin, ibuprofen, kanamycin, metoclopramide, prednisolone and potassium chloride. Review the interaction details before any co-prescription.

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting literature, and the mechanism does not fit: adefovir targets the HBV DNA polymerase, while HCV replicates through an RNA polymerase. The only registered trial linked to this indication was withdrawn with zero participants. The product is also cancelled in the US market. Direct-acting antivirals are now available for HCV, so the need for adefovir in this setting is unclear.

**To proceed, the following is needed:**
- Laboratory evidence (for example, HCV replicon assays) showing whether adefovir has any anti-HCV activity
- The adefovir mechanism of action and the FDA package insert warnings and contraindications
- A kidney safety assessment, given adefovir's nephrotoxicity and the knowledge-graph kidney disease flag

**Note on other predictions for this drug:** The evidence for the HIV infection prediction is stronger than for hepatitis C, with several Phase 2 trials and a placebo-controlled study in advanced HIV. However, development was limited by dose-related nephrotoxicity at the higher doses used for HIV, and tenofovir later replaced adefovir. The hepatitis B result reflects the original approved indication and is not a repurposing opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

