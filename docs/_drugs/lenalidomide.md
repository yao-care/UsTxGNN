---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 844
evidence_level: L5
indication_count: 6
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lenalidomide: From Undocumented Original Indication to Myeloid Leukemia

## One-Sentence Summary

Lenalidomide (DrugBank DB00480) is an oral immunomodulatory imide drug (IMiD); its original approved indication(s) are not recorded in this evidence pack. The TxGNN model predicts it may be effective for **Myeloid Leukemia**, with **50 clinical trials** and **20 publications** currently supporting this direction — though most of that trial base actually reflects lenalidomide's established use in myelodysplastic syndrome (MDS) rather than de novo acute myeloid leukemia (AML).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (no licenses/indication text on file) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified — see caveat below) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for lenalidomide is not available in this evidence pack. Based on publicly known pharmacology, lenalidomide is an immunomodulatory imide drug (IMiD) that binds cereblon (CRBN), promoting ubiquitination and degradation of the transcription factors IKZF1/IKZF3 — this is directly supported by literature in the evidence set (PMID 39881283: "The histone demethylase KDM5C enhances the sensitivity of acute myeloid leukemia cells to lenalidomide by stabilizing cereblon"). Through this mechanism it exerts antiproliferative, anti-angiogenic, and immune-stimulatory (NK/T-cell activating) effects.

Lenalidomide's best-established hematologic use is in myelodysplastic syndrome (MDS), including MDS with deletion 5q — a disease on the same myeloid differentiation spectrum as AML, and one that frequently transforms into AML. The evidence pool for this predicted indication is dominated by MDS trials (including the two completed Phase 3 RCTs), with a substantial secondary layer of Phase 1/2 studies testing lenalidomide directly in AML, largely in combination with azacitidine, cytarabine-based chemotherapy, or as post-transplant/post-remission maintenance.

Mechanistically this extension is plausible: MDS and AML share overlapping myeloid clonal biology, and lenalidomide's immunomodulatory and anti-angiogenic activity has already shown clinical signal in AML settings (post-transplant relapse, maintenance therapy, and combination regimens). However, the strongest (Phase 3) evidence in the pack is for MDS, not AML specifically — direct AML evidence remains Phase 1/2 in scale, which should temper confidence in reading this as an AML-specific L1 signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00179621](https://clinicaltrials.gov/study/NCT00179621) | Phase 3 | Completed | 205 | Lenalidomide (10mg/5mg) vs. placebo in RBC transfusion-dependent low/int-1 risk MDS with del(5q) |
| [NCT01029262](https://clinicaltrials.gov/study/NCT01029262) | Phase 3 | Completed | 239 | Lenalidomide vs. placebo in transfusion-dependent anemia, low/int-1 risk MDS without del(5q) |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | Lenalidomide vs. sequential azacitidine+lenalidomide vs. azacitidine alone in older newly-diagnosed AML |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | Completed | 37 | Sequential azacitidine+lenalidomide in relapsed/refractory AML and high-risk MDS |
| [NCT01772420](https://clinicaltrials.gov/study/NCT01772420) | Phase 2 | Completed | 52 | Lenalidomide + eltrombopag for symptomatic anemia in low/int-1 risk MDS |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML patients in remission |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | Completed | 41 | Lenalidomide + MEC (mitoxantrone/etoposide/cytarabine) in relapsed/refractory AML |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | Completed | 37 | Lenalidomide + azacitidine in advanced MDS |
| [NCT02472691](https://clinicaltrials.gov/study/NCT02472691) | Phase 2 | Completed | 50 | Lenalidomide + azacitidine + donor lymphocyte infusion for MDS/CMML/AML relapse post allo-SCT |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | Completed | 27 | Lenalidomide in relapsed/refractory AML or high-risk MDS with chromosome 5 abnormalities |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35277655](https://pubmed.ncbi.nlm.nih.gov/35277655/) | 2022 | RCT | Leukemia | Randomized Phase II study of azacitidine ± lenalidomide in higher-risk MDS/AML with del(5q) |
| [30653424](https://pubmed.ncbi.nlm.nih.gov/30653424/) | 2019 | Trial | J Clin Oncol | Combination lenalidomide + azacitidine as salvage therapy after allo-SCT relapse in AML |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Trial | Haematologica | Azalena-Trial: azacitidine + lenalidomide + DLI for post-transplant relapse of MDS/AML/CMML |
| [31009835](https://pubmed.ncbi.nlm.nih.gov/31009835/) | 2019 | Trial | Leukemia Research | Sequential azacitidine + lenalidomide in relapsed/refractory AML with predictive modeling |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Trial | J Geriatric Oncology | Phase Ib lenalidomide as post-remission therapy in older AML patients |
| [40250191](https://pubmed.ncbi.nlm.nih.gov/40250191/) | 2025 | Trial | Leukemia Research | Phase I lenalidomide + bortezomib for AML/MDS relapsing after allo-SCT |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Trial | Bone Marrow Transplant | Safety and tolerability of lenalidomide maintenance post-transplant in AML/high-risk MDS |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic Review/Meta-analysis | Hematology (Amsterdam) | Efficacy and adverse events of azacitidine+lenalidomide in AML, MDS, CMML |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making and treatment of myelodysplastic syndromes |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Myelodysplastic syndromes overview, including progression to AML |

---

## US Market Information

Not currently marketed — the evidence pack records zero licenses/NDAs and a market status of "Not Marketed" (未上市).

---

## Cytotoxicity

Lenalidomide is an antineoplastic agent used in hematologic malignancies (MDS, and investigationally AML), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — immunomodulatory imide drug (IMiD), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (missing TFDA label warnings/contraindications) prevents entry into the S1 safety pre-assessment stage, and the drug currently has no market presence or license record in this jurisdiction. While the evidence base is large (50 trials, 20 publications, including 2 completed Phase 3 RCTs), that Phase 3 evidence is anchored in MDS rather than AML itself, so it does not by itself justify proceeding without a safety review.

**To proceed, the following is needed:**
- TFDA label/package insert (warnings, contraindications) — download and parse from the TFDA website (DG001, Blocking)
- Mechanism of action detail from DrugBank API to support mechanistic-relevance analysis (DG002, High)
- A dedicated review of AML-specific (vs. MDS-specific) trial evidence to confirm whether Phase 3-level support genuinely extends to the "myeloid leukemia" indication or is primarily attributable to lenalidomide's existing MDS approval
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

