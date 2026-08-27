---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 762
evidence_level: L5
indication_count: 5
---

# Griseofulvin
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

# Griseofulvin: From Dermatophytosis to Myiasis

## One-Sentence Summary

Griseofulvin is a long-established oral antifungal, originally used to treat dermatophyte infections of the skin, hair, and nails (ringworm-type infections). The TxGNN model predicts it may be effective for **myiasis** (larval fly infestation of tissue), but this direction is currently supported by **0 clinical trials** and only **1 tangential veterinary review article**.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dermatophyte (fungal) infections of skin, hair, and nails — based on the drug's known pharmacological class; no Taiwan license record is present in this evidence pack |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| US/Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on known pharmacological class information, griseofulvin is an antifungal antibiotic that binds fungal microtubules and disrupts mitotic spindle formation, thereby inhibiting fungal cell division. It has traditionally been used for dermatophytosis (ringworm-type infections) of skin, hair, and nails — a fungal, not parasitic, indication.

Myiasis is caused by fly larvae infesting living tissue, a parasitic/entomological condition with no established relationship to fungal cell biology. The repurposing rationale in the evidence pack itself flags this: the single supporting literature item is a general veterinary review on "parasitic skin diseases of dogs and cats," which most likely discusses griseofulvin (for dermatophyte infection) and myiasis as separate topics within the same review rather than presenting any direct evidence that griseofulvin treats myiasis. The high TxGNN score is more plausibly explained by graph topology — both conditions cluster near "skin infection" nodes in the knowledge graph — than by a real pharmacological mechanism.

No larvicidal or insecticidal activity for griseofulvin has been reported. Mechanistically, this prediction should be treated as a model-topology artifact rather than a grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary record | General review of parasitic skin diseases in dogs and cats ("Parasitic skin diseases of dogs and cats"); no abstract available, and the article does not appear to specifically study griseofulvin for myiasis treatment |

## US Market Information

Griseofulvin is not currently marketed in Taiwan (0 licenses on record), so no license/NDA table is available.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA labeling data (DG001) and DDI data are not yet available in this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, there are zero clinical trials, zero ICTRP trials, and only one incidental veterinary review with no direct evidence linking griseofulvin to myiasis. The evidence pack's own rationale identifies this as a likely graph-topology artifact rather than a real mechanistic signal — insufficient to proceed past S0.

**To proceed, the following is needed:**
- TFDA/FDA label data on warnings and contraindications (Blocking gap, DG001) before any safety screening can begin
- Confirmed mechanism of action data (DG002) to properly assess mechanistic plausibility
- In vitro/in vivo evidence of any larvicidal or antiparasitic activity for griseofulvin
- Note: related sub-indications flagged by the model (wound myiasis, creeping myiasis, furuncular myiasis) and echinococcosis carry no clinical trial or literature support at all (L5, model prediction only) and should remain on hold pending the same foundational data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

