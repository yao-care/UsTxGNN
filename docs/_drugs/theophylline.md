---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 639
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Theophylline: From Asthma/COPD to Thrombotic Disease

## One-Sentence Summary

Theophylline is a well-established methylxanthine bronchodilator, historically used for asthma and COPD treatment (note: the original indications field in this dataset is empty, likely a data collection error — the repurposing rationale for rank-5 indication explicitly flags this). The TxGNN model predicts it may be effective for **Thrombotic Disease**, currently supported by **0 clinical trials** and **19 publications**, the majority of which are indirect or methodological rather than directly studying theophylline as an antithrombotic agent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma / COPD (historical; original_indications field empty in current dataset — likely data gap) |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L4 |
| US Market Status | Not Marketed (0 records found) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, theophylline is a non-selective phosphodiesterase (PDE3/PDE4) inhibitor and adenosine receptor antagonist. By blocking PDE enzymes, it elevates intracellular cyclic AMP (cAMP) levels. In the context of thrombosis, elevated platelet cAMP suppresses platelet activation and aggregation — a central mechanism in arterial thrombosis. Its adenosine receptor antagonism may further modulate the thrombotic microenvironment, as adenosine signaling regulates both platelet inhibition and vascular tone.

The mechanistic bridge is biologically plausible but largely inferential. cAMP elevation is a shared pathway in both airway smooth muscle relaxation and platelet inhibition, and clinically approved PDE inhibitors such as cilostazol are already used as antiplatelet agents — lending indirect support to this prediction. The repurposing rationale notes that theophylline's antithrombotic mechanism is extrapolated from other indications, and that no direct clinical bridge currently exists.

A critical interpretive caveat: much of the identified literature involves theophylline not as a therapeutic agent, but as a reagent in the CTAD anticoagulant cocktail (citrate–theophylline–adenosine–dipyridamole) used during blood collection in platelet studies. This distinction sharply limits the clinical relevance of the existing literature for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for theophylline in thrombotic disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Basic science | General Pharmacology | Milrinone (PDE inhibitor) combined with adenosine synergistically inhibits platelet aggregation via cAMP elevation in human PRP and whole blood — mechanistically analogous to theophylline's PDE inhibition |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Thromboxane A2 vs. prostacyclin antagonism in platelet aggregation and atherosclerosis; adenylate cyclase stimulation and cAMP increase identified as key antiplatelet mechanism |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay development | British Journal of Haematology | Theophylline included in EDTA–PGE1–theophylline anticoagulant cocktail to prevent in vitro platelet activation during PF4 measurement — demonstrates theophylline's platelet-inhibitory role as a reagent |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Biomarker study | Platelets | Soluble CLEC-2 evaluated as in vivo platelet activation marker for thrombotic disease risk; theophylline-containing anticoagulant used in sample processing |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Observational study | Inflammatory Bowel Diseases | Platelet–leukocyte aggregates elevated in IBD and thrombotic conditions; platelet and neutrophil co-activation characterised — provides thromboinflammatory context |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Methodological study | PLoS ONE | Demonstrates that theophylline-containing anticoagulant (CTAD) is essential to prevent artifactual platelet activation during plasma preparation for biomarker studies |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Ex vivo study | Rheumatology (Oxford) | Platelet and neutrophil activation in Behçet's disease; age and gender modulate thrombotic risk through platelet activation pathways |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Pharmacological study | Journal of Nutrition | Aged garlic extract inhibits platelet aggregation by suppressing GPIIb/IIIa activation via cAMP/cGMP pathway — confirms cAMP as a druggable antiplatelet target |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observational | Cor et Vasa | Significant elevation of theophylline-resistant T-helper cells observed in patients with myocardial infarction and thrombophlebitis — theophylline used as immunological cell-separation reagent |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical chemistry | Analytica Chimica Acta | Gold nanoparticle RNA aptasensor for theophylline detection; confirms theophylline's narrow therapeutic window and the need for plasma monitoring |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.62%), the supporting evidence for theophylline in thrombotic disease is entirely indirect. The identified literature primarily uses theophylline as a laboratory reagent in platelet studies rather than as a therapeutic agent, and no dedicated preclinical or clinical studies directly test its antithrombotic efficacy. With L4 evidence and no clinical trial data, this indication cannot progress without foundational validation work.

**To proceed, the following is needed:**
- Dedicated in vitro studies directly measuring theophylline's antiplatelet effects (ADP/collagen-induced aggregation assays) across clinically relevant concentrations
- In vivo thrombosis model studies (e.g., laser-induced or FeCl₃ carotid artery injury models) to establish proof of concept
- Mechanism of action confirmation: verify PDE3/PDE4 inhibitor classification via DrugBank API query to close the MOA data gap
- Safety profile retrieval: download and parse the package insert (FDA label) to obtain key warnings, contraindications, and drug interactions — currently all safety fields are empty
- Assessment of therapeutic window overlap: theophylline has a narrow therapeutic index (5–20 µg/mL for bronchodilation); antiplatelet efficacy doses may differ significantly
- Differentiation analysis versus established antiplatelet PDE inhibitors (cilostazol) to assess whether theophylline offers any clinical advantage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

