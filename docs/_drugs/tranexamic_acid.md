---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 1248
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
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

# Tranexamic Acid: From Endometriosis to Amenorrhea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic originally linked to endometriosis in the knowledge graph used for this analysis.
The TxGNN model predicts it may be effective for **Amenorrhea**,
but there are currently **0 clinical trials** and only **2 publications** (both reviews, and neither directly addresses treating amenorrhea) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (endometriosis of uterus), per the knowledge graph; no approved indication text is available from US licences |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licences) |
| Number of NDAs | 13 (1 NDA and 12 ANDAs, all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, tranexamic acid is an antifibrinolytic that inhibits plasminogen activation and so reduces fibrinolysis-driven menstrual blood loss. This underlies its established use in heavy menstrual bleeding.

The link to the predicted indication is **indirect**. Tranexamic acid could plausibly be used for menses suppression or prophylaxis, for example in haematology patients at risk of heavy bleeding. However, it does not act on the hormonal axis that causes or treats true amenorrhea (absence of menses). Any benefit would come from reducing menstrual bleeding, not from treating amenorrhea as a pathological condition.

The high TxGNN score (0.99) is a computational prediction. It may reflect proximity to other menstrual-disorder indications rather than a genuine therapeutic rationale. It should be interpreted cautiously.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of drug therapies for abnormal uterine bleeding. Non-hormonal options such as NSAIDs reduce bleeding by 25–35%, and treatment choice depends on the cause and amount of bleeding, contraception needs and menopausal status. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Systematic approach to menses prophylaxis and suppression in pre-menopausal haematologic cancer patients. Menstrual bleeding adds morbidity alongside cytopenias, and comparative data on suppression agents are scarce. |

## US Market Information

All 13 licences are cancelled, and none carries approved indication text in the data compiled. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203521 | Tranexamic Acid | Injection, solution | Not available |
| ANDA205035 | Tranexamic Acid | Injection, solution | Not available |
| ANDA202093 | Tranexamic Acid | Tablet, film coated | Not available |
| ANDA218320 | Tranexamic Acid | Tablet | Not available |
| ANDA212676 | Tranexamic Acid | Injection, solution | Not available |

Other licences include NDA212020 (tranexamic acid in sodium chloride, Exela Pharma Sciences). Available routes are injectable and oral.

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** The knowledge graph links tranexamic acid with the following conditions, which should be carefully reviewed:
- Cardiovascular and thrombotic: hypertension, coronary artery disease, thrombophlebitis, stroke and cerebrovascular disorder
- Hormone-sensitive cancers: female breast carcinoma, endometrial cancer and uterine corpus cancer
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia, hypertriglyceridemia and obesity
- Hepatic and porphyria: liver disease, gallbladder disease and porphyria
- Neurological and psychiatric: migraine, brain edema, anxiety disorder, neurotic disorder and dysthymic disorder

**Drug Interactions:** 35 interactions were recorded; 20 are shown in the data compiled. Most are **Major**:
- Oestrogens and hormonal agents: ethinylestradiol, estradiol, conjugated estrogens, esterified estrogens, estrone, diethylstilbestrol, norethisterone, drospirenone and etonogestrel
- Pro-coagulant agents: anti-inhibitor coagulant complex and Factor IX complex (human)
- Carfilzomib and estramustine
- **Moderate**: alteplase and anistreplase (thrombolytics)

Combining tranexamic acid with hormonal or pro-coagulant agents raises thrombotic concern.

Label-based warnings and contraindications were not available. Please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score. There are no clinical trials, and the two reviews on menstrual bleeding do not show benefit in treating amenorrhea. The mechanism is indirect, since tranexamic acid reduces bleeding rather than restoring menses. All US licences are cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- Clarify whether the intended use is treating amenorrhea or menses suppression (for example in haematology patients), as these are different questions
- Obtain mechanism of action data from DrugBank
- Obtain and review the FDA package insert for warnings and contraindications
- Collect clinical or observational evidence for the clarified indication
- Evaluate thrombotic risk, especially with concurrent hormonal therapy
- Confirm current US availability and licensing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

