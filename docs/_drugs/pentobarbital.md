---
layout: default
title: Pentobarbital
parent: 僅模型預測 (L5)
nav_order: 1028
evidence_level: L5
indication_count: 10
---

# Pentobarbital
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

# Pentobarbital: From Sedative-Hypnotic (Barbiturate) Use to Obesity Disorder

## One-Sentence Summary

> Pentobarbital is a barbiturate-class central nervous system depressant; the evidence pack does not record a specific approved original indication, and the drug is currently **not marketed**. The TxGNN model predicts a possible new application for **Obesity Disorder**, but this is currently supported by only **1 loosely related clinical trial** and **20 publications** — nearly all of which use pentobarbital merely as an anesthetic or sleep-induction tool in unrelated obesity research rather than evaluating it as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no license/indication text on file; drug historically classified as a barbiturate sedative-hypnotic) |
| Predicted New Indication | Obesity Disorder |
| TxGNN Prediction Score | 99.99% (rank 573) |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002, High severity). Based on known pharmacology, Pentobarbital belongs to the barbiturate class of CNS depressants, acting as a positive allosteric modulator of GABA-A receptors to produce sedation, hypnosis, and — at higher doses — anesthesia. This class-level mechanism is well established even though the evidence pack contains no recorded formal indication for this specific compound.

The predicted new indication, Obesity Disorder, has no established mechanistic pathway connecting GABA-A receptor modulation to appetite regulation, leptin signaling, or energy metabolism. The model's own rationale explicitly notes the absence of a direct pharmacological link: nearly all supporting literature uses pentobarbital solely as an anesthetic/sedative tool to immobilize or euthanize animals during unrelated obesity research (e.g., renal nerve recordings, hypothalamic lesion studies, GH response testing) — not as a treatment being evaluated for obesity itself.

Given this, the high TxGNN similarity score most likely reflects a graph-embedding artifact — frequent literature co-occurrence of "pentobarbital" and "obesity" purely because pentobarbital is a standard laboratory anesthetic used in obesity research — rather than genuine pharmacological plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pediatric pharmacokinetic characterization of understudied drugs (including pentobarbital) administered per standard of care; not designed to evaluate obesity treatment (relevance grade C — low). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5694866](https://pubmed.ncbi.nlm.nih.gov/5694866/) | 1968 | Review | JAMA | Discusses anesthetic management considerations in obese patients; no abstract available, pentobarbital referenced as an anesthetic agent, not a weight-loss therapy. |
| [19321699](https://pubmed.ncbi.nlm.nih.gov/19321699/) | 2009 | Preclinical | Am J Physiol Regul Integr Comp Physiol | Renal sympathetic nerve responses studied in fat-fed rabbits under pentobarbital anesthesia; pentobarbital used only as an anesthetic. |
| [15893702](https://pubmed.ncbi.nlm.nih.gov/15893702/) | 2005 | Preclinical | Autonomic Neuroscience | Gastric electrical stimulation for obesity studied in pentobarbital-anesthetized rats; pentobarbital used as anesthetic tool only. |
| [2674924](https://pubmed.ncbi.nlm.nih.gov/2674924/) | 1989 | Preclinical | Poultry Science | Hypothalamic lesion study of obesity in fowl; pentobarbital's role is incidental/procedural, not therapeutic. |
| [2145525](https://pubmed.ncbi.nlm.nih.gov/2145525/) | 1990 | Preclinical | Neuroendocrinology | GH response to GRF studied in cafeteria-fed obese rats; pentobarbital is not the agent under investigation. |
| [34072024](https://pubmed.ncbi.nlm.nih.gov/34072024/) | 2021 | Preclinical | Molecules | Brazil nut seed extract tested for anxiolytic/lipid-lowering effects in mice; extract (not pentobarbital) potentiated pentobarbital-induced hypnosis as a secondary sedation assay. |
| [34445005](https://pubmed.ncbi.nlm.nih.gov/34445005/) | 2021 | Preclinical | Nutrients | Garcinia cambogia peel extract screened for arousal effects using the pentobarbital-induced sleep test in a weight-loss supplement study. |
| [28347670](https://pubmed.ncbi.nlm.nih.gov/28347670/) | 2017 | Preclinical | Brain Research | Leptin-mimetic peptide localization study in obese mice; pentobarbital used only for terminal anesthesia/euthanasia. |
| [39563316](https://pubmed.ncbi.nlm.nih.gov/39563316/) | 2024 | Unclassified | Cardiovascular Diabetology | Lipoxin A4 effects on diabetic cardiac dysfunction; relevance to pentobarbital or obesity indication unclear from abstract. |
| [12424750](https://pubmed.ncbi.nlm.nih.gov/12424750/) | 2003 | Unclassified | Medicinal Research Reviews | Review of HISS-dependent insulin action pharmacodynamics; no direct evaluation of pentobarbital as an obesity treatment. |

---

## US Market Information

Pentobarbital currently has **no marketing authorization on record** in this evidence pack (`market_status`: Not Marketed, `total_licenses`: 0). No license or product information is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (data gap DG001, Blocking severity — TFDA label warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the underlying evidence and the model's own rationale both indicate the link between pentobarbital and Obesity Disorder is weak or spurious — the single trial is unrelated in purpose (pediatric PK), and virtually all supporting literature uses pentobarbital only as an experimental anesthetic tool rather than as a candidate obesity therapy. Evidence Level is L5 (model prediction only). For context, of the 10 candidates in this evidence pack, only rank 5 ("sleep disorder, initiating and maintaining sleep") has genuine mechanistic plausibility (matches the drug's known GABA-A sedative-hypnotic class, L4/S1) — yet it is also held back by pentobarbital's narrow therapeutic index and obsolete safety profile versus modern hypnotics. The remaining candidates (hypervitaminosis, 16p11.2 microdeletion syndrome, obsolete hypertelorism, frontorhiny, monogenic obesity, trichotillomania) have no supporting evidence at all and likely represent embedding artifacts.

**To proceed, the following is needed:**
- TFDA/FDA package insert data: key warnings and contraindications (DG001, blocking)
- Detailed mechanism of action documentation (DG002)
- A biologically grounded hypothesis linking GABA-A receptor modulation to appetite/energy-metabolism pathways, if this indication is to be pursued further
- Purpose-designed preclinical studies evaluating pentobarbital as a therapeutic agent for obesity (not merely as an anesthesia tool in obesity-model research)
- A formal reassessment of pentobarbital's abuse potential and narrow therapeutic index before considering any new indication development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

