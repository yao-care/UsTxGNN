---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 2
---

# Biotin
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

# Biotin: From Nutritional Supplementation to Dyspepsia

## One-Sentence Summary

Biotin (Vitamin B7) is an essential water-soluble vitamin, historically indicated for the treatment and prevention of biotin deficiency and used broadly as a nutritional supplement.
The TxGNN model predicts it may be effective for **Dyspepsia**,
with **2 clinical trials** and **7 publications** retrieved during the evidence search — however, the majority carry only indirect relevance to this specific repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Biotin deficiency; nutritional supplementation (Vitamin B7) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| US Market Status | Not marketed as prescription drug (available OTC as dietary supplement) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Biotin (Vitamin B7) functions as an obligate coenzyme for four carboxylase enzymes: pyruvate carboxylase, acetyl-CoA carboxylase, propionyl-CoA carboxylase, and 3-methylcrotonyl-CoA carboxylase. These enzymes are central to fatty acid synthesis, gluconeogenesis, and amino acid catabolism — processes that sustain rapid cell turnover in the gastrointestinal epithelium. When biotin is deficient, the energy supply to gastric mucosal cells may be compromised, theoretically impairing acid secretion and mucosal barrier integrity, which could manifest as dyspeptic symptoms such as nausea, early satiety, and epigastric discomfort.

Support for this pathway comes primarily from a case report documenting an infant diagnosed with dyspepsia who developed overt biotin deficiency while on an exclusive amino acid formula (PMID 15863846). Separately, a multi-centre open study found that a composite supplement containing biotin (among other ingredients including sodium alginate, ginger, and α-galactosidase) improved symptoms in functional dyspepsia patients following H. pylori eradication (PMID 25384804). However, because this was a multi-ingredient intervention, biotin's individual contribution cannot be isolated.

Overall, the mechanistic connection is biologically plausible but remains at the level of indirect inference. No single-agent biotin trial targeting dyspepsia exists, and the TxGNN prediction likely reflects shared biological pathways between vitamin co-factor deficiency and gastrointestinal mucosal dysfunction rather than a direct pharmacological effect of biotin supplementation on functional dyspepsia per se.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Assessed serum micronutrient concentrations (including biotin) in post-bariatric surgery patients using a transdermal vitamin patch; primary endpoint was pharmacokinetic absorption, not dyspepsia symptom relief. Indirect relevance only. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Compared oxycodone versus pregabalin as preemptive analgesia for postoperative pain in elective surgeries; unrelated to biotin or dyspepsia. Likely a data collection artifact — should be excluded from evidence evaluation. |

> **Note:** Neither trial provides direct evidence for biotin efficacy in dyspepsia. Both are classified as grade C relevance by the evidence curator.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical Trial (open, multi-centre) | Minerva Gastroenterologica e Dietologica | Multi-component supplement (containing biotin, sodium alginate, pineapple, papaya, ginger, α-galactosidase) showed symptomatic benefit in functional dyspepsia after H. pylori eradication; biotin's individual contribution cannot be separated from other ingredients |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | The Journal of Dermatology | Biotin deficiency in a 5-month-old infant who had been diagnosed with dyspepsia and fed exclusively on amino acid formula; serum and urine biotin were subnormal; skin and GI symptoms resolved with biotin supplementation |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Interventional Review | Experimental & Clinical Gastroenterology | Evaluated Stimbifid (containing inulin, oligofructose, biotin, and other B-vitamins) for intestinal microbiota correction in bronchopulmonary patients on antibiotics; indirect GI relevance; biotin is one of many active components |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | International Journal of Molecular Medicine | Investigated stomach antral endocrine cells in IBS patients vs. healthy controls; provides mechanistic background on GI endocrine pathophysiology relevant to dyspepsia, no direct biotin connection |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World Journal of Gastrointestinal Endoscopy | Studied endocrine cell types in the oxyntic mucosa of IBS patients; background pathophysiology study without biotin-specific findings |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | Journal of Clinical Pathology | Examined IL-10 expression in H. pylori-associated gastritis; provides context for dyspepsia immune pathogenesis, no biotin link |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney International | Investigated small bowel T cells and GroEL stress protein in IgA nephropathy; minimal relevance to biotin or dyspepsia |

---

## US Market Information

Biotin is not registered as a prescription pharmaceutical product in the United States. It is widely available as an over-the-counter dietary supplement regulated under 21 CFR Part 101, and does not require an NDA/BLA filing. No prescription drug authorizations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No NDA/BLA on record | — | Biotin is regulated as an OTC dietary supplement, not a prescription drug |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** TFDA package insert warnings and contraindications (DG001) and detailed mechanism of action data (DG002) were not retrievable during this evidence collection cycle. No drug-drug interaction data were identified in the DDI database query. These gaps should be resolved before any clinical safety evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high computational prediction score (99.43%) for biotin in dyspepsia, the available clinical evidence is weak (L4) — the only interventional data come from a multi-ingredient supplement study where biotin's individual contribution cannot be isolated, and the mechanistic pathway linking biotin to dyspepsia remains speculative and indirect. The totality of evidence does not yet meet the threshold required to advance this candidate toward a formal development decision.

**To proceed, the following is needed:**

- **Mechanistic validation:** A dedicated in vitro or animal study establishing biotin's direct role in gastric mucosal energy metabolism and barrier function
- **Single-agent clinical signal:** A prospective study or retrospective cohort evaluating biotin supplementation alone (not as part of a multi-nutrient formula) in dyspepsia patients, particularly those with confirmed biotin deficiency
- **Deficiency prevalence data:** Characterise the prevalence of biotin insufficiency in functional dyspepsia patient populations to identify a biologically enriched subgroup most likely to respond
- **Data gap resolution:** Obtain TFDA package insert (DG001) and DrugBank MOA data (DG002) to complete the S1 safety screening before any regulatory pathway assessment
- **Dose-finding context:** Determine whether therapeutic (supraphysiological) doses of biotin are required for a GI effect, or whether correction of subclinical deficiency alone is sufficient
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

