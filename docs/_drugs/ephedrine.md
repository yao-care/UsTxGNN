---
layout: default
title: Ephedrine
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 3
---

# Ephedrine
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

# Ephedrine: From Decongestant/Vasopressor Use to Nasal Cavity Disease

## One-Sentence Summary

Ephedrine is a sympathomimetic (α/β-adrenergic agonist) historically used as a nasal decongestant and as a vasopressor for anesthesia-related hypotension, though no Taiwan-approved indication is currently on file for this drug. The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, a finding that is mechanistically plausible but currently supported mainly by indirect, class-level evidence — **18 clinical trials** (mostly non-ephedrine-specific) and **8 publications** were retrieved, with only a handful directly relevant.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan license data (no TFDA license on file); historically used as a nasal decongestant/vasopressor per drug class |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Market Status (Taiwan) | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa`: Data Gap). Based on the drug class and the repurposing rationale attached to this candidate, ephedrine is an indirect-acting α/β-adrenergic agonist that produces vasoconstriction in nasal mucosal blood vessels, reducing mucosal congestion and swelling — the classic "decongestant" mechanism. This is a well-established pharmacological property rather than a speculative link.

Because ephedrine has historically been used in nasal decongestant preparations, the predicted association with Nasal Cavity Disease largely represents **reconfirmation of an already-known pharmacological use** rather than a genuinely novel mechanistic hypothesis. However, since this evidence pack records no formal original indication and no Taiwan licensing history, the prediction still needs to be substantiated with drug-specific (not merely drug-class) clinical evidence before it can be treated as validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Randomized, double-blind, double-dummy, crossover study of an H3-receptor antagonist on nasal congestion after allergen challenge in seasonal allergic rhinitis; methodologically rigorous decongestant-comparison model, but ephedrine is not explicitly confirmed as a study arm |
| [NCT01886768](https://clinicaltrials.gov/study/NCT01886768) | N/A | Unknown | 212 | Compared double- vs single-pledget nasal anesthesia for transnasal endoscopy; ephedrine-soaked pledgets are commonly used clinically for pre-procedural mucosal vasoconstriction |
| [NCT00939393](https://clinicaltrials.gov/study/NCT00939393) | N/A | Completed | 72 | Endoscopic sinus surgery performed in-office vs. operating room; topical vasoconstrictors (including ephedrine-class agents) are routinely used to reduce intraoperative bleeding, but the trial itself compares care setting, not the drug |
| [NCT05131958](https://clinicaltrials.gov/study/NCT05131958) | N/A | Unknown | 30 | Multiparametric (imaging/aerodynamic/acoustic) evaluation of nasality in nasal polyposis; observational, no drug intervention |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Compares esmolol vs. lidocaine infusion for recovery quality after functional endoscopic sinus surgery; unrelated to ephedrine |
| [NCT01854619](https://clinicaltrials.gov/study/NCT01854619) | N/A | Unknown | 48 | Photodynamic disinfection for chronic rhinosinusitis; non-pharmacologic mechanism |
| [NCT06580210](https://clinicaltrials.gov/study/NCT06580210) | N/A | Recruiting | 114 | Mechanical decongestant seawater spray with essential oils for acute rhinitis; medical device, not a drug study |
| [NCT04048174](https://clinicaltrials.gov/study/NCT04048174) | N/A | Completed | 27 | Probiotic bacteria (L. lactis) instilled into nasal/sinus cavities for chronic rhinosinusitis; unrelated mechanism |
| [NCT05494346](https://clinicaltrials.gov/study/NCT05494346) | N/A | Recruiting | 101 | Decongestant seawater spray pocket valve with essential oils; medical device performance/safety study |
| [NCT00015795](https://clinicaltrials.gov/study/NCT00015795) | Phase 1 | Completed | 30 | Laryngeal airflow resistance in abductor spasmodic dysphonia; indication unrelated to nasal cavity congestion |

None of the retrieved trials directly evaluate ephedrine as the study drug for a nasal-cavity indication; relevance is largely inferred from procedural context (e.g., ephedrine's known off-label use as a nasal vasoconstrictor during ENT procedures).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | RCT (early era) | Svenska läkartidningen | Early experimental clinical testing of N-hydroxyethylpromethazine chloride combined with ephedrine hydrochloride applied in the nasal cavity |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative/Cohort | American Journal of Rhinology | Compared oral/topical decongestant effects of phenylpropanolamine and d-pseudoephedrine (related sympathomimetic class, not ephedrine itself) using acoustic rhinometry |
| [1541887](https://pubmed.ncbi.nlm.nih.gov/1541887/) | 1992 | Comparative clinical study | The Journal of Laryngology and Otology | Compared nasal packing vs. spraying for pre-operative nasal preparation |
| [8283338](https://pubmed.ncbi.nlm.nih.gov/8283338/) | 1993 | Case series | Nihon Jibiinkoka Gakkai Kaiho | Case series of congenital nasal stenosis, treated with nasal or oral intervention |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Clinical observation (uncontrolled) | Chinese Journal of Integrated Traditional and Western Medicine | Uncontrolled clinical observation of a rhinitis spray for chronic rhinitis |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal model (pharmacology) | American Journal of Rhinology | Dog model of allergic nasal congestion using acoustic rhinometry |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal model (pharmacology) | Journal of Pharmacological and Toxicological Methods | Pharmacological characterization of a chronic dog model of nasal congestion for studying decongestant mechanisms |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal model (pharmacology) | American Journal of Rhinology | Acoustic rhinometry in dogs as a large-animal model of nasal congestion |

Evidence is weighted toward animal pharmacology models and older/uncontrolled clinical observations; only one early-era (1964) study directly names ephedrine in a nasal-cavity clinical context.

---

## US Market Information

Ephedrine currently holds no marketing authorization license in Taiwan (0 NDAs on file; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all marked as data gaps in this evidence pack — including a Blocking-severity gap for TFDA label warnings/contraindications, which prevents a formal S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L3 (observational/indirect only) with no clinical trial directly confirming ephedrine's efficacy in nasal cavity disease, and a Blocking-severity data gap (missing TFDA label warnings/contraindications) prevents entry into the S1 safety pre-assessment stage. Ephedrine also has no current Taiwan marketing license, further limiting near-term actionability.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety pre-assessment
- Confirmed mechanism of action from DrugBank (DG002)
- Drug-specific (not decongestant-class) clinical trials evaluating ephedrine for nasal cavity disease
- Assessment of Taiwan regulatory pathway, given the drug is currently unmarketed (0 licenses)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

