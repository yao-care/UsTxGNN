---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

---

# Acetazolamide: From Carbonic Anhydrase Inhibitor to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a classic carbonic anhydrase inhibitor (CAI) with established pharmacological uses including diuresis, glaucoma, and altitude sickness, though it currently holds no regulatory approval in this market.
TxGNN predicts up to 10 new indications; the highest-evidence opportunity is **Cardiomyopathy** (heart failure decompensation) — backed by **3 active Phase 4 clinical trials** and **10 publications**, anchored by the landmark ADVOR trial published in *NEJM* (2022) that already demonstrated efficacy in a completed Phase 3 RCT.
Among all 10 predictions, cardiomyopathy carries the top evidence rating (L1) with a "Proceed with Guardrails" recommendation; the remaining nine predictions range from L4 to L5, most warranting a "Hold" at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No regulatory approval on file in this market |
| Predicted New Indication | Cardiomyopathy (acute decompensated heart failure) |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| Market Status | Not Marketed (0 licenses) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acetazolamide inhibits carbonic anhydrase enzymes in the kidney's proximal tubule, blocking bicarbonate (HCO₃⁻) reabsorption and triggering sodium diuresis. Unlike loop diuretics (e.g., furosemide), which target the sodium-potassium-chloride co-transporter in the loop of Henle, acetazolamide acts via a completely distinct pathway — making it a mechanistically complementary, rather than redundant, diuretic agent.

The link to cardiomyopathy and heart failure becomes clear through a well-recognized clinical problem: patients with chronic heart failure who rely on long-term loop diuretics frequently develop **metabolic alkalosis** (elevated bicarbonate levels). This alkalosis paradoxically reduces loop diuretic effectiveness, creating a cycle of "diuretic resistance" and progressive fluid overload. Acetazolamide breaks this cycle by correcting the alkalosis, restoring the proximal tubule's sodium delivery and re-sensitizing patients to loop diuretics.

This mechanistic rationale was rigorously tested in the **ADVOR trial** (NEJM, 2022) — a completed, double-blind Phase 3 RCT demonstrating that adding intravenous acetazolamide to standard loop diuretic therapy significantly improved successful decongestion in acute decompensated heart failure. The subsequent launch of three large Phase 4 trials (n = 400–939 patients each) is a direct consequence of that landmark result, further validating TxGNN's prediction that acetazolamide has a meaningful role in cardiomyopathy management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide for acute decompensated heart failure; evaluates efficacy across both reduced and preserved ejection fraction phenotypes. Phase 4 initiation implies a positive preceding Phase 3 (ADVOR, NEJM 2022). |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | Recruiting | 556 | TAILOR-AHF: Tests a urine-sodium-guided, individualized diuretic algorithm in acute heart failure; acetazolamide is a candidate component of the protocol, with 556 patients enrolled. |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Head-to-head comparison of loop diuretic + metolazone vs. loop diuretic + acetazolamide vs. loop diuretic alone in volume-overloaded acute heart failure; largest of the three trials (n = 939). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Annual Review | ESC Heart Failure | 2024 heart failure update reflecting 2023 ESC guideline revisions; establishes current treatment landscape into which acetazolamide is being integrated. |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Comprehensive review of new cardiovascular pharmacological agents approved in 2022, including mavacamten for obstructive HCM; provides context for evolving heart failure pharmacotherapy. |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | Journal of Cardiology Cases | Acetazolamide successfully corrected hypochloremia (94 mEq/L) and hyponatremia in an 87-year-old with advanced heart failure and hypertrophic cardiomyopathy on multi-agent diuretic therapy; highlights chloride and electrolyte management as a key therapeutic target. |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study | Saudi Medical Journal | Investigated acetazolamide effects in ischemia-reperfused isolated rabbit hearts (2-week and 8-week old); provides mechanistic preclinical data on cardiac effects. |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian Journal of Ophthalmology | Oral acetazolamide used for cystoid macular edema in Danon disease — a cardiomyopathy subtype; documents systemic use in a cardiovascular genetic disorder. |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case Report (Adverse Event) | Acute Medicine & Surgery | ⚠️ Non-cardiogenic pulmonary edema occurred 1 hour after IV acetazolamide in a patient with dilated cardiomyopathy; important safety signal specific to the IV route in advanced heart failure. |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurologica Scandinavica | Acetazolamide (750–1000 mg/day) in hypokalemic periodic paralysis associated with heart muscle disease; exercise-induced angina noted — potential cardiac stress signal at high doses. |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Report | Acta Neurologica Scandinavica | Echocardiographic and cardiological examination of cardiomyopathy in a family with hypokalemic periodic paralysis; documents cardiac involvement in acetazolamide-treated patients. |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | Journal of Medical Case Reports | Congenital hydrocephalus with trisomy 9p and co-existing congenital heart disease; acetazolamide used in complex cardiac-neurological presentation, illustrating use in cardiac comorbidity. |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Case Series | Journal of Nuclear Medicine | SPECT cerebral blood flow study in mitochondrial encephalomyopathy, a condition with cardiac involvement; background context for acetazolamide in mitochondrial disease affecting the heart. |

---

## Market Information

Acetazolamide currently holds no regulatory approval in this market. No product licenses or approved indication texts are available for review.

> Note: Acetazolamide is approved in other major markets (e.g., the United States under the brand Diamox, and various generics) for indications including glaucoma, altitude sickness, epilepsy (absence seizures), and edema. Regulatory data for those markets was not included in this Evidence Pack.

---

## Safety Considerations

Formal safety data (package insert warnings and contraindications) for this market were not available in the Evidence Pack. Please refer to published prescribing information from authorized markets (e.g., FDA labeling for Diamox/generics) for full safety details.

The following clinically important signals were identified from the literature collected during evidence gathering:

- **IV Route Risk**: One case report (PMID 29123889) documents sudden non-cardiogenic pulmonary edema one hour after intravenous acetazolamide in a patient with dilated cardiomyopathy. The oral route may be safer in cardiac patients, consistent with the design of NCT05802849 (oral acetazolamide study).

- **Gastrointestinal Motility — Reverse Signal**: PMID 19653068 reports acetazolamide-induced adynamic ileus (intestinal paralysis), and a 1959 case series (PMID 13659695) documents paralytic ileus with carbonic anhydrase inhibitor class drugs. Acetazolamide should be used with caution in patients with pre-existing gastrointestinal motility disorders; this also explains why the TxGNN prediction for "intestinal obstruction" (rank 8) carries a firm **Hold** — the drug may worsen, not treat, this condition.

- **Electrolyte Monitoring**: Given the drug's mechanism (bicarbonate wasting, promotion of natriuresis), electrolyte imbalances including hypokalemia, hyponatremia, and metabolic acidosis are pharmacologically expected effects requiring monitoring.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ADVOR trial (NEJM 2022) established strong Phase 3 RCT evidence for acetazolamide as an adjunct to loop diuretics in acute decompensated heart failure, and three large Phase 4 trials are actively expanding the evidence base. The mechanistic rationale (correcting diuretic-induced metabolic alkalosis) is well understood and clinically validated. Among all 10 TxGNN-predicted indications, cardiomyopathy is the only one with a track record sufficient to justify moving forward.

**To proceed, the following is needed:**

- **Complete safety screening**: Obtain full prescribing information (package insert/SmPC) to complete the S1 safety assessment — currently the single blocking data gap
- **Confirm MOA documentation**: Retrieve formal DrugBank mechanism of action data to complete mechanistic analysis records
- **Monitor Phase 4 trial readouts**: NCT06166654 (n = 939, completion September 2027) will directly compare acetazolamide vs. metolazone — results will sharpen positioning within the heart failure treatment algorithm
- **IV vs. oral route decision**: Given the pulmonary edema adverse event signal with IV acetazolamide in cardiomyopathy patients, a route-of-administration risk assessment is warranted before deployment in advanced heart failure settings
- **Reverse signal safeguard**: Flag the intestinal obstruction reverse-signal (adynamic ileus) in prescribing guidance; this contraindication should be explicitly documented in any clinical deployment protocol
- **Regulatory pathway planning**: If seeking market entry, determine whether the ADVOR Phase 3 data supports a bridging submission or whether a local bridging study is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

