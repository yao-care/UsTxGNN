---
layout: default
title: Eteplirsen
parent: Model Prediction Only (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
---

# Eteplirsen
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

# Eteplirsen: From Approved Use in Exon 51-Amenable DMD to Duchenne and Becker Muscular Dystrophy

## One-Sentence Summary

Eteplirsen (Exondys 51) is an exon 51-skipping antisense drug already marketed in the US for Duchenne muscular dystrophy (DMD) with exon 51-amenable mutations. The TxGNN model predicts it for **Duchenne and Becker muscular dystrophy**, and **11 clinical trials** and **19 publications** cover this direction. The prediction mostly re-confirms the marketed use rather than finding a new one, and evidence for Becker muscular dystrophy specifically is absent.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Duchenne and Becker muscular dystrophy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 unique NDA (NDA206488; the data lists it twice) |
| Recommended Decision | Proceed with Guardrails |

The label indication text is blank in the source data. The original use is taken from the mechanism rationale in the Evidence Pack (exon 51-amenable DMD).

**Evidence level note:** The pack labels this L1, but under the stated rules L1 needs at least 2 completed Phase 3 RCTs. Only one Phase 3 trial is completed (NCT02255552, open-label with an untreated control arm, not randomized). The second (NCT03992430) is still active. A completed randomized Phase 2 trial (NCT01396239) exists, so L2 is the defensible level.

## Why is This Prediction Reasonable?

Eteplirsen is a phosphorodiamidate morpholino oligomer. It causes exon 51 of the DMD gene to be skipped, which restores the reading frame and lets the body make a shortened but partly functional dystrophin. Detailed mechanism data is not available in DrugBank for this pack, but this description comes from the pack's rationale.

The benefit is genotype-specific. It applies to DMD deletions amenable to exon 51 skipping (about 13% of DMD patients). It is not expected to help other DMD genotypes. For Becker muscular dystrophy, which the prediction label also names, no dedicated evidence was found.

The literature also says the clinical value of the dystrophin increase is still debated, and the FDA approval was accelerated and controversial. Any further development should treat dystrophin expression as confirmatory and rely on functional endpoints.

The other nine predicted indications (ranks 2–10) are all rated L5 / Hold. They include Bethlem myopathy, several Emery-Dreifuss forms, DNAJB6 limb-girdle dystrophy, nebulin-related distal myopathy, POMK-related limb-girdle dystrophy and others. They have different genetic causes, no plausible exon 51 mechanism, and no trials or literature. Their high scores likely reflect knowledge-graph proximity among muscle-disease nodes.

## Clinical Trial Evidence

The pack lists 11 trials. The 10 most relevant are shown; the omitted one (NCT00159250) is an early Phase 1/2 study with 7 patients.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01396239](https://clinicaltrials.gov/study/NCT01396239) | Phase 2 | Completed | 12 | Randomized, double-blind, placebo-controlled study of 30 and 50 mg/kg over 24 weeks in ambulant DMD |
| [NCT03992430](https://clinicaltrials.gov/study/NCT03992430) | Phase 3 | Active, not recruiting | 160 | Randomized, double-blind comparison of 100 and 200 mg/kg vs 30 mg/kg in exon 51-amenable DMD |
| [NCT02255552](https://clinicaltrials.gov/study/NCT02255552) | Phase 3 | Completed | 109 | PROMOVI: open-label with concurrent untreated control arm; efficacy and safety up to 96 weeks |
| [NCT00844597](https://clinicaltrials.gov/study/NCT00844597) | Phase 1/2 | Completed | 19 | First-in-patient safety study of IV eteplirsen in exon 51-amenable DMD |
| [NCT01540409](https://clinicaltrials.gov/study/NCT01540409) | Phase 2 | Completed | 12 | Open-label extension, 212 additional weeks of efficacy and safety |
| [NCT02286947](https://clinicaltrials.gov/study/NCT02286947) | Phase 2 | Completed | 24 | Open-label safety and tolerability in advanced-stage DMD |
| [NCT02420379](https://clinicaltrials.gov/study/NCT02420379) | Phase 2 | Completed | 33 | Open-label safety and efficacy in early-stage DMD |
| [NCT03218995](https://clinicaltrials.gov/study/NCT03218995) | Phase 2 | Completed | 15 | Open-label safety and PK in boys aged 6–48 months |
| [NCT04179409](https://clinicaltrials.gov/study/NCT04179409) | Phase 2 | Completed | 3 | 48-week open-label study of exon-skipping products in patients with single-exon duplications; very small |
| [NCT06606340](https://clinicaltrials.gov/study/NCT06606340) | N/A | Enrolling by invitation | 300 | Long-term observational study of routine clinical use; no results yet |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23907995](https://pubmed.ncbi.nlm.nih.gov/23907995/) | 2013 | Double-blind placebo-controlled trial (pack tags it "Review") | Ann Neurol | Tested dystrophin production and 6-minute walk distance with eteplirsen |
| [34120909](https://pubmed.ncbi.nlm.nih.gov/34120909/) | 2021 | Open-label Phase 3 trial | J Neuromuscul Dis | PROMOVI: 30 mg/kg/week IV for 96 weeks in ambulatory patients aged 7–16 |
| [40831143](https://pubmed.ncbi.nlm.nih.gov/40831143/) | 2026 | Cohort (propensity-matched) | J Neuromuscul Dis | Compared LVEF decline in eteplirsen-treated patients vs natural-history controls |
| [38482981](https://pubmed.ncbi.nlm.nih.gov/38482981/) | 2024 | Cohort | Muscle Nerve | Overall survival with up to 8 years of eteplirsen vs natural-history controls |
| [29254734](https://pubmed.ncbi.nlm.nih.gov/29254734/) | 2018 | Pooled analysis | J Clin Neurosci | Pooled analysis of eteplirsen in paediatric DMD |
| [37207382](https://pubmed.ncbi.nlm.nih.gov/37207382/) | 2023 | Open-label trial | Neuromuscul Disord | Safety, tolerability and PK in boys aged 6–48 months (NCT03218995) |
| [29752304](https://pubmed.ncbi.nlm.nih.gov/29752304/) | 2018 | Review | Neurology | Quantification of novel dystrophin after long-term eteplirsen |
| [40308063](https://pubmed.ncbi.nlm.nih.gov/40308063/) | 2025 | Review | Mol Ther | Exon-skipping ASOs in neuromuscular disease; broad safety profile, but limited exon-skipping efficacy and dystrophin production |
| [28280301](https://pubmed.ncbi.nlm.nih.gov/28280301/) | 2017 | Review | Drug Des Devel Ther | Overview of eteplirsen following its 2016 accelerated FDA approval |
| [29752302](https://pubmed.ncbi.nlm.nih.gov/29752302/) | 2018 | Commentary | Neurology | Commentary on eteplirsen and dystrophin as an outcome |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA206488 | Exondys 51 | Injection | Sarepta Therapeutics, Inc. |

The approved indication text is blank in the source data, and the duplicate record has been merged. The only route is injectable (IV infusion in the trials).

## Safety Considerations

Please refer to the package insert for safety information. Warnings and contraindications are missing from the data, and no drug-interaction records were found. The trial and literature entries above include safety and tolerability studies, including young boys aged 6–48 months, but they do not replace label review.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For exon 51-amenable DMD, the evidence includes a randomized Phase 2 trial, a completed Phase 3 trial with a control arm, and a marketed product. The high score for "Duchenne and Becker" should not be extended to Becker muscular dystrophy or other DMD genotypes, and the clinical meaning of the dystrophin increase is still debated.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap, DG001)
- Results of the Phase 3 high-dose trial NCT03992430 (completion expected 2026-10)
- Dedicated evidence if Becker muscular dystrophy is to be pursued
- Genotype restriction to exon 51-amenable deletions, with functional endpoints as primary and dystrophin expression as confirmatory
- Mechanism of action data from DrugBank (DG002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

