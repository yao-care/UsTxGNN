---
layout: default
title: Alitretinoin
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitretinoin: From Kaposi's Sarcoma to Amenorrhea

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a pan-retinoid approved in the US as a topical agent for AIDS-related Kaposi's sarcoma and in Europe as an oral agent for severe chronic hand eczema.
The TxGNN model ranks **Amenorrhea** as its top predicted new indication with a score of 99.99%, yet **no clinical trials or publications** currently support this direction.
This prediction is based solely on knowledge graph topology and does not yet constitute a viable repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Kaposi's sarcoma (topical, FDA); Chronic hand eczema (oral, EU/Canada) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, alitretinoin is 9-cis-retinoic acid — a naturally occurring retinoid and the only compound known to activate all six nuclear retinoid receptors (RAR-α/β/γ and RXR-α/β/γ). This pan-receptor activation governs transcriptional programs that control cell differentiation, proliferation, and immune regulation, which underpins its utility in Kaposi's sarcoma and inflammatory skin disease.

The proposed link to amenorrhea is indirect. Vitamin A deficiency is epidemiologically associated with menstrual irregularities, and RAR/RXR signaling has theoretical downstream influence on the hypothalamic-pituitary-gonadal (HPG) axis. However, correcting a nutritional deficiency is mechanistically distinct from pharmacologically activating retinoid receptors with a potent 9-cis-RA agonist; the two are not equivalent, and no functional preclinical or clinical data supports 9-cis-RA as an HPG axis modulator.

The high TxGNN score most likely reflects indirect topological proximity in the knowledge graph between retinoid-associated nodes and reproductive system nodes — a structural artifact rather than a biologically actionable relationship. The repurposing rationale for amenorrhea is currently unsubstantiated and requires substantial mechanistic investigation before research investment is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Alitretinoin has no registered products in Taiwan (0 licenses). For reference, the drug is approved under the following international authorizations:

| Market | Product Name | Dosage Form | Approved Indication |
|--------|-------------|-------------|---------------------|
| US (FDA) | Panretin | Topical gel 0.1% | AIDS-related Kaposi's sarcoma cutaneous lesions |
| EU/EEA | Toctino | Oral capsule 10 mg / 30 mg | Severe chronic hand eczema in adults refractory to potent topical corticosteroids |

---

## Cytotoxicity

Alitretinoin is approved for Kaposi's sarcoma (a malignant neoplasm) and belongs to the retinoid class, which includes recognized antineoplastic differentiating agents.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Differentiating / targeted agent (Retinoid class) — not conventional cytotoxic |
| Myelosuppression Risk | Low — retinoids do not typically cause clinically significant myelosuppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests, fasting lipid panel (triglycerides), CBC; mandatory pregnancy testing throughout treatment |
| Handling Protection | Standard oral/topical precautions; teratogenicity risk requires enrollment in a pregnancy prevention program (PPP/iPLEDGE-equivalent) before dispensing |

---

## Safety Considerations

- **Critical Teratogenicity Warning**: Alitretinoin is **Pregnancy Category X** — confirmed teratogen with severe fetal malformation risk. It is absolutely contraindicated during pregnancy and in any patient who cannot comply with a mandatory pregnancy prevention program. Any consideration of use in women with amenorrhea (a reproductive-age population) presents a fundamental safety contradiction that must be resolved before further evaluation.
- **Bone metabolism risk**: High-dose retinoids activate RANK-L signaling and promote osteoclast differentiation. Epidemiological data (Swedish cohort studies) associate high vitamin A intake with increased fracture risk. Long-term use may adversely affect bone mineral density.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Zero clinical or preclinical evidence supports alitretinoin for amenorrhea, and the drug's Pregnancy Category X status creates a serious safety contradiction for use in women of reproductive age presenting with menstrual disorders — the core amenorrhea population.

**To proceed, the following is needed:**

- Preclinical mechanistic studies directly demonstrating 9-cis-RA activity on the HPG axis at therapeutic (non-supraphysiologic) concentrations
- A safety framework that explicitly addresses the Pregnancy Category X risk within the amenorrhea patient population
- DrugBank MOA data retrieval (DG002) to complete mechanism-of-action cross-validation
- Taiwan FDA package insert data (DG001) for local regulatory safety context
- Review of pharmacovigilance / post-marketing data for any reported effects on menstruation in patients receiving Toctino or Panretin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

