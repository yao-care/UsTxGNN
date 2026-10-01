---
layout: default
title: Efavirenz
parent: Model Prediction Only (L5)
nav_order: 642
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Efavirenz: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) marketed for HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection in cats)**.
Support is weak: **1 in vitro biochemical/structural study** and **2 human HIV-1 trials that do not address cats**, with no feline efficacy data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the approved-indication text is blank in the US licence records; this is based on the drug's known class and use) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical/mechanism studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 (the listed licences are all generic ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Efavirenz belongs to the NNRTI class, which blocks HIV-1 reverse transcriptase (RT). Its efficacy in HIV-1 infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV. It causes an AIDS-like syndrome in cats, and no effective treatment has been established for infected cats. Inhibiting reverse transcriptase is therefore biologically plausible. A 2023 study compared NNRTIs (nevirapine, efavirenz, rilpivirine) against feline and human immunodeficiency virus enzymes to assess this potential.

Two cautions apply:
- NNRTI binding pockets differ between lentiviral RTs, so activity against HIV-1 RT does not guarantee activity against FIV RT.
- The very high TxGNN score most likely reflects efavirenz's dense anti-HIV links in the knowledge graph, not FIV-specific evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. efavirenz/emtricitabine/tenofovir (Atripla) in treatment-naive HIV-1 adults. Efavirenz was the comparator; no FIV data |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Once-daily dose selection of dolutegravir in treatment-naive HIV-1 adults, with efavirenz apparently as the comparator arm; no FIV data |

Both trials were run in HIV-1-infected humans, so they provide no direct evidence for FIV. Their Phase 2/3 labels do not raise the evidence level.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Preclinical (in vitro biochemical/structural) | Journal of Veterinary Science | Compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus enzymes to explore NNRTIs for FIV. The available abstract is truncated, so the actual results cannot be confirmed |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA204766 | Efavirenz | Film-coated tablet | Cipla USA Inc. |
| ANDA078064 | Efavirenz | Capsule | Aurobindo Pharma Limited |
| ANDA077673 | Efavirenz | Film-coated tablet | Aurobindo Pharma Limited |
| ANDA078886 | Efavirenz | Film-coated tablet | Camber Pharmaceuticals, Inc. |

Approved-indication text is blank in the source records. These are human oral products, and no veterinary product is listed. ANDA078064 appears twice in the source and is shown once.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only relevant evidence is one in vitro biochemical/structural study, and no feline in vivo efficacy or safety data exist. The two listed trials are human HIV-1 studies in which efavirenz was only a comparator. The high TxGNN score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Full text of PMID 38031646 to confirm efavirenz's actual activity against FIV reverse transcriptase versus HIV-1 reverse transcriptase
- Cell-based FIV antiviral activity data (EC50, selectivity)
- Feline pharmacokinetic and safety data, including tolerability, since the source lacks warning and contraindication information
- The FDA package insert and MOA data to close the current data gaps
- Veterinary regulatory and use-context assessment, since all listed products are for humans
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

