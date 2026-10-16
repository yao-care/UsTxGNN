---
layout: default
title: Sebelipase Alfa
parent: Model Prediction Only (L5)
nav_order: 1146
evidence_level: L5
indication_count: 10
monitor_inn: "SEBELIPASE ALFA"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant", "cholesteryl ester storage disease", "Wolman disease with hypolipoproteinemia and acanthocytosis", "Gaucher disease", "lysosomal storage disease with skeletal involvement", "autosomal ichthyosis syndrome with fatal disease course", "Tay-Sachs disease", "benign neoplasm of adrenal gland"]
---

# Sebelipase Alfa
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

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Cholesteryl Ester Storage Disease

## One-Sentence Summary

Sebelipase alfa is a recombinant human lysosomal acid lipase, originally used as enzyme replacement therapy for Wolman disease and lysosomal acid lipase deficiency (LAL-D).
The TxGNN model's top-ranked predictions are mostly unsupported, but the best-evidenced prediction is **Cholesteryl Ester Storage Disease (CESD)**, with **8 clinical trials** and **20 publications** behind it. CESD is the later-onset form of LAL-D, so this is an on-label use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Wolman disease, lysosomal acid lipase deficiency, lysosomal lipid storage disorder (the US license record has no indication text) |
| Predicted New Indication | Scheie syndrome (TxGNN rank 1); best-supported prediction: cholesteryl ester storage disease (rank 4) |
| TxGNN Prediction Score | 99.80% (Scheie syndrome); 99.72% (cholesteryl ester storage disease) |
| Evidence Level | L5 for Scheie syndrome; L1 for cholesteryl ester storage disease |
| US Market Status | Cancelled only (1 license, cancelled) |
| Number of NDAs | 1 (BLA125561) |
| Recommended Decision | Hold for Scheie syndrome; Proceed with Guardrails for cholesteryl ester storage disease |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, sebelipase alfa is a recombinant human lysosomal acid lipase (LAL). It replaces the deficient enzyme and reduces the lysosomal accumulation of cholesteryl esters and triglycerides.

**Top-ranked prediction (Scheie syndrome, MPS I attenuated form):** The mechanistic rationale is weak. Scheie syndrome is caused by alpha-L-iduronidase deficiency, which sebelipase alfa does not supply. The high score most likely reflects network proximity among lysosomal storage diseases rather than a true biological link. No trials or literature support this use.

**Best-supported prediction (cholesteryl ester storage disease):** CESD is the later-onset, attenuated form of LAL-D, the drug's own approved indication. Enzyme replacement directly addresses the underlying defect. The same applies to rank 5, "Wolman disease with hypolipoproteinemia and acanthocytosis", which corresponds to the severe infantile form of LAL-D.

**Other predictions** (Hurler syndrome, Gaucher disease, Tay-Sachs disease, the STAT5B-related growth hormone insensitivity syndrome, ichthyosis syndrome, skeletal-involvement lysosomal storage disease, benign adrenal neoplasm) have no plausible enzyme-replacement rationale. They likely reflect graph artifacts or shared lysosomal annotation. The only linked trial for several of them is a multi-disorder prenatal enzyme replacement platform study.

---

## Clinical Trial Evidence

The table covers cholesteryl ester storage disease, the best-supported prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Phase 3 | Completed | 66 | Randomized, placebo-controlled study of sebelipase alfa 1 mg/kg every other week in late-onset LAL-D (CESD) |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Phase 2 | Completed | 31 | Open-label multicenter study of safety and efficacy in a broad LAL-D population |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Phase 2/3 | Completed | 9 | Dose-escalation study in children with growth failure due to LAL-D |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Phase 2 | Completed | 8 | Long-term extension of safety and efficacy in adults with LAL-D liver dysfunction |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Phase 1/2 | Completed | 9 | First-in-human dose escalation of safety, tolerability and PK in adults with LAL-D |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Phase 2 | Terminated | 10 | Open-label study in infants with rapidly progressive LAL-D; early termination limits interpretation |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | N/A | No longer available | N/A | US expanded access protocol (1 mg/kg every other week) until commercial product was available |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | Prenatal enzyme replacement platform study across several lysosomal storage disorders; only peripherally related |

For Hurler syndrome and Gaucher disease, the only linked trial is NCT04532047, which gives no direct evidence of sebelipase alfa efficacy in those diseases. The other predictions have no registered trials.

---

## Literature Evidence

The table covers cholesteryl ester storage disease and LAL-D.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26352813](https://pubmed.ncbi.nlm.nih.gov/26352813/) | 2015 | RCT | N Engl J Med | Phase 3 trial of sebelipase alfa in children and adults with LAL-D, an underappreciated cause of cirrhosis and severe dyslipidemia |
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | RCT | J Hepatol | Final results of the phase 3 ARISE study in children aged 4 years and older and adults |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | RCT | J Clin Lipidol | Improved atherogenic cholesterol measures through 52 weeks in the phase 3 study |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Cohort | J Pediatr Gastroenterol Nutr | Long-term efficacy and safety in a single-arm, open-label study |
| [32657505](https://pubmed.ncbi.nlm.nih.gov/32657505/) | 2020 | Cohort | Liver Int | 5-year extension: reduced transaminases and liver fat, improved lipids |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Cohort | Liver Int | Registry data showing improved aminotransferase levels with treatment versus untreated patients |
| [34906190](https://pubmed.ncbi.nlm.nih.gov/34906190/) | 2021 | Cohort | Orphanet J Rare Dis | Nationwide cohort of Wolman disease with up to 10 years of follow-up |
| [38918870](https://pubmed.ncbi.nlm.nih.gov/38918870/) | 2024 | Case series | Orphanet J Rare Dis | Twice-weekly dosing rescued severely ill infants with Wolman disease |
| [34664536](https://pubmed.ncbi.nlm.nih.gov/34664536/) | 2022 | Review | Expert Opin Drug Saf | Safety review of sebelipase alfa in LAL-D |
| [37181111](https://pubmed.ncbi.nlm.nih.gov/37181111/) | 2021 | Systematic review | Ther Adv Rare Dis | Systematic literature review of enzyme replacement therapy in LAL-D |

The literature linked to Gaucher disease concerns Wolman disease treatment, diagnostic overlap and Gaucher natural history. None shows a therapeutic effect of sebelipase alfa in Gaucher disease. The other predictions have no literature.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125561 | KANUMA (Alexion Pharmaceuticals, Inc.) | Injection, solution, concentrate | Not stated in the data compiled; license status: cancelled |

---

## Safety Considerations

Please refer to the package insert for safety information. The data compiled for this report contains no warning or contraindication text, no knowledge-graph contraindications, and no drug interaction records.

---

## Conclusion and Next Steps

**Decision: Hold for Scheie syndrome (the top-ranked prediction); Proceed with Guardrails for cholesteryl ester storage disease (on-label)**

**Rationale:**
- Scheie syndrome and the other off-label predictions have no clinical or literature support and no plausible mechanism. The high TxGNN scores likely reflect lysosomal storage disease network proximity.
- For cholesteryl ester storage disease (and the Wolman disease variant at rank 5), a completed Phase 3 randomized placebo-controlled trial plus multiple completed Phase 2 studies and long-term follow-up support efficacy and safety. This is on-label use of the drug's own indication, not repurposing.
- The only US license (BLA125561) is recorded as cancelled, which needs clarification before any market-based decision.

**To proceed, the following is needed:**
- Confirm the current US regulatory and market status of KANUMA, since the license is recorded as cancelled
- Package insert warnings, contraindications and approved indication text (currently missing and blocking safety screening)
- Detailed mechanism of action data
- Immunogenicity and infusion-reaction monitoring plan
- For any off-label prediction (for example Scheie syndrome or Hurler syndrome), preclinical or mechanistic evidence before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

