---
layout: default
title: Carboplatin
parent: High Evidence (L1-L2)
nav_order: 497
evidence_level: L2
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based chemotherapy drug, originally used to treat ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, particularly triple-negative and HER2-positive subtypes,
with **40 clinical trials** and **20 publications** compiled for this direction, including several randomized trials in the neoadjuvant setting.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and ovarian germ cell tumors) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (all 8 listed authorizations are cancelled) |
| Number of NDAs | 8 (7 ANDAs and 1 NDA) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, carboplatin is a DNA-crosslinking platinum agent. Its efficacy in ovarian cancer is established, and mechanistically it may be applicable to breast cancer.

Breast cancer, especially triple-negative breast cancer (TNBC) and BRCA-deficient tumors with homologous recombination defects, is sensitive to platinum-induced DNA damage. Ovarian cancer and BRCA-related breast cancer share this DNA-repair biology, which is why the model links the two diseases.

Randomized phase II neoadjuvant studies (GeparSixto, CALGB 40603, BrighTNess) show that adding carboplatin to standard chemotherapy mainly increases the pathologic complete response rate. The benefit on long-term survival, and in non-TNBC subtypes, is less well established.

## Clinical Trial Evidence

The data include many trials; the most relevant ones are listed below. Many other trials are phase 1 studies of new agents combined with carboplatin and do not isolate carboplatin's own effect.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomized comparison of carboplatin vs docetaxel in metastatic genetic (BRCA) breast cancer |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | Active, not recruiting | 68 | Double-blind study of carboplatin + nab-paclitaxel with or without vorinostat as preoperative chemotherapy in HER2-negative breast cancer |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: two dose-dense, dose-intensified neoadjuvant regimens (one with carboplatin) in high-risk early breast cancer |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3222 | Adjuvant AC-T vs AC-TH vs TCH (docetaxel, carboplatin, trastuzumab) in HER2-positive operable breast cancer |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel + trastuzumab with or without carboplatin as first-line therapy in HER2-amplified advanced breast cancer |
| [NCT00025688](https://clinicaltrials.gov/study/NCT00025688) | Phase 3 | Unknown | N/A | Weekly paclitaxel with or without carboplatin in women aged 65+ with metastatic breast cancer |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | Neoadjuvant bevacizumab, docetaxel and carboplatin in triple-negative breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Paclitaxel, carboplatin and trastuzumab as first-line therapy in HER2-overexpressing metastatic breast cancer |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | Epirubicin + cyclophosphamide followed by docetaxel + carboplatin in Nigerian women with TNBC |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Phase 2 | Recruiting | 185 | Correlating clinical and pathologic response with neoadjuvant systemic therapy in early breast cancer (carboplatin-specific contribution unclear) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT | Lancet Oncol | GeparSixto: adding carboplatin to neoadjuvant therapy in triple-negative and HER2-positive early breast cancer |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | RCT | J Clin Oncol | CALGB 40603: long-term outcomes of adding carboplatin or bevacizumab to neoadjuvant chemotherapy in TNBC |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | RCT | Lancet Oncol | BrighTNess (phase 3): veliparib plus carboplatin or carboplatin alone added to neoadjuvant chemotherapy in TNBC |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT | Clin Cancer Res | NeoSTOP: anthracycline-free vs anthracycline-containing neoadjuvant carboplatin regimens in stage I-III TNBC |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | RCT | BMJ | CITRINE (phase 3): adjuvant carboplatin-intensified vs standard chemotherapy in high-risk early TNBC |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | RCT (Phase III) | J Clin Oncol | Adding carboplatin to sequential taxane-anthracycline neoadjuvant chemotherapy in TNBC |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT | Nat Commun | ARX788 plus pyrotinib vs standard TCbHP (docetaxel, carboplatin, trastuzumab, pertuzumab) in HER2-positive breast cancer |
| [38492276](https://pubmed.ncbi.nlm.nih.gov/38492276/) | 2024 | Review | Breast | Platinum chemotherapy in early TNBC: improves pathologic complete response, long-term survival effect not fully clear |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Paclitaxel-carboplatin combination in advanced breast cancer: evidence for synergy, efficacy and safety |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Overview of targeted and cytotoxic inhibitors used in breast cancer |

## US Market Information

The compiled data list 8 authorizations, all with cancelled status. Approved indication text was not available.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA208487 | Carboplatin | Injection, solution | Ingenus Pharmaceuticals, LLC |
| ANDA207324 | Carboplatin | Injection, solution | Gland Pharma Limited |
| ANDA205487 | Carboplatin | Injection, solution | Eugia US LLC |
| ANDA077269 | Carboplatin | Injection, solution | Teva Parenteral Medicines, Inc. |
| NDA219921 | KYXATA | Injection | Avyxa Pharma, LLC |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class, DNA-crosslinking agent) |
| Myelosuppression Risk | High (dose-limiting; the knowledge graph links carboplatin to thrombocytopenia, neutropenia, leukopenia and anemia as contraindicated conditions) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function; neurologic and hearing assessment (peripheral neuropathy and hearing disorders appear among the knowledge-graph contraindications) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anemia, blood coagulation disease, peripheral neuropathy and other peripheral nervous system disease, hearing and auditory system disorders, and functional visual loss.
- **Drug Interactions**: 100 interactions were found. Most listed ones are Moderate, including proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), nitroimidazoles (metronidazole, tinidazole), aminoglycosides and related antibiotics (kanamycin, neomycin, streptomycin, vancomycin), and statins (rosuvastatin, simvastatin). Levofloxacin is Minor. Calcitriol, glimepiride, mesalazine, doxycycline and clotrimazole have unknown severity.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized phase II/III neoadjuvant and adjuvant trials show that carboplatin improves pathologic complete response in TNBC, and carboplatin-containing regimens are used in HER2-positive disease. The evidence for long-term survival benefit and for non-TNBC subtypes is less consistent, and the safety profile requires careful myelosuppression monitoring.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clarification of the US market status, since all listed authorizations are cancelled
- Confirmation of survival outcomes (not just pathologic response) and subtype selection (TNBC, BRCA-mutated)
- A hematologic and neurologic/ototoxicity monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

