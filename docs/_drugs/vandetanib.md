---
layout: default
title: Vandetanib
parent: High Evidence (L1-L2)
nav_order: 1284
evidence_level: L2
indication_count: 10
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Vandetanib: From Thyroid Gland Carcinoma to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-target tyrosine kinase inhibitor (VEGFR2, EGFR, RET), originally used to treat thyroid gland carcinoma.
The TxGNN model predicts it may be effective for **Renal Cell Carcinoma**,
with **4 clinical trials** (all small Phase 1/2 or Phase 2 studies, two terminated early) and **5 publications** currently linked to this direction. No Phase 3 data exist.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid gland carcinoma (the US license record has no indication text) |
| Predicted New Indication | Renal cell carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| US Market Status | Cancelled only (no active license) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, vandetanib is a multi-target tyrosine kinase inhibitor acting on VEGFR2, EGFR and RET. Its efficacy in thyroid carcinoma (medullary thyroid cancer) is driven mainly by RET inhibition.

Clear cell renal cell carcinoma is typically characterised by loss of VHL and HIF-driven overexpression of VEGF. This makes VEGFR2 inhibition mechanistically coherent. A combination with metformin has also been tested in rare fumarate hydratase- or SDH-deficient kidney cancers, which are driven by metabolic reprogramming.

However, the rationale is weakened by practical considerations. Established VEGFR tyrosine kinase inhibitors (sunitinib, pazopanib, axitinib, cabozantinib) are already standard of care in renal cell carcinoma. The available vandetanib trials are small, and no Phase 3 study exists.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in von Hippel-Lindau disease with renal tumours. The most informative trial, but no results are available in the data. |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Advanced clear cell renal carcinoma. Stopped at 3 patients, so uninformative for efficacy. |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib plus metformin in HLRCC/SDH-associated kidney cancer or sporadic papillary RCC. Stopped at 7 patients; no meaningful efficacy conclusion. |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomised trial of carboplatin and gemcitabine with or without vandetanib in advanced urothelial cancer. Only indirectly relevant to RCC; results not available. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Targeting metabolic and epigenetic reprogramming in metastatic fumarate hydratase-deficient RCC. Notes that several Phase 2 combination trials are under way and no standard regimen exists. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Profile of anti-angiogenic agents in solid tumours, including vandetanib. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | Systemic therapy for advanced thyroid cancers. Vandetanib is an approved RET inhibitor for medullary thyroid cancer. |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Review | Pharmacol Res | FDA-approved RET inhibitors in RET-driven thyroid and lung cancer. Background only. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3 translocation RCC mouse model identifying possible therapeutic targets. It does not establish vandetanib activity. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022405 (cancelled) | CAPRELSA (Genzyme Corporation) | Film-coated tablet | Not listed in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; given the knowledge-graph contraindications, ECG/QT interval, electrolytes (potassium, calcium), thyroid function, blood pressure, and liver and renal function are relevant |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease links from the TxGNN knowledge graph, not package insert text):
  - Cardiovascular: hypertension, long QT syndrome (including familial), torsades de pointes, congestive heart failure
  - Cerebrovascular: brain ischaemia, transient ischaemic attack, posterior leukoencephalopathy syndrome
  - Endocrine and metabolic: hypothyroidism (including myxedema and congenital hypothyroidism), potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease
  - Renal and pulmonary: impaired renal function, interstitial lung disease
- **Drug Interactions**: 100 interactions were found. Among the 20 listed, the following are rated **Major**:
  - Clarithromycin
  - Levofloxacin
  - Dolasetron
  - Palonosetron
  - Picosulfuric acid
  - Sodium sulfate
  - Polyethylene glycol 3350 with electrolytes

  Several of these are QT-prolonging or electrolyte-altering agents, which fits vandetanib's QT risk. Moderate interactions include famotidine, metformin, loperamide, dexamethasone, bisacodyl and lactitol. Minor interactions include ranitidine and several proton pump inhibitors.
- **Class safety literature**: Meta-analyses of VEGFR tyrosine kinase inhibitors report hepatic toxicity, proteinuria and treatment-related mortality. Long-term follow-up in medullary thyroid cancer (PMID 32691271) informs tolerability, including QT prolongation. A critical commentary (PMID 23185843) describes vandetanib as too dangerous for medullary thyroid cancer.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.92%), and the VEGFR-inhibition rationale in VHL-deficient clear cell RCC is plausible. The clinical evidence is weak, however. Only four small Phase 1/2 or Phase 2 trials exist, two were terminated with 3 and 7 patients, and none has reported results in the available data. Standard VEGFR inhibitors are already established in RCC. Vandetanib carries a notable QT and cardiovascular risk profile, and its only US license is cancelled. The package insert warnings and contraindications are also missing from the compiled data, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (obtain from the FDA website)
- Mechanism of action data (e.g. via the DrugBank API)
- Published results from NCT00566995 (VHL disease, n=37)
- A comparison against current standard-of-care VEGFR inhibitors in RCC
- A QT, cardiovascular and drug-interaction risk management plan
- Clarification of the regulatory pathway given the cancelled US licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

