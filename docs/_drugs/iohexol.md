---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 805
evidence_level: L5
indication_count: 2
---

# Iohexol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Iohexol: From Diagnostic Radiocontrast Imaging to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated contrast agent used for diagnostic imaging procedures (myelography, angiography, CT) — it is not a therapeutic drug and has no established central nervous system activity. The TxGNN model predicts potential efficacy for **Insomnia** (score 99.87%) and, as a secondary candidate, **Anxiety** (score 99.25%), but **no clinical trials or literature directly support either indication** — the evidence pack itself flags the retrieved trial/literature hits as pharmacologically irrelevant noise rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — Iohexol is a radiocontrast imaging agent, not a treated disease indication; no Taiwan license records exist to extract an approved indication text from |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status (Taiwan) | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known pharmacology, Iohexol is a non-ionic iodinated contrast medium used purely for its radiopaque/osmotic properties in imaging procedures such as spinal myelography, angiography, and contrast-enhanced CT. It has no known central nervous system pharmacological activity and no established mechanistic link to sleep-regulation pathways (GABA, melatonin, orexin) or anxiolytic neurotransmission.

Because the original use of Iohexol is diagnostic rather than therapeutic, there is no plausible pharmacological bridge between its imaging role and either insomnia or anxiety treatment. The very high TxGNN scores (99.87% for insomnia, 99.25% for anxiety) most likely reflect graph co-occurrence artifacts — Iohexol frequently appears in clinical datasets alongside patients who separately report insomnia/anxiety symptoms (e.g., during pre-procedure workups, cancer/CKD monitoring, or as an incidental symptom in unrelated imaging studies) — rather than a real biological signal.

This assessment is reinforced by manual review of every retrieved trial and publication (below): none investigate Iohexol as a treatment for insomnia or anxiety.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

## Secondary Predicted Indication: Anxiety (Rank 2, Score 99.25%)

The evidence pack also returned 6 clinical trials and 6 publications for the "anxiety" candidate. On review, all are graded low relevance (Grade C) — none evaluate Iohexol as an anxiety treatment; Iohexol appears only incidentally as a contrast/GFR-marker agent in unrelated studies (renal function, transplant, cardiovascular monitoring), or "anxiety" appears as an incidental symptom description in imaging-procedure papers.

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01053130](https://clinicaltrials.gov/study/NCT01053130) | N/A | Completed | 16 | Weight-loss surgery effect on CKD progression — not relevant, Iohexol likely used only as a GFR clearance marker |
| [NCT01629537](https://clinicaltrials.gov/study/NCT01629537) | Phase 2 | Completed | 41 | Stellate ganglion block for PTSD — Iohexol not the study drug; relates to imaging guidance only |
| [NCT02864706](https://clinicaltrials.gov/study/NCT02864706) | Phase 4 | Completed | 95 | Long-term follow-up of everolimus after heart transplant — unrelated to anxiety treatment |
| [NCT03736005](https://clinicaltrials.gov/study/NCT03736005) | N/A | Completed | 40 | Muscle wasting/renal dysfunction after critical illness — Iohexol used as a kidney-function measurement tool |
| [NCT05428631](https://clinicaltrials.gov/study/NCT05428631) | N/A | Recruiting | 10 | CardioMEMS hemodynamic monitoring device tolerability study — unrelated to anxiety |
| [NCT00634920](https://clinicaltrials.gov/study/NCT00634920) | Phase 4 | Completed | 204 | Everolimus vs. cyclosporine conversion in renal transplant recipients — unrelated to anxiety |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | Double-blind comparison of iodixanol vs. iohexol in extremity phlebography — safety/tolerability of imaging, not anxiety treatment |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohort | Neuroradiology | Side effects of lumbar iohexol myelography; "anxiety/depression" listed as a minor post-procedure side effect, not a treated outcome |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Cohort | Acta Neurochirurgica | Doppler monitoring during cerebral angiography — no anxiety treatment relevance |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | Review | Nutrients | Physical activity and nutrition in onco-nephrology; anxiety mentioned only as a general PA-benefit outcome, unrelated to Iohexol |
| [16034655](https://pubmed.ncbi.nlm.nih.gov/16034655/) | 2005 | Cohort | Cardiovascular and Interventional Radiology | Caval filter placement via arm access in elderly; "patient anxiety" cited as a reason for alternate access site, not an Iohexol indication |
| [25690708](https://pubmed.ncbi.nlm.nih.gov/25690708/) | 2015 | Cohort | La Radiologia Medica | CT hiatal hernia over-reporting causing patient anxiety — incidental mention, unrelated to treatment |

---

## US Market Information

Iohexol is not currently marketed in Taiwan — 0 license records are on file (`total_licenses: 0`), so no NDA/product table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap (DG001) — this prevents any formal S1 safety pre-screening for either candidate indication.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both candidate indications (insomnia and anxiety) score L5 — model prediction only, with zero supporting clinical trials or literature after relevance review. Iohexol's known pharmacology (radiocontrast agent, no CNS activity) offers no mechanistic rationale for either use, and the retrieved evidence is assessed as knowledge-graph noise rather than a real signal.

**To proceed, the following is needed:**
- MOA data from DrugBank API (High-severity data gap, DG002)
- TFDA label warnings/contraindications (Blocking data gap, DG001) — required before any S1 safety pre-screening
- A genuine mechanistic hypothesis connecting Iohexol to CNS/sleep or anxiety pathways before further evidence collection is warranted
- If pursued despite the above, targeted literature search specifically for "iohexol AND (insomnia OR anxiety) AND treatment" (current searches returned no on-topic results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

