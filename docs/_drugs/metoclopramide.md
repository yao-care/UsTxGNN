---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 918
evidence_level: L5
indication_count: 5
monitor_inn: "METOCLOPRAMIDE"
predicted_indications: ["gastric ulcer (disease)", "gastroduodenitis", "peptic ulcer disease", "peptic ulcer perforation", "gastrojejunal ulcer"]
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metoclopramide: From Gastroesophageal Reflux Disease to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic agent, originally used for gastroesophageal reflux disease (GERD) and esophagitis.
The TxGNN model predicts it may be effective for **gastric ulcer**,
but only **1 clinical trial** (a procedural study in upper GI bleeding) and **20 publications** (mostly general reviews) are currently available, so the evidence is **weak and indirect**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal reflux disease, esophagitis, peptic esophagitis (from the knowledge graph; the US license records contain no indication text) |
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (as assessed in the data compiled for this report; no completed Phase 3 or Phase 2/3 RCT for ulcer treatment) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 10 (all ANDAs, generic applications; none is an NDA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, metoclopramide is a dopamine D2 antagonist and 5-HT4 agonist that enhances gastric emptying and upper GI motility.

Its efficacy in reflux disease and esophagitis relates to this prokinetic effect. For gastric ulcer, the link is **symptomatic and adjunctive, not disease-modifying**. It may help with nausea and delayed emptying, and it may improve gastric visualization before endoscopy in upper GI bleeding. It has no acid-suppressing or mucosal-healing action, and standard therapy (PPIs, *H. pylori* eradication) is far more effective.

The very high TxGNN score largely reflects overlap with the drug's original GERD and esophagitis indications and should not be read as independent clinical evidence.

Other predicted indications are weaker still:

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Gastroduodenitis | 99.90% | L4 | Plausible motility effects only; no trials |
| Peptic ulcer disease | 99.85% | L4 | Symptomatic or pre-endoscopy use only; no direct RCT of ulcer healing |
| Gastrojejunal ulcer | 99.78% | L5 | No disease-specific evidence |
| Peptic ulcer perforation | 99.78% | L5 | No credible link; prokinetics are generally contraindicated in suspected perforation |

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind randomized trial of metoclopramide premedication in upper GI bleeding. It tests whether it reduces repeat endoscopy, interventional radiology or surgery and improves visualization; it does not test ulcer healing |

This is the only registered trial. It is relevant to the ulcer population but addresses a procedural use, and its unknown status limits its weight.

---

## Literature Evidence

Most retrieved publications are general reviews of dyspepsia, gastroparesis, reflux and prokinetics. No RCT of ulcer healing was found. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | Double-blind RCT | Am J Gastroenterol | Evaluates IV metoclopramide for gastric visualization in active upper GI bleeding (an endoscopy-preparation use, not ulcer treatment) |
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | Triple-blind RCT | Rev Gastroenterol Mex | Metoclopramide 20 mg IV versus placebo for visualization in upper GI bleeding; the authors describe its usefulness as controversial |
| [42127996](https://pubmed.ncbi.nlm.nih.gov/42127996/) | 2026 | Guideline | Endoscopy | ESGE guideline update on peptic ulcer bleeding; support for metoclopramide in ulcer treatment was not confirmed |
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Review | Drugs | Pharmacology and clinical use, including easing emergency endoscopy in upper GI haemorrhage |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Pharmacology and clinical application of metoclopramide |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Review | Postgrad Med | Strategies for peptic lesions resistant to standard regimens (historical adjunct role) |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | Ulcer-protective and antisecretory effects in aspirin-induced and pylorus-ligated rat ulcer models (preclinical only) |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Alkaline reflux gastritis and esophagitis |
| [1441547](https://pubmed.ncbi.nlm.nih.gov/1441547/) | 1992 | Review | Wiad Lek | Non-ulcer dyspepsia, favouring prokinetics including metoclopramide |
| [12825960](https://pubmed.ncbi.nlm.nih.gov/12825960/) | 2003 | Review | Drugs | Diabetic gastroparesis (general background) |

---

## US Market Information

All 10 US authorizations are generic applications (ANDAs) with a cancelled status, and no approved indication text is recorded. The first 5 are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA072801 | Metoclopramide (Bryant Ranch Prepack) | Tablet | Not recorded |
| ANDA078807 | Metoclopramide (Ipca Laboratories) | Tablet | Not recorded |
| ANDA071402 | Metoclopramide (Bryant Ranch Prepack) | Solution | Not recorded |
| ANDA091392 | Metoclopramide (Fresenius Kabi USA) | Injection, solution | Not recorded |
| ANDA070184 | Metoclopramide (AvKARE) | Tablet | Not recorded |

---

## Safety Considerations

**Contraindications and risk conditions (knowledge-graph drug-disease contraindication links; not taken from label text):**
- Movement and neurological disorders: Parkinson disease and parkinsonian disorders, tardive dyskinesia, lingual-facial-buccal dyskinesia, torsion dystonia, neuroleptic malignant syndrome, epilepsy
- Cardiovascular and tumour-related: hypertension, hypertensive disorder, pheochromocytoma/phaeochromocytoma, sympathetic paraganglioma, adrenal gland cancer, heart cancer
- Gastrointestinal: active peptic ulcer disease, duodenum cancer, small intestine cancer
- Metabolic and organ-related: porphyria (inherited porphyria, porphyrin metabolism disease), cirrhosis of liver, impaired renal function, pyruvate dehydrogenase E3 deficiency, methemoglobinemia due to methemoglobin reductase deficiency
- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder

Note that "active peptic ulcer disease" appears among the knowledge-graph contraindications, which runs against the predicted ulcer indication and warrants careful review.

**Drug Interactions:** 100 interactions were found; the first 20 retrieved are summarized here.
- **Major:** Tramadol, Amisulpride
- **Moderate:** Abiraterone, Fentanyl, Codeine, Dihydrocodeine, Alfentanil, Alprazolam, Amitriptyline, Amantadine, Amifampridine, Amobarbital, Chlorpheniramine, Cetirizine, Phenyltoloxamine, Dichloralphenazone, Ethanol, topical lidocaine and ophthalmic tetracaine
- **Minor:** Acetaminophen

Several of the interactions involve CNS depressants and opioids. Please refer to the package insert for label warnings, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There is no direct clinical evidence that metoclopramide heals gastric ulcers. The only trial concerns pre-endoscopy visualization in GI bleeding, the literature is mostly general reviews, and the high TxGNN score mainly reflects overlap with the original GERD and esophagitis indications.
- Metoclopramide offers no acid suppression or mucosal healing, standard therapy is far more effective, and active peptic ulcer disease appears among its knowledge-graph contraindications. The perforation indication in particular should not be pursued.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (currently missing, and blocking safety screening)
- Mechanism of action data (for example from DrugBank)
- Results of NCT05746377 and the 2024 and 2026 visualization RCTs, to define whether a narrower pre-endoscopy use in upper GI bleeding is worth pursuing as a separate question
- Clarification of the safety conflict with active peptic ulcer disease
- Current US market status check, since all 10 generic licenses are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

