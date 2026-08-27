---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 733
evidence_level: L5
indication_count: 1
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Folic Acid: From Vitamin B9 Supplementation to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (Vitamin B9, DrugBank DB00158) is not currently marketed in the US and has no original indication on file in this evidence pack. The TxGNN model predicts a possible link to **Biotin Metabolic Disease**, but the supporting evidence — **13 clinical trials** and **20 publications** — is largely non-specific nutritional/vitamin research, and the drug's own mechanistic rationale flags this prediction as a **likely false positive**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no original indications or US licenses on file) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for folic acid in this evidence pack. Based on known pharmacology, folic acid (Vitamin B9) participates in one-carbon metabolism via the DHFR/MTHFR pathway, while biotin (Vitamin B7) functions as a cofactor for carboxylase enzymes — these are two distinct vitamin-coenzyme systems with no known shared enzyme or metabolic pathway.

Biotin metabolic disease typically refers to biotinidase deficiency or holocarboxylase synthetase deficiency, both of which are standardly treated with biotin supplementation itself, not folic acid. The reviewer notes accompanying this prediction explicitly assess it as a **potential false positive**: the high TxGNN score most likely reflects structural proximity within the knowledge graph between "vitamin supplementation" and "metabolic disease" node clusters, rather than a genuine mechanistic relationship.

Given this, the mechanistic rationale for repurposing folic acid toward biotin metabolic disease is weak, and any further evaluation should specifically test for a real pharmacological link rather than assume one from the prediction score alone.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Metabolic support therapy (Q10 ubiquinol + multivitamin B/E) in idiopathic and Phelan-McDermid syndrome autism; not specific to biotin metabolic disease or folic acid |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Unknown | 1963 | General nutritional genomics clinical trial platform; not disease-specific |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1000 | Fortified food vs. milk on micronutrient status (including serum folic acid) in malnourished children; no direct link to biotin metabolic disease |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption in post-bariatric surgery patients; unrelated to biotin metabolic disease treatment |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional intervention for oxidative stress/methylation impairment in autism; not a biotin metabolic disease indication |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and neurodevelopment; intervention is iodine, not folic acid |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6824 | Universal newborn genomic screening (may include biotinidase deficiency screening) but is a screening study, not a treatment trial |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin/mineral supplementation for diabetic neuropathy/nephropathy; not biotin metabolic disease |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient intervention as palliative therapy in congestive heart failure; not disease-specific |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completed | 202 | Multivitamin/mineral and fatty acid supplementation on impulsivity/aggression; unrelated to biotin metabolic disease |

**Note:** None of the identified trials directly test folic acid for biotin metabolic disease; all are general nutritional/vitamin studies rated relevance grade C.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders including cobalamin, folate, biotin, B1 and E; folate and biotin discussed as distinct deficiency syndromes, not interchangeable |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Reviews movement disorders in treatable inborn errors of metabolism, a category that includes biotin-responsive conditions |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Not classified | Biologica Latina | Animal model of combined vitamin H (biotin) and folic acid deficiency; demonstrates the two are distinct, co-occurring but separate deficiencies |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Reviews Vitamin B12 as cofactor linking biotin and folic acid synthesis pathways to methionine production; indirect mechanistic context only |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Reviews vitamins (including biotin) and type 2 diabetes; not specific to biotin metabolic disease |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Reviews vitamins and type 2 diabetes, notes lower biotin/thiamine/pyridoxine in diabetics; not disease-specific |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | General review of B vitamin roles in dermatology, including biotin |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterology Clinics of North America | Reviews vitamin/mineral deficiencies in IBD; not biotin metabolic disease specific |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | General review of vitamins in metabolic disease pathogenesis and treatment mechanisms |
| [16343871](https://pubmed.ncbi.nlm.nih.gov/16343871/) | 2006 | Not classified | Archives de Pédiatrie | Reviews neonatal epilepsy from inborn errors of metabolism, a category overlapping with biotin metabolic disease |

**Note:** The literature base is predominantly general vitamin/metabolism reviews; no publication directly evaluates folic acid as a treatment for biotin metabolic disease.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug's own repurposing rationale flags this TxGNN prediction as a likely false positive driven by knowledge-graph structural proximity rather than a genuine mechanistic link — folic acid and biotin operate through distinct, non-overlapping coenzyme pathways, and biotin metabolic disease is standardly treated with biotin itself, not folic acid. Evidence level is L4 (mechanism/preclinical only), no clinical trial or publication directly supports this specific drug-disease pairing, and the drug currently has no US marketing authorization.

**To proceed, the following is needed:**
- Confirmation of folic acid's mechanism of action (MOA) from DrugBank to formally assess mechanistic plausibility
- TFDA/FDA label warnings and contraindications (currently blocking safety review, per data gap DG001)
- A targeted literature or trial search specifically on folic acid in biotinidase deficiency or holocarboxylase synthetase deficiency, rather than general vitamin/metabolism studies
- Re-evaluation of the TxGNN prediction itself, given the internally flagged risk of a knowledge-graph structural false positive
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

