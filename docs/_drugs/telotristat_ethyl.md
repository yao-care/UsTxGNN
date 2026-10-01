---
layout: default
title: Telotristat Ethyl
parent: Model Prediction Only (L5)
nav_order: 1207
evidence_level: L5
indication_count: 2
---

# Telotristat Ethyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Telotristat Ethyl: From Carcinoid Syndrome Diarrhea to Cauda Equina Syndrome

## One-Sentence Summary

Telotristat ethyl is a tryptophan hydroxylase inhibitor marketed in the US as Xermelo for carcinoid syndrome diarrhea. The TxGNN model predicts it may be effective for **cauda equina syndrome**. This prediction rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Carcinoid syndrome diarrhea (from general pharmacology knowledge; the license records provide no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 (both records share NDA208794) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, telotristat ethyl inhibits tryptophan hydroxylase, which lowers peripheral serotonin synthesis. That is why it works for carcinoid syndrome diarrhea.

The link to cauda equina syndrome is weak. Cauda equina syndrome is mainly a compressive, surgical neurological problem affecting the lumbosacral nerve roots. Lowering peripheral serotonin is unlikely to relieve nerve root compression, and the drug has limited CNS penetration.

The high score may reflect proximity in the knowledge graph. Cauda equina syndrome involves bowel and bladder dysfunction, and serotonin pathways touch gut and visceral function. That is a network association, not evidence of a disease-modifying effect. The prediction should be treated as a hypothesis only.

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
| NDA208794 | Xermelo (Lexicon Pharmaceuticals, Inc.) | Tablet | Not listed in the license record |
| NDA208794 | Xermelo (TerSera Therapeutics LLC) | Tablet | Not listed in the license record |

The only route of administration on record is oral.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or publications behind it. The proposed mechanism does not plausibly address nerve root compression. The second predicted indication, "obsolete neurogenic bladder (disease)", is also model-only and points to an outdated ontology term.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for telotristat ethyl in cauda equina syndrome and in neurogenic lower urinary tract dysfunction
- Remapping of the obsolete neurogenic bladder term to a current concept, if that indication is pursued
- A plausibility review of the mechanism, including CNS penetration, before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

