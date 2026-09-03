---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 895
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From NSAID Use in Osteoarthritis/Rheumatoid Arthritis to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Meloxicam is a COX-2 preferential NSAID established for osteoarthritis and rheumatoid arthritis-type joint inflammation. Among 10 TxGNN-predicted indications for this drug, **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA)** is the most clinically defensible candidate — it is mechanistically consistent with meloxicam's known anti-inflammatory action and already has real-world pediatric use in some markets — supported by **1 observational safety study**, though no meloxicam-specific clinical trial currently exists for this exact indication.

*Note on candidate selection*: This evidence pack contains 10 predicted indications. The single highest TxGNN score (acromesomelic dysplasia, Hunter-Thompson type, 99.92%) is explicitly flagged in its own repurposing rationale as a likely **false positive** — a structural/developmental skeletal disorder with no inflammatory pathway for an NSAID to act on, most likely reflecting embedding proximity between skeletal/joint disease nodes in the knowledge graph rather than a real signal. Ranks 2, 3, 4, 9 and 10 are similarly unsupported (all L5/Hold). The JIA candidate (rank 8) was selected as the report's focus because it is the only candidate combining an evidence level above L4, actual literature support, and a documented existing-use precedent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NSAID class — osteoarthritis / rheumatoid arthritis (general pharmacological knowledge; no Taiwan license record exists in this evidence pack) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA) |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for meloxicam in this evidence pack. Based on known information, meloxicam is a preferential COX-2 inhibitor NSAID; its efficacy in reducing synovial inflammation and joint pain in adult osteoarthritis and rheumatoid arthritis has long been established, and mechanistically this same COX-2-mediated anti-inflammatory pathway may be applicable to juvenile idiopathic arthritis.

Rheumatoid factor-positive polyarticular JIA shares the core pathology of multi-joint synovial inflammation with adult rheumatoid arthritis, meloxicam's established indication class. Meloxicam has in fact already been approved in some markets for symptomatic treatment of JIA in children aged 2 and older, giving this prediction a real-world use basis beyond the TxGNN score alone.

The supporting literature is a Phase 4 registry cohort study evaluating long-term safety of celecoxib and non-selective NSAIDs (as a drug class, not meloxicam-specific) in JIA patients. This confirms class-level safety in the pediatric JIA population but does not constitute a meloxicam-specific randomized controlled trial, which is why the evidence level is capped at L3 (observational) rather than L1/L2.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort (Phase 4 registry) | Pediatric Rheumatology Online Journal | Long-term safety and developmental outcomes of celecoxib and non-selective NSAIDs in juvenile idiopathic arthritis patients treated in routine clinical practice |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Meloxicam's established COX-2-mediated anti-inflammatory mechanism directly addresses the synovial inflammation driving polyarticular JIA, and the drug already has precedent pediatric use for this indication class in some markets. However, evidence is limited to a class-level (not meloxicam-specific) observational safety registry, and this evidence pack shows the drug is not currently marketed or licensed in this jurisdiction, with no TFDA label data available.

**To proceed, the following is needed:**
- TFDA-approved label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- Meloxicam-specific pediatric JIA efficacy/safety data (RCT or prospective cohort), rather than class-level NSAID data
- Resolution of local market/licensing status, since the drug currently has zero registered licenses in this market
- Drug-drug interaction (DDI) data, currently unavailable (query status: not_found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

