---
layout: default
title: Progesterone
parent: High Evidence (L1-L2)
nav_order: 1089
evidence_level: L2
indication_count: 7
last_modified_at: 2026-10-14
monitor_inn: "PROGESTERONE"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "renal hypoplasia (disease)", "blunt duct adenosis of breast", "apocrine adenosis of breast"]
description: "Progesterone: predicted new indication Amenorrhea (disease) (evidence level L2). Approved use: Not recorded in the local data"
---

# Progesterone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **7** 
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

## Progesterone: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Progesterone is a natural steroid hormone, originally used for gynecological and hormone-related conditions such as endometriosis, endometrial cancer, and postmenopausal osteoporosis.
The TxGNN model predicts it may be effective for **amenorrhea**,
with **4 clinical trials** and **19 publications** currently linked to this direction. However, the trials mainly test estrogen replacement, so direct evidence for progesterone itself is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L2 (as rated in the compiled data; see the note below) |
| US Market Status | Marketed (valid licenses on record: at least 9) |
| Number of NDAs | 9 (all cancelled) |
| Recommended Decision | Proceed with Guardrails |

*Note on the evidence level:* The evidence level is L2 in the compiled data, but I would treat it as a cautious L2 at best. The Phase 3 and Phase 2/3 trials are completed, but the records do not show that progesterone was the tested arm. In these studies, estrogen replacement is the main intervention.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known pharmacology, progesterone acts through progesterone receptors on estrogen-primed endometrium, causing secretory transformation. When the hormone is withdrawn, bleeding follows. This is why progesterone is a standard tool for diagnosing and treating secondary amenorrhea (the "progestin challenge" test) and for cyclic endometrial protection.

The relationship to its original indications is hormonal. Endometriosis and endometrial conditions are driven by estrogen and progesterone signaling, and amenorrhea reflects disruption of the same hypothalamic-pituitary-ovarian axis. In hypoestrogenic forms of amenorrhea (athletes, anorexia nervosa), the trials mainly use estrogen replacement, with progestin given cyclically to protect the endometrium. This makes progesterone a plausible supporting therapy rather than the main driver of efficacy.

The other predicted indications are weaker. Other predictions (benign breast conditions, additional endometriosis sites) are reported only as research questions. Two kidney-related predictions have no credible mechanistic link and look like TxGNN model (deep learning) artifacts. These are not recommended for further development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Young athletes with menstrual dysfunction; tests transdermal or oral estrogen vs. no estrogen for bone density. Progesterone's role is unclear. |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Anorexia nervosa with hypogonadal amenorrhea; estrogen replacement for bone development. Progesterone's contribution cannot be isolated. |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | Active, not recruiting | 120 | Transdermal estradiol with cyclic progesterone vs. placebo in hypoestrogenemic young women with eating disorders; focus on cognition and reward. Only indirectly relevant. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Cardiovascular and immune effects of hypoestrogenemia in functional hypothalamic amenorrhea. Indirect relevance. |

---

## Literature Evidence

The literature consists mainly of reviews and narrative articles. No randomized trial of progesterone for amenorrhea was found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Rev Endocr Metab Disord | Diagnostic and therapeutic use of oral micronized progesterone in endocrinology; progesterone's role in controlling the cycle and endometrium. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Hormonal treatments for endometriosis; estrogen dependency and progesterone resistance. |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Front Endocrinol | Etiology and treatment of premature ovarian insufficiency. |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Management of vaginal bleeding in postmenopausal women. |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Semin Reprod Med | Intrauterine adhesions (Asherman's syndrome), which can present with amenorrhea. |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | Am Fam Physician | Stepwise evaluation of amenorrhea. |
| [7457308](https://pubmed.ncbi.nlm.nih.gov/7457308/) | 1980 | Review | Am Fam Physician | Amenorrhea work-up, including withdrawal bleeding after a course of progesterone. |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecol Endocrinol | Neuroendocrine control of ovulation; hypothalamic vs. ovarian failure in amenorrhea. |

---

## US Market Information


| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA019781 | Prometrium | Capsule | Not available |
| NDA017362 | Progesterone | Injection, solution | Not available |
| ANDA075906 | Progesterone | Injection, solution | Not available |
| ANDA211285 | Progesterone | Capsule | Not available |
| ANDA200456 | Progesterone | Capsule | Not available |

Available dosage forms across all licenses: oral capsule, injectable solution, and liquid.

---

## Safety Considerations

The compiled data contains no package insert warnings or contraindications. Please refer to the package insert for these.

- **Contraindication signals (knowledge graph, not label text):** Associations were found with hypertension, liver failure and liver disease, epilepsy, kidney disease, gallbladder disease, porphyria, diabetes mellitus and hyperglycemia, hypothyroidism, asthma, systemic lupus erythematosus, osteoporosis, anxiety and mood disorders, hypertriglyceridemia, and substance abuse or dependence. These are database associations and need confirmation against the label.
- **Drug Interactions:** 100 interactions were found in total. The 20 reviewed are all moderate. Most involve glucose-lowering drugs, including metformin, pioglitazone, acarbose, sulfonylureas (glimepiride, chlorpropamide), DPP-4 inhibitors (alogliptin, saxagliptin), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), GLP-1 agonists (liraglutide, semaglutide, dulaglutide, albiglutide), and insulins. Other interactions include aprepitant and clarithromycin. Glycemic monitoring is advisable when co-prescribing.
- **Other note:** Progestogen effects on breast tissue raise safety concerns for the breast-related predictions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Progesterone is already a standard agent for diagnosing and treating secondary amenorrhea, and the mechanism is well understood. The direct evidence base is therefore thin. The other nine predictions are not ready for development: breast and additional endometriosis predictions are research questions, and the kidney and breast adenosis predictions should be held.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- Trial data that isolates progesterone's contribution in amenorrhea, for example the arms and outcomes of the listed trials
- A safety monitoring plan covering glycemic interactions and the comorbidities flagged above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

