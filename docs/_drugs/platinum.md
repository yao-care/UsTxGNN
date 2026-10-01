---
layout: default
title: Platinum
parent: Model Prediction Only (L5)
nav_order: 1053
evidence_level: L5
indication_count: 10
---

# Platinum
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

# Platinum: From Marketed Platinum Products (No Listed Indication) to Urinary Bladder Carcinoma

## One-Sentence Summary

Platinum (DrugBank DB12257) has 13 US-marketed licenses, all for pellet or liquid products, and none of the records lists an approved indication.
The TxGNN model predicts it may be effective for **urinary bladder carcinoma**, with **50 clinical trials** and **20 publications** linked to this prediction.
Most of that evidence concerns platinum-based chemotherapy (mainly cisplatin and carboplatin), not the elemental platinum products currently marketed. This is guideline-concordant use of a drug class rather than novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Urinary bladder carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L1 (per Evidence Pack scoring; platinum-specific attribution is limited, see below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for DB12257. Based on known information, platinum agents such as cisplatin and carboplatin form DNA crosslinks that trigger apoptosis in rapidly dividing tumor cells. This is the mechanism behind platinum-based chemotherapy in urothelial cancer.

The regulatory records list no original indication, so there is no "original-to-new" indication link to trace. What links platinum to bladder cancer is the drug class. Cisplatin-based chemotherapy, such as gemcitabine plus cisplatin, is the established first-line standard for metastatic urothelial cancer. It is also used in the neoadjuvant and perioperative settings. The 2024 *Nature Reviews Urology* review in the literature table below states this directly. The high TxGNN score is consistent with this established use.

The prediction rests on platinum-based chemotherapy compounds, not on the marketed "Platinum Metallicum" pellet products. Whether the evidence applies to DB12257 depends on how that entry is defined, which is the central guardrail for any next step.

---

## Clinical Trial Evidence

Of the 50 linked trials, the 10 most relevant are listed. Many are combination regimens in which platinum is one backbone component, so effects cannot be attributed to platinum alone.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01089088](https://clinicaltrials.gov/study/NCT01089088) | Phase 2 | Completed | 63 | Single-arm trial of cisplatin + gemcitabine + sunitinib as first-line therapy for advanced urothelial carcinoma |
| [NCT00028756](https://clinicaltrials.gov/study/NCT00028756) | Phase 3 | Completed | 285 | Immediate vs deferred adjuvant chemotherapy after radical cystectomy for stage III/IV bladder carcinoma |
| [NCT01993979](https://clinicaltrials.gov/study/NCT01993979) | Phase 3 | Unknown | 261 | POUT: 4 cycles of adjuvant platinum-based chemotherapy vs surveillance in upper tract urothelial cancer; primary endpoint disease-free survival |
| [NCT00055601](https://clinicaltrials.gov/study/NCT00055601) | Phase 2 | Completed | 97 | Randomized trial of paclitaxel + cisplatin vs 5-FU + cisplatin with radiation in muscle-invading bladder cancer |
| [NCT00645593](https://clinicaltrials.gov/study/NCT00645593) | Phase 2 | Completed | 89 | Gemcitabine + cisplatin with or without cetuximab in urothelial carcinoma |
| [NCT00002684](https://clinicaltrials.gov/study/NCT00002684) | Phase 2 | Completed | 40 | Paclitaxel, cisplatin and ifosfamide in advanced, unresectable urothelial tumors |
| [NCT01261728](https://clinicaltrials.gov/study/NCT01261728) | Phase 2 | Completed | 57 | Neoadjuvant gemcitabine + cisplatin (4 cycles) before surgery in high-grade upper tract urothelial carcinoma |
| [NCT00003930](https://clinicaltrials.gov/study/NCT00003930) | Phase 1/2 | Completed | 84 | Transurethral surgery plus paclitaxel, cisplatin and twice-daily irradiation in muscle-invading bladder cancer |
| [NCT04871529](https://clinicaltrials.gov/study/NCT04871529) | Phase 2 | Terminated | 6 | Neoadjuvant gemcitabine + avelumab + carboplatin in cisplatin-ineligible muscle-invasive disease; stopped early, little evidentiary weight |
| [NCT04700124](https://clinicaltrials.gov/study/NCT04700124) | Phase 3 | Completed | 808 | Perioperative enfortumab vedotin + pembrolizumab vs neoadjuvant gemcitabine + cisplatin. The experimental arm is non-platinum, so the trial only reflects the current treatment landscape |

---

## Literature Evidence

Of the 20 linked publications, the 10 most relevant are listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32145825](https://pubmed.ncbi.nlm.nih.gov/32145825/) | 2020 | RCT | Lancet | POUT trial: phase 3 randomized trial assessing systemic platinum-based adjuvant chemotherapy in upper tract urothelial carcinoma after nephroureterectomy |
| [37071838](https://pubmed.ncbi.nlm.nih.gov/37071838/) | 2023 | RCT | J Clin Oncol | JAVELIN Bladder 100: updated follow-up of avelumab maintenance in patients after first-line platinum-containing chemotherapy (platinum is the preceding standard) |
| [36967359](https://pubmed.ncbi.nlm.nih.gov/36967359/) | 2023 | Guideline | Eur Urol | EAU 2023 guideline update on upper urinary tract urothelial carcinoma |
| [34861372](https://pubmed.ncbi.nlm.nih.gov/34861372/) | 2022 | Guideline | Ann Oncol | ESMO clinical practice guideline for bladder cancer diagnosis, treatment and follow-up |
| [38702396](https://pubmed.ncbi.nlm.nih.gov/38702396/) | 2024 | Review | Nat Rev Urol | Cisplatin-based chemotherapy is first-line standard for metastatic urothelial cancer, but up to 50% of patients are cisplatin-ineligible |
| [40478748](https://pubmed.ncbi.nlm.nih.gov/40478748/) | 2025 | Review | CA Cancer J Clin | Perioperative considerations in urothelial carcinoma, including advances in non-platinum-based therapies |
| [40782344](https://pubmed.ncbi.nlm.nih.gov/40782344/) | 2025 | Review | Cancer | Top five bladder cancer advances of 2024, including perioperative immunotherapy and a new first-line metastatic standard of care |
| [38244927](https://pubmed.ncbi.nlm.nih.gov/38244927/) | 2024 | Phase 2 trial | Ann Oncol | TROPHY-U-01: sacituzumab govitecan in metastatic urothelial carcinoma progressing after platinum chemotherapy and checkpoint inhibitors |
| [39536751](https://pubmed.ncbi.nlm.nih.gov/39536751/) | 2024 | Phase 1b/2 trial | Cell Rep Med | Pembrolizumab plus platinum-based chemotherapy in 15 patients with small cell bladder or small cell/neuroendocrine prostate cancer; overall response rate 43% |
| [28982752](https://pubmed.ncbi.nlm.nih.gov/28982752/) | 2017 | Review | J Natl Compr Canc Netw | Survival in metastatic urothelial carcinoma plateaued with platinum chemotherapy, leading to the immunotherapy era |

---

## US Market Information

All 13 licenses are for "Platinum Metallicum" from Hahnemann Laboratories, INC. The records give no authorization number and no approved indication text. The 5 listed licenses are identical.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not listed | Platinum Metallicum | Pellet | Not stated |
| Not listed | Platinum Metallicum | Pellet | Not stated |
| Not listed | Platinum Metallicum | Pellet | Not stated |
| Not listed | Platinum Metallicum | Pellet | Not stated |
| Not listed | Platinum Metallicum | Pellet | Not stated |

Dosage forms recorded across all licenses are pellet and liquid, both under the "Other" route category. Platinum chemotherapy for bladder cancer is intravenous, so route compatibility has not been established.

---

## Cytotoxicity

This section describes the class of platinum-based chemotherapy compounds used in the trials, such as cisplatin and carboplatin. It does not describe the marketed pellet products. Values are class-level and were not drawn from DrugBank toxicity data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum-based DNA-crosslinking agents) |
| Myelosuppression Risk | Medium to High (more prominent with carboplatin) |
| Emetogenicity Classification | High for cisplatin; Moderate for carboplatin |
| Monitoring Items | CBC with differential, renal function (nephrotoxicity is a key concern with cisplatin), electrolytes, liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Platinum-based chemotherapy is established standard care in urothelial carcinoma. The linked evidence includes completed Phase 3 trials, an RCT (POUT) and major guidelines. However, that evidence concerns platinum compounds such as cisplatin and carboplatin, and most trials test combination regimens. It does not concern the marketed elemental platinum pellet and liquid products.

**To proceed, the following is needed:**
- Confirm which chemical entity DB12257 represents and whether the trial evidence applies to it
- Obtain mechanism-of-action data (MOA) and package insert warnings and contraindications, which are currently missing
- Establish route and formulation compatibility, since the marketed forms are non-intravenous
- Retrieve US authorization numbers and approved indication text for the 13 licenses
- Confirm platinum-specific efficacy where platinum is only one component of a combination regimen

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

