---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 733
evidence_level: L5
indication_count: 1
monitor_inn: "FOLIC ACID"
predicted_indications: ["biotin metabolic disease"]
last_modified_at: 2026-10-28
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin deficiency disorder"
---

# Folic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Folic Acid: From Vitamin Deficiency and Folate-Deficiency Anemia to Biotin Metabolic Disease
{: .text-alpha }

## One-Sentence Summary

Folic acid (vitamin B9) was originally used to treat vitamin deficiency disorders and anemias, especially folate-deficiency anemia.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**,
but there are **0 clinical trials** and only indirect literature (**20 publications**, mostly general reviews of B vitamins) behind this prediction, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; folic acid deficiency anemia (other anemias: iron deficiency, hypochromic, deficiency, microcytic) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 8) |
| Number of NDAs | 8 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Folic acid is a water-soluble B vitamin that serves as a cofactor in one-carbon metabolism, supporting nucleotide synthesis and methylation. Its efficacy in correcting folate deficiency and the related anemias is well established.

Biotin (vitamin B7) is also a water-soluble B vitamin. It acts as the cofactor for carboxylases involved in fatty acid synthesis, gluconeogenesis and amino acid catabolism. The two vitamins sit in metabolically adjacent pathways, and the retrieved literature often discusses B vitamins together (for example, vitamin-responsive disorders and vitamins in metabolic disease). The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

This is a pathway-level association only. Folic acid does not replace biotin and would not correct biotinidase or holocarboxylase synthetase deficiency, which are the usual causes of biotin metabolic disease. The prediction is therefore not supported by clinical data and should be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved publications tests folic acid in biotin metabolic disease. They are mostly general reviews of vitamins, and a few are animal or observational studies. The ten most relevant are listed below, with reviews first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Vitamin-responsive disorders (cobalamin, folate, biotin, B1, E); covers inborn errors of vitamin absorption, transport and metabolism |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | International Journal of Molecular Sciences | Vitamin B12 deficiency and the nervous system; notes the shared biochemical roles of B12, biotin and folic acid |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | Overview of B vitamins in cellular metabolism and dermatology |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; thiamine, pyridoxine and biotin levels are lower in diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | Individual and combined vitamins in type 2 diabetes |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Archives of Biochemistry and Biophysics | Micronutrient deficiencies (B12, folic acid, B6 and others) and DNA damage; argues for optimal supplementation |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases: malabsorption, metabolic errors and vitamin-dependent syndromes |
| [39828265](https://pubmed.ncbi.nlm.nih.gov/39828265/) | 2025 | Umbrella review | Asia Pacific Journal of Clinical Nutrition | Water-soluble vitamins and glycemic control; prior meta-analyses were inconsistent |
| [38350491](https://pubmed.ncbi.nlm.nih.gov/38350491/) | 2025 | Cohort | Nutrition Reviews | Micronutrient status in children with severe wasting or nutritional edema |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Combined biotin (vitamin H) and folic acid deficiency induced in rats on a purified diet |

## US Market Information

All eight US authorizations for folic acid are valid, and no approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040796 | Folic Acid (Aphena Pharma Solutions) | Tablet | Not recorded |
| ANDA211064 | Folic Acid (A-S Medication Solutions) | Tablet | Not recorded |
| ANDA040625 | Folic Acid (Cardinal Health 107) | Tablet | Not recorded |
| ANDA202437 | Folic Acid (Cadila Pharmaceuticals) | Tablet | Not recorded |
| NDA216395 | Folic Acid (Ayurax) | Solution | Not recorded |

Three further cancelled authorizations are not listed here: two injection solutions (ANDA089202, Fresenius Kabi; ANDA202522, XGen) and one tablet (ANDA204418, Sunrise Pharmaceutical).

## Safety Considerations

No package insert warnings or contraindications are available in the data compiled for this report.

- **Drug Interactions**: The interaction query returned 100 records, with a sample of 20 reviewed. Most are of unknown severity. The only ones with a graded level are **pancrelipase (Moderate)** and **sulfasalazine (Minor)**. Other listed drugs include calcitriol, pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, acarbose, rosiglitazone, mesalazine, sucralfate, prednisone, triamcinolone, simvastatin, morphine, vancomycin, lactulose, nizatidine and palonosetron.
- **Knowledge-graph contraindication signals** (not label text, so they need verification against the package insert): kidney disease, nephrolithiasis, diabetes and diabetic ketoacidosis, bipolar disorder, peptic ulcer disease, hypercalcemia, hyperparathyroidism, sickle cell anemia, hemolytic anemia, hereditary hemochromatosis, Wilson disease, inflammatory bowel disease and ulcerative colitis, among others.

For definitive safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and general vitamin reviews. There are no clinical trials and no direct evidence (Evidence Level L5). Folic acid does not substitute for biotin and would not correct the usual enzymatic causes of biotin metabolic disease. In addition, although the drug is marketed in the US with eight valid licenses, the package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label, which is currently a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank)
- A clear definition of which biotin-related disorder is meant (biotinidase deficiency, holocarboxylase synthetase deficiency, or another) and a mechanistic case for any role of folic acid
- Preclinical or clinical evidence specific to folic acid in biotin metabolic disease
- Clarification of the cancelled US market status and the route and formulation to be used
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

