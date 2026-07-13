---
layout: default
title: Tetrabenazine
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazine: From Huntington's Disease Chorea to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

Tetrabenazine (brand name: Xenazine) is a VMAT2 inhibitor that depletes presynaptic monoamines and is approved by the US FDA for the treatment of chorea associated with Huntington's disease; it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 with or without Polycystic Liver Disease (PKD3)**,
with **0 clinical trials** and **20 retrieved publications** — however, the retrieved literature covers the disease background rather than any direct evidence of tetrabenazine efficacy in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chorea associated with Huntington's disease (US FDA-approved; not registered in Taiwan) |
| Predicted New Indication | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, tetrabenazine is a reversible inhibitor of vesicular monoamine transporter type 2 (VMAT2), which depletes presynaptic stores of dopamine, serotonin, and norepinephrine. This mechanism underpins its approved use in reducing involuntary choreiform movements in Huntington's disease. It has no established role in metabolic, renal, or hepatic disease.

Polycystic Kidney Disease 3 (PKD3) is caused by mutations in the **GANAB** gene, which encodes glucosidase II alpha subunit — an enzyme critical for N-linked glycoprotein processing in the endoplasmic reticulum. Defective glycosylation leads to misfolded polycystin proteins, triggering progressive renal and hepatic cyst formation. The disease is driven by primary ciliary dysfunction, mTOR pathway hyperactivation, and aberrant cholangiocyte fluid secretion — mechanisms entirely distinct from monoamine neurotransmission.

No pharmacological bridge between VMAT2 inhibition and PKD3 pathophysiology is currently established. As noted in the repurposing rationale embedded in the Evidence Pack, the high TxGNN score most likely reflects indirect topological proximity in the knowledge graph (neurological → metabolic/renal disease node clusters) rather than a genuine drug–disease mechanistic connection. This prediction is best classified as a knowledge graph artifact at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All 20 retrieved publications address polycystic kidney/liver disease pathophysiology, genetics, and clinical management — none specifically evaluate tetrabenazine in this context. They are listed below for disease background reference.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | *Lancet* | Comprehensive review of ADPKD as a systemic disorder; covers hypertension, hepatic cysts, intracranial aneurysms, and molecular genetics advances |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | *Annual Review of Pathology* | Mechanisms of polycystic liver disease — primary gene mutations, cyst initiation, and progression; mTOR and cAMP identified as therapeutic targets |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | *Clinics in Liver Disease* | ADPKD and PCLD clinical course; tolvaptan shown to slow renal cyst progression; hepatomegaly management strategies |
| [29175241](https://pubmed.ncbi.nlm.nih.gov/29175241/) | 2018 | Review | *Journal of Hepatology* | Clinical management of polycystic liver disease; surveillance recommendations, interventional options, and transplantation criteria |
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Clinical Guideline | *American Journal of Gastroenterology* | ACG guideline on focal liver lesions including hepatic cystic lesions and polycystic liver disease management |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Guideline | *Journal of Hepatology* | EASL Clinical Practice Guidelines on cystic liver diseases covering ADPKD, ADPLD, diagnosis, and management |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | *JASN* | Genetic complexity of ADPKD and ADPLD; 8 associated genes (including PKD1, PKD2, GANAB) with significant phenotypic and pathogenic overlap |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | *Advances in Kidney Disease and Health* | Genetic spectrum of polycystic diseases: PKD1 accounts for ~80% of ADPKD; two major and seven minor loci; genotype–phenotype correlations |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | *Hepatic Medicine* | PLD pathogenesis (ductal plate malformation, ciliary dysfunction, cell signaling abnormalities); symptomatic disease in 2–5% of patients |
| [40296340](https://pubmed.ncbi.nlm.nih.gov/40296340/) | 2025 | Cohort | *Annals of Transplantation* | Retrospective analysis of combined liver-kidney transplantation outcomes in 9 PLD patients (2015–2024); postoperative complication monitoring |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.90%) to tetrabenazine for PKD3, but no credible mechanistic link exists between VMAT2/monoamine depletion and the GANAB-driven N-linked glycosylation defects underlying polycystic kidney and liver disease. No clinical trials or disease-specific tetrabenazine literature were retrieved; all 20 retrieved publications describe the target disease in general rather than any tetrabenazine activity within it. The current evidence level is L5 — model prediction only.

**To proceed, the following is needed:**
- **Mechanistic hypothesis**: Identify a credible pharmacological pathway linking VMAT2 inhibition (or off-target tetrabenazine activity) to mTOR signaling, primary ciliary function, or cAMP-driven fluid secretion in GANAB-mutant cystogenesis
- **Preclinical data**: In vitro or animal model studies of GANAB-mutant cholangiocytes/renal tubular cells exposed to tetrabenazine or monoamine depletion
- **Biomarker correlation**: Any reported association between dopaminergic or serotonergic signaling and cyst growth markers in ADPKD/PKD3
- **Safety profile completion**: Resolve data gaps DG001 (TFDA package insert warnings/contraindications) and DG002 (full DrugBank MOA data) before any clinical planning
- **Nephrology expert review**: Specialist assessment of biological plausibility before committing resources to wet-lab or translational studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

