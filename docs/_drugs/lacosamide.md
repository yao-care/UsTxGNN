---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 828
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is an antiepileptic drug (anticonvulsant) currently used for the treatment of epilepsy, specifically partial-onset seizures. The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **1 clinical trial** and **14 publications** currently supporting this direction — though the evidence base remains preliminary, and most of that evidence actually concerns the depressive rather than the manic pole of bipolar disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset seizures) — inferred from trial/literature context in the evidence pack; no formal TFDA license record was found |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA marked as a data gap). Based on known information, Lacosamide belongs to the antiepileptic drug (AED) / anticonvulsant class, and its efficacy in epilepsy (partial-onset seizures) has been established; mechanistically, this class may be applicable to mood disorders such as bipolar disorder.

The supporting literature indicates lacosamide's mechanism consists of selective slow inactivation of voltage-gated sodium channels, promoting extended stabilization of neuronal cell membranes (PMID 28845834). Sodium-channel-blocking anticonvulsants — such as lamotrigine, carbamazepine, and valproate — are an already-established class of mood stabilizers, which is the pharmacological rationale for testing lacosamide in bipolar disorder.

However, an important caveat applies: the direct mechanistic and clinical evidence specifically supports the **depressive** pole of bipolar disorder rather than the **manic** pole named in this prediction. The single registered clinical trial (NCT07412132) targets major depressive episodes in bipolar I/II disorder, not mania, and the open-label pilot data (PMID 33666402) similarly concerns bipolar depression. Evidence for a mechanistic link to mania specifically remains weak.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Evaluates lacosamide as an augmentation treatment for major depressive episodes in bipolar I/II disorder, building on prior observational/open-label signals of improved depressive and manic symptoms in BD; trial targets the depressive pole, not mania directly; results not yet available (est. completion 2027-01) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week open-label pilot study of lacosamide specifically in bipolar depression — the most direct clinical evidence in this evidence pack |
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide vs. a retrospective control group treated with other antiepileptics in bipolar disorder without epilepsy |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report | Indian J Psychol Med | Reports neutropenia precipitated by lacosamide in a patient with bipolar disorder and comorbid epilepsy — a safety signal, not an efficacy signal |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Clinical stabilization with lacosamide of mood disorder comorbid with PTSD and fronto-temporal epilepsy; describes the sodium-channel slow-inactivation mechanism as basis for mood stabilization |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective multicenter study | Epilepsy Behav | Lacosamide's effect on depression and anxiety symptoms in focal refractory epilepsy patients — indirect mood-related signal in a related population |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | Update on therapeutic drug monitoring of AEDs; notes AEDs including lacosamide are also used in bipolar disorder management |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Mechanistic review | ACS Chem Neurosci | Reviews CRMP2 as a druggable target relevant to lacosamide's mechanism, providing indirect mechanistic support |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Review | Adv Drug Deliv Rev | Background review of chemical properties of AEDs approved 1990–2011, including lacosamide |
| [16732716](https://pubmed.ncbi.nlm.nih.gov/16732716/) | 2006 | Review | Expert Opin Investig Drugs | Background review of second-generation AEDs |
| [40072331](https://pubmed.ncbi.nlm.nih.gov/40072331/) | 2025 | Database study | Epilepsia | Real-world therapeutic drug monitoring concentration ranges for antiseizure medications — indirect background data |

---

## US Market Information

Lacosamide is currently **not marketed in Taiwan** (`未上市`) and no license/NDA records were found in this evidence pack (0 authorizations).

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) were not available for this candidate — the DDI query returned no results, and this represents a **blocking data gap** for safety pre-screening (TFDA label/warnings not yet retrieved).

Please refer to the package insert for safety information.

*Supplementary note:* one case report in the literature above (PMID 30275630) describes lacosamide-precipitated neutropenia in a bipolar patient with comorbid epilepsy. This is a single case report, not formal labeling data, but it is an early hematologic safety signal worth tracking as this candidate advances.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence level is L3 (retrospective cohort and open-label pilot data only, no completed RCT), and the sole registered Phase 3 trial (NCT07412132) is still recruiting with results not expected until 2027. Critically, most supporting evidence addresses bipolar *depression* rather than the *manic* indication named by the TxGNN prediction, so the mechanistic case for mania specifically is not yet well established.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap, required for S1 safety pre-screening)
- Detailed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Completion and readout of NCT07412132
- Trial or observational data targeting manic (not just depressive) episodes specifically
- Formal drug-drug interaction data (current DDI query returned no results)

*Note for context:* among this drug's other predicted indications in the same evidence pack, migraine disorder (rank 5) currently has substantially stronger evidence (L1, "Proceed with Guardrails," including a completed head-to-head Phase 3 RCT vs. propranolol) and may warrant a separate, higher-priority evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

