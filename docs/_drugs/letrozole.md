---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 848
evidence_level: L5
indication_count: 10
---

# Letrozole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Letrozole: From Established Aromatase-Inhibitor Therapy to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a third-generation, non-steroidal aromatase inhibitor whose clinical role in hormone receptor-positive breast cancer is already well established in the medical literature and guidelines. The TxGNN model's top-ranked prediction identifies **Female Breast Carcinoma** as the strongest candidate indication, with **50 clinical trials** and **20 publications** identified in the evidence pack — but this signal is best read as a **confirmation of Letrozole's known mechanism-driven use** rather than a genuinely novel repurposing hypothesis (the evidence pack's own scoring notes state this explicitly).

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (per current regulatory dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: "Original Indication" is omitted from this table because the drug-level regulatory record (`taiwan_regulatory.licenses`) contains no entries for Letrozole in this dataset — see Safety Considerations and Conclusion for the related data gap.*

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Letrozole is flagged as a data gap in this evidence pack (item DG002, High severity). However, the model's own evidence layer consistently and repeatedly describes Letrozole's pharmacology: it is a potent, non-steroidal aromatase inhibitor that blocks the enzymatic conversion of androgens to estrogens. By suppressing systemic and intratumoral estrogen synthesis, it deprives estrogen-receptor (ER)-driven breast cancer cells of the hormonal signal needed for proliferation — this mechanism is described directly in the trial and literature evidence (e.g., PMID 17912633, "The discovery and mechanism of action of letrozole"; PMID 18829517, demonstrating superior suppression of tissue/plasma estrogen levels compared with anastrozole).

Importantly, the repurposing rationale attached to this top-ranked prediction states directly that this represents **the drug's core, already-validated clinical use** ("此為藥物核心已知用途而非新預測，機轉直接且已臨床驗證") rather than a new hypothesis. The very large and mature clinical trial and literature base — including landmark Phase 3 trials such as the BIG 1-98 comparison of letrozole versus tamoxifen (PMID 16382061) and multiple completed registration-grade studies — reflects an indication that is already extensively supported, not one requiring exploratory validation.

For completeness: the same evidence pack also surfaces a lower-ranked, mechanistically **contradictory** candidate — "estrogen-receptor negative breast cancer" (rank 3) — which the evidence pack's own analysis flags as a likely knowledge-graph node-confusion artifact (ER-negative tumors lack the pharmacological target Letrozole depends on). This is a useful illustration of why every TxGNN signal, including the top-ranked one, should be read against its mechanistic rationale rather than score alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02214004](https://clinicaltrials.gov/study/NCT02214004) | Phase 2 | Unknown | 132 | Preoperative trastuzumab + letrozole in postmenopausal HR+/HER2+ breast cancer |
| [NCT00369850](https://clinicaltrials.gov/study/NCT00369850) | Phase 3 | Completed | 458 | Bone density/bone loss monitoring in postmenopausal women on letrozole-based therapy (IBCSG-1-98 cohort) |
| [NCT03811509](https://clinicaltrials.gov/study/NCT03811509) | Phase 4 | Unknown | 1000 | B-ABLE cohort: musculoskeletal effects and quality of life during aromatase inhibitor therapy |
| [NCT05969184](https://clinicaltrials.gov/study/NCT05969184) | Phase 2 | Unknown | 94 | Palbociclib + endocrine therapy + anti-HER2 therapy in HR+/HER2+ advanced breast cancer |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Effects of letrozole vs. tamoxifen on bone and lipid metabolism in postmenopausal early breast cancer |
| [NCT00893061](https://clinicaltrials.gov/study/NCT00893061) | Phase 3 | Completed | 44 | Cognitive function effects of adjuvant aromatase inhibitors (incl. letrozole) vs. tamoxifen |
| [NCT00673335](https://clinicaltrials.gov/study/NCT00673335) | Phase 3 | Completed | 170 | Letrozole vs. placebo for breast cancer prevention in postmenopausal BRCA1/BRCA2 carriers |
| [NCT07085767](https://clinicaltrials.gov/study/NCT07085767) | Phase 3 | Recruiting | 1000 | Palazestrant + ribociclib vs. letrozole + ribociclib, first-line ER+/HER2- advanced breast cancer (OPERA-02) |
| [NCT02679755](https://clinicaltrials.gov/study/NCT02679755) | Phase 4 | Completed | 252 | Palbociclib + letrozole in postmenopausal HR+/HER2- advanced breast cancer for whom letrozole is appropriate |
| [NCT00949598](https://clinicaltrials.gov/study/NCT00949598) | Phase 3 | Completed | 177 | Randomized neoadjuvant comparison of letrozole (aromatase inhibitor) vs. tamoxifen (SERM) in ER+ breast adenocarcinoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | RCT | Computational and Mathematical Methods in Medicine | Efficacy, safety and prognosis of sequential tamoxifen→letrozole vs. letrozole monotherapy in breast carcinoma |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | RCT | Women's Health Issues | Clinical implications and remaining questions from the Letrozole Breast Cancer Trial |
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | The New England Journal of Medicine | BIG 1-98: comparison of letrozole vs. tamoxifen as adjuvant therapy in postmenopausal, hormone-receptor-positive early breast cancer |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Pharmacology, toxicity, and potential therapeutic effects of letrozole |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh, Scotland) | Development of letrozole and its use in advanced breast cancer and the neoadjuvant setting |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opinion on Pharmacotherapy | Letrozole's present and future role in the treatment of breast cancer |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Mechanistic | Breast Cancer Research and Treatment | Discovery and mechanism of action of letrozole (aromatase inhibition) |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacodynamic and pharmacokinetic review of letrozole, including clinical efficacy and safety |
| [18829517](https://pubmed.ncbi.nlm.nih.gov/18829517/) | 2008 | Clinical Study | Clinical Cancer Research | Letrozole superior to anastrozole in suppressing breast tumor tissue and plasma estrogen levels |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opinion on Pharmacotherapy | Comparative review of anastrozole, letrozole and exemestane in early breast cancer |

---

## US Market Information

No marketing authorization records are currently available for Letrozole in this dataset — the regulatory record shows a status of "Not Marketed" with zero recorded licenses. This is recorded as a Blocking-severity data gap (DG001) in the evidence pack, since it also prevents formal review of TFDA/FDA label warnings and contraindications. Remediation (per the evidence pack's own remediation plan) requires retrieving and parsing the official product label from the relevant regulatory agency.

---

## Cytotoxicity

**Antineoplastic classification rationale:** Letrozole is a hormonal antineoplastic agent (aromatase inhibitor) used across all evidenced indications for breast carcinoma; it does not fall into conventional cytotoxic chemotherapy classes (fluoropyrimidine, platinum, taxane, etc.).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/targeted antineoplastic agent (non-cytotoxic aromatase inhibitor) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low as monotherapy; risk increases meaningfully when combined with CDK4/6 inhibitors (e.g., palbociclib) — trial NCT02692755 specifically evaluates febrile neutropenia and neutropenia-related discontinuation in this combination setting |
| Emetogenicity Classification | Low (minimal emetogenic potential reported as monotherapy in the evidence base) |
| Monitoring Items | Bone mineral density (DEXA) and lipid profile with long-term use (per NCT00369850, NCT00171704, NCT03811509 bone/lipid-focused trials); CBC monitoring when combined with CDK4/6 inhibitors |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Letrozole in ER-positive/hormone-sensitive breast cancer is extensive and mature (L1: multiple completed Phase 3 RCTs, including BIG 1-98 and IBCSG-1-98-derived cohorts), but this top-ranked TxGNN signal is a confirmation of Letrozole's already-established use rather than a novel repurposing candidate — guardrails are recommended primarily to ensure the report is not mistaken for a new-indication discovery, and because two Blocking/High data gaps (regulatory label and MOA) remain unresolved.

**To proceed, the following is needed:**
- Retrieve and parse the official regulatory product label (TFDA/FDA) to close the Blocking-severity data gap (DG001) and enable formal safety review
- Query DrugBank (or equivalent) for structured mechanism-of-action data to close the High-severity data gap (DG002)
- Clarify why the regulatory dataset shows zero marketing licenses for a drug with an extensive, mature global clinical record, to rule out a data-pipeline matching issue
- If this indication is intended to be reported as a genuine repurposing candidate rather than a confirmatory signal, re-validate against a target indication distinct from Letrozole's existing labeled use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

