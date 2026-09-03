---
layout: default
title: Mycophenolic Acid
parent: 僅模型預測 (L5)
nav_order: 947
evidence_level: L5
indication_count: 10
---

# Mycophenolic Acid
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

# Mycophenolic Acid: From Transplant-Rejection Immunosuppression to Hemoglobinopathy

## One-Sentence Summary

Mycophenolic acid (via its prodrug mycophenolate mofetil, MMF) is a purine-synthesis (IMPDH) inhibitor best established as an immunosuppressant for preventing organ transplant rejection. The TxGNN model predicts it may be effective for **Hemoglobinopathy**, with **27 clinical trials** and **9 publications** currently retrieved — but most of this evidence describes MMF only as a supportive immunosuppressive component of stem-cell transplant regimens, not as a direct treatment for the underlying blood disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan/US license data (drug is unmarketed, 0 licenses on file); literature within this pack (PMID 9399601) notes MMF is established for "prevention of acute renal allograft rejection when given in combination with cyclosporine and steroids" |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field marked as a data gap). Based on information embedded in the retrieved evidence, mycophenolic acid is a selective, reversible inhibitor of inosine monophosphate dehydrogenase (IMPDH), which blocks the de novo purine synthesis pathway that lymphocytes depend on for proliferation. This underlies its use as an immunosuppressant in transplantation and autoimmune disease.

The link to hemoglobinopathy (sickle cell disease, thalassemia) is mechanistically indirect. Nearly all 27 retrieved trials are allogeneic hematopoietic stem cell transplantation (HSCT) studies, in which MMF is used as part of the graft-versus-host disease (GVHD) prophylaxis/conditioning regimen — not as a therapy that corrects the underlying globin-chain or red-cell defect. The rationale attached to this candidate explicitly flags this as a likely **confounded association**: TxGNN appears to have picked up the co-occurrence of "MMF" and "hemoglobinopathy" in transplant literature, rather than a genuine drug-disease treatment relationship. HSCT itself is curative for severe hemoglobinopathies, but MMF's role there is supportive immunosuppression, not disease-modifying treatment of the hemoglobinopathy per se.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06872333](https://clinicaltrials.gov/study/NCT06872333) | Phase 2 | Recruiting | 62 | Allogeneic HSCT for high-risk hemoglobinopathies and red-cell transfusion-dependent disorders; MMF is part of the transplant regimen |
| [NCT02435901](https://clinicaltrials.gov/study/NCT02435901) | Phase 1/2 | Completed | 29 | Reduced-intensity conditioning HSCT for sickle cell disease and β-thalassemia major with standard immunosuppressive medications |
| [NCT01279616](https://clinicaltrials.gov/study/NCT01279616) | Phase 2 | Terminated | 8 | Reduced-toxicity immunosuppressive/myeloablative preparative regimen for unrelated-donor HSCT in severe sickle cell disease |
| [NCT00489281](https://clinicaltrials.gov/study/NCT00489281) | Phase 2 | Terminated | 43 | Non-myeloablative conditioning and HLA-mismatched/matched bone marrow transplant for sickle cell anemia and other hemoglobinopathies |
| [NCT01810588](https://clinicaltrials.gov/study/NCT01810588) | Phase 2 | Active, not recruiting | 270 | Optimal cord-blood selection strategy (IPA/NIMA matching) to improve haplo-cord transplant outcomes |
| [NCT03249831](https://clinicaltrials.gov/study/NCT03249831) | Phase 1 | Active, not recruiting | 3 | Non-myeloablative conditioning and CD4+ T-cell-depleted haploidentical HSCT to induce mixed chimerism in sickle cell disease |
| [NCT03171831](https://clinicaltrials.gov/study/NCT03171831) | Phase 4 | Unknown | 30 | Safety/efficacy of haploidentical HSCT for thalassemia major |
| [NCT01350232](https://clinicaltrials.gov/study/NCT01350232) | N/A | Terminated | 2 | Reduced-intensity allogeneic HSCT for sickle cell anemia from HLA-matched/partially-matched related donors; terminated after only 2 enrollees |
| [NCT02867800](https://clinicaltrials.gov/study/NCT02867800) | Phase 1 | Completed | 24 | Abatacept added to standard GVHD prophylaxis (calcineurin inhibitor + methotrexate) after HSCT for pediatric sickle cell disease; MMF not the study drug |
| [NCT04009525](https://clinicaltrials.gov/study/NCT04009525) | Phase 4 | Completed | 823 | Large multicenter prospective study of allo-HSCT efficacy in thalassemia major |

*Note: 17 additional trials were retrieved but not shown here (mostly ungraded/lower-relevance HSCT studies where MMF appears only as background GVHD prophylaxis).*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Review (PK modeling) | Eur J Drug Metab Pharmacokinet | Population-pharmacokinetics-based MMF dosing recommendations for pediatric thalassemia patients undergoing HSCT |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Cohort | Biol Blood Marrow Transplant | Alternative-donor HSCT with post-transplant cyclophosphamide is curative for nonmalignant disorders including hemoglobinopathies |
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Cohort | Transplant Cell Ther | MMF used to boost immunosuppression in patients with declining mixed chimerism after thalassemia HSCT |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Cohort | Biol Blood Marrow Transplant | Reduced-intensity HSCT shows stable long-term donor engraftment in sickle cell disease |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Cohort (Phase 1) | Biol Blood Marrow Transplant | Unrelated cord blood transplant after reduced-intensity conditioning for severe sickle cell disease |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Cohort | Biol Blood Marrow Transplant | Unrelated-donor HSCT with post-transplant cyclophosphamide and MMF-based GVHD prophylaxis for severe sickle cell disease |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Cohort | Hematology (Amsterdam) | Risk factors for pure red cell aplasia after major ABO-incompatible allo-HSCT |
| [15126382](https://pubmed.ncbi.nlm.nih.gov/15126382/) | 2004 | Review (limited relevance) | Genetics | General genetics/medicine commentary, not specific to MMF or hemoglobinopathy treatment |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case Report (adverse event) | J Perinatol | Neonatal anemia and hydrops fetalis following maternal MMF use during pregnancy — a safety signal, not an efficacy finding |

## US Market Information

This drug currently has no marketed product license records in the dataset — Taiwan/US regulatory status is "Not Marketed" with 0 licenses on file.

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug-interaction data are currently available for this candidate — this is flagged as a **Blocking** data gap (DG001) that prevents entry into the S1 safety pre-assessment stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap exists (no TFDA warnings/contraindications), which by itself prevents starting the S1 safety review.
- The mechanistic link for the top-ranked candidate (hemoglobinopathy) is very likely confounded: nearly all supporting trials/literature describe MMF as a background immunosuppressant within HSCT protocols, not as a treatment acting on the hemoglobinopathy's underlying pathology.
- The other 8 predicted indications in this evidence pack (migraine, chromosome 16p deletion, beta-thalassemia standalone, hereditary pyropoikilocytosis, GPI-deficiency hemolytic anemia, pyruvate kinase deficiency, antithrombin deficiency type 2) are all Evidence Level L5 with zero retrieved trials or literature — pure model prediction with no supporting evidence. Rheumatoid arthritis (rank 9, L3) has a terminated Phase 3 RCT with no conclusive results, and recent literature centers on RA-related interstitial lung disease off-label use rather than RA itself.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) to clear the Blocking gap and enable S1 safety review
- DrugBank MOA detail to support a rigorous mechanism-relevance analysis
- Trial-level analysis that isolates MMF's independent contribution from the overall HSCT conditioning regimen, to resolve the confounded-association concern
- Drug-drug interaction (DDI) data, currently unavailable (query status: not_found)
- Confirmed original-indication/regulatory baseline, since no Taiwan or US license records currently exist for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

