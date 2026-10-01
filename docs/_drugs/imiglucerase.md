---
layout: default
title: Imiglucerase
parent: Moderate Evidence (L3-L4)
nav_order: 791
evidence_level: L4
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase is a recombinant glucocerebrosidase enzyme replacement therapy, marketed in the US as Cerezyme and used for Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**, but **no clinical trials** and only **2 general enzyme replacement therapy (ERT) publications** exist, so the prediction has no direct clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (from known Cerezyme labeling; the approved indication text was empty in the Evidence Pack) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (BLA020367) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Imiglucerase is a recombinant form of glucocerebrosidase. It is taken up by macrophages through the mannose receptor and breaks down glucosylceramide, which accumulates in Gaucher disease.

Hurler syndrome (MPS I) is a different disease. It is caused by alpha-L-iduronidase deficiency, which leads to accumulation of glycosaminoglycans (GAGs). Imiglucerase does not act on GAGs, so it has no plausible direct catalytic effect. The only link is the shared class of lysosomal storage disease treated by ERT, which most likely drives the high TxGNN score.

The other predictions in this pack are weaker or equally indirect:
- **Scheie syndrome** is the attenuated form of MPS I, so the same reasoning applies.
- **Cholesteryl ester storage disease** involves a different enzyme (lysosomal acid lipase), and a disease-specific ERT (sebelipase alfa) already exists.
- **Benign neoplasm of adrenal gland** has no apparent mechanistic rationale and looks like a knowledge-graph artifact.
- **Autosomal ichthyosis syndrome with fatal disease course** has only a speculative link through skin ceramide abnormalities in severe glucocerebrosidase deficiency. Imiglucerase does not cross the blood-brain barrier or address non-Gaucher ichthyosis genetics.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de medecine interne | Overview of ERT for lysosomal storage diseases. It traces the path from placenta-derived alglucerase to recombinant imiglucerase (Cerezyme) in Gaucher disease. This is indirect evidence, with no Hurler-specific imiglucerase data. |
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Other (imaging/ERT overview) | Proc Natl Acad Sci U S A | PET imaging of ERT. It notes that ERT is effective in Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy and Pompe diseases, each with its own disease-specific enzyme. It does not show imiglucerase treating Hurler syndrome. |

Both papers are general ERT overviews. Neither tests imiglucerase in Hurler syndrome.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| BLA020367 | Cerezyme (Genzyme Corporation) | Injection, powder, lyophilized, for solution |

The approved indication text was not provided in the source data. The product is injectable only.

---

## Safety Considerations

- **Drug Interactions**: No interactions were found in the queried database.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.52%) appears to come from the shared lysosomal storage disease/ERT class rather than a real mechanistic link. Imiglucerase targets glucosylceramide, while Hurler syndrome involves GAG accumulation from alpha-L-iduronidase deficiency. There are no trials and no direct literature. A disease-specific ERT (laronidase) already exists for MPS I, so there is little rationale to pursue this.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and the approved indication text
- Detailed mechanism of action data
- Preclinical evidence that imiglucerase affects GAG accumulation, which is mechanistically unlikely
- Any direct clinical or in vitro data for imiglucerase in MPS I or Scheie syndrome

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

