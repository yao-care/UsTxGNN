---
layout: default
title: Pemetrexed
parent: High Evidence (L1-L2)
nav_order: 1025
evidence_level: L2
indication_count: 10
---

# Pemetrexed
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Pemetrexed: From Non-Small Cell Lung Cancer and Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate chemotherapy originally used for non-small cell lung cancer and malignant pleural mesothelioma.
The TxGNN model predicts it may be effective for **malignant peritoneal mesothelioma**,
with **7 clinical trials** (1 directly relevant completed Phase 2 trial) and **20 publications** (mostly reviews and retrospective series) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer, lung cancer, malignant pleural mesothelioma (per the knowledge graph; the US license records contain no indication text) |
| Predicted New Indication | Malignant peritoneal mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (both NDAs cancelled) |
| Number of NDAs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, pemetrexed inhibits thymidylate synthase, DHFR and GARFT, which blocks nucleotide synthesis in rapidly dividing cells. It is a standard partner for cisplatin or carboplatin in pleural mesothelioma.

Pleural and peritoneal mesothelioma share histology and biology, and mesothelioma cells are sensitive to antifolates regardless of anatomic site. The peritoneal indication is therefore a plausible extension of the pleural indication. Peritoneal mesothelioma is not among the listed original indications, and it is a rare disease with few site-specific trials. Systemic therapy recommendations are largely extrapolated from pleural mesothelioma studies. Pemetrexed-platinum is cited as a first-line systemic option in a 2024 review (JNCCN).

Other predictions in the list include pleural mesothelioma subtypes (epithelioid, sarcomatoid, biphasic). These are largely existing indications or subtypes of one. Several others (pleural adenomatoid tumor, iminoglycinuria, lymphohistiocytoid mesothelioma) have no supporting evidence or plausible mechanism and appear to be model artifacts. This report focuses on the top-ranked prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed plus gemcitabine as front-line therapy for pleural or peritoneal mesothelioma (covers the peritoneal site directly) |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized: chemotherapy (carboplatin, pemetrexed, bevacizumab) with or without atezolizumab in peritoneal mesothelioma |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm: sintilimab and bevacizumab plus pemetrexed and cisplatin in unresectable peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | MESOTIP: PIPAC plus systemic cisplatin-pemetrexed vs systemic chemotherapy alone, first-line |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | ICARuS II: intraperitoneal vs intravenous chemotherapy after cytoreductive surgery and HIPEC; pemetrexed's role unclear |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 with cisplatin and pemetrexed in advanced solid tumors, including mesothelioma (mixed population) |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed and imatinib in unresectable or metastatic mesothelioma; safety and maximum tolerated dose |

---

## Literature Evidence

Most items are narrative reviews or retrospective series; no randomized trial specific to peritoneal mesothelioma was identified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Comparative study | Clin Med Insights Oncol | First-line pemetrexed-platinum vs gemcitabine-platinum in peritoneal mesothelioma; pemetrexed-platinum is at the forefront of first-line systemic treatment |
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Review | JNCCN | Systemic options for peritoneal mesothelioma; recommendations extrapolated from pleural trials, with pemetrexed-based chemotherapy among first-line options |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective | Expert Rev Anticancer Ther | Efficacy of first-line pemetrexed plus cisplatin in peritoneal mesothelioma |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | Single-institution series | Tumori | Efficacy and safety of pemetrexed-cisplatin in chemo-naïve peritoneal mesothelioma |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multicenter study | Ann Surg Oncol | Treatment strategies and outcomes in peritoneal mesothelioma |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Review | Cancers | Diagnostic and therapeutic pathway; CRS plus HIPEC gives median OS of 34 to 92 months in selected patients |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Treatment of peritoneal mesothelioma; CRS and HIPEC are the preferred initial treatment in selected patients |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Overview of a rare, poor-prognosis malignancy |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | J Gastrointest Oncol | Diagnosis and management of peritoneal mesothelioma |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Case report | BMJ Case Rep | Nivolumab in peritoneal mesothelioma after initial systemic chemotherapy |

For the pleural site, the pivotal Phase 3 trial (PMID [12860938](https://pubmed.ncbi.nlm.nih.gov/12860938/), 2003) compared pemetrexed plus cisplatin with cisplatin alone, and MAPS (PMID [26719230](https://pubmed.ncbi.nlm.nih.gov/26719230/), 2016) tested adding bevacizumab. These support the pleural indication and underpin the extrapolation to the peritoneum.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210661 (cancelled) | Pemetrexed dipotassium (Avyxa Pharma) | Injection, powder, lyophilized, for solution | Not recorded |
| NDA208419 (cancelled) | Pemetrexed (Teva) | Solution, concentrate | Not recorded |

Both listed NDAs are cancelled, so availability depends on other pemetrexed products not captured in these records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate antimetabolite) |
| Myelosuppression Risk | Medium to High. The knowledge graph lists neutropenia, thrombocytopenia, agranulocytosis and anemia as contraindication-related conditions |
| Emetogenicity Classification | Low to Medium (general drug class; not confirmed by the data compiled) |
| Monitoring Items | CBC with differential, renal function (creatinine clearance), liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

- **Disease-level cautions (knowledge graph, not label text)**: kidney disease and impaired renal function, thrombocytopenia, neutropenia, agranulocytosis, anemia (including macrocytic anemia), and pyoureter.
- **Drug Interactions**: 100 interactions were found, of which the 20 reviewed were all moderate. The main groups are:
  - **H2 blockers and aspirin**: famotidine, ranitidine, cimetidine, acetylsalicylic acid.
  - **Nephrotoxic agents**: amphotericin B (several formulations), vancomycin, kanamycin, neomycin, polymyxin B.
  - **Others**: metformin, amoxicillin, mesalazine, balsalazide, olsalazine, sapropterin, levofloxacin.

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pemetrexed-platinum is an established backbone in pleural mesothelioma, and the peritoneal disease shares its biology. A completed Phase 2 trial covers the peritoneal site, and several ongoing randomized and single-arm Phase 2 trials include pemetrexed. Peritoneal-specific evidence is still limited to small, mostly non-randomized studies, so the evidence level is L2 and the recommendation is conditional.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Results from the ongoing peritoneal mesothelioma trials (NCT05001880, NCT06543069), and the peritoneal-specific outcomes from NCT00061477
- Confirmation of a currently marketed US pemetrexed product, since both listed NDAs are cancelled
- A monitoring plan for renal function and blood counts, with attention to the nephrotoxic and NSAID interactions
- Not recommended at this stage: pleural adenomatoid tumor, lymphohistiocytoid mesothelioma, and iminoglycinuria (no evidence or mechanism)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

