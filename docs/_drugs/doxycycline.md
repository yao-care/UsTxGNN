---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

Using the provided Evidence Pack, I've assembled the report below. Note on the data: `predicted_indications[0]` (highest TxGNN score) is *Punctate Epithelial Keratoconjunctivitis*, which per the template's extraction rules is the primary indication used for the title/overview — but this candidate has weak (L4/Hold) evidence. Because this is a "multi" candidate pack with 10 distinct disease predictions, I've followed the required template structure for the top-ranked candidate and added a supplementary section covering the other nine so the much stronger candidates (L1 and L2, "Proceed with Guardrails") aren't lost.

---

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline-class antibiotic; specific TFDA-approved indication text and mechanism-of-action data were not available in this evidence pack, and the drug currently holds **no marketing authorization** in the reviewed jurisdiction.
The TxGNN model's top-ranked prediction (by score) is **Punctate Epithelial Keratoconjunctivitis**, but this is currently supported by **0 clinical trials** and only **1 case-report-level publication**, with a mechanistic rationale that is weak-to-negative.
Ten disease candidates in total were evaluated for this drug — several others (post-bacterial disorder, chronic gingivitis) carry substantially stronger evidence and are summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (0 licenses on file; doxycycline is generally known as a broad-spectrum tetracycline-class antibacterial) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacology, doxycycline is a tetracycline-class antibiotic with established efficacy against *Chlamydia trachomatis* infection, and mechanistically this could theoretically extend to chlamydial follicular conjunctivitis and its corneal complications.

However, the single literature source available (Hardten et al., 1992) actually describes the opposite scenario: two patients developed **persistent, recurrent punctate epithelial keratitis after their chlamydial follicular conjunctivitis had already resolved** with oral tetracycline or doxycycline therapy. This suggests the corneal lesion may represent a **post-infectious, immune-mediated sequela** rather than active infection — meaning doxycycline's efficacy against the corneal pathology itself (as opposed to the underlying chlamydial infection) is unproven, and possibly not applicable once the lesion has developed. The mechanistic linkage for this specific indication is therefore weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Report | Cornea | Two cases of chlamydial follicular conjunctivitis treated with oral tetracycline/doxycycline (follicles resolved) subsequently developed recurrent, bilateral punctate corneal epithelial lesions with anterior stromal edema in one case — suggesting a post-infectious sequela not addressed by the antibiotic itself |

---

## US Market Information

Doxycycline currently holds **no marketing authorizations** on file in this evidence pack (`total_licenses = 0`, market status = 未上市/Not Marketed). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were all flagged as Data Gaps in this evidence pack — see Conclusion below for remediation.)

---

## Supplementary: Full Candidate List (10 Predicted Indications)

This evidence pack scored 10 disease candidates for doxycycline. The top-score candidate (above) has the weakest evidentiary support in the set; two other candidates below have substantially stronger evidence and warrant separate attention:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|----------------------|:-----------:|:---------------:|:---------------:|-----------------|------|
| 1 | Punctate epithelial keratoconjunctivitis | 99.94% | L4 | S0 | Hold | 1 case report; mechanistic link weak/negative |
| 2 | Otitis externa | 99.90% | L4 | S0 | Hold | 6/7 literature items are veterinary (canine); no human trials |
| 3 | Postinfectious vasculitis | 99.89% | L4 | S1 | Research Question | Plausible only if etiology is rickettsial (RMSF); case-report level only |
| 4 | Post-bacterial disorder | 99.89% | **L1** | S3 | **Proceed with Guardrails** | Largely aggregates *established* doxycycline uses (Lyme/erythema migrans, tick-borne relapsing fever, STI PrEP/PEP) — closer to on-label than true repurposing |
| 5 | Post-infectious syndrome | 99.89% | L2 | S2 | Research Question | Heterogeneous bucket (Q-fever fatigue syndrome, TB host-directed therapy, Kawasaki disease); needs sub-indication scoping |
| 6 | Infective urethral stricture | 99.88% | L4 | S0 | Hold | Antibiotics can prevent but not treat established fibrotic stricture |
| 7 | Chagas cardiomyopathy | 99.87% | L4 | S0 | Hold | Sole comparative study showed **no additive benefit** over benznidazole alone (negative finding) |
| 8 | Infection-related hemolytic uremic syndrome | 99.87% | L5 | S0 | Hold | No clinical trials or literature; model prediction only; theoretical toxin-release risk with antibiotics in STEC-HUS |
| 9 | Exposure keratitis | 99.79% | L4 | S0 | Hold | Likely poor disease-term mapping — exposure keratitis is mechanical/structural, not infectious |
| 10 | Chronic gingivitis | 99.77% | **L2** | S2 | **Proceed with Guardrails** | Reflects sub-antimicrobial-dose doxycycline (SDD/Periostat), an MMP-inhibition mechanism already used clinically as a periodontal adjunct in some markets |

**Note:** Candidates ranked #4 and #10 are the most clinically actionable in this set, but both are closer to *confirmatory* evidence for known/adjacent uses (established anti-infective indications, or an already-marketed sub-antimicrobial-dose formulation) than to a genuinely novel repurposing signal.

---

## Conclusion and Next Steps

**Decision: Hold** *(for the top TxGNN-ranked candidate, Punctate Epithelial Keratoconjunctivitis)*

**Rationale:**
- Evidence level is L4 (single case report), no clinical trials exist, and the only available literature suggests the corneal lesion may be a post-infectious sequela doxycycline does not resolve — the mechanistic case is weak-to-negative, and this candidate should not advance past S0.
- Two Blocking/High-severity data gaps (DG001: TFDA warnings/contraindications; DG002: MOA) also currently block any S1 safety pre-assessment for this drug regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse TFDA/regulatory package insert warnings and contraindications before any indication in this pack can clear S1.
- Resolve DG002 (High): obtain confirmed MOA data from DrugBank to support mechanistic-relevance analysis.
- If pursuing repurposing work on doxycycline, **redirect primary evaluation effort toward candidates #4 (post-bacterial disorder) and #10 (chronic gingivitis)**, which already carry L1/L2 evidence and "Proceed with Guardrails" recommendations, rather than the top-score-but-weakest-evidence candidate reported here.
- For candidate #5 (post-infectious syndrome), disaggregate the bucketed sub-indications (Q-fever fatigue syndrome vs. TB host-directed therapy vs. Kawasaki disease) into separate evidence packs, since they have materially different mechanistic bases and trial support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

