---
layout: default
title: Etodolac
parent: 僅模型預測 (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
---

# Etodolac
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

# Etodolac: From Osteoarthritis/Rheumatic Pain to Ankylosing Spondylitis

> **Note on candidate selection**: This Evidence Pack lists 10 TxGNN-predicted indications. The nominal #1 candidate (acromesomelic dysplasia, Hunter-Thompson type) has a TxGNN score of 99.97% but **zero** supporting trials/literature, and the pack's own rationale states it has "no direct relevance to the NSAID mechanism." Ranks 2–5, 7–9 are similarly unsupported (all L5/Hold, likely knowledge-graph proximity artifacts). Only two candidates have real evidence: **Ankylosing Spondylitis** (rank 6) and **Inflammatory Spondylopathy** (rank 10), which share nearly identical literature/trial evidence. This report focuses on Ankylosing Spondylitis as the higher-scoring, more clinically specific of the two.

## One-Sentence Summary

Etodolac is a COX-2-preferential NSAID; published literature in this evidence pack documents its historical use for osteoarthritis, rheumatoid arthritis, and postoperative pain, alongside ankylosing spondylitis (AS) itself. The TxGNN model predicts continued/expanded relevance for **Ankylosing Spondylitis**, supported by **1 clinical trial** (indirect, not etodolac-specific) and **9 publications**, most dating from 1989–2011.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on file (drug not marketed in this jurisdiction); per literature (PMID 1717225), historically indicated for rheumatoid arthritis, osteoarthritis, and postoperative pain |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Etodolac is a selective COX-2-preferential NSAID that inhibits prostaglandin synthesis, reducing inflammation and pain. This is drawn from the evidence pack's own mechanistic rationale, since the formal `original_moa` field is flagged as a data gap (DG002, High severity) pending DrugBank API confirmation.

NSAIDs are already an ASAS/EULAR first-line treatment class for ankylosing spondylitis, so this is less a novel repurposing hypothesis than a documented historical use: four of the nine literature entries (PMID 1717225, 2525800, 2146130, 2150569) explicitly list AS alongside RA and OA as indications studied for etodolac in the late 1980s–1990s. The mechanistic link is therefore well established, but the supporting evidence predates modern NSAID safety classification and trial standards.

The one registered clinical trial (NCT05164198) is not an etodolac trial — it studies TNF-inhibitor dose tapering in AS — and only overlaps on patient population. It should be read as background-standard-of-care context, not direct efficacy evidence for etodolac.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Evaluates TNF-inhibitor dose reduction in AS patients with stable disease; **not an etodolac trial** — relevance graded C (population overlap only) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | Cohort/Open trial | La Revue de médecine interne | Open trial in 4,947 RA/AS/OA patients (Lodine 200), efficacy and tolerability assessed across indications |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | Cohort (large-scale open trial) | Rheumatology International | Two French open-label safety studies (4,947 + 51,355 patients) covering RA, AS, and OA |
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Review | Drugs | Reappraisal of etodolac pharmacology; effective in RA, OA, AS, and postoperative pain, comparable to other NSAIDs |
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | Review | European Journal of Rheumatology and Inflammation | Randomized, double-blind, parallel-group studies comparing etodolac to naproxen/piroxicam in RA, OA, and AS |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | Review | Inflammopharmacology | Clinical review of etodolac as multipurpose analgesic; COX-2-selective mechanism, applied in RA, AS, gout, OA |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Review (safety) | Cochrane Database of Systematic Reviews | Safety of NSAIDs (including etodolac class) combined with methotrexate in inflammatory arthritis incl. AS |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | Review (methodology) | Annals of the Rheumatic Diseases | ASAS recommendations for recording NSAID intake as an outcome measure in axial spondyloarthritis trials |
| [24449987](https://pubmed.ncbi.nlm.nih.gov/24449987/) | 2013 | Review | The Israel Medical Association Journal | Discussion of "indemonstrable" axial spondyloarthritis diagnosis |
| [21140116](https://pubmed.ncbi.nlm.nih.gov/21140116/) | 2010 | Open prospective trial (non-etodolac) | Singapore Medical Journal | Pamidronate (not etodolac) in NSAID-refractory AS — background only, low direct relevance |

## US Market Information

Currently not marketed in this jurisdiction; no NDA/license records are available (`total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug-interaction data are recorded as data gaps in this evidence pack — notably, TFDA label warnings/contraindications (DG001) are flagged **Blocking** for safety pre-screening.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Etodolac's use in ankylosing spondylitis is mechanistically sound and historically documented across multiple cohort studies and reviews, but the evidence base is dated (mostly 1989–1997), lacks a dedicated modern RCT, and the only registered trial doesn't test etodolac itself. This supports cautious progression, not a clean Go.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/label warnings and contraindications) — currently blocking safety pre-screening (S1)
- Resolve DG002 (confirm MOA via DrugBank API) to formalize the mechanistic rationale
- Reassess GI/CV safety per current NSAID class labeling, since supporting literature predates modern safety standards
- Treat Inflammatory Spondylopathy (rank 10) as an overlapping signal rather than independent confirmation, given near-identical evidence sets
- Deprioritize the seven zero-evidence L5 candidates (ranks 1–5, 7–9) unless new trial/literature data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

