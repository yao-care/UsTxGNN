---
layout: default
title: Cyclophosphamide
parent: High Evidence (L1-L2)
nav_order: 556
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "CYCLOPHOSPHAMIDE"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "lymph node cancer"]
description: "Cyclophosphamide: predicted new indication Myeloid leukemia (evidence level L1). Approved use: Not recorded in the local data"
---

# Cyclophosphamide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **4** 
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

## Cyclophosphamide: Myeloid leukemia
{: .text-alpha }

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy drug originally used for lymphomas, multiple myeloma, neuroblastoma, breast carcinoma and retinoblastoma.
The TxGNN model predicts it may be effective for **Myeloid Leukemia**, with **35 clinical trials** and **20 publications** compiled for this direction. Most of this evidence concerns transplant conditioning and post-transplant use rather than cyclophosphamide as a stand-alone treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L1 (as assigned in the compiled data; see the caveat in the Conclusion) |
| US Market Status | Marketed (valid licenses on record: at least 12) |
| Number of FDA Applications | at least 12 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled data. Based on known pharmacology, cyclophosphamide is an alkylating agent that cross-links DNA. It is both cytotoxic and immunosuppressive. Its efficacy in lymphoma and other malignancies is established, and mechanistically it may be applicable to myeloid leukemia.

In myeloid leukemia, cyclophosphamide is already used in several settings:
- **Transplant conditioning**, for example busulfan-cyclophosphamide, or cyclophosphamide/fludarabine with total body irradiation.
- **Post-transplant cyclophosphamide (PTCy)**, which prevents graft-versus-host disease by selectively depleting alloreactive T cells.
- **Combination salvage regimens**, such as clofarabine/etoposide/cyclophosphamide and Hyper-CVAD.

Biological plausibility is strong, and clinical use is already established in practice. Myeloid leukemia is a distinct disease from the lymphoid and solid tumors on the original list, so this is partly an extension of existing practice rather than a new mechanism.

## Clinical Trial Evidence

The compiled data include 35 trials. The table lists the 10 most relevant, favoring the higher relevance grades and the larger or completed studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | Completed | 19 | Unrelated-donor marrow transplantation, comparing conventional with T-cell-depleted grafts; cyclophosphamide is a conditioning component |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | Completed | 107 | Hyper-CVAD plus dasatinib in Ph+ ALL; the population is lymphoid, so the link to myeloid leukemia is partial |
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | Completed | 25 | Reduced-intensity haploidentical transplant with PTCy and a GVHD prevention regimen in hematologic malignancies including AML |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | Completed | 50 | Clofarabine with etoposide and cyclophosphamide in pediatric relapsed/refractory acute leukemias |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cord blood transplant after cyclophosphamide/fludarabine/TBI myeloablative conditioning |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | Active, not recruiting | 300 | HLA-mismatched unrelated donor transplant with PTCy, tacrolimus and MMF in hematologic malignancies |
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | Active, not recruiting | 700 | Pediatric AML induction trial with gemtuzumab ozogamicin; cyclophosphamide is not the tested agent |
| [NCT05515029](https://clinicaltrials.gov/study/NCT05515029) | Phase 3 | Active, not recruiting | 56 | PTCy plus abatacept, vedolizumab and a calcineurin inhibitor for GVHD prevention in pediatric and young adult hematologic malignancies |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | N/A | Recruiting | 138 | Randomized comparison of venetoclax-enhanced BUCY versus standard BUCY conditioning in high-risk AML/MDS |
| [NCT01350245](https://clinicaltrials.gov/study/NCT01350245) | Phase 2 | Completed | 28 | Two-step haploidentical transplant in hematologic malignancies; mixed population |

Several small trials (for example NCT02441803 with 11 patients and NCT02763475 with 7 patients) and trials where cyclophosphamide is only a lymphodepleting or peripheral component are omitted.

## Literature Evidence

Most of the compiled literature is cohort studies, with no randomized trial of cyclophosphamide against a non-cyclophosphamide comparator in this setting.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39168989](https://pubmed.ncbi.nlm.nih.gov/39168989/) | 2024 | Randomized trial (long-term analysis) | Blood Cancer J | GITMO AML-R2: busulfan-fludarabine versus busulfan-cyclophosphamide in AML transplant (252 patients); BuFlu had significantly better non-relapse mortality |
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compares myeloablative conditioning regimens, including Bu/Cy, in adult AML in remission |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Cohort | Cancer | EBMT registry: PTCy versus ATG versus combination for GVHD prevention in haploidentical transplant for AML |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | 217 AML patients in remission with myeloablative conditioning and PTCy; 2-year overall survival 77% |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Cohort | Bone Marrow Transplant | Single-unit cord blood versus haploidentical transplant with PTCy in AML in first remission |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | BuCy versus FluBu conditioning for allogeneic transplant in AML |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Cyclophosphamide/fludarabine nonmyeloablative versus myeloablative allotransplant in 165 AML patients |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | Prognostic factors in haploidentical transplant with PTCy for AML |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohort | Transpl Immunol | Cladribine added to busulfan-cyclophosphamide conditioning in relapsed/refractory AML |
| [14662323](https://pubmed.ncbi.nlm.nih.gov/14662323/) | 2003 | Review | Exp Hematol | Busulfan-cyclophosphamide versus TBI-cyclophosphamide conditioning in AML; results are conflicting in AML |

## US Market Information

All 12 authorizations are listed as valid in the data, and no approved-indication text was provided. The table shows 5 of the main ones.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203856 | Cyclophosphamide (Hikma Pharmaceuticals USA) | Capsule | Not available |
| NDA012141 | Cyclophosphamide (Baxter Healthcare) | Tablet | Not available |
| NDA212501 | Cyclophosphamide (BluePoint Laboratories) | Injection, solution | Not available |
| NDA210852 | Cyclophosphamide (Avyxa Pharma) | Injection | Not available |
| NDA210735 | Cyclophosphamide (Eugia US) | Injection | Not available |

The remaining seven are ANDAs (generic approvals).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High (dose-dependent; particularly at transplant-conditioning doses) |
| Emetogenicity Classification | Moderate at conventional doses; higher at high doses |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, urinalysis for hematuria |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries are based on the drug class and general knowledge, since no toxicity data were compiled for this report. Please refer to the package insert warnings and precautions.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs; 20 are shown in the compiled data. Most are Moderate, with a few Minor. Notable groups:
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms): Moderate
  - Sulfonylureas and related antidiabetics (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide, nateglinide, repaglinide): Moderate
  - Bupropion, aprepitant, metronidazole, nitisinone, troglitazone: Moderate
  - Levofloxacin and ondansetron: Minor

The key warnings and contraindications from the package insert were not available. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide is already embedded in myeloid leukemia transplant conditioning, PTCy-based GVHD prophylaxis and salvage regimens. The mechanistic rationale is strong, and many completed Phase 2 and Phase 2/3 studies and a randomized trial (GITMO AML-R2) use cyclophosphamide-containing regimens. The L1 level assigned in the compiled data should be read with caution:
- The Phase 3 trials listed are either ongoing or do not test cyclophosphamide specifically.
- The cyclophosphamide contribution is rarely isolated from the rest of the regimen.
- In the one randomized comparison, busulfan-cyclophosphamide had worse non-relapse mortality than busulfan-fludarabine.

The package insert safety data are also missing, although the drug is marketed in the US with 12 valid licenses. For these reasons, I recommend proceeding with guardrails rather than an unqualified Go.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (the safety screening cannot be completed without them)
- Detailed mechanism of action data
- Current US market and licensing status, since 12 licenses are listed as valid
- Trial analyses that isolate the contribution of cyclophosphamide, such as comparisons of conditioning regimens or PTCy against alternatives
- A safety monitoring plan for myelosuppression and for interactions with antifungals and antidiabetic drugs

## Other Predicted Indications (Brief Overview)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Note |
|------|------|------|------|------|------|
| 3 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 0.9938 | L5 | Hold | No trials or literature; immunosuppression may worsen the existing T-cell deficiency |
| 4 | Retroperitoneal neoplasm | 0.9937 | L4 | Research Question | Mixed histologies; case reports and small series only, with no trials |
| 5 | Lymph node cancer | 0.9931 | L1 | Proceed with Guardrails | Large Phase 3 trials in node-positive breast cancer, which largely overlaps existing indications (lymphoma, breast carcinoma) and is closer to an extension of existing use |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

