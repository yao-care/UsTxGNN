---
layout: default
title: Dronabinol
parent: Model Prediction Only (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Dronabinol
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

# Dronabinol: From Its Approved Cannabinoid Uses to Migraine Disorder

## One-Sentence Summary

Dronabinol is synthetic delta-9-tetrahydrocannabinol (THC), a cannabinoid marketed in the US as oral capsules.
The TxGNN model predicts it may be effective for **migraine disorder**, with **7 related clinical trials** and **14 publications** currently touching this direction.
Most of that evidence concerns inhaled cannabis or CBD/THC mixtures rather than dronabinol itself, so support for dronabinol specifically is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the source data (approved indication text is empty for all licenses); confirm against the current label |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 (one completed Phase 2 RCT, but of inhaled cannabis, not dronabinol) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations on record |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source data. Dronabinol is known to be a partial agonist of the CB1 and CB2 cannabinoid receptors. Endocannabinoid signalling modulates trigeminovascular pain transmission and CGRP release, both central to migraine biology.

Mouse and rat studies support this link. THC alone, or combined with CBD, reduced migraine-like behaviours triggered by CGRP, and THC showed anti-migraine effects in the female rat (PMIDs 39988876, 41182862, 29111112). In humans, a 2026 randomized crossover trial of vaporized cannabis in acute migraine (PMID 41469488) was completed, and its registry record (NCT04360044) enrolled 92 participants.

There are important caveats:
- The clinical signal comes from inhaled cannabis (THC/CBD mixtures), not isolated oral dronabinol.
- The dosage form and pharmacokinetics differ from those of oral capsules.
- Preclinical work in medication-overuse headache (PMID 31311288) suggests chronic cannabinoid exposure may cause latent sensitization. This is a safety concern for repeated use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04360044](https://clinicaltrials.gov/study/NCT04360044) | Phase 2 | Completed | 92 | Randomized, double-blind, placebo-controlled crossover of vaporized cannabis (THC, THC/CBD, CBD) for acute migraine; matches the 2026 publication (PMID 41469488). Product is cannabis, not dronabinol |
| [NCT00123201](https://clinicaltrials.gov/study/NCT00123201) | Phase 2 | Completed | Not reported | Placebo-controlled study of dronabinol MDI (metered-dose inhaler) for acute migraine. The title names dronabinol, making it the only trial directly on the drug, though the pack graded it low; results are not in the pack and should be retrieved |
| [NCT04989413](https://clinicaltrials.gov/study/NCT04989413) | Phase 2/3 | Terminated | 110 | CBD + CBG + low-dose THC (4 mg/day) as adjunct in chronic migraine. Weak support, and the reason for termination should be checked |
| [NCT05427630](https://clinicaltrials.gov/study/NCT05427630) | Phase 2 | Suspended | 20 | Pilot, dose-ranging crossover of inhaled cannabis (2.5%, 5%, 10%) vs placebo for acute migraine |
| [NCT05337033](https://clinicaltrials.gov/study/NCT05337033) | Phase 2 | Recruiting | 20 | Open-label tolerability study of CBD-enriched cannabis extract in adolescents with chronic headache; tolerability data only |
| [NCT04091789](https://clinicaltrials.gov/study/NCT04091789) | Phase 2 | Unknown | 30 | Sublingual cannabinoid combination tablets in dysmenorrhea and associated pain; mechanistically relevant only |
| [NCT07146945](https://clinicaltrials.gov/study/NCT07146945) | Phase 1 | Not yet recruiting | 84 | Safety, tolerability and PK of oral CBD/THC liquid (S1-221) in healthy adults; could inform future safety data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41469488](https://pubmed.ncbi.nlm.nih.gov/41469488/) | 2026 | RCT | Headache | Vaporized cannabis vs placebo for acute migraine in a double-blind crossover design (abstract states the aim only) |
| [31715263](https://pubmed.ncbi.nlm.nih.gov/31715263/) | 2020 | Cohort | J Pain | Archival app data on inhaled cannabis and headache/migraine ratings; examined effects of THC, CBD, dose and tolerance |
| [32758396](https://pubmed.ncbi.nlm.nih.gov/32758396/) | 2020 | Cohort | J Integr Med | Real-time naturalistic use of cannabis flower for headache and migraine relief |
| [29797104](https://pubmed.ncbi.nlm.nih.gov/29797104/) | 2018 | Cohort | J Headache Pain | Medicinal cannabis use patterns, strains and medication substitution in migraine, headache, arthritis and chronic pain |
| [34370866](https://pubmed.ncbi.nlm.nih.gov/34370866/) | 2021 | Case-referent | Headache | Examined whether cannabis use predicts medication-overuse headache in chronic migraine |
| [39988876](https://pubmed.ncbi.nlm.nih.gov/39988876/) | 2025 | Preclinical | Cephalalgia | CBD plus THC alleviated migraine-like behaviours in three mouse models (CGRP, SNP, cortical spreading depolarization) |
| [41182862](https://pubmed.ncbi.nlm.nih.gov/41182862/) | 2025 | Preclinical | Cephalalgia | CBD:THC 100:1 rescued migraine-like symptoms caused by central CGRP in mice |
| [29111112](https://pubmed.ncbi.nlm.nih.gov/29111112/) | 2018 | Preclinical | Eur J Pharmacol | THC produced anti-migraine effects in a female rat dural-stimulation model |
| [29462111](https://pubmed.ncbi.nlm.nih.gov/29462111/) | 2018 | Preclinical | Behav Pharmacol | Repeated morphine, but not THC, caused medication-overuse headache in female rats |
| [31311288](https://pubmed.ncbi.nlm.nih.gov/31311288/) | 2020 | Preclinical | Cephalalgia | Cannabinoid receptor agonists induced latent sensitization in a medication-overuse headache model |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA018651 | Dronabinol (Major Pharmaceuticals) | Capsule | Not captured in source data |
| NDA018651 | MARINOL (ThePharmaNetwork, LLC) | Capsule | Not captured in source data |
| ANDA078292 | Dronabinol (Rhodes Pharmaceuticals L.P.) | Capsule | Not captured in source data |

The record also lists an oral solution form. In total, 20 authorizations are on file; only the main ones are shown.

---

## Safety Considerations

- **Literature-derived signal**: Preclinical work suggests chronic cannabinoid exposure may induce latent sensitization in a medication-overuse headache model (PMID 31311288). A human case-referent study examined the link between cannabis use and medication-overuse headache in chronic migraine (PMID 34370866). This matters because migraine treatment often involves repeated dosing.

Please refer to the package insert for warnings, contraindications and drug interactions. No drug-interaction records were found in the source data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible and one completed Phase 2 RCT exists in migraine. However, that trial tested inhaled cannabis rather than dronabinol, and the label safety data needed for screening is missing. Hold, rather than Go, is warranted until the evidence is tied to dronabinol itself.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed original approved indications and mechanism-of-action data
- Results of the dronabinol MDI migraine trial (NCT00123201), and the reason NCT04989413 was terminated
- The full results of the 2026 cannabis RCT (PMID 41469488) and an assessment of whether they translate to oral dronabinol
- A plan to address medication-overuse and latent sensitization risk with repeated use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

