---
layout: default
title: Mycophenolic Acid
parent: Model Prediction Only (L5)
nav_order: 947
evidence_level: L5
indication_count: 10
---

# Mycophenolic Acid
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

# Mycophenolic Acid: From Immunosuppressant Therapy to Hemoglobinopathy

## One-Sentence Summary

Mycophenolic acid is an oral immunosuppressant, marketed in the US as a delayed-release tablet.
The TxGNN model predicts it may be useful for **hemoglobinopathy** (sickle cell disease and thalassemia).
The evidence is **27 registered clinical trials** and **9 publications**, but these are transplant studies in which mycophenolate is a supporting part of the regimen. They do not show that it treats the disease itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 (as scored in the Evidence Pack; effectively weaker, see below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 listed entries (both under ANDA091248) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mycophenolic acid blocks IMPDH, an enzyme that lymphocytes need to make guanosine nucleotides. Without those nucleotides, T and B cells cannot proliferate, which is why the drug works as an immunosuppressant.

In hemoglobinopathies such as thalassemia and sickle cell disease, the only curative option is usually allogeneic stem cell transplantation. Mycophenolate is commonly used in these transplants to prevent graft-versus-host disease (GVHD) and to help donor cells engraft. That is the link the model appears to have found.

This is supportive immunosuppression. Mycophenolic acid does not correct the globin or red-cell defect. Most of the 27 trials are transplant regimen studies, and their titles do not show that mycophenolate is the variable being tested. The Phase 1/2 and Phase 2 data therefore suggest the drug can feasibly be used within transplant regimens. They do not show it is effective against the disease. Only 10 of the 27 trials were reviewed here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01279616](https://clinicaltrials.gov/study/NCT01279616) | Phase 2 | Terminated | 8 | Immunosuppressive and myeloablative conditioning for unrelated-donor transplant in severe sickle cell disease |
| [NCT00489281](https://clinicaltrials.gov/study/NCT00489281) | Phase 2 | Terminated | 43 | Non-myeloablative conditioning with partially HLA-mismatched or matched bone marrow in sickle cell anemia and other hemoglobinopathies |
| [NCT01810588](https://clinicaltrials.gov/study/NCT01810588) | Phase 2 | Active, not recruiting | 270 | Optimal cord blood selection for haplo-cord transplantation (mixed disease population) |
| [NCT03249831](https://clinicaltrials.gov/study/NCT03249831) | Phase 1 | Active, not recruiting | 3 | Mixed chimerism induction in sickle cell disease with non-myeloablative conditioning and haploidentical transplant |
| [NCT03171831](https://clinicaltrials.gov/study/NCT03171831) | Phase 4 | Unknown | 30 | Haploidentical stem cell transplant in thalassemia major |
| [NCT06872333](https://clinicaltrials.gov/study/NCT06872333) | Phase 2 | Recruiting | 62 | Allogeneic transplant for high-risk hemoglobinopathies and other transfusion-dependent red-cell disorders |
| [NCT02435901](https://clinicaltrials.gov/study/NCT02435901) | Phase 1/2 | Completed | 29 | Reduced-intensity conditioning plus standard immunosuppression in sickle cell and β-thalassemia major |
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Abatacept added to cyclosporine and mycophenolate mofetil as GVHD prophylaxis in children with non-malignant diseases |
| [NCT03924401](https://clinicaltrials.gov/study/NCT03924401) | Phase 2 | Active, not recruiting | 30 | Extended abatacept with tacrolimus and mycophenolate mofetil to prevent GVHD in pediatric non-malignant blood diseases |
| [NCT02678143](https://clinicaltrials.gov/study/NCT02678143) | Phase 1 | Terminated | 1 | Non-myeloablative mismatched transplant for severe sickle cell disease, with post-transplant cyclophosphamide-based GVHD prophylaxis |

Several trials were terminated with very few patients, and no trial tests mycophenolic acid against a control.

---

## Literature Evidence

No randomized controlled trials were found. The list is ordered by relevance to mycophenolate in hemoglobinopathy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Retrospective cohort | Transplant Cell Ther | Boosting immunosuppression with mycophenolate mofetil for mixed chimerism after thalassemia transplant |
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | PK / dosing study | Eur J Drug Metab Pharmacokinet | Population pharmacokinetic model and dosing recommendations for mycophenolate mofetil in children with thalassemia undergoing transplant |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Cohort | Biol Blood Marrow Transplant | Unrelated donor transplant in 4 patients with severe sickle cell disease, using post-transplant cyclophosphamide, tacrolimus and mycophenolate |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Phase I trial | Biol Blood Marrow Transplant | Unrelated cord blood transplant after reduced-intensity conditioning in sickle cell disease |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Cohort | Biol Blood Marrow Transplant | Alternative-donor transplant with post-transplant cyclophosphamide for non-malignant disorders |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Cohort | Biol Blood Marrow Transplant | Stable long-term donor engraftment in 7 patients with sickle cell disease after reduced-intensity transplant |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Cohort | Hematology | Pure red cell aplasia after major ABO-incompatible transplant (11 of 42 patients) |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case report | J Perinatol | Neonatal anemia and hydrops fetalis after maternal mycophenolate mofetil use |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA091248 | Mycophenolic Acid | Delayed-release tablet (oral) | Archis Pharma LLC |

The Evidence Pack lists this authorization twice, with identical details, so it is shown once here. The approved-indication text was not captured for this product.

---

## Safety Considerations

- **Pregnancy**: One case report links maternal mycophenolate mofetil use to neonatal anemia and hydrops fetalis ([PMID 17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/)).

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting trials are transplant regimen studies in which mycophenolate's contribution is inferred rather than tested. The drug supports transplant engraftment and GVHD prevention but does not treat hemoglobinopathy. Package insert safety data are also missing, which is a blocking gap for safety screening. The other nine predictions have no or weaker evidence. Rheumatoid arthritis has one terminated Phase 3 mycophenolate trial (NCT00451867), but the target disease and outcome are unconfirmed.

**To proceed, the following is needed:**
- The US package insert, so warnings and contraindications can be parsed for safety screening
- Confirmation of which of the 27 hemoglobinopathy trials list mycophenolate in the regimen, and whether any compare regimens with and without it
- Outcome data (engraftment, GVHD, graft failure) from the completed trials, and published results for the terminated ones
- A decision on whether the goal is a new indication or only documentation of its established supportive role in transplant, given the drug does not address the underlying disease
- Mechanism of action data confirmed from DrugBank

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

