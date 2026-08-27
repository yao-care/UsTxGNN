---
layout: default
title: Doxapram
parent: 僅模型預測 (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
---

# Doxapram
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

Using the evidence pack as provided (no external assumptions), here is the report:

---

# Doxapram (DB00561): From an Undocumented Original Indication to Vascular Disease (Predicted)

## One-Sentence Summary

Doxapram's original indication and mechanism of action are not documented in this evidence pack (DrugBank returned no indication/MOA text, and the drug is not currently marketed in Taiwan). The TxGNN model predicts a possible link to **Vascular Disease**, but this is supported by **0 clinical trials** and only tangential, largely unrelated literature (mostly animal, case-report, and safety-observation studies) — the evidence itself flags this prediction as likely an artifact of the disease-embedding space rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug not marketed in Taiwan; `original_indications` returned empty) |
| Predicted New Indication | Vascular Disease |
| TxGNN Prediction Score | 99.99% (0.99989) |
| Evidence Level | L4 (mechanism/preclinical-adjacent only; no clinical trials) |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as data gap DG002, High severity — "作用機轉 (MOA)"). Based on the literature that was retrieved, doxapram is a respiratory/analeptic stimulant that acts on carotid body chemoreceptors and the medullary respiratory center; several of the retrieved papers describe secondary hemodynamic effects (pressor responses, altered hypoxic pulmonary vasoconstriction) as side effects of this respiratory stimulation, not as a treatment mechanism for vascular disease itself.

The model's own repurposing rationale for this candidate is explicit about the weakness of the mechanistic link: it notes that "vascular disease" is a broad, upper-level category in the TxGNN disease ontology, and that a high similarity score here is more likely to reflect embedding clustering with adjacent vascular-disease subtypes than a specific, validated pharmacological relationship. No clinical trial evidence exists for this indication, and the retrieved literature includes at least one clearly mismatched result (a stroke-prevention anticoagulation trial with no connection to doxapram), reinforcing the concern that this signal may be noise.

Because both the original indication and the MOA are undocumented here, and the model's own rationale casts doubt on the mechanistic plausibility, this candidate should be treated as **hypothesis-generating only** at this stage, not as a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 18 literature hits returned for "vascular disease" are predominantly historical case reports, animal/veterinary studies, and safety observations related to doxapram's respiratory-stimulant use — not therapeutic evidence for a vascular disease indication. The 10 most relevant (by internal tier classification) are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18371030](https://pubmed.ncbi.nlm.nih.gov/18371030/) | 2008 | Retrospective Cohort (veterinary) | J Vet Intern Med | Compared caffeine vs. doxapram for treating hypercapnia in foals with hypoxic-ischemic encephalopathy |
| [4398848](https://pubmed.ncbi.nlm.nih.gov/4398848/) | 1971 | Preclinical/Animal Study | Anesthesia and Analgesia | Hemodynamic (pressor) responses to doxapram in normovolemic and hypovolemic dogs |
| [8737758](https://pubmed.ncbi.nlm.nih.gov/8737758/) | 1996 | Case Series / Safety Report | Eur J Clin Pharmacol | RCT of continuous doxapram infusion vs. placebo for late postoperative hypoxaemia; reports adverse events |
| [11743509](https://pubmed.ncbi.nlm.nih.gov/11743509/) | 2001 | Cohort Study | J Pediatrics | Association between prolonged doxapram therapy for apnea and isolated mental developmental delay in very-low-birth-weight infants |
| [8870121](https://pubmed.ncbi.nlm.nih.gov/8870121/) | 1996 | Preclinical Experimental Study | Semin Perinatol | Effect of hypoxic pulmonary vasoconstriction modulators on inhaled nitric oxide response in a neonatal atelectasis model |
| [40023176](https://pubmed.ncbi.nlm.nih.gov/40023176/) | 2025 | Cohort/Review (likely keyword mismatch — unrelated to doxapram) | Lancet | DOAC vs. no anticoagulation for stroke prevention in ICH survivors with AF; no doxapram content |
| [35318792](https://pubmed.ncbi.nlm.nih.gov/35318792/) | 2022 | Retrospective Case Series (veterinary) | J Vet Emerg Crit Care | Cardiopulmonary arrest and resuscitation outcomes in hospitalized birds (41 cases) |
| [10704775](https://pubmed.ncbi.nlm.nih.gov/10704775/) | 2000 | Preclinical Toxicity Study | Neuroscience Letters | Doxapram accentuated white matter injury in neonatal rats after bilateral carotid artery occlusion |
| [4706757](https://pubmed.ncbi.nlm.nih.gov/4706757/) | 1973 | Case Report | Anesthesiology | Recovery from central respiratory failure with doxapram administration in a patient with a brainstem lesion |
| [4146485](https://pubmed.ncbi.nlm.nih.gov/4146485/) | 1973 | Review | Int Anesthesiol Clin | General review of non-anaesthetic drugs used in anaesthetic practice, including doxapram |

*Note: PMID 40023176 appears to be a keyword-matching artifact (DOAC/stroke trial) rather than genuine evidence for this drug-disease pair; it is retained here for transparency but should not be counted as supporting evidence.*

---

## US Market Information

Doxapram currently holds no regulatory approvals on record for this market — status is **Not Marketed (未上市)** with **0 licenses** on file. No product/dosage-form data is available to tabulate.

---

## Other Predicted Indications (Ranks 2–10)

For completeness, the remaining 9 candidates in this evidence pack (arterial thoracic outlet syndrome, venous thoracic outlet syndrome, angiodysplasia of stomach, blue toe syndrome, hemangioendothelioma, atheroembolism of kidney, neurogenic thoracic outlet syndrome, visceral calciphylaxis, lymphangiectasis) all scored similarly high on the TxGNN metric (~99.98%) but returned **zero clinical trials and zero literature hits each**, and are rated **L5 (model prediction only)**. Their own rationale text uniformly attributes the score to embedding-space clustering around "vascular disease" rather than any identifiable pharmacological mechanism. All are scored **Hold**.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-interaction data were returned by the queried sources for this drug (DrugBank DDI query: not found; TFDA label data flagged as a **Blocking** data gap — DG001 — meaning this candidate cannot yet proceed to safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate set has no supporting clinical trials, only tangential/off-topic literature for the top-ranked indication, and no literature or trials at all for the remaining 9 candidates. Combined with a **Blocking** data gap on TFDA safety labeling (DG001) and a **High**-severity gap on mechanism of action (DG002), there is currently insufficient basis to advance any of these predictions beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert data — warnings, contraindications, DDI (currently Blocking gap, DG001)
- Confirmed mechanism of action from DrugBank or primary literature (currently High-severity gap, DG002)
- Original indication data for doxapram, to allow a genuine mechanistic-relatedness comparison against "vascular disease"
- Expert pharmacological review of whether the "vascular disease" signal reflects a real drug effect or a TxGNN disease-ontology clustering artifact, before committing further evidence-collection resources
- If pursued, targeted preclinical studies directly testing doxapram in a defined vascular disease model, since no such studies currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

