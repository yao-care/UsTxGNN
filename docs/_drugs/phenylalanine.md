---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 1041
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenylalanine: From No Approved Indication to Sclerosing Cholangitis

## One-Sentence Summary

> Phenylalanine is an essential amino acid with no approved therapeutic indication and no marketing authorization on file.
> The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**,
> but a review of the supporting evidence — **0 clinical trials** and **4 publications** — finds no data that actually support this claim.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — phenylalanine is an essential amino acid; no marketed drug license or approved indication text exists in the record |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for phenylalanine in this context. Based on known information, phenylalanine is a naturally occurring essential amino acid rather than a drug with an approved indication, so there is no established pharmacological rationale connecting it to sclerosing cholangitis.

A review of the four literature citations returned for this prediction finds none of them actually support a treatment relationship. One study (PMID 15790420) examines plasma tyrosine — not phenylalanine — as a fatigue biomarker in primary biliary cirrhosis/PSC patients; another (PMID 32025163) is a metabolomics study of cholangiocarcinoma unrelated to treatment; and the remaining two (PMID 8000512, PMID 2103382) concern **fMLP (N-formyl-methionyl-leucyl-phenylalanine)**, a bacterial chemotactic peptide that is a distinct compound from free phenylalanine, and describe it as inducing bile duct inflammation in animal models — i.e., a disease-causing mechanism, not a therapeutic one.

Given the very low TxGNN rank (13,234th out of the model's candidate list, despite a superficially high score), the absence of any supportive mechanism, and the fact that cited literature describes an unrelated compound or the opposite biological effect, this prediction is most plausibly a knowledge-graph false positive driven by node co-occurrence (phenylalanine/tyrosine appearing alongside hepatobiliary disease terms) rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Observational | BMC Gastroenterology | Examines plasma **tyrosine** (not phenylalanine) as a fatigue biomarker in PBC/PSC patients; not a treatment study |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Metabolomics | J Clin Exp Hepatol | Serum metabolomic profiling of cholangiocarcinoma vs. benign hepatobiliary disease; not related to phenylalanine treatment |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal model | J Gastroenterol | fMLT (a chemotactic peptide, not free phenylalanine) induces small duct cholangitis in rats — describes disease pathogenesis, not treatment |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Basic research | J Gastroenterol Hepatol | Studies enterohepatic circulation of the bacterial peptide fMLP, not phenylalanine itself |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials and no supportive literature exist for phenylalanine in sclerosing cholangitis; the cited publications either study a different compound (the peptide fMLP/fMLT) or unrelated biomarkers, and the TxGNN score is undermined by the extremely low candidate rank (13,234). This prediction should be treated as an unconfirmed model artifact rather than a repurposing lead.

A second, lower-priority candidate — **congenital prothrombin deficiency** (TxGNN score 99.26%, rank 16,307) — was also reviewed and shows the same pattern: the only associated trial (NCT06227429) is a withdrawn, zero-enrollment study of an unrelated drug (Nitisinone), in which phenylalanine appears only as a monitored lab value, not as treatment. No plausible mechanism links phenylalanine to prothrombin synthesis. This candidate is also recommended for **Hold**.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for phenylalanine confirming any plausible hepatobiliary or coagulation-related pathway
- Regulatory/label data (currently no marketing authorization exists to review)
- Independent confirmation that the TxGNN association is not an artifact of node co-occurrence (e.g., phenylalanine/tyrosine/fMLP entity conflation in the knowledge graph)
- If pursued further, preclinical mechanistic studies specific to free phenylalanine (not fMLP) in cholestatic liver disease models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

