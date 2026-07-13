---
layout: default
title: Thiamine
parent: 僅模型預測 (L5)
nav_order: 640
evidence_level: L5
indication_count: 4
---

# Thiamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Thiamine: From Thiamine Deficiency to Hyperthyroidism

## One-Sentence Summary

Thiamine (Vitamin B1) is an essential cofactor for mitochondrial energy metabolism, classically used to prevent and treat thiamine deficiency conditions including beriberi and Wernicke's encephalopathy. The TxGNN model predicts it may have therapeutic value as **adjunctive supplementation in Hyperthyroidism** — not as a primary antithyroid agent, but to correct the secondary thiamine depletion driven by the hypermetabolic state. There is currently **1 completed pilot clinical trial** and **20 publications** supporting this mechanistic direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thiamine deficiency, beriberi, Wernicke's encephalopathy |
| Predicted New Indication | Hyperthyroidism (adjunctive thiamine supplementation) |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Market Status (Taiwan FDA) | Not marketed (未上市) |
| Number of Approved Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, Thiamine (Vitamin B1) serves as an indispensable cofactor for two key mitochondrial enzyme complexes: pyruvate dehydrogenase (PDH) and alpha-ketoglutarate dehydrogenase (α-KGDH). Both are central to aerobic energy metabolism — their impairment from either dietary deficiency or accelerated consumption results in cardiac dysfunction (wet beriberi) and neurological injury (Wernicke's encephalopathy).

Hyperthyroidism creates a sustained hypermetabolic state: elevated thyroid hormones increase basal metabolic rate by 60–100%, dramatically accelerating thiamine turnover throughout peripheral tissues. Multiple animal studies (1958, 1963) and human physiological studies (1955) have documented reduced tissue thiamine stores and altered urinary thiamine excretion in hyperthyroid subjects. When consumption outpaces dietary intake, secondary thiamine deficiency develops — clinically manifesting as high-output heart failure or Wernicke's encephalopathy, both well-documented in the case literature.

This prediction is therefore mechanistically grounded in an **"adjunctive deficiency correction"** model: thiamine supplementation in hyperthyroid patients does not treat the thyroid dysfunction itself, but prevents or reverses the downstream metabolic crisis caused by accelerated vitamin depletion. This parallels the established use of thiamine supplementation in chronic alcoholism or prolonged parenteral nutrition — conditions similarly characterized by high consumption or impaired absorption rather than primary vitamin deficiency.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | Not applicable (Pilot) | Completed | 12 | Pilot study assessing prevalence of thiamine deficiency and improvement in cardiovascular function after thiamine supplementation in severe thyrotoxicosis. Designed around the observation that thyrotoxicosis increases thiamine utilization, potentially worsening cardiac output through beriberi-like mechanisms. Results from 2014–2016. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case Report | Crit Care Nurs Clin North Am | High-output heart failure caused by concurrent thyrotoxicosis and wet beriberi; highlights overlapping cardiovascular pathophysiology when both thiamine deficiency and hyperthyroidism co-exist |
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case Report | Cureus | Wernicke's encephalopathy in gestational hyperthyroidism with hyperemesis gravidarum; thiamine deficiency confirmed and reversed with IV supplementation |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case Report | J Gen Intern Med | Thyrotoxicosis-associated Wernicke's encephalopathy in a non-alcoholic patient; establishes hyperthyroidism as an independent precipitant of clinically significant thiamine depletion |
| [36593922](https://pubmed.ncbi.nlm.nih.gov/36593922/) | 2023 | Case Report | Radiology Case Reports | Uncommon Wernicke-Korsakoff syndrome presentation in a pregnant patient with pre-gestational hyperthyroidism; MRI-confirmed and resolved with thiamine |
| [25148818](https://pubmed.ncbi.nlm.nih.gov/25148818/) | 2014 | Case Report | Endocr Pract | Gestational thyrotoxicosis combined with hyperemesis gravidarum leading to Wernicke's encephalopathy; thiamine supplementation was both therapeutic and preventive |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case Report | Cureus | Non-alcoholic Wernicke's encephalopathy precipitated by hyperthyroidism-related vomiting and poor oral intake; the neurological deterioration reversed with thiamine |
| [34995426](https://pubmed.ncbi.nlm.nih.gov/34995426/) | 2021 | Case Report | S D Med | Wernicke's encephalopathy in a Graves' disease patient after sleeve gastrectomy; compounded thiamine deficiency from surgical malabsorption and uncontrolled thyrotoxicosis |
| [22436368](https://pubmed.ncbi.nlm.nih.gov/22436368/) | 2013 | Case Report | Neurologia | Wernicke's encephalopathy secondary to hyperthyroidism combined with thiaminase-rich dietary intake; demonstrates multi-factorial thiamine depletion risk in hyperthyroid patients |
| [21064291](https://pubmed.ncbi.nlm.nih.gov/21064291/) | 1946 | In Vitro / Mechanistic | Fed Proc | Early mechanistic study documenting the combined effect of thiamine deficiency and hyperthyroidism on cardiac muscle ATP content and ATPase activity in rats; establishes metabolic intersection |
| [13934469](https://pubmed.ncbi.nlm.nih.gov/13934469/) | 1963 | Animal Study | Ann Biochem Exp Med | Demonstrated reduced thiamine tissue storage and altered intestinal thiamine synthesis in hyperthyroid rats; provides direct biological evidence that thyrotoxicosis depletes systemic thiamine reserves |

---

## Market Information (Taiwan FDA)

No approved products found in the Taiwan FDA database. Thiamine (Vitamin B1) registered zero pharmaceutical licenses in this search. It is widely available as a nutritional supplement and appears as a component in multi-vitamin preparations, but no NDA records were retrieved as a standalone therapeutic product.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between hyperthyroidism-driven hypermetabolism and secondary thiamine depletion is biologically plausible, internally consistent, and corroborated by multiple case reports across two decades (Evidence Level L3). The critical distinction is that this is **adjunctive supplementation to correct a secondary deficiency**, not a competing antithyroid treatment — which makes the safety bar low and the benefit-risk ratio favorable. However, the only prospective data is a single pilot study (n=12, no formal control arm), insufficient to establish efficacy without further study.

**To proceed, the following is needed:**

- **Confirmatory RCT**: A well-designed Phase 2 trial evaluating thiamine supplementation in moderate-to-severe hyperthyroid patients, with pre-specified endpoints for cardiovascular function (LVEF, cardiac output, BNP), neurological status, and thiamine biomarkers (whole-blood thiamine diphosphate)
- **Biomarker screening protocol**: Identify which hyperthyroid patients are actually thiamine-deficient at baseline — supplementation benefit is likely concentrated in those with documented low thiamine levels, poor nutritional status, or coexisting hyperemesis
- **Safety documentation**: Retrieve TFDA package insert and DrugBank MOA data (both currently data gaps per DG001 and DG002)
- **Population segmentation**: Priority subgroups include severe/uncontrolled thyrotoxicosis, patients with concurrent vomiting or poor oral intake, post-bariatric patients with Graves' disease, and pregnant patients with gestational thyrotoxicosis

> **Note on additional TxGNN predictions:** Ranks 2–4 (THRβ mutation resistance, primary hereditary glaucoma, open-angle glaucoma) were also evaluated. Rank 2 and 3 are classified **Hold (L5)** — no supporting evidence and weak mechanistic rationale. Rank 4 (open-angle glaucoma) reaches **L4** based on observational data showing lower blood thiamine in glaucoma patients and a small combination-formula trial; this warrants a separate research question but is not actionable without a thiamine-specific intervention study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

