---
layout: default
title: Indomethacin
parent: Model Prediction Only (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Indomethacin: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Bursitis, synovitis, tenosynovitis, rheumatoid arthritis…"
monitor_inn: "INDOMETHACIN"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
---

# Indomethacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Indomethacin: From Inflammatory Joint Disease to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Indomethacin is a non-steroidal anti-inflammatory drug (NSAID) originally used for inflammatory and degenerative joint conditions such as rheumatoid arthritis, ankylosing spondylitis, gout and bursitis, and for closing patent ductus arteriosus.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, synovitis, tenosynovitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis, gout, osteoarthritis, frozen shoulder, patent ductus arteriosus (indication text is not recorded in the US license entries, so this comes from the knowledge graph) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no currently valid licenses in the compiled data) |
| Number of NDAs | 7 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Indomethacin is generally known as a COX-1/COX-2 inhibitor that reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory arthritis is established.

That mechanism does not obviously apply to the predicted condition. Brachydactyly-syndactyly syndrome is a rare congenital limb malformation driven by developmental genetics, not by ongoing inflammation. No mechanistic link between COX inhibition and this pathology has been identified. The high score (99.97%) reflects patterns in the knowledge graph, not biological or clinical support. It should be treated as a hypothesis-generating signal at most.

**A more credible direction among the other predictions:** juvenile idiopathic arthritis (JIA, rank 8, score 99.84%) has some literature support, including a 1978 double-blind crossover trial in 30 children comparing ketoprofen and indomethacin (indomethacin was the preferred drug) and several pediatric rheumatology reviews. This reflects historical symptomatic NSAID use, not a new repurposing signal. NSAIDs do not modify the disease, and current JIA care relies mainly on DMARDs and biologics.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All seven US authorizations in the compiled data are cancelled.

| Authorization Number | Product Name | Dosage Form | Manufacturer | Status |
|---------|------|------|------|------|
| ANDA091240 | Indomethacin | Capsule | Bryant Ranch Prepack | Cancelled |
| ANDA201807 | Indomethacin | Capsule, extended release | Proficient Rx LP | Cancelled |
| ANDA073314 | INDOCIN | Suppository | Zyla Life Sciences US Inc. | Cancelled |
| ANDA091276 | Indomethacin | Capsule | DIRECT RX | Cancelled |
| NDA018829 | Indomethacin | Capsule | Chartwell RX, LLC | Cancelled |

Two further cancelled entries (ANDA079175, extended-release capsule; ANDA216184, suppository) are not shown.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** hypertension, epilepsy, gastric and duodenal ulcer, active peptic ulcer disease, kidney disease, liver disease, gallbladder disease, thrombocytopenia, blood coagulation disorders, asthma (intrinsic and allergic), myocardial infarction, cardiovascular and heart disease, ulcerative colitis, inflammatory bowel disease, necrotizing enterocolitis, intracerebral hemorrhage, esophageal dyskinesia, anxiety and related mood disorders, hemoglobinopathy, and infectious disease.
- **Drug Interactions:** 100 interactions were found in total. Of the 20 reviewed:
  - **Moderate:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, acetylsalicylic acid, metformin, glimepiride, chlorpropamide, aprepitant, mesalazine, balsalazide, potassium citrate, potassium bicarbonate, picosulfuric acid, and polyethylene glycol with electrolytes.
  - **Minor:** famotidine, ranitidine, cimetidine, linaclotide.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for brachydactyly-syndactyly syndrome rests only on a model score, with no trials, no literature, and no plausible mechanistic link. All US licenses in the compiled data are also cancelled. This candidate is not suitable for advancement.

**To proceed, the following is needed:**
- Mechanistic evidence connecting COX inhibition or prostaglandin signaling to the pathophysiology of this syndrome
- Preclinical data (cell or animal models) supporting any biological effect
- Package insert warnings and contraindications to complete safety screening
- Detailed mechanism of action data
- Consideration of redirecting effort to juvenile idiopathic arthritis, the better-supported prediction, bearing in mind that NSAIDs are only symptomatic therapy there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

