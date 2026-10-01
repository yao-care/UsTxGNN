---
layout: default
title: Dapsone
parent: High Evidence (L1-L2)
nav_order: 569
evidence_level: L1
indication_count: 1
---

# Dapsone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Dapsone: From Leprosy and Dermatitis Herpetiformis to Pneumocystosis

## One-Sentence Summary

Dapsone is a sulfone antibacterial and anti-inflammatory drug, historically a mainstay for leprosy and dermatitis herpetiformis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (*Pneumocystis jirovecii* pneumonia, PCP), with a score of 99.73%.
This direction is supported by **14 clinical trials** (4 completed Phase 3 trials) and **19 publications**, including two network meta-analyses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy and dermatitis herpetiformis (from the literature; the US label text is not in the record) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (all five listed below are ANDAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record. Based on the published pharmacology, dapsone inhibits dihydropteroate synthase (DHPS) in the microbial folate synthesis pathway. This is the same target as sulfonamides such as sulfamethoxazole. A 1998 review (PMID 9675476) reports that dapsone blocks folic acid synthesis in *Pneumocystis* through this route. It also reports strong anti-*Pneumocystis* activity in vitro, in animal studies and in clinical trials.

Dapsone's original uses are antimicrobial (leprosy) and anti-inflammatory (dermatitis herpetiformis). The PCP indication relies on the antimicrobial side. *Pneumocystis jirovecii* carries a DHPS enzyme, so the drug's action against leprosy bacteria carries over mechanistically. Dapsone is used alone or with trimethoprim or pyrimethamine for prophylaxis and for mild-to-moderate PCP. In practice it is mainly an alternative for patients who cannot take trimethoprim-sulfamethoxazole (TMP-SMX).

The very high TxGNN score agrees with this established pharmacology and with a large body of clinical trial work. This is therefore closer to confirming an already-used indication than to discovering a new one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Daily dapsone vs daily atovaquone for PCP prophylaxis in HIV patients intolerant of TMP-SMX |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Thrice-weekly dapsone vs monthly aerosolized pentamidine for PCP prophylaxis in TMP-SMX-intolerant HIV patients |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim and clindamycin/primaquine vs TMP-SMX for mild-to-moderate PCP in AIDS |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three anti-Pneumocystis agents plus zidovudine for primary prevention in advanced HIV (arm composition, likely including dapsone, should be confirmed) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | Completed | Not reported | Dapsone 100 mg vs 50 mg as primary PCP prophylaxis; also assesses long-term tolerability |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly oral dapsone for PCP prophylaxis in HIV-infected children; toxicity and pharmacokinetics |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate/leucovorin plus dapsone vs TMP-SMX for moderately severe PCP; small sample, dapsone effect not separable |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | Not reported | Dapsone vs TMP-SMX for the first episode of PCP in AIDS; effectiveness and adverse effects |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | Clindamycin plus TMP-SMX for PCP after solid organ transplant; dapsone is mentioned only as a second-line alternative |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | Completed | 168 | Case-control study of PCP risk factors after allogeneic HSCT; notes a higher PCP incidence (up to 7.2%) with low-dose dapsone |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Network meta-analysis of RCTs | Clin Microbiol Infect | Compares PCP prophylaxis regimens in people with HIV, including dapsone-based regimens, TMP-SMX, aerosolized pentamidine and atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Network meta-analysis of RCTs | Clin Microbiol Infect | Compares PCP treatment regimens in people with HIV; TMP-SMX remains the primary treatment |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline (ECIL-5) | J Antimicrob Chemother | Evidence-based PCP prophylaxis recommendations for haematological malignancy and stem cell transplant patients; TMP-SMX is the drug of choice |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clin Infect Dis | Dapsone blocks folate synthesis via DHPS and has strong anti-*Pneumocystis* activity, alone or with trimethoprim/pyrimethamine |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | Overview of PCP risk factors, prevention and treatment |
| [39603840](https://pubmed.ncbi.nlm.nih.gov/39603840/) | 2025 | Article | Transplant Infect Dis | Atovaquone and dapsone are often used as TMP-SMX alternatives in solid organ transplant despite limited data |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | Pharmacokinetic/safety study | Antimicrob Agents Chemother | Weekly dapsone ± pyrimethamine in HIV patients; maximum tolerated weekly dose was 200 mg in patients on at least 500 mg/day zidovudine |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Review (drug monograph) | Dermatol Clin | Dapsone is the most important leprosy drug, is useful for PCP prophylaxis in HIV, and is the treatment of choice for dermatitis herpetiformis |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | Retrospective chart review | Pediatr Transplant | Methemoglobinemia in pediatric kidney recipients on dapsone PCP prophylaxis |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report | Ann Pharmacother | Methemoglobinemia in a patient on dapsone for PCP prophylaxis |

---

## US Market Information

The record lists 20 licenses; the 5 main ones are shown below. Approved indication text is not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA086841 | Dapsone | Tablet | Westminster Pharmaceuticals, LLC |
| ANDA086842 | Dapsone | Tablet | Westminster Pharmaceuticals, LLC |
| ANDA206505 | Dapsone | Tablet | ANI Pharmaceuticals, Inc. |
| ANDA203887 | Dapsone | Tablet | Golden State Medical Supply, Inc. |
| ANDA215718 | Dapsone | Gel (topical) | Alembic Pharmaceuticals Inc. |

An oral tablet is the relevant dosage form for a systemic infection such as PCP. The topical gel is not suitable for this use.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the query.

Package insert warnings and contraindications are not in the record. Please refer to the package insert for safety information.

Signals reported in the supplied literature:
- **Methemoglobinemia**: Reported in PCP prophylaxis, including hypoxia (PMID 32714715) and pediatric kidney transplant recipients (PMIDs 33280223, 9606476).
- **Hepatic complications**: Dapsone-induced liver injury is described as a concern beyond methemoglobinemia (PMID 31631707).
- **Photosensitivity dermatitis**: Rare cases reported (PMID 18309716).
- **Hypersensitivity syndrome**: NCT02550080 (n=3,130) tests prospective HLA-B*13:01 screening to reduce the incidence of dapsone hypersensitivity syndrome.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four completed Phase 3 trials (NCT00000802, NCT00001028, NCT00000640, NCT00000991) and two recent network meta-analyses support dapsone for PCP, and the mechanism (DHPS inhibition) is well characterized. Dapsone is mainly positioned as an alternative for patients who cannot take TMP-SMX. The guardrails come from the missing label safety data and the known hematologic and hypersensitivity risks.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications, approved indications) to complete the safety screening
- Confirmation of the arm composition of NCT00000991, and full-text review of the two network meta-analyses for dapsone-specific efficacy estimates
- A safety monitoring plan covering methemoglobinemia, hemolysis and liver function, plus consideration of hypersensitivity risk screening
- Confirmation that an oral tablet product fits the intended PCP use, and mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

