---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 1042
evidence_level: L5
indication_count: 3
---

# Phenylephrine
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

# Phenylephrine: From Topical Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

> Phenylephrine is a selective α1-adrenergic agonist whose established pharmacology is topical vasoconstriction of nasal/ocular mucosa, used clinically as a decongestant prior to nasal procedures.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
> with **8 clinical trials** and **8 publications** currently supporting this direction, including one completed Phase 2 RCT and one placebo-controlled RCT in the literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in license records (drug not currently marketed); established pharmacological use as a topical nasal/ocular decongestant and vasoconstrictor |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% (rank 1230) |
| Evidence Level | L2 |
| US Market Status | Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank (data gap DG002). Based on known pharmacology, phenylephrine is a selective α1-adrenergic receptor agonist that acts on nasal mucosal vascular smooth muscle to produce vasoconstriction, reducing mucosal congestion and swelling. This local vasoconstrictive effect is already well established in clinical practice (e.g., decongestion prior to nasoendoscopy, bleeding control during endoscopic sinus surgery), so the "new" indication of nasal cavity disease is essentially a formalization of existing off-label/procedural use rather than a novel mechanistic hypothesis.

The relationship between this established use and the predicted indication is therefore mechanistically direct: both rely on the same α1-mediated vasoconstriction of nasal mucosa. The supporting evidence largely comes from ENT procedural settings (nasoendoscopy, functional endoscopic sinus surgery, dacryocystorhinostomy) where phenylephrine or phenylephrine-containing combinations (e.g., Co-phenylcaine, Polydexa with phenylephrine) are used for decongestion and improved visualization — reinforcing plausibility while also indicating that most current evidence targets procedural/symptomatic endpoints rather than disease-modifying treatment of nasal cavity disease as a diagnosis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Co-phenylcaine (phenylephrine + lidocaine) nasal spray vs. nasal nebulization for decongestion/local anesthesia before rigid nasoendoscopy |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, four-way crossover RCT using acoustic rhinometry to assess nasal congestion after allergen challenge |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Comparison of oxymetazoline vs. epinephrine (same α-agonist decongestant class) on blood loss and surgical field visualization before endoscopic sinus surgery |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Cocaine vs. lidocaine/xylometazoline vs. saline for intranasal analgesia before awake nasotracheal intubation |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Esmolol vs. lidocaine IV infusion on recovery quality after functional endoscopic sinus surgery (shared procedural context, no direct phenylephrine arm) |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Kovanaze (tetracaine + oxymetazoline) nasal mist vs. articaine for maxillary dental pulpal anesthesia |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Repeat of Kovanaze vs. articaine maxillary anesthesia trial; withdrawn before enrollment |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | N/A | Unknown | 120 | Endonasal-endoscopic vs. external dacryocystorhinostomy for nasolacrimal duct obstruction |

**Note:** Most trials involve phenylephrine-containing combination products or same-class α-agonists used for procedural decongestion, not disease-specific therapeutic endpoints for nasal cavity disease per se.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Double-blind placebo-controlled RCT (n=98): Cophenylcaine spray reduced pain/discomfort during flexible nasendoscopy vs. placebo |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT/Cohort | PLoS One | Triple-blind RCT on topical tranexamic acid effect on bleeding and surgical field quality during FESS in chronic rhinosinusitis |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | Int J Pediatr Otorhinolaryngol | Acoustic rhinometric evaluation of nasal cavity/nasopharynx geometry after adenotonsillectomy |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental/Clinical safety-efficacy | Vestnik Otorinolaringologii | Safety and efficacy evaluation of Polydexa nasal spray with phenylephrine in acute rhinosinusitis |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik Otorinolaringologii | Differential diagnosis of chronic nasal disease after surgery, referencing Polydexa spray with phenylephrine |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik Otorinolaringologii | Pathogenetic approach to treatment of inflammatory diseases of the nose and paranasal sinuses |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Arch Ophthalmol | Cocaine toxicity during dacryocystorhinostomy, with one patient also reacting to intranasal phenylephrine |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In vitro study | Clin Otolaryngol Allied Sci | Preliminary in vitro study of drug effects (including nasal decongestants) on ciliary beat frequency |

---

## US Market Information

Phenylephrine currently has no marketed license records in this dataset (Market Status: **Not Marketed**, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available in this evidence pack (data gap DG001, flagged as Blocking for safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong (established α1-agonist vasoconstrictor pharmacology already used in nasal procedures) and is supported by one completed Phase 2 RCT and one placebo-controlled RCT (L2 evidence), but a Blocking data gap in TFDA/FDA label warnings and contraindications (DG001) prevents a full safety pre-assessment (S1), and most current evidence targets procedural/symptomatic endpoints rather than a distinct "nasal cavity disease" treatment claim.

**To proceed, the following is needed:**
- Official package insert / label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Clarification of original approved indication(s) and any prior license history
- Route compatibility assessment (currently marked pending in evidence pack)
- Further review distinguishing procedural decongestant use from a genuine disease-modifying indication for nasal cavity disease

**Other candidate indications screened for this drug** (acute laryngopharyngitis, trigeminal autonomic cephalalgia) were both placed on **Hold** — the former lacks any supporting trials or literature (L5, model-prediction only), and the latter's literature base consists exclusively of diagnostic pupillometry studies using phenylephrine as a testing reagent, not as a therapeutic agent (L4).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

