---
layout: default
title: Cefoxitin
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Cefoxitin
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

# Cefoxitin: From Broad-Spectrum Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefoxitin is a semisynthetic cephamycin (second-generation cephalosporin) antibiotic, historically used for surgical prophylaxis and treatment of mixed bacterial infections including intra-abdominal, gynecological, and soft-tissue infections.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
but currently only **0 clinical trials** and **2 publications** touch on this direction — placing the evidence at an early, pre-clinical stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No active US licenses found in current regulatory data |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmaceutical knowledge, cefoxitin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs). Its distinguishing feature is robust stability against many beta-lactamases, giving it broader Gram-negative and anaerobic coverage — including activity against *Bacteroides fragilis* — that is uncommon among older-generation cephalosporins.

Infectious otitis media is predominantly caused by *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. Cefoxitin's antibacterial spectrum offers limited and inconsistent coverage against these typical pathogens compared to first-line agents such as amoxicillin or amoxicillin-clavulanate. The only direct literature linking cefoxitin to otitis media involves rare nontuberculous mycobacterial (NTM) infections — specifically *Mycobacterium fortuitum* — where cefoxitin plays a supporting role in multi-drug combination regimens. This is a highly niche scenario, not representative of common otitis media etiology.

The TxGNN model's high score (99.30%) most likely reflects broad antibiotic–infection co-occurrence patterns embedded in the knowledge graph, rather than strong mechanistic alignment with the typical pathogens responsible for infectious otitis media. Without direct clinical evidence or a compelling mechanistic rationale for common-pathogen coverage, this prediction does not currently support clinical translation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cefoxitin in Infectious Otitis Media.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8783722](https://pubmed.ncbi.nlm.nih.gov/8783722/) | 1996 | Case Report + Literature Review | Clinical Infectious Diseases | Reviews 5 cases of *M. fortuitum* otitis media and mastoiditis; cefoxitin discussed as part of multi-drug NTM combination therapy; notably, the index case showed high-level amikacin resistance, making cefoxitin an alternative — not a primary — agent in this rare NTM context |
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Narrative Review | Infection and Drug Resistance | Broad MRSA epidemiology review that lists otitis media among MRSA clinical manifestations; cefoxitin appears in the context of the cefoxitin disk diffusion test as a surrogate marker for MRSA screening — a diagnostic role, not a therapeutic one |

---

## US Market Information

No active US drug authorizations (NDAs) for Cefoxitin were identified in the current regulatory dataset. The drug is classified as **Not Marketed** under current data.

> **Note:** Cefoxitin (brand name Mefoxin) was originally approved by the US FDA and has been available as a generic. The absence of NDA records in this dataset may reflect that the branded product is no longer actively marketed. Pharmacists should verify current availability and labeling through official FDA resources (e.g., DailyMed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for cefoxitin specifically in infectious otitis media is limited to 2 publications — neither demonstrating direct clinical efficacy against the common causative organisms of typical bacterial otitis media. The mechanistic rationale is weak for standard presentations and only marginally applicable in rare NTM-associated ear infections, which represent an extremely narrow clinical niche.

**Broader Context Worth Noting:**
Among the top-10 TxGNN predictions for cefoxitin, two other indications show meaningfully stronger evidence and clearer mechanistic rationale:
- **Urinary Tract Infection (rank #2, L3):** Two direct Phase 4 trials were conducted specifically testing cefoxitin against ESBL-producing *E. coli* UTI, plus a 1979 intramuscular clinical use record. Both trials terminated early due to enrollment difficulties — not therapeutic failure — suggesting further study may be warranted.
- **Gonococcal Urethritis (rank #6, L3):** Multiple comparative clinical trials from 1979–1987 directly validated cefoxitin's efficacy against *N. gonorrhoeae*, including penicillinase-producing strains (PPNG), with cure rates exceeding 95%. This represents the strongest historical clinical evidence in the dataset.

**To proceed with further evaluation, the following is needed:**
- Mechanism of action data (MOA) retrieved from DrugBank or the current FDA-approved labeling
- Complete safety profile: warnings, contraindications, and drug–drug interactions from the package insert
- Clarification of the specific otitis media subtype and pathogen of interest (NTM-related vs. typical bacterial)
- For UTI and gonococcal urethritis indications: updated susceptibility surveillance data to assess whether cefoxitin remains active against contemporary resistant strains
- Review of current CDC/IDSA treatment guidelines to understand positioning relative to modern standard-of-care agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

