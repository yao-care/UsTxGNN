---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 1
---

# Bumetanide
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

# Bumetanide: From Congestive Heart Failure Edema to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a high-ceiling loop diuretic clinically used to treat edema associated with congestive heart failure, hepatic and renal disease, and acute pulmonary congestion. The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease**, with **3 clinical trials** and **5 publications** currently supporting this direction. The mechanistic rationale is strong — bumetanide's preload-reducing and decongestion effects directly address the pathophysiology of acute cor pulmonale — though the evidence base remains at the observational/review level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in regulatory records (known use: edema associated with congestive heart failure, hepatic and renal disease) |
| Predicted New Indication | Acute Pulmonary Heart Disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| US Market Status | Not found in regulatory query (0 licenses recorded) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bumetanide is a potent loop diuretic that acts on the thick ascending limb of the loop of Henle by inhibiting the NKCC2 (Na⁺/K⁺/2Cl⁻) cotransporter. This results in rapid and substantial natriuresis and diuresis, reducing circulating blood volume and intravascular hydrostatic pressure. The drug can be administered orally, intravenously, or intramuscularly, producing marked diuresis within 30 minutes that persists for 3 to 6 hours — a pharmacokinetic profile well-suited to acute settings.

Acute pulmonary heart disease (cor pulmonale with acute decompensation) is characterized by right heart overload, elevated pulmonary artery pressures, and fluid congestion. Bumetanide's mechanism of preload reduction and pulmonary decongestion directly targets these pathophysiological drivers. The TxGNN knowledge graph score of 0.9958 reflects strong pre-existing edges in the bumetanide → fluid overload → cardiac hypertension → pulmonary disease network, corroborating the mechanistic link computationally.

It is important to note that bumetanide's use in congestive heart failure–related edema and acute pulmonary congestion is already well-established in clinical practice and pharmacological literature (notably the 1984 comprehensive review by Ward & Heel). The TxGNN prediction therefore represents an evidence-consolidation exercise for an extended indication rather than a novel repurposing hypothesis from scratch. Regulatory data for this candidate (especially from TFDA) was not captured in the current evidence pack, which limits formal safety scoring.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Prospective pilot assessing whether single 4 mg intranasal bumetanide acutely reduces pulmonary artery pressure and blood volume in outpatient HF patients with implanted remote monitoring devices (CardioMEMS / Cordella). Trial withdrawn before enrollment; no data available. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Evaluates empagliflozin + sacubitril/valsartan in adults with congenital heart disease–associated HF with reduced EF. Bumetanide likely appears only as concomitant background diuretic; not the primary investigational agent. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Observational seismocardiographic monitoring study in heart failure; focused on device-based remote monitoring rather than pharmacological evaluation. Bumetanide may appear as background therapy but provides no direct drug-efficacy evidence. |

> **Note:** None of the identified trials were designed to directly evaluate bumetanide efficacy in acute pulmonary heart disease. NCT07375212 is the most mechanistically relevant but was withdrawn before generating any data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Prospective Clinical Study | British Journal of Clinical Pharmacology | IV bumetanide (25 µg/kg) in 24 patients with coronary artery disease and acute or chronic HF: reduced cardiac index and pulmonary artery occluded pressure (PAOP) at rest; directly demonstrates acute hemodynamic preload reduction relevant to pulmonary congestion. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Pharmacological Review | Drugs | Comprehensive pharmacodynamic and pharmacokinetic review; documents bumetanide's approved use for edema in CHF, acute pulmonary congestion, hepatic and renal disease; establishes mechanism and clinical profile. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Narrative Review | American Journal of Therapeutics | Reviews therapeutic options for acute decompensated HF; highlights loop diuretics including bumetanide as the cornerstone of acute HF management; contextualizes its role among 1 million annual US hospitalizations. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Comparative Review | Annals of Pharmacotherapy | Systematic comparison of loop diuretics (furosemide, bumetanide, torsemide) for pharmacokinetics, safety, efficacy, and cost; supports bumetanide as a clinically valid alternative to furosemide in HF. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiological Study | American Journal of Emergency Medicine | US ED epidemiology of HF presentations 2016–2023; characterizes the scale of acute HF burden and treatment patterns, providing context for the target patient population. |

---

## US Market Information

No regulatory authorizations were identified in the current query of TFDA records for Bumetanide. The evidence pack reflects 0 licenses and "not marketed" status under the data available at the time of this report.

> **Important caveat:** Bumetanide has historically been approved in the United States under the brand name Bumex (Roche) and as multiple generic formulations. The absence of records in this evidence pack likely reflects a data retrieval gap rather than a true absence of approval. Further regulatory verification is recommended before drawing conclusions about market status.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not captured in this evidence pack.

> As a loop diuretic, clinicians should be alert to class-level risks including electrolyte disturbances (hypokalemia, hyponatremia, hypomagnesemia), ototoxicity (especially at high doses or with concurrent aminoglycosides), volume depletion, and renal function changes. Formal safety review requires retrieval of the TFDA/FDA package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for bumetanide in acute pulmonary heart disease is direct and physiologically sound — loop diuresis reduces preload and pulmonary congestion, the hallmark pathophysiology of this condition. Multiple pharmacological reviews and a prospective hemodynamic study support this connection, placing evidence at L3. The TxGNN score of 99.58% is consistent with this established mechanistic alignment. However, the current evidence pack has critical gaps in safety data and regulatory information that must be resolved before any formal development decision.

**To proceed, the following is needed:**

- **Safety data retrieval:** Download and parse the TFDA and/or FDA package insert to extract formal warnings, contraindications, and drug interactions (currently Blocking gap DG001)
- **MOA documentation:** Retrieve full mechanism of action from DrugBank API to complete mechanistic analysis (currently High gap DG002)
- **Regulatory verification:** Confirm US FDA approval status (Bumex / generic bumetanide) and any approved indications that may overlap with the predicted indication
- **Targeted clinical trial design:** The most promising near-term step is a prospective study of bumetanide specifically in acute cor pulmonale, as NCT07375212 attempted before withdrawal; consider whether a similar design can be revived
- **Electrolyte and renal safety monitoring plan:** Any Proceed pathway should include pre-specified monitoring for hypokalemia, serum creatinine, and fluid balance given the acute pulmonary heart disease population's likely comorbidities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

