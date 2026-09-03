---
layout: default
title: Propafenone
parent: 僅模型預測 (L5)
nav_order: 1090
evidence_level: L5
indication_count: 8
---

# Propafenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Propafenone: From Cardiac Arrhythmia to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Propafenone (DrugBank ID DB01182) is a Class IC antiarrhythmic agent; detailed original-indication licensing data was not found in this evidence pack, but the drug is generally known for treating cardiac arrhythmias.
> The TxGNN model predicts it may be relevant to **manic bipolar affective disorder** (score **99.80%**),
> but the only supporting literature currently available (**3 publications, 0 clinical trials**) describes propafenone **inducing** mania/psychosis as an adverse effect — not treating it. This prediction should be interpreted with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license records found); propafenone is generally recognized as a Class IC antiarrhythmic per DrugBank identity |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (case-report-level literature only; no RCTs; evidence describes adverse drug reaction risk, not therapeutic benefit) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological identity, propafenone is a Class IC antiarrhythmic that blocks cardiac sodium channels and also has mild beta-adrenergic blocking activity; it is structurally related to the antidepressant bupropion. No original approved-indication text was found in the `taiwan_regulatory` license records for this dataset (0 licenses, market status "Not Marketed"), so a direct original-vs-new indication comparison cannot be made from the evidence pack itself.

TxGNN scores propafenone very highly (99.80%) for "manic bipolar affective disorder." However, all three retrieved publications describe the **opposite direction of association** — propafenone triggering mania or psychosis as an adverse drug reaction, not treating it:
- *"A case of mania secondary to propafenone"* (1985) speculates this may stem from propafenone's structural similarity to bupropion, which does have antidepressant/mood-activating activity.
- *"An organic psychosis due to a venlafaxine-propafenone interaction"* (2001) describes a drug-drug interaction precipitating psychosis in a bipolar patient.
- The 2020 pharmacovigilance review discusses harmful interactions between antipsychotics and cardiovascular drugs (including propafenone) in patients with bipolar disorder/schizophrenia comorbid with cardiovascular disease.

This is a case where a knowledge-graph model may have learned a strong **association** between propafenone and bipolar/mania concepts purely from co-occurrence in adverse-event literature, without that association reflecting a **therapeutic benefit**. This distinction is critical before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case report | J Clin Psychiatry | Case of mania secondary to propafenone; authors speculate structural similarity to bupropion may confer mood-activating/antidepressant-like activity |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case report | Int J Psychiatry Med | Organic psychosis triggered by a venlafaxine-propafenone drug interaction in a patient with bipolar affective disorder |
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Pharmacovigilance review | Pharmacological Reports | Evaluates harmful drug-drug interactions between antipsychotics and cardiovascular medications (incl. propafenone) in patients with bipolar disorder/schizophrenia and comorbid cardiovascular disease |

**Note:** None of the above literature supports using propafenone *to treat* bipolar/manic symptoms; all describe it as a potential *trigger or interaction risk* for psychiatric adverse effects.

---

## US Market Information

No marketing authorization records were found in this evidence pack. The drug is currently listed as **Not Marketed** with **0 licenses** on file, so no product/dosage-form/indication table can be produced.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-interaction records) was available in this evidence pack — please refer to the package insert for official safety information.

**Additional safety signal identified from literature (not from official safety data sources):** Case reports indicate propafenone may precipitate mania or psychosis, particularly in patients with bipolar disorder or in combination with other psychoactive/cardiovascular drugs (e.g., venlafaxine). This should be treated as a caution flag rather than supporting evidence for the predicted indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature evidence available for "manic bipolar affective disorder" describes propafenone-induced mania/psychosis as an adverse reaction, not a therapeutic effect — this contradicts rather than supports the predicted indication. There are no clinical trials, no original-indication data, and no MOA data on file, and the TFDA label/warning data gap is Blocking per the meta data-gap list.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert / warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action from DrugBank (currently a High-severity data gap, DG002)
- Original approved-indication and licensing records for propafenone in this jurisdiction
- Reassessment of whether "manic bipolar affective disorder" should remain a candidate indication, or be reclassified as a **safety signal** for psychiatric monitoring in current antiarrhythmic use
- Consider separately evaluating rank 2 (catecholaminergic polymorphic ventricular tachycardia), rank 5 (incessant infant ventricular tachycardia), and rank 6 (arrhythmogenic right ventricular cardiomyopathy) — these show literature with actual **therapeutic use** of propafenone (including a 35-year case of effective CPVT treatment and RyR2-channel-blocking mechanism studies) and are mechanistically consistent with propafenone's known antiarrhythmic action, making them more promising repurposing candidates than the current top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

