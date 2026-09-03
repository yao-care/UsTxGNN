---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 1069
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
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

# Potassium Chloride: From Electrolyte Replacement to Renal Tubular Acidosis

## One-Sentence Summary

Potassium chloride (DB00761) is a well-established electrolyte replacement product used to treat and prevent hypokalemia; no original indication text or NDA data are on record for this evidence pack.
The TxGNN model predicts it may be effective for **Renal Tubular Acidosis (RTA)**, but the supporting evidence base is currently limited to **9 low-relevance clinical trials** (all graded C) and **20 literature references**, none of which directly evaluate KCl in RTA.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available data (no approved indication text or license record) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, potassium chloride is an electrolyte replacement agent used to correct or prevent potassium deficiency, and mechanistically it could be relevant to RTA because hypokalemia is a common complication of several RTA subtypes.

However, the `repurposing_rationale` provided with this candidate raises an important caveat: the TxGNN high score likely reflects a **comorbidity association** ("RTA → hypokalemia → potassium supplementation") rather than a direct disease-modifying drug-disease relationship. More critically, distal (type 1) RTA is characterized by **hyperchloremic metabolic acidosis**, and the clinical standard of care uses **non-chloride potassium salts** (potassium citrate or potassium bicarbonate) precisely because they provide an alkalinizing effect. Potassium chloride, by contrast, delivers an additional chloride load that could theoretically worsen the underlying hyperchloremic acidosis — making it a mechanistically questionable choice for this specific indication.

Because both the original indication and MOA fields are marked as data gaps, and the market status is "Not Marketed," the baseline for assessing this candidate's credibility is weak, further reinforcing a cautious interpretation of the TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | Recruiting | 33 | Compares 24-hour urinary aldosterone measurement methods in primary aldosteronism diagnosis; no direct link to KCl or RTA treatment (relevance C). |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | Terminated | 7 | Evaluates oral sodium bicarbonate (alkali therapy, not KCl) for bicarbonate/potassium correction in Sickle Cell Disease; terminated early (relevance C). |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | Unknown | 31 | Safety of eplerenone in cyclosporine-treated transplant recipients; not a potassium supplement study (relevance C). |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | Recruiting | 130 | SGLT2 inhibitor for cardiorenal syndrome; mechanism unrelated to KCl (relevance C). |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | Unknown | 40 | Sodium bicarbonate (not KCl) used to alkalinize urine in pediatric topiramate-induced RTA; different drug and population (relevance C). |
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Terminated | 3 | Randomized withdrawal study of ADV7103 vs placebo in distal RTA; terminated with only 3 subjects, drug agent not confirmed as KCl (relevance C). |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | Recruiting | 43 | Exogenous ketosis effects on proteinuria in CKD/PKD; unrelated to KCl or RTA (relevance C). |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | Terminated | 36 | Spironolactone for prevention of electrolyte abnormalities with Amphotericin B; not a KCl/RTA study (relevance C). |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn | 0 | Potassium citrate (not potassium chloride) in pediatric idiopathic hypercalciuria; trial withdrawn, no data generated (relevance C). |

**Overall: No clinical trials directly evaluate potassium chloride for renal tubular acidosis. All listed trials are indirect/tangential (relevance grade C).**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Archivos Españoles de Urología | Overview of RTA diagnosis and management, including stone formation in distal RTA. |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Medica Indonesiana | General approach to hypokalemia etiology and workup. |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Médicale | Genotype-phenotype correlation of distal RTA in a Tunisian cohort. |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Archives of Internal Medicine | Pathophysiology and diagnostic approach to RTA subtypes. |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Review | International Journal of Clinical Practice | Clinical approach to RTA in adult patients across proximal/distal subtypes. |
| [33769949](https://pubmed.ncbi.nlm.nih.gov/33769949/) | 2021 | Review | Journal of the American Society of Nephrology | Discusses urine anion gap use and misconceptions in acid-base/RTA evaluation. |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | Journal of Nephrology | Distal RTA with hypokalemic periodic paralysis during pregnancy. |
| [14048071](https://pubmed.ncbi.nlm.nih.gov/14048071/) | 1963 | Review | Medical Bulletin (Ann Arbor) | Historical review of renal tubular acidosis. |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | Journal of Clinical Investigation | Impaired renal sodium/chloride conservation during correction of type 1 RTA with **potassium bicarbonate** (not KCl). |
| [3518609](https://pubmed.ncbi.nlm.nih.gov/3518609/) | 1986 | Review | Annual Review of Medicine | Clinical spectrum of RTA subtypes (proximal, hypokalemic distal, hyperkalemic distal). |

**Note: None of the reviewed literature specifically studies potassium chloride as a therapeutic agent for RTA; several references note that non-chloride potassium salts (citrate, bicarbonate) are the conventional therapeutic choice.**

---

## US Market Information

No NDA or marketing authorization records are available for this product — market status is recorded as **Not Marketed**, and `total_licenses` = 0.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (model prediction supported only by indirect/mechanistic literature, no direct clinical trials), and the underlying rationale itself flags a plausible mechanistic conflict — KCl's chloride load may be unsuitable for hyperchloremic RTA, where non-chloride potassium salts are the established standard. Combined with missing MOA, indication, and safety data, the evidence does not currently support proceeding.

**To proceed, the following is needed:**
- TFDA/FDA label warnings and contraindications (currently blocking, DG001)
- Confirmed mechanism of action data (DG002)
- Original approved indication data for potassium chloride
- Clinical or pharmacological evidence specifically comparing chloride-based vs. citrate/bicarbonate-based potassium salts in RTA management
- Route of administration compatibility assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

