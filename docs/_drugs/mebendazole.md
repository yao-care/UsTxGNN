---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 889
evidence_level: L5
indication_count: 1
---

# Mebendazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Mebendazole: From Enterobiasis, Ascaridiasis and Trichuriasis to Acne

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic, originally used to treat intestinal worm infections such as pinworm (enterobiasis), roundworm (ascaridiasis) and whipworm (trichuriasis).
The TxGNN model predicts it may be effective for **acne**, but there are currently **0 clinical trials** and only **1 publication** (an unrelated case report), so the evidence is essentially model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Enterobiasis, ascaridiasis, trichuriasis (from the knowledge graph; the US license record has no indication text) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, mebendazole is a benzimidazole anthelmintic that binds parasite beta-tubulin and inhibits microtubule polymerization. Its efficacy in intestinal worm infections is established.

No credible mechanistic link to acne was identified. Acne is driven by excess sebum production, follicular hyperkeratinization, *Cutibacterium acnes* colonization and inflammation. No established pathway connects tubulin inhibition to these processes. Possible anti-proliferative or anti-inflammatory effects on keratinocytes or sebocytes are speculative and not supported by the available data.

The high TxGNN score (0.992) reflects a knowledge-graph prediction only and should not be read as evidence of efficacy. The model's rank for this prediction was 17,535.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | The American Journal of Tropical Medicine and Hygiene | Report of a human proliferative sparganosis case in Venezuela; the patient had acne-like skin lesions as a symptom of the parasitic infection. This does not test mebendazole for acne and offers no support for the prediction. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208398 | VERMOX (Janssen Pharmaceuticals, Inc.) | Chewable tablet (oral) | Not recorded; license status: cancelled |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease.
- **Drug Interactions** (10 found; most are moderate):
  - Moderate: metronidazole, iodide I-131, iodide I-123, phenobarbital, carbamazepine, ritonavir, fosphenytoin, phenytoin, primidone.
  - Minor: cimetidine.
  - Several of these are anticonvulsants that induce liver enzymes and may lower mebendazole exposure. Others carry their own clinical cautions.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no relevant literature and no plausible mechanistic link between tubulin inhibition and acne pathology. The only US license is cancelled, and label safety data is unavailable.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and a rigorous assessment of any biological link to acne
- FDA package insert warnings and contraindications, to complete safety screening
- Preclinical evidence (e.g., effects on sebocytes, keratinocytes or *C. acnes*) before any clinical consideration
- Assessment of route compatibility, since the only known formulation is an oral chewable tablet and acne treatment often uses topical therapy
- A review of the 1982 case report's relevance, and a literature search for better evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

