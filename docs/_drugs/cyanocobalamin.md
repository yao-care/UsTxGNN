---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 553
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin is the synthetic form of Vitamin B12, used clinically to treat B12 deficiency states including pernicious anemia, subacute combined degeneration of the spinal cord, and nutritional deficiency.
The TxGNN model predicts it may have therapeutic relevance for **Biotin Metabolic Disease**, with **15 clinical trials** and **20 publications** identified — though most evidence reflects shared metabolic pathway biology rather than direct drug-disease intervention.
Current data supports a mechanistic research question rather than near-term clinical development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin B12 deficiency (pernicious anemia, nutritional supplementation) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cyanocobalamin (Vitamin B12) serves as an obligatory cofactor in two fundamental enzymatic reactions: the conversion of methylmalonyl-CoA to succinyl-CoA via methylmalonyl-CoA mutase, and the remethylation of homocysteine to methionine via methionine synthase. Both reactions sit at the core of organic acid metabolism — the same metabolic network that is disrupted in biotin metabolic disease.

Biotin metabolic disease encompasses biotinidase deficiency, holocarboxylase synthetase deficiency, and biotin transporter defects, all of which impair multiple biotin-dependent carboxylase enzymes. This leads to accumulation of propionic acid and methylmalonic acid — the same organic acids that accumulate in B12-responsive methylmalonic acidemia (MMA). The clinical and biochemical overlap is well-documented: published literature (PMID 23622402, PMID 11031989) explicitly classifies cobalamin and biotin together as the two core vitamins in vitamin-responsive metabolic diseases, and therapeutic megavitamin protocols historically tested both in overlapping enzyme deficiency states.

However, it is critical to recognize that the first-line treatment for biotin metabolic disease is biotin itself, not cyanocobalamin. The TxGNN high score (99.60%) most plausibly reflects the proximity of B12 and biotin nodes within the knowledge graph's organic acid metabolism subnetwork rather than an established therapeutic equivalence. No clinical trial has directly tested cyanocobalamin as a primary or adjunctive agent for biotin metabolic disease. This prediction is scientifically grounded as a metabolic co-factor interaction hypothesis, but the knowledge graph architecture may be amplifying biological adjacency into a spuriously high repurposing score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Baby Detect genomic newborn screening covering 126 treatable conditions including biotinidase deficiency; highest disease relevance but is a screening study, not a cyanocobalamin treatment intervention |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Randomised trial of carglumic acid (Carbaglu) in Propionic Acidemia and Methylmalonic Acidemia; organic acidemia overlap with biotin metabolic disease is scientifically relevant, though drug tested is not cyanocobalamin |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | Enrolling by invitation | 30,000 | Early Check pre-symptomatic newborn screening platform; broad rare disease panel may include biotin metabolic disorders for early identification |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Metabolic support therapy (Q10 ubiquinol + B and E vitamins) in autism/Phelan-McDermid syndrome; B-vitamin complex included but biotin metabolic disease is not the primary outcome |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional intervention addressing methylation and oxidative stress in autism; tests B-vitamin pathway correction but connection to biotin metabolic disease is indirect |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Unknown | 1,963 | Nutritional genomics platform for dietary-disease interaction research; broad recruitment scope, not designed around biotin metabolic disease |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Fortified food vs. milk in malnourished children; includes serum B12 measurement but biotin metabolic disease is not a study outcome |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption post-bariatric surgery; assesses micronutrient levels including B12 but not targeted at biotin metabolic disease |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin and mineral supplementation for diabetic neuropathy and nephropathy; indirect B12 involvement, not a biotin metabolic disease study |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | Terminated | 5 | Fiber and biotin supplementation to improve gut microbiota pre-bariatric surgery; terminated early with N=5, no valid data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Most directly relevant: explicitly classifies cobalamin and biotin together as core vitamins in vitamin-responsive metabolic diseases; describes shared clinical features between inborn errors of cobalamin metabolism and biotin-deficient multiple carboxylase deficiency |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Molecular Sciences | B12 deficiency and nervous system impairment; notes that B12 acts as cofactor for succinyl-CoA synthesis from methylmalonyl-CoA with biotin co-participation — establishes the direct enzymatic link to the biotin metabolic network |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Clinical Study | Pediatric Research | In vivo propionate metabolism measured in patients with PA, MMA, and multiple carboxylase deficiency; includes B12-responsive MMA subgroup — directly relevant to organic acid overlap between B12 and biotin metabolic disorders |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Vitamin dependency syndromes; covers B12- and biotin-responsive enzyme deficiency categories and their differential diagnosis |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatric Clinics of North America | Megavitamin therapy in aminoacidopathies; documents therapeutic trials of B12 and biotin in cofactor-responsive enzyme deficiencies, with dosing guidance for metabolic disease |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Advances in Clinical Chemistry | Vitamin-responsive inborn errors of metabolism; systematic review of therapeutic vitamin supplementation including B12 across enzyme deficiency states with overlapping organic acid pathology |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases; categorises vitamin-dependent syndromes and mechanism of pharmacological vs. nutritional dosing for cofactor-deficient enzymes |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Animal Study | J Endocrinology | B12 deficiency produces prediabetic metabolic phenotype in rats including glucose intolerance and ketogenesis; demonstrates B12's systemic role in metabolic homeostasis beyond classical hematological effects |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine Metabolic Immune Disorders Drug Targets | Vitamins and type 2 diabetes; reviews biotin and B-group vitamins including B12 in glucose metabolism regulation — illustrates functional co-dependency in metabolic pathways |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Annals NY Academy of Sciences | Interactions of B-complex vitamins in metabolic and catabolic reactions; establishes the biochemical rationale for treating B-vitamin interactions as an integrated enzymatic network |

---

## Taiwan Market Information

Cyanocobalamin is currently **not marketed in Taiwan** (未上市) with no approved drug licenses on record. No dosage form or route-of-administration data is available from Taiwan regulatory sources.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological connection between cyanocobalamin and biotin metabolic disease is mechanistically coherent — both cofactors operate within the same organic acid metabolism network — but no clinical trial has directly tested cyanocobalamin as a treatment for biotin metabolic disease. The TxGNN score of 99.60% reflects knowledge graph topology (B12 and biotin node proximity) rather than proven therapeutic efficacy, and the established first-line therapy for biotin metabolic disease is biotin supplementation itself, not B12. Evidence is currently at L4 (mechanistic/preclinical rationale only), insufficient to advance without further targeted research.

**To proceed, the following is needed:**
- Retrieve full MOA and pharmacological profile from DrugBank (DB00115) to confirm the enzymatic pathway overlap with biotin-dependent carboxylases
- Clarify the specific biotin metabolic disease subtype being targeted: biotinidase deficiency, holocarboxylase synthetase deficiency, or biotin transporter deficiency — each has different mechanistic implications for B12 co-supplementation
- Conduct a systematic literature review focused on case reports of B12-responsive MMA with concurrent biotin metabolic disease, where combined therapy was used
- Design a preclinical study to evaluate cyanocobalamin as adjunctive therapy alongside biotin in a biotinidase-deficient animal model
- Evaluate Taiwan regulatory pathway for cyanocobalamin (currently 未上市) before any clinical development plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

