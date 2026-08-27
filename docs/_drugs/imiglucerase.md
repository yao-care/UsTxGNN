---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 791
evidence_level: L5
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase (DrugBank DB00053) is a recombinant enzyme replacement therapy whose established use is Gaucher disease, where it substitutes for deficient glucocerebrosidase. The TxGNN model predicts it may also be effective for **Hurler Syndrome (MPS I)**, but this is currently supported only by **0 clinical trials** and **2 general (non-disease-specific) review articles**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher Disease (per cited literature context; not confirmed by formal regulatory/label data in this pack) |
| Predicted New Indication | Hurler Syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for imiglucerase is not available in this evidence pack (flagged as a High-severity data gap). Based on known information, imiglucerase belongs to the enzyme replacement therapy (ERT) class; its efficacy in Gaucher disease — via replacement of deficient glucocerebrosidase to clear glucocerebroside accumulation — is well established.

However, the mechanistic case for Hurler syndrome is weak. Hurler syndrome (MPS I) results from a deficiency of a *different* enzyme, alpha-L-iduronidase (IDUA), which clears glycosaminoglycans rather than glucocerebroside. The two supporting literature items (PMID 20534487, 21211680) are general reviews of "ERT for lysosomal storage diseases" as a therapeutic class — neither provides evidence specific to imiglucerase treating Hurler syndrome. The high TxGNN score most likely reflects the model clustering imiglucerase with other LSD-targeted ERT drugs by embedding similarity, rather than capturing a true drug-specific, disease-specific mechanistic link.

The same pattern holds for the other candidates in this evidence pack (Scheie syndrome, benign adrenal neoplasm, autosomal ichthyosis, cholesteryl ester storage disease) — all scored similarly high (L5, "Hold") with no literature or trials specific to imiglucerase, and in several cases a distinct causal enzyme already exists with its own approved ERT (e.g., sebelipase alfa for cholesteryl ester storage disease).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review/Imaging | PNAS | General overview of ERT (including imiglucerase) across LSDs — Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe — not specific to imiglucerase-Hurler efficacy |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de medecine interne | History/overview of ERT development starting with alglucerase/imiglucerase for Gaucher disease; broad LSD-ERT class review, no Hurler-specific data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, there are no clinical trials and no disease-specific literature supporting imiglucerase for Hurler syndrome. The proposed mechanistic link is questionable, since Hurler syndrome and Gaucher disease involve different deficient enzymes (IDUA vs. glucocerebrosidase) and different substrates.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (currently a Blocking data gap — required before any S1 safety review)
- Confirmed mechanism of action data for imiglucerase
- Preclinical or case-level evidence directly linking glucocerebrosidase replacement to MPS I/Hurler pathology
- Re-evaluation of the other four predicted indications in this pack (Scheie syndrome, adrenal neoplasm, ichthyosis, cholesteryl ester storage disease), all of which currently have weaker (L5) evidence than the top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

