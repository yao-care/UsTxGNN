---
layout: default
title: Insulin Degludec
parent: High Evidence (L1-L2)
nav_order: 797
evidence_level: L1
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **6** 
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

# Insulin Degludec: From Type 1 Diabetes Mellitus Original Indication to "Drug Repurposing" Prediction (Type 1 Diabetes Mellitus)

## Executive Summary in One Sentence

Insulin Degludec (DB09564) is a long-acting basal insulin analogue clinically used for glycemic control in diabetic patients. The TxGNN model redirects it to **Type 1 Diabetes Mellitus**, with a prediction score of **99.44%**, supported by **50 clinical trials** and **20 publications**—however, this essentially represents the drug's "own existing indication" being re-tagged by the model rather than a traditional cross-domain drug repurposing, due to data gaps in the original indication and Taiwan regulatory information (see explanation below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Data missing: both `original_indications` and `taiwan_regulatory.licenses` are empty; Insulin Degludec is known to be a basal insulin analogue approved for glycemic control in Type 1 and Type 2 Diabetes Mellitus, but cannot be directly cited from this evidence package |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed |
| Number of Drug Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A complete mechanism of action (MOA) description is currently not available in the evidence package (marked as missing), but based on known pharmacological principles and the mechanistic associations presented in this evidence package, Insulin Degludec is a second-generation ultra-long-acting basal insulin analogue. After subcutaneous injection, it forms soluble multimers in the interstitial space that slowly and steadily decompose to release monomers into the bloodstream, with a duration of action exceeding 42 hours and lower glycemic variability compared to conventional basal insulins (e.g., glargine, detemir). Its pharmacological mechanism involves activating insulin receptors to promote glucose uptake by peripheral tissues and inhibit hepatic gluconeogenesis/hepatic glucose output.

The pathophysiological core of Type 1 Diabetes Mellitus is absolute insulin deficiency due to pancreatic β-cell destruction; therefore, exogenous basal insulin replacement therapy is inherently a standard therapeutic component for Type 1 Diabetes Mellitus, with a mechanism of action that directly corresponds without requiring cross-indication extrapolation.

It should be noted: in this evidence package, the mechanistic association analysis for `predicted_indications[0]` explicitly identifies that TxGNN development code NN1250 is Insulin Degludec, and Type 1 Diabetes Mellitus is within the scope of its approved indications; the status in this dataset where "original indication is unfilled" and "not marketed in Taiwan" likely reflects gaps in this dataset's coverage of the drug's original data fields and Taiwan drug approval comparisons, rather than the drug's true regulatory status. This point is listed as requiring supplementation in the "Data Required for Follow-Up" section below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2: randomized crossover trial comparing safety and efficacy of Insulin Degludec versus Insulin Glargine |
| [NCT01046110](https://clinicaltrials.gov/study/NCT01046110) | Phase 3 | Completed | 458 | BEGIN™: EARLY, NN1250 (degludec) vs. sitagliptin in insulin-naïve population for efficacy and safety comparison |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1392 | PRONTO-T1D: LY900014 vs. insulin lispro, both combined with insulin glargine or degludec, in adults with Type 1 Diabetes Mellitus |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | Completed | 1108 | Faster-acting insulin aspart vs. NovoRapid, both combined with insulin degludec, in adults with Type 1 Diabetes Mellitus |
| [NCT01984372](https://clinicaltrials.gov/study/NCT01984372) | N/A (Post-marketing surveillance) | Completed | 6163 | Tresiba® (degludec) long-term post-marketing safety and efficacy monitoring in diabetic patients |
| [NCT02662114](https://clinicaltrials.gov/study/NCT02662114) | N/A (Retrospective observational) | Completed | 2302 | EU-TREAT: multicenter retrospective European study of efficacy in Type 1 or Type 2 Diabetes Mellitus patients switching to Tresiba® (degludec) |
| [NCT04588259](https://clinicaltrials.gov/study/NCT04588259) | Phase 3 | Completed | 331 | Fast-acting insulin aspart vs. NovoRapid, combined with insulin degludec (±metformin) in adults with diabetes |
| [NCT03674866](https://clinicaltrials.gov/study/NCT03674866) | N/A (Retrospective observational) | Completed | 662 | CAN-TREAT: Canadian multicenter retrospective study of Tresiba® efficacy in Type 1 or Type 2 Diabetes Mellitus patients |
| [NCT03557892](https://clinicaltrials.gov/study/NCT03557892) | N/A | Completed | 28 | Randomized crossover trial of continuous subcutaneous insulin infusion (CSII) + CGM vs. multiple injections (with degludec as basal insulin) in Type 1 Diabetes Mellitus |
| [NCT06238778](https://clinicaltrials.gov/study/NCT06238778) | Phase 2 | Active, not recruiting | 227 | HDV-Insulin Lispro vs. standard Insulin Lispro, subjects combined with insulin degludec, adults with Type 1 Diabetes Mellitus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly Insulin Icodec vs. once-daily Insulin Degludec, Phase 3a trial in basal-bolus therapy for Type 1 Diabetes Mellitus |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: once-weekly Insulin Efsitora Alfa vs. once-daily Insulin Degludec, Phase 3 non-inferiority trial in adults with Type 1 Diabetes Mellitus |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: open-label non-inferiority trial of Insulin Degludec vs. Insulin Detemir (both combined with Aspart) in pregnant women with Type 1 Diabetes Mellitus |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | RCT/Review | Clinical Therapeutics | Systematic review and meta-analysis of Insulin Degludec vs. other long-acting basal insulins in Type 1 and Type 2 Diabetes Mellitus treatment |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg: randomized crossover trial of Degludec vs. Glargine U100 in Type 1 Diabetes Mellitus patients prone to nocturnal severe hypoglycemia |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX: single-center randomized controlled trial of Degludec 100 IU/mL vs. Glargine 300 IU/mL in Type 1 Diabetes Mellitus |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP: randomized crossover trial of basal insulin Degludec vs. pump-delivered Aspart in Type 1 Diabetes Mellitus |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1: randomized crossover trial of Glargine 300 U/mL vs. Degludec 100 U/mL before and after exercise in Type 1 Diabetes Mellitus |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Current review of randomized and observational trials of Insulin Degludec in Type 1 and Type 2 Diabetes Mellitus |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Review | Value Health | Systematic review and network meta-analysis of basal insulin treatment regimens in adults with Type 1 Diabetes Mellitus |

---

## US Market Information

Currently, no Taiwan drug license data is available (`taiwan_regulatory.total_licenses = 0`, `licenses` array is empty). This is marked as a high-priority data gap (DG001). It is recommended to verify market status and full approved indications from the FDA website or original product labeling.

---

## Safety Considerations

Please refer to the product labeling for safety information. (`key_warnings`, `contraindications`, drug-drug interaction information are not available, and TFDA labeling warnings/contraindications are listed as Blocking-level data gaps DG001; S1 safety preliminary evaluation cannot be completed at this time.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Type 1 Diabetes Mellitus prediction direction is supported by multiple completed Phase 3 RCTs (such as SWITCH 2, PRONTO-T1D, BEGIN: EARLY) and large post-marketing surveillance studies, achieving L1 evidence level. Mechanistically, Insulin Degludec as exogenous basal insulin directly corresponds to the absolute insulin deficiency pathophysiology of Type 1 Diabetes Mellitus with strong association. However, this case has data gaps in the drug's original indication, Taiwan market status, MOA, and product labeling safety information, which must be filled before completing a comprehensive medication safety assessment.

**To proceed, the following is needed:**
- Complete TFDA labeling warnings/contraindications data (DG001, Blocking, requires downloading and parsing the product labeling PDF)
- Complete DrugBank mechanism of action (MOA) description (DG002, High, requires querying the DrugBank API)
- Clarify and supplement `original_indications` and Taiwan drug licenses (`licenses`) data to confirm whether this is a data gap in existing indications rather than a true not-marketed status
- Drug-drug interaction (DDI) database query results

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

