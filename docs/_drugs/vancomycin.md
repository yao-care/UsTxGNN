---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 1283
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic historically used to treat serious Gram-positive bacterial infections (e.g., MRSA); this evidence pack does not contain a formal approved-indication text or MOA record for the drug (see Data Gaps below). TxGNN's top-ranked prediction is **Diffuse Scleroderma**, an autoimmune fibrotic disease, but the accompanying evidence review found **no supporting clinical trials** and only **1 tangentially related case-report publication**, with the mechanistic analysis explicitly judging the link **not pharmacologically plausible**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license/approved-indication text on file; drug is currently unmarketed in this jurisdiction) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for vancomycin in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, vancomycin is a glycopeptide antibiotic that inhibits bacterial cell-wall synthesis by binding the D-Ala-D-Ala terminus of peptidoglycan precursors in Gram-positive organisms — a mechanism with no known relevance to fibrotic or autoimmune connective-tissue disease.

Diffuse scleroderma is a fibrotic autoimmune disorder driven by aberrant fibroblast activation and collagen deposition, not by bacterial infection. The domain-expert rationale attached to this candidate explicitly states there is **no reasonable mechanistic link**: the only supporting literature is a case report of erythroderma with sepsis in which vancomycin was used to treat a secondary bacterial complication, not the underlying dermatologic/fibrotic condition itself. This strongly suggests the high TxGNN embedding score reflects a knowledge-graph artifact (over-generalized "antibiotic–skin/systemic disease" associations) rather than a biologically grounded repurposing signal.

Given the absence of mechanistic rationale, clinical trial evidence, and even the drug's own basic regulatory/MOA documentation, this candidate should be treated as a low-confidence, model-only signal rather than a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Case of exfoliative erythroderma with sepsis and eosinophilia; vancomycin was used as antimicrobial therapy for a secondary bacterial complication, not as treatment for the underlying dermatologic condition itself. No direct evidence for a scleroderma indication. |

---

## US Market Information

No marketing authorizations are on record for this drug in this evidence pack (Market Status: Not Marketed, 0 licenses/NDAs).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A Blocking-severity data gap (DG001) has been identified — regulatory warnings and contraindication text for this drug have not yet been retrieved, which prevents formal S1 safety screening.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Diffuse Scleroderma) has Evidence Level L5 (model prediction only) — no clinical trials support it, only one indirectly related case report exists, and the mechanistic review explicitly found no plausible pharmacological rationale linking vancomycin's antibacterial mechanism to a fibrotic autoimmune disease. Combined with the drug's unmarketed status and a Blocking-severity safety data gap, there is currently insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- Vancomycin's official warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A biologically grounded hypothesis connecting vancomycin's mechanism to scleroderma pathophysiology (currently absent)
- Preclinical or observational evidence beyond the single unrelated case report before any further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

