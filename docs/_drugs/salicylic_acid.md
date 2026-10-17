---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 1143
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Acne, seborrheic dermatitis, tinea infections, rheumatoid arthritis…"
monitor_inn: "SALICYLIC ACID"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
---

# Salicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Salicylic Acid: From Topical Dermatologic and Inflammatory Conditions to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid is a long-established agent used for skin conditions such as acne, seborrheic dermatitis, warts, and fungal skin infections, and it is also listed for inflammatory conditions such as rheumatoid arthritis and allergic rhinitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it remains a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, seborrheic dermatitis, tinea infections, rheumatoid arthritis, allergic rhinitis, and others (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 5 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, salicylic acid is thought to act through inhibition of COX enzymes, which reduces prostaglandin synthesis and produces anti-inflammatory effects. However, public bioactivity data confirming this at a specific molecular target are lacking. Its keratolytic action is also well known in skin products.

Its listed indications include allergic and inflammatory conditions (allergic rhinitis, vasomotor rhinitis, rheumatoid arthritis). Papillary conjunctivitis is an allergic or inflammatory disease of the ocular surface, so a loose link through anti-inflammatory activity is plausible.

This link is weak. No clinical evidence supports the use of salicylic acid for this eye condition, and the high TxGNN score is a computational prediction only. Ocular safety of topical or systemic salicylic acid has not been established for this use, and the compound may be irritating to the eye.

### Other Predicted Candidates

The model produced nine other predictions, all with no trials or literature. Most are rare congenital or genetic skeletal syndromes with no plausible mechanistic link and are likely knowledge-graph artifacts.

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Spondyloarthropathy, susceptibility to | 99.34% | Most biologically plausible; NSAIDs are first-line in spondyloarthritis, but the entry concerns genetic susceptibility rather than active disease. Classified as a research question |
| Rosacea conjunctivitis | 99.53% | Weak indirect link via acne and seborrheic dermatitis; may be irritating to the ocular surface |
| Pseudoachondroplasia | 99.51% | Speculative anti-inflammatory link only |
| Myosclerosis | 99.49% | Speculative link to muscle fibrosis |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, brachyolmia-amelogenesis imperfecta syndrome, acromesomelic dysplasia (Hunter-Thompson type), brachyolmia | 99.44%–99.78% | No plausible mechanism |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M006 | bareMinerals Blemish Rescue Skin-Clearing Loose Foundation | Powder | Not specified (cancelled) |
| M030 | Salicylic acid (Wal-Mart Stores Inc) | Patch | Not specified (cancelled) |
| M028 | REINREUDE Tag Wart Remover | Patch | Not specified (cancelled) |
| M032 | Gold Bond Psoriasis Relief Medicated Multi-Symptom | Cream | Not specified (cancelled) |
| nan | Acne Healing Dots | Patch | Not specified (cancelled) |

All five records are cancelled, and no valid single-ingredient or combination license is currently on record.

---

## Safety Considerations

- **Drug Interactions**: One pharmacology-based record was found. Salicylic acid is associated with the acid-sensing ion channel ASIC3 (human). No interaction severity level is given. Public data supporting a primary molecular target for the proposed COX-inhibition mechanism could not be found.

Please refer to the package insert for further safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone, with no clinical trials, no literature, and only a loose mechanistic link to papillary conjunctivitis. Ocular safety is not established, and there are no currently valid US licenses. Among the other candidates, spondyloarthropathy is the most biologically plausible and could be pursued as a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- A literature and trial search specific to salicylic acid or salicylates in ocular allergic or inflammatory disease
- Ocular tolerability and safety data for any proposed route of administration
- Assessment of route compatibility, since available dosage forms are topical or skin-directed and none are ophthalmic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

