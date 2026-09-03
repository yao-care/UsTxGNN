---
layout: default
title: Pseudoephedrine
parent: 僅模型預測 (L5)
nav_order: 1098
evidence_level: L5
indication_count: 3
---

# Pseudoephedrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pseudoephedrine: From Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

> Pseudoephedrine is a sympathomimetic decongestant long used to relieve nasal congestion associated with colds and allergic rhinitis.
> The TxGNN model's top prediction — **Nasal Cavity Disease** — largely restates this already-known use rather than identifying a genuinely novel indication,
> with **19 clinical trials** and **7 publications** touching on related decongestant pharmacology, but only **one** trial testing pseudoephedrine directly against placebo.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (no Taiwan/US license record); pseudoephedrine is generally known as an oral α-adrenergic decongestant for nasal congestion |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 (1 completed Phase 2 RCT directly testing pseudoephedrine) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on general pharmacological knowledge, pseudoephedrine is an α-adrenergic receptor agonist that causes vasoconstriction of nasal mucosal blood vessels, reducing tissue edema and nasal airway resistance. This mechanism is the well-established basis for its use as an oral decongestant.

Because the predicted indication "Nasal Cavity Disease" sits mechanistically very close to pseudoephedrine's known decongestant action, the prediction is biologically plausible — but it should be read as **confirmatory of existing pharmacology** rather than a novel repurposing signal. The evidence pack does not contain the drug's actual approved indication (original_indications is empty and no license records exist), so the degree of true "repurposing novelty" cannot be confirmed from this dataset alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | Completed | 53 | Randomized crossover comparing JNJ-39220675, pseudoephedrine, and placebo for allergic rhinitis symptom relief |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | H3-receptor antagonist tested against nasal allergen-induced congestion using acoustic rhinometry |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Topical anesthesia vs. decongestant vs. combination to reduce discomfort during fiberoptic nasal endoscopy |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | Completed | 21 | MRI-based assessment of anti-allergy drug effects on nasal/sinus mucosal dimensions after allergen challenge |
| [NCT03979209](https://clinicaltrials.gov/study/NCT03979209) | Phase 1 | Completed | 16 | Cortisol suppression risk with high-volume nasal mometasone irrigation at varying doses |
| [NCT04048174](https://clinicaltrials.gov/study/NCT04048174) | N/A | Completed | 27 | Live probiotic bacteria (L. lactis) instilled into nasal/sinus cavities for refractory chronic rhinosinusitis |
| [NCT00939393](https://clinicaltrials.gov/study/NCT00939393) | N/A | Completed | 72 | Endoscopic sinus surgery performed in-office vs. operating room, with/without balloon sinuplasty |
| [NCT01886768](https://clinicaltrials.gov/study/NCT01886768) | N/A | Unknown | 212 | Double vs. single nasal pledget decongestion method for transnasal endoscopy tolerance |
| [NCT05131958](https://clinicaltrials.gov/study/NCT05131958) | N/A | Unknown | 30 | Multiparametric (imaging, aerodynamic, acoustic, perceptual) evaluation of nasality in nasal polyposis |
| [NCT06580210](https://clinicaltrials.gov/study/NCT06580210) | N/A | Recruiting | 114 | Mechanical decongestant seawater spray with essential oils for acute rhinitis with nasal obstruction |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative pharmacology study | American Journal of Rhinology | Direct comparison of oral/topical decongestant effects of phenylpropanolamine vs. d-pseudoephedrine using acoustic rhinometry |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy and Asthma Proceedings | Overview chapter on nonallergic rhinitis, including decongestant mucosal mechanisms |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Preclinical (feline model) | American Journal of Rhinology & Allergy | Decongestant effects of D-pseudoephedrine, alone and with desloratadine, in feline nasal congestion model |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Preclinical pharmacology | J Pharmacology and Experimental Therapeutics | Selective α2c-adrenergic agonists evaluated in animal models of nasal congestion |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Preclinical (dog model) | J Pharmacological and Toxicological Methods | Chronic experimental dog model developed to study mechanism of nasal decongestant drugs |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Preclinical (dog model) | American Journal of Rhinology | Acoustic rhinometry-based dog model for studying nasal congestion pharmacology |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Preclinical (dog model) | American Journal of Rhinology | Allergic nasal congestion model in ragweed-sensitized dogs |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are not currently available for this compound in the evidence pack; TFDA label retrieval is flagged as a blocking data gap — see Conclusion.)*

---

## Other Predicted Indications (Lower Priority)

Two additional TxGNN predictions were scored for pseudoephedrine but do not currently warrant advancement:

- **Acute laryngopharyngitis** (score 99.73%, rank 7405) — Evidence Level L5, no supporting trials or literature; purely a model prediction. Recommendation: Hold.
- **Allergic urticaria** (score 99.14%, rank 18755) — Evidence Level L4; available trials and literature actually concern second-generation antihistamines (loratadine, fexofenadine, desloratadine), not pseudoephedrine itself. Mechanistic fit is weak, since pseudoephedrine is an α-adrenergic agonist rather than an H1-antihistamine, and urticaria is histamine-driven. Recommendation: Hold.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (nasal cavity disease) has only L2-level evidence (a single completed Phase 2 RCT directly testing pseudoephedrine) and largely reflects the drug's already-known decongestant pharmacology rather than a novel repurposing opportunity. More importantly, TFDA/FDA label safety data (warnings, contraindications, DDI) are entirely missing — a Blocking-severity gap that prevents any S1 safety evaluation — and the drug currently has no market license record in the evaluated jurisdiction.

**To proceed, the following is needed:**
- Retrieve TFDA package insert (warnings/contraindications) — Blocking gap (DG001)
- Retrieve DrugBank mechanism of action detail — High-priority gap (DG002)
- Confirm the drug's actual original/approved indication to properly assess repurposing novelty (original_indications field is currently empty)
- Clarify market/licensing status given "Not Marketed" flag before any regulatory strategy discussion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

