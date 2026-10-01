---
layout: default
title: Niacin
parent: Moderate Evidence (L3-L4)
nav_order: 963
evidence_level: L4
indication_count: 1
---

# Niacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Niacin: From Lipid Modification to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Niacin is an established lipid-modifying agent, though the supplied data lists no approved indication text.
The TxGNN model predicts it may be useful for **homozygous familial hypercholesterolemia (HoFH)**.
Evidence is thin: **2 clinical trials** and **20 publications** were retrieved, but none shows niacin's efficacy in HoFH.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed (all US license records have empty indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed oral tablets are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Niacin lowers LDL-C, triglycerides and Lp(a) and raises HDL-C. It is thought to work by reducing hepatic VLDL/apoB production, through DGAT2 inhibition and the GPR109A receptor. Formal mechanism-of-action data is not available in the Evidence Pack, so this description comes from general lipid pharmacology.

HoFH is caused mainly by LDL-receptor deficiency. A mechanism that reduces apoB-containing lipoprotein production does not depend on receptor function, so niacin could plausibly serve as an add-on lipid-lowering agent in HoFH.

However, this link is inferred, not shown in HoFH patients:
- The TxGNN score is a model prediction only.
- The retrieved literature is mostly disease-level review material that mentions niacin at most as a non-statin option.
- Large outcome trials of niacin in general dyslipidemia populations, which are not among the supplied records, did not show added cardiovascular benefit.
- Niacin has tolerability limits, including flushing and hepatic and glycemic effects.

## Clinical Trial Evidence

Neither trial tests niacin, and both were graded C (low relevance).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor) in children and adolescents with HoFH. Matches the disease but not the drug, so it only shows the current HoFH treatment landscape. |
| [NCT03110432](https://clinicaltrials.gov/study/NCT03110432) | N/A | Completed | 1695 | German registry of very-high-cardiovascular-risk dyslipidemia patients eligible for PCSK9 inhibitors. Not HoFH-specific and no niacin exposure indicated. |

## Literature Evidence

None of these publications reports niacin efficacy in HoFH.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Review | Expert Rev Cardiovasc Ther | Critical review of non-statin options (fibrates, ezetimibe, bile acid sequestrants, n-3 fatty acids, niacin) for residual risk and statin intolerance. |
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Scientific statement | Arterioscler Thromb Vasc Biol | ATVB Council statement on non-statin LDL-lowering therapy. Notes that niacin monotherapy reduced CVD endpoints in placebo-controlled trials. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK interaction study | Pharmacotherapy | Studied lomitapide's pharmacokinetic interactions with lipid-lowering drugs, including niacin, in the HoFH treatment setting. |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Challenges in diagnosing and treating HoFH, a disease with severely elevated LDL-C and early cardiovascular risk. |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atheroscler Suppl | What current HoFH care (apheresis and lipid-lowering drugs) achieves, and the unmet needs. |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern management of familial hypercholesterolemia, covering both HoFH and heterozygous forms. |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | Review | Nat Rev Cardiol | Lipid-modifying pharmacotherapies beyond statins for severe hypercholesterolemia and mixed dyslipidemia. |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Literature analysis of familial hypercholesterolemia diagnostics and treatment options. |
| [23074505](https://pubmed.ncbi.nlm.nih.gov/23074505/) | 2007 | Health technology assessment | Ont Health Technol Assess Ser | Evidence-based analysis of LDL apheresis for refractory homozygous and heterozygous FH. |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | Clinical study | Arteriosclerosis | Drug regimens in children and adolescents with FH (30 heterozygous, 3 homozygous). |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA203899 | Niacin (Golden State Medical Supply) | Tablet, extended release | Not listed |
| ANDA203578 | Niacin (Amneal Pharmaceuticals) | Tablet, extended release | Not listed |
| ANDA204934 | Niacin (Macleods Pharmaceuticals) | Tablet | Not listed |
| Not listed | THE SKIN HOUSE Vital Bright EyeCream (cosmetic) | Cream | Not listed |
| Not listed | DERLADIE LABORATOIRE PORE TIGHTENING AMPOULE (cosmetic) | Liquid | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a plausible but inferred mechanism. The retrieved trials and publications contain no niacin-specific efficacy or safety data in HoFH. Niacin's tolerability limits and the lack of added cardiovascular benefit in general dyslipidemia outcome trials also argue against advancing now.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap), to allow safety screening
- Mechanism-of-action data from DrugBank and the approved indication text
- Niacin-specific HoFH evidence, such as case series, small trials, or use as an add-on to statins, ezetimibe, or PCSK9 inhibitors
- Comparison against current HoFH standards of care (PCSK9 inhibitors, lomitapide, LDL apheresis) to define any remaining role for niacin

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

