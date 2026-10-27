---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 954
evidence_level: L5
indication_count: 4
monitor_inn: "NAPROXEN"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
last_modified_at: 2026-10-14
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout…"
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Naproxen: From Musculoskeletal Pain and Inflammation to Brachydactyly-Syndactyly Syndrome
{: .text-alpha }

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for inflammatory and painful musculoskeletal conditions such as rheumatoid arthritis, osteoarthritis, gout, tendinitis and bursitis, as well as migraine and headache.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is a computational output only and has no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, bursitis, tendinitis, migraine and headache (the approved-indication text in the US license records is empty, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 14 (all cancelled; 12 ANDAs and 2 NDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Naproxen is generally known as a non-selective COX-1/COX-2 inhibitor that provides symptomatic anti-inflammatory and analgesic effects. Its efficacy in inflammatory joint disease and pain is well established.

Brachydactyly-syndactyly syndromes are rare congenital limb malformations of genetic and developmental origin. A COX-inhibition mechanism has no plausible disease-modifying role in such conditions, and nothing in the available data supports a mechanistic link.

The high TxGNN score (99.35%, model rank 14,678) most likely reflects graph proximity to skeletal and musculoskeletal terms shared with naproxen's original indications, not biological evidence. The other top predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, Hunter-Thompson type acromesomelic dysplasia, and brachyolmia-amelogenesis imperfecta syndrome) are also rare congenital skeletal or developmental syndromes. Each has no trials or literature, and they follow the same pattern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All 14 licenses are listed as cancelled and none is currently valid. The approved-indication text is blank in the records. The five main authorizations are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020204 | Aleve | Tablet | Lil' Drug Store Products, Inc |
| NDA021920 | Naproxen Sodium | Capsule, liquid filled | HEB |
| ANDA208363 | Naproxen Sodium | Capsule, liquid filled | Care One (American Sales Company) |
| ANDA200629 | Naproxen Sodium | Tablet, film coated | Aurobindo Pharma Limited |
| ANDA074140 | Naproxen | Tablet | Granules India Ltd |

All products are oral formulations.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Contraindications flagged in the knowledge graph** (drug-disease edges, not label text): hypertension, heart failure, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders, kidney disease, liver disease and liver failure, blood coagulation disease, anemia, diabetes mellitus and diabetic ketoacidosis, osteoporosis, epilepsy, obesity, gallbladder disease, benign prostatic hyperplasia, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were recorded; the first 20 are all Moderate-level (DDInter). Examples include:
  - Acid suppressants: famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Other: metformin, chlorpropamide, acetylsalicylic acid, aprepitant, mesalazine, balsalazide, potassium citrate, potassium bicarbonate

  Interactions beyond the first 20 were not detailed in the data.
- Theoretical concerns about NSAID use in growing skeletal tissue would need review for the predicted population, which involves skeletal developmental disorders.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link between COX inhibition and a congenital limb malformation. In addition, all US licenses are cancelled, and the safety data are incomplete.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a biologically plausible link to the disease pathway
- Package insert warnings and contraindications, which are needed before any safety screening
- Preclinical or case-level evidence of benefit in brachydactyly-syndactyly syndrome
- A review of NSAID safety in growing skeletal tissue and in the affected population
- Clarification of the current US regulatory status, given that all licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

