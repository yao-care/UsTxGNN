---
layout: default
title: Dapsone
parent: High Evidence (L1-L2)
nav_order: 569
evidence_level: L1
indication_count: 1
monitor_inn: "DAPSONE"
predicted_indications: ["pneumocystosis"]
last_modified_at: 2026-10-14
description: "Dapsone: predicted new indication Pneumocystosis (evidence level L1). Approved use: Dermatitis herpetiformis, acne, leprosy"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Dapsone: From Dermatitis Herpetiformis, Acne and Leprosy to Pneumocystosis

## One-Sentence Summary

Dapsone was originally used to treat dermatitis herpetiformis, acne and leprosy.
The TxGNN model predicts it may be effective for **pneumocystosis (Pneumocystis pneumonia, PCP)**,
with **10 clinical trials** and **20 publications** currently supporting this direction, including 4 completed Phase 3 trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis herpetiformis, acne, leprosy (from the knowledge graph; no approved-indication text is available from US labels) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| US Market Status | Cancelled only (all 15 authorizations are cancelled) |
| Number of NDAs | 15 authorizations in total (2 NDAs and 13 ANDAs) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, dapsone is a sulfone antibacterial that inhibits dihydropteroate synthase in the folate synthesis pathway, the same target as sulfonamides such as sulfamethoxazole. This mechanism has not been verified against the supplied data and should be confirmed from a primary source.

*Pneumocystis jirovecii* depends on this folate pathway. That explains why dapsone has activity as prophylaxis, and, combined with trimethoprim, as treatment of mild-to-moderate PCP. Dapsone's established uses (leprosy, an infection, and dermatitis herpetiformis) show both antimicrobial and anti-inflammatory activity. The very high TxGNN score is consistent with this mechanistic rationale.

The clinical trial record supports the prediction. Dapsone has been tested against atovaquone, aerosolized pentamidine and trimethoprim-sulfamethoxazole in HIV-related PCP, and a review (PMID 11155588) notes that it is useful for PCP prophylaxis in HIV disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Daily dapsone vs daily atovaquone for PCP prophylaxis in HIV patients intolerant of trimethoprim/sulfonamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three anti-Pneumocystis regimens plus zidovudine for primary prevention in advanced HIV |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Monthly aerosolized pentamidine vs thrice-weekly dapsone for PCP prophylaxis |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim and clindamycin/primaquine vs TMP/SMX for mild-to-moderate PCP |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly oral dapsone for PCP prophylaxis in HIV-infected children (toxicity and pharmacokinetics) |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate with leucovorin plus dapsone vs TMP/SMX for moderately severe PCP (safety and pharmacokinetics) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | Not specified | Completed | Not reported | Dapsone 100 mg vs 50 mg as primary PCP prophylaxis in AIDS-related complex |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | Not specified | Completed | Not reported | Randomized comparison of dapsone plus trimethoprim vs TMP/SMX for first-episode PCP in AIDS |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3130 | HLA-B*1301 genetic screening to reduce dapsone hypersensitivity syndrome (safety-related; indirect link to PCP) |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Phase 4 | Withdrawn | 0 | Oral corticosteroids in PCP; not about dapsone and generated no data |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares PCP prophylaxis regimens in people with HIV, including dapsone-based regimens, TMP-SMX, aerosolized pentamidine and atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares treatment regimens for PCP in people with HIV; TMP-SMX remains the primary treatment |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline | J Antimicrob Chemother | ECIL-5 recommendations for PCP prophylaxis in haematological malignancy and stem cell transplant; TMP-SMX is the drug of choice |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | Review of PCP prevention and treatment in immunocompromised hosts |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Review | Dermatol Clin | Dapsone is the key drug for leprosy and dermatitis herpetiformis and is useful for PCP prophylaxis in HIV |
| [1531191](https://pubmed.ncbi.nlm.nih.gov/1531191/) | 1992 | Review | Chest | Trimethoprim-dapsone is among the options for mild-to-moderate PCP |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | Overview of PCP in immunocompromised patients |
| [7937279](https://pubmed.ncbi.nlm.nih.gov/7937279/) | 1994 | Review | Pharmacotherapy | PCP prophylaxis options during pregnancy, including dapsone |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report | Ann Pharmacother | Methemoglobinemia in a patient receiving dapsone for PCP prophylaxis |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Case report | Cureus | Hypoxia from dapsone-induced methemoglobinemia |

## US Market Information

All 15 US authorizations for dapsone are cancelled; none is currently valid. The five below are representative.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021794 | Dapsone (Pacific Pharma) | Gel | Not available (cancelled) |
| NDA207154 | Aczone (Almirall) | Gel | Not available (cancelled) |
| ANDA086841 | Dapsone (Westminster) | Tablet | Not available (cancelled) |
| ANDA086842 | Dapsone (Westminster) | Tablet | Not available (cancelled) |
| ANDA206505 | Dapsone (ANI) | Tablet | Not available (cancelled) |

Oral tablets and topical gels have both been marketed. Only the oral form is relevant to PCP.

## Safety Considerations

- **Contraindications and disease associations (knowledge graph, not label text)**: G6PD deficiency, methemoglobinemia due to methemoglobin reductase deficiency, anemia (including macrocytic anemia), liver disease, gallbladder disease, glycogen storage disease, cystinuria, galactosemia, and pyruvate dehydrogenase E3 deficiency.
- **Safety signals in the literature**: methemoglobinemia and hypoxia (PMID 9606476, 32714715), acute pancreatitis (PMID 14519046), and falsely lowered HbA1c in a diabetic patient (PMID 22370290). Dapsone hypersensitivity syndrome is also addressed by trial NCT02550080 (HLA-B*1301 screening).
- **Drug interactions**: 100 interactions were identified in total. Those listed as moderate include aprepitant, metronidazole, picosulfuric acid, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, activated charcoal and troglitazone. Others, such as pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, morphine, sucralfate, rosiglitazone, calcitriol and vancomycin, have an unknown severity level.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four completed Phase 3 trials (700, 600, 400 and 290 participants) evaluated dapsone-containing regimens for PCP prophylaxis or treatment, and two recent network meta-analyses address these regimens. Guidelines still favor TMP-SMX as first choice, so dapsone fits as an alternative for patients intolerant of sulfonamides. Its known hematologic risks and the cancellation of all US authorizations call for guardrails.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap), obtained from the FDA website
- Verified mechanism of action data from DrugBank
- G6PD deficiency screening before use, and monitoring for methemoglobinemia and hemolysis
- A review of the 100 drug interactions against the intended co-medications
- Confirmation of product availability and formulation, since all US authorizations are cancelled
- Reading of the Phase 3 trial results (dapsone arm outcomes), since the data compiled here give only trial design summaries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

