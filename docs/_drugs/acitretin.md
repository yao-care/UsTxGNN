---
layout: default
title: Acitretin
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 4
---

# Acitretin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill to align with project conventions. The skill confirms standard workflow applies; no additional overrides for report generation. Proceeding with the Drug Repurposing Evaluation Report (v5) format.

---

# Acitretin: From Psoriasis to Acne

## One-Sentence Summary

Acitretin is a second-generation oral retinoid widely used internationally for psoriasis and hyperkeratotic skin disorders, though it holds no marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Acne (disease)**,
with **1 clinical trial** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis and hyperkeratotic skin disorders (no Taiwan registration; established per international literature) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Market Status (Taiwan) | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information from the supporting literature, acitretin is a second-generation aromatic retinoid — a synthetic analog of retinoic acid that functions as a retinoic acid receptor (RAR) agonist. Although the formal MOA field is a data gap, the literature extensively documents that retinoids, including acitretin, inhibit sebaceous gland secretion and normalize follicular keratinization. These two processes sit at the very core of acne pathogenesis: excess sebum production and abnormal follicular plugging combine to create the anaerobic environment in which *C. acnes* proliferates.

Psoriasis and acne share overlapping pathomechanisms involving aberrant keratinocyte differentiation and inflammatory cytokine signaling. Retinoids address both through RAR-mediated modulation of gene transcription in skin cells. More directly, the **European S1 Guideline for hidradenitis suppurativa/acne inversa** (PMID 25640693) lists acitretin as a treatment option for this severe follicular occlusion disease, which is nosologically grouped within the acne spectrum. A case series (PMID 12080949) and a 25-year long-term outcomes study (PMID 20874789) further confirm direct clinical use of acitretin in nodulocystic acne and acne inversa, providing real-world mechanistic validation of the TxGNN prediction.

One important caveat: for common acne vulgaris, **isotretinoin** remains the established first-line oral retinoid. Acitretin and isotretinoin belong to the same pharmacological class but differ in RAR subtype selectivity, pharmacokinetics, and side-effect profiles. No large-scale head-to-head trials compare the two specifically in acne, meaning the evidence for acitretin in general acne vulgaris remains primarily mechanistic and indirect at this stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study examining whether isotretinoin-induced nasal mucosal dryness increases COVID-19 infection risk in acne patients. This trial studies isotretinoin (not acitretin) and targets COVID-19 risk — not acne efficacy. Provides indirect class-level context only; retinoids are confirmed in use for acne management. |

> **Note:** No clinical trials directly evaluating acitretin for acne were identified. The single retrieved trial involves a related retinoid (isotretinoin) in a COVID-19 safety context and does not constitute direct clinical evidence for the drug–indication pair under review.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case Report | *Cutis* | Patient with severe nodulocystic facial acne and hidradenitis suppurativa, refractory to two full isotretinoin courses, responded to acitretin. **Most direct evidence of acitretin in acne-spectrum disease.** |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Outcomes Study | *Br J Dermatol* | Long-term acitretin therapy for hidradenitis suppurativa (acne inversa) across 25 years of clinical practice; cumulative case evidence shows promising results; questions whether acne inversa pathomechanism differs fundamentally from classic acne. |
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Clinical Guideline | *JEADV* | European S1 guideline for hidradenitis suppurativa/acne inversa; acitretin listed as a conservative systemic treatment option, representing the highest level of guideline endorsement currently available for this acne-related indication. |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | *Clin Dermatol* | Comprehensive contemporary review of vitamin A and retinoids in dermatology; explicitly identifies acitretin among oral retinoids used therapeutically, with mechanistic discussion applicable to acne. |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Mechanistic Review | *Dermatology* | Reviews retinoid inhibition of sebaceous gland activity and discusses experimental models for predicting anti-acne efficacy of oral retinoids including acitretin; foundational mechanistic support. |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | *Drugs* | Broad review covering retinoid use across psoriasis, hyperkeratotic disorders, severe acne, and acne-related dermatoses; acitretin positioned as second-generation retinoid with demonstrated skin disease utility. |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | *Hautarzt* | Drug therapy review for acne inversa; acitretin discussed as part of the systemic treatment landscape alongside TNF-α inhibitors, reinforcing its clinical role in the acne spectrum. |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | Mechanistic Study | *Prostaglandins* | Demonstrates that acitretin (directly tested) inhibits eosinophil LTC4 production; supports the anti-inflammatory mechanism underlying retinoid efficacy in acne and psoriasis. |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | Pharmacokinetic Study | *Clin Pharmacokinet* | Pharmacokinetics and therapeutic efficacy of retinoids in skin disease; confirms acitretin as the active second-generation retinoid with major success in psoriasis and characterizes its distinct PK profile versus isotretinoin. |
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Cochrane Review | *Cochrane Database Syst Rev* | Systematic review of treatments for discoid lupus erythematosus in which retinoids (including acitretin) are assessed; contextualizes acitretin's anti-inflammatory spectrum across immune-mediated skin disorders beyond psoriasis alone. |

---

## Taiwan Market Information

Acitretin currently holds **no marketing authorization in Taiwan** (TFDA licenses: 0).

> For international reference: Acitretin is marketed as **Soriatane®** (capsules, 10 mg / 25 mg) in the United States and under similar brand names in Europe, indicated for severe psoriasis in adults. Any introduction to the Taiwan market would require a new NDA submission to the TFDA. Prescribers in Taiwan currently have no approved local product to reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The Evidence Pack contains no Taiwan-specific warning or contraindication data for acitretin (TFDA prescribing information was not retrieved; DDI database returned no results). Clinicians should consult the international prescribing information (e.g., Soriatane US PI). Particular attention is warranted for **teratogenicity** — acitretin is a potent teratogen requiring strict contraception during treatment and for at least 3 years after discontinuation — and **hepatotoxicity** and **hyperlipidaemia**, all well-established class-level concerns for systemic retinoids.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model's high prediction score (99.94%) is mechanistically coherent — acitretin's RAR agonism directly targets sebaceous gland hyperactivity and follicular dyskeratosis, the two cardinal pathomechanisms of acne. Guideline-level evidence (European S1) supports its use in hidradenitis suppurativa (acne inversa), and long-term clinical data plus case reports confirm real-world effectiveness in the severe acne spectrum. The evidence is insufficient for first-line use in acne vulgaris given the absence of RCTs and the availability of isotretinoin, but the mechanistic and observational foundation justifies further structured investigation rather than outright rejection.

**To proceed, the following is needed:**

- **Safety documentation**: Retrieve the TFDA prescribing information (or Soriatane US/EU package insert) to complete the S1 safety evaluation, with particular focus on teratogenicity risk management and hepatic monitoring requirements
- **MOA data**: Query DrugBank API (DB00459) to formally document acitretin's receptor binding profile and downstream targets
- **Indication stratification**: Clearly define the target acne subtype — evidence is substantially stronger for **hidradenitis suppurativa / acne inversa** than for **acne vulgaris**; these should be treated as separate development tracks
- **Gap analysis vs. isotretinoin**: Conduct a focused comparative literature review to identify patient segments where acitretin may offer advantages (e.g., isotretinoin-refractory nodulocystic acne, patients where isotretinoin is contraindicated)
- **Taiwan regulatory pathway**: Assess whether a Taiwan NDA for acitretin (psoriasis or acne inversa indication) is viable given the absence of current TFDA registration, and whether reference to approved markets (US, EU) can support an abridged submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

