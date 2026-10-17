---
layout: default
title: Mercaptopurine
parent: Model Prediction Only (L5)
nav_order: 901
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mercaptopurine: predicted new indication Myeloid leukemia (evidence level L5). Approved use: Acute lymphoblastic leukemia"
monitor_inn: "MERCAPTOPURINE"
predicted_indications: ["myeloid leukemia", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "pulmonary blastoma", "Hodgkins lymphoma", "primary pulmonary lymphoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine is a purine antimetabolite originally used to treat acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **myeloid leukemia**,
with **15 clinical trials** and **20 publications** currently supporting this direction. Most of this evidence comes from multi-agent regimens in which mercaptopurine is only one component.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (the compiled data contain no approved indication text from US labels; this indication comes from the knowledge graph) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 (see the note below the table) |
| US Market Status | Cancelled only (all licenses are cancelled) |
| Number of NDAs | 4 (1 NDA and 1 further NDA-numbered entry are listed below; in total 2 NDAs and 2 ANDAs) |
| Recommended Decision | Hold |

Note on evidence level: Phase 3 trials exist for myeloid leukemia, but they test whole regimens, not mercaptopurine itself, and none isolates its contribution. A strict reading of the grading rules would therefore put this closer to L3. L2 is the level assigned in the compiled data.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, mercaptopurine is a purine antimetabolite. Its thioguanine nucleotide metabolites are incorporated into DNA and RNA and inhibit de novo purine synthesis. Its efficacy in ALL, where it is a backbone of maintenance therapy, is well established.

Myeloid blasts are also rapidly dividing cells, so interfering with nucleotide synthesis is mechanistically plausible. In practice, mercaptopurine appears in myeloid disease mainly as part of combination regimens: oral maintenance with mercaptopurine and methotrexate in AML patients ineligible for transplant, ALL-like consolidation for pediatric AML, and maintenance in acute promyelocytic leukemia (APL). Because these are combinations, the contribution of mercaptopurine alone cannot be separated out.

## Clinical Trial Evidence

Trials most relevant to myeloid leukemia (up to 10 shown):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | Active, not recruiting | 280 | Response-based, risk-stratified chemotherapy for AML/MDS in Down syndrome; multi-agent regimen |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea + valproic acid, or 6-MP + valproic acid, in AML/high-risk MDS unfit for standard therapy |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | Venetoclax + 6-MP in relapsed/refractory AML (ApoAML); small and early |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: maintenance vs observation in low/intermediate-risk APL; combination-based |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin + chemotherapy ± arsenic trioxide, then maintenance with tretinoin vs tretinoin + mercaptopurine + methotrexate in APL |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Unknown | 750 | ATRA + idarubicin, consolidation, and randomized maintenance in APL |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | Completed | 133 | ATO + ATRA + idarubicin vs AIDA in high-risk APL; 6-MP is not the tested variable |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Completed | 276 | ATO + ATRA vs ATRA + anthracycline chemotherapy (AIDA) in non-high-risk APL |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | Two multi-agent regimens with different cytarabine doses in AML/MDS; 6-MP involvement indirect |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Completed | 106 | Risk-adapted treatment of childhood APL with arsenic trioxide in consolidation |

Most of these trials test regimens or other drugs; only NCT06199557 and NCT05506332 study mercaptopurine as an explicit combination partner, and both are early-phase.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Oral maintenance with 6-MP and methotrexate in transplant-ineligible AML patients |
| [27275453](https://pubmed.ncbi.nlm.nih.gov/27275453/) | 2016 | Prospective pilot | South Asian J Cancer | Metronomic oral 6-MP in elderly AML |
| [38828002](https://pubmed.ncbi.nlm.nih.gov/38828002/) | 2024 | Cohort | Ther Adv Hematol | Dual induction with ALL-like consolidation for childhood AML in China |
| [32459546](https://pubmed.ncbi.nlm.nih.gov/32459546/) | 2020 | Retrospective | Pediatr Hematol Oncol | Sequential cytarabine and 6-MP in juvenile myelomonocytic leukemia |
| [3513537](https://pubmed.ncbi.nlm.nih.gov/3513537/) | 1986 | Clinical study | Am J Clin Oncol | Hydroxyurea with 6-MP in chronic granulocytic leukemia |
| [12057059](https://pubmed.ncbi.nlm.nih.gov/12057059/) | 2000 | Review | Curr Treat Options Oncol | Treatment options for acute promyelocytic leukemia |
| [22715121](https://pubmed.ncbi.nlm.nih.gov/22715121/) | 2012 | Cohort (phase 2) | Blood | ATRA, idarubicin and arsenic trioxide as initial APL therapy (APML4) |
| [2676034](https://pubmed.ncbi.nlm.nih.gov/2676034/) | 1989 | Review | Blood Rev | Purine metabolism as a target in leukemia chemotherapy, including 6-MP |
| [33183436](https://pubmed.ncbi.nlm.nih.gov/33183436/) | 2021 | Review | J Nanosci Nanotechnol | 6-MP nanomedicine formulations in leukemia |
| [34442422](https://pubmed.ncbi.nlm.nih.gov/34442422/) | 2021 | Review | J Pers Med | NUDT15 polymorphisms and thiopurine toxicity |

The evidence is mainly small cohorts, pilot studies and reviews; no randomized trial isolates the effect of mercaptopurine in myeloid leukemia.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040528 | Mercaptopurine (Hikma) | Tablet | Not listed (cancelled) |
| NDA205919 | Mercaptopurine (Nova Laboratories) | Suspension | Not listed (cancelled) |
| ANDA216418 | Mercaptopurine (Hikma) | Suspension | Not listed (cancelled) |
| NDA009053 | Mercaptopurine (Florida Pharmaceutical Products) | Tablet | Not listed (cancelled) |

All four authorizations are recorded as cancelled, so current product availability needs to be verified.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine antimetabolite, thiopurine class) |
| Myelosuppression Risk | High. Neutropenia, thrombocytopenia and anemia are recognized concerns; risk is greater with TPMT/NUDT15 variants (excess thioguanine nucleotides worsen neutropenia) |
| Emetogenicity Classification | Low (oral antimetabolite; please confirm against the package insert) |
| Monitoring Items | CBC with differential, liver function (6-methylmercaptopurine metabolites are linked to hepatotoxicity), renal function, bilirubin; TPMT/NUDT15 genotyping and metabolite monitoring where available |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Key Warnings and Contraindications**: Label-based warnings and contraindications are not available in the compiled data; please refer to the package insert.
- **Conditions flagged in the knowledge graph (not label text)**: kidney disease, pancreatitis, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anemia, hyperbilirubinemia, Gilbert syndrome, cholestasis, leukopenia, and hepatosplenic T-cell lymphoma.
- **Drug Interactions**: 100 interactions were found. The main ones rated Moderate are mesalazine, balsalazide, olsalazine, sulfasalazine and naltrexone. Levofloxacin is rated Minor. Many others (for example prednisone, hydrocortisone, omeprazole, metformin and vancomycin) have an unknown severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.94%), and mercaptopurine is already used within AML and APL maintenance regimens. However, the Phase 3 trials test whole regimens, not mercaptopurine, and the direct evidence is limited to small, early-phase or uncontrolled studies. Package insert safety data are missing, and all US licenses are cancelled. This is better treated as a research question than a ready candidate.

**To proceed, the following is needed:**
- Mechanism of action data from a primary source
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Evidence that isolates the contribution of mercaptopurine in myeloid leukemia, such as results from NCT06199557 and NCT05506332, or a randomized comparison
- A TPMT/NUDT15 genotyping and myelosuppression/hepatotoxicity monitoring plan
- Confirmation of current product availability in the US
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

