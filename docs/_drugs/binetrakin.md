---
layout: default
title: Binetrakin
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 9
---

# Binetrakin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Binetrakin: From Investigational Drug to Craniostenosis Cataract

## One-Sentence Summary

Binetrakin (DB12182) is an investigational compound with no approved indication in any major regulatory jurisdiction.
The TxGNN model predicts it may be effective for **Craniostenosis Cataract** — notably, all top 9 predicted indications are cataract subtypes sharing near-identical scores, suggesting a model clustering effect rather than independent predictions.
There are **0 clinical trials** and **0 publications** directly supporting this specific indication, yielding an evidence level of **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication (investigational drug) |
| Predicted New Indication | Craniostenosis Cataract |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for Binetrakin is currently unavailable. Based on indirect hints embedded in the supporting literature retrieved for adjacent cataract subtypes, Binetrakin may possess immunomodulatory properties — possibly involving cytokine pathways such as IL-2 or IL-4. However, this remains speculative without confirmed MOA data, and no pharmacokinetic, clinical, or preclinical data specific to Binetrakin is available to anchor the hypothesis.

A structurally important observation is that TxGNN assigned **nearly identical prediction scores** (0.9914) to ranks 1 through 5, and highly similar scores across all 9 predicted indications — every one of which is a cataract subtype. This pattern is a hallmark of **model grouping behavior**: the algorithm has associated Binetrakin with other compounds linked to cataract-relevant biological pathways and clustered the predictions accordingly. Practically, the nine predictions should be interpreted as a single collective hypothesis — "possibly relevant to cataract pathology" — rather than nine independently validated signals.

Craniostenosis cataract, the top-ranked prediction, is an extremely rare secondary cataract arising as a complication of craniosynostosis (premature skull suture fusion). Its pathogenesis is structural and mechanical rather than inflammatory, placing it among the least biologically plausible targets for an immunomodulatory agent. There is no published pharmacological literature on drug intervention in this subtype, and the prediction is best understood as a byproduct of the model grouping effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Binetrakin in craniostenosis cataract.

---

## Literature Evidence

Currently no related literature available for craniostenosis cataract.

> **Contextual note on adjacent cataract subtypes:** While no literature exists for the top-ranked prediction, a small number of indirect preclinical and observational studies were retrieved for **diabetic cataract** (rank 8, L4) and **senile cataract** (rank 9, L4). These studies do not investigate Binetrakin and are presented below solely as background mechanistic context. They do not constitute evidence of efficacy.

**Diabetic Cataract — Background Literature (indirect; does not study Binetrakin)**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20213480](https://pubmed.ncbi.nlm.nih.gov/20213480/) | 2010 | Animal Study | Graefe's Archive for Clinical and Experimental Ophthalmology | IL-2 and IFN-γ elevated in retinas of streptozotocin-diabetic rats; inflammatory cytokines implicated in early diabetic eye pathology |
| [35585570](https://pubmed.ncbi.nlm.nih.gov/35585570/) | 2022 | Clinical Observational | BMC Ophthalmology | 28 aqueous humor cytokines profiled in PDR/NVG patients; cytokine shifts after intravitreal conbercept correlated with intraoperative bleeding |
| [23049540](https://pubmed.ncbi.nlm.nih.gov/23049540/) | 2012 | Animal Study | Experimental Diabetes Research | Nicotine accelerates lens opacity progression in type 1 diabetic rats; demonstrates oxidative and metabolic cataract mechanisms |

**Senile Cataract — Background Literature (indirect; does not study Binetrakin)**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10502054](https://pubmed.ncbi.nlm.nih.gov/10502054/) | 1999 | Molecular Biology | Graefe's Archive for Clinical and Experimental Ophthalmology | TGF-α, TGF-β2, and IL-8 mRNA expressed in lens epithelial cells post-cataract surgery; inflammatory mediators present in pseudophakic environment |
| [8157173](https://pubmed.ncbi.nlm.nih.gov/8157173/) | 1994 | Clinical Observational | Graefe's Archive for Clinical and Experimental Ophthalmology | IL-4 and IgG elevated in aqueous humor of complicated senile cataract patients; immune involvement greater in uveitis-associated cases |

---

## US Market Information

Binetrakin has no approved products in the US market. No NDAs or other marketing authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

No key warnings, contraindications, or drug-drug interaction data are currently available for this investigational compound.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Binetrakin is an investigational compound with no approved indication, no confirmed mechanism of action, and zero direct clinical or preclinical evidence supporting any of the nine predicted cataract subtypes. The TxGNN predictions reflect a model clustering artifact rather than a validated biological signal, and the top-ranked target — craniostenosis cataract — is a rare, mechanically-driven secondary cataract with no pharmacological intervention literature whatsoever.

**To proceed, the following is needed:**
- **Confirmed MOA for Binetrakin** — this is a blocking prerequisite; all downstream mechanistic and safety analysis is contingent on it
- **Current clinical development status** — identification of any Phase I/II trials or IND filings for Binetrakin
- **Ocular pharmacokinetics** — systemic vs. local bioavailability, particularly the potential for ocular tissue penetration
- **Preclinical proof-of-concept** — if MOA confirms immunomodulatory activity, prioritize inflammatory cataract subtypes (e.g., uveitic or corticosteroid-induced cataract) rather than the rare or degenerative subtypes currently predicted
- **Safety and regulatory baseline** — first-in-human safety data and package insert once MOA and development status are established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

