---
layout: default
title: Pitavastatin
parent: 僅模型預測 (L5)
nav_order: 1051
evidence_level: L5
indication_count: 10
---

# Pitavastatin
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

# Pitavastatin: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pitavastatin is an HMG-CoA reductase inhibitor (statin) with an established global role in treating dyslipidemia and cardiovascular risk reduction, though it currently holds no marketing authorization in this jurisdiction.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
but this specific indication is currently supported by only **0 clinical trials** and **2 publications**, both indirect. Much stronger evidence exists for closely related entities in the same hypercholesterolemia spectrum (e.g., familial hypercholesterolemia, hyperlipoproteinemia), which likely reflects the true weight of the underlying pharmacology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing license on record in this jurisdiction (drug not currently marketed) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L3 (indirect RCT + case report; no trials registered specifically for this indication) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on known pharmacology, pitavastatin is an HMG-CoA reductase inhibitor of the statin class. Its lipid-lowering efficacy has been established across multiple dyslipidemia settings — for example, the INTREPID trial (Aberg et al., 2017) demonstrated efficacy versus pravastatin in adults with HIV-associated dyslipidemia, and the large REPRIEVE trial (Grinspoon et al., 2023, NEJM) confirmed cardiovascular risk reduction with pitavastatin in a general at-risk population. Mechanistically, this potent LDL-C-lowering effect is directly relevant to HoFH, an extreme genetic form of LDL receptor dysfunction that requires aggressive LDL-C reduction.

It is worth noting that within this same evidence pack, several other TxGNN-predicted indications — hyperlipoproteinemia (rank 2, L1 evidence, multiple completed Phase 3/4 RCTs), familial hypercholesterolemia (rank 3, extensive pediatric and adult literature including dedicated Japan/Europe trials), and autosomal dominant hypercholesterolemia (rank 5, L2 evidence) — represent the same underlying disease spectrum as HoFH. This convergence across ranks suggests the model is correctly identifying pitavastatin's core statin pharmacology as broadly applicable to genetically defined hypercholesterolemia, even though direct trial evidence specifically labeled "HoFH" remains sparse. In several pediatric FH studies (e.g., Harada-Shiba et al. 2016, 2018; Nishioka et al. 2025), pitavastatin has already been used successfully in severe heterozygous and combination-therapy contexts, supporting biological plausibility for the homozygous form as well.

## Clinical Trial Evidence

Currently no related clinical trials registered specifically under "Homozygous Familial Hypercholesterolemia."

*(For context, the closely related entity "familial hypercholesterolemia" (rank 3) and "hyperlipoproteinemia" (rank 2) have multiple completed Phase 3/4 RCTs directly evaluating pitavastatin — see rationale above.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Phase 4) | The Lancet HIV | INTREPID trial: pitavastatin vs pravastatin in HIV-1-infected adults with dyslipidaemia; both statins avoid CYP450-mediated drug interactions, relevant to lipid-lowering strategy design in high-risk populations. |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Case Report | Journal of Clinical Lipidology | Two cases of autosomal recessive hypercholesterolemia (ARH), a condition clinically indistinguishable from HoFH, showing rapid lipid-lowering response — supports statin applicability in HoFH-like phenotypes. |

## US Market Information

No marketing authorization records are currently available for this jurisdiction — `total_licenses` is 0 and the drug's market status is recorded as "Not Marketed." A regulatory filing/license review would be required before any local marketing pathway can be assessed.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — see data gap DG001, flagged as Blocking.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap exists (DG001 — missing local regulatory warnings/contraindications), which prevents entry into the S1 safety evaluation stage. In addition, the top-ranked indication (HoFH) itself has no directly registered trials and only two indirect literature references, so the strongest supporting evidence in this pack actually clusters around adjacent indications (familial hypercholesterolemia, hyperlipoproteinemia) rather than HoFH specifically.

**To proceed, the following is needed:**
- Obtain official label/warning and contraindication data (DG001) to complete S1 safety screening
- Obtain confirmed mechanism-of-action documentation (DG002) via DrugBank API
- Clarify local regulatory pathway, given the drug currently holds no marketing authorization in this jurisdiction
- Consider prioritizing "familial hypercholesterolemia" (rank 3) or "hyperlipoproteinemia" (rank 2) as the lead repurposing candidate given their substantially stronger direct trial evidence, using HoFH as a genetically-related extension indication rather than the primary claim
- Complete DDI dataset (currently `not_found`, 0 interactions recorded)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

