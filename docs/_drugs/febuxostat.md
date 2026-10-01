---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 693
evidence_level: L4
indication_count: 3
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Febuxostat: From Hyperuricemia and Gout to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor that lowers serum urate. The US license records in this package carry no indication text, so its original use of hyperuricemia and gout is inferred from the mechanism rather than read from a label.
The TxGNN model predicts it for **renal hypouricemia**, a condition in which serum urate is already too low, but only **1 clinical trial of doubtful relevance** and **2 publications** support this direction.
The high score is most likely an artifact of the shared urate-metabolism neighborhood in the knowledge graph, not evidence of therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (inferred: hyperuricemia and gout) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (all listed records are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Febuxostat is known to inhibit xanthine oxidoreductase, the enzyme that makes uric acid, and to lower serum urate.

Renal hypouricemia is usually caused by loss-of-function variants in the urate transporters URAT1 (SLC22A12) or GLUT9 (SLC2A9). These variants make the kidney waste urate into the urine, so serum urate is low. Lowering urate further, as febuxostat does, looks counterintuitive.

The only plausible rationale comes from a 2023 report on exercise-induced acute kidney injury (EIAKI) in renal hypouricemia. It suggests that cutting urate production might reduce the urinary urate load and the crystal or oxidative stress during strenuous exercise. This is a hypothesis with no supporting clinical data here, and pushing serum urate below an already low baseline could add risk.

The 99.99% score should therefore not be read as therapeutic support. It probably reflects the drug and disease sharing the same urate-metabolism neighborhood in the graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with calculi and hyperuricemia. The registry title is only a department name. The condition and intervention cannot be confirmed as febuxostat in renal hypouricemia, so this is not direct evidence (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report / hypothesis | Internal Medicine (Tokyo) | A 16-year-old football player with familial renal hypouricemia (compound heterozygous URAT1 mutations) had recurrent EIAKI despite hydration. Febuxostat was tried as prophylaxis, and the authors propose non-purine XOR inhibitors for preventing EIAKI. The abstract in the package is truncated, so the outcome is not confirmed. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrative review | Clinical Rheumatology | Background review of hypouricemia (serum urate < 2 mg/dL) covering causes and clinical considerations. It is not specific to febuxostat. |

---

## US Market Information

The package lists 20 authorizations in total, and the 5 below are the ones supplied. None includes approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA205443 | febuxostat | Tablet | Zydus Lifesciences Limited |
| ANDA205467 | Febuxostat | Tablet, film coated | Sun Pharmaceutical Industries, Inc. |
| ANDA210461 | Febuxostat | Tablet, film coated | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA205467 | Febuxostat | Tablet, film coated | NorthStar RxLLC |
| ANDA205467 | Febuxostat | Tablet, film coated | NorthStar RxLLC |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The direction of effect is counterintuitive: the drug lowers urate in a condition where urate is already low. The evidence is a single case-level report, and the only listed trial is of unconfirmed relevance. Lowering urate further could cause harm. The evidence level is L4.

Two other predictions in the same package have a more coherent mechanism, though still with only case-level evidence. Partial HPRT deficiency (score 99.98%) and Lesch-Nyhan syndrome (score 99.68%) both involve urate overproduction, where febuxostat could control the hyperuricemia. Both are marked "Research Question" and need attention to xanthine and hypoxanthine accumulation, particularly in children.

**To proceed, the following is needed:**
- Check the NCT04398251 registry record for its condition, intervention and arms.
- Obtain the full text of PMID 36754409 to confirm the febuxostat outcome and safety findings.
- Obtain the package insert warnings and contraindications (a blocking gap for safety screening).
- Obtain detailed mechanism of action data from DrugBank.
- Prepare a risk assessment of further lowering serum urate below baseline in renal hypouricemia, including renal and urinary tract outcomes.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

