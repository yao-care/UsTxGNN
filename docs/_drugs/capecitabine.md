---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Cancer Chemotherapy to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine chemotherapy drug, and the source record does not list its approved indications.
The TxGNN model predicts it may be effective for **gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)**, with a very high score of 99.94%.
However, there are currently **0 clinical trials** and **0 publications** for this specific disease, so the prediction is **model-only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the source record (approved indication text is empty) |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on general pharmacology, capecitabine is an oral prodrug converted to 5-fluorouracil (5-FU). 5-FU inhibits thymidylate synthase and disrupts DNA synthesis in rapidly dividing cells.

GAPPS is a rare hereditary syndrome affecting the stomach, and it is predisposed to gastric adenocarcinoma. The high score most likely reflects the close position of this node to gastric adenocarcinoma in the knowledge graph. It does not reflect disease-specific evidence. The record contains no trials or literature for GAPPS.

Because the original indications are missing, it is also not possible to judge how novel a gastric indication would be for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The record lists 20 authorizations in total. Five are shown below. All are generic (ANDA) products, and none has approved indication text in the record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA211724 | Capecitabine (Lifestar Pharma LLC) | Film-coated tablet | Not listed in record |
| ANDA207652 | Capecitabine (Ascend Laboratories, LLC) | Film-coated tablet | Not listed in record |
| ANDA207652 | Capecitabine (CivicaScript LLC) | Film-coated tablet | Not listed in record |
| ANDA204668 | Capecitabine (Sun Pharmaceutical Industries, Inc.) | Film-coated tablet | Not listed in record |
| ANDA091649 | Capecitabine (Teva Pharmaceuticals USA, Inc.) | Film-coated tablet | Not listed in record |

---

## Cytotoxicity

Capecitabine is a fluoropyrimidine antineoplastic. The record has no DrugBank toxicity data, so the entries below reflect general class knowledge.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Low to moderate |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC (with differential), liver and renal function |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The GAPPS prediction rests only on knowledge-graph proximity, with no trials or literature. It is Evidence Level L5. Safety screening also cannot proceed because package insert warnings and contraindications are missing.

Other gastric predictions for this drug have far more support. Gastric tubular adenocarcinoma reaches L1 with several Phase 3 RCTs, including CLASSIC (PMID 22226517), but this is effectively established gastric cancer therapy rather than novel repurposing. Signet ring cell gastric adenocarcinoma and gastric body carcinoma each have only indirect evidence (L3). Gastric cardia adenocarcinoma has a directly relevant Phase 2 capecitabine trial (L2). Prioritizing these over GAPPS is worth considering.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block safety screening (download and parse the FDA package insert)
- Mechanism of action data (query DrugBank)
- The original approved indications, to judge novelty
- GAPPS-specific evidence: clinical trials, case series, or a rationale for systemic fluoropyrimidine therapy in this hereditary syndrome

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

