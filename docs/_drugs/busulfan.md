---
layout: default
title: Busulfan
parent: High Evidence (L1-L2)
nav_order: 480
evidence_level: L1
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Busulfan: From Transplant Conditioning Chemotherapy to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is an alkylating chemotherapy drug used to clear bone marrow before allogeneic stem cell transplantation, and the approved-indication text is empty in the supplied US license records.
The TxGNN model predicts it may be useful for **myelodysplastic syndrome (MDS)**, as a conditioning component of transplant rather than a stand-alone treatment.
The evidence pack lists **50 clinical trials** and **20 publications**, including several randomized phase 3 studies of busulfan-based regimens.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is empty in all listed licenses) |
| Predicted New Indication | Myelodysplastic syndrome |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Busulfan is a bifunctional alkylating agent that ablates hematopoietic stem and progenitor cells. It is used for myeloablative or reduced-intensity conditioning before allogeneic hematopoietic stem cell transplantation (HSCT).

Allogeneic HSCT is the only potentially curative treatment for MDS and is the standard of care for eligible patients with higher-risk disease. In MDS, busulfan therefore works as one part of the transplant conditioning regimen. Its role is to clear diseased marrow and allow donor cells to engraft, not to modify the disease on its own. Busulfan-based regimens (Bu/Cy, Flu/Bu, Bu/TBI) are widely studied in MDS.

This link rests on known pharmacology plus the trial and literature evidence. Key caveats:
- In several of the large randomized studies, busulfan is a comparator or backbone, and the tested variable is another drug, dose intensity or donor type.
- Use is limited to HSCT conditioning regimens and should not be read as a general MDS drug.

---

## Clinical Trial Evidence

The pack retrieved 50 trials. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | Randomized: G-CSF + decitabine + Bu/Cy vs Bu/Cy alone before transplant in RAEB-1/2 and MDS-derived AML. Busulfan is in both arms. |
| [NCT00469014](https://clinicaltrials.gov/study/NCT00469014) | Phase 2 | Completed | 72 | Busulfan-fludarabine-clofarabine conditioning for advanced or refractory AML/MDS/CML. Directly tests busulfan-based conditioning, with no randomized comparator. |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | G-CSF + decitabine + Bu/Cy vs G-CSF + decitabine + Bu/Flu conditioning in high-risk MDS. |
| [NCT06829472](https://clinicaltrials.gov/study/NCT06829472) | Phase 3 | Recruiting | 120 | Randomized comparison of melphalan 100 vs 140 mg/m² within melphalan-busulfan-fludarabine conditioning for AML or MDS. |
| [NCT00226512](https://clinicaltrials.gov/study/NCT00226512) | Phase 3 | Withdrawn | 203 (planned) | Planned randomized trial of fludarabine/busulfan with or without anti-lymphocyte antibodies in AML/MDS. Withdrawn, so no results. |
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Venetoclax + azacitidine followed by modified Bu/Cy conditioning in high-risk MDS and AML. |
| [NCT00445744](https://clinicaltrials.gov/study/NCT00445744) | N/A | Completed | 52 | Cyclophosphamide followed by IV busulfan conditioning in myelofibrosis, AML or MDS. |
| [NCT06802315](https://clinicaltrials.gov/study/NCT06802315) | Phase 2 | Recruiting | 38 | Adds total marrow irradiation to myeloablative fludarabine/busulfan in high-risk AML, CML and MDS. The busulfan-specific contribution needs confirming. |
| [NCT02143830](https://clinicaltrials.gov/study/NCT02143830) | Phase 2 | Recruiting | 70 | Busulfan/cyclophosphamide/fludarabine conditioning in Fanconi anemia. This population overlaps with MDS but is different. |
| [NCT05457556](https://clinicaltrials.gov/study/NCT05457556) | Phase 3 | Active, not recruiting | 435 | Matched unrelated vs haploidentical donor in young patients with acute leukemia or MDS. It tests donor source, and busulfan involvement is not confirmed. |

---

## Literature Evidence

The pack retrieved 20 publications. The 10 most relevant are shown below. Study types partly follow the pack's classification and are inferred from titles and abstract fragments, so they should be checked against full records.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT (phase 3) | Lancet Haematol | Treosulfan plus fludarabine vs reduced-intensity busulfan plus fludarabine in older AML/MDS patients (non-inferiority design). |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT (final analysis) | Am J Hematol | Final analysis of the same phase 3 trial. The title reports better outcomes with treosulfan than with reduced-intensity busulfan. |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (phase 3) | Lancet Haematol | G-CSF + decitabine + Bu/Cy vs Bu/Cy on relapse in MDS-RAEB or secondary AML undergoing HSCT. |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (phase 3) | J Clin Oncol | Myeloablative vs reduced-intensity conditioning in AML and MDS. Busulfan-specific data are not shown in the abstract fragment. |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic review / meta-analysis | Front Oncol | Long-term outcomes of treosulfan- vs busulfan-based conditioning in MDS and AML. |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analysis of RCTs | Front Oncol | Reduced-intensity conditioning vs myeloablative conditioning in AML and MDS. |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | Contemporary review of allogeneic HCT for myelofibrosis and MDS. HCT is described as the only potentially curative therapy. |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Retrospective (propensity-matched) | Bone Marrow Transplant | Flu/Bu vs Bu/Cy myeloablative conditioning for MDS, using Japanese registry data. |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Retrospective (propensity-matched) | Transplant Cell Ther | Myeloablative vs reduced-intensity Flu/Bu for MDS, using Japanese registry data. |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Risk assessment | Pediatr Blood Cancer | Evidence-based assessment of subsequent malignancy risk after busulfan exposure. |

---

## US Market Information

The pack lists 11 licenses in total. Four distinct authorizations are shown here, and a duplicate ANDA212127 entry is omitted. The approved-indication text is empty in all of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020954 | BUSULFEX (Otsuka America Pharmaceutical) | Injection | Not stated in the data |
| ANDA210148 | Busulfan (Accord Healthcare) | Injection | Not stated in the data |
| ANDA210931 | Busulfan (Armas Pharmaceuticals) | Injection, solution | Not stated in the data |
| ANDA212127 | Busulfan (Meitheal Pharmaceuticals) | Injection, solution | Not stated in the data |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (bifunctional alkylating agent) |
| Myelosuppression Risk | High (marrow ablation is the intended effect at conditioning doses) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function (hepatic VOD/SOS risk), neurological status (seizure risk), long-term follow-up for secondary malignancy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Label warnings, contraindications and drug-interaction data were not available in the pack.

The pack's own repurposing analysis lists the following toxicities as points to account for. They are not label-derived:
- Hepatic veno-occlusive disease / sinusoidal obstruction syndrome
- Seizures
- Secondary malignancy

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized phase 3 studies and meta-analyses evaluate busulfan-based conditioning in MDS, and allogeneic HSCT is the standard curative option for higher-risk disease. However, busulfan works here only as part of a transplant conditioning regimen. In many trials it is a comparator or backbone rather than the variable under test, so this is not a stand-alone MDS therapy. Use should stay within HSCT conditioning, with attention to busulfan's own toxicity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Approved indication text for the US licenses
- Mechanism-of-action data from DrugBank
- MDS-specific, busulfan-attributable comparative evidence (for example Bu/TBI vs Cy/TBI, or busulfan vs treosulfan)
- Confirmation of study types and busulfan roles in the trials and publications flagged above
- A toxicity monitoring plan covering hepatic, neurological and secondary-malignancy risks

The other nine model predictions have weaker support and are not evaluated here. Refractory cytopenia of childhood and aregenerative anemia rank as research questions, and the rest are on hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

