---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

Using `txgnn-pipeline` skill noted — it confirms this is a TxGNN repurposing pipeline report task. Now generating the report from the Evidence Pack.

---

# Avapritinib: From GIST / Systemic Mastocytosis to Axial Spondylometaphyseal Dysplasia

## One-Sentence Summary

Avapritinib (Ayvakit) is a selective KIT and PDGFRA kinase inhibitor, approved in the United States for gastrointestinal stromal tumors (GIST) harboring PDGFRA D842V mutations and for advanced systemic mastocytosis.
The TxGNN model predicts it may be effective for **Axial Spondylometaphyseal Dysplasia** — a rare skeletal developmental disorder caused by TRPV4 gene mutations —
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally known for GIST (PDGFRA D842V mutation) and advanced systemic mastocytosis |
| Predicted New Indication | Axial Spondylometaphyseal Dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on known information, avapritinib is a highly selective type I kinase inhibitor targeting KIT and PDGFRA receptor tyrosine kinases. Its approved oncology indications — GIST with activating PDGFRA D842V mutations and advanced systemic mastocytosis — are both diseases driven by constitutive overactivation of these same kinases.

Axial spondylometaphyseal dysplasia, by contrast, is a rare congenital skeletal dysplasia caused by loss-of-function mutations in the *TRPV4* gene, which encodes a calcium-permeable ion channel critical for cartilage and bone development. There is no established direct connection between the KIT/PDGFRA signaling axis and TRPV4-mediated skeletal pathology. The TxGNN model may have detected an indirect link through shared bone remodeling nodes in the knowledge graph — such as downstream osteoblast/osteoclast regulatory pathways — but this is highly speculative.

In summary, while TxGNN's score is high (99.92%), the biological rationale for applying a KIT/PDGFRA inhibitor to a TRPV4-driven skeletal dysplasia is currently unsupported. This prediction is best interpreted as a knowledge-graph pattern capture rather than a clinically actionable hypothesis, and requires substantial mechanistic validation before further pursuit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No licensed products registered in the Taiwan regulatory database. Avapritinib (Ayvakit) holds FDA approval in the United States but has not been registered in Taiwan as of the data cutoff (2026-05-01).

---

## Cytotoxicity

Avapritinib is a targeted antineoplastic agent used in oncology (KIT/PDGFRA-driven malignancies).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective KIT / PDGFRA kinase inhibitor (Type I) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Follow institutional cytotoxic/oral targeted-therapy handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or preclinical evidence linking avapritinib to axial spondylometaphyseal dysplasia, and the mechanistic bridge between KIT/PDGFRA inhibition and TRPV4-driven skeletal dysplasia has not been established. The high TxGNN score likely reflects indirect knowledge-graph connectivity rather than true biological plausibility.

**To proceed, the following is needed:**
- Retrieve MOA data from DrugBank (DG002) to complete a proper mechanistic rationale assessment
- Retrieve Taiwan TFDA package insert (DG001) to evaluate safety warnings, contraindications, and dose-limiting toxicities
- Commission a focused literature review or in silico pathway analysis specifically examining whether KIT/PDGFRA or downstream MAPK/PI3K pathways intersect with TRPV4 bone dysplasia biology
- Consult a rare skeletal disease specialist to assess whether any indirect pharmacological rationale exists before advancing to any experimental stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

