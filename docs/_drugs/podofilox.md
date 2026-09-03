---
layout: default
title: Podofilox
parent: 僅模型預測 (L5)
nav_order: 1057
evidence_level: L5
indication_count: 10
---

# Podofilox
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

# Podofilox: From Anogenital Warts to Vulvovaginal Candidiasis

## One-Sentence Summary

Podofilox (DB01179) is the active antimitotic component of podophyllotoxin-based topical treatments, historically used against anogenital warts (HPV-related condyloma acuminata). The TxGNN model's top-ranked prediction is **vulvovaginal candidiasis**, but this is supported by only **1 non-specific literature reference** and **0 clinical trials**, with the evidence pack's own mechanistic review explicitly flagging the link as unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from TFDA/US license data (drug not marketed); literature within this evidence pack (see rank-3 candidate) indicates historical use for anogenital warts (condyloma acuminata) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank (flagged as a High-severity data gap, DG002). Based on the analysis embedded in this evidence pack, podofilox acts as an **antimitotic / microtubule inhibitor**, arresting cell division in rapidly proliferating epithelium — this is the mechanism thought to underlie its efficacy against HPV-driven wart tissue. It has **no known antifungal activity**.

Vulvovaginal candidiasis is a fungal infection requiring an antifungal mechanism (e.g., azole or polyene action on fungal cell membranes), which is mechanistically unrelated to microtubule inhibition. The sole supporting reference (PMID 10537386) is a 1999 general review of STD treatment that discusses vaginal discharge, genital warts, and other conditions within the same article — this is **topical co-occurrence, not evidence that podofilox treats candidiasis**. The evidence pack's own rationale explicitly labels this as "無合理機轉" (no reasonable mechanism) and classifies it as embedding noise rather than a genuine signal.

Notably, a lower-ranked candidate in this same batch — human papillomavirus infection (rank 3) — is supported by substantial direct clinical literature (e.g., PMID 8192173, a controlled study of 0.5% podofilox in anogenital warts; PMID 8245513, mechanistic regression data in papilloma models). This suggests the model correctly recovers podofilox's known clinical use elsewhere in its output, while the top-ranked candidate here reflects noise, likely amplified by structural embedding overlap with related podophyllotoxin derivatives (e.g., etoposide) seen throughout this candidate's other predictions (herpes zoster, tongue neoplasm, hypopharyngeal neoplasm, etc.).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10537386](https://pubmed.ncbi.nlm.nih.gov/10537386/) | 1999 | Review | American Family Physician | General review of STD treatment (1998 CDC guidelines); covers vaginal discharge, genital warts, and other conditions in separate sections — does not directly evaluate podofilox for candidiasis |

## US Market Information

No regulatory license records are available. The drug's market status is recorded as **not marketed**, with 0 total licenses on file.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score (99.47%) but is backed by zero clinical trials and a single non-specific review article that does not directly address podofilox in candidiasis. The pack's own mechanistic analysis confirms no plausible pharmacological link (antimitotic vs. antifungal mechanisms), so this should not proceed as a repurposing candidate at this time.

**To proceed, the following is needed:**
- DrugBank/label-confirmed mechanism of action (currently a data gap, DG002)
- TFDA/FDA-equivalent warnings and contraindications (currently a Blocking data gap, DG001)
- Any direct preclinical or clinical evidence specifically testing podofilox against *Candida* species
- Consider re-scoping evaluation toward the rank-3 candidate (human papillomavirus infection), which is supported by direct clinical trial and literature evidence and more closely reflects podofilox's established pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

