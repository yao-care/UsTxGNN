---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fluvastatin: From Lipid Lowering (Original Indication Not Recorded) to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is an HMG-CoA reductase inhibitor (statin) that is already marketed in the US as oral capsules and extended-release tablets. The TxGNN model predicts it may be effective for **hyperlipoproteinemia**. The supplied evidence includes **5 registered clinical trials** and **20 publications**, but none of the trials tests fluvastatin directly. This is most likely an on-label lipid-lowering use rather than true repurposing, and it needs label verification.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the approved indication text is empty in all listed licenses) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (as assigned in the Evidence Pack; see the caveat under Clinical Trial Evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 13 licenses (NDA and ANDA combined) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank. Based on the Evidence Pack's mechanistic analysis, fluvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis and upregulates LDL receptors. This is the drug's established lipid-lowering mechanism.

Hyperlipoproteinemia is a disorder of elevated blood lipoproteins, and lowering LDL cholesterol is the core effect of statins. The mechanistic fit is therefore strong. The pack also flags that this is very likely an approved on-label use, not a new indication. The label should be checked before the prediction is treated as repurposing.

The evidence for direct fluvastatin efficacy comes from published clinical studies. These include the extended-release vs immediate-release comparison and combinations with fibrates or bezafibrate. No registered fluvastatin-specific Phase 2/3 trial appears in the list, so L1 is not assigned.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | N/A | Completed | 3270 | Surveillance of several marketed statins (including fluvastatin) in hyperlipidemia; class-level support only, and fluvastatin's inclusion is not confirmed |
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Phase 3 | Terminated | 411 | Lapaquistat acetate added to statins in hypercholesterolemia; does not test fluvastatin |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | Completed | 81 | Evolocumab (PCSK9 inhibitor) pilot for lipid management in renal transplant recipients; different drug and population |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in children and adolescents with homozygous FH; does not test fluvastatin |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | N/A | Completed | 55 | Erythrocyte-bound apoB after statin withdrawal; biomarker focus, not fluvastatin efficacy |

**Caveat:** None of these trials tests fluvastatin for this indication. The L2 rating rests on published clinical studies, not on registered fluvastatin trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clin Ther | Extended-release (80 mg once daily) vs immediate-release fluvastatin in primary hypercholesterolemia |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clin Ther | 12-month double-blind comparison of fluvastatin + fenofibrate vs fluvastatin alone in combined hyperlipidemia with type 2 diabetes and CHD |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT | Atherosclerosis | FACT study: fluvastatin, bezafibrate and their combination in 333 patients with coronary disease and mixed hyperlipidaemia |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Clinical trial | Eur J Clin Pharmacol | Double-blind study of high-dose fluvastatin in 52 patients with familial hypercholesterolaemia |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | Clinical trial | Acta Paediatr | Fluvastatin in children and adolescents with heterozygous FH, assessing lipid profile and vascular changes |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Clinical study | Ter Arkh | Simvastatin vs fluvastatin in primary hyperlipoproteinemia, examining lipoprotein metabolic parameters |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Clinical study | Am J Cardiol | Effects of fluvastatin on lipid profile and apolipoproteins in 31 Chinese patients with hypercholesterolemia |
| [24944371](https://pubmed.ncbi.nlm.nih.gov/24944371/) | 2003 | Clinical study | Curr Ther Res | 24-week open-label dose-increasing study of effects on LDL subfractions, oxidized LDL and adhesion molecules |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | Clinical study | Thromb Res | Fluvastatin 40 mg for 8 weeks in 20 hypercholesterolemic patients (type IIa/IIb), with tissue factor pathway inhibitor measured |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | Review article on fluvastatin (no abstract available) |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021192 | Lescol (Sandoz Inc) | Tablet, extended release | Not provided in source data |
| ANDA078407 | Fluvastatin (Teva Pharmaceuticals USA) | Capsule | Not provided in source data |
| ANDA090595 | Fluvastatin Sodium (Mylan Pharmaceuticals) | Capsule | Not provided in source data |
| ANDA079011 | Fluvastatin Sodium (Teva Pharmaceuticals USA) | Tablet, film coated, extended release | Not provided in source data |
| ANDA078407 | Fluvastatin (Bryant Ranch Prepack) | Capsule | Not provided in source data |

All listed products are oral.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism (HMG-CoA reductase inhibition and LDL receptor upregulation) fits hyperlipoproteinemia well, and published clinical studies, including randomized trials, support fluvastatin's lipid-lowering effect. However, no registered trial directly tests fluvastatin for this indication, and the use is likely already on-label. It should be treated as label confirmation, not as a new indication.

**To proceed, the following is needed:**
- Download and parse the FDA package insert to confirm the approved indications, warnings and contraindications
- Confirm the mechanism of action through DrugBank
- Verify that the published studies (many classified only from titles) match the predicted indication
- Monitor hepatic and muscle safety, and consider combination therapy where a lower-potency statin is insufficient
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

