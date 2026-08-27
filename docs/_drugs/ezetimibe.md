---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 690
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor globally used to treat hypercholesterolemia and mixed dyslipidemia, though it is not currently registered or marketed in Taiwan.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia**,
with **50 clinical trials** and **19 publications** currently supporting this direction — though this largely reflects an extension of ezetimibe's already-established lipid-lowering use rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / mixed dyslipidemia (globally approved use; no Taiwan-specific license record in this dataset) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| US Market Status | Not Marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is flagged as a data gap in this evidence pack. Based on well-established pharmacology, however, ezetimibe selectively inhibits the intestinal Niemann-Pick C1-Like 1 (NPC1L1) transporter, blocking absorption of dietary and biliary cholesterol at the brush border of the small intestine. This reduces delivery of cholesterol to the liver, upregulates LDL receptor expression, and lowers circulating LDL cholesterol (LDL-C) — an effect that is additive when combined with a statin.

Hyperlipoproteinemia is a broad classification of lipid disorders characterized by elevated lipoprotein/LDL-C levels, and it already encompasses conditions (such as hypercholesterolemia and familial hypercholesterolemia) for which ezetimibe's efficacy is firmly established. As the evidence pack's own repurposing rationale notes, this prediction reflects "the same mechanism as in familial hypercholesterolemia (NPC1L1 inhibition → reduced intestinal cholesterol absorption → lowered LDL-C)" and represents an existing pharmacological extension rather than a truly novel indication.

Because NPC1L1 inhibition acts directly on the lipid-handling pathway underlying hyperlipoproteinemia, the mechanistic rationale is strong, and this is corroborated by an extensive body of completed Phase 3 trials evaluating ezetimibe (alone or in fixed-dose combinations) across related hypercholesterolemia/dyslipidemia populations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe + atorvastatin/simvastatin in homozygous familial hypercholesterolemia; efficacy/safety confirmed |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration effective and safe in mixed hyperlipidemia |
| [NCT00701883](https://clinicaltrials.gov/study/NCT00701883) | Phase 2 | Completed | 183 | Placebo/active-controlled study of MBX-8025 ± atorvastatin in hyperlipidemic patients; supportive comparator data |
| [NCT04929249](https://clinicaltrials.gov/study/NCT04929249) | Phase 3 | Completed | 450 | "Inclisiran-first" strategy vs usual care in ASCVD with elevated LDL-C; ezetimibe part of background therapy |
| [NCT00652431](https://clinicaltrials.gov/study/NCT00652431) | Phase 1 | Completed | 18 | PK interaction study of Vytorin (ezetimibe/simvastatin) with niacin extended-release |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Completed | 511 | Evolocumab vs ezetimibe in statin-intolerant hypercholesterolemic patients |
| [NCT03337308](https://clinicaltrials.gov/study/NCT03337308) | Phase 3 | Completed | 382 | Bempedoic acid + ezetimibe fixed-dose combination effective/safe vs components and placebo on maximal statin therapy |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib + ezetimibe FDC evaluated in HeFH/ASCVD patients on maximal lipid-lowering therapy |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in HeFH |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate coadministration in mixed hyperlipidemia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT (TANDEM) | Lancet | Fixed-dose obicetrapib + ezetimibe combination significantly reduces LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide evaluated against standard lipid-lowering background including ezetimibe in HeFH |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Pathophysiology, diagnosis, and treatment of postprandial hyperlipidemia |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Current drug classes targeting hyperlipidemia, including cholesterol absorption inhibitors |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors as add-on to statin/ezetimibe therapy |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nat Rev Dis Primers | Comprehensive primer on familial hypercholesterolaemia pathophysiology and management |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Curr Cardiol Rep | Global burden and management approaches for familial hypercholesterolemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C/ApoB-lowering therapies, positioning ezetimibe among current options |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consensus Statement | Eur Heart J | EAS consensus on underdiagnosis/undertreatment of FH and screening/treatment guidance |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | Overview of familial hypercholesterolemia treatments including statins, ezetimibe, and LDL apheresis |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is supported by an extensive body of completed Phase 3 evidence (L1), but this largely reflects ezetimibe's already-established global lipid-lowering use rather than a novel mechanism-based hypothesis. Since the drug is not currently registered or marketed in Taiwan, and TFDA label warnings/contraindications and formal MOA documentation are marked as data gaps (one of them Blocking severity), the drug cannot yet clear a full safety pre-assessment (S1).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — download and parse from the TFDA website (Blocking gap)
- Confirmed mechanism of action documentation via DrugBank API (High-priority gap)
- Taiwan registration/import status verification, since the drug is currently unmarketed locally
- Drug-drug interaction (DDI) data, currently returning "not found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

