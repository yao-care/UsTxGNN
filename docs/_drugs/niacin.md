---
layout: default
title: Niacin
parent: 僅模型預測 (L5)
nav_order: 963
evidence_level: L5
indication_count: 1
---

# Niacin
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

# Niacin: From Unmarketed Status to Predicted Use in Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Niacin (Vitamin B3, DrugBank DB00627) currently holds **no market authorization in Taiwan**, so no TFDA-approved indication text is on file for this candidate.
> The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, with a **99.74%** prediction score, though the supporting evidence base of **2 clinical trials** and **20 publications** consists mostly of disease-context studies rather than niacin-specific HoFH trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Niacin has no Taiwan market authorization on file (0 licenses); no approved indication text exists to extract |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.74% (rank 6966) |
| Evidence Level | L4 (see caveat below) |
| Market Status | 未上市 (Not marketed in Taiwan) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (MOA: [Data Gap], flagged as High-severity gap DG002). Based on general pharmacological knowledge, niacin is a B-vitamin that at pharmacologic doses inhibits hepatic diacylglycerol acyltransferase-2 and reduces VLDL/LDL secretion while raising HDL — a mechanism historically applied to primary hypercholesterolemia and mixed dyslipidemia.

HoFH is a severe genetic disorder (LDLR/APOB/PCSK9 mutations) causing markedly elevated LDL-C from birth, typically managed with combination lipid-lowering therapy plus apheresis. Since niacin's core pharmacology targets the same LDL/VLDL pathway, a mechanistic rationale for its use as an *adjunct* in HoFH combination regimens is plausible — several of the retrieved reviews (e.g., PMID 26376908, 24506448) discuss niacin alongside statins, ezetimibe, and PCSK9 inhibitors as part of the broader non-statin/nonstatin-adjunct armamentarium for severe hypercholesterolemia, including HoFH.

**Caveat:** Neither of the two retrieved clinical trials tests niacin directly — NCT03110432 is a German dyslipidemia registry, and NCT03510715 evaluates alirocumab (a PCSK9 inhibitor) in pediatric HoFH. The literature similarly discusses niacin mostly as one agent within broader lipid-lowering treatment reviews, not as a dedicated HoFH intervention. This is disease-context evidence, not direct niacin-in-HoFH trial evidence — the score should be read as a strong knowledge-graph mechanistic signal rather than confirmed clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03110432](https://clinicaltrials.gov/study/NCT03110432) | N/A | Completed | 1,695 | German registry of very-high-cardiovascular-risk dyslipidemia patients meeting G-BA criteria for PCSK9i use, treated by cardiologists/lipid clinics. Does not test niacin directly. |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab in children/adolescents (8–17y) with HoFH; evaluated LDL-C reduction at Week 12/24/48 on top of background therapy. Does not test niacin directly. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Overview of FH genetics, diagnosis, and current treatment options |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Diagnostic/treatment challenges specific to HoFH, including LDL-C burden from birth |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern management of both HoFH and HeFH, focused on LDL receptor defects |
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Review | Expert Rev Cardiovasc Ther | Critical review of non-statin lipid therapies including niacin, for statin-intolerant/severe dyslipidemia |
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Review/Statement | Arterioscler Thromb Vasc Biol | ATVB Council statement: RCTs show bile acid sequestrants, **niacin**, and fibrates each reduce CVD endpoints as monotherapy |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atherosclerosis Suppl | Unmet needs in HoFH management despite apheresis and lipid-lowering drugs |
| [19947811](https://pubmed.ncbi.nlm.nih.gov/19947811/) | 2009 | Case Report | Pharmacotherapy | Case of tuberous/tendinous xanthomas in an 18-year-old with HoFH |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Efficacy/safety review of atorvastatin in primary hypercholesterolemia and mixed dyslipidemias |
| [3548303](https://pubmed.ncbi.nlm.nih.gov/3548303/) | 1987 | Case Series | Am J Cardiol | Liver transplantation vs. medication/plasma exchange for HoFH-related cardiovascular disease |
| [7040850](https://pubmed.ncbi.nlm.nih.gov/7040850/) | 1982 | Review | Med Clin North Am | Drug therapy for hypercholesterolemia, including combined regimens and homozygous forms |

---

## US Market Information

Niacin currently holds no market authorization record in this dataset — `total_licenses` is 0 and the `licenses` array is empty. No product/dosage-form table can be generated until TFDA license data (DG001) is obtained.

---

## Safety Considerations

Please refer to the package insert for safety information — key warnings, contraindications, and drug-drug interaction data are all currently unavailable (flagged as Blocking data gap DG001: TFDA label warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
DG001 (TFDA label warnings/contraindications) is a **Blocking** gap that prevents this candidate from entering the S1 safety pre-screen at all, regardless of the promising 99.74% TxGNN score. In addition, the retrieved clinical trials do not test niacin directly in HoFH, so the current evidence base supports the mechanistic plausibility of the prediction more than clinical proof.

**To proceed, the following is needed:**
- TFDA label PDF (warnings/contraindications) to clear the Blocking gap and enable S1 safety evaluation
- Confirmed mechanism of action (MOA) data from DrugBank to support the mechanistic rationale
- DDI data (current query returned `not_found`)
- Ideally, trials or literature evaluating niacin specifically as an adjunct therapy in HoFH patients, rather than general dyslipidemia/HoFH-context studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

