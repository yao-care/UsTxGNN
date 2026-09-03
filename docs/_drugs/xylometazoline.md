---
layout: default
title: Xylometazoline
parent: 僅模型預測 (L5)
nav_order: 1299
evidence_level: L5
indication_count: 2
---

# Xylometazoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Xylometazoline: From an Undocumented Original Indication to Nasal Cavity Disease

## One-Sentence Summary

> Xylometazoline (DrugBank DB06694) is a topical decongestant compound; however, its original approved indication and detailed mechanism of action are not documented in this evidence pack, and it is currently **not marketed** in Taiwan.
> The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
> supported by **2 clinical trials** and **7 publications**, though most of this evidence is procedural/adjunctive rather than a direct treatment trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text or original_indications entries in evidence pack |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data (`original_moa`) is not available in this evidence pack. However, the repurposing rationale attached to the top prediction identifies xylometazoline as an **alpha-2 adrenergic agonist**: it acts locally on nasal mucosal blood vessels to induce vasoconstriction, reducing mucosal swelling and expanding the nasal airway. This is a well-characterized pharmacological action of the compound class.

The predicted indication — "nasal cavity disease" — is mechanistically consistent with this decongestant action, since reduced mucosal congestion directly addresses the broad symptom category of nasal cavity disease (nasal obstruction, mucosal swelling). However, because `original_indications` is empty in this pack, it cannot be confirmed whether this represents a genuinely *new* indication or simply reflects the drug's already well-known, label-consistent decongestant use. This ambiguity should be resolved before treating the prediction as a novel repurposing signal.

A second, lower-ranked prediction (acute laryngopharyngitis, score 99.89%) follows a similar plausible mechanism — reduced upper airway mucosal congestion may indirectly ease laryngopharyngeal inflammation-related nasal symptoms — but has **no supporting clinical trial or literature evidence** and is a pure knowledge-graph association (Evidence Level L5, recommendation: Hold).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Triple-crossover comparison of cocaine, lidocaine/xylometazoline, and saline for intranasal analgesia during awake fiberoptic nasotracheal intubation; not a direct treatment trial for nasal cavity disease (Grade C relevance). |
| [NCT05072392](https://clinicaltrials.gov/study/NCT05072392) | N/A | Unknown | 80 | Evaluated Foley catheter-assisted nasal intubation to reduce nasal bleeding; xylometazoline use is procedural/adjunctive rather than a therapeutic endpoint (Grade C relevance). |

*Note: both trials relate to peri-procedural nasal decongestion, not to treatment of nasal cavity disease as a clinical condition.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | RCT (small) | Arzneimittel-Forschung | Double-blind rhinomanometric study comparing tuaminoheptane/N-acetyl-cysteine vs. xylometazoline vs. placebo on nasal resistance in healthy subjects. |
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | RCT (small, pediatric) | JAMA Otolaryngology–Head & Neck Surgery | Double-blind, placebo-controlled trial of intranasal local anesthetic/decongestant (including xylometazoline) for flexible nasendoscopy in children. |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestnik Otorinolaringologii | Reviews treatment approaches for inflammatory nasal/paranasal sinus disease in elderly patients, including combined decongestant nasal sprays. |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Cohort/Physiological study | Korean Journal of Anesthesiology | Compared xylometazoline spray vs. epinephrine gauze packing for nasal cavity expansion before nasotracheal intubation. |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Physiological study | Rhinology | Investigated nasal airflow asymmetry and the effect of topical xylometazoline decongestant on nasal airway resistance. |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Prospective comparative study | Eur Arch Otorhinolaryngol | Compared cotton pledget packing vs. topical spray (including xylometazoline) for nasal preparation before endoscopy. |
| [20632242](https://pubmed.ncbi.nlm.nih.gov/20632242/) | 2010 | Animal/comparative anatomy study | Pneumologie | Evaluated xylometazoline and surgical turbinectomy effects on nasal airflow resistance in brachycephalic dogs. |

---

## US Market Information

No license records are available — xylometazoline is currently **not marketed** in Taiwan (0 NDAs on file in this evidence pack).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Taiwan-specific labeling (warnings/contraindications) for this product is flagged as a **Blocking** data gap (DG001) — TFDA package insert data has not yet been retrieved and parsed. This must be resolved before any safety evaluation (S1 stage) can proceed. No drug-drug interaction records were found in the queried database (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (nasal cavity disease) has only Evidence Level L3, and the supporting clinical trials/literature are largely procedural or adjunctive (e.g., pre-intubation decongestion, endoscopy preparation) rather than direct treatment trials for nasal cavity disease as a condition. Combined with a **Blocking** safety data gap (no TFDA label data) and unresolved ambiguity over whether this is genuinely a new indication, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- Retrieve and parse TFDA package insert (warnings, contraindications) — currently blocking (DG001)
- Confirm original approved indication(s) and MOA via DrugBank to determine if "nasal cavity disease" is a novel repurposing signal or an existing label use (DG002)
- Identify clinical trials/literature directly evaluating xylometazoline as a *treatment* for nasal cavity disease, rather than as a peri-procedural adjunct
- Given the second candidate (acute laryngopharyngitis) has zero supporting evidence, it should remain at Hold/S0 pending any literature or trial data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

