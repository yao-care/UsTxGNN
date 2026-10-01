---
layout: default
title: Arginine
parent: Model Prediction Only (L5)
nav_order: 396
evidence_level: L5
indication_count: 1
---

# Arginine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Arginine: Repurposing Prediction for Gastroparesis

## One-Sentence Summary

Arginine is a marketed amino-acid drug, and the Evidence Pack does not list an approved original indication for it.
The TxGNN model predicts it may be effective for **gastroparesis**, but the support is so far only **1 registered trial (not relevant to arginine)** and **9 publications, all preclinical or a single case report**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. The rationale below comes from the mechanistic link in the prediction record.

Arginine is the substrate of neuronal nitric oxide synthase (nNOS), which makes nitric oxide. Nitrergic signaling helps the stomach relax to accept food (gastric accommodation) and helps the pyloric sphincter open. Loss or dysfunction of nitrergic neurons is a recognized feature of diabetic gastroparesis. If the nitrergic pathway is short of substrate, giving arginine could in principle support it.

Preclinical papers point in this direction:
- Glucocorticoid-induced gastroparesis in mice was linked to depletion of L-arginine (PMID 25057793).
- Deficiency of BH4, the nNOS cofactor, caused gastroparesis in newborn mice (PMID 23639814).
- Impaired nitrergic pyloric relaxation was reported in a rat Parkinson's model (PMID 35380456).

All of this evidence comes from animals and is indirect. No human interventional data for arginine in gastroparesis were provided. The high TxGNN score therefore rests on knowledge-graph prediction plus mechanistic plausibility, not on clinical confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | Unknown | 150 | Observational study of autologous pancreatic islet transplantation for glycaemic control after pancreatectomy. It does not test arginine or target gastroparesis, so it gives no direct or supportive evidence (relevance grade C). |

## Literature Evidence

No randomized trials or reviews were found. All entries are preclinical studies unless noted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Preclinical (mouse) | Endocrinology | Oral dexamethasone caused gastroparesis and stomach enlargement in mice. The effect was tied to depletion of L-arginine and depended on the glucocorticoid receptor. |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Preclinical (mouse) | Am J Physiol Gastrointest Liver Physiol | BH4 (nNOS cofactor) deficiency in newborn mice was associated with gastroparesis and abnormal gastric emptying. |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | In a 6-OHDA Parkinson's rat model with gastroparesis, nitrergic relaxation of the pyloric sphincter was impaired. |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Preclinical (rat) | Neurogastroenterol Motil | Decreased nNOS expression and function is proposed as a mechanism of diabetic gastroparesis. Studied in the jejunum of diabetic BB-rats. |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Preclinical (dog) | Am J Physiol Gastrointest Liver Physiol | Synchronized gastric electrical stimulation improved vagotomy-induced impaired gastric accommodation via the nitrergic pathway. |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Preclinical (rodent) | Am J Physiol Gastrointest Liver Physiol | Hyperglycemia inhibits gastric motility through KATP channels in vagal nodose ganglia. |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Preclinical (mouse) | World J Gastroenterol | Studied ghrelin and GHRP-6 as gastric motility therapies in diabetic mice with gastroparesis. Arginine was not tested. |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | Sacral nerve stimulation increased gastric accommodation through spinal afferent and vagal efferent pathways. Arginine was not tested. |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case report | Am J Case Rep | Lifestyle changes normalized serum lactate in an m.3243A>G (MELAS) carrier. Little direct relevance to arginine in gastroparesis. |

## US Market Information

The Evidence Pack contains no approved-indication text for any of these products. Two entries list the product Velsipity (NDA216956), and two list no NDA number.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA216956 | Velsipity | Film-coated tablet | U.S. Pharmaceuticals |
| NDA216956 | Velsipity | Film-coated tablet | Pfizer Laboratories Div Pfizer Inc |
| NDA016931 | R-Gene | Solution for injection | Pharmacia & Upjohn Company LLC |
| No NDA number listed | L-Arginine High | Liquid | Professional Complementary Health Formulas |
| No NDA number listed | L-Arginine | Liquid | Professional Complementary Health Formulas |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.42%), but the evidence is preclinical only (L4, stage S0). The one registered trial does not test arginine, and no human data exist for gastroparesis. Package-insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications, to complete safety screening.
- Mechanism-of-action data for arginine from DrugBank.
- Approved-indication information for the listed US products.
- Human evidence, such as pilot or exploratory clinical studies of arginine or nitric-oxide pathway modulation in gastroparesis.
- A route-compatibility assessment (oral, injectable or other), which is still pending.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

