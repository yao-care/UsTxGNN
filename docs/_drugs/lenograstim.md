---
layout: default
title: Lenograstim
parent: Model Prediction Only (L5)
nav_order: 845
evidence_level: L5
indication_count: 4
---

# Lenograstim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Lenograstim: From G-CSF Therapy to Primary Release Disorder of Platelets

## One-Sentence Summary

Lenograstim is a recombinant human granulocyte colony-stimulating factor (G-CSF) that acts on the neutrophil lineage and mobilizes hematopoietic stem cells.
The TxGNN model predicts it may be relevant to **primary release disorder of platelets**, but the supporting evidence is very weak.
The **13 matched clinical trials** are stem cell transplant, GVHD or unrelated trials that do not test lenograstim for this condition, and there are **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only; the pack lists L4, but no matched study tests lenograstim for this indication) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lenograstim is recombinant human G-CSF. It stimulates neutrophil production and mobilizes hematopoietic stem cells. Detailed mechanism of action data is not available in the source record, and the approved indication text is also blank.

A platelet release disorder is a defect in platelet granule release and function. G-CSF has no established action on this pathway. The very high TxGNN score is a graph-based association, most likely driven by shared hematologic and transplant-related neighbors in the knowledge graph. It is not evidence of a mechanistic link.

The other three predictions are weaker still. No supporting mechanism, trials or literature were found for any of them.

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Glanzmann thrombasthenia | 99.89% | L5 | Inherited defect of platelet integrin αIIbβ3, which G-CSF does not correct |
| Pseudo-von Willebrand disease | 99.88% | L5 | Gain-of-function GPIbα variants, a pathway G-CSF does not act on |
| Severe nonproliferative diabetic retinopathy | 99.61% | L5 | Only a speculative link through endothelial progenitor mobilization, and neovascularization could be a safety concern |

---

## Clinical Trial Evidence

Thirteen trials were matched to this prediction and 10 are listed below. All 10 were graded C (low relevance). None shows that lenograstim was the intervention, and none addresses a platelet release disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated-donor stem cell transplant for hematologic malignancies |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Autologous stem cell transplant vs best available therapy in relapsing multiple sclerosis |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Post-transplant cyclophosphamide GVHD prophylaxis platform |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic transplant with busulfan, fludarabine and irradiation |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Banked HLA-mismatched donor marrow with post-transplant cyclophosphamide; no data |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir for CMV reactivation in acute lung injury (antiviral trial) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic stem cell transplant in pediatric sarcomas |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Oral dapansutrile for moderate COVID-19 with early cytokine release syndrome |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Dose-finding for post-transplant cyclophosphamide in GVHD prophylaxis |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion with autologous stem cell transplant in severe lupus |

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761134 | RYZNEUTA (Acrotech Biopharma Inc) | Injection | Not specified in the data |
| Not available | GUNA-GCSF (Guna spa) | Solution/drops | Not specified in the data |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a graph-based association only. There is no plausible mechanism linking G-CSF to platelet release disorders, and none of the matched trials tests lenograstim for this condition. There is no literature. The 13 matched trials are stem cell transplant, GVHD or unrelated trials.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the US licenses
- Direct preclinical or clinical evidence that G-CSF affects platelet granule release or function
- Review of the 3 matched trials that were not graded

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

