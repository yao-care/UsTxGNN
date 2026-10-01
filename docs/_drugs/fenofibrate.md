---
layout: default
title: Fenofibrate
parent: Moderate Evidence (L3-L4)
nav_order: 699
evidence_level: L4
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Fenofibrate: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate lipid-lowering drug, used mainly for high triglycerides and mixed dyslipidemia.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, but the direct support is weak: **1 clinical trial** (which does not test fenofibrate) and **11 publications**, mostly reviews and small, old studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license data. Literature in the pack describes use in hypertriglyceridemia and mixed dyslipidemia |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fenofibrate activates PPARα. This increases lipoprotein lipase activity and fatty-acid oxidation and reduces hepatic VLDL production. The result is lower triglycerides and higher HDL. Detailed DrugBank mechanism data were not available in the pack, so this description comes from the pack's mechanistic rationale.

The link to HoFH is weak. HoFH is caused by severely impaired LDL-receptor function. Fenofibrate's LDL-C lowering depends largely on LDL-receptor-mediated clearance, so little effect is expected. A 1984 study of patients with type II hyperlipoproteinemia included one HoFH patient with a marked fall in cholesterol, but that is a single case in an uncontrolled study.

The very high TxGNN score is therefore not backed by a plausible mechanism or by direct clinical evidence. Standard care for HoFH relies on statins, ezetimibe, PCSK9-pathway agents, lomitapide and LDL apheresis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (a PCSK9 inhibitor) in children and adolescents aged 8–17 with HoFH, measuring LDL-C at Week 12. **Fenofibrate is not part of this trial**, so it gives no direct evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Clinical study | Pharmacol Res Commun | 22 patients with type II hyperlipoproteinemia took fenofibrate 300 mg/day for 4–12 months. Total cholesterol fell 22% and LDL-C 24%; in familial hypercholesterolemia, 28% and 31%. One HoFH patient showed the greatest fall |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review / case report | Intern Med J | First Australian adult with HoFH to receive a liver transplant, because standard drugs and apheresis were not sufficient |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical options for dyslipidemic children, mostly FH. Fenofibrate is among the agents that reduced lipids |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines on dyslipidemia management and cardiovascular prevention |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin drugs. The clearest indication for fenofibrate monotherapy is fasting triglycerides >500 mg/dL, to reduce pancreatitis risk |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atheroscler Rep | Lipid disorders and dyslipidemia management in pregnancy |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Lomitapide (approved for HoFH) showed pharmacokinetic interactions with several lipid drugs, including fenofibrate |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe as a cholesterol absorption inhibitor. Background on non-fenofibrate options |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart J | LDL-C lowering with statins and PCSK9 inhibitors in severe hypercholesterolemia |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and use in hyperlipidemia. Background only |

## US Market Information

The US license data do not include approved-indication text, so that column is omitted. The 5 main authorizations are listed below (20 in total).

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076509 | FENOFIBRATE | Tablet | Amneal Pharmaceuticals of New York LLC |
| ANDA209660 | Fenofibrate | Tablet, film coated | Alembic Pharmaceuticals Inc. |
| ANDA210670 | Fenofibrate | Tablet, film coated | Bryant Ranch Prepack |
| NDA021695 | ANTARA | Capsule | Lupin Pharmaceuticals, Inc. |
| ANDA202856 | Fenofibrate | Tablet, film coated | Mylan Pharmaceuticals Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for HoFH is very high (99.91%), but no fenofibrate trial exists in this population. The only listed trial tests alirocumab, the mechanism is not plausible given the LDL-receptor defect, and existing options are far stronger. Evidence is at L4.

For context, the pack's second-ranked prediction, hyperlipoproteinemia (mixed dyslipidemia), has L1 evidence and a "Proceed with Guardrails" recommendation. It is close to fenofibrate's existing use, so it is not a true repurposing.

**To proceed, the following is needed:**
- HoFH-specific data on fenofibrate, for example LDL-receptor-negative versus defective patients, or add-on use to standard therapy
- Package insert warnings and contraindications (a blocking gap for safety screening)
- DrugBank mechanism-of-action data
- A safety plan for children and pregnancy, which are relevant HoFH populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

