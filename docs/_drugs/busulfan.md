---
layout: default
title: Busulfan
parent: High Evidence (L1-L2)
nav_order: 480
evidence_level: L1
indication_count: 10
monitor_inn: "BUSULFAN"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-30
description: "Busulfan: predicted new indication Myelodysplastic syndrome (evidence level L1). Approved use: Not available in the data compiled for this report"
---

# Busulfan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

## Busulfan: From Hematologic Malignancy Transplant Conditioning to Myelodysplastic Syndrome
{: .text-alpha }

## One-Sentence Summary

Busulfan is an alkylating chemotherapy agent used as a myeloablative conditioning drug before stem cell transplantation, and it is marketed in the US as injection (Busulfex and generics) and oral tablet (Myleran).
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**,
with **39 clinical trials** and **18 publications** compiled for this prediction. The role is as a transplant-conditioning backbone, not as a stand-alone disease-modifying therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (approved indication text is blank for all licenses) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L1 |
| US Market Status | Marketed (valid licenses: 8 of 9) |
| Number of FDA Applications | 9 (valid: 8) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on established pharmacology, busulfan is an alkylating agent that cross-links DNA and is myeloablative.

In MDS, allogeneic stem cell transplantation is the only potentially curative approach, and busulfan-based regimens (Bu/Cy, Flu/Bu, Bu/Cy with additions) clear malignant marrow and create space for donor engraftment. The benefit is therefore a transplant-conditioning role rather than direct disease modification. This is consistent with a randomized phase 3 trial comparing busulfan-TBI with cyclophosphamide-TBI in advanced MDS (NCT00005866), and with several newer trials adding venetoclax or decitabine to busulfan backbones.

Toxicity (veno-occlusive disease, mucositis, seizures, long-term complications) requires guardrails such as targeted PK dosing of IV busulfan and intensity matched to age and comorbidity.

Other predictions in the list are weaker. Refractory cytopenia of childhood (pediatric MDS) and aplastic anemia rest on the same transplant-conditioning logic with limited disease-specific evidence. Unclassified MDS, HIV infection (as gene-therapy conditioning) have limited or experimental support. Del(5q), congenital sideroblastic anemia, a neurodevelopmental disorder, seborrheic keratosis and SIV infection have no supporting studies and should be held.

## Clinical Trial Evidence

The compiled data contains 39 trials for MDS. The most relevant are listed below. Many trials involve mixed AML/MDS populations and combination regimens, so busulfan's individual contribution is hard to isolate.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | Completed | 240 | Randomized busulfan-TBI vs cyclophosphamide-TBI in advanced MDS or MDS-related AML (sibling PBSC transplant) |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | Completed | 570 | Treosulfan-based vs reduced-intensity busulfan-based conditioning in AML/MDS patients ineligible for standard conditioning |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Recruiting | 324 | Venetoclax added to fractionated busulfan regimen in high-risk AML and MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | G-CSF+decitabine+BUCY vs G-CSF+decitabine+BF conditioning in high-risk MDS |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Same comparison in RAEB-1, RAEB-2 and AML secondary to MDS |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | Completed | 200 | Targeted IV busulfan plus fludarabine with allogeneic transplant in AML and MDS |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Venetoclax with timed sequential busulfan, cladribine and fludarabine conditioning in AML/MDS |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | Completed | 68 | Busulfan/fludarabine/ATG reduced-intensity transplant plus azacitidine in MDS and older AML |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | Unknown | 59 | Single-arm FLU-BU-MEL conditioning for MDS |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | Completed | 34 | Reduced-intensity busulfan/clofarabine conditioning before allogeneic transplant |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (phase 3) | Lancet Haematol | Treosulfan plus fludarabine vs reduced-intensity busulfan plus fludarabine in older AML/MDS patients (non-inferiority) |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Randomized trial, final analysis | Am J Hematol | Treosulfan improved outcomes vs reduced-intensity busulfan in older AML/MDS (n=476 at interim) |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (phase 3) | Lancet Haematol | G-CSF + decitabine + BuCy vs BuCy to reduce relapse in MDS/secondary AML |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT (phase 2) | Transplant Cell Ther | Two busulfan fractionation schedules with fludarabine and cladribine in AML/MDS |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohort | Bone Marrow Transplant | Flu/Bu4 vs Bu4/Cy myeloablative conditioning for MDS (propensity-matched registry analysis) |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Cohort | Transplant Cell Ther | Myeloablative vs reduced-intensity Flu/Bu in MDS (propensity-matched) |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic review/meta-analysis | Front Oncol | Long-term outcomes of treosulfan- vs busulfan-based conditioning in MDS/AML |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analysis | Front Oncol | Reduced-intensity vs myeloablative conditioning in AML/MDS randomized trials |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | Allogeneic transplant for myelofibrosis and MDS, the only potentially curative therapy |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Risk assessment | Pediatr Blood Cancer | Evidence-based assessment of subsequent malignancy risk after busulfan |

Note: the literature shows that treosulfan compared favorably with reduced-intensity busulfan in older patients, so busulfan is an established but not uniquely superior conditioning option.

## US Market Information

All 9 listed licenses are valid (9 of 9); the approved indication text is blank in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020954 | BUSULFEX (Otsuka) | Injection | Not available |
| NDA009386 | MYLERAN (Waylis) | Tablet, film coated | Not available |
| ANDA210148 | Busulfan (Accord) | Injection | Not available |
| ANDA210931 | Busulfan (Armas) | Injection, solution | Not available |
| ANDA212127 | Busulfan (Meitheal) | Injection, solution | Not available |

Four more ANDAs (Amneal, Sagent, Eugia, Hospira) are also listed as cancelled.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High (myeloablative at conditioning doses) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function (veno-occlusive disease risk), renal function, electrolytes, PK-targeted dosing for IV busulfan, seizure monitoring |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (model-derived, not label text): epilepsy, thrombocytopenia, neutropenia, agranulocytosis, anemia (including macrocytic and Fanconi anemia), pulmonary fibrosis, infectious and fungal disease, dermatophytosis, hyperglycemia, potassium deficiency and hyperuricemia.
- **Drug Interactions**: 100 interactions were found. Metronidazole is rated Major. Aprepitant and miconazole are rated Moderate. Levofloxacin is rated Minor. The remainder are of unknown severity, including antifungals/antibiotics (amphotericin B, vancomycin), acid suppressants (omeprazole, pantoprazole, lansoprazole, ranitidine, famotidine), corticosteroids and antiemetics.
- Seizures, veno-occlusive disease, mucositis and secondary malignancy are known conditioning-related concerns noted in the literature.

Package insert warnings and contraindications are not available in the compiled data; please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized phase 3 and phase 2/3 trials and several phase 3 publications support busulfan-based conditioning in MDS, giving L1 evidence. The benefit is as a transplant-conditioning component rather than a stand-alone therapy, treosulfan is a competitive alternative, and toxicity is substantial.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data
- Clarification of the approved indications; all 9 of 9 US licenses are valid and the drug is marketed
- Safety guardrails: PK-targeted IV busulfan dosing, conditioning intensity matched to age and comorbidity, seizure prophylaxis and VOD monitoring
- Disease-specific evidence before considering the lower-ranked predictions (refractory cytopenia of childhood and aplastic anemia may warrant follow-up; the remaining predictions should be held)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

