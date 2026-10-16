---
layout: default
title: Pentobarbital
parent: Model Prediction Only (L5)
nav_order: 1028
evidence_level: L5
indication_count: 10
monitor_inn: "PENTOBARBITAL"
predicted_indications: ["obesity disorder", "manic bipolar affective disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "sleep disorder, initiating and maintaining sleep", "obsolete hypertelorism (disease)", "major affective disorder", "frontorhiny", "monogenic obesity", "trichotillomania"]
---

# Pentobarbital
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pentobarbital: From Epilepsy and Insomnia to Obesity Disorder

## One-Sentence Summary

Pentobarbital is a barbiturate sedative-hypnotic, originally used for conditions such as epilepsy, insomnia, status epilepticus, and cerebral ischaemia.
The TxGNN model predicts it may be effective for **obesity disorder**, but there are **0 clinical trials** and only **20 publications** that mention the drug, mostly as an anaesthetic in animal experiments, so the prediction is **not supported by clinical evidence**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, insomnia, status epilepticus, brain ischaemia, transient ischaemic attack (from the knowledge graph; the US licence records contain no indication text) |
| Predicted New Indication | Obesity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no active licences) |
| Number of NDAs | 2 (both ANDAs, both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, pentobarbital is a barbiturate that enhances GABA-A receptor signalling, producing sedation, hypnosis, and anticonvulsant effects. This explains its original uses in epilepsy and insomnia.

For obesity, **no credible mechanistic link was identified**. The retrieved publications are animal or physiology studies on insulin kinetics, hypothalamic lesions, leptin mimetics, and gastric electrical stimulation. In these papers pentobarbital appears almost entirely as an **anaesthetic used during experiments**, not as a treatment. Barbiturates are not known to reduce body fat or appetite. The high TxGNN score therefore looks like a model signal rather than a pharmacologically grounded hypothesis.

Other top-ranked predictions are similarly weak. Sleep disorder (initiating and maintaining sleep) overlaps with the original insomnia indication and so is not true repurposing. Manic bipolar disorder and major affective disorder rest only on uncontrolled 1960s reports or indirect studies. The remaining predictions have no evidence at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications tests pentobarbital as a treatment for obesity. The table lists the most relevant ones, all preclinical or physiological.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7649094](https://pubmed.ncbi.nlm.nih.gov/7649094/) | 1995 | Animal study | Endocrinology | Insulin turnover in Zucker lean and obese rats; pentobarbital used as anaesthesia |
| [12424750](https://pubmed.ncbi.nlm.nih.gov/12424750/) | 2003 | Review / physiology methods | Medicinal Research Reviews | Methods for measuring insulin action and insulin resistance mechanisms |
| [2674924](https://pubmed.ncbi.nlm.nih.gov/2674924/) | 1989 | Animal study | Poultry Science | Hypothalamic lesions causing obesity and hyperphagia in fowl |
| [15893702](https://pubmed.ncbi.nlm.nih.gov/15893702/) | 2005 | Animal study | Autonomic Neuroscience | Gastric electrical stimulation changes brainstem neuronal activity in anaesthetised rats |
| [9145938](https://pubmed.ncbi.nlm.nih.gov/9145938/) | 1997 | Animal study | Physiology & Behavior | Ventromedial hypothalamic lesions reduce post-meal thermogenesis in rats |
| [19321699](https://pubmed.ncbi.nlm.nih.gov/19321699/) | 2009 | Animal study | Am J Physiol Regul Integr Comp Physiol | Altered kidney responses to renal nerve activation in fat-fed rabbits under pentobarbital anaesthesia |
| [16914422](https://pubmed.ncbi.nlm.nih.gov/16914422/) | 2006 | Animal study | Am J Physiol Regul Integr Comp Physiol | Enhanced sympathetic reactivity linked to insulin resistance in young Zucker rats |
| [34445005](https://pubmed.ncbi.nlm.nih.gov/34445005/) | 2021 | Animal study | Nutrients | Garcia cambogia peel extract shortens pentobarbital-induced sleep in mice (pentobarbital as an assay tool) |
| [34072024](https://pubmed.ncbi.nlm.nih.gov/34072024/) | 2021 | Animal study | Molecules | Brazil nut extract reduces anxiety-like behaviour and lipids in mice; potentiates pentobarbital hypnosis |
| [28347670](https://pubmed.ncbi.nlm.nih.gov/28347670/) | 2017 | Animal study | Brain Research | Oral leptin-mimetic peptides localise in the mouse hypothalamus |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA206404 (cancelled) | Pentobarbital sodium (Sagent Pharmaceuticals) | Injection, solution | Not listed |
| ANDA203619 (cancelled) | Pentobarbital Sodium (Hikma Pharmaceuticals USA Inc., dba Leucadia Pharmaceuticals) | Injection, solution | Not listed |

Both authorizations are cancelled, so there is no currently valid US licence for a single-ingredient product.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for label safety information.

- **Knowledge-graph contraindications** (not from label text): the knowledge graph lists many conditions, including:
  - Liver disease, liver failure, hepatic coma, and hepatic encephalopathy
  - Kidney disease
  - Chronic obstructive pulmonary disease, and sleep apnoea syndromes
  - Heart disease, cardiovascular disease, hypertension, and hypotension
  - Porphyria and other porphyrin metabolism disorders
  - Substance abuse or dependence
  - Blood disorders: thrombocytopenia, neutropenia, agranulocytosis, anaemia
  - Anxiety and neurotic disorders
- **Drug interactions**: 100 interactions were found. Examples:
  - **Major**: morphine (additive central nervous system and respiratory depression)
  - **Moderate**: corticosteroids (dexamethasone, hydrocortisone, betamethasone, triamcinolone), doxycycline, metronidazole, bupropion, aprepitant, vitamin D analogues (cholecalciferol, calcifediol, calcitriol), canagliflozin, saxagliptin, linagliptin, dronabinol, nabilone, and eliglustat
  - **Minor**: pyridoxine and cimetidine

Barbiturates in general also carry risks of dependence, respiratory depression, and a narrow therapeutic index.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The obesity prediction has no clinical trials, no human studies, and no plausible mechanism. The literature uses pentobarbital only as an experimental anaesthetic. The drug also has no active US licence and a substantial safety burden. Other top predictions are either overlapping with original indications (insomnia), supported only by outdated uncontrolled reports (mood disorders), or have no evidence at all.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Any credible pharmacological rationale linking GABA-A modulation to weight or appetite regulation
- Evidence from controlled human or well-designed pharmacological studies that tests pentobarbital as the intervention, not as an anaesthetic
- A risk-benefit comparison against existing obesity therapies, given pentobarbital's dependence and respiratory depression risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

