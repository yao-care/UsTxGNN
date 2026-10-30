---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 1143
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "SALICYLIC ACID"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Salicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Salicylic Acid: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salicylic acid is a long-established agent used for skin conditions such as acne, seborrheic dermatitis, warts, and fungal skin infections, and it is also listed for inflammatory conditions such as rheumatoid arthritis and allergic rhinitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it remains a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of FDA Applications | 5 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, salicylic acid is thought to act through inhibition of COX enzymes, which reduces prostaglandin synthesis and produces anti-inflammatory effects. However, public bioactivity data confirming this at a specific molecular target are lacking. Its keratolytic action is also well known in skin products.

Its listed indications include allergic and inflammatory conditions (allergic rhinitis, vasomotor rhinitis, rheumatoid arthritis). Papillary conjunctivitis is an allergic or inflammatory disease of the ocular surface, so a loose link through anti-inflammatory activity is plausible.

This link is weak. No clinical evidence supports the use of salicylic acid for this eye condition, and the high TxGNN score is a computational prediction only. Ocular safety of topical or systemic salicylic acid has not been established for this use, and the compound may be irritating to the eye.

### Other Predicted Candidates

The model produced nine other predictions, all with no trials or literature. Most are rare congenital or genetic skeletal syndromes with no plausible mechanistic link and are likely TxGNN model (deep learning) artifacts.

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Rosacea conjunctivitis | 0.9953 | Weak indirect link via acne and seborrheic dermatitis; may be irritating to the ocular surface |
| Pseudoachondroplasia | 0.9951 | Speculative anti-inflammatory link only |
| Myosclerosis | 0.9949 | Speculative link to muscle fibrosis |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, brachyolmia-amelogenesis imperfecta syndrome, acromesomelic dysplasia (Hunter-Thompson type), brachyolmia | 0.9944–0.9978 | No plausible mechanism |

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
| M006 | bareMinerals Blemish Rescue Skin-Clearing Loose Foundation | Powder | Not specified (valid) |
| M030 | Salicylic acid (Wal-Mart Stores Inc) | Patch | Not specified (valid) |
| M028 | REINREUDE Tag Wart Remover | Patch | Not specified (valid) |
| M032 | Gold Bond Psoriasis Relief Medicated Multi-Symptom | Cream | Not specified (valid) |
| nan | Acne Healing Dots | Patch | Not specified (valid) |


---

## Safety Considerations

- **Drug Interactions**: One pharmacology-based record was found. Salicylic acid is associated with the acid-sensing ion channel ASIC3 (human). No interaction severity level is given. Public data supporting a primary molecular target for the proposed COX-inhibition mechanism could not be found.

Please refer to the package insert for further safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone, with no clinical trials, no literature, and only a loose mechanistic link to papillary conjunctivitis. Among the other candidates, spondyloarthropathy is the most biologically plausible and could be pursued as a research question.

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

