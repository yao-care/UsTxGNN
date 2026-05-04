---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 8
---

# Cefazolin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Cefazolin: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, widely established for surgical prophylaxis and treatment of susceptible gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**,
with **1 clinical trial** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No registration data available (known use: surgical prophylaxis, gram-positive bacterial infections) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| US Market Status | Not marketed (0 registered licenses) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), resulting in bactericidal activity. Its primary spectrum covers gram-positive organisms — particularly *Staphylococcus aureus* and *Streptococcus* species — as well as limited gram-negative coverage.

Infectious otitis media (AOM) is predominantly caused by *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. Cefazolin addresses the gram-positive component effectively, but faces a critical spectrum gap: *H. influenzae* is intrinsically resistant to first-generation cephalosporins, and *M. catarrhalis* exhibits high β-lactamase production rates — together accounting for 25–40% of pediatric AOM cases. This mechanistic mismatch limits cefazolin's utility as an empirical first-line agent.

Where cefazolin does show clinical relevance is in complicated AOM presentations. PMID 39567876 (2025) reports its use as part of a ceftazidime + cefazolin combination for Gradenigo Syndrome — a rare petrous apicitis complication of otitis media — where gram-positive coverage complements ceftazidime's gram-negative spectrum. This represents a niche combinational role rather than a standalone indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Double-blind, placebo-controlled RCT in children aged 6–23 months comparing 5-day vs. 10-day antibiotic courses for AOM, aimed at assessing antimicrobial resistance reduction strategies. Trial was terminated prior to completion; root cause of termination (efficacy failure, safety signal, or recruitment difficulty) has not been disclosed and represents a key negative signal. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Series | Annals of Otology, Rhinology & Laryngology | Ceftazidime + Cefazolin empiric combination for Gradenigo Syndrome (AOM-related petrous apicitis). Describes rationale for including cefazolin to cover *Staphylococcus* and *Streptococcus* in a complex otitis media complication. |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Medical Journal | Review of cephalosporin use in pediatric practice; notes efficacy of cephalosporins against gram-positive cocci in pediatric infections including ear infections, with discussion of spectrum and safety profile. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Case Series | Clinical Pharmacy | Stevens-Johnson syndrome case in a 2.5-year-old child treated with IV cefazolin (among other agents) for otitis media and upper airway infection. Documents incidental IV cefazolin use in a pediatric AOM context with subsequent adverse drug reaction workup. |

---

## US Market Information

No registered licenses or NDA records are available for Cefazolin in the current regulatory dataset (0 licenses). This likely reflects a data gap in the Evidence Pack rather than true non-availability, given cefazolin's extensive parenteral use in US clinical practice. Regulatory data should be verified directly via the FDA Orange Book or DailyMed before drawing conclusions about market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.44%), the available clinical evidence is limited to a single terminated Phase 2b trial and three publications of moderate-to-low quality (case series, a 1977 review). More critically, cefazolin's antimicrobial spectrum systematically misses the two most prevalent AOM pathogens (*H. influenzae* and *M. catarrhalis*), creating a fundamental mechanistic mismatch for empirical infectious otitis media treatment.

**To proceed, the following is needed:**

- **Termination root cause for NCT01511107** — if terminated for futility or a safety signal, this is a strong negative signal that should effectively close the infectious otitis media indication
- **Regulatory data verification** — confirm US FDA approved indications via Orange Book/DailyMed, as 0-license status appears to be a data gap
- **Formal MOA data from DrugBank** — complete the mechanistic link analysis with structured PBP-binding and spectrum data
- **Pathogen-stratified clinical evidence** — data on cefazolin's outcomes specifically in gram-positive AOM (e.g., MSSA-driven otitis media) to test whether a narrowed indication is viable
- **Package insert safety review** — key warnings, contraindications, and drug interactions must be evaluated before any S1 safety screening can proceed
- **Reconsider the primary investigation target** — Middle Ear Disease (rank 3, evidence level L2, "Proceed with Guardrails") has stronger evidence for surgical prophylaxis in otologic procedures, which aligns better with cefazolin's established clinical role and may represent a more productive repurposing direction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

