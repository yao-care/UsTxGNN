---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 1243
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Topotecan is a topoisomerase I inhibitor originally developed for relapsed ovarian cancer and later extended to small cell lung cancer and cervical cancer.
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**,
> with **5 clinical trials** and **20 publications** currently informing this direction — though the trial evidence is mixed in strength and relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer / small cell lung cancer / cervical cancer (well-established international indications; no formal local regulatory record in this evidence pack) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A dedicated MOA record is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, the repurposing rationale attached to this prediction and the supporting literature consistently describe topotecan as a semisynthetic camptothecin derivative that acts as a **topoisomerase I inhibitor**: it stabilizes the DNA–Topo I cleavage complex, causing single-strand DNA breaks and replication fork collapse, which triggers apoptosis preferentially in rapidly dividing cells.

This is a broad-spectrum cytotoxic mechanism, not one restricted to gynecologic malignancy. Ovarian cancer (the drug's classic indication) and breast cancer share overlapping biology — including BRCA1/2-related DNA-repair deficiency and high proliferative subtypes — which provides mechanistic plausibility for cross-tumor activity. Preclinical work specifically links topotecan to triple-negative breast cancer (TNBC), the most aggressive and highest-proliferation subtype, via targets such as TFDP1 and MYC-driven synthetic lethality.

Clinically, this plausibility is only partially confirmed: a completed CALGB Phase II trial and several small Phase I/II studies tested topotecan directly in breast cancer, but results are dated (1990s–2000s), come from small cohorts, and predate modern subtype-directed trial design. No confirmatory Phase III trial in breast cancer currently exists in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan + ifosfamide/mesna + etoposide) followed by autologous stem cell rescue in metastatic breast cancer; trial terminated, no efficacy conclusion available |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's-choice chemotherapy in gBRCA-mutated, platinum-sensitive relapsed ovarian cancer; large completed trial, but topotecan's specific role in the comparator arm is not detailed in the summary |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib triplet vs. standard-of-care chemotherapy in platinum-resistant recurrent ovarian/peritoneal/fallopian cancer; topotecan is a comparator/backbone agent, not the primary study drug |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with standard chemo/immunotherapy regimens (including topotecan) in advanced malignancies; safety-focused, terminated early |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid high-throughput drug screening to guide chemotherapy selection in refractory solid tumors; not a direct treatment trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II Trial (CALGB) | American Journal of Clinical Oncology | Topotecan monotherapy in advanced breast cancer after prior chemotherapy; 40 of 53 patients evaluable — earliest direct efficacy data in this population |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Cohort/Pilot | Onkologie | Pilot study of topotecan as primary chemotherapy for breast cancer patients with brain metastases |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase 1/2 Trial | British Journal of Cancer | Continuous infusional topotecan in advanced breast cancer and NSCLC; no evidence of increased efficacy over standard dosing |
| [21514634](https://pubmed.ncbi.nlm.nih.gov/21514634/) | 2011 | Phase II RCT | Gynecologic Oncology | Lapatinib + topotecan in platinum-refractory/resistant ovarian/peritoneal carcinoma (note: population is ovarian, not breast, cancer despite indexing) |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical/Mechanistic | International Journal of Biological Macromolecules | TFDP1 identified as a druggable target for topotecan in triple-negative breast cancer |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan + pazopanib shows potent efficacy in preclinical models of primary and metastatic TNBC |
| [39657238](https://pubmed.ncbi.nlm.nih.gov/39657238/) | 2024 | Preclinical | ACS Applied Materials & Interfaces | Biomimetic topotecan + anti-VEGF gene nanoparticle combination for metastatic breast cancer |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacological Research | Daidzein enhances topotecan's anticancer effect and reverses BCRP-mediated drug resistance in breast cancer |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical/Mechanistic | Cancer Research | Topoisomerase I inhibition induces synthetic lethality via R-loop accumulation in MYC-driven breast cancer cell lines |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-Geburtshilfliche Rundschau | Review of new cytotoxic agents (including topotecan) in breast carcinoma therapy |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor, camptothecin derivative) |
| Myelosuppression Risk | High — dose-limiting toxicity reported in related trial data (e.g., PMID 8617580: median nadir neutrophil count 1.55 cells/mm³, platelet count 20,500/mm³) |
| Emetogenicity Classification | Low to moderate (typical for topoisomerase I inhibitor class) |
| Monitoring Items | CBC with differential (neutrophils, platelets), renal function (drug is renally cleared), signs of infection |
| Handling Protection | Must be handled per cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (DG001 — TFDA warnings/contraindications unavailable) prevents even an initial safety review (S1), and the breast cancer efficacy evidence, while mechanistically plausible, rests on small, dated Phase I/II trials rather than confirmatory Phase III data; several cited trials/publications are also indexed with likely disease-label mismatches (e.g., NCT02282020 and PMID 21514634 concern ovarian, not breast, cancer) and need manual verification before further scoring.

**To proceed, the following is needed:**
- TFDA (or equivalent) approved label: warnings, contraindications, and dosing information
- Confirmed mechanism of action documentation from DrugBank
- Manual re-verification of disease-label matches for NCT02282020, NCT04739800, and PMID 21514634
- Drug–drug interaction (DDI) data, currently unavailable
- Assessment of whether any ongoing/planned Phase III trial specifically targets breast cancer (particularly TNBC) populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

