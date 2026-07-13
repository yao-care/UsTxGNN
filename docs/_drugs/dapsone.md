---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 569
evidence_level: L5
indication_count: 1
---

# Dapsone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dapsone: From Leprosy to Pneumocystosis

## One-Sentence Summary

Dapsone is a sulfone-class antimicrobial and antiprotozoal agent historically used as a first-line treatment for leprosy and dermatitis herpetiformis, though it carries no current US regulatory registration in this dataset.
The TxGNN model predicts it may be effective for **pneumocystosis** (Pneumocystis jirovecii pneumonia, PJP), with **14 clinical trials** and **19 publications** currently supporting this direction.
Notably, this prediction is among the strongest model validations in the dataset: multiple completed Phase 3 RCTs from the 1990s AIDS era independently confirm dapsone's established efficacy for both PCP prophylaxis and treatment, with Level 1 guideline endorsement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Leprosy / Dermatitis herpetiformis (inferred from literature; no US license found in this dataset) |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii Pneumonia) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| US Market Status | Not registered in this dataset |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although the formal mechanism of action (MOA) field is flagged as a data gap in this evidence pack, the mechanistic basis is clearly established in published literature and the repurposing rationale. Dapsone is a sulfone-class compound with dual antimicrobial and anti-inflammatory properties. It inhibits **dihydropteroate synthase (DHPS)** in *Pneumocystis jirovecii*, thereby blocking the organism's de novo folate synthesis pathway. When combined with trimethoprim or pyrimethamine, dapsone creates a **bi-sequential folate blockade** — simultaneously inhibiting two consecutive steps in folate biosynthesis — producing synergistic anti-PCP activity. This is pharmacologically analogous to the same DHPS-inhibition mechanism that underlies dapsone's antibacterial efficacy in leprosy, making the mechanistic extrapolation both direct and well-validated. The TxGNN score of 0.9973 reflects the high connectivity strength of this mechanistic link within the knowledge graph.

The connection between leprosy (a mycobacterial infection) and pneumocystosis (an opportunistic fungal/protozoal pneumonia) is not through disease similarity, but through shared **pathway pharmacology**: both pathogens depend on de novo folate biosynthesis, a pathway absent in mammalian cells. This selectivity makes DHPS inhibition an effective and well-tolerated target. Dapsone is efficiently absorbed orally (70–80% bioavailability), reaches peak serum levels in 2–6 hours, and distributes adequately into alveolar fluid — a pharmacokinetic profile well-suited for treating pulmonary infections.

Importantly, the TxGNN prediction is not speculative: it directly recovers a decades-old clinical observation. Multiple Phase 3 RCTs conducted during the 1990s AIDS epidemic demonstrated dapsone's efficacy for PCP prophylaxis (versus pentamidine and atovaquone) and for PCP treatment (dapsone/trimethoprim versus TMP/SMX). The 2016 ECIL-5 clinical guidelines and a 2024 network meta-analysis both formally position dapsone-based regimens as established alternatives to TMP/SMX. In this context, the model's high-confidence prediction serves as strong validation of TxGNN's predictive architecture, while simultaneously identifying dapsone as a repurposing candidate worth evaluating in broader immunocompromised populations beyond HIV — including solid organ transplant recipients and patients with haematological malignancies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Largest direct RCT comparing daily dapsone vs. atovaquone for PCP prophylaxis in HIV patients (CD4 ≤200/mm³) intolerant to TMP/sulfonamides; established comparative efficacy and safety benchmarks for dapsone |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three-arm RCT comparing anti-PCP regimens (including dapsone) plus zidovudine for primary prevention in advanced HIV (CD4 <200/mm³); multi-arm design provides cross-agent comparative efficacy data |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Head-to-head comparison of aerosolized pentamidine vs. thrice-weekly dapsone for PCP prophylaxis in HIV patients intolerant to trimethoprim/sulfonamides; directly established dapsone as a viable prophylaxis alternative |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim vs. clindamycin/primaquine vs. TMP/SMX for treatment of mild-to-moderate PCP in AIDS; evaluates dapsone combination in the active treatment setting, not just prophylaxis |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3,130 | Largest enrolled study to date evaluating prospective HLA-B*1301 genetic screening to reduce dapsone hypersensitivity syndrome (DHS) incidence; covers PCP and other dapsone indications — status unknown, result availability uncertain |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | Completed | 168 | Case-control study on PCP risk factors and PCR use after allogeneic HSCT; dapsone prophylaxis arm showed incidence up to 7.2%, providing real-world safety signal for low-dose regimens in transplant settings |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Pediatric PCP prophylaxis: daily vs. weekly oral dapsone in HIV-infected infants and children; established pediatric pharmacokinetics, breakthrough rate, and safety in this population |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | Completed | N/A | Dose-optimization study comparing dapsone 100 mg vs. 50 mg for primary PCP prophylaxis in AIDS-related complex patients; addressed long-term tolerability and optimal dosing for this indication |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | N/A | Randomized comparison of dapsone + trimethoprim vs. TMP/SMX for first-episode PCP treatment in AIDS patients; assessed treatment response rate, adverse effect rates, and suitability for outpatient management |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | Pilot study of clindamycin-TMP/SMX for severe PCP after solid organ transplantation; formally identifies dapsone as a recognized second-line alternative when TMP-SMX fails — supports evidence of real-world use beyond HIV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Network Meta-Analysis | Clin Microbiol Infect | Systematic review + NMA of RCTs comparing all PCP prophylaxis regimens (TMP-SMX, dapsone-based, aerosolized pentamidine, atovaquone) in people living with HIV; provides quantitative comparative efficacy and safety rankings — most comprehensive recent synthesis |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Network Meta-Analysis | Clin Microbiol Infect | NMA of RCTs for PCP treatment regimens in PLHIV; positions dapsone-containing combinations in the therapeutic hierarchy relative to TMP-SMX and other alternatives |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Clinical Guideline | J Antimicrob Chemother | ECIL-5 evidence-based recommendations for PCP prophylaxis in haematological malignancies and HSCT recipients; formally endorses TMP/SMX as first-line and dapsone as an alternative when TMP-SMX is contraindicated (Grade A-II recommendation) |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Drug Review | Clin Infect Dis | Definitive dapsone-specific review covering in vitro anti-PCP activity, animal studies, and clinical trials; confirms DHPS inhibition mechanism, 70–80% oral bioavailability, adequate alveolar distribution, and synergistic effects with trimethoprim/pyrimethamine |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Narrative Review | Expert Opin Pharmacother | Contemporary review of PCP pathogen biology, risk factors across HIV and non-HIV populations (transplant, rheumatologic conditions), and full range of prophylaxis and treatment options including dapsone regimens |
| [39603840](https://pubmed.ncbi.nlm.nih.gov/39603840/) | 2025 | Retrospective Study | Transplant Infect Dis | Real-world analysis of atovaquone and dapsone as TMP-SMX alternatives for PJP prophylaxis in solid organ transplant recipients; addresses the critical evidence gap in non-HIV immunocompromised populations |
| [1727534](https://pubmed.ncbi.nlm.nih.gov/1727534/) | 1992 | Narrative Review | Med Clin North Am | Landmark review establishing that PCP is "almost entirely preventable and eminently treatable"; foundational historical context for the prophylaxis guidelines that subsequently incorporated dapsone |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Drug Review | Dermatol Clin | Pharmacology review of dapsone and sulfapyridine describing dual antimicrobial and anti-inflammatory mechanisms; summarizes dapsone's established role in PCP prophylaxis for HIV patients and its toxicity profile |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case Series | Ann Pharmacother | Case of methemoglobinemia in a patient receiving dapsone for PCP prophylaxis; documents the most clinically significant adverse effect requiring active monitoring during dapsone therapy |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Case Report | Cureus | Dapsone-induced hypoxia secondary to methemoglobinemia in a patient treated for PCP/toxoplasmosis; reinforces the need for clinical suspicion and oximetry monitoring in all patients on dapsone |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dapsone's efficacy against pneumocystosis is substantiated by multiple completed Phase 3 RCTs, endorsed in ECIL-5 clinical guidelines, and confirmed by a 2024 network meta-analysis — placing this candidate at the highest evidence level (L1). The TxGNN prediction is not speculative but rather a validated recovery of a well-documented clinical indication, lending exceptional confidence to the mechanistic and clinical signal. The primary constraints are regulatory (no US registration found in this dataset) and safety data gaps rather than efficacy uncertainty.

**To proceed, the following is needed:**

- **Safety profile extraction**: Retrieve formal warnings, contraindications, and boxed warnings from the US package insert (FDA Orange Book / DailyMed) — blocking gap identified in this evidence pack
- **MOA formal documentation**: Query DrugBank API (DB00250) to populate the mechanism of action field for downstream pharmacological analysis
- **US FDA registration verification**: Dapsone has historical FDA approvals (e.g., for dermatitis herpetiformis; Aczone gel for acne); NDA numbers should be confirmed via FDA Orange Book and the 0-license finding investigated
- **DDI profile**: Conduct formal drug interaction query — known interactions include rifampicin (reduces dapsone levels), probenecid (increases dapsone levels), trimethoprim (increases monoacetyldapsone metabolite), and folic acid antagonists
- **Methemoglobinemia monitoring protocol**: Establish G6PD screening before initiation and pulse oximetry monitoring plan for clinical use, given documented adverse event signal in evidence
- **HLA-B\*1301 screening consideration**: Evaluate applicability, especially for Asian patient populations, based on NCT02550080 findings when results become available
- **Non-HIV population scoping**: Define target patient populations beyond HIV (solid organ transplant, haematological malignancy, autoimmune disease on biologics) where TMP-SMX is contraindicated and dapsone provides a validated alternative
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

