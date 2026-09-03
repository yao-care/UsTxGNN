---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 1311
evidence_level: L5
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Zolmitriptan is a selective 5-HT1B/1D receptor agonist (triptan) used globally for the acute treatment of migraine.
> The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
> but this indication carries a well-known drug-class safety concern that current evidence does **not** resolve —
> supporting literature covers general migraine/triptan use, with **no clinical trials** specifically on this aura subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine, acute treatment (general population; formal Taiwan indication text unavailable — drug not licensed) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 (Review/observational literature; no disease-specific RCTs) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data for zolmitriptan is not available in this evidence pack (data gap). Based on the supporting literature, zolmitriptan is known to be a selective serotonin 5-HT1B/1D receptor agonist that constricts intracranial (extracerebral) blood vessels and inhibits neuropeptide release from the trigeminovascular system — the standard mechanism underlying triptan efficacy in typical migraine, with or without aura.

However, "migraine with brainstem aura" (formerly known as basilar-type or basilar migraine) is a distinct clinical entity involving posterior (vertebrobasilar) circulation symptoms. Because triptans theoretically cause vasoconstriction, this subtype has traditionally been treated as a **relative contraindication** for the triptan class in several international guidelines (including AHS/AAN), out of concern for exacerbating posterior-circulation ischemia. None of the 19 supporting publications specifically evaluate zolmitriptan's safety or efficacy in this aura subtype with controlled data — they largely address migraine in general or migraine with typical aura.

TxGNN's high prediction score (99.99%) most likely reflects zolmitriptan's strong association with the broader "migraine" disease node rather than validated applicability to this specific, mechanistically sensitive subtype. This is a case where the model's output should be interpreted with caution rather than as straightforward evidence of a novel, safe indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Report | Headache | Directly addresses triptan use in basilar migraine and migraine with prolonged aura — the most topic-relevant reference, but reports clinical experience rather than controlled trial data. |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Review/Meta-analysis | J Headache Pain | Compares frovatriptan vs. rizatriptan/zolmitriptan/almotriptan specifically in migraine **with aura**; notes triptans are generally not effective when taken during the aura phase itself. |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT (subgroup analysis) | Neurol Sci | Double-blind, randomized, multicenter Italian study; subgroup of 18 patients with migraine with aura compared frovatriptan vs. zolmitriptan 2.5 mg. |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | RCT | Cephalalgia | Randomized trial across six triptans in migraine patients with/without aura and early allodynia; examined differential pain-reduction response. |
| [15581383](https://pubmed.ncbi.nlm.nih.gov/15581383/) | 2004 | RCT | CNS Drugs | Zolmitriptan 5 mg orally disintegrating tablet showed rapid onset of headache response in acute migraine (general population, not aura-subtype specific). |
| [27329280](https://pubmed.ncbi.nlm.nih.gov/27329280/) | 2016 | RCT (TEENZ study) | Headache | Randomized, double-blind, multicenter trial (NCT01211145) of zolmitriptan nasal spray in adolescents (12–17y) for acute migraine; pain-free at 2h as primary endpoint. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | AHS evidence assessment of acute migraine pharmacotherapies; establishes zolmitriptan's evidence tier for general migraine, not brainstem-aura subtype. |
| [9399016](https://pubmed.ncbi.nlm.nih.gov/9399016/) | 1997 | Cohort (safety) | Cephalalgia | Large tolerability dataset (>3,000 subjects, ~50,000 doses) for zolmitriptan; establishes general adverse event profile. |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opin Pharmacother | General review of zolmitriptan pharmacology and clinical applications in migraine. |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | Comprehensive review of zolmitriptan's efficacy/tolerability across RCTs in general migraine populations. |

---

## US Market Information

Zolmitriptan currently has **no market authorization records** in this jurisdiction — market status is **Not Marketed** with **0 licenses** on file. No dosage form, brand name, or approved-indication data is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information (TFDA warning/contraindication data and DDI data are currently unavailable — see data gap DG001, marked as **Blocking** for safety assessment).

**Known drug-class caution (from mechanistic literature, not formal label data):** Triptans, including zolmitriptan, are conventionally treated as a relative contraindication in migraine with brainstem (basilar-type) aura due to theoretical vasoconstrictive risk in the posterior circulation. This should be treated as a priority safety question pending formal label review, not as a resolved issue.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is not supported by disease-specific clinical evidence, and the underlying pharmacology raises a recognized safety concern (relative contraindication of triptans in brainstem-aura migraine) that current data cannot resolve. Formal TFDA safety labeling data is also blocked (DG001), preventing even an initial (S1) safety screen.

**To proceed, the following is needed:**
- TFDA/international package insert warnings and contraindications specific to zolmitriptan (resolve DG001)
- Confirmed formal mechanism-of-action documentation from DrugBank (resolve DG002)
- Any case series, pharmacovigilance data, or controlled studies specifically evaluating triptan safety in migraine with brainstem aura
- Expert neurology/headache-specialist review of the vasoconstriction risk-benefit before any further advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

