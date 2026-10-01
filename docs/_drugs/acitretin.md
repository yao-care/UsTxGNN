---
layout: default
title: Acitretin
parent: Moderate Evidence (L3-L4)
nav_order: 123
evidence_level: L4
indication_count: 4
---

# Acitretin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Acitretin: From Severe Psoriasis to Acne

## One-Sentence Summary

Acitretin is an oral retinoid whose main use in dermatology is psoriasis. The TxGNN model predicts it may be effective for **acne**, but the only acitretin-specific human evidence is **1 case report** (in a patient who also had hidradenitis suppurativa), and the single linked clinical trial is off-target. Most of the **19 retrieved publications** are retinoid-class reviews or guidelines that support the idea only indirectly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records. The literature describes acitretin's main success as psoriasis. |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed records are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acitretin is a second-generation oral retinoid. It is described as normalizing keratinocyte differentiation and having anti-inflammatory effects. Its efficacy in psoriasis is well established, and mechanistically it may be applicable to acne.

Retinoids as a class reduce sebaceous gland activity and follicular hyperkeratinization, which is the rationale for using them in acne. However, this evidence comes mostly from isotretinoin, not acitretin. A 1995 review notes that the anti-acne effect of newer oral retinoids cannot simply be predicted from experimental models. The only drug-specific human report is a single case of nodulocystic acne with hidradenitis suppurativa (acne inversa), which is a different disease from acne vulgaris.

The high graph score is therefore best read as a class-level signal rather than proof for acitretin. Isotretinoin remains the established retinoid comparator for acne vulgaris.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Studies whether oral **isotretinoin** raises COVID-19 infection risk in acne patients. It gives no efficacy evidence for acitretin (relevance grade C). |

## Literature Evidence

No randomized controlled trials were found. The list below is ordered by relevance to acitretin.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case report | Cutis | Patient with severe nodulocystic acne and hidradenitis suppurativa. The patient improved on two courses of isotretinoin, but some draining cysts persisted. The report describes acitretin treatment for this patient. |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Clinical study (long-term results) | Br J Dermatol | Long-term acitretin outcomes in hidradenitis suppurativa, a related but different disease. Isotretinoin is thought to have only a limited effect there. |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | Review | Clin Pharmacokinet | Isotretinoin helps severe recalcitrant acne. Acitretin and etretinate have had their main success in psoriasis. |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | Drugs | Retinoids are used in psoriasis, keratotic disorders, severe acne and skin cancer chemoprevention. |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clin Dermatol | Overview of oral and topical retinoids in dermatology, including acitretin. |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Review | Dermatology | Isotretinoin's acne efficacy is attributed to inhibition of sebaceous gland activity. Whether new oral retinoids share this effect is an open question. |
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Guideline | J Eur Acad Dermatol Venereol | European guideline for hidradenitis suppurativa/acne inversa. Not about acne vulgaris. |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Hautarzt | Drug therapy of acne inversa: antibiotics, clindamycin plus rifampicin, and TNF-α inhibitors. |
| [26617362](https://pubmed.ncbi.nlm.nih.gov/26617362/) | 2016 | Review | Dermatol Clin | Medical treatments of hidradenitis suppurativa, with low levels of evidence overall. |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | Laboratory study | Prostaglandins | Examined the effect of eight retinoids, including acitretin, on eosinophil LTC4 release, as a possible anti-inflammatory mechanism. |

## US Market Information

Records list capsules for oral use only. Approved indication text is not stated in these records. The last two source rows were duplicates of ANDA217774, so four unique authorizations are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202552 (Amneal) | Acitretin | Capsule | Not stated in record |
| ANDA202148 (Mylan) | Acitretin | Capsule | Not stated in record |
| ANDA204633 (Sigmapharm) | Acitretin | Capsule | Not stated in record |
| ANDA217774 (Alembic) | Acitretin | Capsule | Not stated in record |

## Safety Considerations

- **Teratogenicity**: Acitretin is a potent teratogen. Its effective washout is very long, and pregnancy must be avoided for 3 years after stopping. Alcohol can convert it to etretinate.
- **Long-term concerns**: Bone and lipid effects are noted, and they are especially problematic in children.
- **Drug Interactions**: The interaction query returned no records. This is not confirmation that none exist.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only drug-specific human evidence is one case report in a different disease, and the single linked trial concerns isotretinoin, not acitretin. The high TxGNN score is likely a class-level signal. Acitretin's teratogenic risk is severe, and isotretinoin is already the standard retinoid for acne vulgaris. Other predicted indications (pediatric systemic lupus erythematosus, fetal erythroblastosis, familial cutaneous telangiectasia syndrome) are model-only, have no linked evidence, and should also be held. Fetal erythroblastosis is likely a graph artifact, since acitretin is contraindicated in pregnancy.

**To proceed, the following is needed:**
- Acitretin-specific efficacy data in acne vulgaris (controlled trials, or at least a systematic search beyond retinoid-class reviews)
- The package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, for example via the DrugBank API
- A comparison against isotretinoin, plus strict pregnancy-prevention guardrails in any future study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

