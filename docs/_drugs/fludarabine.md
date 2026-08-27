---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Fludarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fludarabine: Toward Plasma Cell Myeloma (Original Indication Not on Record)

## One-Sentence Summary

Fludarabine is a purine nucleoside antimetabolite chemotherapy agent; the evidence pack for this candidate does not contain a documented original approved indication or market license. The TxGNN model predicts it may be effective for **Plasma Cell Myeloma**, with **50 clinical trials** and **20 publications** currently associated with this direction — though most of this body of evidence reflects fludarabine's well-established role as a stem-cell transplant *conditioning* agent rather than direct evidence of anti-myeloma monotherapy efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no approved-indication or license text on file) |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fludarabine is not available in this evidence pack, and no original approved indication is on record for cross-reference. However, other entries within this same dataset independently describe fludarabine's pharmacology: it is a purine nucleoside analog that inhibits DNA synthesis and induces apoptosis in malignant marrow cells and lymphocytes. This mechanism underlies its long-standing, well-documented use as a core component of induction regimens (e.g., FLAG-IDA) and as the backbone of reduced-intensity/nonmyeloablative conditioning regimens ahead of allogeneic stem-cell and CAR-T therapies for hematologic malignancies.

For plasma cell myeloma specifically, the rationale is twofold. First, there is direct preclinical evidence (PMID 17976186) that fludarabine inhibits human myeloma cell lines both *in vitro* and *in vivo*, concomitant with decreased Akt phosphorylation. Second, fludarabine is widely used — alone or combined with melphalan/bortezomib — as the conditioning backbone for allogeneic transplantation and, increasingly, as the lymphodepletion regimen preceding BCMA-directed CAR-T and bispecific-antibody therapies in myeloma.

That said, this evidence base has an important limitation: no completed Phase 3 randomized controlled trial specifically tests fludarabine as a stand-alone anti-myeloma treatment (as opposed to a supportive/conditioning agent). The large majority of trials and publications capture fludarabine's role *within* a transplant or cellular-therapy regimen, not as an independently validated therapeutic option for myeloma. This distinction should be kept in mind when interpreting the TxGNN prediction score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231412](https://clinicaltrials.gov/study/NCT01231412) | Phase 3 | Completed | 174 | Randomized comparison of post-transplant immunosuppression strategies to prevent acute GVHD after fludarabine-based nonmyeloablative conditioning in hematologic malignancies (including myeloma); fludarabine is a background conditioning agent, not the trial's primary endpoint drug. |
| [NCT00427557](https://clinicaltrials.gov/study/NCT00427557) | Phase 2 | Completed | 31 | Tested adding umbilical cord blood to standard stem-cell transplant conditioning (including fludarabine) for advanced hematologic malignancies, including myeloma, to improve transplant response and evaluate safety. |
| [NCT04098393](https://clinicaltrials.gov/study/NCT04098393) | Phase 1 | Active, not recruiting | 39 | Pilot study of a condensed busulfan/melphalan/fludarabine conditioning regimen plus ATG before CD34+-selected allogeneic transplant for various blood cancers, including myeloma. |
| [NCT06577025](https://clinicaltrials.gov/study/NCT06577025) | Phase 2 | Active, not recruiting | 43 | Evaluates different treatment sequences of cilta-cel, talquetamab, and teclistamab after DVRd induction in newly diagnosed standard-risk multiple myeloma; fludarabine is used for pre-CAR-T/bispecific lymphodepletion. |
| [NCT06242249](https://clinicaltrials.gov/study/NCT06242249) | Phase 1/2 | Not yet recruiting | 10 | Determines safety and maximum tolerated dose of anti-BCMA CAR-NK cell therapy in relapsed/refractory multiple myeloma, with fludarabine included in the lymphodepleting pre-treatment. |
| [NCT00560053](https://clinicaltrials.gov/study/NCT00560053) | Phase 3 | Completed | 500 | Multicenter "Multiple Myeloma 2000" trial evaluating an optimized therapeutic strategy including tandem autotransplantation (BUMEL) for multiple myeloma, with analysis of minimal residual disease and prognostic impact. |
| [NCT00615589](https://clinicaltrials.gov/study/NCT00615589) | Phase 2 | Terminated | 22 | Allogeneic HSCT with reduced-toxicity myeloablative conditioning for high-risk multiple myeloma patients who typically relapse after autologous transplant, testing whether a graft-versus-myeloma effect improves outcomes. |
| [NCT03767725](https://clinicaltrials.gov/study/NCT03767725) | Phase 1 | Unknown | 10 | Anti-BCMA and/or anti-CD19 CAR T-cell therapy for relapsed multiple myeloma refractory to chemotherapy and prior autologous transplant, using fludarabine-based lymphodepletion before CAR-T infusion. |
| [NCT03322735](https://clinicaltrials.gov/study/NCT03322735) | Phase 1/2 | Unknown | 10 | BCMA-targeted CAR-T cells (with fludarabine/cyclophosphamide lymphodepletion) for safety and feasibility assessment in relapsed/refractory multiple myeloma. |
| [NCT04579523](https://clinicaltrials.gov/study/NCT04579523) | Phase 1 | Not yet recruiting | 30 | Dose-escalation trial of ²¹¹At-labeled anti-CD38 monoclonal antibody combined with fludarabine (± cyclophosphamide and low-dose TBI) as pre-transplant conditioning for high-risk multiple myeloma. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 trial | American Journal of Clinical Oncology | Phase 1 study of bortezomib + fludarabine + melphalan (± total marrow irradiation) as allogeneic HSCT conditioning for high-risk/relapsed-refractory multiple myeloma. |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective cohort | Bone Marrow Transplantation | Multicenter analysis of fludarabine + treosulfan reduced-toxicity conditioning before allogeneic SCT in 34 myeloma patients; regimen found feasible. |
| [15389436](https://pubmed.ncbi.nlm.nih.gov/15389436/) | 2004 | Cohort | Biology of Blood and Marrow Transplantation | Prognostic-factor analysis of melphalan/fludarabine dose-reduced allografts in 120 myeloma patients; relapse after prior autograft and chronic GVHD were the strongest predictors of treatment-related mortality. |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohort | Blood Cancer Journal | Compared bendamustine vs. fludarabine/cyclophosphamide lymphodepletion prior to BCMA CAR-T therapy in multiple myeloma. |
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | Real-world cohort | Transplantation and Cellular Therapy | Fludarabine lymphodepletion exposure is associated with toxicities after idecabtagene vicleucel (ide-cel) CAR-T in relapsed/refractory multiple myeloma; highlights pharmacokinetic variability of fludarabine. |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 trial | Nature Medicine | UNIVERSAL trial: allogeneic BCMA-targeting CAR-T (ALLO-715) with anti-CD52-containing lymphodepletion in 43 relapsed/refractory myeloma patients; established safety and tolerability. |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Long-term follow-up | Journal of Hematology & Oncology | 5-year follow-up of LEGEND-2 (first-in-human LCAR-B38M/cilta-cel BCMA CAR-T trial), showing deep and durable responses in relapsed/refractory myeloma. |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Real-world cohort | Blood | Standard-of-care outcomes of ciltacabtagene autoleucel in 236 relapsed/refractory myeloma patients across 16 US academic centers. |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Case report/commentary | European Journal of Haematology | Early report specifically discussing fludarabine use in the context of plasma cell leukemia. |
| [28473042](https://pubmed.ncbi.nlm.nih.gov/28473042/) | 2017 | Review | Mayo Clinic Proceedings | Review of monoclonal gammopathy-associated peripheral neuropathy across the plasma cell disorder spectrum, including multiple myeloma. |

---

## US Market Information

Currently no marketing authorization records are available for fludarabine in this evidence pack — `taiwan_regulatory.total_licenses` is 0 and the market status is recorded as **Not Marketed**.

---

## Cytotoxicity

Fludarabine is a purine nucleoside analog / antimetabolite chemotherapy agent used across leukemia, lymphoma, and hematopoietic transplant conditioning regimens, and therefore qualifies as an antineoplastic drug for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Note that a **Blocking**-severity data gap (TFDA/FDA label warnings and contraindications) has been flagged for this drug and must be resolved before any safety-stage (S1) assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN system itself stages this candidate as "Research Question" (decision stage S2, evidence level L2) — supportive but not yet decision-grade evidence, since no completed Phase 3 RCT has tested fludarabine as a stand-alone anti-myeloma therapy; nearly all cited trials and publications document its role as a *conditioning/lymphodepletion* agent rather than a direct treatment.
- A **Blocking** data gap on labeled warnings and contraindications (DG001) means safety cannot yet be evaluated, and the drug is not currently marketed (0 licenses on file), further limiting near-term actionability.

**To proceed, the following is needed:**
- TFDA/FDA package-insert warnings, precautions, and contraindications (resolves DG001, currently Blocking)
- Documented mechanism of action and original approved indication for this candidate (resolves DG002)
- Trial-level evidence isolating fludarabine's direct anti-myeloma activity from its conditioning/lymphodepletion role, ideally a prospective comparative study
- Drug interaction (DDI) data, currently unavailable (`query_status: not_found`)

**Note:** Within this same evidence pack, other predicted indications carry notably stronger evidence than the top-ranked plasma cell myeloma candidate — most importantly **myelodysplastic syndrome** (rank 7, evidence level L1, decision stage S3, "Proceed with Guardrails"), where fludarabine is an established component of both induction chemotherapy (FLAG-IDA) and standard conditioning regimens. That candidate may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

