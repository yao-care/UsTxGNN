---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 935
evidence_level: L5
indication_count: 2
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
last_modified_at: 2026-10-28
description: "Misoprostol: predicted new indication Amenorrhea (evidence level L4). Approved use: Not available"
---

# Misoprostol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Misoprostol: From Gastric Ulcer Indication (Label Text Unavailable) to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analog; the approved-indication text for its US licenses was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are **0 registered clinical trials** and **7 publications** (mostly about pregnancy termination, not amenorrhea treatment) behind this prediction.
The evidence is weak, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved-indication text is empty in all license records) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 0.9964 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 5) |
| Number of NDAs | 5 (all cancelled; 1 NDA and 4 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, misoprostol is a prostaglandin E1 analog that induces uterine contraction and cervical ripening, and it is used clinically in uterine evacuation.

The link to amenorrhea is indirect. Misoprostol is used where absent menses are caused by pregnancy-related conditions (for example, missed abortion or anembryonic pregnancy), helping to empty the uterus and restore the cycle. The retrieved literature, however, shows no evidence that misoprostol treats amenorrhea itself. Most of the papers describe mifepristone plus misoprostol regimens for ending early pregnancy, where "amenorrhea" appears only as an inclusion criterion (for example, amenorrhea ≤35 days).

The high TxGNN score (0.9964) is a computational prediction only. It should not be read as proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reprod Sci | 744 women with amenorrhea ≤35 days; low-dose mifepristone with self-administered misoprostol for ultra-early medical abortion |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reprod Sci | 2,500 women; mifepristone 50–150 mg followed by 200 µg oral misoprostol for ultra-early pregnancy termination |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Prospective clinical study | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone with self-administered misoprostol for early pregnancy termination |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort/clinical study | Hum Reprod | Low-dose mifepristone plus misoprostol before expected menstruation to prevent unintended pregnancy |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation in the management of abnormal uterine bleeding (not specific to misoprostol) |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy; amenorrhea was a presenting symptom, unrelated to misoprostol treatment |

None of these papers tests misoprostol as a treatment for amenorrhea.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019268 | Cytotec (Pfizer) | Tablet | Not available; license valid |
| ANDA076095 | Misoprostol (GenBioPro) | Tablet | Not available; license valid |
| ANDA091667 | Misoprostol (Novel Laboratories) | Tablet | Not available; license valid |
| ANDA210201 | Misoprostol (AvPAK) | Tablet | Not available; license valid |
| ANDA216872 | Misoprostol (Micro Labs) | Tablet | Not available; license valid |

All five licenses are valid and the only dosage form is an oral tablet.

## Safety Considerations

- **Disease-level cautions from the knowledge graph (not label text):** The TxGNN knowledge graph links misoprostol to contraindication-type relationships with several conditions, including:
  - cardiovascular: hypertension, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders
  - liver and gastrointestinal: liver failure or disease, drug-induced liver injury, gallbladder disease, inflammatory bowel disease, active peptic ulcer disease
  - respiratory: asthma
  - blood: blood coagulation disease, anemia, hemoglobinopathy
  - other: substance abuse/dependence, non-infectious meningitis
- **Drug interactions:** The data compiled for this report list 100 interactions in total. The main ones are:
  - **Major:** dinoprostone (topical), another prostaglandin
  - **Moderate:** magnesium-containing antacids (magnesium oxide, magnesium carbonate, magnesium hydroxide, magaldrate) and quinapril
  - **Minor:** sodium citrate, aluminum hydroxide, calcium carbonate, sodium bicarbonate and naproxen
- **Pregnancy-related risk:** Because misoprostol stimulates the uterus, pregnancy-related risks, including congenital anomalies after exposure, argue against repurposing it for a menstrual disorder without careful exclusion of pregnancy.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials exist, and the literature concerns pregnancy termination rather than treating amenorrhea. The drug is marketed in the US with five valid licenses, but mechanism and label safety data are missing.

The second predicted indication, atypical coarctation of aorta, has no supporting trials or literature (Evidence Level L5). It is also not recommended.

**To proceed, the following is needed:**
- Official package insert warnings, contraindications and approved indications. This is a blocking gap for safety screening.
- Mechanism of action data (for example, from DrugBank) to support the mechanistic link.
- A focused literature review for misoprostol in amenorrhea of non-pregnancy causes (for example, a cervical-stenosis or hysteroscopy-related setting).
- A pregnancy-exclusion and teratogenicity risk assessment for any amenorrhea population.
- Confirmation of current US availability and licensing status, given that the drug is marketed with five valid licenses.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

